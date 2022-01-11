# GV System modules
import  sys
import  os
import  getpass
# GV Import logging functions
import  logging
#import  importlib.util
import  configparser
# GV Library modules
from    time                                import strftime
from    time                                import sleep
from    configparser                        import ConfigParser, ExtendedInterpolation
from    pprint                              import pprint
# GV Setting up Application Context
from    flask_sqlalchemy                    import SQLAlchemy
from    sqlalchemy                          import create_engine
# GV Emtec group collector code
# GV Import Emtec Group's modules
from    emtec                               import *
from    emtec.collector.db.orm              import *
from    emtec.common.functions              import *
from    emtec.collector.common.chk_c000001  import *
from    emtec.collector.common.context      import Context
# GV Import actual collectors codes
from    service.collectors.Nutanix_ETL              import Nutanix_ETL_Collector
from    service.collectors.Nutanix_CI_Check         import Nutanix_CI_Check_Collector
from    service.collectors.Nutanix_Image_Load       import Nutanix_Image_Load_Collector
from    service.collectors.Nutanix_Snapshot_Load    import Nutanix_Snapshot_Load_Collector
from    service.collectors.Nutanix_VGroup_Load      import Nutanix_VGroup_Load_Collector
from    service.collectord_exec                     import Execute_Collector_Daemon

# GV ---------------------------------------------------------------------------------------
# GV Daemon functions here

# GV Command line parameters are mandatory

config_file = sys.argv[1]
driver_group = sys.argv[2]

add_Logging_Levels()

COLLECTOR_DRIVER_NAME='Collector for Nutanix'
COLLECTOR_DRIVER=__file__.replace('.pyc','')
COLLECTOR_DRIVER=__file__.replace('.py','')

# GV create logger
logger  = logging.getLogger(COLLECTOR_DRIVER_NAME)
logger.propagate=False
handler=None

db = Collector_ORM_DB()

