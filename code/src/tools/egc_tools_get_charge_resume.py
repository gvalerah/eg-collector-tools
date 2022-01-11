"""
Command Line Get Charge Resume
"""
import logging
import os
import argparse
from pprint import pprint,pformat
from    emtec                               import *
from    emtec.feedback                      import *
from    emtec.collector.db.orm              import *
from    sqlalchemy                          import create_engine

import  simplejson              as json
from sqlalchemy import tuple_
import jinja2
import configparser

# Minimum requirement to use db object ---------------------------------
from    flask                               import Flask
from    flask_sqlalchemy                    import SQLAlchemy
from    config                              import *
from    emtec                               import *
from    emtec.collector.db.orm              import *
db                                          = Collector_ORM_DB()


# Logging logics
# create logger
logger = logging.getLogger('egc_tools_get_charge_resume')
logger.setLevel(logging.WARNING)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.WARNING)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(levelname)8s - %(lineno)d - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

def create_app(config_name):
    app = Flask(__name__)
    logger.debug(f"{this()}: config_name         = {config_name}")
    logger.debug(f"{this()}: config[config_name] = {config[config_name]}")
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    # Inititializes applications (incomplete by now)
    logger.debug(f"{this()}: app                 = {app}")
    db.init_app             (app)
    logger.debug(f"{this()}: db                  = {db}")
    return app 
# ----------------------------------------------------------------------

# Here I can setup multiple Collector Tool Services
'''
valid_modes =   {   'customer':'Arbitrary query to DB',
                    'cost-center':'Dumps a Configuration Item',
                    'usage':'gets period usage',
                }
mode_help = "Any of: [%s]"%'|'.join(valid_modes.keys())
'''

"""
QUERY="
SELECT
    Typ_Code as TIPO,
    CIT_Is_Active as ACTIVO,
    IF(Typ_Code = 'CPU' OR Typ_Code = 'RAM',CIT_Is_Active,1) AS FACT,
    COUNT(*) as HORAS,
    SUM(CIT_Quantity) as QHR,
    SUM(CIT_Quantity)/720 as QMO,
    IF(Typ_Code = 'CPU' OR Typ_Code = 'RAM',720,1) AS RTMF,
    IF(Typ_Code = 'CPU',0.000072571429,
        IF(Typ_Code = 'RAM',0.000076142857,
            0.001186
        )
      ) AS RATE,
    IF(Typ_Code = 'CPU',0.000072571429*720,
        IF(Typ_Code = 'RAM',0.000076142857*720,
            0.001186
        )
      ) AS RATEMO,
    SUM(CIT_Quantity)/720
    *
    IF(Typ_Code = 'CPU',0.000072571429*720,
        IF(Typ_Code = 'RAM',0.000076142857*720,
            0.001186
        )
      )
    AS LUMEN
    FROM Charge_Items_${PERIOD}
    JOIN Charge_Units        USING (CU_Id)
    JOIN Configuration_Items USING (CI_Id)
    WHERE Cus_Id > 2 and CC_Id>2
    GROUP BY TIPO,ACTIVO
    ORDER BY TIPO,ACTIVO
"

"""

