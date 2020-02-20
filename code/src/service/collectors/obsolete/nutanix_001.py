import os
# Import configuration functions
import configparser
from time                       import strftime
from app.common.context         import Context
from service.plugins.nutanix.etl_1_0    import Nutanix

def Nutanix_001_Collector(C,ini_file):
    C.logger.info("%s: NUTANIX Data Injector: Execution start"%(__name__))
    C.logger.info("%s: Using Configuration file: %s"%(__name__,ini_file))
    
    if (os.path.isfile(ini_file)):    
        config          =   configparser.ConfigParser()    
        config.read(ini_file)
        name            =   config['General']['name']
        active          =   config['General']['active']
        
        if active == 'True':
            N=Nutanix(ini_file,C)  
            nutanix_sql_file = strftime("service/sql/%Y%m%d_injector.sql")
            N.ETL_Set_SQL_Output_File(nutanix_sql_file)
            # Este json file esta forzado hasta implementar rutina de captura desde plataforma   
            file            =   config['General']['json_file_name']
            C.logger.info("%s: Procesing file = '%s'"%(__name__,file))
            N.json_file_name=file
            C.logger.debug  ("%s: ETL Logging to '%s' (%s) and saving SQL in '%s'"  % (__name__,C.L.Get_File_Name(),C.L.Get_Level_Name(),N.sql_file))
            C.logger.warning("%s: API version    = %d"                              % (__name__,N.API_version)  )  
            C.logger.warning("%s: JSON file name = %s"                              % (__name__,N.json_file_name)  )  
            N.ETL_load_json()
            N.ETL_data_to_tuples()
            C.logger.info("%s: ETL json is in '%s' and contains %d entities generating %d tuples"%(__name__,N.json_file_name,len(N.data['entities']),len(N.tuples)))    
            N.ETL_tuples_to_db()
        else:
            C.logger.info("%s: Collector Inactive.",(__name__))    
    else:
        C.logger.critical("%s: Configuration file '%s' does not exist."%(__name__,nutanix_ini_file))
    
    C.logger.info("%s: Completed"%(__name__))
