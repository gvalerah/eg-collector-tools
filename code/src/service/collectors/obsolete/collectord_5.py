
import os
import calendar
# Import configuration functions
import configparser

from sqlalchemy                 import create_engine
from sqlalchemy.orm             import sessionmaker

from .orm_models                import Configuration_Items
from .orm_models                import Platforms

from time                       import strftime

from app.common.context         import Context
from service.plugins.nutanix.etl_1_0    import Nutanix

def Collector_5(C,ini_file):
    C.logger.info("%s: Nutanix Check for CI Commissioning: Execution start"%(__name__))
    
    if (os.path.isfile(ini_file)):    
        config          =   configparser.ConfigParser()
        
        config.read(ini_file)
        
        # Dealing with time data
              
        name            =   config['General']['name']
        platform        =   config.getint('General','platform')
        active          =   config.getboolean('General','active')
        
        if active:
            # NUTANIX STUFF: Get VM List 
            N=Nutanix(ini_file,C)
            C.logger.warning("%s: API version    = %d"                              % (__name__,N.API_version) )  

            # Codigo temporal de prueba carga los datos desde jason ---->
            file            =   config['General']['json_file_name']
            C.logger.info("%s: Procesing file = '%s'"%(__name__,file))
            N.json_file_name=file
            C.logger.warning("%s: API version    = %d"                              % (__name__,N.API_version)  )  
            C.logger.warning("%s: JSON file name = %s"                              % (__name__,N.json_file_name)  )  
            N.ETL_load_json()
            vm_list=N.ETL_get_vm_list()

            print("%s: %d Configuration Items in vm_list'."%(__name__,len(vm_list)))
            # <----

            """ Codigo real debe ser activado al tener laboratorio de prueba
            
            status=N.ETL_request_data_001(API_version=api_version)

            if status == 200:
                N.ETL_get_vm_list(self):
            else:
                C.logger.error("%s: got error %d getting data for colector %s"      % (__name__,status,name) )                    

            """       
            Session = sessionmaker(bind=C.db)
            session = Session()

            #rows = session.query(Configuration_Items).filter(Configuration_Items.Pla_Id == Pla_Id)
        
            # for every C.U. in DB that has CIT_Generation marked as "Monthly" (3)
            # for every C.U. asociated to de monthly CI
            CIs_searched        =   0
            CIs_decommissioned  =   0
            platform_name = session.query(Platforms.Pla_Name).filter(Platforms.Pla_Id==platform).first()
            
            for CI in session.query(Configuration_Items).filter(Configuration_Items.Pla_Id == platform): # Generates Monthly Items Only
                C.logger.debug("%s: CI=%s",(__name__,CI))
                # For each execution Daemon tries to create/update a monthly C.IT record, for the first day of the month at noon
                # Id, Date, Time, Quantity, Status=1 Created, Is_Active=1=True, DateTime=Date+Time
                CI_no_longer_exists=True
                for vm in vm_list:
                    if CI.CI_Name == vm['name']:
                        CI_no_longer_exists = False
                        break

                # Actual check in platform Nutanix goes here
                CIs_searched    +=   1
                if CI_no_longer_exists:
                    C.logger.audit("%s:OLD:%s"%(name,CI))
                    date_time                   =   strftime("%Y-%m-%d %H:%M:%S")
                    CI.CI_Decommissioning_DateTime =   date_time
                    session.merge(CI)
                    #Debe ser AUDIT
                    C.logger.audit("%s:UPD:%s"%(name,CI))
                    CIs_decommissioned  +=  1
            session.commit()
            session.close()  
            C.logger.info("%s: %d Configuration Items searched in platform '%s'."%(__name__,CIs_searched,platform_name[0]))
            C.logger.info("%s: %d Configuration Items decommissioned from platform '%s' detected."%(__name__,CIs_decommissioned,platform_name[0]))
        else:
            C.logger.info("%s: Collector Inactive."%(__name__))        
    else:
        C.logger.critical("%s: Configuration file '%s' does not exist."%(__name__,nutanix_ini_file))
    C.logger.info("%s: Nutanix Check for CI Commissioning: Completed"%(__name__))

