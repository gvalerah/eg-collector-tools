import os
# Import configuration functions
import configparser
from time                       import strftime
from app.common.context         import Context
from service.platforms.nutanix_etl_1_0    import Nutanix

def Nutanix_000_Collector(C,ini_file):
    C.logger.info("%s: NUTANIX Platform Collector: Execution start"%(__name__))
    C.logger.info("%s: Using Configuration file: %s"%(__name__,ini_file))

    if (os.path.isfile(ini_file)):    
        config          =   configparser.ConfigParser()    
        config.read(ini_file)
        name            =   config['General']['name']
        api_version     =   int(config['General']['api_version'])
        active          =   config['General']['active']
        if active == 'True':
            N=Nutanix(ini_file,C.logger,C.db)
            C.logger.warning  ("%s: ETL Logging to '%s' ..."  % (__name__,C.logger) )
            C.logger.warning("%s: API version    = %d"      % (__name__,N.API_version) )  

            N.platform        = config.getint('General','platform',fallback=1)
            N.cost_center     = config.getint('General','default_cost_center',fallback=1)
            N.customer        = config.getint('General','default_customer',fallback=1)
            N.CIT_generation  = config.getint('General','CIT_generation',fallback=1)
            N.chunk_size      = config.getint('General','chunk_size',fallback=100)
            C.logger.warning("%s: will enter loop has more data = %s"      % (__name__,N.has_more_data) )  
            while N.has_more_data:
                C.logger.warning("%s: in loop has more data = %s total=%d processed=%d"      % (__name__,N.has_more_data,N.total_matches,N.processed_vms) )  
                #status=N.ETL_request_data_001(API_version=api_version)
                status=N.Extract(API_version=api_version)
                if status == 200:
                    N.Transform()     
                    N.ETL_Load()
                else:
                    C.logger.error("%s: got error %d getting data for colector %s"      % (__name__,status,name) )                    
            C.logger.warning("%s: out loop has more data = %s total=%d processed=%d"      % (__name__,N.has_more_data,N.total_matches,N.processed_vms) )  
        else:
            C.logger.info("%s: Collector Inactive.",(__name__))                    
    else:
        C.logger.critical("%s: Configuration file '%s' does not exist."             % (__name__,nutanix_ini_file) )

    C.logger.info("%s: Completed"%(__name__))
