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

# ======================================================================

import simplejson as json

@main.route('/report/Period_Usage', methods=['GET','POST'])
@login_required
def report_Period_Usage():
    logger.debug(f'{this()}: Enter')    
    collectordata=get_collectordata()
    #print(f"collectordata={collectordata}")
    
    db.session.flush()
    db.session.commit()
    
    Cus_Id          =  3
    Rates           = {}
    """
    cfg = config[os.getenv('COLLECTOR_CONFIG') or 'default']
    logger.debug(f"cfg={cfg}")
    logger.debug(f"cfg type={type(cfg)}")
    logger.debug(f"cfg dir={dir(cfg)}")
    logger.debug(f"COLLECTOR_CONFIG_FILE={cfg.COLLECTOR_CONFIG_FILE}")
    """
    parser = configparser.ConfigParser(
            allow_no_value=False,     # don't allow "key" without "="
            delimiters=('=',),        # inifile "=" between key and value
            comment_prefixes=(';','#'),  # only ';' for comments (fixes #channel)
            inline_comment_prefixes=(';'),     # comments after lines
            interpolation=configparser.ExtendedInterpolation(),
            empty_lines_in_values=False  # empty line means new key
            )
    #arser.read(cfg.COLLECTOR_CONFIG_FILE)
    parser.read(current_app.config.get('COLLECTOR_CONFIG_FILE'))
    # Read Configuration
    # Rates
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

    # Updated cached data for this specific query if requested 
    try:
        return render_template('report_period_usage.html',data=usage,collectordata=collectordata)
    except Exception as e:
        return f"{this()}: Exception:  {str(e)}"
        
@main.route('/download/Period_Usage', methods=['GET','POST'])
@login_required
def download_Period_Usage():
    logger.debug(f'{this()}: Enter')    
    collectordata=get_collectordata()
    
    db.session.flush()
    db.session.commit()
    
    Cus_Id          =  request.args.get('Cus_Id',None,type=int)
    Cus_Name        =  request.args.get('Cus_Name',None,type=str)
    CIT_Date_From   =  request.args.get('CIT_Date_From',None,type=str)
    CIT_Date_To     =  request.args.get('CIT_Date_To',None,type=str)
    CIT_Status      =  request.args.get('CIT_Status',None,type=int)
    CIT_Status_Value=  request.args.get('CIT_Status_Value',None,type=str)
    Cur_Code        =  request.args.get('Cur_Code',None,type=str)
    Cur_Name        =  request.args.get('Cur_Name',None,type=str)
    Update          =  request.args.get('Update',0,type=int)
    FILTER          =  request.args.get('filter_type',0,type=int)
    CODE            =  request.args.get('filter_code',None)
        
    print(f"**********************************************************")
    print(f"{this()}: FILTER={FILTER} CODE={CODE} {type(CODE)}")
    print(f"**********************************************************")
    CODE=int(CODE)
    # Get Actual Remume Data from Database
    # NOTE: Here needs some Sand-Clock Message or something in case it takes so long ...
    # Gets Charge Resume from DB
    logger.debug(f"**********************************************************")
    logger.debug(f"{this()}: FILTER={FILTER} CODE={CODE} {type(CODE)}")
    logger.debug(f"{this()}: FROM={CIT_Date_From} TO={CIT_Date_To} ST:{CIT_Status} CUR:{Cur_Code}")
    logger.debug(f"{this()}: User={current_user}")
    logger.debug(f"**********************************************************")
    
    rows = db.Get_Charge_Resume_Filter(
                FILTER,
                CODE,
                CIT_Date_From,
                CIT_Date_To,
                CIT_Status,
                Cur_Code,
                User_Id=current_user.id
                )
    if rows is not None:
        logger.debug(f"{this()}: {len(rows)} rows found to export ...")
    else:
        logger.error(f"{this()}: None rows found to export ...")
        
    temp_name   = next(tempfile._get_candidate_names())
    output_file = f"CR_{FILTER}_{CODE}_{CIT_Date_From}_{CIT_Date_To}_{CIT_Status}_{current_user.id}_{temp_name}.xlsx"
    
    d = {
        'detail':[],
        'Cus-Id':Cus_Id,
        'CIT_Date_From':CIT_Date_From,
        'CIT_Date_To':CIT_Date_To,
        'CIT_Status':CIT_Status,
        'Cur_Code':Cur_Code,
        'file':output_file,
        'rows':len(rows)
    }
    # Build list of records to export from query
    for row in rows:
        d['detail'].append({
                'ccCode':row.CC_Code,
                'ccDescription':row.CC_Description,
                'ciName':row.CI_Name,
                'cuDescription':row.CU_Description,
                'items':row.CIT_Count,
                'mu':row.Rat_MU_Code,
                'price':float(row.Rat_Price),
                'rateCurrency':row.Cur_Code,
                'ratePeriodDescription':row.Rat_Period_Description,
                'resumeQuantityAtRate':float(row.CR_Quantity_at_Rate),
                'totalAtCurrency':float(row.CR_ST_at_Rate_Cur),
                'from':row.CR_Date_From,
                'to':row.CR_Date_To,
        })
    # List of fields in desired order 
    headers=[
                'ccCode',
                'ccDescription',
                'ciName',
                'cuDescription',
                'items',
                'mu',
                'price',
                'rateCurrency',
                'ratePeriodDescription',
                'resumeQuantityAtRate',
                'totalAtCurrency',
                'from',
                'to',
    ]
    # Normalize data into a Pandas Dataframe
    df1 = json_normalize(d, 'detail')
    # Reorder columns
    df1 = df1.reindex(columns=headers)
    # create temporary filename       
    xlsx_file="%s/%s"%(current_app.root_path,url_for('static',filename='tmp/%s'%(output_file)))
    df1.to_excel(xlsx_file,'Sheet 1')
    return send_file(xlsx_file,as_attachment=True,attachment_filename=output_file)
