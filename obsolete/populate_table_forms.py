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
    
logger = Log('populate_table_forms',log_folder,log_format,logging.DEBUG).logger

# 'application' code

logger.info("Start Execution")

# Connect to DB
engine_string=str("%s://%s:%s@%s:%s/%s?charset=%s"%(driver,user,password,host,port,schema,charset))
engine = create_engine(engine_string)


    
# Creating Base Connection module    
#file_name=app_folder+"populate_forms.sql"

#logger.debug("Creating '%s'..."%(file_name))

#f=open(file_name,'w')



# Get Schema relationships
logger.info("Getting Schema Relationships ...")
query = text("SELECT " 
               "`TABLE_SCHEMA`,"                           # -- Foreign key schema
               "`TABLE_NAME`,"                             # -- Foreign key table
               "`COLUMN_NAME`,"                            # -- Foreign key column
               "`REFERENCED_TABLE_SCHEMA`,"                # -- Origin key schema
               "`REFERENCED_TABLE_NAME`,"                  # -- Origin key table
               "`REFERENCED_COLUMN_NAME` "                 # -- Origin key column
             "FROM"
               "`INFORMATION_SCHEMA`.`KEY_COLUMN_USAGE` "  # -- Will fail if user don't have privilege
             "WHERE"
                   "`TABLE_SCHEMA` =  'collector'"            # -- Forces Schema as input for population 
               "AND `REFERENCED_TABLE_NAME` IS NOT NULL;") # -- Only tables with foreign keys

logger.debug("Query = %s"%(query))

RELATIONS = engine.execute(query).fetchall()

logger.debug("Query = %s executed"%(query))

logger.info("{} Schema Relationships ...".format(len(RELATIONS)))

F = Forms(None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None)

#print("RELATIONS = ",RELATIONS)

logger.info("Getting Schema Tables ...")
query = text("SHOW TABLES IN collector")

TABLES = engine.execute(query).fetchall()
#print("TABLES = ",RELATIONS)

logger.info("{} Tables in schema ...".format(len(TABLES)))
    
for t in range(len(TABLES)):
    table_name = TABLES[t][0]
    logger.debug("Creating inserts for '%s'..."%(table_name))
    print("Creating inserts for '%s'..."%(table_name))
    
    # Here needs to be replaced by parameter use, next test
    query = text("SHOW COLUMNS FROM collector."+table_name)
    COLUMNS = engine.execute(query).fetchall()
    
    F = Forms(None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None)
             
    for c in range(len(COLUMNS)):
        Table   = table_name        
        Field   = COLUMNS[c][0]        
        Type    = COLUMNS[c][1]
        Null    = COLUMNS[c][2]
        Key     = COLUMNS[c][3]
        Default = COLUMNS[c][4]
        Extra   = COLUMNS[c][5]
        Foreign_Key = None
        Referenced_Table = None
        Foreign_Field = None
        Length = None
        Validation = None
        Validation_Type= None
        Validation_String = None        
        Caption_String = Field        
        Options_String = None
        
        if (Key == "PRI"):
                print ("\tPrimary Key: collector.%s.%s"%(table_name,Field))
                Validation = True 
                Validation_Type = 'PK' 
                Validation_String = 'Required()' 
                
        for r in range(len(RELATIONS)):
            rel=RELATIONS[r]
            if ((rel[1] == table_name) and (rel[2] == Field)):
                Foreign_Key = rel[2]
                Referenced_Table = rel[4]
                Foreign_Field = rel[2]
                print ("\tRelationship Found(%02d %s:%s): collector.%s.%s -> collector.%s.%s" % \
                        (r,table_name,Field,rel[1],rel[2],Referenced_Table,Foreign_Field)) 
                break
        
        F.engine = engine
        try:        
            print("F=",F,id(F))
            F.insert(Table, Field, Type, Null, Key, Default, Extra, Foreign_Key, Referenced_Table, Foreign_Field, Length, Validation, Validation_Type, Validation_String, Caption_String, Options_String)
        except IntegrityError as e:
            logger.warning("Duplicate Key Ignored : (%s/%s)"%(Table,Field))

logger.info("End Execution")

