""" 
EG Collector Test API tool
"""
import sys
import argparse
import simplejson as json
import requests
import urllib3
from   jinja2 import Environment, BaseLoader
from   emtec                  import *
from   emtec.debug            import *
import datetime

def get_args():

    # Argument's parser definitions
    parser = argparse.ArgumentParser()
    parser.add_argument('-c','--config'  ,help='Configuration filename',     required=True)
    parser.add_argument('-g','--group'   ,help='Configuration group',   required=True)
    parser.add_argument("-v",'--verbose' ,help='Increase output verbosity',action='count',required=False,default=0)

    args = parser.parse_args()
    return args
    
    
args = get_args()

def get_request(test,username,password,url,connection_timeout=5,read_timeout=20):
        session         = requests.Session()
        session.auth    = (username, password)
        session.verify  = False                                            
        session.headers.update({'Content-Type': 'application/json; charset=utf-8'})
        session.headers.update({'Accept': 'application/json;'})
        # Disable warnings
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)    
        try:
            logger.debug(f"{test.get('method')} url={url}")
            if test.get('method') == 'GET':
                serverResponse = session.get(url,timeout=(connection_timeout,read_timeout))
            elif test.get('method') == 'POST':
                serverResponse = session.post(url,timeout=(connection_timeout,read_timeout),data=json.dumps(test.get('data')))
            else:
                logger.error(f"Invalid method: {test.get('method')}")
        except ConnectionError:
            logger.error("%s: getClusterInformation: Connection Error trying version=%d call=%s URL=%s"     %(this(),version,call_type,vmsURL))            
            return  None,None
        except ConnectTimeout:
            logger.error("%s: getClusterInformation: Connection Timeout trying version=%d call=%s URL=%s"     %(this(),version,call_type,vmsURL))            
            return None,None
        except Exception as e:
            emtec_handle_general_exception(e,logger=logger,module=this())
            return None,None
        if serverResponse is not None and is_json(serverResponse.text):
            return serverResponse.status_code, json.loads(serverResponse.text)
        else:
            return serverResponse.status_code, None