usage_template = """
<html>
<body>
</body>
    <h1>USASE RESUME {{data.period}}</H1><br>
    
    <table border=1>
    <tr><td>Configuration Items:</td><td>{{data.count_cis}}</td></tr>
    <tr><td>Virtual machines:   </td><td>{{data.count_vms}}</td></tr>
    <tr><td>Images:             </td><td>{{data.count_imgs}}</td></tr>
    <tr><td>Volume Groups:      </td><td>{{data.count_vgs}}</td></tr>
    </table>
    <table border = 1>
    <tr>
         <td>Componente</td>
         <td>Activo</td>
         <td>Horas</td>
         <td>Cantidad</td>
         <td>Cantidad Periodo</td>
         <td>Tarifa Base</td>
         <td>rtmf</td>
         <td>Tarifa Mensual</td>
         <td>Sub Total</td>
    </tr>
    <tr>
         <td>Virtual CPUs</td>
         <td>Active</td>
         <td>{{data.CPU.1.hours}}</td>
         <td>{{data.CPU.1.Q_Hours}}</td>
         <td>{{data.CPU.1.Q_Month}}</td>
         <td>{{"%.12f"|format(data.CPU.1.rate)}}</td>
         <td>{{data.CPU.1.rtmf}}</td>
         <td>{{"%.12f"|format(data.CPU.1.rate_month)}}</td>
         <td>{{"%.12f"|format(data.CPU.1.bill)}}</td>
    </tr>
    <tr>
         <td>Virtual CPUs</td>
         <td>Inactive</td>
         <td>{{data.CPU.0.hours}}</td>
         <td>{{data.CPU.0.Q_Hours}}</td>
         <td>{{data.CPU.0.Q_Month}}</td>
         <td>{{"%.12f"|format(data.CPU.0.rate)}}</td>
         <td>{{data.CPU.1.rtmf}}</td>
         <td>{{"%.12f"|format(data.CPU.0.rate_month)}}</td>
         <td>{{"%.12f"|format(data.CPU.0.bill)}}</td>
    </tr>
    <tr>
         <td>Virtual RAMs</td>
         <td>Active</td>
         <td>{{data.RAM.1.hours}}</td>
         <td>{{data.RAM.1.Q_Hours}}</td>
         <td>{{data.RAM.1.Q_Month}}</td>
         <td>{{"%.12f"|format(data.RAM.1.rate)}}</td>
         <td>{{data.RAM.1.rtmf}}</td>
         <td>{{"%.12f"|format(data.RAM.1.rate_month)}}</td>
         <td>{{"%.12f"|format(data.RAM.1.bill)}}</td>
    </tr>
    <tr>
         <td>Virtual RAMs</td>
         <td>Inactive</td>
         <td>{{data.RAM.0.hours}}</td>
         <td>{{data.RAM.0.Q_Hours}}</td>
         <td>{{data.RAM.0.Q_Month}}</td>
         <td>{{"%.12f"|format(data.RAM.0.rate)}}</td>
         <td>{{data.RAM.1.rtmf}}</td>
         <td>{{"%.12f"|format(data.RAM.0.rate_month)}}</td>
         <td>{{"%.12f"|format(data.RAM.0.bill)}}</td>
    </tr>
    <tr>
         <td>Virtual DSKs</td>
         <td>Active</td>
         <td>{{data.DSK.1.hours}}</td>
         <td>{{data.DSK.1.Q_Hours}}</td>
         <td>{{data.DSK.1.Q_Month}}</td>
         <td>{{"%.12f"|format(data.DSK.1.rate)}}</td>
         <td>{{data.DSK.1.rtmf}}</td>
         <td>{{"%.12f"|format(data.DSK.1.rate_month)}}</td>
         <td>{{"%.12f"|format(data.DSK.1.bill)}}</td>
    </tr>
    <tr>
         <td>Virtual DSKs HDD</td>
         <td>Active</td>
         <td>{{data.DSK.1.HDD.hours}}</td>
         <td>{{data.DSK.1.HDD.Q_Hours}}</td>
         <td>{{data.DSK.1.HDD.Q_Month}}</td>
         <td>{{"%.12f"|format(data.DSK.1.HDD.rate)}}</td>
         <td>{{data.DSK.1.rtmf}}</td>
         <td>{{"%.12f"|format(data.DSK.1.HDD.rate_month)}}</td>
         <td>{{"%.12f"|format(data.DSK.1.HDD.bill)}}</td>
    </tr>
    <tr>
         <td>Virtual DSKs SSD</td>
         <td>Active</td>
         <td>{{data.DSK.1.SSD.hours}}</td>
         <td>{{data.DSK.1.SSD.Q_Hours}}</td>
         <td>{{data.DSK.1.SSD.Q_Month}}</td>
         <td>{{"%.12f"|format(data.DSK.1.SSD.rate)}}</td>
         <td>{{data.DSK.1.rtmf}}</td>
         <td>{{"%.12f"|format(data.DSK.1.SSD.rate_month)}}</td>
         <td>{{"%.12f"|format(data.DSK.1.SSD.bill)}}</td>
    </tr>
    <tr>
         <td>Virtual DSKs</td>
         <td>Inactive</td>
         <td>{{data.DSK.0.hours}}</td>
         <td>{{data.DSK.0.Q_Hours}}</td>
         <td>{{data.DSK.0.Q_Month}}</td>
         <td>{{"%.12f"|format(data.DSK.0.rate)}}</td>
         <td>{{data.DSK.1.rtmf}}</td>
         <td>{{"%.12f"|format(data.DSK.0.rate_month)}}</td>
         <td>{{"%.12f"|format(data.DSK.0.bill)}}</td>
    </tr>
    <tr>
         <td>Virtual DSKs HDD</td>
         <td>Inactive</td>
         <td>{{data.DSK.0.HDD.hours}}</td>
         <td>{{data.DSK.0.HDD.Q_Hours}}</td>
         <td>{{data.DSK.0.HDD.Q_Month}}</td>
         <td>{{"%.12f"|format(data.DSK.0.HDD.rate)}}</td>
         <td>{{data.DSK.0.rtmf}}</td>
         <td>{{"%.12f"|format(data.DSK.0.HDD.rate_month)}}</td>
         <td>{{"%.12f"|format(data.DSK.0.HDD.bill)}}</td>
    </tr>
    <tr>
         <td>Virtual DSKs SSD</td>
         <td>Inactive</td>
         <td>{{data.DSK.0.SSD.hours}}</td>
         <td>{{data.DSK.0.SSD.Q_Hours}}</td>
         <td>{{data.DSK.0.SSD.Q_Month}}</td>
         <td>{{"%.12f"|format(data.DSK.0.SSD.rate)}}</td>
         <td>{{data.DSK.0.rtmf}}</td>
         <td>{{"%.12f"|format(data.DSK.0.SSD.rate_month)}}</td>
         <td>{{"%.12f"|format(data.DSK.0.SSD.bill)}}</td>
    </tr>
    
    
    </table>
    
</html>
"""

