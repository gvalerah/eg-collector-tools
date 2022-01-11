"""
Command Line Get Charge Resume
"""
import logging
import os
from pprint import pprint,pformat
from    emtec                               import *
from    emtec.feedback                      import *
from    emtec.collector.db.orm              import *
import  simplejson              as json

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

# Minimum requirement to use db object ---------------------------------
from    flask                               import Flask
from    flask_sqlalchemy                    import SQLAlchemy
from    config                              import config
from    emtec                               import *
from    emtec.collector.db.orm              import *
db                                          = Collector_ORM_DB()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # Inititializes applications (incomplete by now)
    db.init_app             (app)
    # Collector's modules
    return app 
# ----------------------------------------------------------------------

# Here I can setup multiple Collector Tool Services
valid_modes =   {   'customer':'Arbitrary query to DB',
                    'cost-center':'Dumps a Configuration Item',
                }
mode_help = "Any of: [%s]"%'|'.join(valid_modes.keys())


def Get_Charging_Resume(args=None):
    logger.debug(f'{this()}: Enter')    
    #collectordata=get_collectordata()
    db.session.flush()
    db.session.commit()
    logger.debug(f'{this()}: DB Flushed and commited ...')    
    
    charge_item  = None
    current_user = 1
    
    # Updated cached data for this specific query if requested 
    if args.update:
        
        # BE SURE all CU records has proper description ----------------
        updated_cus = db.Update_CU_Names()
        if updated_cus:
            logger.info(f"Updated Name CUs = {updated_cus}")
        # BE SURE all CU records has proper rate id
        updated_cus = db.Update_CU_Rates()
        if updated_cus:
            logger.info(f"Updated Rate CUs = {updated_cus}")
        # --------------------------------------------------------------
        
        logger.debug(f"args.customer_id={args.customer_id} args.cost_center={args.cost_center}")
        #f args.customer_id is not None and args.cost_center is None:
        if args.mode == 'customer':
            logger.info(f"custome mode: looking for matching CIs ...")
            query = db.session.query(
                    Configuration_Items.CI_Id
                    ).filter(Configuration_Items.Cus_Id==args.customer_id
                    ).order_by( Configuration_Items.CC_Id,
                                Configuration_Items.CI_Id
                    )
            logger.debug (f"{this()}: Cus_Id= {args.customer_id} query: {query}")
            CI = query.all()
            logger.info (f"{this()}: {len(CI)} CI's found for customer {args.customer_id}")
            resume_records=0
        
            logger.info(f"{this()}: Updating Charge Resume Update ...")
            ci_list = []
            for ci in CI:
                ci_list.append(ci.CI_Id)
            logger.info(f"{this()}: CI List updated ({len(ci_list)}) ...")
            charge_item  = None
            current_user = 1
            logger.debug(f"customer    = {args.customer_id}")
            logger.debug(f"period      = {args.start}-{args.end}")
            logger.debug(f"cit status  = {args.cit_status}")
            logger.debug(f"currency    = {args.currency}")
            logger.debug(f"ci_list     = {ci_list}")
            logger.debug(f"charge item = {charge_item}")
            logger.debug(f"current_user= {current_user}")
        
        #f args.customer_id is None and args.cost_center is None:
        if args.mode == 'cost-center':
            logger.info(f"cost center mode: looking for matching CIs ...")
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
            logger.debug(f"customer    = {args.customer_id}")
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
        if args.fast:
            records=0
            logger.info(f"Update resume using fast algorithm ...")
        else:
            logger.info(f"Update resume using standard algorithm ...")

            records = db.Update_Charge_Resume_CIS(
                args.customer_id,
                args.start.strftime('%Y-%m-%d'),
                args.end.strftime('%Y-%m-%d'),
                args.cit_status,
                args.currency,
                ci_list,             # <-- Lista de CIs Requeridos          
                Charge_Items,        # <-- Sharded CITs table
                current_user,
                callback=display_advance,
                step=args.feedback_step,
                fp=fp,
                fifo=fifo_filename,
                progress=args.progress
                
                )
        end = datetime.datetime.now().timestamp()
        logger.info(f"Update completed {records} records modified in {end-start:.3f} seconds...")
    # Get Actual Remume Data from Database
    if args.mode == 'customer':
        FILTER=FILTER_CUSTOMER
    elif args.mode == 'cost-center':
        FILTER=FILTER_COST_CENTER
    else:
        FILTER == FILTER_ALL
    
    #Get_Charge_Resume_Filter(self,FILTER,CODE,DFROM,DTO,STATUS,CUR,CC_Id=None,Pla_Id=None,User_Id=None):

    rows = db.Get_Charge_Resume_Filter(
                FILTER,
                args.customer_id,
                args.start.strftime('%Y-%m-%d'),
                args.end.strftime('%Y-%m-%d'),
                args.cit_status,
                args.currency,
                CC_Id=args.cost_center,
                User_Id=current_user
                )
    if type(rows) == list:
        if len(rows):
            logger.debug(f"{this()}: PRE RENDER")
            logger.debug(f"{this()}: FILTER CUSTOMER = {FILTER_CUSTOMER}")
            logger.debug(f"{this()}: type rows        = {type(rows)}")
            try:
                logger.debug(f"{this()}: len rows         = {len(rows)}")
            except:
                logger.warning(f"{this()}: len rows         = ERROR")        
            logger.debug(f"{this()}: Cus_Id           = {args.customer_id}")
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
                export_to_xls(output_file,rows,args.customer_id,args.start,args.end,args.cit_status,args.currency)
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

