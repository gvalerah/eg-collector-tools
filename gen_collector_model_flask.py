def box(msg):
    print()
    print("*"*(len(msg)+4))
    print("* %s *"%msg)
    print("*"*(len(msg)+4))
    print()

box("gen collector model flask")

# Import system modules
import sys
import os

# Import logging functions
import logging

# Import SQL Alchemy related functions
from sqlalchemy                     import create_engine
from sqlalchemy                     import text
from sqlalchemy.orm                 import sessionmaker

# Import time formatter fuctions
from time                           import strftime
# Import Flask Application related functions
from flask                          import Flask
from flask_sqlalchemy               import SQLAlchemy
from config                         import config

# Collector application required modules
from emtec.collector.common.functions           import *
from emtec.collector.common.context             import Context

# Import App Modules
# Auto-Code Generation Modules
# ----------------------------------------------------------------
# This program will use specific models for Code Generation Tables
from Forms                          import Forms
from Tables                         import Tables
# ----------------------------------------------------------------
from gen.gen_functions              import print_log, Mensaje
from gen.gen_build_iterations       import Build_Iterations
from gen.gen_functions              import Dash,Do_not_modify,Dash_Jinja,Do_not_modify_Jinja
from gen.gen_populate_table_columns import Populate_Table_Columns
from gen.gen_model_base             import Gen_Model_Base
from gen.gen_model_flask            import Gen_Model_Flask
from gen.gen_model_flask            import Gen_Model_Schema
from gen.gen_views                  import Gen_Views
from gen.gen_templates              import Gen_Templates

from gen.gen_menu_functions import *

add_Logging_Levels()
logger  = logging.getLogger('Collector')
logger.propagate=False    

app = Flask(__name__)
        
# Calls configuration Manager 
app.config.from_object(config['tools'])
config['tools'].init_app(app)
"""
import configparser
xconfig = configparser.ConfigParser()
xconfig.read('gen_collector.ini')
schema = xconfig.get('General','schema',fallback='collector')
host = xconfig.get('General','host',fallback='localhost')
port = xconfig.getint('General','port',fallback=3306)
user = xconfig.get('General','user',fallback='collector')
password = xconfig.get('General','password',fallback='password')
driver = 'mysql'
dialect = 'pymysql'
exclude_tables=xconfig.get('General','exclude_tables').split(',')

engine_string = "%s+%s:http://%s:%s@%s:%s/%s"%(driver,dialect,user,password,host,port,schema)

print("engine string  =",engine_string)
print("exclude tables =",exclude_tables)
"""

db = SQLAlchemy()
db.init_app             (app)
db = create_engine(config['tools'].SQLALCHEMY_DATABASE_URI)
#db = create_engine(engine_string)

C = Context("gen_collector_model_flask","collector.ini",logger)
C.Set()
logger.name="Gen Collector Model Flask"

box("gen collector model flask: logger = %s"%logger)

# Defaults
schema = "collector"
app_folder          =   collector_folder
log_folder          =   collector_folder+"/log"
log_format          =   "col_%Y-%m-%d.log"
log_format_debug    =   "col_%Y-%m-%d-%H.log"

logger.info ("** gen_collector_model_flask: Initialized")
logger.info ("app         = %s"%(app))
#logger.info ("config_name = %s"%(config_name))
#logger.info ("config      = %s"%(config[config_name]))
logger.info ("db          = %s"%(db))
logger.info ("logger      = %s"%(logger))

    
# PUSH app context in order to make it visible 
app_ctx = app.app_context()
app_ctx.push()

logger.debug ('Number of arguments: %s arguments.'%(len(sys.argv)))
logger.debug ('Argument List      : %s'%(str(sys.argv)))

if (len(sys.argv) > 1):
    schema = sys.argv[1]
    
logger.info ('Generating code for schema: [%s]'%schema)

# 'application' code

logger.info("Start Execution")

# Connect to DB

# General variables

Session = sessionmaker(bind=db)
session = Session()

# Get Table Names using text SQL Command
logger.info("Getting Schema Tables ...")
query = text("SHOW TABLES")

#Mensaje("Getting Tables using engine=%s & query=%s"%(engine,query))
Mensaje("Getting Tables using engine=%s & query=%s"%(db,query))

# Get all DB Schema's Table names (Metadata from RDBMS instance)

TABLES = db.execute(query).fetchall()

logger.info("{} Tables in schema ...".format(len(TABLES)))

Mensaje("%d Tables found in schema. loading ..."%(len(TABLES)))

