from time           import strftime
from datetime       import datetime     
from pprint         import pprint,pformat                    
from sqlalchemy     import exc
from sqlalchemy     import func
from flask          import render_template, session, redirect, url_for, current_app, flash
from flask          import request
from flask          import Markup
from flask          import current_app
#rom flask          import current_process
from flask_login    import login_required
from flask_login    import current_user
#from ..email import send_email

from .              import main

from ..             import db
from ..             import logger

from ..decorators   import admin_required, permission_required

from emtec                                 import *
#rom emtec.collector.common.functions      import *
from emtec.common.functions                import *
from emtec.collector.db.flask_models       import User
from emtec.collector.db.flask_models       import Permission
# 20200224 GV from emtec.collector.db.orm_model          import Interface
from emtec.collector.db.flask_models       import *
from emtec.collector.db.orm_model          import *
from emtec.api                             import *

""" Application decorators for routes """
""" Decorators specify main routes to be handled by Collector Solution """

@main.route('/', methods=['GET', 'POST'])
def index():
    
    # Espera a capitulo 3 para mejorar procedimiento de respuesta, hard coding mucho aqui
    
    # Aqui debo setear el ambiente de variables de periodo -------------
    try:
        Period = get_period_data(current_user.id,db.engine,Interface)
    except:
        Period = get_period_data()
    # ------------------------------------------------------------------
    # Setup all data to render in template
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
    collectordata={
                "COLLECTOR_PERIOD":Period,
    }
    return render_template('collector.html',data=data,collectordata=collectordata)

@main.route('/under_construction', methods=['GET','POST'])
def under_construction():   
    return render_template('under_construction.html')

@main.route('/demo', methods=['GET','POST'])
def demo():   
    return render_template('demo.html')

@main.route('/test_index', methods=['GET', 'POST'])
def test_index():
    
    # Espera a capitulo 3 para mejorar procedimiento de respuesta, hard coding mucho aqui

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

# Flask Caching avoider
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

# Application specific functions
# ----------------------------------------------------------------------
# This function is intented to define dinamic context data
# Collector Charge Items sharding period and table setup
# A context 'collectordata' object is returned
# ----------------------------------------------------------------------
def get_collectordata():
    collectordata = {}
    # Here we'll include al important Collector context data 
    collectordata.update({"COLLECTOR_PERIOD":get_period_data(current_user.id,db.engine,Interface)})
    collectordata.update({"CONFIG":current_app.config})
    active_period = collectordata['COLLECTOR_PERIOD']['active']
    dt = datetime.strptime(active_period,"%Y%m")
    start,end = Get_Period(dt,PERIOD_MONTH)
    collectordata['COLLECTOR_PERIOD'].update({'start':start,'end':end})
    logger.debug(f"{this()}: dt: {dt} active_period={active_period}") 
    logger.debug(f"{this()}: COLLECTOR_PERIOD={collectordata['COLLECTOR_PERIOD']}") 
    
    sharding = False
    # GV Here we'll include sharding required code
    if 'COLLECTOR_CIT_SHARDING' in current_app.config: 
        sharding = current_app.config['COLLECTOR_CIT_SHARDING']
    if sharding:
        # GV Get customer id, just in case is needed
        customer = current_user.cost_center.Cus_Id
        cus_sharding = current_app.config.get('COLLECTOR_CUS_SHARDING') if current_app.config.get('COLLECTOR_CUS_SHARDING') else None
        # GV If required customer sharding then affect suffix
        if cus_sharding:
            cus_sharding = True if cus_sharding.upper() in ['TRUE','T','YES','Y','VERDADERO','V'] else False
        if cus_sharding:
            suffix = f"{customer}{active_period}"
        else:
            # Use default non tenant suffix 
            suffix = active_period  
        # GV Nedd to check if sharded table exists, if not should be created
        charge_item.set_shard(suffix)
        flash(                 f"Using shardened table: {charge_item.__table__.name}") 
        logger.debug(f"{this()}: Using shardened table: {charge_item.__table__.name}") 
    
    return collectordata





