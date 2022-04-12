from time           import strftime
from datetime       import datetime     
from pprint         import pprint,pformat                    
from sqlalchemy     import exc
from sqlalchemy     import func
from flask          import render_template
from flask          import session
from flask          import redirect 
from flask          import url_for 
from flask          import current_app 
from flask          import flash
from flask          import request
from flask          import Markup
# GV from flask          import current_process
from flask_login    import login_required
from flask_login    import current_user
from flask_babel    import gettext
from flask_babel    import lazy_gettext
# GV from ..email import send_email

from .              import main

from ..             import db
from ..             import logger
from ..             import babel
from emtec.plugins  import *

# add to you main app code
@babel.localeselector
def get_locale():
    try:
        if current_app.config.CURRENT_LANGUAGE is not None:
            language =  current_app.config.CURRENT_LANGUAGE
        else:
            language =  request.accept_languages.best_match(
                            current_app.config.LANGUAGES.keys()
                        )
    except Exception as e:
        print(f"get_locale: exception: {str(e)}")
        language = 'en'
    return language

MONTHS={
    'january':      gettext('january'),
    'february':     gettext('february'),
    'march':        gettext('march'),
    'april':        gettext('april'),
    'may':          gettext('may'),
    'june':         gettext('june'),
    'july':         gettext('july'),
    'august':       gettext('august'),
    'september':    gettext('september'),
    'october':      gettext('october'),
    'november':     gettext('november'),
    'december':     gettext('december'),
}
DAYS={
    'sunday':       gettext('sunday'),
    'monday':       gettext('monday'),
    'tuesday':      gettext('tuesday'),
    'wednesday':    gettext('wednesday'),
    'thursday':     gettext('thursday'),
    'friday':       gettext('friday'),
    'saturday':     gettext('saturday'),
}
# hay que ver como ajustar procedimiento para incluir simbolos desde 
# plugins
TRANSLATION_SYMBOLS=[
    gettext('Adds'),
    gettext('Admin Adds'),
    gettext('Queries'),
    gettext('Reports'),
    gettext('AAAA - Display Period Usage'),
]

from ..decorators   import admin_required, permission_required

from emtec                                 import *
# GV from emtec.collector.common.functions      import *
from emtec.common.functions                import *
from emtec.collector.db.flask_models       import User
from emtec.collector.db.flask_models       import Permission
# GV 20200224 GV from emtec.collector.db.orm_model          import Interface
from emtec.collector.db.flask_models       import *
from emtec.collector.db.orm_model          import *
from emtec.api                             import *

# GV EG Collector Global required role constants
ROLE_CUSTOMER=1
ROLE_REPORTER=2
ROLE_CHARGER=3
ROLE_ADMINISTRATOR=4
ROLE_AUDITOR=5
ROLE_GOD=6
ROLE_RESERVED=7

""" Application decorators for routes """
""" Decorators specify main routes to be handled by Collector Solution """

@main.route('/', methods=['GET', 'POST'])
def index():
    
    # GV Espera a capitulo 3 para mejorar procedimiento de respuesta, hard coding mucho aqui
    
    # GV Aqui debo setear el ambiente de variables de periodo -------------
    try:
        Period = get_period_data(current_user.id,db.engine,Interface)
    except:
        Period = get_period_data()
    # GV ------------------------------------------------------------------
    # GV Setup all data to render in template
    data =  {   "name":current_app.name,
                "app_name":current_app.name,
                "date_time":strftime('%Y-%m-%d %H:%M:%S'),
                "user_agent":request.headers.get('User-Agent'),
                "db":db,
                "logger":logger,
                "VERSION_MAYOR":VERSION_MAYOR,
                "VERSION_MINOR":VERSION_MINOR,
                "VERSION_PATCH":VERSION_PATCH,
            }
    if current_user.is_authenticated:
        collectordata=get_collectordata()
    else:
        collectordata={"COLLECTOR_PERIOD":Period}
        
    return render_template('collector.html',data=data,collectordata=collectordata)

