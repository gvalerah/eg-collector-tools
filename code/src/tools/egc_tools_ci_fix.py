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
from    flask                               import Flask

FORMAT = '%(asctime)-15s %(levelname)s %(message)s'
logging.basicConfig(format=FORMAT)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
# Lee argumentos de linea de comandos

parser = argparse.ArgumentParser()
parser.add_argument('-ci' , '--ci_id'    , help='CI Id'        ,type=int,required=False)
parser.add_argument('-p'  , '--period', help='Period AAAAMM',type=int,required=False)
parser.add_argument('-H'  , '--host'  , help='DB Host'      ,type=str,default='localhost',required=False)
parser.add_argument('-P'  , '--port'  , help='DB Port'      ,type=int,default=3306,required=False)
parser.add_argument('-U'  , '--username'  , help='DB User'      ,type=str,default='root',required=False)
parser.add_argument('-W'  , '--password'  , help='DB Password'  ,type=str,default='36MMySQLr00t1.,',required=False)

args = parser.parse_args()

app = Flask(__name__)
db = Collector_ORM_DB(
        rdbms    = 'mysql',
        dialect  = 'pymysql',
        host     = args.host,
        port     = args.port,
        user     = args.username,
        password = args.password,
        instance = 'collector'
        )

db.init_app(app)
db.sharding=True
#db.set_sharding_cit('202107')
db.session=db.Session()

#cs=f"mysql+pymysql://{args.username}:{args.password}@{args.host}:{args.port}/collector"
#db=create_engine(cs)
#SessionMaker = sessionmaker(bind=db)
#session = SessionMaker()

logger.debug(f"db                         = {db}")
#logger.debug(f"Charge_Items               = {Charge_Items}")
#logger.debug(f"Charge_Items.__name__      = {Charge_Items.__name__}")
#logger.debug(f"Charge_Items.__tablename__ = {Charge_Items.__tablename__}")

if __name__ == "__main__":
    logger.debug(f"args = {args}")
    try:
        CI_Id  = args.ci_id
        period = args.period
        db.sharding=True
        
        month  = period%100
        year   = int(period/100)
        suffix = f"{year:04d}{month:02d}"
        logger.debug(f"suffix = {suffix}")
        #db.set_sharding_cit(suffix)
        dt = datetime.datetime(year=year,month=month,day=1)
        start,end = Get_Period(dt)
        
        Charge_Items.set_shard(suffix)
        #Charge_Items.__table__.name= f"Charge_Items_{args.period}"
        #Charge_Items.__tablename__ = f"Charge_Items_{args.period}"
        logger.debug(f"Charge_Items                = {Charge_Items}")
        logger.debug(f"Charge_Items.__table__.name = {Charge_Items.__table__.name}")
        logger.debug(f"Charge_Items.__tablename__  = {Charge_Items.__tablename__ }")
        
        logger.debug(f"month={month} year={year} start={start} end={end}")
        # use shardened Charge Items here baed on period

        logger.debug(f"start={start} end={end}")
        slices = Get_Slices(start=start,end=end) # Get list of slices in period
        logger.debug(f"slices={len(slices)}")
        logger.debug(f"db                  = {db}")
        logger.debug(f"db.session          = {db.session}")
        logger.debug(f"Configuration_Items = {Configuration_Items}")
        CI = db.session.query(Configuration_Items
            ).filter(Configuration_Items.CI_Id == CI_Id).one()
        logger.debug(f"CI                  = {CI}")
        logger.debug(f"slices              = {len(slices)}")

        CUS = session.query(Charge_Units
            ).filter(Charge_Units.CI_Id==CI_Id
            ).all()
        logger.debug(f"CUS={len(CUS)}")
        DATA={}
        for CU in CUS:
            #logger.debug(f"CU={CU}")
            # Get actual CITS for this CU
            CITS = session.query(Charge_Items
                ).filter(Charge_Items.CU_Id==CU.CU_Id
                ).all()
            logger.debug(f"{CI_Id} {CU.CU_Id} CITS={len(CITS)}")
            if len(CITS):
                cits = {}
                for CIT in CITS:
                    cits.update({
                    CIT.DateTime: CIT.as_dict()
                    })
                DATA[CI_Id].update({
                    CU.CU_Id:{
                        'CU':CU.as_dict(),
                        CITS:cits
                    }
                })
        print(92)
        pprint(DATA)
        missing_slices = {}
        first = None
        last  = None

        for CI_Id in DATA:
            for CU_Id in CI:
                for slice in slices:
                    if CU_Id.get(slice,None) is None:
                        missing_slices.update({
                            CU_Id:{
                                slice:{
                                    previous : None,
                                    next     : None
                                    }
                                }
                            })
                    else:
                        if first is None:
                            first = CU_Id.get(CU)
                        last = CU_Id.get(CU)
        pprint(missing_slices)
    except Exception as e:
        logger.error(f"exception: {str(e)}")

