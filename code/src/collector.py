#!/usr/bin/env python
# GV -------------------------------------------------------------------
# GV Top level required definitions
# GV -------------------------------------------------------------------
import  os
import  sys
import  getpass
from    pprint              import pprint
from    flask               import current_app
# GV 20220310 from    flask_script        import Manager, Shell
# GV 20220310 from    flask_migrate       import Migrate, MigrateCommand
import  configparser
from    configparser        import ConfigParser, ExtendedInterpolation
from    sqlalchemy          import create_engine
# GV -------------------------------------------------------------------

# GV -------------------------------------------------------------------
# GV G Unicorn required definitions
# GV -------------------------------------------------------------------
import  multiprocessing
import  gunicorn
from    gunicorn.app.base   import Application, Config
from    gunicorn            import glogging
from    gunicorn.workers    import sync

def number_of_workers(max_workers=65):
    return min((multiprocessing.cpu_count() * 2) + 1,max_workers)

class GUnicornFlaskApplication(Application):
    def __init__(self, app):
        self.usage, self.callable, self.prog, self.app = None, None, None, app

    def run(self, **options):
        self.cfg = Config()
        [self.cfg.set(key, value) for key, value in options.items()]
        return Application.run(self)

    load = lambda self:self.app
# GV -------------------------------------------------------------------

# GV -------------------------------------------------------------------
# GV Emtec group required definitions
# GV -------------------------------------------------------------------

from    emtec.common.functions             import *
from    emtec.collector.common.context     import Context
from    emtec.collector.db.orm_model       import *
# GV -------------------------------------------------------------------

# GV Setup context data depending on configuration file

# Get Version and Build data
def print_version():
    print (f"EG Collector v {MAYOR}.{MINOR}.{PATCH} build {BUILD}")

def version():
    print (f"{MAYOR}.{MINOR}.{PATCH}")

from collector_version import *

if len(sys.argv) < 2:
    sys.exit(1)

if sys.argv[1] == '--version':
    version()
    sys.exit(1)
elif sys.argv[1] == '--print_version':
    print_version()
    sys.exit(1)

# GV Macro level default values
config_file = "collector.ini"
run_mode    = 'GUNICORN'

command     = sys.argv[0]
config_file = sys.argv[1]

if len(sys.argv) > 2:        
    run_mode=sys.argv[2]

if (os.path.isfile(config_file)):
        config_ini = configparser.ConfigParser(interpolation=ExtendedInterpolation())
        config_ini.read( config_file )        
        flask_host    = config_ini.getint('General','flask_host'   ,fallback='0.0.0.0')
        flask_port    = config_ini.getint('General','flask_port'   ,fallback=8000)
        gunicorn_host = config_ini.getint('General','gunicorn_host',fallback='0.0.0.0')
        gunicorn_port = config_ini.getint('General','gunicorn_port',fallback=8000)
        max_workers   = config_ini.getint('General','max_workers'  ,fallback=0)
        timeout       = config_ini.getint('General','timeout'      ,fallback=120)

else:
    sys.exit(1)

from    app                 import db
from    app                 import logger
from    app                 import create_flask_app
from    app                 import babel

C = Context("Collector Web Server",config_file,logger)
C.Set()

app     = create_flask_app('Collector',config_file)
# GV GV Defines templates globals !!!!
app.add_template_global(name='current_app', f=current_app)
# GV CONFIGURATION PATCH !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

logger.name="Collector Web Server"
# GV Setup logger handlers
# GV Actual File system all logger -------------------------------------
file_handler=add_Logging_Handler(
    logger=logger,
    level=C.log_level,
    folder=C.log_folder,
    nameFormat="%s.log"%logger.name.replace(' ','_'),
    handlerType='TIME_ROTATING'
    )
# GV Default File logger filters (omits) AUDIT records, then an audit
# GV logger needs to be defined
file_handler.addFilter(LevelFilter(logging.AUDIT))
# GV -------------------------------------------------------------------

# GV Specialized AUDIT LOG logger --------------------------------------
audit_handler=add_Logging_Handler(
    logger=logger,
    level=logging.AUDIT,
    folder=C.log_folder,
    nameFormat="%s.aud"%logger.name.replace(' ','_'),
    handlerType='TIME_ROTATING'
    )
# GV -------------------------------------------------------------------

# GV Internationalization code -----------------------------------------
from flask_babel import Babel, gettext, ngettext, lazy_gettext, force_locale

print(f"Set App enabled Languages ...")
setattr(app.config,'LANGUAGES',{
        'en': 'English',
        'es': 'Español'
    })
    
print(f"Set Default App Language ...")
setattr(app.config,'CURRENT_LANGUAGE',None)

print (f"Set Global multilanguage strings ...")

# GV -------------------------------------------------------------------
# GV Global JINJA 2 Functions
app.jinja_env.globals.update(has_access=has_access)
# GV -------------------------------------------------------------------

from emtec.plugins import *
# Plugins management enabler

plugins_dir = os.path.join(app.root_path,'plugins')
print(f"Loading plugins from: {plugins_dir}")
plugins_manager = PluginsManager(app=app,user=None,folder=plugins_dir,logger=logger) 
app.config.update({'PLUGINS_MANAGER':plugins_manager})
#print(f"app.config.PLUGINS_MANAGER = {app.config.get('PLUGINS_MANAGER')}")
plugins = plugins_manager.plugins
#print(f"plugins= {plugins}")
plugins_manager.loaded()
app.config.update({
    'CUSTOMER_OPTIONS':[],
    'ADMINISTRATOR_OPTIONS':[],
})