@main.route('/language/<string:langcode>', methods=['GET', 'POST'])
def language(langcode):
    current_app.config.CURRENT_LANGUAGE = langcode
    return redirect('/')

@main.route('/under_construction', methods=['GET','POST'])
def under_construction():   
    collectordata = get_collectordata()
    return render_template('under_construction.html',collectordata=collectordata)

@main.route('/demo', methods=['GET','POST'])
def demo():   
    return render_template('demo.html')

@main.route('/test_index', methods=['GET', 'POST'])
def test_index():
    
    # GV Espera a capitulo 3 para mejorar procedimiento de respuesta, hard coding mucho aqui

    if logger is not None:
        logger.debug("index() IN")
    else:
        print("*** WARNING *** Route: test_index: logger is undefined. !!! No logging functions possible. !!!")

    data =  {   "name":current_app.name,
                "app_name":C.app_name,
                "date_time":strftime('%Y-%m-%d %H:%M:%S'),
                "user_agent":request.headers.get('User-Agent'),
                "current_time":datetime.utcnow(),
                "db":db,
                "logger":logger,
                "C":C,
                "C.db":C.db,
                "C.logger":C.logger,
                "current_app":current_app,
                "current_app_dir":dir(current_app),
                "current_app_app_context":current_app.app_context(),
                "current_app_app_context DIR":dir(current_app.app_context()),
                }
    name = None
    password = None
    form = NameForm()

    return render_template('test.html',data=data, name=name,password=password, form=form)

''' GV 20210430
@main.route('/collector_faq', methods=['GET','POST'])
def collector_faq():   
    return render_template('collector_faq.html')

@main.route('/collector_about', methods=['GET','POST'])
def collector_about():   
    return render_template('collector_about.html')
'''
# Plugins handler views this are reqrured for interface
# plugins call handlers
# Main plugins caller view
@main.route("/plugin/<name>",methods=['GET','POST'])
def plugin(name):
    collectordata = get_collectordata()
    print(f"enter view: plugin/{name}")
    print(f"current_app  = {current_app}")
    print(f"current_user = {current_user}")
    print(f"db           = {db}")
    print(f"logger       = {logger}")
    pim   = current_app.config.get('PLUGINS_MANAGER')
    plgin = pim.plugins.get(name).get('instance')
    print(f"pim          = {pim}")
    print(f"plgin        = {plgin.name}")

    try:
        Period = get_period_data(current_user.id,db.engine,Interface)
    except:
        Period = get_period_data()
    if current_user.is_authenticated:
        collectordata=get_collectordata()
    else:
        collectordata={"COLLECTOR_PERIOD":Period}
    
    # load here any argument data
    data = {}

    kwargs = {
        'name'              :name,
        'title'             :plgin.title,
        'short_description' :plgin.short_description,
        'long_description'  :plgin.long_description,
        'app'               :current_app,
        'user'              :current_user,
        'request'           :request,
        'url'               :request.url,
        'method'            :request.method,
        'args'              :request.args,
        'form'              :request.form,
        'db'                :db,
        'session'           :session,
        'rows'              :[],
        'application_data'  :collectordata,
        'logger'            :logger,
        'data'              :data
    }
    print(f"will execute plgin.execute ")
    result = plgin.execute(**kwargs)
    if plgin.format == 'html_body':
        result=render_template('plugin.html',body=result,collectordata=collectordata)
    return result

# Main plugins reporter
# should ve decorated as administrator only
@main.route("/plugins",methods=['GET','POST'])
def plugins():
    output = ""
    pim    = current_app.config.get('PLUGINS_MANAGER')
    for name in pim.plugins:
        plugin=pim.plugins[name]
        output+=f"{plugin.get('name')} {plugin.get('type')} {plugin.get('scope')} {plugin.get('instance').title}<br>"
    return output


