import os
# Import configuration functions
import configparser

from time                           import strftime
from emtec                          import *
from emtec.collector.common.context import Context
from service.platforms.nutanix_etl  import Nutanix

def Nutanix_ETL_Collector(C,config,group):
    C.logger.info("%s: NUTANIX Platform Collector: Execution start"%(__name__))
    C.logger.info("%s: Using Group         : %s"%(__name__,group))

    good_bye_message=''
    
    try:    
        name            =   config[group]['name']
        api_version     =   int(config[group]['api_version'])
        active          =   config[group]['active']
        if active == 'True':
            N=Nutanix(config,group,logger=C.logger,db=C.db)
            C.logger.debug("%s: %s logging to '%s' ..."  % (__name__,name,C.logger) )
            C.logger.debug("%s: API version    = %d"      % (__name__,N.API_version) )  

            N.platform        = config.getint(group,'platform',fallback=1)
            N.cost_center     = config.getint(group,'default_cost_center',fallback=1)
            N.customer        = config.getint(group,'default_customer',fallback=1)
            N.CIT_generation  = config.getint(group,'CIT_generation',fallback=1)
            N.chunk_size      = config.getint(group,'chunk_size',fallback=100)
            N.sharding        = config.getboolean('General','collector_cit_sharding',fallback=False)
            
            C.logger.debug("%s: will enter loop has more data = %s"      % (__name__,N.has_more_data) )  
            while N.has_more_data:
                C.logger.info("%s: in loop has more data = %s total=%d processed=%d"      % (__name__,N.has_more_data,N.total_matches,N.processed_vms) )  
                status=N.Extract(API_version=api_version)
                if status == 200:
                    N.Transform() 
                    N.ETL_Load()
                else:
                    C.logger.error("%s: got error %s getting data for collector : '%s'"      % (__name__,status,name) )
                    N.has_more_data=False                    
            C.logger.debug("%s: out loop has more data = %s total=%d processed=%d"      % (__name__,N.has_more_data,N.total_matches,N.processed_vms) ) 
            good_bye_message=" %d entities processed out of %d matched in platform '%s'."%(N.processed_vms,N.total_matches,name)
        else:
            C.logger.info("%s: Collector Inactive.",(__name__))                    
    except Exception as e:
        emtec_handle_general_exception    (e,detail=None,module=None,function='Nutanix_ETL_Collector',logger=None,fp=None)
        good_bye_message="%s: EXCEPTION: '%s'."%(__name__,str(e))
    C.logger.info("%s: Completed.%s"%(__name__,good_bye_message))
