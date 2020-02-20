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
            N=Nutanix(ini_file,C)
            C.logger.debug  ("%s: ETL Logging to '%s' ..."  % (__name__,C.logger) )
            C.logger.warning("%s: API version    = %d"      % (__name__,N.API_version) )  

            N.platform        = int(config['General']['platform'])
            N.cost_center     = int(config['General']['default_cost_center'])
            N.customer        = int(config['General']['default_customer'])
            N.CIT_generation  = int(config['General']['CIT_generation'])

            while N.has_more_data:
                #status=N.ETL_request_data_001(API_version=api_version)
                status=N.Extract(API_version=api_version)
                if status == 200:
                    N.ETL_data_to_tuples()     
                    N.ETL_tuples_to_db()
                else:
                    C.logger.error("%s: got error %d getting data for colector %s"      % (__name__,status,name) )                    
        else:
            C.logger.info("%s: Collector Inactive.",(__name__))                    
    else:
        C.logger.critical("%s: Configuration file '%s' does not exist."             % (__name__,nutanix_ini_file) )

    C.logger.info("%s: Completed"%(__name__))
