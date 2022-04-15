import os
import sys
import configparser
import datetime
import time
import logging
import simplejson as json
from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from    emtec.common.functions              import *
from    emtec.collector.common.context      import Context
from emtec.collector.statistics import *
from emtec.feedback import *
from flask import current_app

# Application Initialization function
def create_flask_app(app_name,config_file=None):
    config_ini = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation())
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
    # GV 20220304 bootstrap.init_app      (app)
    #mail.init_app           (app)
    #moment.init_app         (app)
    db.init_app             (app)
    #login_manager.init_app  (app)
    #babel.init_app          (app)
    # Collector's modules
    
    # attach routes and custom error pages here
    #from app.main   import main as main_blueprint          # NOTE: Example talks on main here .main was required . (Why?)
    #app.register_blueprint(main_blueprint)
    
    #from .auth import auth as auth_blueprint
    #app.register_blueprint(auth_blueprint, url_prefix='/auth')

    return app

def Get_Resumes(
        db        = None,
        today     = None,
        customer  = 0,
        force_all = False,
        logger    = logging.getLogger(),
        cit_status= 1,
        cur_code  = 'UF',
        ci_id     = [],
        user_id   = '1',
        platform  = 2,
        cc_id     = '30000000',
        fast      = True,
        callback  = None,
        **kwargs
    ):
    today = Get_Today(today)
    periods = Get_Periods(today,logger)
    resumes = {}
    logger.debug(f"{this()}: current_app={current_app}")
    logger.debug(f"{this()}: __file__={__file__}")
    logger.debug(f"{this()}: os.path.basename(__file__)={os.path.basename(__file__)}")
    logger.debug(f"{this()}: os.getcwd()={os.getcwd()}")
    cache_filename = os.path.join(os.getcwd(),f"{os.path.basename(__file__).split('.')[0]}.cache")
    logger.info(f"{this()}: cache_filename={cache_filename}")
    
    if os.path.exists(cache_filename):
        with open(cache_filename,"r") as fp:
            cache = json.load(fp)
    else:
        cache = {}
    logger.debug(f"{this()}: cache = {cache}")
    for name in periods:
        # previous month will be calculated only in day 1 or forced
        #if not force_all and name == 'previous_month':
        #    if today.day > 1 :
        #        continue
        period = periods.get(name)
        start,end = period
        suffix = f"{customer}_{start.year:04d}{start.month:02d}"
        logger.info(f"{this()}: Process resume '{name}' for Charge Items {suffix} {start.day:02d}-{end.day:02d}")
        logger.debug(f"{this()}: user={user_id} customer={customer} cost_center={cc_id}")
        count = None
        key=f"{user_id}-{customer}-{platform}-{cc_id}-{start.strftime('%Y%m%d')}-{end.strftime('%Y%m%d')}-{name}"
        logger.debug(f"{this()}: key= {key}")
        # Allways update 'current_mont' and today' resumes, avoid other already generated resumes
        # already available in 'cache'
        # unless 'force_all' is specified
        # 'previous_month' is static and should be generated only once a month
        # 'current_month_so_far' is static and should be generated only once a day (yesterday's info)
        logger.debug(f"{this()}: force_all={force_all} name={name} key={key} missing={key not in cache.keys()}")
        if force_all or name in ['current_month','today'] or  key not in cache.keys():
            logger.info(f"{this()}: Processing resume key = {key}")
            
            if db is not None:
                count = Generate_Resume(
                    db,
                    customer,
                    start,
                    end,
                    cit_status,
                    cur_code,
                    ci_id,
                    user_id,
                    cc_id,
                    fast=True,
                    logger=logger,
                    callback=callback,
                    **kwargs
                    )
            if count is not None and count>0:
                cache.update({key:{'count':count}})
                with open(cache_filename,'w') as fp:
                    fp.write(json.dumps(cache))
            resumes.update({name:{'count':count}})
        else:
            logger.warning(f"{this()}: Avoid processs of resume key = {key}")
        # lo movi hacia arriba 2 lineas por velocidad y evitar redundacia probar
        # resumes.update({name:{'count':count}})
    for name in resumes:
        period = periods.get(name)
        start,end = period
        logger.info(f"{this()}: resume: {name} {start.strftime('%Y-%m-%d')}/{end.strftime('%Y-%m-%d')} = {resumes[name].get('count')}")
        Consolidate_Resume(db,user_id,customer,start,end,cit_status,cur_code,platform,logger)
        for agregation in AGREGATIONS:
            resume = Get_Resume(db,user_id,customer,start,end,cit_status,cur_code,platform,agregation,logger=logger)
            if resume:
                logger.info(
                    f"{this()}: resume: "
                    f"Q@R = {resume.get('Quantity_at_Rate'):,.0f} "
                    f"Q = {resume.get('Quantity'):,.0f} "
                    f"P = {resume.get('ST_at_Cur'):,.2f} {resume.get('currency')} "
                    f"rows = {len(resume.get('rows',[])):7,.0f} "
                    f"{resume.get('description','Unknown')}"
                )