def Get_Arguments():
    # Argument's parser definitions
    parser = argparse.ArgumentParser()
    parser.add_argument('-m' ,'--mode'         ,help=mode_help,   required=True,default=None)
    parser.add_argument('-R' ,'--rdbms'        ,help='ORM RDBMS',     required=False,default='mysql')
    parser.add_argument('-D' ,'--dialect'      ,help='ORM Dialect',   required=False,default='pymysql')
    parser.add_argument('-H' ,'--host'         ,help='DB Host name or IP',      required=False,default='localhost')
    parser.add_argument('-P' ,'--port'         ,help='D Port',      required=False,default=3306)
    parser.add_argument('-u' ,'--user'         ,help='DB User',      required=False,default='collector')
    parser.add_argument('-p' ,'--password'     ,help='DB Password',  required=False,default='collector')
    parser.add_argument('-s' ,'--schema'       ,help='DB Schema',    required=False,default='collector')
    parser.add_argument('-U' ,'--user-id'      ,help='Collector User Id',    required=False,default=1)
    parser.add_argument('-C' ,'--customer-id'  ,help='Collector Customer Id',    required=False,default=None)
    parser.add_argument('-CC','--cost-center'  ,help='Collector Top Cost Center',    required=False,default=None)
    parser.add_argument('-F' ,'--start'        ,help='Period Start Date',    required=False,default=None)
    parser.add_argument('-T' ,'--end'          ,help='Period End   Date',    required=False,default=None)
    parser.add_argument('-CU','--currency'     ,help='Currency Code',    required=False,default='UF')
    parser.add_argument('-S' ,'--cit-status'   ,help='CIT-Status',    required=False,default=1)
    parser.add_argument('-M' ,'--month'        ,help='Report Month (1-12)',    required=False,default=None)
    parser.add_argument("-v" ,'--verbose'      ,help='Increase output verbosity',action='count',required=False,default=0)
    parser.add_argument(      '--progress'     ,help='Feedback progress filename',required=False,default=None)
    parser.add_argument(      '--filename'     ,help='Feedback output filename',required=False,default=None)
    parser.add_argument(      '--fifo'         ,help='Feedback FIFO filename',required=False,default=None)
    parser.add_argument(      '--feedback-step',help='Feedback step % (0.00 - 1.00)',required=False,type=float,default=0.01) # 1.00 %
    parser.add_argument(      '--update'       ,help='Update DB prior report (default=False)',action='store_true',required=False,default=False)
    parser.add_argument(      '--fast'         ,help='Use fast population algorithm  (default=False)',action='store_true',required=False,default=False)

    args = parser.parse_args()
    return args
    
args = Get_Arguments()
logger.debug(f"args={args}")
 
dt = datetime.datetime.now()
if args.month is not None:
    year=datetime.datetime.now().year
    date=f'01-{str(args.month)}-{year}'
    logger.debug(f"year={year} default date={date}")
    dt=datetime.datetime.now() if args.month is None else datetime.datetime.strptime(date,'%d-%m-%Y') 
args.start,args.end = Get_Period(dt)
logger.debug(f"args={args}")

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

if __name__ == "__main__":
    # Required: Push context to use the global "db" variable
    logger.debug(f"COLLECTOR_CONFIG={os.getenv('COLLECTOR_CONFIG')}")
    app     = create_app(os.getenv('COLLECTOR_CONFIG') or 'default')
    app_ctx = app.app_context()
    app_ctx.push()

    logger.debug(f"logger={logger}")
    db.logger=logger
    logger.debug(f"db={db} db.logger={db.logger}")
    try:                  
        try:
            if args.verbose > 0: logger.info(f"connecting to {db}' ...")
            if args.verbose > 0: logger.info("DB connection successful.")
            logger.debug(f'args={args}')            
        except Exception as e:
            logger.error(str(e))
            logger.warning("WARNING: DB connection unsuccessful.")
        if db is not None:
            logger.info(f"Getting resume from {args.start} to {args.end}")
            # GV Need to populate 'customer' variable
            period = f"{customer}_{args.start.year}{args.start.month:02d}"
            cits_table = f"Charge_Items_{period}"
            logger.debug(f"Period =  {period}")
            Charge_Items.set_shard(period,db.engine)
            logger.debug(f"CIT  =  {Charge_Items}")
            logger.debug(f"CIT  =  {Charge_Items.__table__.name}")
            logger.debug(f"CIT  =  {Charge_Items.__tablename__}")
            test = db.session.query(Charge_Items).count()
            logger.info(f"{test} rows in {Charge_Items.__tablename__}")
            if   args.mode == 'customer':
                logger.info(f"Enter 'customer' mode ...")
                Get_Charging_Resume(args)
                Report_Charging_Resume(args)
            elif args.mode == 'cost-center':
                logger.info(f"Enter 'cost-center' mode ...")
                Get_Charging_Resume(args)
                Report_Charging_Resume(args)
            else:
                logger.error("Unimplemented mode: %s"%args.mode)
        else:
            logger.error("DB session couldn't be open.")
    except Exception as e:
        logger.error("EXCEPTION: ",str(e))
        raise e
    logger.info("Execution completed.")
    