# Get Schema relationships
logger.info("Getting Schema Relationships ...")
"""
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
                   "`TABLE_SCHEMA` = SCHEMA() "            # -- Detect current schema in USE 
               "AND `REFERENCED_TABLE_NAME` IS NOT NULL "   # -- Only tables with foreign keys
	           "ORDER BY `TABLE_NAME`,`COLUMN_NAME`;") 

RELATIONS = db.execute(query).fetchall()
"""
query = text("SELECT " 
               "'collector' AS 'TABLE_SCHEMA',"                           # -- Foreign key schema
               "`Table` AS 'TABLE_NAME',"                             # -- Foreign key table
               "`Field` AS 'COLUMN_NAME',"                            # -- Foreign key column
               "'collector' AS 'REFERENCED_TABLE_SCHEMA',"                # -- Origin key schema
               "`Referenced_Table` AS 'REFERENCED_TABLE_NAME',"                  # -- Origin key table
               "`Foreign_Key` AS 'REFERENCED_COLUMN_NAME' "                 # -- Origin key column
             "FROM "
               "Dev_Forms "  # -- Will fail if user don't have privilege
             "WHERE "
               "referenced_Table IS NOT NULL "   # -- Only tables with foreign keys
	           "ORDER BY `TABLE_NAME`,`COLUMN_NAME`;") 

RELATIONS = db.execute(query).fetchall()


# Create Metadata Dictionary

Metadata = {}

Metadata.update(    {   'relations' : []  } )
Metadata.update(    {   'tables'    : {}  } )

# Create Relations List of Dictionaries
for r in range(len(RELATIONS)):
    Metadata['relations'].append    ({  'table_schema':             RELATIONS[r][0],
                                        'table_name':               RELATIONS[r][1],
                                        'column_name':              RELATIONS[r][2],
                                        'referenced_table_schema':  RELATIONS[r][3],
                                        'referenced_table_name':    RELATIONS[r][4],
                                        'referenced_column_name':   RELATIONS[r][5]
                                    })
logger.debug ("METADATA RELATIONS")
c=1
for r in Metadata['relations']:
    logger.debug ("%2d %-20s.%-20s -> %-20s.%-20s"%(c, r['table_name'], r['column_name'], r['referenced_table_name'], r['referenced_column_name']))
    print ("%2d %-20s.%-20s -> %-20s.%-20s"%(c, r['table_name'], r['column_name'], r['referenced_table_name'], r['referenced_column_name']))
    c=c+1
  
# Create Tables Dictionary
for t in range(len(TABLES)):
    Metadata['tables'].update({TABLES[t][0]:{},})

logger.info("{} Schema Relationships ...".format(len(RELATIONS)))

# Loop required for mapping class names to tables prior code generation
# 1st Loop required for context Metadata Complete