# GV Flask Caching avoider
@main.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers["Cache-Control"] = "public, max-age=0"
    return r

# GV Application specific functions
# GV -------------------------------------------------------------------
# GV This function is intented to define dynamic context data
# GV Collector Charge Items sharding period and table setup
# GV A context 'collectordata' object is returned
# GV -------------------------------------------------------------------
def get_collectordata():
    collectordata = {}
    # GV Here we'll include al important Collector context data 
    collectordata.update({"COLLECTOR_PERIOD":get_period_data(current_user.id,db.engine,Interface)})
    collectordata.update({"CONFIG":current_app.config})
    active_period = collectordata['COLLECTOR_PERIOD']['active']
    dt = datetime.datetime.strptime(active_period,"%Y%m")
    start,end = Get_Period(dt,PERIOD_MONTH)
    collectordata['COLLECTOR_PERIOD'].update({'start':start,'end':end})
    logger.debug(f"{this()}: dt: {dt} active_period={active_period}") 
    logger.debug(f"{this()}: COLLECTOR_PERIOD={collectordata['COLLECTOR_PERIOD']}") 
    
    sharding = False
    # GV GV Here we'll include sharding required code
    if 'COLLECTOR_CIT_SHARDING' in current_app.config: 
        sharding = current_app.config['COLLECTOR_CIT_SHARDING']
        logger.debug(f"{this()}: sharding={sharding}") 
    if sharding:
        # GV GV Get customer id, just in case is needed
        customer = current_user.cost_center.Cus_Id
        cus_sharding = current_app.config.get('COLLECTOR_CUS_SHARDING') if current_app.config.get('COLLECTOR_CUS_SHARDING') else None
        # GV GV If required customer sharding then affect suffix
        if cus_sharding:
            cus_sharding = True if cus_sharding.upper() in ['TRUE','T','YES','Y','VERDADERO','V'] else False
        logger.debug(f"{this()}: cus_sharding={cus_sharding}") 
        # GV if cus_sharding:
        # Default suffix will be multitenant
        suffix = f"{customer}_{active_period}"
        # GV else:
        # GV Use default non tenant suffix 
        # GV   suffix = active_period  
        logger.debug(f"{this()}: suffix={suffix}") 
        # GV GV Need to check if sharded table exists, if not should be created
        charge_item.set_shard(suffix,db.engine)
        flash(gettext('Using shardened table: %s')%(charge_item.__table__.name)) 
        logger.debug(f"{this()}: Using shardened table: {charge_item.__table__.name}") 
    
    # Aqui debe leer configuracion
    config = configparser.ConfigParser()
    logger.debug(f"views_py_header: get_collectordata(): COLLECTOR_CONFIG_FILE = {current_app.config.get('COLLECTOR_CONFIG_FILE')}")
    config.read(current_app.config.get('COLLECTOR_CONFIG_FILE'))
    if current_user.role.id in [ROLE_CUSTOMER,ROLE_ADMINISTRATOR,ROLE_GOD]:
        collectordata.update({'customer_options':{'Adds':{'options':[]}}})
        if 'Customer_Options' in config.sections():
            collectordata['customer_options']['Adds']['options']+=json.loads(config.get('Customer_Options','options'))
        collectordata['customer_options']['Adds']['options']+=current_app.config.get('CUSTOMER_OPTIONS',[])
    if current_user.role.id in [ROLE_ADMINISTRATOR,ROLE_GOD]:
        collectordata.update({'customer_options':{'Admin Adds':{'options':[]}}})
        if 'Administrator_Options' in config.sections():
            collectordata['customer_options']['Admin Adds']['options']+=json.loads(config.get('Administrator_Options','options'))
        collectordata['customer_options']['Admin Adds']['options']+=current_app.config.get('ADMINISTRATOR_OPTIONS',[])
        
    logger.debug(f"views_py_header: get_collectordata(): collectordata = {collectordata}")
    
    return collectordata





