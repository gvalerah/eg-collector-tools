# GV *******************************************************************
# GV Automatic rates filler for charge units
# GV (c) Emtecgroup 2018-2022
# GV GLVH 2018       Initial version
# GV GLVH 2022-02-09 Exception handling
# GV gvalera@emtecgroup.net
# GV *******************************************************************
# GV Minimal Collector Data Handler service ----------------------------
# GV purpose: Fill Up CU's Rates with actual Data, it will refresh Rates
# GV Periodically in order to refresh Rates to accomodate CI CC changes
# GVor Rates modifications ---------------------------------------------

# GV import system modules
import os
# GV Import configuration functions
import configparser
from time                                           import strftime

# GV Import Emtec's modules
from emtec                                          import *
from emtec.collector.db.orm                         import *
from emtec.collector.db.orm_model                   import *
from emtec.collector.common.context                 import Context
# GV import specific platform modules

# Minimal Collector Data Handler service -------------------------------
# purpose: Fill Up CU's Rates with actual Data, it will refresh Rates
# Periodically in order to refresh Rates to accomodate CI CC changes
# or Rates modifications -----------------------------------------------

def Fill_CU_Rates_Collector(C,config,group=None):
    C.logger.info("%s: Automatic CU rates filler : Execution start"%(__name__))
    CUs_updated    = 0
    if C is not None:
        logger = C.logger
    else:
        logger = None
    try:
        # GV Will refresh all rate CUs
        CUs_updated = C.db.Update_CU_Rates(refresh_all=True)
    except Exception as e:
        emtec_handle_general_exception(e,logger=logger)
    C.logger.debug(f"CUs Updated = {CUs_updated}")
    C.logger.info("Completed")