config_file = sys.argv[1]
driver_group = 'Statistics'

add_Logging_Levels()

# GV create logger
logger           = logging.getLogger('Collector Statistics')
logger.propagate = False
handler          = None

db = Collector_ORM_DB()

if (os.path.isfile(config_file)):
    config_ini = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation())
    config_ini.read( config_file )
    # GV Forced production environment configuration
    # GV from config_ini file
    handlerType = config_ini.get(driver_group,'handler_type',fallback='TIME_ROTATING')
    when        = config_ini.get(driver_group,'when',fallback='d')
    interval    = config_ini.getint(driver_group,'interval',fallback=7)
    backupCount = config_ini.getint(driver_group,'backupCount',fallback=53)
            
    # GV Will work with configuration file
    C = Context(app_name="Collector Statistics",app_ini_file=config_file,logger=logger)    
    C.Set()
    C.db=db
    C.db.logger=logger
    logger.name=driver_group    
    logger.setLevel(C.log_level)
    logger.propagate=True
    config_name=os.getenv('COLLECTOR_CONFIG') or 'default'
    app     = create_minimal_app(config_file,config_name,db=db,logger=logger)
    app_ctx = app.app_context()
    app_ctx.push()   
    
    print(f"app = {app}") 
    print(f"db = {db}") 
    print(f"Charge_Items = {Charge_Items}") 
    print(f"Charge_Items.__tablename__ = {Charge_Items.__tablename__}") 
    
    if (C):

        while True:

            handler,log_file = Reset_Log_File_Name(
                            logger=logger,
                            folder=C.log_folder,
                            nameFormat="%s.log"%driver_group.replace(' ','_'),
                            level=C.log_level,
                            handler=handler,
                            handlerType=handlerType,
                            when=when,
                            interval=interval,
                            backupCount=backupCount
                            )
            log_file_previous = None

            name = 'Statistics'
            statistics = ['Get_Resumes'] 
            pool_seconds = config_ini.getint('Statistics','pool_seconds',fallback=3600)

            logger.info(f"{name}: ****** Daemon Start *********************")
            logger.info(f"{name}: as '{getpass.getuser()}' Using configuration: '{config_file}'")
            logger.info(f"{name}: *****************************************")
            # GV --------------------------------------------------------------
            # GV Overrides default log level for this driver group only
            log_level       = config_ini.get('Statistics','log_level',fallback=C.log_level)        
            logger.info(f"{name}: log level from config is  = {log_level}")
            if type(log_level) == str:
                log_level=log_level.lower()
                if      log_level == 'debug':       log_level=logging.DEBUG
                elif    log_level == 'information': log_level=logging.INFO
                elif    log_level == 'error':       log_level=logging.ERROR
                elif    log_level == 'warning':     log_level=logging.WARNING
                elif    log_level == 'critical':    log_level=logging.CRITICAL
                elif    log_level == 'fatal':       log_level=logging.FATAL
                else:                               log_level=C.log_level
            logger.setLevel(log_level)
            logger.info(f"{name}: driver {name} log level set to           = {logger.level}")
            logger.info(f"{name}: driver {name} log effective level set to = {logger.getEffectiveLevel()}")
            logger.info(f"{name}: driver {name} logger                     = {logger}")
            # GV --------------------------------------------------------------

            logger.debug(f"{name}: name         = {name}")
            logger.debug(f"{name}: pool_seconds = {pool_seconds}")

            # GV Required to handle multiple collector services in one daemon
            # GV services are serialized
            date=datetime.datetime.now()
            customer    = config_ini.getint    ('Statistics','customer',fallback=3)        
            status      = config_ini.getint    ('Statistics','status',fallback=1)        
            currency    = config_ini.get       ('Statistics','currency',fallback='UF')        
            cis         = config_ini.get       ('Statistics','cis',fallback=None)        
            user        = config_ini.getint    ('Statistics','user',fallback=1)        
            cost_center = config_ini.get       ('Statistics','cost_center',fallback=None)        
            platform    = config_ini.get       ('Statistics','platform',fallback=2)        
            force_all   = config_ini.getboolean('Statistics','force_all',fallback=False)        
            fast        = config_ini.getboolean('Statistics','fast',fallback=True)        
            callback    = config_ini.get       ('Statistics','callback',fallback='default')        

            if callback is not None:
                if  callback == 'default':
                    callback=display_advance
                else:
                    callback=globals().get(callback)

            # GV Check for propper log file for this iteration
            if (log_file_previous != log_file):
                logger.info(f"{name}: Logging to '{log_file}'")
                logger.info(f"{name}: *****************************************")
                log_file_previous = log_file
            # GV Will create a new child process to isolate service
            child_pid = os.fork()
            if child_pid == 0:
                # GV Child new process instantiated
                # GV -------------------------------------------------    
                try:
                    if 'sqlite' in str(C.db):
                        logger.error(f"{name}: DB engine not expected is      : '{C.db}'")
                        logger.error(f"{name}: os.environ['COLLECTOR_CONFIG'] : '{os.environ['COLLECTOR_CONFIG']}'")
                        logger.error(f"{name}: os.environ['DATABASE_URL']     : '{os.environ['DATABASE_URL']}'")
                        break
                    for statistic in statistics:
                        logger.info(f"{name}: Executing statistics mode '{statistic}'")
                        print(f"{name}: {time.strftime('%H:%M:%S')} Executing statistics mode '{statistic}'")
                        db.session.close()
                        db.session.flush()
                        start=datetime.datetime.now().timestamp()
                        if statistic == 'Get_Resumes':
                            Get_Resumes(
                                db         = db,
                                today      = date,
                                customer   = customer,
                                force_all  = force_all,
                                logger     = logger,
                                cit_status = status,
                                cur_code   = currency,
                                ci_id      = cis,
                                user_id    = user,
                                cc_id      = cost_center,
                                fast       = fast,
                                callback   = callback,
                            )
                        else:
                            C.logger.error(f"{name}: Invalid statistics name '{statistic}'.")
                        end=datetime.datetime.now().timestamp()
                        logger.info(f"{name}: '{statistic}' took {end-start:,.0f} seconds")
                except Exception as e:
                    C.logger.error(f"{name}: Exception catched during Statistical execution.'errno:{e.errno},strerror:{e.strerror},args:{e.args}'")
                    #break
                os._exit(0)
                # GV --------------------------------------------------
                C.logger.debug(f"{name}: Execution completed @ {strftime('%H:%M:%S')}. Waiting {pool_seconds} seconds ...")
            else:
                # GV Parent main loop process continues
                # GV WAIT FOR PROCESS # GV child_pid
                logger.info(f"{name}: Child Process started as pid={child_pid} @ {time.strftime('%H:%M:%S')}.")
                if logger.level < logging.INFO:
                    print(f"{name}: Child Process started as pid={child_pid} @ {time.strftime('%H:%M:%S')}.")
                try:
                    # GV WAIT FOR PROCESS # GV child_pid
                    childProcExitInfo = os.wait()
                    signal=childProcExitInfo[1]%256
                    status=int(childProcExitInfo[1]/256)
                    message = f"{name}: Child process %d exited with exit info = %d (signal %d status %d)"%(
                        childProcExitInfo[0],
                        childProcExitInfo[1],
                        signal,
                        status,
                        )
                    logger.info(message)
                    logger.info(f"{name}: Waiting {pool_seconds} seconds ...")
                    print(message)
                    print(f"{name}: {time.strftime('%H:%M:%S')} Waiting {pool_seconds} seconds ...")
                    time.sleep(pool_seconds)
                except Exception as e:
                    logger.error(f"{name}: Exception catched while pooling. 'errno:{e.errno},strerror:{e.strerror},args:{e.args}'")
                    break        
        # GV Out of loop service should never get here unless system shutdown
        logger.warning(f"{name}: *** Unexpected Deamon Interruption ***")
else:
    # GV Configuration error
    print(f"{sys.argv[0]}: ERROR: Configuration file '{config_file}' does not exists. aborting.")
    print(f"{sys.argv[0]}: ERROR: Number of arguments: {len(sys.argv)} arguments.")
    print(f"{sys.argv[0]}: ERROR: Argument List: {str(sys.argv)}")

print()    
print(f"{sys.argv[0]}: ERROR: Collector Deamon FAIL **********************")
print()