for name in Metadata['tables']:
    logger.info ('Creating Metadata for %s'%name)

    Tab                                 = Metadata['tables'][name]
    # Gets Table Data from DB Table "Dev_Tables"
    try:    
        table   = session.query(Tables).filter(Tables.Name == name).one()
    except Exception as e:
        logger.warning ("Table '%s' is not registered in Dev_Table. Code will not be generated for this table"%(name))
        Tab.update({'generate_code':False})
        continue
    
    Tab.update(             { 'generate_code'               : True                              })
    # First populate with Data from Dev_Tables
    Tab.update(             { 'table'                       : table.Name                        })
    Tab.update(             { 'caption'                     : table.Caption                     })
    Tab.update(             { 'entity'                      : table.Entity                      })
    Tab.update(             { 'class'                       : table.Class_Name                  })
    # Code Generation options
    Tab.update(             { 'child_table'                 : {'table':table.Child_Table}       })
    Tab.update(             { 'parent_table'                : {'table':table.Parent_Table}      })
    Tab.update(             { 'pagination'                  : table.Use_Pagination              })
    Tab.update(             { 'children_pagination'         : table.Use_Children_Pagination     })
    Tab.update(             { 'gen_form_one'                : table.Generate_Form_One           })
    Tab.update(             { 'gen_form_all'                : table.Generate_Form_All           })
    Tab.update(             { 'gen_form_filter'             : table.Generate_Form_Filter        })
    Tab.update(             { 'gen_children'                : table.Generate_Children           })
    Tab.update(             { 'gen_foreign_fields'          : table.Generate_Foreign_Fields     })
    # Exclude creation of standard Flask Methods 
    if name in ['Users']:
        Tab.update(         { 'gen_flask_methods'           : False                             })
    else:
        Tab.update(         { 'gen_flask_methods'           : True                              })
    
    # Permissions flags
    Tab.update(             { 'permission_view'             : table.Permission_View             })
    Tab.update(             { 'permission_delete'           : table.Permission_Delete           })
    Tab.update(             { 'permission_modify'           : table.Permission_Modify           })
    Tab.update(             { 'permission_report'           : table.Permission_Report           })
    Tab.update(             { 'permission_export'           : table.Permission_Export           })
    Tab.update(             { 'permission_view_private'     : table.Permission_View_Private     })
    Tab.update(             { 'permission_modify_private'   : table.Permission_Modify_Private   })
    Tab.update(             { 'permission_administer'       : table.Permission_Administer       })
    # Prepare fields for further Use
    Tab.update(             { 'parent'                      : {}                                })
    Tab.update(             { 'child'                       : {}                                })
    Tab.update(             { 'columns'                     : []                                })
    Tab.update(             { 'keys'                        : []                                })
    Tab.update(             { 'primary_key_auto_increment'  : ''                                })
    Tab.update(             { 'num_key_fields'              : 0                                 })
    Tab.update(             { 'relations'                   : []                                })
    Tab.update(             { 'max_column_name_length'      : 0                                 })
    Tab.update(             { 'has_child'                   : False                             })
    Tab.update(             { 'has_parent'                  : False                             })
    Tab.update(             { 'has_relations'               : False                             })
    Tab.update(             { 'has_references'              : False                             })
    Tab.update(             { 'has_fks'                     : False                             })       
    
    # New dictionary fields in the same Table
    Tab.update(             { 'code'                        : {}                    })

    Tab['code'].update(     { 'key_fields'                  : ''                    })        
    Tab['code'].update(     { 'key_params'                  : ''                    })        
    Tab['code'].update(     { 'key_redirs'                  : ''                    })        
    Tab['code'].update(     { 'non_keys_fields'             : ''                    })        
    Tab['code'].update(     { 'key_filter'                  : ''                    })        
    Tab['code'].update(     { 'row_keys'                    : ''                    })
    Tab['code'].update(     { 'my_relations'                : []                    })
    Tab['code'].update(     { 'my_joins'                    : ''                    })
    Tab['code'].update(     { 'get_choices'                 : ''                    })
    
    # ----------------------------------------------------------------------------------------------------------
    # Get Metadata of Table from DB Schema 
    # ----------------------------------------------------------------------------------------------------------
    query                               = text("SHOW COLUMNS FROM "+name)
    columns                             = db.execute(query).fetchall()
    
    for c in range(len(columns)):
        Tab['columns'].append({})
        cc=Tab['columns'][c]
        cc['field']             = columns[c][0]
        cc['type']              = columns[c][1]
        cc['type_flask']        = columns[c][1]
        cc['type_sqlalchemy']   = columns[c][1]
        cc['null']              = columns[c][2]
        cc['key']               = columns[c][3]
        cc['default']           = columns[c][4]
        cc['extra']             = columns[c][5]

# 2nd Loop All Basic Metadata is complete for all Tables 
for name in Metadata['tables']:
    Tab = Metadata['tables'][name]

    
    if Tab['generate_code']:
        logger.info ("%s generate code = %s"%(Tab['table'],Tab['generate_code']))
        Tab                                 = Metadata['tables'][name]

        # ----------------------------------------------------------------------------------------------------------
        logger.info ("    Populating columns for %s"%Tab['table'])
        Populate_Table_Columns(Metadata,Tab,session)
        # ----------------------------------------------------------------------------------------------------------
                       
        Tab.update({'key':Tab['keys'][0]})  # In case of compound keys, first component will be always primary key

        if Tab['parent_table']['table'] != 'NULL':
            Tab['has_parent']        = True
            parent   = session.query(Tables).filter(Tables.Name == table.Parent_Table).first()
            Tab['parent_table'].update({'key':''})
            try:
                form_field = session.query(Forms).filter(Forms.Table==Tab['parent_table']['table'],Forms.Key=='PRI',Forms.Extra=='auto_increment').one()
            except Exception as e:
                print("WARNING: Exception completing Metadata for '%s'"%name)
                print("WARNING: Exception =",e)
                continue
            Tab['parent_table'].update({'key':form_field.Field})
            
        # ----------------------------------------------------------------------------------------------------------
        # Populate Child Table info if required       
        # ----------------------------------------------------------------------------------------------------------
        if Tab['child_table']['table'] != 'NULL':
            logger.info ("Populating columns for %s's child %s"%(Tab['table'],Tab['child_table']['table']))
            Tab['has_child']        = True
    
            child   = session.query(Tables).filter(Tables.Name == Tab['child_table']['table']).first()
            Tab['child_table'].update({'class':child.Class_Name})
            Tab['child_table'].update({'pagination':table.Use_Children_Pagination})
            Tab['child_table'].update({'columns':[]})
            Tab['child_table'].update({'headers':[]})
            Tab['child_table'].update({'key':''})
            query                               = text("SHOW COLUMNS FROM "+Tab['child_table']['table'])
            columns                             = db.execute(query).fetchall()
            # Generate Child Data
            for c in range(len(columns)):
                try:
                    form_field = session.query(Forms).filter(Forms.Table==Tab['child_table']['table'],Forms.Field==columns[c][0]).one()
                except Exception as e:
                    logger.debug ("Exception generating child data:")
                    logger.debug ("Tab=",Tab['table'])
                    logger.debug ("child=",Tab['child_table'])
                    logger.debug ("child table =",Tab['child_table']['table'])
                    logger.debug ("column =",columns[c][0])
                    logger.debug ("EXCEPTION =",e)
                    continue                
                
                Tab['child_table']['columns'].append(form_field.Field) 
                Tab['child_table']['headers'].append(form_field.Caption_String) 
                if form_field.Key == 'PRI':
                    Tab['child']['key'] = form_field.Field 
                
        # ----------------------------------------------------------------------------------------------------------
        # Generation of iteration code for further Code Generation
        # ----------------------------------------------------------------------------------------------------------
        logger.debug ("    Building Iterations for %s"%(Tab['table']))
        Build_Iterations(Tab)
        # ----------------------------------------------------------------------------------------------------------

