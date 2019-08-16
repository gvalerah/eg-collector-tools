from datetime import datetime                         
from flask import render_template, session, redirect, url_for, current_app, flash
from .              import main

from flask          import request
from time           import strftime

#from .forms import NameForm
from ..             import db
from ..             import logger
from ..             import C
from ..models       import User
#from ..email import send_email
from sqlalchemy     import exc

from flask_login    import login_required
from ..decorators   import admin_required, permission_required
from ..models       import Permission


""" Application decorators for routes """
""" Decorators specify main routes to be handled by Collector Solution """

@main.route('/', methods=['GET', 'POST'])
def index():
    
    # Espera a capitulo 3 para mejorar procedimiento de respuesta, hard coding mucho aqui

    #logger.debug("index() IN")

    data =  {   "name":current_app.name,
                "app_name":C.app_name,
                "date_time":strftime('%Y-%m-%d %H:%M:%S'),
                "user_agent":request.headers.get('User-Agent'),
                "current_time":datetime.utcnow(),
                "db":db,
                "logger":logger,
                "C":C,
                "current_app.logger":current_app.logger
            }
    name = None
    #password = None
    #form = NameForm()
    """
    if form.validate_on_submit():
        name = form.name.data
        password = form.password.data
        form.name.data = ''            
        form.password.data = ''  
        return redirect(url_for('.index'))          
    #logger.debug("index() OUT")
    #return render_template('collector.html',data=data, form=form, name=name,password=password)
    """
    #return render_template('collector.html',data=data, name=name,password=password, form=form)
    return render_template('collector.html',data=data)


@main.route('/under_construction', methods=['GET','POST'])
def under_construction():   
    return render_template('under_construction.html')

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



"""
@main.route('/', methods=['GET', 'POST'])
def index():
    #print()
    #print("globals()             =")
    #for x in globals():
    #    print("   ",x)
    #print()
    #print("locals()             =")
    #for x in locals():
    #    print("   ",x)
    #print()
    #print("def index: db     =",db)
    #print("def index: C      =",C)
    #print("def index: logger =",logger)
    #print("def index: main   =",main)
    #print("def index: dir(main)=")
    #for x in dir(main):
    #    print("   ",x)
    #print()
    
    #print("vars(globals()        =",vars(globals()))
    #print()
    #print("def index: dir current_app       =")
    #for x in dir(current_app):
    #    print("   ",x)
    #print()
    #print()
    #print("def index: current_app           =",current_app)
    #print("def index: current_app.name      =",current_app.name    ,"next is logger"   )
    #print("def index: current_app.logger    =",current_app.logger  ,"next is db"       )
    #print("def index: dir.current_app.config=")
    #for x in dir(current_app.config):
    #    print("   ",x)
    #print("def index: current_app.config.keys()=",current_app.config.keys())
    #print("def index: current_app.config['C']  =",current_app.config['C'])
    #print("def index: vars(current_app.config['C']  =",vars(current_app.config['C']))
    #C=current_app.config['C']
    #print("def index: C=",C)
    #db=C.db
    #print("def index: db=",db)
    #logger=C.logger
    #print("def index: logger=",logger)

    #print()
    #"print("current_app.db        =",current_app.db      ,"next is C"        )
    #"print("current_app.C         =",current_app.C                           )
    #"print("vars current_app.C    =",vars(current_app.C)                     )
    print()
    print("def index: type current_app",type(current_app),"app",current_app)
    print("def index: type db ",type(db),"db",db)
    print("def index: type logger ",type(logger),"logger",logger)
    print("def index: type C.logger ",type(C.logger),"C.logger",C.logger)
    # Espera a capitulo 3 para mejorar procedimiento de respuesta, hard coding mucho aqui
    #logger.debug("index() IN")
    print()

    data =  {   "name":current_app.name,
                "app_name":C.app_name,
                "date_time":strftime('%Y-%m-%d %H:%M:%S'),
                "user_agent":request.headers.get('User-Agent'),
                "current_time":datetime.utcnow(),
                "db":db,
                "logger":logger,
                "C":C
            }
    name = None
    password = None
    form = NameForm()
    " ""
    if form.validate_on_submit():
        name = form.name.data
        password = form.password.data
        form.name.data = ''            
        form.password.data = ''            
    #logger.debug("index() OUT")
    #return render_template('collector.html',data=data, form=form, name=name,password=password)
    " ""
    return render_template('test.html',data=data, name=name,password=password, form=form)
"""