if __name__ == '__main__':
    
    if args.verbose==1:
        logger_level=logging.INFO
    elif args.verbose>=1:
        logger_level=logging.DEBUG
    else:
        logger_level=logging.WARNING
            
    logger = logging.getLogger('egc_tools_snapshots')
    logger.setLevel(logger_level)
    formatter = logging.Formatter('%(asctime)s %(levelname)8s (%(lineno)3d): %(message)s')
    ch = logging.StreamHandler()
    try:
        ch.setFormatter(formatter)
        logger.addHandler(ch)
    except:
        logger.exception("creating logger ...")
    logger.debug(f"Process IN: logger={logger}")

    logger.debug(f"args={args}")
    with open(args.config) as fp:
        config=json.load(fp)
    data  = config.get(args.group)
    tests = config.get('tests')
    logger.debug(f"data={data}")
    connection_timeout=5
    read_timeout=30
    counter = 0
    total   = 0
    ok=0
    fail=0
    entities={}
    queries=open(f'egc_tools_test_api_{args.group}.txt','w')
    message = f"{args.group}:"
    logger.info(message)
    queries.write(f"{message}\n")
    Total_Protection_Domains    = 0
    Total_Snapshots             = 0
    Total_Remote_Snapshots      = 0
    Total_Snapshots_Size        = 0
    Total_Remote_Snapshots_Size = 0
    Total_Size                  = 0
    Expired_Snapshots           = 0
    # will take advantage of previous code but process just one test
    # configuration
    suffix=datetime.datetime.now().strftime("%Y%m%d_%H")
    with open(f"egc_tools_snapshots_{suffix}.csv","w") as fp:
        fp.write("HOST;VM;PD;TYPE;DATE;TIME;EDATE;ETIME;ID;UUID;STATE;SIZE;GB\n")
        for test in tests:
            if test.get('name') == 'protection_domains':
                servers = data.get(test.get('server'))
                snapshots_counter = 0
                for server in servers:
                    protocol = server.get('protocol')
                    host     = server.get('host')
                    port     = server.get('port')
                    username = server.get('username')
                    password = server.get('password')
                    base_url = server.get('base_url')
                    url = f"{protocol}://{host}:{port}/{base_url}/protection_domains"
                    logger.info(f"url={url}")
                    status,text = get_request(test,username,password,url,connection_timeout,read_timeout)
                    logger.debug(text.keys())
                    if text.get('metadata'): matches = text.get('metadata').get('grand_total_entities')
                    logger.info(f"status = {status} matches={matches}")
                    protection_domains = text.get('entities')
                    counter = 0
                    for protection_domain in protection_domains:
                        Total_Protection_Domains += 1
                        counter+=1
                        name = protection_domain.get('name')
                        url = f"{protocol}://{host}:{port}/{base_url}/protection_domains/{name}/dr_snapshots"
                        status,text = get_request(test,username,password,url,connection_timeout,read_timeout)
                        if status == 200:
                            pd_total_size = 0
                            snapshots = text.get('entities')
                            for snapshot in snapshots:
                                if snapshot.get('state') != 'EXPIRED':
                                    snapshots_counter += 1
                                    size_in_bytes = snapshot.get('size_in_bytes',0)
                                    pd_total_size += size_in_bytes
                                    ts = snapshot.get('snapshot_create_time_usecs',0)/1000000
                                    dt = datetime.datetime.fromtimestamp(ts)
                                    ts = snapshot.get('snapshot_expiry_time_usecs')
                                    #logger.warning(f"ts={ts}")
                                    if ts is not None:
                                        de = datetime.datetime.fromtimestamp(ts/1000000)
                                        expiry = f"{de.strftime('%Y-%m-%d;%H:%M:%S')}"
                                    else:
                                        de = ";"
                                    size_in_kilobytes = size_in_bytes/1024
                                    size_in_megabytes = size_in_kilobytes/1024
                                    size_in_gigabytes = size_in_megabytes/1024
                                    if snapshot.get('snapshot_id').isdigit():
                                        snapshot_type         = 'SNP'
                                        Total_Snapshots      += 1
                                        Total_Snapshots_Size += size_in_bytes
                                        Total_Size           += size_in_bytes 
                                    else:
                                        snapshot_type                = 'DRP'
                                        Total_Remote_Snapshots      += 1
                                        Total_Remote_Snapshots_Size += size_in_bytes
                                        Total_Size                  += size_in_bytes 
                                    logger.debug(
                                        f"{snapshot.get('vms')[0].get('vm_name')} "
                                        f"{dt.strftime('%Y-%m-%d,%H:%M:%S')} "
                                        f"{snapshot.get('snapshot_id')} "
                                        f"{snapshot.get('snapshot_uuid')} "
                                        f"{snapshot.get('state')} "
                                        f"{size_in_bytes:19,.0f} bytes "
                                        f"{size_in_kilobytes:,.12f} KB "
                                        f"{size_in_gigabytes:,.12f} GB "
                                        f"{pd_total_size:19,.0f} bytes"
                                    )
                                    fp.write(
                                        f"{host};"
                                        f"{snapshot.get('vms')[0].get('vm_name')};"
                                        f"{name};"
                                        f"{snapshot_type};"
                                        f"{dt.strftime('%Y-%m-%d;%H:%M:%S')};"
                                        f"{expiry};"
                                        f"{snapshot.get('snapshot_id')};"
                                        f"{snapshot.get('snapshot_uuid')};"
                                        f"{snapshot.get('state')};"
                                        f"{size_in_bytes};"
                                        f"=L{snapshots_counter+1}/1024/1024/1024\n"
                                    )
                                else:
                                    Expired_Snapshots += 1
                            logger.info(f"PD {Total_Protection_Domains:5} = {host}:{counter:04d}:{name:30} status = {status} {len(snapshots):2} snapshots size = {pd_total_size:19,.0f} bytes {pd_total_size/1024/1024/1024:10,.2f} GB")
                        #break
                    #break
                logger.info( f"Total PD               = {Total_Protection_Domains:15,.0f}" )
                logger.info( f"Total Snapshots        = {Total_Snapshots         :15,.0f}" )
                logger.info( f"Total Remote Snapshots = {Total_Remote_Snapshots  :15,.0f}" )
                logger.info( f"Expired Snapshots      = {Expired_Snapshots       :15,.0f}" )
                
                Total_Snapshots_Size_GB        = Total_Snapshots_Size       /1024/1024/1024
                Total_Remote_Snapshots_Size_GB = Total_Remote_Snapshots_Size/1024/1024/1024
                Total_Size_GB                  = Total_Size                 /1024/1024/1024
                
                Total_Snapshots_Size_TB        = Total_Snapshots_Size_GB       /1024
                Total_Remote_Snapshots_Size_TB = Total_Remote_Snapshots_Size_GB/1024
                Total_Size_TB                  = Total_Size_GB                 /1024

                logger.info(f"Total Snapshots Size        = {Total_Snapshots_Size       :20,.0f} bytes {Total_Snapshots_Size_GB       :13,.1f} GB {Total_Snapshots_Size_TB       :13,.1f} TB" )
                logger.info(f"Total Remote Snapshots Size = {Total_Remote_Snapshots_Size:20,.0f} bytes {Total_Remote_Snapshots_Size_GB:13,.1f} GB {Total_Remote_Snapshots_Size_TB:13,.1f} TB" )
                logger.info(f"Total Size                  = {Total_Size                 :20,.0f} bytes {Total_Size_GB                 :13,.1f} GB {Total_Size_TB                 :13,.1f} TB" )
                        
'''
{
    'snapshot_id': '508251375', 
    'snapshot_uuid': '1dbffd6d-3d8e-4bec-9de9-caf1b0ce4dfb', 
    'snapshot_create_time_usecs': 1640811620614485, 
    'snapshot_expiry_time_usecs': 1642021220614485, 
    'oob_schedule_ids': [], 
    'state': 'AVAILABLE', 
    'consistency_groups': ['SRVAABDHDESKD'], 
    'vms': [
        {
            'vm_handle': 916557, 
            'vm_id': '8e438431-a586-4517-ad48-4d256618e1d6', 
            'vm_name': 'SRVAABDHDESKD', 
            'vm_power_state_on_recovery': 'Powered On', 
            'consistency_group': 'SRVAABDHDESKD', 
            'app_consistent_snapshots': False, 
            'vm_recoverability': [], 
            'vm_files': [
                '/SelfServiceContainer/.acropolis/vmdisk/7faa0db5-ff95-4e25-a88c-154ce091e463', 
                '/SelfServiceContainer/.acropolis/vmdisk/bee93d12-9fac-48e8-a634-a0c367ba60b5', 
                '/SelfServiceContainer/.acropolis/vmdisk/55f72a16-787c-4c7e-9539-a6f20b216169'
                ], 
            'related_entity_uuids': []
        }
    ], 
    'nfs_files': [], 
    'volume_groups': [], 
    'missing_entities': [], 
    'located_remote_site_name': None, 
    'remote_site_names': [], 
    'size_in_bytes': 6218260992, 
    'exclusive_usage_in_bytes': 201310208
}
'''
                            