def Get_Charging_Resume(**kwargs):
    logger.debug(f'{this()}: Enter')
    logger.debug(f'{this()}: kwargs = {kwargs}')
    args = kwargs.get('args',None)   
    logger.debug(f"{this()}: args = {args}")
    
    #collectordata=get_collectordata()
    db.session.flush()
    db.session.commit()
    logger.debug(f'{this()}: DB Flushed and commited ...')    
    
    charge_item  = None
    current_user = 1
    ci_list      = []
    
    # Updated cached data for this specific query if requested 
    if args.update:
        
        # BE SURE all CU records has proper description ----------------
        updated_cus = db.Update_CU_Names()
        if updated_cus:
            logger.info(f"{this()}: Updated Name CUs = {updated_cus}")
        # BE SURE all CU records has proper rate id
        updated_cus = db.Update_CU_Rates()
        if updated_cus:
            logger.info(f"{this()}: Updated Rate CUs = {updated_cus}")
        # --------------------------------------------------------------
        
        logger.debug(f"args.customer id={args.customer} args.cost_center={args.cost_center}")
        #f args.customer_id is not None and args.cost_center is None:
        if args.filter == 'customer':
            logger.info(f"{this()}: filter customer mode: looking for matching CIs ...")
            query = db.session.query(
                    Configuration_Items.CI_Id
                    ).filter(Configuration_Items.Cus_Id==args.customer
                    ).order_by( Configuration_Items.CC_Id,
                                Configuration_Items.CI_Id
                    )
            logger.debug (f"{this()}: Cus_Id= {args.customer} query: {query}")
            CI = query.all()
            logger.info (f"{this()}: {len(CI)} CI's found for customer {args.customer}")
            resume_records=0
        
            logger.info(f"{this()}: Updating Charge Resume Update ...")
            ci_list = []
            for ci in CI:
                ci_list.append(ci.CI_Id)
            logger.info(f"{this()}: CI List updated ({len(ci_list)}) ...")
            charge_item  = None
            current_user = 1
            logger.debug(f"{this()}: customer    = {args.customer}")
            logger.debug(f"{this()}: period      = {args.start}-{args.end}")
            logger.debug(f"{this()}: cit status  = {args.cit_status}")
            logger.debug(f"{this()}: currency    = {args.currency}")
            logger.debug(f"{this()}: ci_list     = {ci_list}")
            logger.debug(f"{this()}: charge item = {charge_item}")
            logger.debug(f"{this()}: current_user= {current_user}")
        
        #f args.customer_id is None and args.cost_center is None:
        if args.filter == 'cost-center':
            logger.info(f"{this()}: filter cost center mode: looking for matching CIs ...")
            query = db.session.query(
                    Configuration_Items.CI_Id
                    ).filter(Configuration_Items.CC_Id==args.cost_center
                    ).order_by( 
                                Configuration_Items.CI_Id
                    )
            logger.debug (f"{this()}: CC_Id= {args.cost_center} query: {query}")
            CI = query.all()
            logger.info (f"{this()}: {len(CI)} CI's found for cost center {args.cost_center}")
            resume_records=0
        
            logger.info(f"{this()}: Updating Charge Resume Update ...")
            ci_list = []
            for ci in CI:
                ci_list.append(ci.CI_Id)
            logger.info(f"{this()}: CI List updated ({len(ci_list)}) ...")
            charge_item  = None
            current_user = 1
            logger.debug(f"customer    = {args.customer}")
            logger.debug(f"period      = {args.start}-{args.end}")
            logger.debug(f"cit status  = {args.cit_status}")
            logger.debug(f"currency    = {args.currency}")
            logger.debug(f"ci_list     = {ci_list}")
            logger.debug(f"charge item = {charge_item}")
            logger.debug(f"current_user= {current_user}")
        
        if args.filename:
            fp=open(filename,'a')
        else:
            if args.verbose:
                fp=sys.stdout
            else:
                fp=None
        start = datetime.datetime.now().timestamp() 
        if args.fifo:
            fifo_filename = f'{args.fifo}.fifo'
        else:
            fifo_filename = os.path.join(tempfile.mkdtemp(),'fifo')
        if os.path.exists(fifo_filename):
            os.remove(fifo_filename)
        os.mkfifo(fifo_filename)
        logger.warning(f"FIFO opening filename = {fifo_filename} for reading at the 'server' side")
        fifo_reader = os.open(fifo_filename,os.O_RDONLY|os.O_NONBLOCK)
        console  = True
        logger.warning(f"FIFO feedback filename = {fifo_filename} fp={fifo_reader}")
        records=0
        logger.info(f"Update resume using '{args.function}' algorithm ...")
        if args.queue:
            queue_id = queue.Queue(maxsize=0)
        else:
            queue_id = None
        logger.into(f"queue_id = {queue_id}")
        records = db.Update_Charge_Resume_CIS(
            args.customer,
            args.start.strftime('%Y-%m-%d'),
            args.end.strftime('%Y-%m-%d'),
            args.cit_status,
            args.currency,
            ci_list,             # <-- Lista de CIs Requeridos          
            Charge_Items,        # <-- Sharded CITs table
            current_user,
            fast=args.fast,
            callback = display_advance,    # Callback function if any, arguments follows
            step     = args.feedback_step, # Expected step, decimal representing a percentage
            fp       = fp,                 # file handler to display/write output to
            fifo     = fifo_filename,      # fifo handler to write output to
            progress = args.progress,      # progress filename (records actual advance)
            queue    = queue_id
            verbose  = args.verbose
            
            )
        end = datetime.datetime.now().timestamp()
        logger.info(f"Update completed {records} records modified in {end-start:.3f} seconds...")
    # Get Actual Remume Data from Database
    if args.filter == 'customer':
        FILTER=FILTER_CUSTOMER
    elif args.filter == 'cost-center':
        FILTER=FILTER_COST_CENTER
    else:
        FILTER == FILTER_ALL
    
    #Get_Charge_Resume_Filter(self,FILTER,CODE,DFROM,DTO,STATUS,CUR,CC_Id=None,Pla_Id=None,User_Id=None):

    start = datetime.datetime.now().timestamp()
    logger.info(f"getting data start: {datetime.datetime.now()}")
    rows = db.Get_Charge_Resume_Filter(
                FILTER,
                args.customer,
                args.start.strftime('%Y-%m-%d'),
                args.end.strftime('%Y-%m-%d'),
                args.cit_status,
                args.currency,
                CC_Id=args.cost_center,
                User_Id=current_user
                )
    end = datetime.datetime.now().timestamp()
    logger.info(f"getting data end: {datetime.datetime.now()}")
    logger.info(f"got data in {end-start:.3f} seconds")
    if type(rows) == list:
        if len(rows):
            logger.debug(f"{this()}: PRE RENDER")
            logger.debug(f"{this()}: FILTER CUSTOMER = {FILTER_CUSTOMER}")
            logger.debug(f"{this()}: type rows        = {type(rows)}")
            try:
                logger.debug(f"{this()}: len rows         = {len(rows)}")
            except:
                logger.warning(f"{this()}: len rows         = ERROR")        
            logger.debug(f"{this()}: Cus_Id           = {args.customer}")
            #print(f"{this()}: Cus_Name         = {Cus_Name}")
            logger.debug(f"{this()}: CIT_Date_From    = {args.start}")
            logger.debug(f"{this()}: CIT_Date_To      = {args.end}")
            logger.debug(f"{this()}: CIT_Status       = {args.cit_status}")
            logger.debug(f"{this()}: Cur_Code         = {args.currency}")
            logger.debug(f"{this()}: template         : report_charging_resume.html")
            try:
                """
                AQUI DEBE GUARDAR RESULTADO EN EXCEL y/O MOSTRARLO
                traer codigo de exportacion a xlsx e incluirlo aqui
                
                cols=[
                    'User_Id',
                    'Cus_Id',
                    'CR_Date_From',
                    'CR_Date_To',
                    'CIT_Status',
                    'Cur_Code',
                    'CU_Id',
                    'CIT_Count', 
                    'CIT_Quantity',
                    'CIT_Generation',
                    'CI_CC_Id',
                    'CU_Operation',
                    'Typ_Code',
                    'CC_Cur_Code',
                    'CI_Id',
                    'Rat_Id',
                    'Rat_Price',
                    'Rat_MU_Code',
                    'Rat_Cur_Code',
                    'Rat_Period',
                    'Rat_Hourly',
                    'Rat_Daily',
                    'Rat_Monthly',
                    'CR_Quantity',
                    'CR_Quantity_at_Rate',
                    'CC_XR',
                    'CR_Cur_XR',
                    'CR_ST_at_Rate_Cur',
                    'CR_ST_at_CC_Cur',
                    'CR_ST_at_Cur',
                    'Cus_Name',
                    'CI_Name',
                    'CU_Description',
                    'CC_Description',
                    'Rat_Period_Description',
                    'CC_Code',
                    'Pla_Id',
                    'Pla_Name'
                ]                
                with open(f'CR_{period}.csv','w') as fp:
                    for col in cols:
                        fp.write(f'"{col}";')
                    fp.write('\n')
                    for row in rows:
                        for col in cols:
                            fp.write(f'"{getattr(row,col)}";')
                        fp.write('\n')
                """
                output_file=f"CR_{period}"
                export_to_xls(output_file,rows,args.customer,args.start,args.end,args.cit_status,args.currency)
            except Exception as e:
                logger.error( f"{this()}: Exception:  {str(e)}")
        else:
            logger.warning(f"Empty (0) rows from DB !!!")            
    else:
        logger.error(f"Invalid rows {(type(rows))} from DB !!!")
    
    return
    
