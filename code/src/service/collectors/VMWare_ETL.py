import os
# Import configuration functions
import configparser
from time                           import strftime
# GV 20190819
#from app.common.context             import Context
from emtec.collector.common.context             import Context
from service.platforms.vmware_etl   import VMWare

def VMWare_ETL_Collector(C,ini_file):
    C.logger.info("%s: VMWare Platform Collector: Execution start"%(__name__))
    C.logger.info("%s: Using Configuration file: %s"%(__name__,ini_file))

    good_bye_message=''
    
    if (os.path.isfile(ini_file)):    
        config          =   configparser.ConfigParser()    
        config.read(ini_file)
        name            =   config['General']['name']
        api_version     =   int(config['General']['api_version'])
        active          =   config['General']['active']
        if active == 'True':
            # GV 20190819
            VMW=VMWare(ini_file,logger=C.logger,db=C.db)
            VMW.logger=C.logger
            C.logger.debug("%s: %s logging to '%s' ..."  % (__name__,name,C.logger) )
            C.logger.debug("%s: API version    = %d"      % (__name__,VMW.API_version) )  

            VMW.platform        = config.getint('General','platform',fallback=1)
            VMW.cost_center     = config.getint('General','default_cost_center',fallback=1)
            VMW.customer        = config.getint('General','default_customer',fallback=1)
            VMW.CIT_generation  = config.getint('General','CIT_generation',fallback=1)
            VMW.chunk_size      = config.getint('General','chunk_size',fallback=100)
            
            C.logger.debug("%s: will enter loop has more data = %s"      % (__name__,VMW.has_more_data) )  
            
            while VMW.has_more_data:
                C.logger.debug("%s: in loop has more data = %s total=%d processed=%d"      % (__name__,VMW.has_more_data,VMW.total_matches,VMW.processed_vms) )  
                status=VMW.Extract(API_version=api_version)
                if status is not None and status == 200:
                    VMW.Transform()     
                    VMW.ETL_Load()
                else:
                    C.logger.error("%s: got error %s getting data for collector: '%s'"      % (__name__,status,name) )                    
                    VMW.has_more_data = False
            C.logger.debug("%s: out loop has more data = %s total=%d processed=%d"      % (__name__,VMW.has_more_data,VMW.total_matches,VMW.processed_vms) ) 
            good_bye_message=" %d entities processed out of %d matched in platform '%s'."%(VMW.processed_vms,VMW.total_matches,name)
        else:
            C.logger.info("%s: Collector Inactive.",(__name__))                    
    else:
        C.logger.critical("%s: Configuration file '%s' does not exist."             % (__name__,ini_file) )

    C.logger.info("%s: Completed.%s"%(__name__,good_bye_message))
