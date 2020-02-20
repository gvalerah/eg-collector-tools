# Platform specific libraries
from pyVim.connect import SmartConnect, Disconnect
from pyVmomi import vim


# Import System Libs
import  json
import  ssl

# Import configuration functions
import configparser

# Import logging functions
import logging

from time       import strftime

from emtec                  import *
from emtec.class_etl        import *

class VMWare(ETL):
    """ VMware ETL Class """

    """ Members """
    
    
    # Multi version variables
    API_version     = None
    BASE_URL        = []
    base_url        = []
    total_matches   = 0
    processed_vms   = 0
    chunk_size      = 100
    has_more_data   = True
       
    # Data Creation Flags
    # create_XXX    = False
          
    """ Methods """

    def __init__(self,ini_file,logger=None,ormdb=None,db=None):
        if logger is not None:
            self.logger = logger
            self.ETL_Set_Logger(logger)

        if ormdb is not None:
            self.ormdb = ormdb
            self.db = ormdb.engine                         

        if db is not None:
            self.db = db
            
        self.Read_ETL_Configuration(ini_file)

        self.API_version = self.config.getint('General','API_version',fallback=5)
        
        if self.port == None:
            self.port = 443
        

    def LoadVmInfo(self,DATA, vm, depth=1):
        if (self.logger): self.logger.debug("%s: LoadVMInfo(). IN"%(__name__))

        #print("LoadVMInfo: type(DATA)=%s type(vm)=%s vm=%s depth=%s"%(type(DATA),type(vm),vm,depth))

        """
        Load information for a particular virtual machine or recurse into a folder
        or vApp with depth protection
        """
        maxdepth = 10
    
        # if this is a group it will have children. if it does, recurse into them
        # and then return
        if hasattr(vm, 'childEntity'):
            if depth > maxdepth:
                return
            vmList = vm.childEntity
            for c in vmList:
                self.LoadVmInfo(DATA,c, depth+1)
            return
        
        # if this is a vApp, it likely contains child VMs
        # (vApps can nest vApps, but it is hardly a common usecase, so ignore that)
        if isinstance(vm, vim.VirtualApp):
            vmList = vm.vm
            for c in vmList:
                self.LoadVmInfo(DATA,c, depth + 1)
            return

        #print("LoadVMInfo: type vm=",type(vm),"vm=",vm)

        summary = vm.summary

        DATA.append({})
        VM=len(DATA)-1

        DATA[VM].update ( {'vm'    : VM })
        DATA[VM].update ( {'name'  : summary.config.name } )
        DATA[VM].update ( {'path'  : summary.config.vmPathName } )
        DATA[VM].update ( {'guest' : summary.config.guestFullName } )
        DATA[VM].update ( {'uuid'  : summary.config.uuid } )
        DATA[VM].update ( {'ram'   : summary.config.memorySizeMB } ) #,summary.config.memorySizeMB/1024,"GB" } )
        DATA[VM].update ( {'cpu'   : summary.config.numCpu } )
        DATA[VM].update ( {'disks' : summary.config.numVirtualDisks })
        DATA[VM].update ( {'disk_list' : [] })
        
        
        DATA[VM].update ( {'nics'  : summary.config.numEthernetCards } )
        DATA[VM].update ( {'nic_list' : [] })
        for device in vm.config.hardware.device:
            if   type(device).__name__ == 'vim.vm.device.VirtualDisk':
                sumary=device.deviceInfo.summary.split(' ')
                size=int(sumary[0].replace(',','')) # size in KB
                DATA[VM]['disk_list'].append({
                                                'size':     size,
                                                'label':    device.deviceInfo.label,
                                                'uuid':     device.backing.uuid 
                                                })
            elif type(device).__name__ in ('vim.vm.device.VirtualE1000','vim.vm.device.VirtualE1000e'):
                DATA[VM]['nic_list'].append({  
                                                'name':         device.deviceInfo.summary, 
                                                'label':        device.deviceInfo.label, 
                                                'network':      str(device.backing.network).replace("'",""), 
                                                'macaddress':   device.macAddress,
                                                'type':         type(device).__name__.split('.')[3] 
                                                })
   
        # VMWare Storage Data is reported in bytes
        DATA[VM].update ( {'storage' : {
            'committed'  : summary.storage.committed,
            'uncommitted': summary.storage.uncommitted,
            'unshared'   : summary.storage.unshared,
            'total'      : summary.storage.uncommitted+summary.storage.unshared,
            'timestamp'  : str(summary.storage.timestamp)
            }})
        annotation = summary.config.annotation
        if annotation != None and annotation != "":
            DATA[VM].update({'annotation' :annotation})
                    
        DATA[VM].update({'state'      : 'ON' if summary.runtime.powerState =='poweredOn' else 'OFF'})
        
        if summary.guest != None:
            ip = summary.guest.ipAddress
        
        if ip != None and ip != "":
            DATA[VM].update({'ip'         : ip})
        
        if summary.runtime.question != None:
            DATA[VM].update({'question'  : summary.runtime.question.text})
        
        return


    def VMW_Connect(self, host, username, password, port=443, context=None):
        if (self.logger): self.logger.debug("%s: VMW_Connect(). IN"%(__name__))
        # Setup SSL Context
        if context is None:
            if hasattr(ssl, '_create_unverified_context'):
                context = ssl._create_unverified_context()
        # Connect to V Center
        if username is not None:
            self.username = username
        if password is not None:
            self.password = password

        if (self.logger):
            self.logger.debug("%s: host=%s port=%s username=%s password=%s context=%s"%(__name__,self.host,self.port,self.username,self.password,context))

        session = SmartConnect(host=host,
                         user=username,
                         pwd=password,
                         port=port,           
                         sslContext=context)
        return session
        
    
    def Extract(self,file=None,API_version=None):
        if (self.logger): self.logger.debug("%s: Extract(). IN"%(__name__))
        
        # Actual connection to V Center
        session = False
        try:
            session=self.VMW_Connect(self.host,self.username,self.password,self.port)
        except vim.fault.InvalidLogin:
            self.logger.error("%s: %s: Invalid Login trying to connect '%s:%s@%s:%s'"%(__name__,'Extract',self.username,'********',self.host,self.port))
            return None
        except TimeoutError:
            self.logger.warning("%s: %s: Timeout Error trying to connect %s:%s"%(__name__,'Extract',self.host,self.port))
            return None
        except Exception as e:
            emtec_handle_general_exception(e,logger=self.logger,module=__name__,function='Extract')
            return None
        if not session:
            if (self.logger):
                self.logger.debug("%s: Could not connect to the specified host using specified username and password"%(__name__))
   
        content = session.RetrieveContent()   # Check if retrieves all content in V Center or can/need to be "sliced"

        # Created a container for V Center Data
        self.data=[]
        # Loops for al V Center's children, LoadVMInfo is recurses into folder children
        for child in content.rootFolder.childEntity:
            if hasattr(child, 'vmFolder'):
                datacenter = child
                vmFolder = datacenter.vmFolder
                vmList = vmFolder.childEntity
                for vm in vmList:
                    #print("Extract: type vm=",type(vm),"vm=",vm)
                    self.LoadVmInfo(self.data,vm)
        status=200
        
        # NOTE: VMWare considers all data is retrieved at once, not slicing
        self.total_matches =    len(self.data)
        self.processed_vms +=   len(self.data)
        if self.processed_vms >= self.total_matches:
            self.has_more_data = False
                    
        Disconnect(session)
    
        if (self.logger): self.logger.debug("%s: Extract(). OUT returns %s"%(__name__,status))
        return status
    
    def Transform(self):
        if (self.logger): self.logger.debug("%s: Transform(). IN"%(__name__))

        API_version = self.API_version


        if API_version is None:
            API_version = self.API_version
        
        if      API_version == 5:    
            entities = len(self.data) 
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
            vm    = self.data[e]

            if API_version == 5:

                NAME  = vm['name'] 
                UUID  = vm['uuid']
                CCPU  = vm['cpu']
                #vsock = vm ['spec']['resources']['num_sockets']

                #vcpux = vm ['spec']['resources']['num_vcpus_per_socket']
                #vsock = vm ['spec']['resources']['num_sockets']
                CPU   = 1
                CORES = CCPU * CPU
                RAM   = vm ['ram']      # Validar RAM Reportada en MB conversion lineas abajo
                ACTIVE= vm ['state']    # Ajustar valor aqui
                RAMGB = RAM/1024
                DATE  = strftime("%Y-%m-%d")
                TIME  = strftime("%H:00:00")

                disks = len(vm['disk_list'])
                nics  = len(vm['nic_list'])
                
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
                
                    bytes       = 0
                    kilobytes   = 0
                    megabytes   = 0
                    gigabytes   = 0
                    disk_UUID   = "UNKNOWN"
                    
                    
                    disk = vm['disk_list'][d]

                    if      API_version == 5:
                            bytes = disk['size']*1024   # VMWare reporta summary en KB
                            disk_UUID = disk['uuid']
                    
                    kilobytes = bytes/1024
                    megabytes = kilobytes/1024
                    gigabytes = megabytes/1024

                    # Creates/Updates CU Child Records for Virtual Disk Drives (for VM Entity)
                    self.tuples.append(("CU-CREATE","DSK",UUID,disk_UUID,gigabytes,"BTOGB",1,'NULL','NULL','NULL'))
                    self.tuples.append(("CIT-CREATE","DSK",UUID,disk_UUID,gigabytes,DATE,TIME,ACTIVE))

            if self.create_NIC:
                for n in range(nics):
                    
                    mac_address = 'NULL'
                    subnet_name = 'NULL'
                    subnet_UUID = 'NULL'
                      
                    if API_version == 5:
                        nic = vm['nic_list'][n]
                        nic_UUID="UNKNOWN"
                        
                        if      API_version == 5:
                                nic_UUID    = nic['name']
                                mac_address = nic['macaddress']
                                subnet_name = nic['network']
                                subnet_UUID = nic['type']
                        
                        # Creates/Updates CU Child Records for not Virtual Disk Drives (for VM Entity)
                        self.tuples.append(("CU-CREATE","NIC",UUID,nic_UUID,1,"NONE",1,mac_address,subnet_name,subnet_UUID))
                        self.tuples.append(("CIT-CREATE","NIC",UUID,nic_UUID,1,DATE,TIME,ACTIVE))
    
        if (self.logger): self.logger.debug("%s: Transform. OUT"%(__name__))
        return 0 

