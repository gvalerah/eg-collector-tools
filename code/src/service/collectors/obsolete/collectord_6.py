import os
# Import configuration functions
import configparser
from time                       import strftime
from app.common.context         import Context
from service.plugins.nutanix.nutanix_etl_1_0    import Nutanix

def Collector_6(C,ini_file):
    C.logger.info ("%s: Collector data Injector NUTANIX 2: Execution start"%(__name__))

    if (os.path.isfile(ini_file)):    
    
        config          =   configparser.ConfigParser()    
        config.read(ini_file)
        name            =   config['General']['name']
        active          =   config['General']['active']
        
        if active:
            N=Nutanix(ini_file,logger=C.logger,db=C.db)  
            
            # Este json file esta forzado hasta implementar rutina de captura desde plataforma   
            file            =   config['General']['json_file_name']
            C.logger.info("%s: Procesing file = '%s'"%(__name__,file))
            N.json_file_name=file
            C.logger.debug("%s: ETL Logging to '%s' and saving SQL in '%s'"  % (__name__,C.logger,N.sql_file))
            C.logger.debug("%s: API version    = %s"                         % (__name__,N.API_version)  )  
            C.logger.debug("%s: JSON file name = %s"                         % (__name__,N.json_file_name)  )  
            # N.Extract
            N.ETL_load_json()
            N.Transform()
            C.logger.info("%s: ETL json is in '%s' and contains %d entities generating %d tuples"%(__name__,N.json_file_name,len(N.data['entities']),len(N.tuples)))    
            N.ETL_Load()
        else:
            C.logger.info("%s: Collector Inactive.",(__name__))    
    else:
        C.logger.critical("%s: Configuration file '%s' does not exist."%(__name__,nutanix_ini_file))
    
    C.logger.info("%s: Completed"%(__name__))
