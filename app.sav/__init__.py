# Application package constructor
# ---------------
# app.__init__.py
# ---------------

print()
print("module %s import entry point"%__name__)

from flask                  import Flask, render_template

""" GV 20181101 from flask.ext.bootstrap    import Bootstrap """
from flask_bootstrap        import Bootstrap

""" GV 20181101 from flask.ext.mail         import Mail """
from flask_mail             import Mail

""" GV 20181101 from flask.ext.moment       import Moment """
from flask_moment           import Moment

""" GV 20181101 from flask.ext.sqlalchemy   import SQLAlchemy """
from flask_sqlalchemy       import SQLAlchemy

from config                 import config

# Collector application required modules
from .common.context        import Context

bootstrap   = Bootstrap()
mail        = Mail()
moment      = Moment()
db          = SQLAlchemy()
print("    app/__init__.py:",id(db),"db Inicializado como",db)

C           = Context()

import logging

# create logger
logger = logging.getLogger('initial import logger')
#logger.setLevel(logging.DEBUG)

print("    app/__init__.py:",id(C),"C Inicializado como",C)

print("module %s import globals defined"%__name__)

def create_app(config_name):
    print()
    print("    app/__init__.py: ---------------------------")
    print("    app/__init__.py: create_app (config_name=%s) IN"%(config_name))
    
    app = Flask(__name__)
    
    print("    app/__init__.py: app = ",app)
    
    # Calls configuration Manager 
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # Inititializes applications (incomplete by now)
    bootstrap.init_app  (app)
    mail.init_app       (app)
    moment.init_app     (app)
    db.init_app         (app)
    # Collector's modules
    C.init_app          (app)
    logger=C.logger
 
 
    # 20181121 GV --->
    from sqlalchemy                     import create_engine

    db     = create_engine(config[config_name].SQLALCHEMY_DATABASE_URI)
    print("%s: Initilized"%(__name__))
    print("%s: app         = %s"%(__name__,app))
    print("%s: config_name = %s"%(__name__,config_name))
    print("%s: config      = %s"%(__name__,config[config_name]))
    print("%s: db          = %s"%(__name__,db))
    print("%s: logger      = %s"%(__name__,logger))

    # 20181121 GV <---
 
 
 
 
    
    # attach routes and custom error pages here
    # ---
    #Example 7-5. app/_init_.py: Blueprint registration
    print("    app/__init__.py: from .main import main as main_blueprint  ...")
    #from .main   import main as main_blueprint          # NOTE: Example talks on main here .main was required . (Why?)
    print("    app/__init__.py: app.register_blueprint(main_blueprint)  ...")    
    #app.register_blueprint(main_blueprint)
    print()
    print("    app/__init__.py:create_app completed ...")
    print()
    #config_file = "collector.ini"
    #C = Context("Collector Server",config_file)
    print("    app/__init__.py: create_app(onfig_name=%s) OUT: returns app = %s"%(config_name,app))
    print("    app/__init__.py: ---------------------------")
    print()
    # ---
    return app
    
print("module %s import exit point"%__name__)
print()



"""






# Import create_engine function
from sqlalchemy import create_engine
from sqlalchemy import text
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

driver = "mysql+pymysql"
user =  "root"
password = "Zj1245//$$"
host = "127.0.0.1"
port = 3306
schema = "collector"
schema_dev = "collector_development"
app_folder = "/home/gvalera/CODE/Python/collector"
log_folder = "/home/gvalera/CODE/Python/collector/log"
log_format = "col_%Y-%m-%d.log"
charset="utf8mb4"

# Connect to DB
engine_string       =   str("%s://%s:%s@%s:%s/%s?charset=%s"%(driver,user,password,host,port,schema,charset))
engine              =   create_engine(engine_string)
engine_string_dev   =   str("%s://%s:%s@%s:%s/%s?charset=%s"%(driver,user,password,host,port,schema_dev,charset))
engine_dev          =   create_engine(engine_string_dev)

print("%s: enfine_string_dev=%s"%(__name__,engine_string_dev))

#basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = engine_string_dev
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)
db.init_app(app)
"""
