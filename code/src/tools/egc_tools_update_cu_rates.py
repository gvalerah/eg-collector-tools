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
    
if __name__ == '__main__':
    try:
        app     = create_app('production')
        app_ctx = app.app_context()
        app_ctx.push()
        
        if len(sys.argv)<2:
            config_file = f"{os.getenv('HOME')}/collector.ini"
        else:
            config_file = sys.argv[1]
        tool_config = configparser.ConfigParser()
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
        print()
        print()
        print(db)
        print(db.session)
        print(db.engine)
        os.environ['DATABASE_URL'] = save_key
        
        print( "------------------------------------------------------")
        print(f"Update_CU_Rates {db} ...")
        print( "------------------------------------------------------")
        result = db.Update_CU_Rates(refresh_all=True)
        print(result,"registros actualizados")
        print()

    except Exception as e:
        print("EXCEPTION: %s"%(e))
        raise e
