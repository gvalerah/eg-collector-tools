
import os
import sys
from time                               import strftime
from pprint                             import pprint,pformat
import calendar
# Import configuration functions
import configparser

from sqlalchemy                         import create_engine
from sqlalchemy.orm                     import sessionmaker

from emtec.data                         import *

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
        nodes           =   config.get(group,'nodes').split(',')
        

        
        
        
        ci_list         =   []
        vms             =   0
        imgs            =   0
        vgs             =   0
        if active:
            # NUTANIX STUFF: Get VM,Images & VGroups Lists from Nutanix 
            N=Nutanix(config,group,logger=C.logger,db=C.db)
            #N.platform        = config.getint(group,'platform',fallback=1)
            #N.cost_center     = config.getint(group,'default_cost_center',fallback=1)
            #N.customer        = config.getint(group,'default_customer',fallback=1)
            #N.CIT_generation  = config.getint(group,'CIT_generation',fallback=1)
            N.chunk_size      = config.getint(group,'chunk_size',fallback=100)
            #N.sharding        = config.getboolean('General','collector_cit_sharding',fallback=False)
            C.logger.info("%s: will enter loop has more data = %s"      % (__name__,N.has_more_data) )  
            C.logger.info("%s: processed = %s"      % (__name__,N.processed_vms) )  
            processed_vms = 0
            while N.has_more_data:
                try:
                    status,data = N.getVMsInformation(N.API_version)
                    if status == 200:
                        # Adjust to get total number of VMs in system
                        if N.API_version == 2:
                            N.total_matches =    int(data['metadata']['grand_total_entities'])
                            N.processed_vms +=   int(data['metadata']['count'])
                            
                        elif N.API_version == 3:
                            N.total_matches =    int(data['metadata']['total_matches'])
                            N.processed_vms +=   int(data['metadata']['length'])
                        C.logger.debug("%s: total matches = %s"      % (__name__,N.total_matches) )  
                        C.logger.debug("%s: processed     = %s"      % (__name__,N.processed_vms) )  

                        C.logger.info (f"{__name__}: Found {len(data.get('entities'))} CIs of type VM in {group} ({N.processed_vms}/{N.total_matches})")
                        vms += len(data.get('entities'))
                        for e in data.get('entities'):
                            ci_list.append({'name': e['spec']['name'], 'uuid': e['metadata']['uuid'],'type':'VM'})
                        if N.processed_vms >= N.total_matches:
                            N.has_more_data = False
                            C.logger.info(f"{__name__}: NO MORE DATA EXPECTED has_more_data={N.has_more_data} total = {N.total_matches} processed={N.processed_vms}")
                    else:
                        C.logger.info(f"{__name__}: VM. status = {status}. total cis={len(ci_list)}")                
                        C.logger.error("%s: got error %s getting data for collector : '%s'"      % (__name__,status,name) )
                        N.has_more_data=False                    
                except Exception as e:
                    C.logger.warning(f"{__name__}: VMs: No data from Nutanix. exception: ({str(e)})")
                    N.has_more_data=False                    

            for node in nodes:
                #print(f"node={node}")
                # Images
                N=Nutanix(config,node,logger=C.logger,db=C.db)
                status,data = N.getImagesInformation(N.API_version)
                if status == 200:
                    C.logger.info(f"{__name__}: Found {len(data.get('entities'))} CIs of type Image in {node}")
                    imgs += len(data.get('entities'))
                    for e in data.get('entities'):
                        ci_list.append({'name': e['name'], 'uuid': e['uuid'],'type':'IMG'})
                # Volume Groups
                status,data = N.getVGroupsInformation(N.API_version)
                if status == 200:
                    if len(data):
                        vgs += len(data[0].get('entities'))
                        C.logger.info(f"{__name__}: Found {len(data[0].get('entities'))} CIs of type Volume Group  in {node}")
                        for e in data[0].get('entities'):
                            ci_list.append({'name': e['name'], 'uuid': e['uuid'],'type':'VG'})
            C.logger.info(f"{__name__}: {len(ci_list)} CIs found in Nutanix (vms={vms},imgs={imgs},vgs={vgs})")
            C.logger.info(f"{__name__}: Overriding Decommissioning DateTime for active CIs")
            uuid_list = []
            for CI in ci_list:
                uuid_list.append(CI.get('uuid'))
            C.logger.info(f"{__name__}: {len(uuid_list)} uuids in overrride list")
            C.logger.info(f"{__name__}: {len(unique_list(uuid_list))} unique uuids in overrride list")
            # Will patch Decommissioning DateTime for revived CIs
            reseted=0
            for CI in C.db.session.query(
                Configuration_Items
                ).filter(Configuration_Items.CI_UUID.in_(uuid_list)
                ): # Process al CIs for platform
                CI.CI_Decommissioning_DateTime = None
                C.db.session.merge(CI)
                reseted+=1
            C.db.session.commit()
            #20210630 GV C.db.session. close()
            C.db.session.flush()  
            C.logger.info(f"{__name__}: {reseted} CIs reseted in DB prior to check ...")

            C.logger.debug("%s: API version    = %d"                              % (__name__,N.API_version) )  

            # Get Actual Nutanix Data ----------------------------------

            #retcode=N.Extract(API_version=N.API_version)
            #if retcode is not None and retcode==200:
            if True:
                # 20211024 GV Changing revision to include other types
                CIs_searched                =   0
                CIs_decommissioned          =   0
                CIs_alreadydecommissioned   =   0
                platform_name = C.db.session.query(
                    Platforms.Pla_Name
                    ).filter(Platforms.Pla_Id==platform
                    ).first()
                # Will check all CIs actually in DB
                for CI in C.db.session.query(
                    Configuration_Items
                    ).filter(Configuration_Items.Pla_Id == platform
                    ): # Process al CIs for platform
                    C.logger.debug("%s: CI=%s"%(__name__,CI))
                    CI_no_longer_exists=True
                    # GV 20211024
                    #for vm in vm_list:
                    #    if CI.CI_Name == vm['name']:
                    #        CI_no_longer_exists = False
                    #        break
                    for ci in ci_list:
                        if CI.CI_UUID == ci['uuid']:
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
                    elif CI_no_longer_exists and CI.CI_Decommissioning_DateTime is not None:
                        CIs_alreadydecommissioned += 1 # Ignored Decom DateTime Update
                    else:
                        CI.CI_Decommissioning_DateTime = None
                        C.db.session.merge(CI)
                        
                C.db.session.commit()
                #20210630 GV C.db.session. close()
                C.db.session.flush()  
                C.logger.info("%s: %d Configuration Items searched in platform '%s'."%(__name__,CIs_searched,platform_name[0]))
                C.logger.info("%s: %d Configuration Items decommissioned from platform '%s' detected."%(__name__,CIs_decommissioned,platform_name[0]))
                C.logger.info("%s: %d Configuration Items decommission ignored from platform '%s' detected."%(__name__,CIs_decommissioned,platform_name[0]))
            else:
                C.logger.error("%s: loading %s file. Extract return code=%s"%(__name__,N.json_file_name,retcode) )           
        else:
            C.logger.info("%s: Collector Inactive."%(__name__))        
    else:
            C.logger.critical("%s: Configuration file '%s' does not exist."%(__name__,nutanix_ini_file))
    C.logger.info("%s: Nutanix Check for CI Commissioning: Completed"%(__name__))

