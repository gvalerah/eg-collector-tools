
# Import System Libs
import  json
import  shutil

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

class Nutanix:
    """ Nutanix ETL Class """

    """ Members """

    # NUTANIX Platform members
    brand           = None
    model           = None
    version         = None
    api_version     = None
    host            = None
    port            = None
    username        = None
    password        = None
    url             = None
    platform        = None
    cost_center     = None
    customer        = None
    CIT_generation  = None
    
    # DB members
    db              = None
    sql_file        = None
    
    # API members
    data            = []
    json_file_name  = None
    tuples          = []
    logger          = None
    context         = None
    API_version     = None
    session         = None
    
    # Multi version variables
    BASE_URL        = []
    base_url        = []
   
    # Resquest Session()
    session         = None
    
    # Data Creation Flags
    create_RAM      = False
    create_CPU      = False
    create_COR      = False
    create_DSK      = False
    create_NIC      = False
      
    """ Methods """

    def __init__(self,ini_file,context):
        self.Read_Configuration(ini_file)
        self.context    = context
        self.db         = self.context.db
        self.logger     = self.context.logger
        if (self.logger):
            self.logger.debug("%s: __init__ executed Read Configuration already happen."%(__name__))
            self.logger.debug("%s: ini_file       = %s "%(__name__,ini_file))
            self.logger.debug("%s: host           = %s "%(__name__,self.host))
            self.logger.debug("%s: port           = %d "%(__name__,self.port))
            self.logger.debug("%s: username       = %s "%(__name__,self.username))
            self.logger.debug("%s: password       = %s "%(__name__,self.password))
            self.logger.debug("%s: platform       = %s "%(__name__,self.platform))
            self.logger.debug("%s: customer       = %s "%(__name__,self.customer))
            self.logger.debug("%s: cost_center    = %s "%(__name__,self.cost_center))
            self.logger.debug("%s: CIT_generation = %s "%(__name__,self.CIT_generation))
            self.logger.debug("%s: API_version    = %d "%(__name__,self.API_version))
            self.logger.debug("%s: create_RAM     = %s "%(__name__,self.create_RAM))
            self.logger.debug("%s: create_CPU     = %s "%(__name__,self.create_CPU))
            self.logger.debug("%s: create_COR     = %s "%(__name__,self.create_COR))
            self.logger.debug("%s: create_DSK     = %s "%(__name__,self.create_DSK))
            self.logger.debug("%s: create_NIN     = %s "%(__name__,self.create_NIC))
        
        # Hard Coded API URL Data, Possible to go to Configuration also, incase of changes
        self.BASE_URL = []
        self.BASE_URL = [   'https://%s:%d/api/nutanix/v0.8/',
                            'https://%s:%d/PrismGateway/services/rest/v1/',
                            'https://%s:%d/api/nutanix/v2.0/',
                            'https://%s:%d/api/nutanix/v3/'
                        ]

        self.base_url = []
        for api in range(len(self.BASE_URL)):
            self.base_url.append(self.BASE_URL[api] % (self.host,self.port))
            if (self.logger):
                self.logger.debug("%s: base_url[%d]=%s"%(__name__,api,self.base_url[api]))
        
        self.session = self.get_server_session(self.username, self.password)    

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
        print ("Getting cluster information for cluster %s" % self.serverIpAddress)
        serverResponse = self.session.get(clusterURL)
        return serverResponse.status_code, json.loads(serverResponse.text)
        
    # GET VM DATA
    def getVMsInformation(self,version=None):
        if version is None:
            version = self.api_version 
    
        call = [    'vms/?includeVMDiskSizes=true&includeAddressAssignments=true',
                    'vms/',
                    'vms/?include_vm_disk_config=true&include_vm_nic_config=true',
                    'vms/list'
                    ]
        
        if version == 3:
            self.session.headers.update( {'Accept': 'application/json' } )   

        vmsURL = self.base_url[version] + call[version]

        if version == 3:
            serverResponse = self.session.post(vmsURL,'{"kind":"vm"}')
            call_type="POST"
        else:
            serverResponse = self.session.get(vmsURL)
            call_type="GET"
            
        if (self.logger):
            self.logger.debug("%s: version        = %d"%(__name__,version))
            self.logger.debug("%s: vmsURL         = %s"%(__name__,vmsURL))
            self.logger.debug("%s: call_Type      = %s"%(__name__,call_type))
            self.logger.debug("%s: serverResponse = %s"%(__name__,serverResponse))

        return serverResponse.status_code, json.loads(serverResponse.text)

        
    def Read_Configuration(self,ini_file):
        self.ini_file = ini_file
        config = configparser.ConfigParser()
        config.read(self.ini_file)
              
        self.brand          = config['General']['brand']
        self.model          = config['General']['model']
        self.version        = config['General']['version']
        self.host           = config['General']['host']
        #self.port           = int(config['General']['port'])
        self.port           = config.getint('General','port',fallback=9440)
        self.username       = config['General']['username']
        self.password       = config['General']['password']
        self.url            = config['General']['url']
        self.platform       = config['General']['platform']
        self.customer       = config['General']['default_customer']
        self.cost_center    = config['General']['default_cost_center']
        self.CIT_generation = config['General']['CIT_generation']
        """
        self.API_version    = int(config['General']['API_version'])
        self.create_RAM     = True if config['General']['create_ram'] == "True" else False
        self.create_CPU     = True if config['General']['create_cpu'] == "True" else False
        self.create_COR     = True if config['General']['create_cor'] == "True" else False
        self.create_DSK     = True if config['General']['create_dsk'] == "True" else False
        self.create_NIC     = True if config['General']['create_nic'] == "True" else False
        """
        self.API_version    = config.getint('General','API_version',fallback=2)
        self.create_RAM     = config.getboolean('General','create_ram',fallback=False)
        self.create_CPU     = config.getboolean('General','create_cpu',fallback=False)
        self.create_COR     = config.getboolean('General','create_cor',fallback=False)
        self.create_DSK     = config.getboolean('General','create_dsk',fallback=True)
        self.create_NIC     = config.getboolean('General','create_nic',fallback=False)
        
        if (self.logger):
            self.logger.debug("%s: ini_file       = %s "%(__name__,ini_file))
            self.logger.debug("%s: host           = %s "%(__name__,self.host))
            self.logger.debug("%s: port           = %d "%(__name__,self.port))
            self.logger.debug("%s: username       = %s "%(__name__,self.username))
            self.logger.debug("%s: password       = %s "%(__name__,self.password))
            self.logger.debug("%s: platform       = %s "%(__name__,self.platform))
            self.logger.debug("%s: customer       = %s "%(__name__,self.customer))
            self.logger.debug("%s: cost_center    = %s "%(__name__,self.cost_center))
            self.logger.debug("%s: CIT_generation = %s "%(__name__,self.CIT_generation))
            self.logger.debug("%s: API_version    = %d "%(__name__,self.API_version))
            self.logger.debug("%s: create_RAM     = %s "%(__name__,self.create_RAM))
            self.logger.debug("%s: create_CPU     = %s "%(__name__,self.create_CPU))
            self.logger.debug("%s: create_COR     = %s "%(__name__,self.create_COR))
            self.logger.debug("%s: create_DSK     = %s "%(__name__,self.create_DSK))
            self.logger.debug("%s: create_NIC     = %s "%(__name__,self.create_NIC))
        

    def ETL_Set_Logger(self,logger):
        self.logger = logger 
    
    def ETL_Set_SQL_Output_File(self,sql_file):
        self.sql_file = sql_file

    def ETL_request_data_001(self,file=None,API_version=None):
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
        status, self.data = self.getVMsInformation(API_version)
        return status
        # -----------------------------------------------------------

    def ETL_load_json(self):
        if (self.logger):
            self.logger.debug("  ETL_load_json. Loads '%s'"%(self.json_file_name)) 
        with open(self.json_file_name,"r") as fp:
            self.data = json.load(fp)

    def ETL_dump_data(self):
        pprint(self.data)
        
    def ETL_get_vm_list(self):
        vm_list=[]
        for vm in self.data['entities']:
            vm_list.append({'name': vm['name'], 'uuid': vm['uuid']})
        return vm_list

    def ETL_print_data(self):
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

    def ETL_data_to_tuples(self,API_version=None):
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
                vsock = vm ['spec']['resources']['num_sockets']

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
            self.tuples.append(("CU-CREATE","VM" ,UUID,CU_UUID,1,"NONE",1,'NULL','NULL','NULL'))
            self.tuples.append(("CIT-CREATE","VM" ,UUID,CU_UUID,1    ,DATE,TIME,ACTIVE))

            if self.create_CPU:
                self.tuples.append(("CU-CREATE","CPU",UUID,CU_UUID,CPU,"NONE",1,'NULL','NULL','NULL'))
                self.tuples.append(("CIT-CREATE","CPU",UUID,CU_UUID,CPU  ,DATE,TIME,ACTIVE))
            if self.create_RAM:
                self.tuples.append(("CU-CREATE","RAM",UUID,CU_UUID,RAMGB,"MBTOGB",1,'NULL','NULL','NULL'))
                self.tuples.append(("CIT-CREATE","RAM",UUID,CU_UUID,RAMGB,DATE,TIME,ACTIVE))
            if self.create_COR:
                self.tuples.append(("CU-CREATE","COR",UUID,CU_UUID,CORES,"NONE",1,'NULL','NULL','NULL'))
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
                        self.tuples.append(("CU-CREATE","DSK",UUID,disk_UUID,gigabytes,"BTOGB",1,'NULL','NULL','NULL'))
                        self.tuples.append(("CIT-CREATE","DSK",UUID,disk_UUID,gigabytes,DATE,TIME,ACTIVE))

            if self.create_DSK:
                for n in range(nics):
                    
                    mac_address = 'NULL'
                    subnet_name = 'NULL'
                    subnet_UUID = 'NULL'
                    
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
    
        if (self.logger): self.logger.debug("%s: ETL_data_to_tuples. OUT"%(__name__))
        return 0 
        
    def ETL_tuples_print(self):
        print()
        print("ETL_tuples_print().Brand: '%s' model '%s' version '%s'"%(self.brand,self.model,self.version))
        for t in range(len(self.tuples)):
            print(self.tuples[t])
        print(t,"tuples printed from data")
        print    
        print("<<<EOF>>>")
        
    def ETL_tuples_to_db(self):
        if (self.logger):
            self.logger.debug("%s: Brand: '%s' model '%s' version '%s'" % (__name__, self.brand, self.model, self.version))

        sql = None
        if (self.sql_file):
            sql = open(self.sql_file,'w')
            
        if (sql):
            self.logger.debug("%s: Saving SQL code in '%s'"%(__name__,self.sql_file))
        
        for t in range(len(self.tuples)):
            # print(".",end='',flush=True)
            T=self.tuples[t]
            transaction = T[0]
            if   transaction == "CI-CREATE":
                name = T[1]
                UUID = T[2]
                if (self.logger): self.logger.debug("Create Configuration Item '%s' with UUID '%s'.",name,UUID)
                # SQL Query call here
                query = text("CALL Create_Configuration_Item('%s','%s',%s,%s,%s,%s)"%\
                            (name,UUID,self.platform,self.cost_center,self.CIT_generation,self.customer))
                if (self.logger):
                    self.logger.debug("%s: %s"%(__name__,query))
                if (sql):
                    sql.write(str('%s;\n'%query))
                try:
                    result = self.db.execute(query)
                except exc.SQLAlchemyError:
                    if (self.logger):
                        self.logger.error("%s: Exception in [%s] %s"%(__name__,query,exc.SQLAlchemyError))
            elif transaction == "CU-CREATE":
                type            = T[1]
                CI_UUID         = T[2]
                UUID            = T[3]
                quantity        = T[4]
                operation       = T[5]
                CIT_Generation  = T[6]
                CU_Reference_1  = T[7]
                CU_Reference_2  = T[8]
                CU_Reference_3  = T[9]
                
                query = "SELECT Get_CI_Id_From_UUID('%s')"%(CI_UUID)                  
                try:
                    result = self.db.execute(query).fetchall()
                    CI_ID = result[0][0]
                    if (CI_ID):
                        query = "SELECT CI_Name FROM Configuration_Items WHERE CI_Id=%s"%(CI_ID)
                        try:
                            result = self.db.execute(query).fetchall()
                            CI_name         = result[0][0]
                            #CIT_Generation  = result[0][1]
                            CU_description = "%s - %s"%(CI_name,type)
                            if (self.logger):
                                self.logger.debug("%s: Create Charge Unit '%s'(%s) for CI='%s' with UUID '%s'" % \
                                                    (__name__, CU_description,type,CI_ID,UUID))
                            # SQL Query call here
                            query = text("CALL Create_Charge_Unit(%s,'%s','%s',TRUE,TRUE,%s,'%s','%s',%s,%s,'%s','%s','%s')" % \
                                        (CI_ID, CU_description, UUID,quantity, operation, type, self.cost_center,\
                                        CIT_Generation, CU_Reference_1, CU_Reference_2,CU_Reference_3))
                            if (self.logger):
                                self.logger.debug('%s: %s'%(__name__,query))
                            if (sql):
                                sql.write(str('%s;\n'%query))
                            try:
                                result = self.db.execute(query)
                            except exc.SQLAlchemyError:
                                if (self.logger):
                                    self.logger.error("%s: Exception in query [%s] %s"%(__name__,query,exc.SQLAlchemyError))
                        except exc.SQLAlchemyError:
                            if (self.logger):
                                self.logger.error("%s: Exception in query [%s] %s"%(__name__,query,exc.SQLAlchemyError))
                except exc.SQLAlchemyError:
                    if (self.logger):
                        self.logger.error("%s: Exception in query [%s] %s"%(__name__,query,exc.SQLAlchemyError))
                    
            elif transaction == "CIT-CREATE":
                type            =   T[1]
                CI_UUID         =   T[2]
                UUID            =   T[3]
                quantity        =   T[4]
                date            =   T[5]
                time            =   T[6]
                if T[7].lower() ==  'on':
                    active = 'TRUE'
                else:
                    active = 'FALSE'
                if (self.logger):
                    self.logger.debug("%s: Create Charge Item '%s' for CI='%s' with UUID '%s' by q=%s @ %s/%s" % \
                                        (__name__, type, CI_UUID, UUID, quantity, date, time))
                # SQL Query call here
                query = text("CALL Record_Item('%s','%s','%s',%s,'%s','%s',%s)"%(type,CI_UUID,UUID,quantity,date,time,active))
                if (self.logger):
                    self.logger.debug('%s: %s'%(__name__,query))
                if (sql):
                    sql.write(str('%s;\n'%query))
                try:
                    result = self.db.execute(query)
                except exc.SQLAlchemyError as e:
                    if (self.logger):
                        self.logger.error("%s: %s"%(__name__,e))                 
            else:
                self.logger.debug("%s: Unknown transaction: '%s'."%(__name__,transaction))

        if (sql): sql.close()
       
        if (self.logger):
            self.logger.debug("%s: ETL_tuples_to_db().%d tuples processed from data"%(__name__,len(self.tuples)))
    
