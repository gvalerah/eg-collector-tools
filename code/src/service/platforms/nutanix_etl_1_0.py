# ----------------------------------------------------------------------
# Nutanix Storage API ETL exploit Class
# code/src/service/platforms/nutanix_etl_1_0.py
# GLVH 2018
# GVLV 2021-04-03 Refactoring + Add snapshots
# GVLV 2021-09-12 Add volume groups
# GVLV 2021-10-24 Adjust CI get lists functions (get_..._list)
# Gerardo L Valera
# gvalera@emtecgroup.net
# ----------------------------------------------------------------------
# Import System Libs
import  json
import  shutil
import  urllib3

# Import configuration functions
import configparser

# Import logging functions
import logging

# Import html requests
import requests

from pprint     import pprint
from pprint     import pformat
from time       import strftime

# Import sqlalchemy functions function
from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy import exc
# GV 20190818

from emtec                  import *
from emtec.debug            import *
from emtec.class_etl        import *
from emtec.nutanix          import *

class Nutanix(ETL):
    """ Nutanix ETL Class """

    """ Members """
    
    
    # Multi version variables
    API_version         = None
    BASE_URL            = []
    base_url            = []
    total_matches       = 0
    processed_vms       = 0
    processed_images    = 0
    processed_snapshots = 0
    processed_vgroups   = 0
    chunk_size          = 100
    has_more_data       = True
    sharding            = False
    sharding_suffix     = None
    sharding_cit_class  = None
    
    # Data Creation Flags
    # create_XXX    = False
          
    """ Methods """

    def __init__(self,config,group,logger=None,ormdb=None,db=None):
        # in case logger is not specified then system wide root logger
        # will be used
        if logger is None:
            #20210710 GV replace bad working function self.logger = check_logger()
            self.logger = logging.getLogger()
        else:
            self.logger = logger
            self.ETL_Set_Logger(logger)

        if db is not None:
            self.db = db
        self.Read_ETL_Configuration(config=config,group=group)
        self.API_version = self.config.getint(group,'API_version',fallback=2)
        if self.port == None:
            self.port = 9440
        
        # Hard Coded API URL Data, Possible to go to Configuration also, in case of changes
        # Can be overrided , see below
        self.BASE_URL = [   'https://%s:%d/api/nutanix/v0.8/',
                            'https://%s:%d/PrismGateway/services/rest/v1/',
                            'https://%s:%d/PrismGateway/services/rest/v2.0/',
                            'https://%s:%d/api/nutanix/v3/'
                        ]
                        
        self.base_url = []
        for api in range(len(self.BASE_URL)):
            self.base_url.append(self.BASE_URL[api] % (self.host,self.port))
            if (self.logger):
                self.logger.debug("%s: base_url[%d]=%s"%(this(),api,self.base_url[api]))
        
        # Overrides default route for selected API version if specified in configuration
        # If URL specied
        if self.url is not None:
            if (self.logger):
                self.logger.debug("%s: overrriding base URL for version %d (%s) with URL from configuration (%s)"%(this(),api,self.base_url[self.API_version],self.url))
            self.base_url[self.API_version]=self.url                
        else:
            # If route specified
            if (self.logger):
                self.logger.debug("%s: overrriding base URL for version %d (%s) with route from configuration (%s)"%(this(),api,self.base_url[self.API_version],self.route))
            if self.route is not None:
                self.base_url[self.API_version]='https://%s:%d/%s'%(self.host,self.port,self.route)                

        self.logger.debug("%s: self.url        = %s"%(this(),self.url))
        self.logger.debug("%s: self.route      = %s"%(this(),self.route))
        self.logger.debug("%s: self.API_version= %s"%(this(),self.API_version))
        for api in range(len(self.BASE_URL)):
            self.logger.debug("%s: %d: [%s]"%(this(),api,self.base_url[api]))
                   
        self.session = self.get_server_session(self.username, self.password)

        # Disable warnings
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)    
        
        
    def Load_Node(self,node):
        # overrides Prism Central configurations with Node (Prism Element)
        # configuration and open/reopen session
        try:
            self.host               = self.config.get    (node,'host',                  fallback=None)
            self.port               = self.config.getint (node,'port',                  fallback=0)
            self.connection_timeout = self.config.getint (node,'connection_timeout',    fallback=5)
            self.read_timeout       = self.config.getint (node,'read_timeout',          fallback=10)
            self.protocol           = self.config.get    (node,'protocol',              fallback='https')
            self.username           = self.config.get    (node,'username',              fallback=None)
            self.password           = self.config.get    (node,'password',              fallback=None)
            self.API_version        = self.config.getint (node,'API_version',           fallback=None)
            self.session            = self.get_server_session(self.username, self.password)
        except Exception as e:
            emtec_handle_general_exception(e,logger=self.logger)
        
    def get_server_session(self, username=None, password=None):
    
        if username is not None:
            self.username = username
        if password is not None:
            self.password = password

        if (self.logger):
            self.logger.debug("%s: username=%s password=%s"%(this(),self.username,self.password))

        session         = requests.Session()
        session.auth    = (self.username, self.password)
        session.verify  = False                                            
        session.headers.update(
            {'Content-Type': 'application/json; charset=utf-8'})
        return session

    # GET CLUSTER DATA
    def getClusterInformation(self,version):
        # version 2 coded by now (will be usable for other versions?)
        clusterURL = self.base_url + "/cluster"
        try:
            serverResponse = self.session.get(clusterURL,timeout=(self.connection_timeout,self.read_timeout))
        except ConnectionError:
            self.logger.error("%s: getClusterInformation: Connection Error trying version=%d call=%s URL=%s"     %(this(),version,call_type,vmsURL))            
            return None,None
        except ConnectTimeout:
            self.logger.error("%s: getClusterInformation: Connection Timeout trying version=%d call=%s URL=%s"     %(this(),version,call_type,vmsURL))            
            return None,None
        except Exception as e:
            emtec_handle_general_exception(e,logger=self.logger,module=this(),function='getClusterInformation')
            return None,None
        if serverResponse is not None and is_json(serverResponse.text):
            return serverResponse.status_code, json.loads(serverResponse.text)
        else:
            return serverResponse.status_code, None
            
    # GET VM DATA
    def getVMsInformation(self,version=None):
        if version is None:
            version = self.api_version 
        call = [    'vms/?includeVMDiskSizes=true&includeAddressAssignments=true',
                    'vms/',
                    'vms/?offset=%s&length=%s&include_vm_disk_config=true&include_vm_nic_config=true'%(self.processed_vms,self.chunk_size),
                    'vms/list'
                    ]
        
        if version == 3:
            self.session.headers.update( {'Accept': 'application/json' } )   

        vmsURL = self.base_url[version] + call[version]

        parameters=''
        call_type=None
        server_Response=None
        try:
            if version == 3:
                call_type="POST"
                h=strftime("%H:%M:%S")
                parameters = '{"kind":"vm","offset":%d,"length":%d}'%(self.processed_vms,self.chunk_size)
                serverResponse = self.session.post(vmsURL,parameters,timeout=(self.connection_timeout,self.read_timeout))
            else:
                call_type="GET"
                serverResponse = self.session.get(vmsURL,timeout=(self.connection_timeout,self.read_timeout))
        except ConnectionError:
            self.logger.error("%s: getVMsInformation: Connection Error trying version=%d call=%s URL=%s"     %(this(),version,call_type,vmsURL))            
            return None,None
        except ConnectTimeout:
            self.logger.error("%s: getVMsInformation: Connection Timeout trying version=%d call=%s URL=%s"     %(this(),version,call_type,vmsURL))            
            return None,None
        except Exception as e:
            emtec_handle_general_exception(e,logger=self.logger,module=this(),function='getVMsInformation')
            return None,None
        if (self.logger):
            self.logger.debug("%s: version        = %d"     %(this(),version))
            self.logger.debug("%s: vmsURL         = %s"     %(this(),vmsURL))
            self.logger.debug("%s: call_Type      = %s %s"  %(this(),call_type,parameters))
            self.logger.debug("%s: serverResponse = %s"     %(this(),serverResponse))
            if serverResponse is not None:
                self.logger.debug("%s:       Code     = %s"     %(this(),serverResponse.status_code))
                self.logger.debug("%s:       Text     = %s"     %(this(),serverResponse.text))

        if serverResponse is not None:
            if is_json(serverResponse.text):
                data = json.loads(serverResponse.text)
            else:
                data = None
            return serverResponse.status_code, data
        else:
            return None, None
    
    # GET Image DATA
    def getImagesInformation(self,version=None):
        if self.logger:
            self.logger.debug(f'{this()}: version={version}')
        if version is None:
            version = self.api_version 
        call = [    '',
                    '',
                    'images/?include_vm_disk_sizes=true',
                    ''
                    ]
        
        if version == 3:
            self.session.headers.update( {'Accept': 'application/json' } )   

        imagesURL = self.base_url[version] + call[version]

        parameters=''
        call_type=None
        server_Response=None
        try:
            if version == 3:
                call_type="POST"
                h=strftime("%H:%M:%S")
                parameters = '{"kind":"image","offset":%d,"length":%d}'%(
                    self.processed_images,self.chunk_size)
                serverResponse = self.session.post(
                    imagesURL,
                    parameters,
                    timeout=(
                        self.connection_timeout,
                        self.read_timeout)
                    )
            else:
                call_type="GET"
                serverResponse = self.session.get(
                    imagesURL,
                    timeout=(
                        self.connection_timeout,
                        self.read_timeout)
                    )
        except ConnectionError:
            if self.logger:
                self.logger.error("%s: getImagesInformation: Connection Error trying version=%d call=%s URL=%s"     %(this(),version,call_type,imagesURL))            
            return None,None
        except ConnectTimeout:
            if self.logger:
                self.logger.error("%s: getImagesInformation: Connection Timeout trying version=%d call=%s URL=%s"     %(this(),version,call_type,imagesURL))            
            return None,None
        except Exception as e:
            emtec_handle_general_exception(e,logger=self.logger,module=this(),function='getImagesInformation')
            return None,None
        if (self.logger):
            self.logger.debug("%s: version        = %d"     %(this(),version))
            self.logger.debug("%s: imagesURL      = %s"     %(this(),imagesURL))
            self.logger.debug("%s: call_Type      = %s %s"  %(this(),call_type,parameters))
            self.logger.debug("%s: serverResponse = %s"     %(this(),serverResponse))
            if serverResponse is not None:
                self.logger.debug("%s:       Code     = %s"     %(this(),serverResponse.status_code))
                self.logger.debug("%s:       Text     = %s"     %(this(),serverResponse.text))

        if serverResponse is not None:
            if is_json(serverResponse.text):
                data = json.loads(serverResponse.text)
            else:
                data = None
            return serverResponse.status_code, data
        else:
            return None, None

    # GET Protection Domains DATA
    # D.Lira must get data from all nodes
    def getProtectionDomainsInformation(self,version=None):
        if self.logger:
            self.logger.debug(f'{this()}: version={version}')
        if version is None:
            version = self.api_version
        self.logger.debug(f'{this()}: self.session={self.session} {type(self.session)}')

        call = [    '',
                    '',
                    'protection_domains/',
                    ''
                ]
        
        data   = []
        status = 0
        if version == 2:
            self.session.headers.update( {'Accept': 'application/json' } )   
            host_base_url =  f"https://{self.host}:{self.port}/api/nutanix/v2.0/"

        pdURL = host_base_url + call[version]
        
        self.logger.debug(f"{this()}: version={version} pdURL={pdURL}")            

        parameters = None
        
        call_type  = None
        server_Response = None
        try:
            if version == 2:
                call_type="GET"
                h=strftime("%H:%M:%S")
                
                parameters = {
                    "timeout":(
                        self.connection_timeout,
                        self.read_timeout
                        )
                    }
                
                self.logger.debug(f"{this()}:V{version}  pdURL = {pdURL}")
                self.logger.debug(f"{this()}:V{version}  parameters   = {parameters}")
                
                serverResponse = self.session.get(
                    pdURL,
                    data=parameters
                    )
            else:
                call_type="GET"
                logger.debug(f"{this()}:V{version}  pdURL = {snapshotsURL}")

                serverResponse = self.session.get(
                    pdURL,
                    timeout=(
                        self.connection_timeout,
                        self.read_timeout)
                    )
        except ConnectionError:
            if self.logger:
                self.logger.error(f"{this()}: Connection Error trying version={version} call={call_type} URL={pdURL}")            
            return None,None
        except ConnectTimeout:
            if self.logger:
                self.logger.error(f"{this()}: Connection Timeout trying version={version} call={call_type} URL={pdURL}")            
            return None,None
        except Exception as e:
            emtec_handle_general_exception(e,logger=self.logger,module=this(),function=this())
            return None,None
        if (self.logger):
            self.logger.debug(f"{this()}: version        = {version}")
            self.logger.debug(f"{this()}: pdURL          = {pdURL}")
            self.logger.debug(f"{this()}: call_Type      = {call_type} {parameters}")
            self.logger.debug(f"{this()}: serverResponse = {serverResponse}")
            if serverResponse is not None:
                self.logger.debug(f"{this()}:       Code     = {serverResponse.status_code}")
                self.logger.debug(f"{this()}:       Text     = {serverResponse.text[:100]}")

        if serverResponse is not None:
            status = max(status,serverResponse.status_code)
            if is_json(serverResponse.text):
                data.append(json.loads(serverResponse.text))
                    
        # data here is a list of data members and need to be treated as so
        if self.logger:
            self.logger.debug(f"{this()}: status = {status}")
            self.logger.debug(f"{this()}: data   = START -----------------------------")
            self.logger.debug(f"{this()}: data.type   = {type(data)}")
            self.logger.debug(f"{this()}: data.len    = {len(data)}")
            if data is not None and len(data):
                self.logger.debug("data.0.type",type(data[0]))
                self.logger.debug("data.0.metadata",pformat(data[0].get('metadata')))
                with open ("/tmp/protection_domains.json","w") as fp:
                    fp.write(json.dumps(data[0]))
            
            self.logger.debug(f"{this()}: data   = ------------------------------- END")
        return status,data

    # GET Snapshots DATA
    # D.Lira must get data from all nodes
    def getSnapshotsInformation(self,version=None):
        if self.logger:
            self.logger.debug(f'{this()}: version={version}')
        if version is None:
            version = self.api_version
        self.logger.debug(f'{this()}: self.session={self.session} {type(self.session)}')

        call = [    '',
                    '',
                    'protection_domains/dr_snapshots/',
                    ''
                ]
        
        # Since there's and API snapshots list limitation (max 5000 snapshots)
        # then actual extraction will get a list of protection domains
        # and get snapshots individually for each PD at a time
        pd_status,pd_data = self.getProtectionDomainsInformation(version=version)
        self.logger.debug(f"pd_status = {pd_status}")
        self.logger.debug(f"pd_data   = {type(pd_data)}")
        pd_exists = False
        if type(pd_data) == list:
            self.logger.debug(f"entities   = {len(pd_data)}")
            if type(pd_data[0]) == dict:
                if pd_data[0].get('entities'):
                    self.logger.debug(f"entities   = {len(pd_data[0].get('entities',0))}")
                    if len(pd_data[0].get('entities',0)):
                        pd_exists = True
                else:
                    self.logger.error(f"NO PROTECTION DOMAINS FOUND!!!!")
        
        data   = []
        status = 0
        pd_drsnapshots_counter=0
        # If any Protection Domains available then ...
        if pd_exists:
            if version == 2:
                self.session.headers.update( {'Accept': 'application/json' } )   
                host_base_url =  f"https://{self.host}:{self.port}/PrismGateway/services/rest/v2.0"

            # Will loop by Protection Domain if any ...
            for pd in pd_data[0].get('entities'):
                pd_name = pd.get('name')
                snapshotsURL = f"{host_base_url}/protection_domains/{pd_name}/dr_snapshots"        
                self.logger.debug(f"{this()}: version={version} snapshotsURL={snapshotsURL}")            

                parameters = None
                
                call_type  = None
                server_Response = None
                try:
                    if version == 2:
                        call_type="GET"
                        h=strftime("%H:%M:%S")
                        
                        parameters = {
                            "fulldetails":True,
                            #"offset":self.processed_snapshots,
                            #"count":self.chunk_size,
                            "timeout":(
                                self.connection_timeout,
                                self.read_timeout
                                )
                            }
                        
                        self.logger.debug(f"{this()}:V{version}  snapshotsURL = {snapshotsURL}")
                        self.logger.debug(f"{this()}:V{version}  parameters   = {parameters}")
                        
                        serverResponse = self.session.get(
                            snapshotsURL,
                            data=parameters
                            )
                    else:
                        call_type="GET"
                        logger.debug(f"{this()}:V{version}  snapshotsURL = {snapshotsURL}")

                        serverResponse = self.session.get(
                            snapshotsURL,
                            timeout=(
                                self.connection_timeout,
                                self.read_timeout)
                            )
                except ConnectionError:
                    if self.logger:
                        self.logger.error(f"{this()}: Connection Error trying version={version} call={call_type} URL={snapshotsURL}")            
                    return None,None
                except ConnectTimeout:
                    if self.logger:
                        self.logger.error(f"{this()}: Connection Timeout trying version={version} call={call_type} URL={snapshotsURL}")            
                    return None,None
                except Exception as e:
                    emtec_handle_general_exception(e,logger=self.logger,module=this(),function=this())
                    return None,None
                if (self.logger):
                    self.logger.debug(f"{this()}: version        = {version}")
                    self.logger.debug(f"{this()}: snapshotsURL   = {snapshotsURL}")
                    self.logger.debug(f"{this()}: call_Type      = {call_type} {parameters}")
                    self.logger.debug(f"{this()}: serverResponse = {serverResponse}")
                    if serverResponse is not None:
                        self.logger.debug(f"{this()}:       Code     = {serverResponse.status_code}")
                        self.logger.debug(f"{this()}:       Text     = {serverResponse.text[:100]}")

                if serverResponse is not None:
                    self.logger.debug(f"serverResponse={serverResponse}")
                    status = max(status,serverResponse.status_code)
                    if is_json(serverResponse.text):
                        pd_drsnapshots=json.loads(serverResponse.text)
                        data.append(pd_drsnapshots)
                        if pd_drsnapshots.get('metadata'):
                            pd_drsnapshots_counter+=pd_drsnapshots.get('metadata').get('grand_total_entities',0)
                            
        # data here is a list of data members and need to be treated as so
        if self.logger:
            self.logger.debug(f"{this()}: status = {status}")
            self.logger.debug(f"{this()}: data   = START -----------------------------")
            self.logger.debug(f"{this()}: data.type   = {type(data)}")
            self.logger.debug(f"{this()}: data.len    = {len(data)}")
            self.logger.info (f"{this()}: data = {len(data)} protection domains, {pd_drsnapshots_counter} snapshots")

            if data is not None and len(data):
                self.logger.debug(f"data.0.type {type(data[0])}")
                self.logger.debug(f"data.0.metadata {pformat(data[0].get('metadata'))}")
                with open ("/tmp/snapshots.json","w") as fp:
                    fp.write(json.dumps(data[0]))
            
            self.logger.debug(f"{this()}: data   = ------------------------------- END")
        return status,data

    # GET Volume Groups DATA
    # D.Lira must get data from all nodes
    def getVGroupsInformation(self,version=None):
        if self.logger:
            self.logger.debug(f'{this()}: version={version}')
        if version is None:
            version = self.api_version
        self.logger.debug(f'{this()}: self.session={self.session} {type(self.session)}')

        call = [    '',
                    '',
                    'volume_groups/',
                    ''
                ]
        
        data   = []
        status = 0
        if version == 2:
            self.session.headers.update( {'Accept': 'application/json' } )   
            host_base_url =  f"https://{self.host}:{self.port}/PrismGateway/services/rest/v2.0/"

        VGroupsURL = host_base_url + call[version]
        
        self.logger.debug(f"{this()}: version={version} VGroupsURL={VGroupsURL}")            

        parameters = None
        
        call_type  = None
        server_Response = None
        try:
            if version == 2:
                call_type="GET"
                h=strftime("%H:%M:%S")
                
                parameters = {
                    "include_disk_size":True,
                    "include_disk_path":True,
                    "timeout":(
                        self.connection_timeout,
                        self.read_timeout
                        )
                    }
                
                self.logger.debug(f"{this()}:V{version}  VGroupsURL = {VGroupsURL}")
                self.logger.debug(f"{this()}:V{version}  parameters   = {parameters}")
                
                serverResponse = self.session.get(
                    VGroupsURL,
                    data=parameters
                    )
            else:
                call_type="GET"
                logger.debug(f"{this()}:V{version}  VGroupsURL = {VGroupsURL}")

                serverResponse = self.session.get(
                    VGroupsURL,
                    timeout=(
                        self.connection_timeout,
                        self.read_timeout)
                    )
        except ConnectionError:
            if self.logger:
                self.logger.error(f"{this()}: Connection Error trying version={version} call={call_type} URL={VGroupsURL}")            
            return None,None
        except ConnectTimeout:
            if self.logger:
                self.logger.error(f"{this()}: Connection Timeout trying version={version} call={call_type} URL={VGroupsURL}")            
            return None,None
        except Exception as e:
            emtec_handle_general_exception(e,logger=self.logger,module=this(),function=this())
            return None,None
        if (self.logger):
            self.logger.debug(f"{this()}: version        = {version}")
            self.logger.debug(f"{this()}: VGroupsURL     = {VGroupsURL}")
            self.logger.debug(f"{this()}: call_Type      = {call_type} {parameters}")
            self.logger.debug(f"{this()}: serverResponse = {serverResponse}")
            if serverResponse is not None:
                self.logger.debug(f"{this()}:       Code     = {serverResponse.status_code}")
                self.logger.debug(f"{this()}:       Text     = {serverResponse.text[:100]}")

        if serverResponse is not None:
            status = max(status,serverResponse.status_code)
            if is_json(serverResponse.text):
                data.append(json.loads(serverResponse.text))
                    
        # data here is a list of data members and need to be treated as so
        if self.logger:
            try:
                self.logger.debug(f"{this()}: status = {status}")
                self.logger.debug(f"{this()}: data   = START -----------------------------")
                self.logger.debug(f"{this()}: data.type   = {type(data)}")
                self.logger.debug(f"{this()}: data.len    = {len(data)}")
                if data is not None and len(data):
                    self.logger.debug(f"data.0.type {type(data[0])}")
                    self.logger.debug(f"data.0.metadata {pformat(data[0].get('metadata'))}")
                    with open ("/tmp/volume_groups.json","w") as fp:
                        fp.write(json.dumps(data[0]))
                
                self.logger.debug(f"{this()}: data   = ------------------------------- END")
            except Exception as e:
                self.logger.error(f"{this()}EXCEPTION: {str(e)}")
        return status,data


    def getConfigurationItemsList(self,version):
        ci_list = []
        try:
            status,data = self.getVMsInformation(version)
            if status == 200:
                self.logger.warning(f"Found {len(data.get('entities'))} CIs of type VM")
                for e in data.get('entities'):
                    ci_list.append({'name': e['spec']['name'], 'uuid': e['metadata']['uuid'],'type':'VM'})
            else:
                self.logger.warning(f"VM. status = {status}. total cis={len(ci_list)}")                
        except Exception as e:
            self.logger.warning(f"VMs: No data from Nutanix. exception: ({str(e)})")
        try:
            status,data = self.getImagesInformation(version)
            if status == 200:
                self.logger.warning(f"Found {len(data.get('entities'))} CIs of type Image")
                for e in data.get('entities'):
                    ci_list.append({'name': e.get('name') , 'uuid': e.get('uuid'),'type':'IMG' })
            else:
                self.logger.warning(f"Images. status = {status}. total cis={len(ci_list)}")                
        except Exception as e:
            self.logger.warning(f"Images: No data from Nutanix. exception: ({str(e)})")
        try:
            status,data = self.getVGroupsInformation(version)
            if status == 200:
                self.logger.warning(f"Found {len(data.get('entities'))} CIs of type Volume Group")
                for e in data.get('entities'):
                    ci_list.append({'name': e.get('name') , 'uuid': e.get('uuid'),'type':'VG' })
            else:
                self.logger.warning(f"VGs. status = {status}. total cis={len(ci_list)}")                
        except Exception as e:
            self.logger.warning(f"VGs: No data from Nutanix. exception: ({str(e)})")
        try:
            self.logger.warning(f"return CI List len = {len(ci_list)}")
        except Exception as e:
            self.logger.error(f"EXCEPTION: {str(e)}")
        return ci_list
        
    def Read_Configuration(self,ini_file):
        self.ini_file = ini_file
        config = configparser.ConfigParser()
        config.read(self.ini_file)
        self.API_version    = config.getint('General','API_version')

    def Extract(self,file=None,API_version=None):
        """ Method that actually request data from Platform Platform Connection data should be available """
        if file is not None:
            json_file_name=file
        else:
            json_file_name="/tmp/collector.tmp" # then needs to call randon unique temporary file name generator
        # Here executes request to platform using platform parameters
        # -----------------------------------------------------------
        if (self.logger):
            self.logger.debug("%s: file=%s API_version=%d"%(this(),file,API_version))
        else:
            print("%s: file=%s API_version=%d"%(this(),file,API_version))
        if API_version is None:
            API_version = self.API_version
        
        self.data = []      # Cleanup Data for next "Chunk"
        status, self.data = self.getVMsInformation(API_version)
        if status == 200:
            if API_version == 2:
                self.total_matches =    int(self.data['metadata']['grand_total_entities'])
                self.processed_vms +=   int(self.data['metadata']['count'])
            elif API_version == 3:
                self.total_matches =    int(self.data['metadata']['total_matches'])
                self.processed_vms +=   int(self.data['metadata']['length'])
            if self.processed_vms >= self.total_matches:
                self.has_more_data = False
        else:
            if (self.logger):
                self.logger.error("%s: status=%s data=%s"%(this(),status,self.data))
            
        return status
        # -----------------------------------------------------------
        
    def get_vm_list(self):
        vm_list=[]
        for vm in self.data['entities']:
            vm_list.append({'name': vm['spec']['name'], 'uuid': vm['metadata']['uuid']})
        return vm_list

    def Extract_Images(self,file=None,API_version=None):
        """ Method that actually request data from Platform Platform Connection data should be available """
        if file is not None:
            json_file_name=file
        else:
            json_file_name="/tmp/collector.tmp" # then needs to call randon unique temporary file name generator
        # Here executes request to platform using platform parameters
        # -----------------------------------------------------------
        if (self.logger):
            self.logger.debug(f"{this()}: file=%s API_version={API_version}")
        else:
            print(f"{this()}: file=%s API_version={API_version}")
        if API_version is None:
            API_version = self.API_version
        
        self.data = []      # Cleanup Data for next "Chunk"
        status, self.data = self.getImagesInformation(API_version)
        if status == 200:
            if API_version == 2:
                self.total_matches =    int(self.data['metadata']['grand_total_entities'])
                self.processed_images +=   int(self.data['metadata']['total_entities'])
            elif API_version == 3:
                self.total_matches =    int(self.data['metadata']['total_matches'])
                self.processed_images +=   int(self.data['metadata']['length'])
            if self.processed_images >= self.total_matches:
                self.has_more_data = False
        else:
            if (self.logger):
                self.logger.error(f"{this()}: status={status} data={self.data}")
        return status
        # -----------------------------------------------------------

    def Extract_Snapshots(self,API_version=None):
        """ Method that actually request data from Platform Platform Connection data should be available """
        # Here executes request to platform using platform parameters
        # -----------------------------------------------------------
        if (self.logger):
            self.logger.debug(f"{this()}: file=%s API_version={API_version}")
        else:
            print            (f"{this()}: file=%s API_version={API_version}")
        if API_version is None:
            API_version = self.API_version
        
        status, self.data = self.getSnapshotsInformation(API_version)
        self.logger.debug(f"status={status} self.data={len(self.data)}")
        self.logger.debug(f"self.data.0 = {self.data[0]}")
        entities=0
        if len(self.data) and self.data[0]:
            if self.data[0].get('metadata'):
                if   API_version == 2:
                    entities = self.data[0].get('metadata').get('grand_total_entities')
                elif API_version == 3:
                    entities = self.data[0].get('metadata').get('total_matches')
            else:
                self.logger.warning(f"Invalid metadata: {self.data[0].get('metadata')}")
                
        else:
            self.logger.warning(f"Invalid data: status = {status} data={type.self.data}")
        self.logger.info(f"{this()}: API {API_version}: host:{self.host} status={status}")
        try:
            self.total_matches = 0
            # need to calculate new totals for all list previously
            for data in self.data:
                if status == 200:
                    if   API_version == 2:
                        self.total_matches += int(data['metadata'].get('grand_total_entities',0))
                    elif API_version == 3:
                        self.total_matches += int(data['metadata'].get('total_matches',0))
            # actual loop
            for data in self.data:
                if status == 200:
                    if   API_version == 2:
                        self.processed_snapshots += int(data['metadata'].get('grand_total_entities',0))
                    elif API_version == 3:
                        self.processed_snapshots += int(data['metadata'].get('total_matches',0))
                    if self.processed_snapshots >= self.total_matches:
                        self.has_more_data = False
                else:
                    if (self.logger):
                        self.logger.error(f"{this()}: status={status} data={data}")
            #elf.logger.info(f"{this()}: total matches {self.total_matches} processed snapshots: {self.processed_snapshots}")
        except Exception as e:
            self.logger.error(f"{this()}: exception={str(e)}")
            
        self.logger.debug(f"self.data                = {len(self.data)}")
        self.logger.debug(f"self.total_matches       = {self.total_matches}")
        self.logger.debug(f"self.processed_snapshots = {self.processed_snapshots}")
        self.logger.debug(f"status                   = {status}")
        self.logger.info   (f"{this()}: data={len(self.data)} protection domains,  snapshots processed ({self.processed_snapshots}/{self.total_matches}) status={status}. OUT")
        return status
        # -----------------------------------------------------------

    def Extract_VGroups(self,API_version=None):
        """ Method that actually request data from Platform Connection data should be available """
        # Here executes request to platform using platform parameters
        # -----------------------------------------------------------
        if (self.logger):
            self.logger.debug(f"{this()}: file=%s API_version={API_version}")
        else:
            print            (f"{this()}: file=%s API_version={API_version}")
        if API_version is None:
            API_version = self.API_version
        
        status, self.data = self.getVGroupsInformation(API_version)
        entities = self.data[0].get('metadata').get('grand_total_entities')
        self.logger.info(f"{this()}: host:{self.host} status={status} entities={entities} volume groups")
        try:
            self.total_matches = 0
            # need to calculate new totals for all list previously
            for data in self.data:
                if status == 200:
                    if   API_version == 2:
                        self.total_matches += int(data['metadata']['grand_total_entities'])
                    elif API_version == 3:
                        self.total_matches += int(data['metadata']['total_matches'])
            # actual loop
            for data in self.data:
                if status == 200:
                    if   API_version == 2:
                        self.processed_snapshots += int(data['metadata']['total_entities'])
                    elif API_version == 3:
                        self.processed_snapshots += int(data['metadata']['length'])
                    if self.processed_snapshots >= self.total_matches:
                        self.has_more_data = False
                else:
                    if (self.logger):
                        self.logger.error(f"{this()}: status={status} data={data}")
        except Exception as e:
            self.logger.error(f"{this()}: exception={str(e)}")
            
        return status
        # -----------------------------------------------------------
        
    def get_image_list(self):
        image_list=[]
        for image in self.data['entities']:
            image_type = None
            if 'image_type' in image.keys(): image_type=image['image_type']
            image_list.append({
                'name' : image['name'], 
                'uuid' : image['uuid'],
                'type' : image_type,
                'state': image['image_state'],
                'size' : image['vm_disk_size'],
                })
        return image_list

    def print_data(self):
        print("data['metadata']=",self.data['metadata'])
        print("data['metadata']['count']=",self.data['metadata']['count'])

        entities = self.data['metadata']['count']
        print("entities=",entities)

        for e in range(entities):
            NAME  = self.data['entities'][e]['name'] 
            UUID  = self.data['entities'][e]['uuid']
            CCPU  = self.data['entities'][e]['num_cores_per_vcpu']
            CPU   = self.data['entities'][e]['num_vcpus']
            CORES = CCPU * CPU
            RAM   = self.data['entities'][e]['memory_mb']
            RAMGB = RAM/1024
            ACTIVE= self.data['entities'][e]['power_state']
            

            print("  Entity : ",e,NAME," (",UUID,")")
            print("            ",CCPU," cores per cpu")
            print("            ",CPU," cpus")
            print("            ",CORES," cores")
            print("            ",RAM," MB",RAMGB,"GB")

            disks = len(self.data['entities'][e]['vm_disk_info'])
            print("            ",disks," disks")
    

            for d in range(disks):
                if self.data['entities'][e]['vm_disk_info'][d]['is_cdrom']:
                    print("            ",d,self.data['entities'][e]['vm_disk_info'][d]['disk_address']['disk_label']," CD-ROM")
                else:
                    bytes=0
                    disk_UUID="UNKNOWN"
                    print("            ",d,self.data['entities'][e]['vm_disk_info'][d]['disk_address']['disk_label']," DISK ")
                    if 'size' in self.data['entities'][e]['vm_disk_info'][d]:
                        bytes = self.data['entities'][e]['vm_disk_info'][d]['size']
                        kilobytes = bytes/1024
                        megabytes = kilobytes/1024
                        gigabytes = megabytes/1024
                    if 'vmdisk_uuid' in self.data['entities'][e]['vm_disk_info'][d]['disk_address']:
                        disk_UUID = self.data['entities'][e]['vm_disk_info'][d]['disk_address']['vmdisk_uuid']
                    elif 'volume_group_uuid' in self.data['entities'][e]['vm_disk_info'][d]['disk_address']:
                        disk_UUID = self.data['entities'][e]['vm_disk_info'][d]['disk_address']['volume_group_uuid']

                    print("                 (",bytes,"bytes,",gigabytes,"GB")
                    print("                 (",disk_UUID,")")
                    print("                 (",ACTIVE,")")
        print    
        print("<<<EOF>>>")