def export_to_xls(output_file,rows,Customer,From,To,Status,Currency):
    logger.info(f"{this()} IN")
    try:
        import  simplejson              as json
        from    pandas.io.json          import json_normalize
        #json_file="%s.json"%(output_file)
        json_file = export_to_json(output_file,rows,Customer,From,To,Status,Currency)
        
        #json_file   ="%s%s"%(current_app.root_path, url_for('static',filename='tmp/%s.json'%(output_file)))
        
        with open(json_file) as data_file:    
            d= json.load(data_file)  

        df1 = json_normalize(d, 'detail').assign(**d['header'])
            
        xlsx_file="%s/%s.xlsx"%('/tmp',output_file)
        
        df1.to_excel(xlsx_file,'Sheet 1')
               
        logger.info(f"{this()} {xlsx_file} created.")
        return xlsx_file    
    except Exception as e:
        emtec_handle_general_exception(e,logger=logger)
        return None

def export_to_csv(output_file,rows,Customer,From,To,Status,Currency,full=False):
    cvs_file="%s/%s"%(current_app.root_path,url_for('static',filename='tmp/%s'%(output_file)))
    f=open(cvs_file,"w")

    f.write('H,Customer,From,To,Status,Currency\n')
    f.write('H,"%s","%s","%s","%s","%s"\n'%(Customer,From,To,Status,Currency))
 
    if full:
        count = 0
        for row in rows:
            if count==0:
                _=[x.upper().replace("_","") for x in row.get_column_headers()]
                f.write('D,%s\n'%','.join(_))
            _=[str(x) for x in row.get_json_array()]
            f.write ("D,%s\n"%','.join(_))
            count += 1
    else:
        f.write('D,Records,CU,Rate,Q,Subtotal,XR,Total\n')
        count = 0
        for row in rows:
            f.write ("D,%s,%s,%s,%s,%s,%s,%s\n"%(
                        row.CIT_Count,
                        row.CU_Description,
                        row.Rat_Price,
                        row.CR_Quantity,
                        row.CR_ST_at_Rate_Cur,
                        row.CR_Cur_XR,
                        row.CR_ST_at_Cur
                        )
                    )
            count += 1
    f.write("T,%d\n"%(count))
    f.close()
    return cvs_file
    
