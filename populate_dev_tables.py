print()
print("************************************************************")
print("** populate dev tables                                    **")
print("************************************************************")
print()
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
#from app.common.log import Log
from Forms   import Forms

# Setup DB connection parameters

from app                             import create_app,db,logger
from app.common.context              import Context

C = Context("populate dev tables","collector.ini",logger)
C.Set()
logger.name="Populate Development Tables"

# 'application' code

logger.info("Start Execution")

# Connect to DB
#engine_string=str("%s://%s:%s@%s:%s/%s?charset=%s"%(driver,user,password,host,port,schema,charset))

engine = create_engine(C.engine_string)

# Get Schema relationships
logger.info("Getting Schema Relationships ...")

TABLE_SCHEMA                =   0   # -- Foreign key schema
TABLE_NAME                  =   1   # -- Foreign key table
COLUMN_NAME                 =   2   # -- Foreign key column
REFERENCED_TABLE_SCHEMA     =   3   # -- Origin key schema
REFERENCED_TABLE_NAME       =   4   # -- Origin key table
REFERENCED_COLUMN_NAME      =   5   # -- Origin key column

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

logger.info("Getting Schema Tables ...")
query = text("SHOW TABLES IN collector")

TABLES = engine.execute(query).fetchall()

logger.info("{} Tables in schema ...".format(len(TABLES)))

Session = sessionmaker(bind=engine)
session = Session()

new_fields=0
for t in range(len(TABLES)):
    table_name = TABLES[t][0]
    
    """
    if table_name in (["Charge_Resumes","User_Resumes"]):
        logger.warning("OMITING TABLE '%s'"%table_name)
        continue
    """
    if table_name in (["User_Resumes"]):
        logger.warning("OMITING TABLE '%s'"%table_name)
        continue
    
    logger.debug("Creating inserts for '%s'..."%(table_name))
    logger.debug("")
    logger.debug("Creating inserts for '%s'..."%(table_name))
    logger.debug("*******************************************")
    
    # Here needs to be replaced by parameter use, next test
    query = text("SHOW COLUMNS FROM collector."+table_name)
    COLUMNS = engine.execute(query).fetchall()
    
    order=1
    for c in range(len(COLUMNS)):
        field_name=COLUMNS[c][0]
        try:
            logger.debug("looking for '%s'.'%s'"%(table_name,field_name))
            forms=session.query(Forms).filter(Forms.Table==table_name).filter(Forms.Field==field_name).all()
            if len(forms)==1:
                F=forms[0]
                logger.debug("\t%s.%s FOUND !!!"%(table_name,field_name))
            else:
                logger.warning("\t**********************************************")
                logger.warning("\t%s.%s NOT FOUND in Dev_Forms!!!"%(table_name,field_name))
                logger.warning("\t**********************************************")
                F=Forms()
                F.Table   = table_name        
                F.Field   = field_name        
                F.Foreign_Key = None
                F.Referenced_Table = None
                F.Foreign_Field = None
                F.Length = None
                F.Validation = None
                F.Validation_Type= None
                F.Validation_String = None        
                F.Caption_String = field_name        
                F.Field_Order = order
                F.Field_Format = None
                F.Form_Editable = 1
                logger.warning("\t\tsession add %s.%s"%(table_name,field_name))
                session.add(F)
                new_fields+=1            
            # If Found Update data from actual DB Metadata
        except Exception as e:
            logger.error("EXCEPTION:",e)
            # If not Found initalizes record Data
            F=Forms()
            F.Table   = table_name        
            F.Field   = field_name        
            F.Foreign_Key = None
            F.Referenced_Table = None
            F.Foreign_Field = None
            F.Length = None
            F.Validation = None
            F.Validation_Type= None
            F.Validation_String = None        
            F.Caption_String = field_name        
            F.Field_Order = order
            F.Field_Format = None
            F.Form_Editable = 1
            logger.warning("\t\ŧsession add %s.%s"%(table_name,field_name))
            session.add(F)
            new_fields+=1            
            
        # Allways updates main Metadata from DB
        F.Type          = COLUMNS[c][1]
        F.Null          = COLUMNS[c][2]
        F.Key           = COLUMNS[c][3]
        F.Default       = COLUMNS[c][4]
        F.Extra         = COLUMNS[c][5]
        F.Field_Order   = order
        order=order+1
        
        # Adjust PK Data
        if (F.Key == "PRI"):
                logger.info ("\t\tPrimary Key: collector.%s.%s"%(table_name,F.Field))
                F.Validation = True 
                F.Validation_Type = 'PK' 
                F.Validation_String = 'Required()' 
                
        # Allways resets FK Data in order to re-create if needed
        #F.Foreign_Key = None
        #F.Referenced_Table = None
        #F.Foreign_Field = None
        # Updates Relations Data        
        for r in range(len(RELATIONS)):
            rel=RELATIONS[r]
            if ((rel[TABLE_NAME] == table_name) and (rel[COLUMN_NAME] == F.Field)):
                if F.Foreign_Key is None:
                    F.Foreign_Key = rel[COLUMN_NAME]
                if F.Referenced_Table is None:
                    F.Referenced_Table = rel[REFERENCED_TABLE_NAME]
                if F.Foreign_Field is None:
                    #F.Foreign_Field = rel[REFERENCED_COLUMN_NAME] forces column name because MySQL "lowers" columns names
                    F.Foreign_Field = rel[COLUMN_NAME]
                logger.info ("\tRelationship Found(%02d %s:%s): collector.%s.%s -> collector.%s.%s" % \
                        (r,table_name,F.Field,rel[1],rel[2],F.Referenced_Table,F.Foreign_Field)) 
                break
        
        try:        
            logger.debug ("\t\t\tsession add (UPDATE) %s.%s"%(table_name,field_name))
            session.add(F)
            session.commit()
        except IntegrityError as e:
            logger.warning("\tDuplicate Key Ignored : (%s/%s)"%(Table,F.Field))


session.close()

if new_fields > 0:
    logger.warning("*********************************************")
    logger.warning("%d new fields found"%new_fields)
    logger.warning("*********************************************")

logger.info("End Execution")

