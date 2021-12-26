# ----------------------------------------------------------------------
# Application package constructor
# ----------------------------------------------------------------------
import  base64
import  logging
from    configparser                        import ConfigParser
from    configparser                        import ExtendedInterpolation

from    flask                               import Flask
from    flask                               import render_template
from    flask_bootstrap                     import Bootstrap
from    flask_mail                          import Mail
from    flask_moment                        import Moment
from    flask_sqlalchemy                    import SQLAlchemy
from    flask_login                         import LoginManager
# GV 20210705
from flask_login                        import login_user
from flask_login                        import logout_user
from flask_login                        import login_required
from flask_login                        import current_user
from flask                              import current_app

from    emtec.common.functions              import *
#from    emtec.collector.common.functions    import *
from    emtec.collector.db.orm              import *

# Expand System libraries ----------------------------------------------
add_Logging_Levels()

# Local objects --------------------------------------------------------
bootstrap                           = Bootstrap()
mail                                = Mail()
moment                              = Moment()
login_manager                       = LoginManager()
# Setup Login manager
login_manager.session_protection    = 'strong'
login_manager.login_view            = 'auth.login'

# Common Application wide objects --------------------------------------
db                                  = Collector_ORM_DB()
# create logger logger. Logger name need to be hardcoded at creation
# time, need to evaluate variable naming
logger                              = logging.getLogger(__name__)
# ----------------------------------------------------------------------

