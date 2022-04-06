# ======================================================================
# View for Fast Calculation of Period Usage up to now
# (c) Sertechno 2021
# GLVH @ 2021-12-04 Initial version
# ======================================================================

import tempfile
import datetime
from pprint                         import pformat
from babel.numbers                  import format_number
from babel.numbers                  import format_decimal
from babel.numbers                  import format_percent
import simplejson as json
import configparser
from flask                          import flash
from flask                          import render_template
from flask                          import send_file
from pandas.io.json                 import json_normalize
from emtec.debug                    import *
from emtec.collector.forms          import frm_charging_resume
from emtec.collector.db.orm_model   import Customers
from emtec.collector.db.orm_model   import Configuration_Items
from emtec.collector.db.orm_model   import Charge_Items
# GV Internationalization code -----------------------------------------
from flask_babel import Babel, gettext, ngettext, lazy_gettext, force_locale

# ======================================================================

import os
import jinja2
from emtec.plugins import Plugin

template_main = """
"""

class Instance(Plugin):
    name      = 'aaaa_period_usage'
    version   = '1.0.1'
    templates = {'main':template_main}
    kwargs    = {}
    title     = 'Period Usage'
    short_description = 'Period Usage Report'
    long_description  = 'AAAA Period Usage Report'
    format = "html_body"

    def execute(self,data=None,**kwargs):
        # will render template here
        # sets up kwargs for expansion oportunities
        for kwarg in kwargs:
            setattr(self,kwarg,kwargs.get(kwarg))
        #self.details()
        # Initialize Instance variables

        result = self.report_Period_Usage()
            
        return result

    def report_Period_Usage(self):
        self.logger.debug(f'{this()}: Enter')    
        collectordata=self.application_data
        
        self.db.session.flush()
        self.db.session.commit()
            
        Cus_Id          =  self.user.cost_center.Cus_Id
        Rates           = {}
        
        parser = configparser.ConfigParser(
                allow_no_value=False,     # don't allow "key" without "="
                delimiters=('=',),        # inifile "=" between key and value
                comment_prefixes=(';','#'),  # only ';' for comments (fixes #channel)
                inline_comment_prefixes=(';'),     # comments after lines
                interpolation=configparser.ExtendedInterpolation(),
                empty_lines_in_values=False  # empty line means new key
                )
        parser.read(self.app.config.get('COLLECTOR_CONFIG_FILE'))
        # Read Configuration
        Rates = {}
        # Reads Rates from configuration file
        for option in parser.options('Rates'):
            values = parser.get('Rates',option).split(',')
            self.logger.debug(f"values={values}")
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
        suffix = f"{self.user.cost_center.Cus_Id}_{collectordata['COLLECTOR_PERIOD']['active']}"
        Charge_Items.set_shard(suffix,self.db.engine)  
        # GV BETA Message, to be removed --------------------------------------
        flash(gettext('Beta version. Query in development. Results are referential only'),'warning')
        # GV BETA Message, to be removed --------------------------------------
        usage = self.db.Get_Period_Usage(customer_id=Cus_Id,rates=Rates)
        # GV pprint(usage)
        # Updated cached data for this specific query if requested 
        dt = datetime.datetime.strptime(usage.get('period'),'%Y%m')
        usage.update({'period_month':f"{dt.strftime('%B').lower()}" })
        usage.update({'period_year':f"{dt.strftime('%Y')}"          })
        usage.update({'period_text':f"{dt.strftime('%B %Y')}"       })
        customer = self.db.session.query(Customers.Cus_Name
                    ).filter(Customers.Cus_Id==self.user.cost_center.Cus_Id
                    ).one_or_none()
        if customer is not None and len(customer):
            customer = customer[0]
        else:
            customer = ''
        usage.update({'customer':customer})
        try:
            temp_folder   = "/tmp"
            temp_filename = f"{temp_folder}/{next(tempfile._get_candidate_names())}.json"
            with open(temp_filename,"w") as fp:
                fp.write(json.dumps(usage))
            return render_template('report_period_usage.html',data=usage,collectordata=collectordata,temp_filename=temp_filename)
        except Exception as e:
            return f"{this()}: Exception:  {str(e)}"
            
    def download_Period_Usage(self):
        self.logger.debug(f'{this()}: Enter')    
        collectordata=self.application_data
        
        self.db.session.flush()
        self.db.session.commit()
        
        temp_filename   =  self.request.args.get('temp_filename',None,type=str)
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
        
        xlsx_file="%s/%s"%(app.root_path,url_for('static',filename='tmp/%s'%(temp_name)))
        #print(f"df1={df1}")
        #print(f"xlsx_file={xlsx_file}")
        df1.to_excel(xlsx_file,f"Usage {data.get('period')}")
        
        return send_file(xlsx_file,as_attachment=True,attachment_filename=temp_name)


