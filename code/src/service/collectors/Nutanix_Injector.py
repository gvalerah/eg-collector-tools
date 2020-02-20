# Import system modules
import os
# Import configuration functions
import configparser
from time                               import strftime
from emtec.collector.common.context     import Context
from emtec.class_etl                    import *
from service.platforms.nutanix_etl_1_0  import Nutanix

def Nutanix_Injector_Collector(C,ini_file):
    C.logger.info("%s: NUTANIX Data Injector: Execution start"%(__name__))
    C.logger.info("%s: Using Configuration file: %s"%(__name__,ini_file))
    
    if (os.path.isfile(ini_file)):    
        config          =   configparser.ConfigParser()    
        config.read(ini_file)
        name            =   config['General']['name']
        active          =   config['General']['active']
        
        if active == 'True':
            N=Nutanix(ini_file,logger=C.logger,db=C.db)  
            # Este json file esta forzado hasta implementar rutina de captura desde plataforma   
            
            # ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
            # OJO EMERGENCIA DEBE ARREGLARSE ESTO
            jsonfilename    =   config['General']['json_file_name']
            C.logger.info("%s: Procesing file = '%s'"%(__name__,jsonfilename))
            N.json_file_name=jsonfilename
            # ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
            
            C.logger.debug ("%s: ETL Logging to '%s'"  % (__name__,C.logger))
            C.logger.debug ("%s: API version    = %d"                              % (__name__,N.API_version)  )  
            C.logger.debug ("%s: JSON file name = %s"                              % (__name__,N.json_file_name)  )  
            if N.ETL_load_json() == ETL_OK:
                N.Transform()
                C.logger.info("%s: ETL json is in '%s' and contains %d entities generating %d tuples"%(__name__,N.json_file_name,len(N.data['entities']),len(N.tuples)))    
                N.ETL_Load()
            else:
                C.logger.error("%s: JSON file '%s' coudn't be loaded"%(__name__,N.json_file_name))                    
        else:
            C.logger.info("%s: Collector Inactive.",(__name__))    
    else:
        C.logger.critical("%s: Configuration file '%s' does not exist."%(__name__,nutanix_ini_file))
    
    C.logger.info("%s: Completed"%(__name__))
