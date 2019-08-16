# Import configuration functions
import configparser
from configparser import ConfigParser, ExtendedInterpolation

# Import logging functions
import logging

# Import sqlalchemy functions
from sqlalchemy import create_engine

# Import App Modules
from .log   import Log
from .audit import Audit


class Context:
    """ Collector Context Class """

    """ Members """
    # Application General Members
    config          = None
    app             = None
    app_ini_file    = None
    app_name        = None
    app_home        = None
    app_folder      = None
    

    # DB connection members
    driver          = "mysql+pymysql"
    user            = "user"
    password        = "Password"
    host            = "127.0.0.1"
    port            = 3306
    schema          = "collector"
    engine_string   = None
    db              = None
    engine          = None
    
    # Log Members
    L               = None
    logger          = None
    log_file_name   = None
    log_level       = logging.INFO
    log_folder      = None
    log_format      = None
    log_format_debug= None
    # Audit Members
    #A               = None
    #auditor         = None
    #audit_file_name = None
    #audit_level     = logging.WARNING
    
    # Deamon Members
    pool_seconds    = 3600

    def __init__(self,app_name="Collector",app_ini_file="collector.ini",logger=None):
        self.app_name       = app_name
        self.app_ini_file   = app_ini_file
        if logger is not None:
            self.logger = logger
        self.Set()

    def init_app(self,app=None,app_name="Collector",app_ini_file="collector.ini"):
        self.app=app
        self.app_name = app_name
        self.app_ini_file = app_ini_file
        
    def Set(self): 
        self.Read_Configuration(self.app_ini_file)
        self.Set_Logger(self.log_level)
        self.Set_Engine()
        
    def Read_Configuration(self,app_ini_file):
        self.app_ini_file = app_ini_file
        self.config = configparser.ConfigParser(interpolation=ExtendedInterpolation())
        self.config.read(self.app_ini_file)
        
        self.app_home = self.config['General']['app_home']
        self.app_folder = self.config['General']['app_folder']
        
        self.driver = self.config['DB']['driver']
        self.user = self.config['DB']['user']
        self.password = self.config['DB']['password']
        self.host = self.config['DB']['host']
        self.port = self.config['DB']['port']
        self.schema = self.config['DB']['schema']
        
        log_level = self.config['General']['log_level'].capitalize()
        
        self.log_folder = self.config['General']['log_folder']
        self.log_format = self.config['General']['log_format']
        self.log_format_debug = self.config['General']['log_format_debug']

        if (log_level == 'Trace'):
            self.log_level = logging.TRACE
        elif (log_level == 'Debug'):
            self.log_level = logging.DEBUG
        elif (log_level == 'Information'):
            self.log_level = logging.INFO
        elif (log_level == 'Warning'):
            self.log_level = logging.WARNING
        elif (log_level == 'Error'):
            self.log_level = logging.ERROR
        elif (log_level == 'Critical'):
            self.log_level = logging.CRITICAL
        else:
            self.log_level = logging.INFO

        """
        audit_level = self.config['General']['audit_level'].capitalize()
        
        self.audit_folder = self.config['General']['audit_folder']
        self.audit_format = self.config['General']['audit_format']

        if (audit_level == 'Debug'):
            self.audit_level = logging.DEBUG
        elif (audit_level == 'Information'):
            self.audit_level = logging.INFO
        elif (audit_level == 'Warning'):
            self.audit_level = logging.WARNING
        elif (audit_level == 'Error'):
            self.audit_level = logging.ERROR
        elif (audit_level == 'Critical'):
            self.audit_level = logging.CRITICAL
        else:
            self.audit_level = logging.INFO
        """           
        self.pool_seconds = int(self.config['Deamon']['pool_seconds'])
                   
                   
       
    def Set_Logger(self,log_level):
        self.log_level = log_level
        #print()
        #print("Context Set_Logger 1: logger:",self.logger,id(self.logger))
        # 20181211 GV Cambios aqui para afinar logging .... revisar de ser posible excluir 
        if self.logger is None:
            self.L = Log(self.app_name,self.log_folder,self.log_format,self.log_format_debug,self.log_level,self.logger)    
            self.logger = self.L.logger
            self.log_file_name = self.L.file_name
        #print("Context Set_Logger 2: logger:",self.logger,id(self.logger))
    
    """
    def Set_Auditor(self,audit_level=logging.WARNING):
        self.audit_level = audit_level
        self.A = Audit(self.app_name,self.audit_folder,self.audit_format,self.audit_level)    
        self.auditor = self.A.auditor
        self.audit_file_name = self.A.file_name
    """    
    def Set_Engine(self):    
        # Connect to DB
        self.engine_string=str("%s://%s:%s@%s:%s/%s"%(self.driver,self.user,self.password,self.host,self.port,self.schema))
        try:
            self.db     = create_engine(self.engine_string)
            self.engine = self.db
            self.logger.debug("Create Engine success with [%s]"%self.engine_string)
        except:
            self.logger.error("Create Engine fails [%s]"%self.engine_string)
        
"""
    def __init__(self, app=None, use_native_unicode=True, session_options=None,
                 metadata=None, query_class=BaseQuery, model_class=Model):

        self.use_native_unicode = use_native_unicode
        self.Query = query_class
        self.session = self.create_scoped_session(session_options)
        self.Model = self.make_declarative_base(model_class, metadata)
        self._engine_lock = Lock()
        self.app = app
        _include_sqlalchemy(self, query_class)

        if app is not None:
            self.init_app(app)
            
    def init_app(self, app):
        " ""This callback can be used to initialize an application for the
        use with this database setup.  Never use a database in the context
        of an application not initialized that way or connections will
        leak.
        " ""
        if (
            'SQLALCHEMY_DATABASE_URI' not in app.config and
            'SQLALCHEMY_BINDS' not in app.config
        ):
            warnings.warn(
                'Neither SQLALCHEMY_DATABASE_URI nor SQLALCHEMY_BINDS is set. '
                'Defaulting SQLALCHEMY_DATABASE_URI to "sqlite:///:memory:".'
            )

        app.config.setdefault('SQLALCHEMY_DATABASE_URI', 'sqlite:///:memory:')
        app.config.setdefault('SQLALCHEMY_BINDS', None)
        app.config.setdefault('SQLALCHEMY_NATIVE_UNICODE', None)
        app.config.setdefault('SQLALCHEMY_ECHO', False)
        app.config.setdefault('SQLALCHEMY_RECORD_QUERIES', None)
        app.config.setdefault('SQLALCHEMY_POOL_SIZE', None)
        app.config.setdefault('SQLALCHEMY_POOL_TIMEOUT', None)
        app.config.setdefault('SQLALCHEMY_POOL_RECYCLE', None)
        app.config.setdefault('SQLALCHEMY_MAX_OVERFLOW', None)
        app.config.setdefault('SQLALCHEMY_COMMIT_ON_TEARDOWN', False)
        track_modifications = app.config.setdefault(
            'SQLALCHEMY_TRACK_MODIFICATIONS', None
        )

        if track_modifications is None:
            warnings.warn(FSADeprecationWarning(
                'SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and '
                'will be disabled by default in the future.  Set it to True '
                'or False to suppress this warning.'
            ))

        app.extensions['sqlalchemy'] = _SQLAlchemyState(self)

        @app.teardown_appcontext
        def shutdown_session(response_or_exc):
            if app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']:
                if response_or_exc is None:
                    self.session.commit()

            self.session.remove()
            return response_or_exc

            
"""