def export_to_json(output_file,rows,Customer,From,To,Status,Currency,codes=False):
    logger.info(f"{this()} IN")
    import  simplejson              as json
    try:
        json_file="%s/%s.json"%('/tmp',output_file)
        logger.info(f"JSON file is : {json_file}")
        f=open(json_file,"w")
        
        dict = {}
        dict.update({'header':{}})
        dict['header'].update({'customer': Customer})
        dict['header'].update({'from'    : From.strftime('%Y-%m-%d')})
        dict['header'].update({'to'      : To.strftime('%Y-%m-%d')})
        dict['header'].update({'status'  : Status})
        dict['header'].update({'currency': Currency})
        dict.update({'detail':[]})
        count = 0
        #pprint(rows)
        
        for row in rows:
            if codes:
                dict['detail'].append(
                    {   
                        'customer':               row.Cus_Id,
                        'dateFrom':               row.CR_Date_From.strftime('%Y-%m-%d'),
                        'dateTo':                 row.CR_Date_To.strftime('%Y-%m-%d'),
                        'status':                 row.CIT_Status,
                        'currency':               row.Cur_Code,
                        'items':                  row.CIT_Count, 
                        'quantity':               row.CIT_Quantity, 
                        'generation':             row.CIT_Generation, 
                        'cu':                     row.CU_Id,
                        'cc':                     row.CI_CC_Id,
                        'operation':              row.CU_Operation,
                        'type':                   row.Typ_Code,
                        'ccCurrency':             row.CC_Cur_Code,           
                        'ci':                     row.CI_Id,     
                        'rate':                   row.Rat_Id,      
                        'price':                  row.Rat_Price,
                        'mu':                     row.Rat_MU_Code,
                        'rateCurrency':           row.Rat_Cur_Code,
                        'rateHourly':             row.Rat_Hourly,
                        'rateDaily':              row.Rat_Daily,
                        'rateMonthly':            row.Rat_Monthly,
                        'resumeQuantity':         row.CR_Quantity,          # CIT Quantity after conversion, if any
                        'resumeQuantityAtRate':   row.CR_Quantity_at_Rate, 
                        'ccXR':                   row.CC_XR,
                        'resumeCurrencyXR':       row.CR_Cur_XR,
                        'subtotalAtRateCurrency': row.CR_ST_at_Rate_Cur,
                        'subtotalAtCcCurrency':   row.CR_ST_at_CC_Cur,
                        'totalAtCurrency':        row.CR_ST_at_Cur,
                        'cusName':                row.Cus_Name,
                        'ciName':                 row.CI_Name,
                        'cuDescription':          row.CU_Description,
                        'ccDescription':          row.CC_Description, 
                        'ratePeriodDescription':  row.Rat_Period_Description, 
                        'ccCode':                 row.CC_Code, 
                        'platform':               row.Pla_Id, 
                        'platformName':           row.Pla_Name, 
                    }
                )
            else:
                dict['detail'].append(
                    {   
                        'items':                  row.CIT_Count, 
                        'quantity':               row.CIT_Quantity, 
                        'type':                   row.Typ_Code,
                        'price':                  row.Rat_Price,
                        'mu':                     row.Rat_MU_Code,
                        'rateCurrency':           row.Rat_Cur_Code,
                        'rateHourly':             row.Rat_Hourly,
                        'rateDaily':              row.Rat_Daily,
                        'rateMounhtly':           row.Rat_Monthly,
                        'resumeQuantity':         row.CR_Quantity,
                        'resumeQuantityAtRate':   row.CR_Quantity_at_Rate, 
                        'ccXR':                   row.CC_XR,
                        'resumeCurrencyXR':       row.CR_Cur_XR,
                        'subtotalAtRateCurrency': row.CR_ST_at_Rate_Cur,
                        'subtotalAtCcCurrency':   row.CR_ST_at_CC_Cur,
                        'totalAtCurrency':        row.CR_ST_at_Cur,
                        'ciName':                 row.CI_Name,
                        'cuDescription':          row.CU_Description,
                        'ccDescription':          row.CC_Description, 
                        'ratePeriodDescription':  row.Rat_Period_Description, 
                        'ccCode':                 row.CC_Code, 
                        'platformName':           row.Pla_Name, 
                    }
                )
                
            #if count == 0:
            #    for key in dict['detail'][0]:
            #        print(f"key= {key:30s} type= {str(type(dict['detail'][0][key])):40s} value= {dict['detail'][0][key]}")
            count += 1
        dict['header'].update({'count':count})
        jsonarray = json.dumps(dict)
        
        f.write(jsonarray)

        f.close()
        logger.info(f"{this()} {json_file} created.")
        return json_file
    except Exception as e:
        emtec_handle_general_exception(e,logger=logger)
        return None

