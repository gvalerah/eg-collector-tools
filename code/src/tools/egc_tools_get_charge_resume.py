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
from sqlalchemy import tuple_
import jinja2
import configparser

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
    print(f"create_app: db = {db}")
    # Collector's modules
    return app 
# ----------------------------------------------------------------------

# Here I can setup multiple Collector Tool Services
valid_modes =   {   'customer':'Arbitrary query to DB',
                    'cost-center':'Dumps a Configuration Item',
                    'usage':'gets period usage',
                }
mode_help = "Any of: [%s]"%'|'.join(valid_modes.keys())


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

"""
def Get_Period_Usage(customer_id=0,rates={}):
    logger.debug(f'{this()}: Enter')    
    #collectordata=get_collectordata()
    db.session.flush()
    db.session.commit()
    logger.debug(f'{this()}: DB Flushed and commited ...')    
    
    charge_item  = None
    current_user = 1
    
    rate_cpu   = rates.get('cpu').get('rate',0.000072571429)     
    rate_ram   = rates.get('ram').get('rate',0.000076142857)      
    rate_dsk   = rates.get('dsk').get('rate',0.001186000000)      
    rate_hdd   = rates.get('hdd').get('rate',0.001186000000)      
    rate_ssd   = rates.get('ssd').get('rate',0.00363857142857143)  
    factor_hdd = rates.get('factor_hdd').get('rate',0.8)
    factor_ssd = 1 - factor_hdd
    
    period = Charge_Items.__tablename__.split('_')[2]
    
    usage = {
        'period'                 : period,
        'billeable_records'      : 0,
        'contributing_records'   : 0,
        'total_q_hours'          : 0,
        'total_q_month'          : 0,
        'total_cpus'             : 0,
        'total_rams'             : 0,
        'total_dsks'             : 0,
        'total_bill'             : 0,
        'total_bill_distributed' : 0,
        'rate_cpu'               : rate_cpu,
        'rate_ram'               : rate_ram,
        'rate_dsk'               : rate_dsk,
        'rate_hdd'               : rate_hdd,
        'rate_ssd'               : rate_ssd,
        'factor_hhd'             : factor_hdd,
        'factor_ssd'             : factor_ssd,
        'rates'                  : rates
    }
    

    logger.debug(f"usage mode: counting records in {Charge_Items.__tablename__} ...")
    total_db_cits = db.session.query(Charge_Items.CU_Id).count()
    logger.debug(f"Charge Items in DB = {total_db_cits}")
    total_db_cus = db.session.query(Charge_Items.CU_Id).distinct().count()
    logger.debug(f"Charge Units in DB = {total_db_cus}")

    total_cits = db.session.query(Charge_Items.CU_Id
                    ).select_from(Charge_Items
                    ).join(Charge_Units,Charge_Units.CU_Id==Charge_Items.CU_Id
                    ).join(Configuration_Items,Configuration_Items.CI_Id==Charge_Units.CI_Id
                    ).filter(Configuration_Items.Cus_Id==customer_id
                    ).count()
    logger.debug(f"Customer Components = {total_cits}")

    cus = db.session.query(
                    Charge_Items.CU_Id
                    ).select_from(Charge_Items
                    ).join(Charge_Units,Charge_Units.CU_Id==Charge_Items.CU_Id
                    ).join(Configuration_Items,Configuration_Items.CI_Id==Charge_Units.CI_Id
                    ).filter(Configuration_Items.Cus_Id==customer_id
                    ).distinct(
                    ).all()
    total_cus = len(cus)
    logger.debug(f"Components = {total_cus}")

    logger.debug(f"usage mode: counting CIs in {Charge_Items.__tablename__} ...")
    cis = db.session.query(
                    Configuration_Items.CI_Id,
                    Configuration_Items.CI_Name,
                    Configuration_Items.CI_UUID
                    ).select_from(Charge_Items
                    ).join(Charge_Units,Charge_Units.CU_Id==Charge_Items.CU_Id
                    ).join(Configuration_Items,Configuration_Items.CI_Id==Charge_Units.CI_Id
                    ).filter(Configuration_Items.Cus_Id==customer_id
                    ).distinct(tuple_(Configuration_Items.CI_Id)
                    ).order_by(tuple_(Configuration_Items.CI_Id)
                    ).all()
    total_cis = len(cis)
    logger.debug(f"Configuration Items = {total_cis}")
    ci_vms  = 0
    ci_imgs = 0
    ci_vgs  = 0
    query = db.session.query(
                Configuration_Items.CI_Id,
                Charge_Units.Typ_Code,
                Configuration_Items.CI_Name,
                Configuration_Items.CI_UUID
                ).select_from(Charge_Items
                ).join(Charge_Units,Charge_Units.CU_Id==Charge_Items.CU_Id
                ).join(Configuration_Items,Configuration_Items.CI_Id==Charge_Units.CI_Id
                ).filter(Configuration_Items.Cus_Id==customer_id
                ).distinct(tuple_(Configuration_Items.CI_Id,Charge_Units.Typ_Code)
                ).order_by(Configuration_Items.CI_Id,Charge_Units.Typ_Code
                )
    logger.debug(f"query = {query}")
    cis=query.all()
    inventory = {}
    for ci in cis:
        if ci.CI_Id not in inventory:
            inventory.update({
                ci.CI_Id:{'CPU':0,'RAM':0,'IMG':0,'DSK':0,'SNP':0,'DRP':0}
                })
        inventory[ci.CI_Id][ci.Typ_Code] += 1
    for ci in inventory:
        if inventory[ci]['CPU'] >= 1:
            ci_vms += 1
        elif inventory[ci]['IMG'] >= 1:
            ci_imgs += 1
        elif inventory[ci]['DSK'] >= 1:
            ci_vgs += 1
    
    logger.debug(f"{this()}: ci vms   = {ci_vms}")
    logger.debug(f"{this()}: ci img   = {ci_imgs}")
    logger.debug(f"{this()}: ci vgs   = {ci_vgs}")
    logger.debug(f"{this()}: total ci = {ci_vms+ci_imgs+ci_vgs}")
    usage.update({
        'count_cis' :total_cis,
        'count_vms' :ci_vms,
        'count_imgs':ci_imgs,
        'count_vgs' :ci_vgs,
        # DB
        'count_total_db_cits':total_db_cits,
        'count_total_db_cus':total_db_cus,
        # Customers
        'count_total_cits':total_cits,
        'count_total_cus':total_cus,
        'count_total_cis':total_cis,
    })
            
    
    # Updated cached data for this specific query if requested 
    logger.debug(f"{this()}: usage mode: looking for matching CIs ...")
    logger.debug(f"{this()}: Customer Id         = {customer_id}")
    query = db.session.query(
            func.count(Charge_Items.CU_Id).label('Hours'),
            Charge_Items.CIT_Is_Active.label('Active'),
            Charge_Units.Typ_Code.label('Type'),
            func.sum(Charge_Items.CIT_Quantity).label('Q_Hours')
            ).join(Charge_Units,Charge_Units.CU_Id==Charge_Items.CU_Id
            ).join(Configuration_Items,Configuration_Items.CI_Id==Charge_Units.CI_Id
            ).filter(Configuration_Items.Cus_Id==customer_id
            ).group_by( Charge_Units.Typ_Code,
                        Charge_Items.CIT_Is_Active
            ).order_by( Charge_Units.Typ_Code,
                        Charge_Items.CIT_Is_Active
            )
    logger.debug(f"{this()}: Charge_Items        = {Charge_Items.__tablename__}")
    logger.debug(f"{this()}: Charge_Units        = {Charge_Units.__tablename__}")
    logger.debug(f"{this()}: Configuration_Items = {Configuration_Items.__tablename__}")
    logger.debug(f"{this()}: query={query}")
    result = query.all()
    
    billeable_records = 0
    contributing_records = 0
    total_q_hours          = 0
    total_q_month          = 0
    total_cpus             = 0
    total_rams             = 0
    total_dsks             = 0
    total_bill             = 0
    total_bill_distributed = 0
    for row in result:
        # Aqui billeable debe depender del tipo de componente y de si el
        # flag is allways billeable esta encendido, por ahora forzado 
        # para CPU y RAM
        if row.Type not in usage:
            usage.update({
                row.Type:{
                    0:{
                        'hours': 0,
                        'Q_hours': 0,
                        'Q_month': 0,
                        'rate': 0,
                        'rtmf':0,
                        'rate_month':0,
                        'bill':0
                    },
                    1:{
                        'hours': 0,
                        'Q_hours': 0,
                        'Q_month': 0,
                        'rate': 0,
                        'rtmf':0,
                        'rate_month':0,
                        'bill':0
                    }
                }
            })
            if row.Type in ['DSK','IMG','SNP','DRP']:
                usage[row.Type][0].update({
                    'HDD':{
                        'Q_month'    : 0,
                        'rate'       : 0,
                        'rate_month' : 0,
                        'bill'       : 0,
                    },
                    'SSD':{
                        'Q_month'    : 0,
                        'rate'       : 0,
                        'rate_month' : 0,
                        'bill'       : 0,
                    }
                })
                usage[row.Type][1].update({
                    'HDD':{
                        'Q_month'    : 0,
                        'rate'       : 0,
                        'rate_month' : 0,
                        'bill'       : 0,
                    },
                    'SSD':{
                        'Q_month'    : 0,
                        'rate'       : 0,
                        'rate_month' : 0,
                        'bill'       : 0,
                    }
                })
                
        #pprint(usage)
        Active = 1 if row.Active else 0
        #if Active not in usage[row.Type]:
        #    usage[row.Type].update({Active:{}})
        
        billeable = row.Active if row.Type in ('CPU','RAM') else True
        if billeable: billeable_records += 1 
        total_q_hours += row.Q_Hours
        q_month   = float(row.Q_Hours/720)
        total_q_month += q_month
        rate_to_month_factor = 720 if row.Type in ('CPU','RAM') else 1
        if   row.Type == 'CPU': 
            rate = rate_cpu
            total_cpus += 1
        elif row.Type == 'RAM': 
            rate = rate_ram
            total_rams += 1
        else:                   
            rate = rate_dsk
            total_dsks += 1
        logger.debug(f"{this()}: billeable  = {billeable}")
        logger.debug(f"{this()}: q month    = {q_month} {type(q_month)}")
        logger.debug(f"{this()}: rtm factor = {rate_to_month_factor}")
        logger.debug(f"{this()}: rate       = {rate}")
        rate_month = rate * rate_to_month_factor
        logger.debug(f"{this()}: rate month = {rate_month} {type(rate_month)}")
        bill = q_month * rate_month if billeable else 0
        if bill > 0:
            contributing_records += 1        
            total_bill += bill
        logger.debug(f"{this()}: row = h:{row.Hours:6d} a:{row.Active:5} t:{row.Type:3s} qhr={row.Q_Hours:20.12f} qmo={q_month:20.12f} r:{rate:20.12f} rtmf:{rate_to_month_factor:3d} rmo={rate_month:.12f} bill:{bill:8.2f}")
        
        usage[row.Type][Active].update({
            'hours': row.Hours,
            'Q_hours': row.Q_Hours,
            'Q_month': q_month,
            'rate': rate,
            'rtmf':rate_to_month_factor,
            'rate_month':rate_month,
            'bill':bill
        })
        if row.Type in ['DSK','SNP','DRP','IMG']:
            Q_month_hdd = usage[row.Type][Active]['Q_month'] * factor_hdd
            Q_month_ssd = usage[row.Type][Active]['Q_month'] * factor_ssd
            rate_month_hdd = rate_hdd * rate_to_month_factor
            rate_month_ssd = rate_ssd * rate_to_month_factor
            bill_hdd = Q_month_hdd * rate_month_hdd if billeable else 0
            bill_ssd = Q_month_ssd * rate_month_ssd if billeable else 0
            usage[row.Type][Active].update({
                'HDD':{
                    'Q_month'    : Q_month_hdd,
                    'rate'       : rate_hdd,
                    'rate_month' : rate_month_hdd,
                    'bill'       : bill_hdd,
                },
                'SSD':{
                    'Q_month'    : Q_month_ssd,
                    'rate'       : rate_ssd,
                    'rate_month' : rate_month_ssd,
                    'bill'       : bill_ssd,
                }
            })
            bill_distributed = bill_hdd + bill_ssd
            total_bill_distributed += bill_distributed
        else:
            total_bill_distributed += bill

    usage.update({
        'billeable_records'      : billeable_records,
        'contributing_records'   : contributing_records,
        'total_q_hours'          : float(total_q_hours),
        'total_q_month'          : total_q_month,
        'total_cpus'             : total_cpus,
        'total_rams'             : total_rams,
        'total_dsks'             : total_dsks,
        'total_bill'             : total_bill,
        'total_bill_distributed' : total_bill_distributed,
    })

    logger.debug(f"{this()}: billeable   recs = {billeable_records}")
    logger.debug(f"{this()}: contibuting recs = {contributing_records}")
    logger.debug(f"{this()}: total_q_hours    = {total_q_hours}")
    logger.debug(f"{this()}: total_q_month    = {total_q_month}")
    logger.debug(f"{this()}: total_cpus       = {total_cpus}")
    logger.debug(f"{this()}: total_rams       = {total_rams}")
    logger.debug(f"{this()}: total_dsks       = {total_dsks}")
    logger.debug(f"{this()}: total_bill       = {total_bill}")
    return usage
"""

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
    parser.add_argument('-P' ,'--port'         ,help='DB Port',      required=False,default=3306)
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
    cfg = config[os.getenv('COLLECTOR_CONFIG') or 'default']
    logger.debug(f"cfg={cfg}")
    logger.debug(f"cfg type={type(cfg)}")
    logger.debug(f"cfg dir={dir(cfg)}")
    logger.debug(f"COLLECTOR_CONFIG_FILE={cfg.COLLECTOR_CONFIG_FILE}")
    parser = configparser.ConfigParser(
            allow_no_value=False,     # don't allow "key" without "="
            delimiters=('=',),        # inifile "=" between key and value
            comment_prefixes=(';','#'),  # only ';' for comments (fixes #channel)
            inline_comment_prefixes=(';'),     # comments after lines
            interpolation=configparser.ExtendedInterpolation(),
            empty_lines_in_values=False  # empty line means new key
            )
    parser.read(cfg.COLLECTOR_CONFIG_FILE)
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
    
    logger.debug(f"logger={logger}")
    db.logger=logger
    logger.debug(f"db={db} db.logger={db.logger}")
    try:                  
        try:
            if args.verbose > 0: logger.debug(f"connecting to {db}' ...")
            if args.verbose > 0: logger.info("DB connection successful.")
            logger.debug(f'args={args}')            
        except Exception as e:
            logger.error(str(e))
            logger.warning("WARNING: DB connection unsuccessful.")
        if db is not None:
            logger.info(f"Getting resume from {args.start} to {args.end}")
            period = f"{args.start.year}{args.start.month:02d}"
            cits_table = f"Charge_Items_{period}"
            logger.debug(f"Period =  {period}")
            Charge_Items.set_shard(period)
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
            elif args.mode == 'usage':
                logger.info(f"Enter 'usage' mode ...")
                usage = db.Get_Period_Usage(customer_id=args.customer_id,rates=Rates)
                # render template from memory
                #tm = jinja2.Environment().from_string(usage_template)
                #html = tm.render(data=usage)
                # rendering Template from File System
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
            logger.error("DB session couldn't be open.")
    except Exception as e:
        logger.error("EXCEPTION: ",str(e))
        raise e
    logger.info("Execution completed.")
    