"""        
        # ========================================================
        # VMWare V Center Device Types
        # ========================================================
        # device= (vim.vm.device.ParaVirtualSCSIController) 
        # device= (vim.vm.device.VirtualCdrom) 
        # device= (vim.vm.device.VirtualDisk) 
        # device= (vim.vm.device.VirtualE1000) 
        # device= (vim.vm.device.VirtualE1000e) 
        # device= (vim.vm.device.VirtualFloppy) 
        # device= (vim.vm.device.VirtualIDEController) 
        # device= (vim.vm.device.VirtualKeyboard) 
        # device= (vim.vm.device.VirtualLsiLogicController) 
        # device= (vim.vm.device.VirtualLsiLogicSASController) 
        # device= (vim.vm.device.VirtualPCIController) 
        # device= (vim.vm.device.VirtualPointingDevice) 
        # device= (vim.vm.device.VirtualPS2Controller) 
        # device= (vim.vm.device.VirtualSIOController) 
        # device= (vim.vm.device.VirtualUSBController) 
        # device= (vim.vm.device.VirtualVideoCard) 
        # device= (vim.vm.device.VirtualVMCIDevice) 
        # device= (vim.vm.device.VirtualVmxnet2) 
        # device= (vim.vm.device.VirtualVmxnet3) 
        
"""
