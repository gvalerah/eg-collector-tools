
import os
from time                               import strftime
import calendar
# Import configuration functions
import configparser

from sqlalchemy                         import create_engine
from sqlalchemy.orm                     import sessionmaker

from emtec.collector.db.orm_model       import Configuration_Items
from emtec.collector.db.orm_model       import Platforms


from emtec.collector.common.context     import Context
from service.platforms.nutanix_etl_1_0  import Nutanix

def Nutanix_CI_Check_Collector(C,config,group):

    C.logger.info("%s: Nutanix Check for CI Commissioning: Execution start"%(__name__))
    if True:    
                      
        name            =   config[group]['name']
        platform        =   config.getint(group,'platform')
        active          =   config.getboolean(group,'active')
        
        if active:
            # NUTANIX STUFF: Get VM List 
            N=Nutanix(config,group,logger=C.logger,db=C.db)

            C.logger.debug("%s: API version    = %d"                              % (__name__,N.API_version) )  

            retcode=N.Extract(API_version=N.API_version)
            if retcode is not None and retcode==200:
                vm_list=N.get_vm_list()
    
                CIs_searched        =   0
                CIs_decommissioned  =   0
                platform_name = C.db.session.query(Platforms.Pla_Name).filter(Platforms.Pla_Id==platform).first()
                
                for CI in C.db.session.query(Configuration_Items).filter(Configuration_Items.Pla_Id == platform): # Generates Monthly Items Only
                    C.logger.debug("%s: CI=%s"%(__name__,CI))
                    CI_no_longer_exists=True
                    for vm in vm_list:
                        if CI.CI_Name == vm['name']:
                            CI_no_longer_exists = False
                            break
    
                    # Actual check in platform Nutanix goes here
                    CIs_searched    +=   1
                    if CI_no_longer_exists and CI.CI_Decommissioning_DateTime is None:
                        C.logger.audit("%s:OLD:%s"%(name,CI))
                        date_time                   =   strftime("%Y-%m-%d %H:%M:%S")
                        CI.CI_Decommissioning_DateTime =   date_time
                        C.db.session.merge(CI)
                        #Debe ser AUDIT
                        C.logger.audit("%s:UPD:%s"%(name,CI))
                        CIs_decommissioned  +=  1
                C.db.session.commit()
                C.db.session.close()  
                C.logger.info("%s: %d Configuration Items searched in platform '%s'."%(__name__,CIs_searched,platform_name[0]))
                C.logger.info("%s: %d Configuration Items decommissioned from platform '%s' detected."%(__name__,CIs_decommissioned,platform_name[0]))
            else:
                C.logger.error("%s: loading %s file. Extract return code=%s"%(__name__,N.json_file_name,retcode) )           
        else:
            C.logger.info("%s: Collector Inactive."%(__name__))        
    else:
            C.logger.critical("%s: Configuration file '%s' does not exist."%(__name__,nutanix_ini_file))
    C.logger.info("%s: Nutanix Check for CI Commissioning: Completed"%(__name__))

