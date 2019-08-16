# Import create_engine function
from sqlalchemy import create_engine
from sqlalchemy import text

ANO=2018
MES=10
DIA=1


status=1
is_active=1

counter = 0

CU=[[2,1],[3,1],[4,1],[5,1],[6,2097152],[7,42949672960]]


# Setup DB connection parameters
driver = "mysql+pymysql"
user =  "root"
password = "Zj1245//$$"
host = "127.0.0.1"
port = 3306
schema = "collector"
app_folder = "/home/gvalera/CODE/Python/collector"
log_folder = "/home/gvalera/CODE/Python/collector/log"
log_format = "col_%Y-%m-%d.log"
charset="utf8mb4"


print("Start Execution")

# Connect to DB
engine_string       =   str("%s://%s:%s@%s:%s/%s?charset=%s"%(driver,user,password,host,port,schema,charset))
engine              =   create_engine(engine_string)

print("Deleting Charge_Items records ...")
query = "DELETE FROM Charge_Items WHERE CU_Id > 1"
engine.execute(query)

print("Looking for Charge_Unit records ...")
query = "SELECT CU_Id,CU_Quantity FROM Charge_Units Where CU_ID > 1"

CU = engine.execute(query)

# Get Table Names using text SQL Command
print("Inserting data Schema Tables ...")

print("Inserting Charge Items ...")

for cu in CU:
    for DIA in range(1,32):
        for HORA in range(0,24):
            counter+=1
            values="%s,'%4d-%02d-%02d','%02d:00:00',%f,%d,%d"%(cu[0],ANO,MES,DIA,HORA,cu[1],status,is_active)
            query = "INSERT INTO Charge_Items VALUES(%s)"%(values)
            print("%4d %s"%(counter,query))
            engine.execute(query)
            