def export_to_fix(output_file,rows,Customer,From,To,Status,Currency):
    fix_file="%s/%s"%(current_app.root_path,url_for('static',filename='tmp/%s'%(output_file)))

    f=open(fix_file,"w")

    f.write("H%06d%-45s%-10s%-10s%-45s%-45s*\n"%(0,Customer,From,To,Status,Currency))
    count = 0
    for row in rows:
        f.write ("D%06d%-45s%020.6f%020.6f%020.6f%020.6f%020.6f%010d*\n"%(
                    row.CIT_Count,
                    row.CU_Description,
                    row.Rat_Price,
                    row.CR_Quantity,
                    row.CR_ST_at_Rate_Cur,
                    row.CR_Cur_XR,
                    row.CR_ST_at_Cur,
                    0)
                )
        count += 1
    f.write("T%06d%0155d*\n"%(count,0))
    f.close()
    return fix_file

    
def Report_Charging_Resume(args=None):
    logger.debug('Report_Charging_Resume')
    return
    

def get_args():
    
    valid_modes =   [   
                        'charge',
                        'usage',
                    ]
    mode_help         = "Any of: [%s]"%'|'.join(valid_modes)
    mode_help        += " 'test': Charge Resume detail mode."
    mode_help        += " 'usage': Fast Usage resume mode."
    
    # Models help
    charge_help       = 'Charge mode detailed help. Intented to calculate period charges at detail.'
    usage_help        = 'Period Usage detailed help Intented to calculate fast period usage for non complex accounts.'
    # Common modes arguments
    config_help       = "JSON configuration file. Content overrides arguments if any."
    log_filename_help = "Log filename. If defined a filesystem file that captures process behavior"
    verbose_help      = "Increase output and log verbosity (default 0=No output, 1=Information, 2=Debug)."
    function_help     = "charge: Calculation function"
    
    # Argument's common_parser definitions -----------------------------
    common_parser     = argparse.ArgumentParser(description="EG Collector - Get Pre-Billing Resumes")
    # common arguments
    common_parser.add_argument('-M' ,'--month'         ,help='Report Month (1-12)',required=False,default=None,type=int)
    common_parser.add_argument('-Y' ,'--year'          ,help='Report Year (YYYY)' ,required=False,default=None,type=int)
    common_parser.add_argument('-c', '--config'        ,help=config_help,          required=False,default=None)
    common_parser.add_argument("-l", '--log-filename'  ,help=log_filename_help,    required=False,default=None)
    common_parser.add_argument("-v", '--verbose'       ,help=verbose_help,         required=False,default=0,action='count')
    # ------------------------------------------------------------------
    # Define main parser
    main_parser = argparse.ArgumentParser()
    # Create mode subparsers
    subparsers = main_parser.add_subparsers(title="Execution modes dest='mode'",dest='mode',help=mode_help)
    charge = subparsers.add_parser('charge', parents=[common_parser], add_help=False, description='Charge Detail Mode',help=charge_help)
    usage  = subparsers.add_parser('usage' , parents=[common_parser], add_help=False, description='Period Usage Mode' ,help=usage_help)
    # sub arguments per mode
    # charge ----------------------------------------------------------
    charge.add_argument('-f', '--function'          ,help=function_help,required=True,default=None)
    charge.add_argument(      '--filter'            ,help='charge filter',required=False,default='customer')
    charge.add_argument(      '--customer'          ,help='customer id',required=False,default=1)
    charge.add_argument(      '--cit-status'        ,help='cit status',required=False,default=1)
    charge.add_argument(      '--currency'          ,help='currency',required=False,default=1)
    charge.add_argument(      '--cost-center'       ,help='customer id',required=False,default=1)
    charge.add_argument(      '--start'             ,help='Period Start',required=False,default=None)
    charge.add_argument(      '--end'               ,help='Period End',required=False,default=None)
    charge.add_argument(      '--today'             ,help='Today Only',required=False,default=False,action='store_true')
    charge.add_argument(      '--yesterday'         ,help='Up to Yesterday',required=False,default=False,action='store_true')
    charge.add_argument(      '--feedback_function' ,help='feedback_function help',required=False,default=None)
    charge.add_argument(      '--progress'          ,help='Feedback progress filename',required=False,default=None)
    charge.add_argument(      '--filename'          ,help='Feedback output filename',required=False,default=None)
    charge.add_argument(      '--fifo'              ,help='Feedback FIFO filename',required=False,default=None)
    charge.add_argument(      '--queue'             ,help='Uses Queue for IPC',required=False,default=False,action='store_true')
    charge.add_argument(      '--feedback-function' ,help='Calculation Function Name',required=False,type=float,default=0.01) # 1.00 %
    charge.add_argument(      '--feedback-step'     ,help='Feedback step %% (0.00 - 1.00)',required=False,type=float,default=0.01) # 1.00 %
    charge.add_argument(      '--update'            ,help='Update DB prior report (default=False)',action='store_true',required=False,default=False)
    charge.add_argument(      '--fast'              ,help='Use fast population algorithm  (default=False)',action='store_true',required=False,default=False)
    # usage ----------------------------------------------------------

    args = main_parser.parse_args()
    
    return args

