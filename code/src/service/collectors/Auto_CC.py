# import system modules
import os
import calendar
import re
# Import configuration functions
import configparser
from time                                           import strftime

# Import Emtec's modules
from emtec                                          import *
from emtec.collector.db.orm                         import *
from emtec.collector.db.orm_model                   import *
from emtec.collector.common.context                 import Context
# import specific platform modules

def Auto_CC_Collector(C,config,group):
    # Este json file esta forzado hasta implementar rutina de captura desde plataforma
    C.logger.info("%s: Auto Cost Center assigner: Execution start"%(__name__))
    C.logger.info("%s: Using Group         : %s"%(__name__,group))
    
    if True:    
        # Dealing with time data
              
        name            =   config.get(group,'name',fallback=group)
        active          =   config.getboolean(group,'active',fallback=False)
        if active:
            CIs_candidates = 0
            CIs_updated    = 0
            # for every C.I. in DB that has CC_Id = 1 (default non 
            # meaningfull code) and check for Name matching CC regexp
            CCs = C.db.session.query(Cost_Centers
                        ).filter(Cost_Centers.CC_Reg_Exp.isnot(None)
                        ).all()
            C.logger.debug("%s: CCs=%s (%s)"%(__name__,CCs,len(CCs)))
            if CCs is not None and len(CCs):
                for CI in C.db.session.query(Configuration_Items
                            ).filter(Configuration_Items.CC_Id<2 
                            ).all(): 
                    CIs_candidates += 1
                    C.logger.debug("%s: CI candidate =%s"%(__name__,CI))
                    # Compara aqui CI_Name con Reg_Exp de cada CC,
                    # si match entonces actualiza CC_Id
                    CC_Id = None
                    for CC in CCs:
                        if len(CC.CC_Reg_Exp)>0:
                            C.logger.trace("%s: CC Pattern=%s ? CI_Name=%s %s"%(
                                        __name__,
                                        CC.CC_Reg_Exp,
                                        CI.CI_Name,
                                        re.match(CC.CC_Reg_Exp,CI.CI_Name)))
                            if re.match(CC.CC_Reg_Exp,CI.CI_Name) is not None:
                                CC_Id=CC.CC_Id
                        if CC_Id is not None: # If MATCH !!!!
                            C.logger.audit("%s: OLD %s"%(__name__,CI))
                            CI.CC_Id = CC_Id
                            C.db.session.merge(CI)
                            C.logger.audit("%s: UPD %s"%(__name__,CI))
                            CIs_updated +=1
                            break   # Only first match will cause update
            C.db.session.commit()
            C.db.session.close()  
            C.logger.info("%s: Identified %d Configuration Item candidates."%(__name__,CIs_candidates))
            C.logger.info("%s: Updated %d Configuration Items to matching CC pattern."%(__name__,CIs_updated))
        else:
            C.logger.info("%s: Collector Inactive."%(__name__))        
    else:
        C.logger.critical("%s: Configuration file '%s' does not exist."%(__name__,ini_file))
    C.logger.info("%s: Auto Cost Center assigner: Completed"%(__name__))

