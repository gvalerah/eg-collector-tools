# System modules
import  sys
import  os
import  getpass
# Import logging functions
import  logging
#import  importlib.util
import  configparser
# Library modules
from    time                                import strftime
from    time                                import sleep
from    configparser                        import ConfigParser, ExtendedInterpolation
from    pprint                              import pprint
# Setting up Application Context
from    flask_sqlalchemy                    import SQLAlchemy
from    sqlalchemy                          import create_engine
# Emtec group collector code
# Import Emtec Group's modules
from    emtec                               import *
from    emtec.collector.db.orm              import *
from    emtec.collector.common.functions    import *
from    emtec.collector.common.chk_c000001  import *
from    emtec.collector.common.context      import Context
# Import actual collectors codes
from    service.collectors.Nutanix_ETL      import Nutanix_ETL_Collector
from    service.collectors.Nutanix_CI_Check import Nutanix_CI_Check_Collector
from    service.collectord_exec             import Execute_Collector_Daemon

# ---------------------------------------------------------------------------------------
# Daemon functions here

# Command line parameters are mandatory

config_file = sys.argv[1]
driver_group = sys.argv[2]

add_Logging_Levels()

COLLECTOR_DRIVER_NAME='Collector for Nutanix'
COLLECTOR_DRIVER=__file__.replace('.pyc','')
COLLECTOR_DRIVER=__file__.replace('.py','')

# create logger
logger  = logging.getLogger(COLLECTOR_DRIVER_NAME)
logger.propagate=False
handler=None

db = Collector_ORM_DB()

