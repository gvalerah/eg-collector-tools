# ----------------------------------------------------------------------
# Nutanix Storage API ETL exploit Class
# code/src/service/platforms/nutanix_etl_1_0.py
# GLVH 2018
# GVLV 2021-04-03 Refactoring + Add snapshots
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
from time       import strftime

# Import sqlalchemy functions function
from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy import exc
# GV 20190818

from emtec                  import *
from emtec.debug            import *
from emtec.class_etl        import *

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
    chunk_size          = 100
    has_more_data       = True
    sharding            = False
    sharding_suffix     = None
    sharding_cit_class  = None
    
    # Data Creation Flags
    # create_XXX    = False
          
    """ Methods """

    def __init__(self,config,group,logger=None,ormdb=None,db=None):
        if logger is not None:
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
                self.logger.debug("%s: base_url[%d]=%s"%(__name__,api,self.base_url[api]))
        
        # Overrides default route for selected API version if specified in configuration
        # If URL specied
        if self.url is not None:
            if (self.logger):
                self.logger.debug("%s: overrriding base URL for version %d (%s) with URL from configuration (%s)"%(__name__,api,self.base_url[self.API_version],self.url))
            self.base_url[self.API_version]=self.url                
        else:
            # If route specified
            if (self.logger):
                self.logger.debug("%s: overrriding base URL for version %d (%s) with route from configuration (%s)"%(__name__,api,self.base_url[self.API_version],self.route))
            if self.route is not None:
                self.base_url[self.API_version]='https://%s:%d/%s'%(self.host,self.port,self.route)                

        self.logger.debug("%s: self.url        = %s"%(__name__,self.url))
        self.logger.debug("%s: self.route      = %s"%(__name__,self.route))
        self.logger.debug("%s: self.API_version= %s"%(__name__,self.API_version))
        for api in range(len(self.BASE_URL)):
            self.logger.debug("%s: %d: [%s]"%(__name__,api,self.base_url[api]))
                   
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
            self.port               = self.config.getint (node,'port',                  fallback=0)
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
            self.logger.debug("%s: username=%s password=%s"%(__name__,self.username,self.password))

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
            self.logger.error("%s: getClusterInformation: Connection Error trying version=%d call=%s URL=%s"     %(__name__,version,call_type,vmsURL))            
            return None,None
        except ConnectTimeout:
            self.logger.error("%s: getClusterInformation: Connection Timeout trying version=%d call=%s URL=%s"     %(__name__,version,call_type,vmsURL))            
            return None,None
        except Exception as e:
            emtec_handle_general_exception(e,logger=self.logger,module=__name__,function='getClusterInformation')
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
            self.logger.error("%s: getVMsInformation: Connection Error trying version=%d call=%s URL=%s"     %(__name__,version,call_type,vmsURL))            
            return None,None
        except ConnectTimeout:
            self.logger.error("%s: getVMsInformation: Connection Timeout trying version=%d call=%s URL=%s"     %(__name__,version,call_type,vmsURL))            
            return None,None
        except Exception as e:
            emtec_handle_general_exception(e,logger=self.logger,module=__name__,function='getVMsInformation')
            return None,None
        if (self.logger):
            self.logger.debug("%s: version        = %d"     %(__name__,version))
            self.logger.debug("%s: vmsURL         = %s"     %(__name__,vmsURL))
            self.logger.debug("%s: call_Type      = %s %s"  %(__name__,call_type,parameters))
            self.logger.debug("%s: serverResponse = %s"     %(__name__,serverResponse))
            if serverResponse is not None:
                self.logger.debug("%s:       Code     = %s"     %(__name__,serverResponse.status_code))
                self.logger.debug("%s:       Text     = %s"     %(__name__,serverResponse.text))

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
            self.logger.debug(f'{__name__}: version={version}')
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
                self.logger.error("%s: getImagesInformation: Connection Error trying version=%d call=%s URL=%s"     %(__name__,version,call_type,imagesURL))            
            return None,None
        except ConnectTimeout:
            if self.logger:
                self.logger.error("%s: getImagesInformation: Connection Timeout trying version=%d call=%s URL=%s"     %(__name__,version,call_type,imagesURL))            
            return None,None
        except Exception as e:
            emtec_handle_general_exception(e,logger=self.logger,module=__name__,function='getImagesInformation')
            return None,None
        if (self.logger):
            self.logger.debug("%s: version        = %d"     %(__name__,version))
            self.logger.debug("%s: imagesURL      = %s"     %(__name__,imagesURL))
            self.logger.debug("%s: call_Type      = %s %s"  %(__name__,call_type,parameters))
            self.logger.debug("%s: serverResponse = %s"     %(__name__,serverResponse))
            if serverResponse is not None:
                self.logger.debug("%s:       Code     = %s"     %(__name__,serverResponse.status_code))
                self.logger.debug("%s:       Text     = %s"     %(__name__,serverResponse.text))

        if serverResponse is not None:
            if is_json(serverResponse.text):
                data = json.loads(serverResponse.text)
            else:
                data = None
            return serverResponse.status_code, data
        else:
            return None, None

    # GET Snapshots DATA
    def getSnapshotsInformation(self,version=None):
        if self.logger:
            self.logger.debug(f'{this()}: version={version}')
        if version is None:
            version = self.api_version
        self.logger.debug(f'{__name__}: self.session={self.session} {type(self.session)}')
        #endpoint  = '/PrismGateway/services/rest/v2.0/protection_domains/dr_snapshots'
        #arguments = '/?fulldetails=true'

        call = [    '',
                    '',
                    'protection_domains/dr_snapshots/',
                    ''
                    ]
        
        if version == 2:
            self.session.headers.update( {'Accept': 'application/json' } )   

        snapshotsURL = self.base_url[version] + call[version]

        parameters=None
        
        call_type=None
        server_Response=None
        try:
            if version == 2:
                call_type="GET"
                h=strftime("%H:%M:%S")
                
                parameters = {
                    "fulldetails":True,
                    "offset":self.processed_snapshots,
                    "count":self.chunk_size,
                    "timeout":(
                        self.connection_timeout,
                        self.read_timeout),
                    }
                
                serverResponse = self.session.get(
                    snapshotsURL
                    )
            else:
                call_type="GET"
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
            emtec_handle_general_exception(e,logger=self.logger,module=__name__,function=this())
            return None,None
        if (self.logger):
            self.logger.debug(f"{this()}: version        = {version}")
            self.logger.debug(f"{this()}: snapshotsURL   = {snapshotsURL}")
            self.logger.debug(f"{this()}: call_Type      = {call_type} {parameters}")
            self.logger.debug(f"{this()}: serverResponse = {serverResponse}")
            if serverResponse is not None:
                self.logger.debug(f"{this()}:       Code     = {serverResponse.status_code}")
                self.logger.debug(f"{this()}:       Text     = {serverResponse.text}")

        if serverResponse is not None:
            if is_json(serverResponse.text):
                data = json.loads(serverResponse.text)
            else:
                data = None
            return serverResponse.status_code, data
        else:
            return None, None

            
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
            self.logger.debug("%s: file=%s API_version=%d"%(__name__,file,API_version))
        else:
            print("%s: file=%s API_version=%d"%(__name__,file,API_version))
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
                self.logger.error("%s: status=%s data=%s"%(__name__,status,self.data))
            
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
            self.logger.debug(f"{__name__}: file=%s API_version={API_version}")
        else:
            print(f"{__name__}: file=%s API_version={API_version}")
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
                self.logger.error(f"{__name__}: status={status} data={self.data}")
        return status
        # -----------------------------------------------------------

    def Extract_Snapshots(self,file=None,API_version=None):
        """ Method that actually request data from Platform Platform Connection data should be available """
        if file is not None:
            json_file_name=file
        else:
            json_file_name="/tmp/collector.tmp" # then needs to call randon unique temporary file name generator
        # Here executes request to platform using platform parameters
        # -----------------------------------------------------------
        if (self.logger):
            self.logger.debug(f"{__name__}: file=%s API_version={API_version}")
        else:
            print(f"{__name__}: file=%s API_version={API_version}")
        if API_version is None:
            API_version = self.API_version
        
        self.data = []      # Cleanup Data for next "Chunk"
        status, self.data = self.getSnapshotsInformation(API_version)
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
                self.logger.error(f"{__name__}: status={status} data={self.data}")
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
        if (self.logger): self.logger.debug("%s: Transform(). IN"%(__name__))

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
            if (self.logger): self.logger.error("%s:  API_version %d can't be processed"%(__name__,API_version)) 
            return 1
            
        if (self.logger): self.logger.debug("%s: ETL_data_to_tuples. IN. %d entities to process"%(__name__,entities)) 

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
                if (self.logger): self.logger.error("%s:  API_version %d can't be processed"%(__name__,API_version)) 
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
    
        if (self.logger): self.logger.debug("%s: Transform. OUT"%(__name__))
        return 0 

    def Transform_Images(self):
        if (self.logger): self.logger.debug("%s: Transform_Images(). IN"%(__name__))

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
            if (self.logger): self.logger.error("%s:  API_version %d can't be processed"%(__name__,API_version)) 
            return 1
            
        if (self.logger): self.logger.debug("%s: ETL_data_to_tuples. IN. %d entities to process"%(__name__,entities)) 

        self.tuples.clear()

        NAME   = '' 
        UUID   = ''
        DATE   = strftime("%Y-%m-%d")
        TIME   = strftime("%H:00:00")

        for e in range(entities):
            image = self.data['entities'][e]

            if API_version == 2:
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
                if (self.logger): self.logger.error("%s:  API_version %d can't be processed"%(__name__,API_version)) 
                return 1
            if ACTIVE == 'ACTIVE':
                CU_UUID = image['storage_container_uuid']
                # Creates/Updates CI Mother Record
                self.tuples.append(("CI-CREATE",NAME,UUID))
                # Creates/Updates CU Child Records (for IMAGE Entity)
                self.tuples.append(("CU-CREATE","IMG",UUID,CU_UUID,SIZEGB,"NONE",1,REF1,REF2,REF3))
                self.tuples.append(("CIT-CREATE","IMG",UUID,CU_UUID,SIZEGB,DATE,TIME,ACTIVE))
        if (self.logger):
            self.logger.debug("%s: Transform. OUT"%(__name__))
        return 0

    def Transform_Snapshots(self):
        if (self.logger): self.logger.debug("%s: Transform_Snapshots(). IN"%(__name__))

        API_version = self.API_version

        if API_version is None:
            API_version = self.API_version
        
        if      API_version == 0:    
            return 1
        elif    API_version == 1:    
            return 1
        elif    API_version == 2:    
            entities = len(self.data['entities'])
        elif    API_version == 3:    
            return 1
        else:    
            if (self.logger): self.logger.error("%s:  API_version %d can't be processed"%(__name__,API_version)) 
            return 1
            
        if (self.logger): self.logger.debug("%s: ETL_data_to_tuples. IN. %d entities to process"%(__name__,entities)) 

        self.tuples.clear()

        NAME   = '' 
        UUID   = ''
        DATE   = strftime("%Y-%m-%d")
        TIME   = strftime("%H:00:00")

        for e in range(entities):
            snapshot = self.data['entities'][e]
            self.logger.debug(f"snapshot {e} = {pformat(snapshot)}")
            self.logger.debug(f"API version  = {API_version}")
            if API_version == 2:
                if len(snapshot['vms']):
                    NAME   = snapshot['vms'][0].get('vm_name',None)  # Nombre sera el de la 1ra VM Asociada
                    if NAME is None:
                        NAME = snapshot['vms'][0].get('consistency_group',None)
                    CU_UUID = None
                    UUID   = snapshot['vms'][0].get('vm_id',None)    # <==== Por ahora solo consdera 1ra maquina
                    ACTIVE = snapshot.get('state',None) ############## OJO ###############################
                    SIZE   = snapshot.get('exclusive_usage_in_bytes',0)
                    SIZEGB = SIZE/1024/1024/1024
                    DATE   = strftime("%Y-%m-%d")
                    TIME   = strftime("%H:00:00")
                    if len(snapshot['remote_site_names']):
                        REF1   = snapshot['remote_site_names'][0]
                    else:
                        REF1   = None
                    REF2   = snapshot.get('protection_domain_name',None)
                    REF3   = snapshot['vms'][0].get('consistency_group',None)
                                # Only valid data will be recorded -------------------------
                    if NAME is not None and UUID is not None and SIZE > 0:
                        # Creates/Updates CI Mother Record/actually this 
                        # does not have to have any effect
                        # it should exist prior to SNP existence ..........
                        # Check Snapshot location and sets up proper
                        # code depending on it
                        if location == 'local':
                            snapshot_type_code = 'SNP'
                        else:
                            snapshot_type_code = 'DRP'
                        if self.db.Get_CI_Id_From_UUID(UUID) is not None:
                            # if first appereance of SNaPshot then creates Charge Unit
                            self.tuples.append(("CU-CREATE" ,snapshot_type_code,UUID,CU_UUID,SIZEGB,"NONE",1,REF1,REF2,REF3))
                            self.tuples.append(("CIT-CREATE",snapshot_type_code,UUID,CU_UUID,SIZEGB,DATE,TIME,ACTIVE))
                        else:
                            if (self.logger): self.logger.debug(f"{this()}:  Snapshot {snapshot.get('snapshot_id')} for an unknown VM {NAME}:{UUID}. ignored") 
                else:
                    if (self.logger): self.logger.debug(f"{this()}:  Snapshot {snapshot.get('snapshot_id')} does not have a valid VMs list. ignored") 
            else:
                if (self.logger): self.logger.error("%s:  API_version %d can't be processed"%(__name__,API_version)) 
                return 1
        if (self.logger):
            self.logger.debug("%s: Transform. OUT"%(__name__))
        return 0

# ----------------------------------------------------------------------
