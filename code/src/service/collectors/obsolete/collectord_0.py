
import os
import calendar
# Import configuration functions
import configparser

from sqlalchemy                 import create_engine
from sqlalchemy.orm             import sessionmaker
"""
from db.Configuration_Items     import Configuration_Items
from db.Charge_Units            import Charge_Units
from db.Charge_Items            import Charge_Items
"""
from .orm_models                 import Configuration_Items
from .orm_models                 import Charge_Units
from .orm_models                 import Charge_Items

from time                       import strftime
from app.common.context         import Context
from service.plugins.nutanix.etl_1_0    import Nutanix

def Collector_0(C,ini_file):
    # Este json file esta forzado hasta implementar rutina de captura desde plataforma
    C.logger.info("%s: Mounthly Auto Collector: Execution start"%(__name__))
    
    if (os.path.isfile(ini_file)):    
        config          =   configparser.ConfigParser()
        
        config.read(ini_file)
        
        # Dealing with time data
              
        name            =   config['General']['name']
        active          =   config.getboolean('General','active')
        if active:
            year            =   int(strftime("%Y"))
            month           =   int(strftime("%m"))
            today           =   strftime("%Y-%m-%d")
            first_dow,days  =   calendar.monthrange(year,month)
            last_day        =   "%4d-%2d-%2d"%(year,month,days)
            first_day       =   "%4d-%2d-%2d"%(year,month,1)        # First day of the month is an adecuated date , les calculus
            date_time       =   "%s %s"%(first_day,"12:00:00")

            CITs_generated = 0
        
            Session = sessionmaker(bind=C.db)
            session = Session()
        
            # for every C.U. in DB that has CIT_Generation marked as "Monthly" (3)
            # for every C.U. asociated to de monthly CI
            for CU in session.query(Charge_Units).filter(Charge_Units.CIT_Generation == 3): # Generates Monthly Items Only
                C.logger.debug("%s: CU=%s",(__name__,CU))
                # For each execution Daemon tries to create/update a monthly C.IT record, for the first day of the month at noon
                # Id, Date, Time, Quantity, Status=1 Created, Is_Active=1=True, DateTime=Date+Time
                CIT=Charge_Items(CU.CU_Id,first_day,'12:00:00',1,1,1,date_time)
                C.logger.debug("%s: CIT=%s",(__name__,CIT))
                session.merge(CIT)
                CITs_generated = CITs_generated + 1
            session.commit()
            session.close()  
            C.logger.info("%s: Generated %d Monthly Charge Items."%(__name__,CITs_generated))
        else:
            C.logger.info("%s: Collector Inactive."%(__name__))        
    else:
        C.logger.critical("%s: Configuration file '%s' does not exist."%(__name__,nutanix_ini_file))
    C.logger.info("%s: Mounthly Auto Collector: Completed"%(__name__))

