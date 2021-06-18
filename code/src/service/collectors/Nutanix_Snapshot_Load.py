
import os
from time                               import strftime
from pprint                             import pprint,pformat
import calendar
# Import configuration functions
import configparser

from sqlalchemy                         import create_engine
from sqlalchemy.orm                     import sessionmaker

from emtec.collector.db.orm_model       import Configuration_Items
from emtec.collector.db.orm_model       import Platforms


from emtec.collector.common.context     import Context
from service.platforms.nutanix_etl_1_0  import Nutanix

def Nutanix_Snapshot_Load_Collector(C,config,group):

    C.logger.info(f"{__name__}: Nutanix Snapshot List Storage Loader : Execution start")
    if True:    
                      
        name            =   config[group]['name']
        platform        =   config.getint(group,'platform')
        active          =   config.getboolean(group,'active')
        nodes           =   config.get(group,'nodes').split(',')
        # Will Probe all nodes (Prism Elements asociated to Prism Central
        # at once
        for node in nodes:
            if active:
                # NUTANIX STUFF: Get Snapshot List 
                N=Nutanix(config,node,logger=C.logger,db=C.db)
                # Changes configuration to Prism Element Node
                N.Load_Node(node)
                C.logger.debug(f"{__name__}: API version    = {N.API_version}")  
                C.logger.warning(f"{__name__}: Node = {node}  = {N.username}@{N.host}")  
                
                N.platform        = config.getint(group,'platform',fallback=1)
                N.cost_center     = config.getint(group,'default_cost_center',fallback=1)
                N.customer        = config.getint(group,'default_customer',fallback=1)
                N.CIT_generation  = config.getint(group,'CIT_generation',fallback=1)
                N.chunk_size      = config.getint(group,'chunk_size',fallback=100)
                N.sharding        = config.getboolean('General','collector_cit_sharding',fallback=False)
                C.logger.debug(f"{__name__}: will enter loop has more data = {N.has_more_data}")  
                while N.has_more_data:
                    #etcode=N.Extract_Snapshots(API_version=N.API_version) version 2 API available only
                    retcode=N.Extract_Snapshots(API_version=2)
                    if retcode is not None and retcode==200:
                        N.Transform_Snapshots() 
                        N.ETL_Load()
                    else:
                        C.logger.error(f"{__name__}: got error {retcode} getting data for collector : '{name}'")
                        N.has_more_data=False                    
                C.logger.debug(f"{__name__}: out loop has more data = {N.has_more_data} total={N.total_matches} processed={N.processed_snapshots}")
                good_bye_message=f" {N.processed_snapshots} entities processed out of {N.total_matches} matched in platform '{name}'."
            else:
                C.logger.info(f"{__name__}: Collector Inactive.")        
    else:
            C.logger.critical(f"{__name__}: Configuration file '{nutanix_ini_file}' does not exist.")
    C.logger.info(f"{__name__}: Nutanix Snapshot List Storage Loader : Completed")

