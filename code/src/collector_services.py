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
# GV 20210408 from    emtec.collector.common.functions    import *
from    emtec.common.functions              import *
from    emtec.collector.common.context      import Context
# Import actual collectors codes
from    service.collectors.Monthly_Auto     import Monthly_Auto_Collector
from    service.collectors.Auto_CC          import Auto_CC_Collector
from    service.collectors.Fill_CU_Rates    import Fill_CU_Rates_Collector
from    service.collectord_exec             import Execute_Collector_Daemon

# ---------------------------------------------------------------------------------------
# Daemon functions here

# Command line parameters are mandatory

config_file = sys.argv[1]
driver_group = sys.argv[2]

add_Logging_Levels()

# create logger
logger           = logging.getLogger('Collector Services')
logger.propagate = False
handler          = None

db = Collector_ORM_DB()

if (os.path.isfile(config_file)):
    config_ini = configparser.ConfigParser(interpolation=ExtendedInterpolation())
    config_ini.read( config_file )
    # Forced production environment configuration
    # from config_ini file
    handlerType=config_ini.get(driver_group,'handler_type',fallback='TIME_ROTATING')
    when=config_ini.get(driver_group,'when',fallback='d')
    interval=config_ini.getint(driver_group,'interval',fallback=7)
    backupCount=config_ini.getint(driver_group,'backupCount',fallback=53)
            
    # Will work with configuration file
    C = Context(app_name="Collector Services",app_ini_file=config_file,logger=logger)    
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
        driver_name = config_ini.get(driver_group,'name',fallback=driver_group)
    
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
        log_file_previous = None
        name            = config_ini.get   (driver_group,'name'        ,fallback=driver_group)
        collector       = config_ini.get   (driver_group,'collector'   ,fallback=None)
        pool_seconds    = config_ini.getint(driver_group,'pool_seconds',fallback=C.pool_seconds)
        logger.info(f"{name}: ****** Daemon Start *********************")
        logger.info(f"{name}: as '{getpass.getuser()}' Using configuration: '{config_file}'")
        logger.info(f"{name}: *****************************************")
        # --------------------------------------------------------------
        # Overrides default log level for this driver group only
        log_level       = config_ini.get(driver_group,'log_level',fallback=C.log_level)        
        logger.info(f"{name}: log level from config is  = {log_level}")
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
        logger.info(f"{name}: driver {name} log level set to           = {logger.level}")
        logger.info(f"{name}: driver {name} log effective level set to = {logger.getEffectiveLevel()}")
        logger.info(f"{name}: driver {name} logger                     = {logger}")
        # --------------------------------------------------------------
        logger.debug(f"{name}: name         = {name}")
        logger.debug(f"{name}: collector    = {collector}")
        logger.debug(f"{name}: pool_seconds = {pool_seconds}")

        # Required to handle multiple collector services in one daemon
        # services are serialized 
        collectors=collector.split(',')
        while True:
            # Check for propper log file for this iteration
            if (log_file_previous != log_file):
                logger.info(f"{name}: Logging to '{log_file}'")
                logger.info(f"{name}: *****************************************")
                log_file_previous = log_file
            # Will create a new child process to isolate service
            child_pid = os.fork()
            if child_pid == 0:
                # Child new process instantiated
                # -------------------------------------------------    
                try:
                    if 'sqlite' in str(C.db):
                        logger.error(f"{name}: DB engine not expected is      : '{C.db}'")
                        logger.error(f"{name}: os.environ['COLLECTOR_CONFIG'] : '{os.environ['COLLECTOR_CONFIG']}'")
                        logger.error(f"{name}: os.environ['DATABASE_URL']     : '{os.environ['DATABASE_URL']}'")
                        break
                    for collector in collectors:
                        logger.info(f"{name}: Executing collector mode '{collector}'")
                        if collector == 'Monthly_Auto':
                            Execute_Collector_Daemon(C,config_ini,driver_group,Monthly_Auto_Collector)
                        elif collector == 'Auto_CC':
                            Execute_Collector_Daemon(C,config_ini,driver_group,Auto_CC_Collector)
                        elif collector == 'Fill_CU_Rates':
                            Execute_Collector_Daemon(C,config_ini,driver_group,Fill_CU_Rates_Collector)
                        else:
                            C.logger.error(f"{name}: Invalid collector name '{collector}'.")
                except Exception as e:
                    C.logger.error(f"{name}: Exception catched during ETL execution.'errno:{e.errno},strerror:{e.strerror},args:{e.args}'")
                    #break
                os._exit(0)
                # --------------------------------------------------
                C.logger.debug(f"{name}: Execution completed @ {strftime('%H:%M:%S')}. Waiting {pool_seconds} seconds ...")
            else:
                # Parent main loop process continues
                # WAIT FOR PROCESS # child_pid
                logger.info(f"{name}: Child Process started as pid={child_pid} @ {strftime('%H:%M:%S')}.")
                if logger.level < logging.INFO:
                    print(f"{name}: Child Process started as pid={child_pid} @ {strftime('%H:%M:%S')}.")
                try:
                    # WAIT FOR PROCESS # child_pid
                    childProcExitInfo = os.wait()
                    print(f"{name}: Child process %d exited with status %d %d"%(
                        childProcExitInfo[0],
                        childProcExitInfo[1],
                        int(childProcExitInfo[1]/256)
                        ))
                    print(f"{name}: Waiting {pool_seconds} seconds ...")
                    sleep(pool_seconds)
                except Exception as e:
                    logger.error(f"{name}: Exception catched while pooling. 'errno:{e.errno},strerror:{e.strerror},args:{e.args}'")
                    break        
        # Out of loop service should never get here unless system shutdown
        logger.warning(f"{name}: *** Unexpected Deamon Interruption ***")
else:
    # Configuration error
    print(f"{sys.argv[0]}: ERROR: Configuration file '{config_file}' does not exists. aborting.")
    print(f"{sys.argv[0]}: ERROR: Number of arguments: {len(sys.argv)} arguments.")
    print(f"{sys.argv[0]}: ERROR: Argument List: {str(sys.argv)}")

print()    
print(f"{sys.argv[0]}: ERROR: Collector Deamon FAIL **********************")
print()


