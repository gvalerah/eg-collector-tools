# ======================================================================
# View for Fast Calculation of Period Usage up to now
# (c) Sertechno 2021
# GLVH @ 2021-12-04 Initial version
# ======================================================================

from pprint                         import pformat
from emtec.collector.forms          import frm_charging_resume
from babel.numbers                  import format_number
from babel.numbers                  import format_decimal
from babel.numbers                  import format_percent
from emtec.collector.db.orm_model   import Configuration_Items
import simplejson as json

# ======================================================================


@main.route('/report/Period_Usage', methods=['GET','POST'])
@login_required
def report_Period_Usage():
    logger.debug(f'{this()}: Enter')    
    collectordata=get_collectordata()
    
    db.session.flush()
    db.session.commit()
        
    Cus_Id          =  current_user.cost_center.Cus_Id
    Rates           = {}
    
    parser = configparser.ConfigParser(
            allow_no_value=False,     # don't allow "key" without "="
            delimiters=('=',),        # inifile "=" between key and value
            comment_prefixes=(';','#'),  # only ';' for comments (fixes #channel)
            inline_comment_prefixes=(';'),     # comments after lines
            interpolation=configparser.ExtendedInterpolation(),
            empty_lines_in_values=False  # empty line means new key
            )
    parser.read(current_app.config.get('COLLECTOR_CONFIG_FILE'))
    # Read Configuration
    Rates = {}
    # Reads Rates from configuration file
    for option in parser.options('Rates'):
        values = parser.get('Rates',option).split(',')
        logger.debug(f"values={values}")
        if len(values)>1:
            rate,measure_unit,period,is_allways_billeable = values
        else:
            rate = values[0]
        Rates.update({
            option:{
                'rate'                : round(float(rate),12),
                'measure_unit'        : str(measure_unit).strip().upper(),
                'period'              : str(period).strip().upper(),
                'is-allways_billeable': True if str(is_allways_billeable).upper() in ['TRUE','VERDADERO','SI','T','V','S'] else False
            }
        })
    # set shardened Charge Items Table as per active period
    Charge_Items.set_shard(collectordata['COLLECTOR_PERIOD']['active'])  
    # BETA Message, to be removed --------------------------------------
    flash('Beta version. Query in development. Results are referential only','error')
    # BETA Message, to be removed --------------------------------------
    usage = db.Get_Period_Usage(customer_id=Cus_Id,rates=Rates)
    pprint(usage)
    # Updated cached data for this specific query if requested 
    try:
        temp_folder   = "/tmp"
        temp_filename = f"{temp_folder}/{next(tempfile._get_candidate_names())}.json"
        with open(temp_filename,"w") as fp:
            fp.write(json.dumps(usage))
        return render_template('report_period_usage.html',data=usage,collectordata=collectordata,temp_filename=temp_filename)
    except Exception as e:
        return f"{this()}: Exception:  {str(e)}"
        
@main.route('/download/Period_Usage', methods=['GET','POST'])
@login_required
def download_Period_Usage():
    logger.debug(f'{this()}: Enter')    
    collectordata=get_collectordata()
    
    db.session.flush()
    db.session.commit()
    
    temp_filename   =  request.args.get('temp_filename',None,type=str)
    if not temp_filename:
        return "Invalid data"

    with open(temp_filename,'r') as fp:
        data = json.load(fp)
    
    if data is None:
        return "Invalid data"
        
    
    d = {
        'detail':[],
        'rows':0
    }
    # Build list of records to export from query
    for Component_Type in ['CPU','RAM']:
        for Power_Status in ['0','1']:
            try:
                row = data[Component_Type][Power_Status]
                d['detail'].append({
                        'type'      :Component_Type,
                        'power'     :'ON' if Power_Status=='1' else 'OFF',
                        'hours'     :row.get('hours',0),
                        'Q_hours'   :row.get('Q_hours',0),
                        'Q_month'   :row.get('Q_month',0),
                        'rate'      :row.get('rate',0),
                        'rtmf'      :row.get('rtmf',0),
                        'rate_month':row.get('rate_month',0),
                        'bill'      :row.get('bill',0),
                })
            except Exception as e:
                print(f"Exception: str({e})")
    for Component_Type in ['DSK','SNP','DRP','IMG']:
        for Power_Status in ['0','1']:
            try:
                row = data[Component_Type][Power_Status]
                d['detail'].append({
                        'type'      :Component_Type,
                        'power'     :'ON' if Power_Status=='1' else 'OFF',
                        'hours'     :row.get('hours',0),
                        'Q_hours'   :row.get('Q_hours',0),
                        'Q_month'   :row.get('Q_month',0),
                        'rate'      :0,
                        'rtmf'      :0,
                        'rate_month':0,
                        'bill'      :0,
                })
                for Disk_Type in ['HDD','SSD']:
                    rox = row[Disk_Type]
                    d['detail'].append({
                            'type'      :f"{Component_Type}-{Disk_Type}",
                            'power'     :'ON' if Power_Status=='1' else 'OFF',
                            'hours'     :0,
                            'Q_hours'   :0,
                            'Q_month'   :rox.get('Q_month',0),
                            'rate'      :rox.get('rate',0),
                            'rtmf'      :row.get('rtmf',0),
                            'rate_month':rox.get('rate_month',0),
                            'bill'      :rox.get('bill',0),
                    })
            except Exception as e:
                print(f"Exception: str({e})")
                    
    # List of fields in desired order 
    headers=[
                'type',
                'power',
                'hours',
                'Q_hours',
                'Q_month',
                'rate',
                'rtmf',
                'rate_month',
                'bill',
    ]
    # Normalize data into a Pandas Dataframe
    df1 = json_normalize(d, 'detail')
    # Reorder columns
    df1 = df1.reindex(columns=headers)
    # create temporary filename       
    temp_name   = f"{ next(tempfile._get_candidate_names()) }.xlsx"
    #print(f"temp_name={temp_name}")
    
    xlsx_file="%s/%s"%(current_app.root_path,url_for('static',filename='tmp/%s'%(temp_name)))
    #print(f"df1={df1}")
    #print(f"xlsx_file={xlsx_file}")
    df1.to_excel(xlsx_file,f"Usage {data.get('period')}")
    
    return send_file(xlsx_file,as_attachment=True,attachment_filename=temp_name)