for name in plugins:
    #print()
    #print(f"Loaded plugin:   {name} {plugins.get(name).get('version')}")
    instance = plugins.get(name).get('instance')
    #print(f"         instance: {instance}")
    #print(f"            title: {instance.title}")
    #print(f"short_description: {instance.short_description}")
    #print(f" long_description: {instance.long_description}")
    #print(f" scope/visibility: {instance.scope}/{instance.visibility}")
    if instance.scope=='customer':
        app.config['CUSTOMER_OPTIONS'].append({"name":instance.short_description,"url":f"/plugin/{name}","header":None,"hr":False,"test":False})
    else:
        app.config['ADMINISTRATOR_OPTIONS'].append({"name":instance.short_description,"url":f"/plugin/{name}","header":None,"hr":False,"test":False})

# pprint (app.config)



if __name__ == '__main__':
    app_ctx = app.app_context()
    app_ctx.push()
    
    logger.setLevel(C.log_level)
    db.logger = logger
    
    if logger is not None:
        db.logger = logger
        logger.info("****** Collector Server *****************")
        logger.info(" * %s: as '%s' Using configuration: '%s'"%
            (sys.argv[0],getpass.getuser(),config_file))
        logger.info(" * %s: db connection is '%s'"%(sys.argv[0],db))
        logger.info("*****************************************")
        for variable in os.environ:
            logger.debug("%s=%s"%(variable,os.environ.get(variable)))
        logger.debug("logger                = %s"%logger)
        logger.debug("db                    = %s"%db)
        logger.debug("db.logger             = %s"%db.logger)
        logger.debug("app                   = %s"%app)
        logger.debug("app.root_path         = %s"%app.root_path)
        logger.debug("app.static_folder     = %s"%app.static_folder)
        logger.debug("app.template_folder 1 = %s"%app.template_folder)
        app.template_folder="%s/templates"%(app.root_path)
        logger.debug("app.template_folder 2 = %s"%app.template_folder)
        logger.debug("babel                 = %s"%babel)
        for key in app.config.keys():
            if key == key.upper():
                logger.debug("%-40s = %s"%(key,app.config[key]))
        logger.debug("%-40s = %s"%("app.root_path",app.root_path))

        logger.info("*****************************************")
        print("****** Collector Server *****************")
        print(" * %s: as '%s' Using configuration: '%s'"%
            (sys.argv[0],getpass.getuser(),config_file))
        print(" * %s: db connection is '%s'"%(sys.argv[0],db))
        print(" * logger is %s"%(logger))
        if logger.getEffectiveLevel() < logging.INFO:
            print("*** logger.handlers are :"%logger.handlers)        
            for h in logger.handlers:
                print("    handler",h,id(h))
                print("      format",h.format,id(h.format))
                print("      formatter",h.formatter,id(h.formatter))
                print("      filter",h.filter,id(h.filter))
                print("      filters",h.filters,id(h.filters))
                print('      name',h.name,'level',h.level,'mode',h.mode)
        logger.trace    ("trace Init Collector Web Server Execution")
        logger.debug    ("debug Init Collector Web Server Execution")
        logger.info     ("info Init Collector Web Server Execution")
        logger.warning  ("warning Init Collector Web Server Execution")
        logger.error    ("error Init Collector Web Server Execution")
        logger.critical ("critical Init Collector Web Server Execution")
        logger.audit    ("audit Init Collector Web Server Execution")
        logger.trace("os.environ=%s"%os.environ)
        logger.trace("app.config=%s"%app.config)
        logger.info("*****************************************")        
        print("*****************************************")
    else:
        print("****************************************")
        print("**** WARNING **** No logger defined ****")
        print("****************************************")

    print(f" * Will execute app {app} here")   
    # GV 20200217 LOCATION OPORTINITY CHANGE DUE TO CONFIG ISSUES ------
    from    emtec.collector.db.flask_models    import User, Role
    # GV ---------------------------------------------------------------
    # GV Will be replaced by embedded Green Unicorn HTTP Server
    if run_mode == 'FLASK':
        print(f" * Running in Flask app mode ({flask_host}:{flask_port})")
        app.run(host=flask_host,port=flask_port)
    else:
        # GV Calculates maximum number of workers or by config
        max_workers = int(app.config.get('COLLECTOR_MAX_WORKERS',65))
        options = {
            'bind': '%s:%s' % (gunicorn_host, gunicorn_port),
            'workers': number_of_workers(max_workers),
            'worker_class':"gunicorn.workers.sync.SyncWorker",
            'timeout': timeout
        }
        print(f" * Running in Green Unicorn powered mode {options['workers']}/{max_workers} workers ({options.get('bind')})")
        logger.debug("Application CPUs   = %s" % multiprocessing.cpu_count())
        logger.debug("Application options= %s" % options)
        logger.debug("Application Flask  = %s" % app)
        gunicorn_app = GUnicornFlaskApplication(app)
        gunicorn_app.run(
            **options
        )

