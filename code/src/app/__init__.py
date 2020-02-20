#print("**** app.__init__.py ***")
# Application package constructor
# ---------------
# app.__init__.py
# ---------------
import  logging
import  configparser
from    configparser        import ConfigParser, ExtendedInterpolation

from    flask                              import Flask, render_template
from    flask_bootstrap                    import Bootstrap
from    flask_mail                         import Mail
from    flask_moment                       import Moment
from    flask_sqlalchemy                   import SQLAlchemy
from    flask_login                        import LoginManager

from    emtec.common.functions             import *
from    emtec.collector.common.context     import Context
from    emtec.collector.db.orm             import *

bootstrap                           = Bootstrap()
mail                                = Mail()
moment                              = Moment()
db                                  = Collector_ORM_DB()
login_manager                       = LoginManager()

# Setup Login manager
login_manager.session_protection    = 'strong'
login_manager.login_view            = 'auth.login'

# create logger logger
add_Logging_Levels()
logger  = logging.getLogger('Collector')

def create_app(config_file='collector.ini',config_name='production',C=None):
    config_ini = configparser.ConfigParser(interpolation=ExtendedInterpolation())
    config_ini.read( config_file )
    
    app = Flask(__name__,root_path='%s/app'%C.app_folder)
    # Calls configuration Manager 
    DATABASE_URL = "%s://%s:%s@%s:%s/%s"%(
            config_ini.get('DB','driver'),
            config_ini.get('DB','user'),
            config_ini.get('DB','password'),
            config_ini.get('DB','host'),
            config_ini.get('DB','port'),
            config_ini.get('DB','schema')
            )

    app.config.update({'COLLECTOR_CONFIG_FILE':         config_file})
    app.config.update({'SECRET_KEY':                    config_ini.get       ('General','SECRET_KEY',fallback='hard to guess string')})
    app.config.update({'SQLALCHEMY_DATABASE_URI':       DATABASE_URL})
    app.config.update({'SQLALCHEMY_COMMIT_ON_TEARDOWN': config_ini.getboolean('General','SQLALCHEMY_COMMIT_ON_TEARDOWN',fallback=True)})
    app.config.update({'SQLALCHEMY_TRACK_MODIFICATIONS':config_ini.getboolean('General','SQLALCHEMY_TRACK_MODIFICATIONS',fallback=False)})
    app.config.update({'MAIL_SERVER':                   config_ini.get       ('General','MAIL_SERVER',fallback='localhost')})
    app.config.update({'MAIL_PORT':                     config_ini.get       ('General','MAIL_PORT',fallback=25)})
    app.config.update({'MAIL_USE_TLS':                  config_ini.getboolean('General','MAIL_USE_TLS',fallback=False)})
    app.config.update({'MAIL_USE_SSL':                  config_ini.getboolean('General','MAIL_USE_SSL',fallback=False)})
    app.config.update({'MAIL_USERNAME':                 config_ini.get       ('General','MAIL_USERNAME',fallback='collector@localhost.localdomain')})
    app.config.update({'MAIL_PASSWORD':                 config_ini.get       ('General','MAIL_PASSWORD',fallback='MailPassword')})
    app.config.update({'COLLECTOR_MAIL_SUBJECT_PREFIX': config_ini.get       ('General','COLLECTOR_MAIL_SUBJECT_PREFIX',fallback='[Collector]')})
    app.config.update({'COLLECTOR_MAIL_SENDER':         config_ini.get       ('General','COLLECTOR_MAIL_SUBJECT_PREFIX',fallback='Collector Admin <gvalera@emtecgroup.net>')})
    app.config.update({'COLLECTOR_ADMIN':               config_ini.get       ('General','COLLECTOR_ADMIN',fallback='collector')})
    app.config.update({'LINES_PER_PAGE':                config_ini.getint    ('General','LINES_PER_PAGE',fallback=5)})
    app.config.update({'DEBUG':                         config_ini.getboolean('General','DEBUG',fallback=False)})
    app.config.update({'TESTING':                       config_ini.getboolean('General','TESTING',fallback=False)})
    
    if app.config['DEBUG']:
        print("create_app: %-40s = %s"%("name",__name__))
        print("create_app: %-40s = %s"%("config_file",config_file))
        print("create_app: %-40s = %s"%("config_name",config_name))
        print("create_app: %-40s = %s"%("C",C))
        print("create_app: %-40s = %s"%("C.app_folder",C.app_folder))
        print("create_app: %-40s = %s"%("config_ini",config_ini))
        for key in app.config.keys():
            if key == key.upper():
                print("create_app: %-40s = %s"%(key,app.config[key]))
        print("%-40s = %s"%("create_app: app.root_path",app.root_path))
    
    # Inititializes applications (incomplete by now)
    bootstrap.init_app      (app)
    mail.init_app           (app)
    moment.init_app         (app)
    db.init_app             (app)
    login_manager.init_app  (app)
    # Collector's modules
    
    # attach routes and custom error pages here
    from app.main   import main as main_blueprint          # NOTE: Example talks on main here .main was required . (Why?)
    app.register_blueprint(main_blueprint)
    
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    return app
    