# 3rd Loop
# ----------------------------------------------------------------------------------------------------------
# Look for BACK REFERENCES (all tables need to be loaded)
# Find backreference relationships for tables for further class code generation
# ----------------------------------------------------------------------------------------------------------
relacion=0
for name in Metadata['tables']:
    Tab = Metadata['tables'][name]
    relacion+=1
    if Tab['generate_code']:
        logger.info ("%s buscando referencias"%(Tab['table']))
        for rel in Metadata['relations']:
            referenced_table = rel['referenced_table_name']
            relation_table = rel['table_name']
            if referenced_table == Tab['table']:
                try:
                    ref = Metadata['tables'][rel['table_name']]
                    logger.info ("    %s es referenciado por %s agregando referencia ..."%(Tab['table'],ref['table']))
                except Exception as e:
                    print()
                    print("------------------------------------------------------------------------------------------------")
                    print("WARNING : Exception @ line 379 buscando referencias para '%s' . WILL CONTINUE"%Tab['table'])
                    print("Buscando referencias para '%s'"%name)
                    print("comparando con tabla referenciada '%s' en la relacion %d"%(referenced_table,relacion))
                    print("relacion %d = %s"%(relacion,rel))
                    print("referencia ref = %s"%(ref))
                    print("Exception e =",e)
                    print("------------------------------------------------------------------------------------------------")
                    print()
                    continue
                Tab['relations'].append ( {'name':ref['table'].lower(),'class':ref['class'],\
                'backref':Tab['class'], 'caption':ref['caption'], 'table':ref['table']})

# -------------------------------------------------------------
# Actual CODE GENERATION happens here
# -------------------------------------------------------------

# --------------------------------
# Creating Base Connection module    
# --------------------------------

Gen_Model_Base(app_folder)

# This is a partial file that need to be open upon creation of DB classes

file_name = auto_includes+"/models_py_imports.py"

logger.info("Creating '%s' model import sentences ..."%(file_name))

f2 = open(file_name,"w")
f2.write(Dash)
f2.write(Do_not_modify)
f2.write(Dash)
f2.write("\n")

# --------------------------------
# Creating Table modules. Flask views and Jinja templates    
# --------------------------------
logger.info ("CODE GENERATION")
for name in Metadata['tables']:
    Tab = Metadata['tables'][name]
    if Tab['generate_code']:
        Par = Tab['parent_table']   if Tab['has_parent']    else None
        Chd = Tab['child_table']    if Tab['has_child']     else None
        parent = Tab['parent_table']['table']   if Tab['has_parent']    else None
        child  = Tab['child_table']['table']   if Tab['has_child']    else None
        logger.info ("Generating Code for %-20s (%s/%s) "%(Tab['table'],parent ,child))
        logger.info ("  Flask SQL Alchemy Models ... ")
        Gen_Model_Flask (Metadata,Tab,session,Forms,app_folder)
        logger.info ("  Flask Views ... ")
        Gen_Views       (Tab,app_folder,f2)    
        logger.info ("  HTML Jinja Templates ...")
        Gen_Templates   (Metadata,Tab,Chd,app_folder)

logger.info ("  ORM Schema Creation function for SQL Alchemy Models ... ")
Gen_Model_Schema(Metadata['tables'])
    
f2.write("\n")
f2.close()
logger.info("** gen_collector_model_flask: End Execution")

