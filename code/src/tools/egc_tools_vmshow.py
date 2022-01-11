""" --------------------------------------------------------------------
ORM DB FUNCTIONS TEST PROGRAM

IN ORDER TO EXECUTE THIS PROGRAM A VALID config.py SCRIPT SHOULD BE
PRESENT IN THE CURRENT EXECUTION FOLDER, BETTER WAY IS TO SYMBOLIC LINK
AN ACTUAL CONFIG DEFINITION, BE SURE USE 'testing' MODE AND DB FOR 
TESTING PURPOSES

---------------------------------------------------------------------"""


import  os
import  sys
import  configparser

import  requests
import  urllib3
from    flask                               import Flask
from    flask_sqlalchemy                    import SQLAlchemy
from    config                              import config
from    emtec                               import *
from    emtec.collector.db.orm              import *

db = Collector_ORM_DB()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # Inititializes applications (incomplete by now)
    db.init_app             (app)
    # Collector's modules
    return app    
    
KB=1024
MB=KB*1024
GB=MB*1024
KiB=1000
MiB=KB*1000
GiB=MB*1000
    
if __name__ == '__main__':
    try:
        app     = create_app('production')
        app_ctx = app.app_context()
        app_ctx.push()
        
        try:
            if len(sys.argv)<2:
                config_file = f"{os.getenv('HOME')}/collector.ini"
                VMNAME = "MV0628020"
            else:
                config_file = sys.argv[1]
                VMNAME = sys.argv[2]
                PE = sys.argv[3]
        except:
            print(f"Uso es: {sys.argv[0]} <ini> <vmname> <prism element section>")
            sys.exit(1)
        tool_config = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation())
        tool_config.read(config_file)
        rdbms    = tool_config.get('DB','rdbms'   ,fallback='mysql')
        dialect  = tool_config.get('DB','dialect' ,fallback='pymysql')
        user     = tool_config.get('DB','user'    ,fallback='collector')
        password = tool_config.get('DB','password',fallback='collector')
        host     = tool_config.get('DB','host'    ,fallback='127.0.0.1')
        port     = tool_config.get('DB','port'    ,fallback='3306')
        schema   = tool_config.get('DB','schema'  ,fallback='collector')
        charset  = tool_config.get('DB','charset' ,fallback='utf8mb4')
        
        save_key=os.environ['DATABASE_URL']
        os.environ['DATABASE_URL'] = f'{rdbms}{dialect}://{user}:{password}@{host}:{port}/{schema}'
        os.environ['DATABASE_URL'] = save_key
        # Need to populate customer !!!!!
        suffix=f"{customer}_{datetime.datetime.strftime(datetime.datetime.now(),'%Y%m')}"
        print()
        print(f"current period = {suffix}")
        print()
        print(f"EG COLLECTOR resume @ {datetime.datetime.now()}")
        print(f"------------------------------------------------------")
        Charge_Items.set_shard(suffix,db.engine)

        ci = db.session.query(Configuration_Items
                ).filter(Configuration_Items.CI_Name==VMNAME).one_or_none()
        if ci is None:
            print(f"Virtual machine '{VMNAME}' not found")
            sys.exit(1)
        else:
            print("MV",ci.CI_Id,ci.CI_Name)
        cus = db.session.query(Charge_Units
                ).filter(Charge_Units.CI_Id==ci.CI_Id).all()
        replications={'SNP':None,'DRP':None}
        total = 0
        for cu in cus:
            if cu.Typ_Code in ["SNP","DRP"]:
                replications[cu.Typ_Code]=cu.CU_Id
            cits= db.session.query(Charge_Items
                ).filter(Charge_Items.CU_Id==cu.CU_Id).all()
            quantity = db.session.query(
                func.sum(Charge_Items.CIT_Quantity).label("sum"),
                func.count(Charge_Items.CIT_Quantity).label("count")
                ).filter(Charge_Items.CU_Id==cu.CU_Id).all()
            q=quantity[0]
            print(f"  CU {cu.CU_Id:6d} {cu.CU_Description:20s} C={q.count:4d} Q={q.sum:20.12f} GB/hr avg:{q.sum/q.count:20.12f} GB/hr  bill:{q.sum/720:20.12f} GB/mo")
        print()
        print('REPLICATION VIEWS')
        print()
        print(f'EG Collector replication Charge Items in period {suffix}')
        print( '--------------------------------------------------------')
        counter = 0
        total   = 0
        snp     = 0
        drp     = 0
        for replication in replications:
            rows = db.session.query(Charge_Items
                ).filter(Charge_Items.CU_Id==replications[replication]).all()
            for row in rows:
                counter+=1
                print(f"  {counter:4d} {replication} {row.CIT_DateTime} {row.CIT_Quantity} GB/hr")
                total+=row.CIT_Quantity
                if replication == 'SNP': snp += row.CIT_Quantity
                if replication == 'DRP': drp += row.CIT_Quantity
        print()
        print(f"SNP   = {snp  :20,.12f} GB/hr {snp  /720:20,.12f} GB/mo")
        print(f"DRP   = {drp  :20,.12f} GB/hr {drp  /720:20,.12f} GB/mo")
        print(f"Total = {total:20,.12f} GB/hr {total/720:20,.12f} GB/mo")
        # Protection domain data
        print()
        print('Nutanix Protection Domains')
        print('--------------------------')
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)    
        
        username = tool_config.get(PE,'username',fallback='gvalera')
        password = tool_config.get(PE,'password',fallback='Pass1010.,')
        host     = tool_config.get(PE,'host'    ,fallback='10.26.1.180')
        port     = tool_config.get(PE,'port'    ,fallback='9440')
        
        url = f"https://{host}:{port}/api/nutanix/v2.0/protection_domains/"
        headers={'Accept': 'application/json' }
        result = requests.get(
            url=url,
            auth=(username,password),
            headers=headers,
            verify=False
            )
        if result is not None:
            data = result.json()
            for e in data['entities']:
                if len(e.get('vms')):
                    if e.get('vms')[0].get('vm_name') == VMNAME:
                        print(f"  pdname = {e.get('name')} {e.get('vms')[0].get('vm_name')} {int(e.get('usage_stats').get('dr.exclusive_snapshot_usage_bytes'))} bytes")
                        print(f"  pdname = {e.get('name')} {e.get('vms')[0].get('vm_name')} {int(e.get('usage_stats').get('dr.exclusive_snapshot_usage_bytes'))/GB} GB {int(e.get('usage_stats').get('dr.exclusive_snapshot_usage_bytes'))/GiB} GiB")
        else:
            print(f"error getting protection domains from host:{host} result={result}")
            sys.exit(1)
        # snapshots data
        print()
        print('Nutanix Snapshots NOW')
        print('---------------------')
        url = f"https://{host}:{port}/PrismGateway/services/rest/v2.0/protection_domains/dr_snapshots/"
        data = {"fulldetails":True}
        result = requests.get(
            url=url,
            data=data,
            auth=(username,password),
            headers=headers,
            verify=False
            )
        if result is not None:
            full_size=0
            full_reclaimable=0
            if result.ok:
                data = result.json()
                #print(data.get('metadata'))
                order=0
                count=0
                total_size =0
                total_reclaimable =0
                print(f"Total snapshots in host {host} = {len(data.get('entities'))}")
                print(f"Filtered snapshots in host {host} for VM '{VMNAME}':")
                print()
                for e in data['entities']:
                    order+=1
                    if len(e.get('vms')):
                        vm_name          =  e.get('vms')[0].get('vm_name')
                        pd_name          =  e.get('protection_domain_name')
                        size             =  int(e.get('size_in_bytes'))
                        reclaimable      =  int(e.get('exclusive_usage_in_bytes'))
                        snapshot_id      =  e.get('snapshot_id')
                        state            =  e.get('state')
                        full_size        += size
                        full_reclaimable += reclaimable
                        factor           =  reclaimable*100/size if size>0 else 0
                        if vm_name == VMNAME:
                            count += 1
                            print(  f" {count:4d} {order:4d} pdname={pd_name}"
                                    f" {vm_name} siz:{size:20,d}b {size/GB:8,.3f}GB {size/GiB:8,.3f}GiB"
                                    f" rec:{reclaimable:20,d}b {reclaimable/GB:8,.3f}GB {reclaimable/GiB:8,.3f}GiB"
                                    f" {factor:4.0f} % of size"
                                    f" id:{snapshot_id} {state}"
                                )
                            if state != 'EXPIRED':
                                total_size        += size
                                total_reclaimable += reclaimable
                print()
                total_factor = total_reclaimable*100/total_size if total_size>0 else 0
                print(f"  count = {count:4} size = {total_size:20,d} bytes reclaimable = {total_reclaimable:20,d} bytes {total_factor:4.0f}% of size")
                print(f"  count = {count:4} size = {total_size/GB:20,.6f} GB    reclaimable = {total_reclaimable/GB:20,.6f} GB")
                print(f"  count = {count:4} size = {total_size/GiB:20,.6f} GiB   reclaimable = {total_reclaimable/GiB:20,.6f} GiB")
                print()
                full_factor = full_reclaimable*100/full_size if full_size>0 else 0
                print(f"  order = {order:4} size = {full_size:20,d} bytes reclaimable = {full_reclaimable:20,d} bytes {full_factor:4.0f}% of size")
                print(f"  order = {order:4} size = {full_size/GB:20,.6f} GB    reclaimable = {full_reclaimable/GB:20,.6f} GB")
                print(f"  order = {order:4} size = {full_size/GB:20,.6f} GiB   reclaimable = {full_reclaimable/GB:20,.6f} GiB")
            else:
                print(f"  result.reason={result.reason}")
                print(f"  result.text  ={result.text}")
        else:
            print(f"invalid result from snapshots query of host {host}")
            print(f"result={result}")
            sys.exit(1)
    except Exception as e:
        print("EXCEPTION: %s"%(e))
        raise e