args = get_args()

if args.verbose==0:
    logger.setLevel(logging.NOTSET)
    for handler in logger.handlers:
        handler.setLevel(logging.NOTSET)
if args.verbose==1:
    logger.setLevel(logging.INFO)
    for handler in logger.handlers:
        handler.setLevel(logging.INFO)
if args.verbose>1:
    logger.setLevel(logging.DEBUG)
    for handler in logger.handlers:
        handler.setLevel(logging.DEBUG)

logger.debug(f"logger = {logger}")
for handler in logger.handlers:
    logger.debug(f"  handler = {handler}")
for arg in args.__dict__:
    logger.debug(f"args.{arg}={getattr(args,arg)}")
logger.debug(f"db = {db}")

logger.info(f"args.year      = {args.year}")
logger.info(f"args.month     = {args.month}")
logger.info(f"args.today     = {args.today}")
logger.info(f"args.yesterday = {args.yesterday}")
logger.info(f"args.start     = {args.start}")
logger.info(f"args.end       = {args.end}")
if args.month is not None:   # Check for specific month required
    year=datetime.datetime.now().year if args.year is None else args.year
    date=f'01-{str(args.month)}-{year}'
    logger.debug(f"year={year} default date={date}")
    dt=datetime.datetime.now() if args.month is None else datetime.datetime.strptime(date,'%d-%m-%Y') 
    args.start,args.end = Get_Period(dt,PERIOD_MONTH)
elif args.yesterday:         # Check for from start of month up to yesterday report required
    args.start,args.end = Get_Period(datetime.datetime.now(),PERIOD_YESTERDAY)
elif args.today:             # Check for today only just up to now report required
    args.start,args.end = Get_Period(datetime.datetime.now(),PERIOD_DAY)
elif args.start or args.end: # Check for specific period report required
    if args.start is None:
        args.start,end = Get_Period(datetime.datetime.now())
    else:
        args.start = datetime.datetime.strptime(args.start,"%Y-%m-%d")
    if args.end is None:
        start,args.end = Get_Period(datetime.datetime.now())
    else:
        args.end = datetime.datetime.strptime(args.end,"%Y-%m-%d")
else:                       # Check for from start of month to up to now report required
    args.start,args.end = Get_Period(datetime.datetime.now(),PERIOD_MONTH)
    
logger.debug(f"args={args}")
logger.info(f"args.start     = {args.start}")
logger.info(f"args.end       = {args.end}")

