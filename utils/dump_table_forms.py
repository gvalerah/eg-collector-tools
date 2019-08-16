# Import system modules
import sys
# Import logging functions
import logging

# Import time formatter fuctions
from time           import strftime

# Import create_engine function
from sqlalchemy         import create_engine
from sqlalchemy         import text
from sqlalchemy.orm     import sessionmaker

#import sqlalchemy.orm.exc 
from sqlalchemy.exc     import IntegrityError

# Import App Modules
from common.log import Log
from db.Forms   import Forms

from sqlalchemy import inspect

def object_as_dict(obj):
    return {c.key: getattr(obj, c.key)
            for c in inspect(obj).mapper.column_attrs}




# Setup DB connection parameters
driver = "mysql+pymysql"
user =  "root"
password = "Zj1245//$$"
host = "127.0.0.1"
port = 3306
schema = "collector_development"
app_folder = "/home/gvalera/CODE/Python/collector"
log_folder = "/home/gvalera/CODE/Python/collector/log"
log_format = "col_%Y-%m-%d.log"
charset="utf8mb4"
    
logger = Log('dump_table_forms',log_folder,log_format,logging.DEBUG).logger

# 'application' code

logger.info("Start Execution")

# Connect to DB
engine_string=str("%s://%s:%s@%s:%s/%s?charset=%s"%(driver,user,password,host,port,schema,charset))
engine = create_engine(engine_string)
    
csv_file = strftime("data/Forms_%Y%m%d_%H%M.csv")
sql_file = strftime("data/Forms_%Y%m%d_%H%M.sql")

# Get Schema relationships
print      ("Dumping form data into %s and %s ..."%(csv_file,sql_file))
logger.info("Dumping form data into %s and %s ..."%(csv_file,sql_file))

Session = sessionmaker(bind=engine)

session = Session()

form_fields = session.query(Forms).all()

fcsv=open(csv_file,"w")
fsql=open(sql_file,"w")

for ff in form_fields:
    d=object_as_dict(ff)        
    s=''
    values=''
    for k in d.keys():
        if d[k] is None:
            v='NULL'
        else:
            v=d[k]
        if k=='Length' or k=='Validation' or v=='NULL':    
            values = values + "%s%s"%(s,v)
        else:
            if v.find(',') != -1:
                values = values + '%s"%s"'  %(s,v)
            else:
                values = values + '%s%s'    %(s,v)
        s=','
    
    fsql.write ("INSERT IGNORE INTO Forms VALUES (%s);\n"   %   values)
    fcsv.write ("%s\n"                                      %   values)
fsql.close()    
fcsv.close()    

logger.info("End Execution")

