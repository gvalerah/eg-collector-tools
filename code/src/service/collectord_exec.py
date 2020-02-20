# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-15 16:02:19
# =============================================================================

#import  importlib.util
import  configparser
from    configparser    import ConfigParser, ExtendedInterpolation
from    time            import strftime
from    pprint          import pprint
from    emtec           import *

def Execute_Collector_Daemon(C,config,driver_group,collector):
    C.logger.debug("%s: Enter Execute_Collector_Daemon with C=%s"%(__name__,C))
    C.logger.debug("%s: config             = %s"%(__name__,config))
    C.logger.debug("%s: driver_group       = %s"%(__name__,driver_group))
    C.logger.debug("%s: collector          = %s"%(__name__,collector))
    
    name=config.get(driver_group,'name',fallback=driver_group)
    C.logger.debug("%s: name               = %s"%(__name__,name))
    
    C.logger.info("%s: ****************************************"%__name__)
    try:
        try:
                if config.getboolean(driver_group,'active',fallback=True):
                    try:
                        collector(C,config,driver_group)
                    except Exception as e:
                        emtec_handle_general_exception(e,"execution of collector '%s'() FAILED ..."%(collector),
                            logger=C.logger,module=__name__,function='Execute_Collector_Daemon')
                else:
                    C.logger.info("%s: collector '%s' is inactive"%(__name__,name))                    
        except Exception as e:
                emtec_handle_general_exception(e,"execution of configuration '%s' FAILED ..."%(driver_config_file),
                    logger=C.logger,module=__name__,function='Execute_Collector_Daemon')                    
    except Exception as e:
        emtec_handle_general_exception(e,logger=C.logger,module=__name__,function='Execute_Collector_Daemon')                    
    C.logger.info("%s: Collector '%s' Daemon Execution completed @ %s"%(__name__,name,strftime("%Y-%m-%d %H:%M:%S")))
    C.logger.info("%s: ****************************************"%__name__)

