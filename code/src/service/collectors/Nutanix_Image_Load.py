
import os
from time                               import strftime
from pprint                             import pprint,pformat
import calendar
# Import configuration functions
import configparser

from sqlalchemy                         import create_engine
from sqlalchemy.orm                     import sessionmaker

from emtec                              import *
from emtec.collector.db.orm_model       import Configuration_Items
from emtec.collector.db.orm_model       import Platforms


from emtec.collector.common.context     import Context
from service.platforms.nutanix_etl_1_0  import Nutanix

def Nutanix_Image_Load_Collector(C,config,group):

    C.logger.info(f"{this()}: Nutanix Image List Storage Loader : Execution start")
    if True:    
                      
        name            =   config[group]['name']
        platform        =   config.getint(group,'platform')
        active          =   config.getboolean(group,'active')
        nodes           =   config.get(group,'nodes').split(',')
        for node in nodes:
            if active:
                # NUTANIX STUFF: Get Image List 
                N=Nutanix(config,node,logger=C.logger,db=C.db)
                C.logger.debug(f"{this()}: API version    = {N.API_version}")  
                
                N.platform        = config.getint(group,'platform',fallback=1)
                N.cost_center     = config.getint(group,'default_cost_center',fallback=1)
                N.customer        = config.getint(group,'default_customer',fallback=1)
                N.CIT_generation  = config.getint(group,'CIT_generation',fallback=1)
                N.chunk_size      = config.getint(group,'chunk_size',fallback=100)
                N.sharding        = config.getboolean('General','collector_cit_sharding',fallback=False)
                C.logger.debug(f"{this()}: will enter loop has more data = {N.has_more_data}")  
                while N.has_more_data:
                    retcode=N.Extract_Images(API_version=N.API_version)
                    if retcode is not None and retcode==200:
                        N.Transform_Images() 
                        N.ETL_Load()
                    else:
                        C.logger.error(f"{this()}: got error {retcode} getting data for collector : '{name}'")
                        N.has_more_data=False                    
                C.logger.debug(f"{this()}: out loop has more data = {N.has_more_data} total={N.total_matches} processed={N.processed_images}")
                good_bye_message=f" {N.processed_images} entities processed out of {N.total_matches} matched in platform '{name}'."
            else:
                C.logger.info(f"{this()}: Collector Inactive.")        
    else:
            C.logger.critical(f"{this()}: Configuration file '{nutanix_ini_file}' does not exist.")
    C.logger.info(f"{this()}: Nutanix Image List Storage Loader : Completed")

