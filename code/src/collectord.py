# System modules
import sys
import os
import getpass

# Library modules
from time import strftime
from time import sleep

# Import logging functions
import logging
#logging.StreamHandler(stream=None)

# GV 20190819
#from app.common.functions      import *
from emtec                              import *   
from emtec.collector.common.functions   import *

# Import App Modules

dir_path = os.path.dirname(os.path.realpath(__file__))
cwd = os.getcwd()

# GV 20190819
#from app.common.context          import Context
from emtec.collector.common.context          import Context
from service.collectord_exec import Execute_Collector_Daemon

# GV 20190924 DB FORCE HERE
from sqlalchemy import create_engine


# ---------------------------------------------------------------------------------------
# Daemon functions here

# 'application' code

if (len(sys.argv) > 1):
    config_file = sys.argv[1]
else:
    config_file = "collector.ini"

add_Logging_Levels()

# create logger
logger  = logging.getLogger('Collector Daemon')
logger.propagate=False


# Setting up Application Context

from    flask_sqlalchemy            import SQLAlchemy
from    config                      import config
from    emtec                       import *
from    emtec.collector.db.orm      import *

db                                  = Collector_ORM_DB()


fh=None
if (os.path.isfile(config_file)):

    # Will work with configuration file
    C = Context(app_name="Collector Daemon",app_ini_file=config_file,logger=logger)
    
    C.Set()
    C.db=db
    C.db.logger=logger
    logger.name="Collector Daemon"    
    logger.setLevel(C.log_level)
    #if logger.level == DEBUG:
    logger.propagate=True
    # App Context required code
    config_name=os.getenv('COLLECTOR_CONFIG') or 'default'
    app     = create_minimal_app(config,config_name,db=db,logger=logger)
    app_ctx = app.app_context()
    app_ctx.push()    
    
    if (C):
        fh,log_file = Reset_Log_File_Name(logger,C.log_folder,C.log_format,log_level=C.log_level,fh=fh)
        logger.info("****** Daemon Start *********************")
        logger.info("%s: as '%s' Using configuration: '%s'"%(sys.argv[0],getpass.getuser(),config_file))
        logger.info("*****************************************")
        log_file_previous = None
        while True:
            # Be Sure Log file changes @ change of day
            fh,log_file = Reset_Log_File_Name(logger,C.log_folder,C.log_format,log_level=C.log_level,fh=fh)
            if (log_file_previous != log_file):
                logger.info("%s: Logging to '%s'"%(sys.argv[0],log_file))
                logger.info("*****************************************")
                log_file_previous = log_file
            # -------------------------------------------------    
            try:
                Execute_Collector_Daemon(C)
            except Exception as e:
                C.logger.error("%s: Exception catched during ETL execution.'errno:%s,strerror:%s,args:%s'"%(sys.argv[0],e.errno,e.strerror,e.args))
                break
            # --------------------------------------------------
            C.logger.debug("%s: Execution completed @ %s. Waiting %d seconds ..."%(sys.argv[0],strftime("%H:%M:%S"),C.pool_seconds))
            if logger.level == logging.DEBUG:
                print("%s: Execution completed @ %s. Waiting %d seconds ..."%(sys.argv[0],strftime("%H:%M:%S"),C.pool_seconds))
            try:
                sleep(C.pool_seconds)
            except Exception as e:
                logger.error("Exception catched while pooling. 'errno:%s,strerror:%s,args:%s'"%(sys.argv[0],e.errno,e.strerror,e.args))
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