if (os.path.isfile(config_file)):
    config_ini = configparser.ConfigParser(interpolation=ExtendedInterpolation())
    config_ini.read( config_file )
    handlerType     = config_ini.get(driver_group,'handler_type',fallback='TIME_ROTATING')
    when            = config_ini.get(driver_group,'when',fallback='d')
    interval        = config_ini.getint(driver_group,'interval',fallback=7)
    backupCount     = config_ini.getint(driver_group,'backupCount',fallback=53)
    c000001_seconds = config_ini.getint('General','c000001_seconds',fallback=86400)

    # GV Will work with configuration file
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
        # GV --------------------------------------------------------------
        # GV Overrides default log level for this driver group only
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
        # GV --------------------------------------------------------------
        logger.debug("%s: name        =%s"%(COLLECTOR_DRIVER,name))
        logger.debug("%s: collector   =%s"%(COLLECTOR_DRIVER,collector))
        logger.debug("%s: pool_seconds=%s"%(COLLECTOR_DRIVER,pool_seconds))

        # GV Required to handle multiple collector services in one daemon
        # GV services are serialized 
        if collector is not None:
            collectors=collector.split(',')
        else:
            collectors=[]
        CHEQUEOS = 0

        while True:
            # GV ----------------------------------------------------------
            # GV LICENSE HANDLING MAY BE REMOVED IF CENTRALLY HANDLED
            # GV AT THE COLLECTOR SERVICE MODULE, OR NOT ....
            logger.debug("{COLLECTOR_DRIVER}: checking licence")
            logger.debug("****************************************************")
            CHEQUEOS += 1
            logger.debug(f"VOY A CHEQUEAR LICENCIA CHEQUEO={CHEQUEOS}")
            context={}
            rc=0
            """
            rc=chk_c000001( debug=(logger.level==logging.DEBUG),
                            seconds=c000001_seconds,
                            context=context,
                            silent=True,
                            logger=logger
                            )
            """
            logger.debug(f"{COLLECTOR_DRIVER}: checking licence rc={rc}")
            logger.debug(f"YA CHEQUEE LICENCIA CHEQUEO={CHEQUEOS} rc={rc}")
            logger.debug( "****************************************************")
            # GV ----------------------------------------------------------
            if (log_file_previous != log_file):
                logger.info("%s: Logging to '%s'"%(COLLECTOR_DRIVER,log_file))
                logger.info("*****************************************")
                log_file_previous = log_file
            # GV -------------------------------------------------    
            # GV Will create a new child process to isolate service
            child_pid = os.fork()
            if child_pid == 0:
                try:
                    # GV Child new process instantiated
                    # GV -------------------------------------------------    
                    # GV Check for invalid,unexpected db engine
                    if 'sqlite' in str(C.db):
                        logger.error("DB engine not expected is      : '%s'"%(C.db))
                        logger.error("os.environ['COLLECTOR_CONFIG'] : '%s'"%(os.environ['COLLECTOR_CONFIG']))
                        logger.error("os.environ['DATABASE_URL']     : '%s'"%(os.environ['DATABASE_URL']))
                        break
                    logger.info(f"{COLLECTOR_DRIVER}: collectors '{collectors}'")
                    for collector in collectors:                    
                        logger.info(f"{COLLECTOR_DRIVER}: Executing collector mode '{collector}'")
                        if collector == 'Nutanix_ETL':
                            Execute_Collector_Daemon(C,config_ini,driver_group,Nutanix_ETL_Collector)
                        elif collector == 'Nutanix_CI_Check':
                            Execute_Collector_Daemon(C,config_ini,driver_group,Nutanix_CI_Check_Collector)
                        elif collector == 'Nutanix_Image_Load':
                            Execute_Collector_Daemon(C,config_ini,driver_group,Nutanix_Image_Load_Collector)
                        elif collector == 'Nutanix_Snapshot_Load':
                            Execute_Collector_Daemon(C,config_ini,driver_group,Nutanix_Snapshot_Load_Collector)
                        elif collector == 'Nutanix_VGroup_Load':
                            Execute_Collector_Daemon(C,config_ini,driver_group,Nutanix_VGroup_Load_Collector)
                        else:
                            C.logger.error(f"{COLLECTOR_DRIVER}: Invalid collector name '{collector}'.")
                except Exception as e:
                    C.logger.error(f"{COLLECTOR_DRIVER}: Exception catched during ETL execution.'errno:{e.errno},strerror:{e.strerror},args:{e.args}'")
                    #break
                os._exit(0)
            else:
                # GV --------------------------------------------------
                C.logger.debug(f"{COLLECTOR_DRIVER}: Execution completed @ {strftime('%H:%M:%S')}. Waiting {pool_seconds} seconds ...")
                if logger.level == logging.DEBUG:
                    print(f"{COLLECTOR_DRIVER}: Execution completed @ {strftime('%H:%M:%S')}. Waiting {pool_seconds} seconds ...")
                # GV Parent main loop process continues
                # GV WAIT FOR PROCESS # GV child_pid
                logger.info(f"{COLLECTOR_DRIVER}: Child Process started as pid={child_pid} @ {strftime('%H:%M:%S')}.")
                if logger.level < logging.INFO:
                    print(f"{COLLECTOR_DRIVER}: Child Process started as pid={child_pid} @ {strftime('%H:%M:%S')}.")
                try:
                    # GV WAIT FOR PROCESS # GV child_pid
                    childProcExitInfo = os.wait()
                    signal=childProcExitInfo[1]%256
                    status=int(childProcExitInfo[1]/256)
                    message = f"{COLLECTOR_DRIVER}: Child process %d exited with exit info = %d (signal %d status %d)"%(
                        childProcExitInfo[0],
                        childProcExitInfo[1],
                        signal,
                        status,
                        )
                    logger.info(message)
                    logger.info(f"{COLLECTOR_DRIVER}: Waiting {pool_seconds} seconds ...")
                    print(message)
                    print(f"{COLLECTOR_DRIVER}: Waiting {pool_seconds} seconds ...")
                    sleep(pool_seconds)
                except Exception as e:
                    logger.error(f"{COLLECTOR_DRIVER}:Exception catched while pooling. 'errno:{e.errno},strerror:{e.strerror},args:{e.args}'")
                    break        
        # GV Out of loop service should never get here unless system shutdown
        logger.warning(f"{COLLECTOR_DRIVER} *** Unexpected Deamon Interruption ***")
else:
    # GV Configuration error
    print("ERROR: Configuration file '%s' does not exists. aborting."%config_file)
    print('ERROR: Number of arguments:', len(sys.argv), 'arguments.')
    print('ERROR: Argument List:', str(sys.argv))

print()    
print("ERROR: Collector Deamon FAIL **********************")
print()