if (os.path.isfile(config_file)):
    config_ini = configparser.ConfigParser(interpolation=ExtendedInterpolation())
    config_ini.read( config_file )
    handlerType=config_ini.get(driver_group,'handler_type',fallback='TIME_ROTATING')
    when=config_ini.get(driver_group,'when',fallback='d')
    interval=config_ini.getint(driver_group,'interval',fallback=7)
    backupCount=config_ini.getint(driver_group,'backupCount',fallback=53)
    c000001_seconds=config_ini.getint('General','c000001_seconds',fallback=86400)

    # Will work with configuration file
    C = Context(app_name="Collector for Nutanix",app_ini_file=config_file,logger=logger)    
    C.Set()
    C.db=db
    C.db.logger=logger
    logger.name=driver_group    
    logger.setLevel(C.log_level)
    logger.propagate=True
    config_name=os.getenv('COLLECTOR_CONFIG') or 'default'
    app     = create_minimal_app(config_file,config_name,db=db,logger=logger)
    app_ctx = app.app_context()
    app_ctx.push()    

    if driver_group in config_ini.sections():
        driver_name = config_ini.get(driver_group,'name',fallback=None)
    
    if (C):
        handler,log_file = Reset_Log_File_Name(
                        logger=logger,
                        folder=C.log_folder,
                        nameFormat="%s.log"%driver_group.replace(' ','_'),
                        level=C.log_level,
                        handler=handler,
                        handlerType=handlerType,
                        when=when,
                        interval=interval,
                        backupCount=backupCount
                        )
        logger.info("****** Daemon Start *********************")
        logger.info("%s: as '%s' Using configuration: '%s'"%(COLLECTOR_DRIVER,getpass.getuser(),config_file))
        logger.info("*****************************************")
        log_file_previous = None
        name            = config_ini.get(driver_group,'name',fallback=None)
        collector       = config_ini.get(driver_group,'collector',fallback=None)
        pool_seconds    = config_ini.getint(driver_group,'pool_seconds',fallback=C.pool_seconds)
        # --------------------------------------------------------------
        # Overrides default log level for this driver group only
        log_level       = config_ini.get(driver_group,'log_level',fallback=C.log_level)        
        logger.info("%s: log level from config is  =%s"%(COLLECTOR_DRIVER,log_level))
        if type(log_level) == str:
            log_level=log_level.lower()
            if      log_level == 'debug':       log_level=logging.DEBUG
            elif    log_level == 'information': log_level=logging.INFO
            elif    log_level == 'error':       log_level=logging.ERROR
            elif    log_level == 'warning':     log_level=logging.WARNING
            elif    log_level == 'critical':    log_level=logging.CRITICAL
            elif    log_level == 'fatal':       log_level=logging.FATAL
            else:                               log_level=C.log_level
        logger.setLevel(log_level)
        logger.info("%s: driver %s log level set to =%s"%(COLLECTOR_DRIVER,name,logger.level))
        logger.info("%s: driver %s log level set to =%s"%(COLLECTOR_DRIVER,name,logger.getEffectiveLevel()))
        logger.info("%s: driver %s logger           =%s"%(COLLECTOR_DRIVER,name,logger))
        # --------------------------------------------------------------
        logger.debug("%s: name        =%s"%(COLLECTOR_DRIVER,name))
        logger.debug("%s: collector   =%s"%(COLLECTOR_DRIVER,collector))
        logger.debug("%s: pool_seconds=%s"%(COLLECTOR_DRIVER,pool_seconds))

        # Required to handle multiple collector services in one daemon
        # services are serialized 
        collectors=collector.split(',')

        CHEQUEOS = 0

        while True:
            logger.debug("%s: checking licence"%(COLLECTOR_DRIVER))
            logger.debug("****************************************************")
            CHEQUEOS += 1
            logger.debug("VOY A CHEQUEAR LICENCIA CHEQUEO=",CHEQUEOS)
            context={}
            rc=chk_c000001(debug=(logger.level==logging.DEBUG),seconds=c000001_seconds,context=context,silent=True,logger=logger)
            logger.debug("%s: checking licence rc=%s"%(COLLECTOR_DRIVER,rc))
            logger.debug("YA CHEQUEE LICENCIA CHEQUEO=",CHEQUEOS,"rc=",rc)
            logger.debug("****************************************************")
            if (log_file_previous != log_file):
                logger.info("%s: Logging to '%s'"%(COLLECTOR_DRIVER,log_file))
                logger.info("*****************************************")
                log_file_previous = log_file
            # -------------------------------------------------    
            try:
                if 'sqlite' in str(C.db):
                    logger.error("DB engine not expected is      : '%s'"%(C.db))
                    logger.error("os.environ['COLLECTOR_CONFIG'] : '%s'"%(os.environ['COLLECTOR_CONFIG']))
                    logger.error("os.environ['DATABASE_URL']     : '%s'"%(os.environ['DATABASE_URL']))
                    break
                for collector in collectors:                    
                    logger.info("%s: Executing collector mode '%s'"%(COLLECTOR_DRIVER,collector))
                    if collector == 'Nutanix_ETL':
                        Execute_Collector_Daemon(C,config_ini,driver_group,Nutanix_ETL_Collector)
                    elif collector == 'Nutanix_CI_Check':
                        Execute_Collector_Daemon(C,config_ini,driver_group,Nutanix_CI_Check_Collector)
                    else:
                        C.logger.error("%s: Invalid collector name '%s'."%(COLLECTOR_DRIVER, collector))
            except Exception as e:
                C.logger.error("%s: Exception catched during ETL execution.'errno:%s,strerror:%s,args:%s'"%(COLLECTOR_DRIVER,e.errno,e.strerror,e.args))
                break
            # --------------------------------------------------
            C.logger.debug("%s: Execution completed @ %s. Waiting %d seconds ..."%(COLLECTOR_DRIVER,strftime("%H:%M:%S"),pool_seconds))
            if logger.level == logging.DEBUG:
                print("%s: Execution completed @ %s. Waiting %d seconds ..."%(COLLECTOR_DRIVER,strftime("%H:%M:%S"),pool_seconds))
            try:
                sleep(pool_seconds)
            except Exception as e:
                logger.error("Exception catched while pooling. 'errno:%s,strerror:%s,args:%s'"%(COLLECTOR_DRIVER,e.errno,e.strerror,e.args))
                break        
        # Out of loop service should never get here unless system shutdown
        logger.warning("*** Unexpected Deamon Interruption ***")
else:
    # Configuration error
    print("ERROR: Configuration file '%s' does not exists. aborting."%config_file)
    print('ERROR: Number of arguments:', len(sys.argv), 'arguments.')
    print('ERROR: Argument List:', str(sys.argv))

print()    
print("ERROR: Collector Deamon FAIL **********************")
print()


