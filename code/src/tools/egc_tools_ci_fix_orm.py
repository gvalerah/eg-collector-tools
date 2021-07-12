# CI Period Fixer
# **********************************************************************
# NO ESTA FUNCIONANDO REVISAR PARA FULL ORM CON SHARDING !!!!!
# **********************************************************************
import logging
import argparse
from pprint                         import pprint
from sqlalchemy                     import create_engine
from emtec                          import *
from emtec.debug                    import *
from emtec.eg_datetime              import *
from emtec.collector.db.orm         import *
from emtec.collector.db.orm_model   import *
from    flask_sqlalchemy                import SQLAlchemy

FORMAT = '%(asctime)-15s %(lineno)s %(levelname)s %(message)s'
logging.basicConfig(format=FORMAT)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
# Lee argumentos de linea de comandos

parser = argparse.ArgumentParser()
parser.add_argument('-ci' , '--ci_id'    , help='CI Id'        ,type=int,required=False)
parser.add_argument('-p'  , '--period', help='Period AAAAMM',type=int,required=False)
parser.add_argument('-H'  , '--host'  , help='DB Host'      ,type=str,default='localhost',required=False)
parser.add_argument('-P'  , '--port'  , help='DB Port'      ,type=int,default=3306,required=False)
parser.add_argument('-U'  , '--username'  , help='DB User'      ,type=str,default='collector',required=False)
parser.add_argument('-W'  , '--password'  , help='DB Password'  ,type=str,default='Password1$',required=False)

args = parser.parse_args()


connection_string=f"mysql+pymysql://{args.username}:{args.password}@{args.host}:{args.port}/collector"
logger.debug(f"connection_string = {connection_string}")
engine=create_engine(connection_string)
logger.debug(f"engine            = {engine}")
Session=sessionmaker(bind=engine)
logger.debug(f"Session           = {Session}")
session=Session()
logger.debug(f"session           = {session}")
logger.debug(f"just loaded class : {Charge_Items}")    
logger.debug(f"__tablename__     : {Charge_Items.__tablename__}")    
logger.debug(f"__table__.name    : {Charge_Items.__table__.name}")   
rows=session.query(Charge_Items).all()
logger.debug(f"rows              = {len(rows)}") 
#result=session.query(Charge_Items,Charge_Units).join(Charge_Units,Charge_Items.CU_Id==Charge_Units.CU_Id).limit(5)
suffix='202107'
new_Table=Charge_Items.set_shard(suffix)
logger.debug(f"New table name    = {new_Table}")
logger.debug(f"__tablename__     = {Charge_Items.__tablename__}")    
logger.debug(f"__table__.name    = {Charge_Items.__table__.name}")    
rows=session.query(Charge_Items).all()
logger.debug(f"rows              = {len(rows)}") 


if __name__ == "__main__":
    logger.debug(f"args = {args}")
    DATA={}
    try:
        CI_Id  = args.ci_id
        period = args.period
        logger.debug(62)
        month  = period%100
        year   = int(period/100)
        logger.debug(f"65 month={month} year={year}")
        suffix = f"{year:04d}{month:02d}"
        logger.debug(f"suffix = {suffix}")
        dt = datetime.datetime(year=year,month=month,day=1)
        start,end = Get_Period(dt)
        logger.debug(f"70 start={start} end={end}")
        Charge_Items.set_shard(suffix)
        logger.debug(f"Charge_Items                = {Charge_Items}")
        logger.debug(f"Charge_Items.__table__.name = {Charge_Items.__table__.name}")
        logger.debug(f"Charge_Items.__tablename__  = {Charge_Items.__tablename__ }")
        
        logger.debug(f"month={month} year={year} start={start} end={end}")
        # use shardened Charge Items here baed on period

        logger.debug(f"start={start} end={end}")
        slices = Get_Slices(start=start,end=end) # Get list of slices in period
        logger.debug(f"slices={len(slices)}")
        logger.debug(f"session             = {session}")
        logger.debug(f"Configuration_Items = {Configuration_Items}")
        CI = session.query(Configuration_Items
            ).filter(Configuration_Items.CI_Id == CI_Id).one()
        logger.debug(f"CI                  = {CI}")
        logger.debug(f"slices              = {len(slices)}")
        
        CUS = session.query(Charge_Units
            ).filter(Charge_Units.CI_Id==CI_Id
            ).all()
        logger.debug(f"CUS={len(CUS)}")
        
        DATA.update({CI_Id:{}})
        for CU in CUS:
            CITS = session.query(Charge_Items
                ).filter(Charge_Items.CU_Id==CU.CU_Id
                ).all()
            logger.debug(f"{CI_Id} {CU.CU_Id} CITS={len(CITS)}")
            if len(CITS):
                cits = {}
                for CIT in CITS:
                    #logger.debug(f"{CIT.get_dict()}")
                    cits.update({
                    datetime.datetime.timestamp(CIT.CIT_DateTime): CIT.get_dict()
                    })
                #print(cits)
                DATA[CI_Id].update({
                    CU.CU_Id:{
                        'CU':CU.get_dict(),
                        'cits':cits
                    }
                })
        print(DATA)
        #sys.exit(1)
        missing_slices = {}
        first = None
        last  = None

        for CI_Id in DATA:
            for CU_Id in DATA.get(CI_Id):
                logger.debug(f"CU_Id={CU_Id}")
                for slice in slices:
                    if CU_Id not in DATA[CI_Id]:
                        DATA[CI_Id].update({CU_Id:{'CU':None,'cits':{}}})
                    slice = datetime.datetime.timestamp(slice)
                    if DATA.get(CI_Id).get(CU_Id).get('cits').get(slice,None) is None:
                        logger.debug(f"missing slice={CI_Id}:{CU_Id}:cits:{slice} {datetime.datetime.fromtimestamp(slice)}")
                        if CI_Id not in missing_slices:
                            missing_slices.update({CI_Id:{}})
                        if CU_Id not in missing_slices[CI_Id]:
                            missing_slices[CI_Id].update({CU_Id:{}})
                        missing_slices[CI_Id][CU_Id].update({
                                slice:{
                                    'previous' : None,
                                    'next'     : None
                                    }
                            })
                    else:
                        pass
                        #if first is None:
                        #    first = CU_Id.get(CU)
                        #last = CU_Id.get(CU)
        #pprint(missing_slices)
    except Exception as e:
        logger.error(f"exception: {str(e)}")