if __name__ == "__main__":
    logger.debug("Enter main ...")
    # Required: Push context to use the global "db" variable
    logger.debug(f"COLLECTOR_CONFIG={os.getenv('COLLECTOR_CONFIG')}")
    logger.debug(f"config = {config}")
    app     = create_app(os.getenv('COLLECTOR_CONFIG') or 'default')
    logger.debug(f"app        = {app}")
    logger.debug(f"app.config = {app.config}")
    logger.debug(f"db         = {db}")

    app_ctx = app.app_context()
    logger.debug(f"app_ctx    = {app_ctx}")
    app_ctx.push()
    db.init_app(app)
    logger.debug(f"app        = {app}")
    logger.debug(f"db         = {db}")
    
    cfg = config[os.getenv('COLLECTOR_CONFIG') or 'default']
    logger.debug(f"cfg        = {cfg}")
    logger.debug(f"cfg type   = {type(cfg)}")
    logger.debug(f"COLLECTOR_CONFIG_FILE   = {cfg.COLLECTOR_CONFIG_FILE}")
    logger.debug(f"SQLALCHEMY_DATABASE_URI = {cfg.SQLALCHEMY_DATABASE_URI}")
    parser = configparser.ConfigParser(
            allow_no_value=False,     # don't allow "key" without "="
            delimiters=('=',),        # inifile "=" between key and value
            comment_prefixes=(';','#'),  # only ';' for comments (fixes #channel)
            inline_comment_prefixes=(';'),     # comments after lines
            interpolation=configparser.ExtendedInterpolation(),
            empty_lines_in_values=False  # empty line means new key
            )
    parser.read(cfg.COLLECTOR_CONFIG_FILE)
    
    # Time context
    today = datetime.datetime.now()
    yesterday = datetime.datetime.now() - datetime.timedelta(1)
    logger.info(f"yesterday        = {yesterday}")
    logger.info(f"today            = {today}")

    if today.month == yesterday.month:
        logger.info(f"estoy en el mismo mes hoy es el dia {today.day} period={PERIOD_DAY}")
        today_start    ,today_end     = Get_Period(today,PERIOD_DAY)
        yesterday_start,yesterday_end = Get_Period(today,PERIOD_YESTERDAY)
        #esterday_end = yesterday.replace(yesterday.year, yesterday.month, yesterday.day, 23, 0, 0, 0)
        yesterday_suffix = f"{yesterday.year}{yesterday.month}{yesterday.day}"
        today_suffix     = f"{today.year}{today.month}{today.day}"
    else:
        logger.info(f"cambio de mes debo estar en el dia 1={today.day}")
        today_start    ,today_end     = Get_Period(today,PERIOD_DAY)
        yesterday_start,yesterday_end = Get_Period(today,PERIOD_YESTERDAY)
        yesterday_suffix = None
        today_suffix     = f"{today.year}{today.day}"
    logger.info(f"yesterday suffix = {yesterday_suffix} {yesterday_start} {yesterday_end}")
    logger.info(f"today suffix     = {today_suffix} {today_start} {today_end}")
    
    # Read Configuration
    # Rates
    Rates = {}
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
    
    logger.debug(f"logger     = {logger}")
    db.logger=logger
    logger.debug(f"db         = {db} db.logger = {db.logger}")
    try:    
        db_connection_is_successfull = False              
        try:
            if args.verbose > 0: logger.debug(f"connecting to {db}' ...")
            cis = db.session.query(Configuration_Items).count()
            logger.debug(f"cis        = {cis}")
            if args.verbose > 0: logger.info("DB connection successful.")
            db_connection_is_successfull = True              
            logger.debug(f'args       = {args}')            
            if db is not None and db_connection_is_successfull:
                logger.info(f"Getting resume from {args.start} to {args.end}")
                # Need to populate 'customer' variable
                period = f"{customer}_{args.start.year}{args.start.month:02d}"
                cits_table = f"Charge_Items_{period}"
                logger.debug(f"Period     =  {period}")
                Charge_Items.set_shard(period,db.engine)
                logger.debug(f"CIT        =  {Charge_Items}")
                logger.debug(f"CIT        =  {Charge_Items.__table__.name}")
                logger.debug(f"CIT        =  {Charge_Items.__tablename__}")
                test = db.session.query(Charge_Items).count()
                logger.info(f"{test} rows in {Charge_Items.__tablename__}")
                if   args.mode == 'charge':
                    logger.info(f"Enter 'charge' mode ...")
                    if   args.function == 'standard':
                        args.fast = False
                    elif args.function == 'fast':
                        args.fast = True
                    logger.info(f"Setting '{args.mode}-{args.function}' mode ...")
                    
                    Get_Charging_Resume(args=args)
                    Report_Charging_Resume(args)
                elif args.mode == 'usage':
                    logger.info(f"Enter 'usage' mode ...")
                    usage = db.Get_Period_Usage(customer_id=args.customer,rates=Rates)
                    templateLoader = jinja2.FileSystemLoader(searchpath="./")
                    templateEnv = jinja2.Environment(loader=templateLoader)
                    TEMPLATE_FILE = "get_period_usage.html"
                    template = templateEnv.get_template(TEMPLATE_FILE)
                    html = template.render(data=usage)  
                    with open('usage.html','w') as fp:
                        fp.write(html)
                else:
                    logger.error("Unimplemented mode: %s"%args.mode)
            else:
                logger.error("DB session couldn't be open. Connection unsuccessful.")
        except Exception as e:
            logger.error(str(e))

    except Exception as e:
        logger.error("EXCEPTION: ",str(e))
        raise e
    logger.info("Execution completed.")
    
