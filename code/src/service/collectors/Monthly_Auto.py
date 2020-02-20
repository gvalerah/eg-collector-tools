# import system modules
import os
import calendar
# Import configuration functions
import configparser
from time                                           import strftime

# Import Emtec's modules
from emtec                                          import *
from emtec.collector.db.orm                         import *
from emtec.collector.db.orm_model                   import *
from emtec.collector.common.context                 import Context
# import specific platform modules
#from service.platforms.nutanix_etl_1_0              import Nutanix

def Monthly_Auto_Collector(C,config,group):
    # Este json file esta forzado hasta implementar rutina de captura desde plataforma
    C.logger.info("%s: Mounthly Auto Collector: Execution start"%(__name__))
    C.logger.info("%s: Using Group         : %s"%(__name__,group))
    
    #if (os.path.isfile(ini_file)):    
    if True:    
        #config          =   configparser.ConfigParser()
        
        #config.read(ini_file)
        
        # Dealing with time data
              
        name            =   config.get(group,'name',fallback=group)
        active          =   config.getboolean(group,'active',fallback=False)
        if active:
            year            =   int(strftime("%Y"))
            month           =   int(strftime("%m"))
            today           =   strftime("%Y-%m-%d")
            first_dow,days  =   calendar.monthrange(year,month)
            last_day        =   "%4d-%02d-%02d"%(year,month,days)
            first_day       =   "%4d-%02d-%02d"%(year,month,1)        # First day of the month is an adecuated date , les calculus
            date_time       =   "%s %s"%(first_day,"12:00:00")

            CITs_generated = 0
        
            # for every C.U. in DB that has CIT_Generation marked as "Monthly" (3)
            # for every C.U. asociated to de monthly CI
            for CU in C.db.session.query(Charge_Units).filter(Charge_Units.CIT_Generation == 3): # Generates Monthly Items Only
                C.logger.debug("%s: CU=%s"%(__name__,CU))
                # For each execution Daemon tries to create/update a monthly C.IT record, for the first day of the month at noon
                # Id, Date, Time, Quantity, Status=1 Created, Is_Active=1=True, DateTime=Date+Time
                CIT=Charge_Items(CU.CU_Id,first_day,'12:00:00',1,1,1,date_time)
                C.logger.audit("%s: NEW CIT=%s"%(__name__,CIT))
                C.db.session.merge(CIT)
                CITs_generated = CITs_generated + 1
            C.db.session.commit()
            C.db.session.close()  
            C.logger.info("%s: Generated %d Monthly Charge Items."%(__name__,CITs_generated))
        else:
            C.logger.info("%s: Collector Inactive."%(__name__))        
    else:
        C.logger.critical("%s: Configuration file '%s' does not exist."%(__name__,ini_file))
    C.logger.info("%s: Mounthly Auto Collector: Completed"%(__name__))