# Application Initialization function
def create_flask_app(app_name,config_file=None):
    config_ini = configparser.ConfigParser(interpolation=ExtendedInterpolation())
    if config_file is None:
        config_file = f'{app_name.lower()}.ini'
    config_ini.read( config_file )
    app_code      = app_name.lower()
    app_key       = app_name.upper()
    app_folder    = config_ini.get('General','app_folder',fallback='.')
    app_root_path = f'{app_folder}/app'
    app           = Flask(app_name,root_path=app_root_path)

    logger.name   = app_name
    
    # setup all driver specifics here ----------------------------------
    rdbms   = config_ini.get('DB','rdbms'  ,fallback='mysql')
    dialect = config_ini.get('DB','dialect',fallback='pymysql')
    if dialect is not None and len(dialect)>0:
        driver = f"{rdbms}+{dialect}"
    else:
        driver = rdbms
    # setup engine specifics
    if rdbms == 'mysql':
        charset=config_ini.get('DB','charset',fallback=None)
        if charset is not None:
            charset='?charset=%s'%str(charset)
        else:
            charset=''
    else:
        charset=''
    # setup full connection engine here
    DATABASE_URL = "%s://%s:%s@%s:%s/%s%s"%(
            config_ini.get('DB','driver',   fallback=driver),
            config_ini.get('DB','user',     ),
            config_ini.get('DB','password', ),
            config_ini.get('DB','host',     fallback='localhost'),
            config_ini.get('DB','port',     fallback=3306),
            config_ini.get('DB','schema',   fallback='collector'),
            charset
            )
    # Application app config variables here ------------------------------
    app.config.update({f'{app_key}_CONFIG_FILE':         config_file})
    app.config.update({f'{app_key}_MAIL_SUBJECT_PREFIX': config_ini.get       ('General',f'{app_key}_MAIL_SUBJECT_PREFIX',fallback=f'[{app_name}]')})
    app.config.update({f'{app_key}_MAIL_SENDER':         config_ini.get       ('General',f'{app_key}_MAIL_SUBJECT_PREFIX',fallback=f'{app_name} Admin <gvalera@emtecgroup.net>')})
    app.config.update({f'{app_key}_ADMIN':               config_ini.get       ('General',f'{app_key}_ADMIN',fallback='collector')})
    app.config.update({f'{app_key}_CIT_SHARDING':        config_ini.getboolean('General',f'{app_key}_CIT_SHARDING',fallback=False)})
    
    # default Flask app config settings --------------------------------
    app.config.update({'NAME':                          config_ini.get       ('General','NAME',fallback='Collector')})
    app.config.update({'SECRET_KEY':                    config_ini.get       ('General','SECRET_KEY',fallback='Hard to guess string')})
    app.config.update({'SQLALCHEMY_DATABASE_URI':       DATABASE_URL})
    app.config.update({'SQLALCHEMY_COMMIT_ON_TEARDOWN': config_ini.getboolean('General','SQLALCHEMY_COMMIT_ON_TEARDOWN',fallback=True)})
    app.config.update({'SQLALCHEMY_TRACK_MODIFICATIONS':config_ini.getboolean('General','SQLALCHEMY_TRACK_MODIFICATIONS',fallback=False)})
    app.config.update({'MAIL_SERVER':                   config_ini.get       ('General','MAIL_SERVER',fallback='localhost')})
    app.config.update({'MAIL_PORT':                     config_ini.get       ('General','MAIL_PORT',fallback=25)})
    app.config.update({'MAIL_USE_TLS':                  config_ini.getboolean('General','MAIL_USE_TLS',fallback=False)})
    app.config.update({'MAIL_USE_SSL':                  config_ini.getboolean('General','MAIL_USE_SSL',fallback=False)})
    app.config.update({'MAIL_USERNAME':                 config_ini.get       ('General','MAIL_USERNAME',fallback='collector@localhost.localdomain')})
    app.config.update({'MAIL_PASSWORD':                 config_ini.get       ('General','MAIL_PASSWORD',fallback='MailPassword')})
    app.config.update({'LINES_PER_PAGE':                config_ini.getint    ('General','LINES_PER_PAGE',fallback=5)})
    app.config.update({'DEBUG':                         config_ini.getboolean('General','DEBUG',fallback=False)})
    app.config.update({'TESTING':                       config_ini.getboolean('General','TESTING',fallback=False)})
    app.config.update({'WTF_CSRF_ENABLED':              config_ini.getboolean('General','WTF_CSRF_ENABLED',fallback=False)})
    # Force no caching of FLASK JS CSS files & Updates -----------------
    app.config.update({'SEND_FILE_MAX_AGE_DEFAULT':     0})
    app.config.update({'API_USERS':                     config_ini.get       ('API'    ,'USERS',fallback='collector:collector')})
    temp_API_Users = app.config['API_USERS'].split(',')
    API_Users= []
    for userpass in temp_API_Users:
        API_Users.append(f'Basic {base64.b64encode(userpass.encode()).decode()}')
    app.config['API_USERS'] = API_Users
    pprint(app.config['API_USERS'])

    # get all keys in General Section
    # this lets setup customized app config variable without
    # modifying this initialization code
    # if key is not in app.config then its appended
    all_keys = dict(config_ini.items('General'))
    for key in all_keys:
        if re.match(f"^{app_code}_.*$",key) is not None:
            if key.upper() not in app.config.keys():
                app.config.update({key.upper():config_ini.get('General',key)})

    if app.config['DEBUG']:
        print("create_flask_app: %-30s = %s"%("__name__"      , __name__      ))
        print("create_flask_app: %-30s = %s"%("app"           , app           ))
        print("create_flask_app: %-30s = %s"%("app_name"      , app_name      ))
        print("create_flask_app: %-30s = %s"%("app_code"      , app_code      ))
        print("create_flask_app: %-30s = %s"%("app_key"       , app_key       ))
        print("create_flask_app: %-30s = %s"%("app_folder"    , app_folder    ))
        print("create_flask_app: %-30s = %s"%("app_root_path" , app_root_path ))
        print("create_flask_app: %-30s = %s"%("logger"        , logger        ))
        print("create_flask_app: %-30s = %s"%("config_ini"    , config_ini    ))
        print("create_flask_app: %-30s = %s"%("config_file"   , config_file   ))
        for key in sorted(app.config.keys()):
            print("create_flask_app: %-30s = %s"%(key,app.config[key]))
    
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
    