# TRANSFORMATION FUNCTIONS ---------------------------------------------
# Should Transfor input data into list of tuples ready lo load
#
    def Transform(self):
        if (self.logger): self.logger.debug("%s: Transform(). IN"%(this()))

        API_version = self.API_version

        if API_version is None:
            API_version = self.API_version
        
        if      API_version == 0:    
            entities = self.data['metadata']['count']
        elif    API_version == 1:    
            entities = self.data['metadata']['count']
        elif    API_version == 2:    
            entities = self.data['metadata']['count']
        elif    API_version == 3:    
            entities = self.data['metadata']['length']
        else:    
            if (self.logger): self.logger.error("%s:  API_version %d can't be processed"%(this(),API_version)) 
            return 1
            
        if (self.logger): self.logger.debug("%s: ETL_data_to_tuples. IN. %d entities to process"%(this(),entities)) 

        self.tuples.clear()

        NAME   = '' 
        UUID   = ''
        CCPU   = 0
        CPU    = 0
        CORES  = 0
        RAM    = 0
        ACTIVE = False
        RAMGB  = 0
        DATE   = strftime("%Y-%m-%d")
        TIME   = strftime("%H:00:00")
        disks  = 0
        nics   = 0

        for e in range(entities):
            vm    = self.data['entities'][e]

            if API_version == 0:
                pass
                
            if API_version == 1:
                pass
                
            if API_version == 2:
                NAME  = vm['name'] 
                UUID  = vm['uuid']
                CCPU  = vm['num_cores_per_vcpu']
                CPU   = vm['num_vcpus']
                CORES = CCPU * CPU
                RAM   = vm['memory_mb']
                ACTIVE= vm['power_state']
                RAMGB = RAM/1024
                DATE  = strftime("%Y-%m-%d")
                TIME  = strftime("%H:00:00")
                if any ('vm_disk_info' in x for x in vm):
                    disks = len(vm['vm_disk_info'])
                else:
                    disks = 0
                if any ('vm_nics' in x for x in vm):
                    nics  = len(vm['vm_nics'])
                else:
                    nics = 0
                
            elif API_version == 3:

                NAME  = vm['spec']['name'] 
                UUID  = vm['metadata']['uuid']
                CCPU  = 1
                #vsock = vm ['spec']['resources']['num_sockets']

                vcpux = vm ['spec']['resources']['num_vcpus_per_socket']
                vsock = vm ['spec']['resources']['num_sockets']
                CPU   = vcpux * vsock
                CORES = CCPU * CPU
                RAM   = vm ['spec']['resources']['memory_size_mib']
                ACTIVE= vm ['spec']['resources']['power_state']
                RAMGB = RAM/1024
                DATE  = strftime("%Y-%m-%d")
                TIME  = strftime("%H:00:00")

                disks = len(vm['spec']['resources']['disk_list'])
                nics  = len(vm['spec']['resources']['nic_list'])
                
            else:
                if (self.logger): self.logger.error("%s:  API_version %d can't be processed"%(this(),API_version)) 
                return 1

    
            CU_UUID = ''
            # Creates/Updates CI Mother Record
            self.tuples.append(("CI-CREATE",NAME,UUID))
            
            # Creates/Updates CU Child Records (for VM Entity)
            if self.create_VM:
                self.tuples.append(("CU-CREATE","VM" ,UUID,CU_UUID,1,"NONE",1,None,None,None))
                self.tuples.append(("CIT-CREATE","VM" ,UUID,CU_UUID,1    ,DATE,TIME,ACTIVE))
            if self.create_CPU:
                self.tuples.append(("CU-CREATE","CPU",UUID,CU_UUID,CPU,"NONE",1,None,None,None))
                self.tuples.append(("CIT-CREATE","CPU",UUID,CU_UUID,CPU  ,DATE,TIME,ACTIVE))
            if self.create_RAM:
                self.tuples.append(("CU-CREATE","RAM",UUID,CU_UUID,RAMGB,"NONE",1,None,None,None))
                self.tuples.append(("CIT-CREATE","RAM",UUID,CU_UUID,RAMGB,DATE,TIME,ACTIVE))
            if self.create_COR:
                self.tuples.append(("CU-CREATE","COR",UUID,CU_UUID,CORES,"NONE",1,None,None,None))
                self.tuples.append(("CIT-CREATE","COR",UUID,CU_UUID,CORES,DATE,TIME,ACTIVE))
            if self.create_DSK:
                for d in range(disks):
                
                    # Check if CDROM
                    is_CDROM = False
                    if API_version == 0:
                        pass
                    if API_version == 1:
                        pass
                    if API_version == 2:
                        disk = vm['vm_disk_info'][d]
                        is_CDROM = disk['is_cdrom']
                    if API_version == 3:
                        disk = vm['spec']['resources']['disk_list'][d]
                        if disk['device_properties']['device_type'] == 'CDROM':
                            is_CDROM = True
               
                    if is_CDROM:
                        pass
                    else:
                        bytes       = 0
                        kilobytes   = 0
                        megabytes   = 0
                        gigabytes   = 0
                        disk_UUID   = "UNKNOWN"
                    
                    
                        if      API_version == 0:
                                pass
                        elif    API_version == 1:
                                pass
                        elif    API_version == 2:
                            if 'size' in disk:
                                bytes = disk['size']
                            if 'vmdisk_uuid' in disk['disk_address']:
                                disk_UUID = disk['disk_address']['vmdisk_uuid']
                            elif 'volume_group_uuid' in disk['disk_address']:
                                disk_UUID = disk['disk_address']['volume_group_uuid']
                        elif    API_version == 3:
                                bytes = disk['disk_size_bytes']
                                disk_UUID = disk['uuid']
                        
                        kilobytes = bytes/1024
                        megabytes = kilobytes/1024
                        gigabytes = megabytes/1024

                        # Creates/Updates CU Child Records for Virtual Disk Drives (for VM Entity)
                        self.tuples.append(("CU-CREATE","DSK",UUID,disk_UUID,gigabytes,"NONE",1,None,None,None))
                        self.tuples.append(("CIT-CREATE","DSK",UUID,disk_UUID,gigabytes,DATE,TIME,ACTIVE))
            if self.create_NIC:
                for n in range(nics):
                    
                    mac_address = None
                    subnet_name = None
                    subnet_UUID = None
                    
                    if API_version == 0:
                        pass
                    if API_version == 1:
                        pass
                    if API_version == 2:
                        nic = vm['vm_nics'][n]
                    if API_version == 3:
                        nic = vm['spec']['resources']['nic_list'][n]
                        nic_UUID="UNKNOWN"
                        
                        if      API_version == 0:
                                pass
                        elif    API_version == 1:
                                pass
                        elif    API_version == 2:
                                nic_UUID    = nic['network_uuid']
                                mac_address = nic['mac_address']
                                subnet_name = nic['model']
                        elif    API_version == 3:
                                nic_UUID    = nic['uuid']
                                mac_address = nic['mac_address']
                                subnet_name = nic['subnet_reference']['name']
                                subnet_UUID = nic['subnet_reference']['uuid']
                        
                        # Creates/Updates CU Child Records for not Virtual Disk Drives (for VM Entity)
                        self.tuples.append(("CU-CREATE","NIC",UUID,nic_UUID,1,"NONE",1,mac_address,subnet_name,subnet_UUID))
                        self.tuples.append(("CIT-CREATE","NIC",UUID,nic_UUID,1,DATE,TIME,ACTIVE))
    
        if (self.logger): self.logger.debug("%s: Transform. OUT"%(this()))
        return 0 

    def Transform_Images(self):
        if (self.logger): self.logger.debug("%s: Transform_Images(). IN"%(this()))

        API_version = self.API_version

        if API_version is None:
            API_version = self.API_version
        
        if      API_version == 0:    
            entities = self.data['metadata']['count']
        elif    API_version == 1:    
            entities = self.data['metadata']['count']
        elif    API_version == 2:    
            entities = self.data['metadata']['total_entities']
        elif    API_version == 3:    
            entities = self.data['metadata']['length']
        else:    
            if (self.logger): self.logger.error("%s:  API_version %d can't be processed"%(this(),API_version)) 
            return 1
            
        if (self.logger): self.logger.debug("%s: ETL_data_to_tuples. IN. %d entities to process"%(this(),entities)) 

        self.tuples.clear()

        NAME   = '' 
        UUID   = ''
        DATE   = strftime("%Y-%m-%d")
        TIME   = strftime("%H:00:00")

        for e in range(entities):
            image = self.data['entities'][e]
            try:
                if API_version == 2:
                    if image['image_state'] == 'ACTIVE':
                        NAME   = image['name'] 
                        UUID   = image['uuid']
                        ACTIVE = image['image_state']
                        SIZE   = image['vm_disk_size']
                        SIZEGB = SIZE/1024/1024/1024
                        DATE   = strftime("%Y-%m-%d")
                        TIME   = strftime("%H:00:00")
                        REF1=REF2=REF3=None
                        if 'image_type' in image.keys():
                            REF1   = image['image_type']
                        if 'vm_disk_path' in image.keys():
                            REF2   = image['vm_disk_path']
                        if 'updated_time_in_usecs' in image.keys():
                            REF3   = image['updated_time_in_usecs']
                    else:
                        if (self.logger):
                            self.logger.info(
                                f"{this()}: image {image.get('name')} is not ACTIVE ({image.get('image_state')})"
                            ) 
                        
                else:
                    if (self.logger): self.logger.error("%s:  API_version %d can't be processed"%(this(),API_version)) 
                    return 1
                if ACTIVE == 'ACTIVE':
                    CU_UUID = image.get('storage_container_uuid')
                    # Creates/Updates CI Mother Record
                    self.tuples.append(("CI-CREATE",NAME,UUID))
                    # Creates/Updates CU Child Records (for IMAGE Entity)
                    self.tuples.append(("CU-CREATE","IMG",UUID,CU_UUID,SIZEGB,"NONE",1,REF1,REF2,REF3))
                    self.tuples.append(("CIT-CREATE","IMG",UUID,CU_UUID,SIZEGB,DATE,TIME,ACTIVE))
            except Exception as e:
                self.logger.error(f"image = {image}")
                emtec_handle_general_exception(e,logger=self.logger)
        if (self.logger):
            self.logger.debug("%s: Transform. OUT"%(this()))
        return 0

    def Transform_Snapshots(self,API_version=None,use_size_in_bytes=True):
        if self.logger:
            self.logger.debug(f"{this()}: Transform_Snapshots(). IN")
            if type(self.data) == list: # list of snapshots ... 
                self.logger.debug(f"{this()}: len(self.data) = {len(self.data)}")

        if API_version is None:
            API_version = self.API_version
        
        if      API_version == 0:    
            return 1
        elif    API_version == 1:    
            return 1
        elif    API_version == 2:    
            # 20210605 GV entities = len(self.data['entities'])
            entities = len(self.data)
        elif    API_version == 3:    
            return 1
        else:    
            if (self.logger): self.logger.error("%s:  API_version %d can't be processed"%(this(),API_version)) 
            return 1
            
        if (self.logger): self.logger.info("%s: ETL_data_to_tuples. IN. %d protection domains to process"%(this(),entities)) 

        self.tuples.clear()

        NAME   = '' 
        UUID   = ''
        DATE   = strftime("%Y-%m-%d")
        TIME   = strftime("%H:00:00")
        # data is actually a list oh host's snapshots, an item for
        # each host
        snapshots_count=0
        ignored_count=0
        for e in range(entities):
            # 20210605 GV snapshot = self.data['entities'][e]
            host = self.data[e]
            if (self.logger): self.logger.debug(f"API version  = {API_version} host {e} keys = {host.keys()}")
            if API_version == 2:
                if self.logger: self.logger.debug(f"{this()}: {len(host.get('entities',[]))} snapshots found ..." )
                vms_found         = 0
                local_found       = 0
                remote_found      = 0
                existent_ci       = 0
                non_existent_ci   = 0
                non_existent      = []
                non_existent_dict = {}
                control_vm        = []
                local_tuples      = {}
                for snapshot in host.get('entities',[]):
                    snapshots_count+=1
                    try: 
                        if 'vms' in snapshot.keys():
                            vms_found+=1
                            if len(snapshot['vms']):
                                NAME   = snapshot['vms'][0].get('vm_name',None)     # Nombre sera el de la 1ra VM Asociada
                                # if VM name is not available then uses consstency group name
                                if NAME is None:
                                    NAME = snapshot['vms'][0].get('consistency_group',None)
                                #CU_UUID = ''
                                UUID   = snapshot['vms'][0].get('vm_id',None)       # <==== Por ahora solo consdera UUID de 1ra maquina
                                ACTIVE = snapshot.get('state',None) ############## OJO ###############################
                                if use_size_in_bytes:
                                    SIZE   = snapshot.get('size_in_bytes',0)            # Este campo representa consumo del snapshot
                                else:
                                    SIZE   = snapshot.get('exclusive_usage_in_bytes',0) # Usable para calculo de recuperacion al borrado
                                SIZEKB = SIZE/1024
                                SIZEMB = SIZEKB/1024
                                SIZEGB = SIZEMB/1024
                                DATE   = strftime("%Y-%m-%d")
                                TIME   = strftime("%H:00:00")
                                
                                REF1   = snapshot.get('protection_domain_name',None)
                                REF2   = snapshot['vms'][0].get('consistency_group',None)
                                REF3   = snapshot['remote_site_names'][0] if len(snapshot['remote_site_names']) else None 
                                
                                ID     = snapshot.get('snapshot_id','0') 
                                
                                # Este codigo solo durante desarrollo como codigo de control 
                                '''
                                if NAME == "MV0628020": 
                                    control_vm.append(
                                        (NAME,UUID,ACTIVE,SIZEGB,ID)
                                    )
                                '''
                                # Only valid data will be recorded -------------------------
                                if NAME is not None and UUID is not None and SIZE > 0:
                                    # Creates/Updates CI Mother Record/actually this 
                                    # does not have to have any effect
                                    # it should exist prior to snapshot existence ..
                                    # Check Snapshot location and sets up proper
                                    # code depending on it
                                    # if ID is digits only then local (SNP)
                                    # if not remote (DRP), 
                                    # remote ids should be <cluster>:<digits>
                                    
                                    CI_Id = self.db.Get_CI_Id_From_UUID(UUID)
                                    
                                    # Failure VM UUID not found  will be logged and ignored
                                    if CI_Id is not None:
                                        # Check for snapshot type (local or remote)
                                        if ID.isdigit():
                                            snapshot_type_code = 'SNP'
                                            local_found+=1
                                            if (self.logger): self.logger.debug(f"{this()}: SNP VM:{NAME} {UUID} {SIZEGB}GB SNP:{ID} {ACTIVE} CI:{CI_Id}")
                                        else:
                                            snapshot_type_code = 'DRP'
                                            remote_found+=1
                                            if (self.logger): self.logger.debug(f"{this()}: DRP VM:{NAME} {UUID} {SIZEGB}GB DRP:{ID} {ACTIVE} CI:{CI_Id}")
                                        existent_ci+=1
                                        #### if first appereance of SNaPshot then creates Charge Unit
                                        #### CU_Id = self.db.Get_CU_Id_From_CI(CI_Id,snapshot_type_code)
                                        #### if (self.logger): self.logger.warning(f"{this()}: CU_Id = {CU_Id} for CI:{CI_Id} Type:{snapshot_type_code}") 
                                        #### CU_UUID = ''
                                        # will populate temporaty tuple dict to acummulate
                                        # actual snapshots data
                                        # create a key for UUID+snapshot_type_code as required
                                        if UUID not in local_tuples.keys():
                                            local_tuples.update({UUID:{}})
                                        # if first appearance then create a subkey per snap type as required
                                        if snapshot_type_code not in local_tuples.get(UUID).keys():
                                            local_tuples.get(UUID).update({
                                                snapshot_type_code:{
                                                'ci_id'  : CI_Id,
                                                'size_gb': 0,
                                                'date'   : DATE,
                                                'time'   : TIME,
                                                'active' : ACTIVE,
                                                'ref1'   : REF1,
                                                'ref2'   : REF2,
                                                'ref3'   : REF3,
                                                }
                                            })
                                        self.logger.debug(f"local_tuples.get({UUID}).update({snapshot_type_code}={local_tuples.get(UUID).get(snapshot_type_code)}")
                                        size_gb = local_tuples.get(UUID).get(snapshot_type_code).get('size_gb',0)
                                        self.logger.debug(f"size_gb={size_gb} SIZEGB={SIZEGB}")
                                        # here accummulates sizes for all snapshots of each typep on VM
                                        if ACTIVE != "EXPIRED":
                                            local_tuples.get(UUID).get(snapshot_type_code).update({ 'size_gb' : SIZEGB+size_gb })
                                            ignored_count+=1
                                        self.logger.debug(f"local_tuples.get({UUID}).get({snapshot_type_code})={local_tuples.get(UUID).get(snapshot_type_code)}")                                        
                                    else:
                                        non_existent_ci+=1
                                        non_existent.append((NAME,UUID,ACTIVE,SIZE))
                                        non_existent_dict.update({NAME:UUID})
                                        if (self.logger): self.logger.debug(f"{this()}:  Snapshot {snapshot.get('snapshot_id')} for an unknown VM {NAME}:{UUID}. ignored") 
                                        ignored_count+=1
                                else:
                                    if (self.logger):
                                        self.logger.debug(f"{this()}:  Excluded snapshot {ID} for vm: {NAME} uuid: {UUID} size: {SIZE} bytes") 
                                        if NAME is None: self.logger.debug(f"NAME is {NAME}")
                                        if UUID is None: self.logger.debug(f"UUID is {UUID}")
                                        if SIZE <=0    : self.logger.debug(f"Size is {SIZE}")
                                    ignored_count+=1
                            else:
                                if (self.logger): self.logger.debug(f"{this()}:  Snapshot {snapshot.get('snapshot_id')} have an empty VMs list. ignored") 
                                ignored_count+=1
                        else:
                            if (self.logger): self.logger.debug(f"{this()}:  Snapshot {snapshot.get('snapshot_id')} does not have a valid VMs list. ignored") 
                            ignored_count+=1
                    except Exception as e:
                            if (self.logger): self.logger.error(f"{this()}:  exception. {str(e)}") 
                            
                if self.logger:
                    self.logger.debug(f"{this()}: vms_found       = {vms_found}")
                    self.logger.debug(f"{this()}: local_found     = {local_found}")
                    self.logger.debug(f"{this()}: remote_found    = {remote_found}")
                    self.logger.debug(f"{this()}: existent_ci     = {existent_ci}")
                    self.logger.debug(f"{this()}: non_existent_ci = {non_existent_ci}")
                    self.logger.debug(f"{this()}: snapshots count = {snapshots_count}")
                    self.logger.debug(f"{this()}: ignored count   = {ignored_count}")
                    self.logger.debug(f"{this()}: NON EXISTENT VMs LIST")
                    self.logger.debug(f"\n{pformat(non_existent_dict)}")
                    '''
                    self.logger.debug(f"{this()}: CONTROLVM {len(control_vm)} snapshots")
                    if len(control_vm):
                        self.logger.debug(f"name: {control_vm[0][0]} {control_vm[0][1]}")
                    ss=0
                    for s in control_vm:
                        ss+=s[3]
                        self.logger.debug(f"stat: {s[2]:10} {s[3]:.12f} gb snap:{s[4]}")
                    self.logger.debug    (f"size: {s[2]:10} {ss:.12f} gb")
                    '''
                    self.logger.debug(f"local tuples={pformat(local_tuples)}")
                # Aqui local tuples tiene los requerimientos de actualizacion
                # consolidados a partir de estos se crearan las tuplas
                # de actualizacion necesarias
                self.logger.debug(f"local_tuples={len(local_tuples)}")
                for UUID in local_tuples:
                    for TYP_CODE in local_tuples.get(UUID):

                        SIZEGB  = local_tuples.get(UUID).get(TYP_CODE).get('size_gb',0)
                        DATE    = local_tuples.get(UUID).get(TYP_CODE).get('date')
                        TIME    = local_tuples.get(UUID).get(TYP_CODE).get('time')
                        ACTIVE  = local_tuples.get(UUID).get(TYP_CODE).get('active')
                        CI_Id   = local_tuples.get(UUID).get(TYP_CODE).get('ci_id')
                        CU_Id   = self.db.Get_CU_Id_From_CI(CI_Id,TYP_CODE) # searchs from existing CU_Id
                        CU_UUID = ""
                        REF1    = local_tuples.get(UUID).get(TYP_CODE).get('ref1')
                        REF2    = local_tuples.get(UUID).get(TYP_CODE).get('ref1')
                        REF3    = local_tuples.get(UUID).get(TYP_CODE).get('ref1')
                        if CU_Id is None or CU_Id == 0:
                            self.tuples.append(("CU-CREATE" ,snapshot_type_code,UUID,CU_UUID,SIZEGB,"NONE",1,REF1,REF2,REF3))
                            if (self.logger): self.logger.debug    (("CU-CREATE" ,TYP_CODE,UUID,CU_UUID,SIZEGB,"NONE",1,REF1,REF2,REF3))
                        self.tuples.append                  (("CIT-CREATE",TYP_CODE,UUID,CU_UUID,SIZEGB,DATE,TIME,ACTIVE))
                        if (self.logger): self.logger.debug(("CIT-CREATE",TYP_CODE,UUID,CU_UUID,SIZEGB,DATE,TIME,ACTIVE))
            else:
                if (self.logger): self.logger.error(f"{this()}: API_version {API_version} can't be processed") 
                return 1
        
        
        if (self.logger):
            self.logger.debug(f"{this()}: **************************************")
            self.logger.debug(f"{this()}: OUTPUT TUPLES")
            self.logger.debug(f"{this()}: **************************************")
            for t in self.tuples:
                self.logger.debug(f"{this()}:{self.host}: {t}")
            self.logger.debug(f"{this()}: **************************************")
            self.logger.debug(f"{this()}: Transform. OUT")
            self.logger.info (f"{this()}: tuples={len(self.tuples)}. Transform. OUT")
        return 0

    def Transform_VGroups(self,API_version=None,use_size_in_bytes=True):
        if self.logger:
            self.logger.debug(f"{this()}: Transform_VGroups(). IN")
            if type(self.data) == list: # list of volume groups ... 
                self.logger.debug(f"{this()}: len(self.data) = {len(self.data)}")

        if API_version is None:
            API_version = self.API_version
        
        if      API_version == 0:    
            return 1
        elif    API_version == 1:    
            return 1
        elif    API_version == 2:    
            # 20210605 GV entities = len(self.data['entities'])
            entities = len(self.data)
        elif    API_version == 3:    
            return 1
        else:    
            if (self.logger): self.logger.error("%s:  API_version %d can't be processed"%(this(),API_version)) 
            return 1
            
        if (self.logger): self.logger.debug("%s: ETL_data_to_tuples. IN. %d entities to process"%(this(),entities)) 

        self.tuples.clear()

        NAME   = '' 
        UUID   = ''
        DATE   = strftime("%Y-%m-%d")
        TIME   = strftime("%H:00:00")
        # data is actually a list of volume group's disks, an item for
        # each disk
        
        self.logger.debug(f"{this()} len self.data = {len(self.data)}")
        metadata=None
        entities=[]
        if len(self.data):
            metadata = self.data[0].get('metadata')
            entities = self.data[0].get('entities')
            self.logger.debug(f"{this()} metadata = {metadata}")
            self.logger.debug(f"{this()} entities = {len(entities)}")
            self.logger.debug(f"{this()} self..cc = {self.config.get('Services','default_cost_center')}")
        
        #for vg in range(len(entities)):
        vg_counter=0
        total_cits=0
        cits_counter=0
        ci_uuids=[]
        cu_uuids=[]
        vm_uuids=[]
        for vg in entities:
            ci_uuids.append(vg.get('uuid'))
            disk_list = vg.get('disk_list',[])
            attachment_list = vg.get('attachment_list',[])
            for disk in disk_list:
                if disk.get('vmdisk_uuid') is not None:
                    cu_uuids.append(disk.get('vmdisk_uuid'))
            for attachment in attachment_list:
                if attachment.get('client_uuid') is not None:
                    if self.logger:
                        self.logger.debug(f"{vg.get('uuid')} client {attachment.get('client_uuid')}")
                    vm_uuids.append(attachment.get('client_uuid'))
                elif attachment.get('vm_uuid') is not None:
                    if self.logger:
                        self.logger.debug(f"{vg.get('uuid')} vm {attachment.get('vm_uuid')}")
                    vm_uuids.append(attachment.get('vm_uuid'))
        if self.logger:
            self.logger.debug(f"input lists ...")
        self.logger.debug(f"ci_uuids={len(ci_uuids)}")
        self.logger.debug(f"cu_uuids={len(cu_uuids)}")
        self.logger.debug(f"vm_uuids={len(vm_uuids)}")
        ci_uuids = unique_list(ci_uuids)
        cu_uuids = unique_list(cu_uuids)
        vm_uuids = unique_list(vm_uuids)
        if self.logger:
            self.logger.debug(f"compacted lists ...")
        self.logger.debug(f"ci_uuids={len(ci_uuids)}")
        self.logger.debug(f"cu_uuids={len(cu_uuids)}")
        self.logger.debug(f"vm_uuids={len(vm_uuids)} {vm_uuids}")
        VMS=self.db.session.query(
            Configuration_Items.CI_UUID,    
            Configuration_Items.CI_Id,
            Configuration_Items.CC_Id
                ).filter(Configuration_Items.CC_Id!=None
                ).filter(Configuration_Items.CI_UUID.in_(vm_uuids)
                )
        #print(f"VMS query = {VMS}")
        VMS=VMS.all()
        #print(f"{len(VMS)} VMS={VMS}")
        
        CIS=self.db.session.query(
                Configuration_Items.CI_UUID,
                Configuration_Items.CI_Id                
                ).filter(Configuration_Items.CI_UUID.in_(ci_uuids)
                ).all()
        ci_ids = []
        for CI in CIS:
            ci_ids.append(CI[1])
        #print(f"{len(CIS)} CIS={CIS}")
        #print(f"{len(ci_ids)} CI ids={ci_ids}")
        CUS=self.db.session.query(Charge_Units.CU_UUID,Charge_Units.CU_Id
            ).filter(Charge_Units.CI_Id.in_(ci_ids)
            ).all()
        #print(f"{len(CUS)} CUS={CUS}")
        data={'CI':{},'CU':{},'VM':{},'CI_count':0,'CU_count':0,'VM_count':0}
        for CI in CIS:
            data['CI'].update({CI.CI_UUID:CI.CI_Id})
        for CU in CUS:
            data['CU'].update({CU.CU_UUID:CU.CU_Id})
        for VM in VMS:
            data['VM'].update({VM.CI_UUID:VM.CI_Id})
        data.update({
            'CI_count':len(data['CI']),
            'CU_count':len(data['CU']),
            'VM_count':len(data['VM']),
        })
        #print(f"data ci {len(data['CI'])}")
        #print(f"data cu {len(data['CU'])}")
        #print(f"data vm {len(data['VM'])}")
        #pprint(data)
        #print(time.strftime("%H:%M:%S"))
        #return
        prev=time.time()
        for vg in entities:
            vg_counter+=1
            if self.logger:
                self.logger.debug(f"vg {vg_counter} of {len(entities)} {vg_counter*100/len(entities):.1f}% {time.time()-prev:6.3f} seconds")
            prev=time.time()
            self.logger.debug("+++++++++++++++++++++++++++++++++++++++")
            # 20210605 GV snapshot = self.data['entities'][e]
            
            '''
            disk_list       = vg.get('disk_list',[]) 
            attachment_list = vg.get('attachment_list',[])
            uuid            = vg.get('uuid',None)
            name            = vg.get('name',None)
            description     = vg.get('description',None)
            is_shared       = vg.get('is_shared',False)
            '''
            
            try:
                disk_list       = vg['disk_list']       
            except: 
                disk_list=[] 
            try: 
                attachment_list = vg['attachment_list'] 
            except: 
                attachment_list=[]
            try: 
                uuid            = vg['uuid']            
            except: 
                uuid=None
            try: 
                name            = vg['name']            
            except: name=None
            
            # Calculates Total storage space provisionned --------------
            total_size_bytes = 0
            total_size_mb    = 0
            total_size_gb    = 0
            for d in range(len(disk_list)):
                disk=disk_list[d]
                try: 
                    size_mb    = disk['vmdisk_size_mb']    
                except: 
                    size_mb=0
                try: 
                    size_bytes = disk['vmdisk_size_bytes'] 
                except: 
                    size_bytes=0
                total_size_mb    += size_mb
                total_size_bytes += size_bytes
            total_size_gb = total_size_mb/1024
            # ----------------------------------------------------------
            self.logger.debug(f"{this()} uuid            = {uuid}")
            self.logger.debug(f"{this()} name            = {name}")
            #self.logger.debug(f"{this()} description     = {description}")
            #self.logger.debug(f"{this()} is_shared       = {is_shared}")
            self.logger.debug(f"{this()} disk_list       = {len(disk_list)}")
            self.logger.debug(f"{this()} Total Size      = {total_size_bytes} {total_size_mb} {total_size_gb}")
            self.logger.debug(f"{this()} attachment_list = {len(attachment_list)}")
            self.logger.debug(f"{this()} default cost c  = {self.config['Services']['default_cost_center']}")
            self.logger.debug(f"**************************************************")
            
            if API_version == 2:
                if self.logger: 
                    self.logger.debug(f"{this()}: {len(disk_list)} disks found ..." )
                disks_found       = 0
                vms_found         = 0
                existent_ci       = 0
                non_existent_ci   = 0
                non_existent      = []
                non_existent_dict = {}
                control_vm        = []
                local_tuples      = {}
                disk_counter = 0  
                total_cits += len(disk_list)
                prev_disk=time.time()              
                for disk in disk_list:
                    disk_counter+=1
                    if self.logger:
                        self.logger.debug(f"  disk {disk_counter:3} of {len(disk_list):3} {disk_counter*100/len(disk_list):5.1f}% {time.time()-prev_disk:6.3f} seconds")
                        prev_disk=time.time()
                    try: 
                        NAME    = vg['name']
                        UUID    = vg['uuid']
                        CU_UUID = disk['vmdisk_uuid']
                        ACTIVE  = 'on'
                        SIZE    = disk['vmdisk_size_bytes']
                        SIZEKB  = SIZE/1024
                        SIZEMB  = SIZEKB/1024
                        SIZEGB  = SIZEMB/1024
                        DATE    = strftime("%Y-%m-%d")
                        TIME    = strftime("%H:00:00")
                        
                        REF1   = 'Shared'
                        REF2   = f"disk {disk['index']}"
                        REF3   = f"{SIZEGB}GB of {total_size_gb}GB"
                        
                        ID     = None
                        
                        if self.logger:
                            self.logger.debug(f"NAME={NAME} UUID={UUID} SIZE={SIZE}")
                            self.logger.debug(f"ACTIVE={ACTIVE} DATE={DATE} TIME={TIME}")
                                                
                        # Only valid data will be recorded -------------------------
                        if NAME is not None and UUID is not None and SIZE > 0:
                            # Creates/Updates CI Mother Record/actually this 
                            # does not have to have any effect
                            # it should exist prior to disk existence ..
                            try: 
                                CI_Id = data['CI'][UUID] 
                            except: 
                                CI_Id=None
                            if self.logger: self.logger.debug(f"{this()}: CI_Id={CI_Id} UUID={UUID} CU_UUID={CU_UUID}")
                            # Failure VM UUID not found  will be logged and ignored
                            if CI_Id is not None:
                                #### if first appereance of Volume Group then creates Charge Unit if required
                                try: 
                                    CU_Id=data['CU'][CU_UUID] 
                                except:
                                    CU_Id=None
                                if self.logger:
                                    self.logger.debug(f"{this()}: CU_Id = {CU_Id} for CI:{CI_Id} Type:{'DSK'}") 
                            else:                                
                                ''' Not required until CI Tuple management accepts CC
                                # Gets CI CC if required -----------------------------------
                                cc_list = []
                                for a in range(len(attachment_list)):
                                    cc = None
                                    vm_uuid = attachment_list[a].get('vm_uuid')
                                    cc = data['VM'].get(vm_uuid,None)
                                    if cc is not None:
                                        cc_list.append(cc)
                                    self.logger.debug(f"{this()} vm_uuid={vm_uuid} cc = {cc}")
                                self.logger.debug(f"{this()} cc_list = {cc_list}")
                                cc_list = unique_list(cc_list)
                                self.logger.debug(f"{this()} cc_list = {cc_list}")
                                
                                if len(cc_list)==1:
                                    vg_cc = cc_list[0]
                                else:
                                    vg_cc = self.config.get('Services','default_cost_center')                                
                                '''
                                self.tuples.append(("CI-CREATE",NAME,UUID))
                                if (self.logger):
                                    self.logger.debug    (("CI-CREATE" ,NAME,UUID))
                                CU_Id = 0
                            if self.logger: self.logger.debug(f"{this()}: CI_Id={CI_Id} CU_Id={CU_Id} CU_UUID={CU_UUID}")
                            if CU_Id is None or CU_Id == 0:
                                # NOTE: CU Create Tuple may accept aditional Name Field
                                self.tuples.append(("CU-CREATE" ,'DSK',UUID,CU_UUID,SIZEGB,"NONE",1,REF1,REF2,REF3))
                                if self.logger:
                                    self.logger.debug    (("CU-CREATE" ,'DSK',UUID,CU_UUID,SIZEGB,"NONE",1,REF1,REF2,REF3))
                            self.tuples.append                  (("CIT-CREATE",'DSK',UUID,CU_UUID,SIZEGB,DATE,TIME,ACTIVE))
                            cits_counter+=1
                            if (self.logger):
                                self.logger.debug(("CIT-CREATE",'DSK',UUID,CU_UUID,SIZEGB,DATE,TIME,ACTIVE))
                            self.logger.debug(f"{cits_counter}/{total_cits} {cits_counter*100/total_cits:.1f}%")
                    except Exception as e:
                        if (self.logger): 
                            self.logger.error(f"{this()}: Exception {str(e)} processing disk {disk['uuid']}.")
                    '''
                    if self.logger:
                        for t in self.tuples:
                            self.logger.debug(f"{this()}:{self.host}: {t}")
                        self.logger.debug("++++++++++++++++++++++++++++++")
                    '''   
            else:
                if (self.logger): self.logger.error(f"{this()}: API_version {API_version} can't be processed") 
                return 1

        if (self.logger):
            self.logger.debug(f"{this()}: **************************************")
            self.logger.info (f"{this()}: {len(self.tuples)} OUTPUT TUPLES")
            self.logger.debug(f"{this()}: **************************************")
            for t in self.tuples:
                self.logger.debug(f"{this()}:1582 {self.host}: {t}")
            self.logger.debug(f"{this()}: **************************************")
            self.logger.debug(f"{this()}: Transform. OUT")
        return 0

# ----------------------------------------------------------------------
