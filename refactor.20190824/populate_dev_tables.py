""" ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
populate_dev_tables.py

Script designed to populate database metadata

DB Schema should be an MySQL Schema. From this it will get all required
metadata to populate table Forms
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::"""
print()
print("************************************************************")
print("** populate dev tables                                    **")
print("************************************************************")
print()
# Import system modules
import  sys
import  configparser
from    configparser            import ConfigParser, ExtendedInterpolation
# Import time formatter fuctions
from    time                    import strftime
# Import logging functions
import  logging
from    pprint                  import pprint

# Import create_engine function
from    sqlalchemy              import create_engine
from    sqlalchemy              import text
from    sqlalchemy.orm          import sessionmaker
from    sqlalchemy.exc          import IntegrityError

# Import App Modules
from    Forms                   import Forms

# Setup DB connection parameters

#from app                                import create_app,db,logger
from emtec.common.functions             import *
from emtec.collector.common.context     import Context

# Setuo additional logging levels
add_Logging_Levels()

if __name__ == "__main__":

    arguments=len(sys.argv)
    if arguments > 1:
        config_file = sys.argv[1]
        print("Will use config_file : %s"%(config_file))
        config           = configparser.ConfigParser(interpolation=ExtendedInterpolation())
        config.read(config_file)
        schema          = config['General']['schema']
        host            = config['General']['host']
        port            = config['General']['port']
        user            = config['General']['user']
        password        = config['General']['password']
        exclude_tables  = config['General']['exclude_tables']
        app_config      = config['General']['app_config']
        engine_string   = "mysql+pymysql://%s:%s@%s:%s/%s?charset=%s"%(user,password,host,port,schema,'utf8mb4')
        exclude_tables  = exclude_tables.split(',')
        engine = create_engine(engine_string)
        if engine is not None:
            print("will use engine      : %s"%(engine))
            print("will exclude tables  : %s"%(exclude_tables))
            # create logger
            logger  = logging.getLogger('Populate Development Tables')
            C = Context("populate dev tables",app_config,logger)
            C.Set()
            logger.level=C.log_level
            print("will log to          : %s"%(logger))
            if logger is not None:
                logger.name="Populate Development Tables"
                # Setup logger handlers
                fh=add_Logging_Handler(logger,C.log_level,C.log_folder,C.log_format)
                if hasattr(logging,'AUDIT'):
                    fh.addFilter(LevelFilter(logging.AUDIT))
                    ah=add_Logging_Handler(logger,logging.AUDIT,C.log_folder,C.log_format)
                pprint(logger.handlers)
        else:
            print("Incorrect DB parameters")
            sys.exit(1)
    else:
        print("Incorrect number of parameters")
        sys.exit(1)

    # 'application' code

    logger.info("Start Execution")

    # Get Schema relationships
    logger.info("Getting '%s' Schema Relationships ..."%schema)

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
                       "`TABLE_SCHEMA` =  '%s' "            # -- Forces Schema as input for population 
                   "AND `REFERENCED_TABLE_NAME` IS NOT NULL;"%schema) # -- Only tables with foreign keys

    logger.debug("Query = %s"%(query))

    RELATIONS = engine.execute(query).fetchall()

    logger.debug("Query = %s executed"%(query))

    logger.info("{} Schema Relationships ...".format(len(RELATIONS)))

    logger.info("Getting '%s' Schema Tables ..."%schema)
    query = text("SHOW TABLES IN %s"%schema)

    TABLES = engine.execute(query).fetchall()

    logger.info("{} Tables in schema ...".format(len(TABLES)))

    Session = sessionmaker(bind=engine)
    session = Session()

    new_fields=0
    for t in range(len(TABLES)):
        table_name = TABLES[t][0]
        
        if table_name in exclude_tables:
            logger.warning("OMITING TABLE '%s'"%table_name)
            continue
        
        logger.debug("Creating inserts for '%s'..."%(table_name))
        logger.debug("")
        logger.debug("Creating inserts for '%s'..."%(table_name))
        logger.debug("*******************************************")
        
        query = text("SHOW COLUMNS FROM %s.%s"%(schema,table_name))
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
                    logger.info ("\t\tPrimary Key: %s.%s.%s"%(schema,table_name,F.Field))
                    F.Validation = True 
                    F.Validation_Type = 'PK' 
                    F.Validation_String = 'Required()' 
                    
            # Updates Relations Data        
            for r in range(len(RELATIONS)):
                rel=RELATIONS[r]
                if ((rel[TABLE_NAME] == table_name) and (rel[COLUMN_NAME] == F.Field)):
                    if F.Foreign_Key is None:
                        F.Foreign_Key = rel[COLUMN_NAME]
                    if F.Referenced_Table is None:
                        F.Referenced_Table = rel[REFERENCED_TABLE_NAME]
                    if F.Foreign_Field is None:
                        F.Foreign_Field = rel[COLUMN_NAME]
                    logger.info ("\tRelationship Found(%02d %s:%s): %s.%s.%s -> %s.%s.%s" % \
                            (r,table_name,F.Field,schema,rel[1],rel[2],schema,F.Referenced_Table,F.Foreign_Field)) 
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

    logger.info("End of Execution")
    sys.exit(0)

