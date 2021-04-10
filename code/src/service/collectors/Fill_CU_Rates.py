# import system modules
import os
#import calendar
#import re
# Import configuration functions
import configparser
from time                                           import strftime

# Import Emtec's modules
from emtec                                          import *
from emtec.collector.db.orm                         import *
from emtec.collector.db.orm_model                   import *
from emtec.collector.common.context                 import Context
# import specific platform modules

# Minimal Collector Data Handler service -------------------------------
# purpose: Fill Up CU's Rates with actual Data, it will refresh Rates
# Periodically in order to refresh Rates to accomodate CI CC changes
# or Rates modifications -----------------------------------------------

def Fill_CU_Rates_Collector(C,config,group=None):
    C.logger.info("Execution start")              
    CUs_updated    = 0
    try:
        # Will refresh only pending rate CUs
        CUs_updated = C.db.Update_CU_Rates(refresh_all=True)
    except Exception as e:
        C.logger.error(f"EXCEPTION: {str(e)}")
    C.logger.debug(f"CUs Updated = {CUs_updated}")
    C.logger.info("Completed")
