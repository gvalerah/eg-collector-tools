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
# =============================================================================

# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-11-30 16:47:18
# =============================================================================


from ..models import cit_generation,frm_cit_generation,frm_cit_generation_delete
from ..models import cit_status,frm_cit_status,frm_cit_status_delete
from ..models import cu_operation,frm_cu_operation,frm_cu_operation_delete
from ..models import cu_type,frm_cu_type,frm_cu_type_delete
from ..models import charge_item,frm_charge_item,frm_charge_item_delete
from ..models import charge_unit,frm_charge_unit,frm_charge_unit_delete
from ..models import configuration_item,frm_configuration_item,frm_configuration_item_delete
from ..models import cost_center,frm_cost_center,frm_cost_center_delete
from ..models import country,frm_country,frm_country_delete
from ..models import country_currency,frm_country_currency,frm_country_currency_delete
from ..models import currency,frm_currency,frm_currency_delete
from ..models import customer,frm_customer,frm_customer_delete
from ..models import dev_form,frm_dev_form,frm_dev_form_delete
from ..models import dev_table,frm_dev_table,frm_dev_table_delete
from ..models import exchange_rate,frm_exchange_rate,frm_exchange_rate_delete
from ..models import measure_unit,frm_measure_unit,frm_measure_unit_delete
from ..models import platform,frm_platform,frm_platform_delete
from ..models import rat_period,frm_rat_period,frm_rat_period_delete
from ..models import rate,frm_rate,frm_rate_delete
from ..models import trace,frm_trace,frm_trace_delete

""" Application decorators for routes """
""" Decorators specify main routes to be handled by Collector Solution """

"""
@main.route('/', methods=['GET', 'POST'])
def index():
    # Espera a capitulo 3 para mejorar procedimiento de respuesta, hard coding mucho aqui
    logger.debug("index() IN")

    data =  {   "name":current_app.name,
                "app_name":C.app_name,
                "date_time":strftime('%Y-%m-%d %H:%M:%S'),
                "user_agent":request.headers.get('User-Agent'),
                "current_time":datetime.utcnow()
            }
    name = None
    password = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        password = form.password.data
        form.name.data = ''            
        form.password.data = ''            
    logger.debug("index() OUT")
    return render_template('collector.html',data=data, form=form, name=name,password=password)
"""
       
@main.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name

@main.route('/reports/<report>&<customer>&<fromx>&<tox>&<currency>')
def reports(report,customer,fromx,tox,currency):
    logger.debug("reports() IN %s,%s,%s,%s,%s"% (report,customer,fromx,tox,currency))

    r = page_header()
    r+= '<h1>Get \'%s\' for customer %s in period %s to %s cur=%s</h1>' % (report,customer,fromx,tox,currency)
    # SQL Query call here
    query = text("CALL Get_Billing_Resume(%s,'%s','%s',1,'%s')"%(customer,fromx,tox,currency))
    try:
        result = C.db.execute(query).fetchall()
    except Exception as e:
        r+="<h2>EXCEPTION:%s</h2>"%e
    r+="<table>"
    sum=0.0
    for row in result:
        r+='<tr>'
        for c in range(len(row)):
            r+="<td>%s</td>"%str(row[c])
        sum+=row[25]
        r+="<td>%.2f</td>"%sum
        r+='</tr>'
    r+="</table>"
    r+="<p>Total in %s = %10.2f<p>"%(currency,sum)
    r+=page_footer()
    logger.debug("reports() OUT %s"% (r))
    return r

@main.route('/table/<name>')
def table(name):
    logger.debug("table() IN %s"% (name))

    r = page_header()
    r+= '<h1>Get \'%s\' data</h1>' % (name)

    # SQL Query call here
    
    try:
        # Build Query
        query = text("SELECT * FROM %s"%(name))

        # Get keys (column names) from Query        
        keys=C.db.execute(query).keys()

        r+="<p>Query=%s</p>"%str(query)
        r+="<p>Keys =%s</p>"%str(keys)
        r+="<table>"
        r+='<tr style="border:2px solid blue ; background-color:blue; color:yellow">'
        for key in keys:
           r+="<td><b>%s</b></td>"%key
        r+='</tr>'           
               
        result=None
        result = C.db.execute(query).fetchall()
        rc = 0
        for row in result:
            if (rc%2):
                r+='<tr style="background-color:cyan">'
                #r+='<tr id="tr01">'
            else:
                r+='<tr style="background-color:white">'
                #r+='<tr id="tr02">'
            
            for c in range(len(row)):
                r+="<td>%s</td>"%str(row[c])
            r+='</tr>'
            rc+=1
        r+="</table>"
        if rc:
            r+="<p>Count=%s</p>"%str(rc)
    except Exception as e:
        r+="<h2>EXCEPTION:%s</h2>"%e
    r+=page_footer()
    logger.debug("table() out %s"% (r))
    return r

@main.route('/query/<name>')
def query(name):
    logger.debug("query() IN %s"% (name))

    # SQL Query call here    
    try:
        # Build Query
        query = text("SELECT * FROM %s"%(name))

        # Get keys (column names) from Query        
        keys=C.db.execute(query).keys()

        rows = C.db.execute(query).fetchall()
    except Exception as e:
        msg="EXCEPTION: %s"%e
        logger.error("query() %s"% (msg))
        return "<h2>%s</h2>"%msg
    
    logger.debug("query() out")
    return render_template('query.html',name=name,keys=keys,rows=rows,count=len(rows))

@main.route('/query_orm/<table_name>')
def query_orm(table_name):
    logger.debug("query() IN %s"% (table_name))
    # SQL Query call here    
    try:
        Session = sessionmaker(bind=C.db)  
        session=Session()
        keys = ("ID","NOMBRE","CC")
        rows = session.query(Customers.Cus_Id,Customers.Cus_Name,Customers.CC_Id).all()
    except Exception as e:
        msg="EXCEPTION: %s"%e
        logger.error("query() %s"% (msg))
        return "<h2>%s</h2>"%msg
    
    logger.debug("query() out")
    return render_template('query_orm.html',name=table_name,keys=keys,rows=rows,count=len(rows))
    
# =============================================================================

# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-11-30 16:47:18
# =============================================================================


@main.route('/forms/Charge_Items', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@permission_required(Permission.MODIFY)
@admin_required
def forms_Charge_Items():
    """ Form handling function for table Charge_Items """

    logger.debug('Enter: forms_Charge_Items()')
    CU_Id  =  request.args.get('CU_Id',0,type=int)
    CIT_Date  =  request.args.get('CIT_Date',0,type=int)
    CIT_Time  =  request.args.get('CIT_Time',0,type=int)
    parent_key  =  request.args.get('parent_key',None,type=str)
    parent_value=  request.args.get('parent_value',0,type=int)

    row =  charge_item.query.filter(charge_item.CU_Id == CU_Id,charge_item.CIT_Date == CIT_Date,charge_item.CIT_Time == CIT_Time).first()
    if row is None:
        row=charge_item()

    session['data'] =  { 'CU_Id':row.CU_Id, 'CIT_Date':row.CIT_Date, 'CIT_Time':str(row.CIT_Time), 'CIT_Quantity':row.CIT_Quantity, 'CIT_Status':row.CIT_Status, 'CIT_Is_Active':row.CIT_Is_Active}
    if parent_key is not None:
       session['data'][parent_key] = parent_value

       print('parent_key  = ',parent_key)
       print('parent_value= ',parent_value)
       print('session["data"][parent_key] = %s'%(parent_key,session['data'][parent_key]))

    form = frm_charge_item()

    if form.has_FKs:
        form.CU_Id.choices = db.session.query(charge_unit.CU_Id,charge_unit.CU_Description).order_by(charge_unit.CU_Description).all()
        form.CIT_Status.choices = db.session.query(cit_status.CIT_Status,cit_status.Value).order_by(cit_status.Value).all()

    if form.validate_on_submit():
        if     form.submit_Save.data:
            row.CU_Id = form.CU_Id.data
            row.CIT_Date = form.CIT_Date.data
            row.CIT_Time = form.CIT_Time.data
            row.CIT_Quantity = form.CIT_Quantity.data
            row.CIT_Status = form.CIT_Status.data
            row.CIT_Is_Active = form.CIT_Is_Active.data
            try:
               db.session.close()
               db.session.add(row)
               db.session.commit()
               db.session.close()
               flash('Record %s saved OK'%(CU_Id,CIT_Date,CIT_Time))
            except Exception as e:
               db.session.rollback()
               db.session.close()
               flash('ERROR saving record : %s'%(e))
            return redirect(url_for('.select_Charge_Items_query'))
        elif   form.submit_New.data:
            print('New Data Here...')
            db.session.close()
            row=charge_item()
            return redirect(url_for('.forms_Charge_Items'))

        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.forms_Charge_Items'))

    form.CU_Id.data = row.CU_Id
    form.CIT_Date.data = row.CIT_Date
    form.CIT_Time.data = row.CIT_Time
    form.CIT_Quantity.data = row.CIT_Quantity
    form.CIT_Status.data = row.CIT_Status
    form.CIT_Is_Active.data = row.CIT_Is_Active
    return render_template('charge_items.html', form=form, row=row)

# =============================================================================

@main.route('/forms/Charge_Items_delete', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@admin_required
def forms_Charge_Items_delete():
    """ Delete record handling function for table Charge_Items """

    logger.debug('Enter: forms_Charge_Items_delete()')
    CU_Id  =  request.args.get('CU_Id',0,type=int)
    CIT_Date  =  request.args.get('CIT_Date',0,type=int)
    CIT_Time  =  request.args.get('CIT_Time',0,type=int)
    row =  charge_item.query.filter(charge_item.CU_Id == CU_Id,charge_item.CIT_Date == CIT_Date,charge_item.CIT_Time == CIT_Time).first()
    if row is None:
        row=charge_item()
    session['data'] =  { 'CU_Id':row.CU_Id, 'CIT_Date':row.CIT_Date, 'CIT_Time':str(row.CIT_Time), 'CIT_Quantity':row.CIT_Quantity, 'CIT_Status':row.CIT_Status, 'CIT_Is_Active':row.CIT_Is_Active}
    form = frm_charge_item_delete()

    if form.validate_on_submit():
        if  form.submit_Delete.data:
            print('Delete Data Here...')
            print('Delete Data Here...')
            try:
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                flash('Record %s deleted OK'%(CU_Id,CIT_Date,CIT_Time))
            except exc.IntegrityError as e:
                db.session.rollback()
                flash('INTEGRITY ERROR: Are you sure there are no dependant records in other tables?')
                return redirect(url_for('.forms_Charge_Items_delete',CU_Id=session['data']['CU_Id'],CIT_Date=session['data']['CIT_Date'],CIT_Time=session['data']['CIT_Time']))

            return redirect(url_for('.select_Charge_Items_query'))
        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
            return redirect(url_for('.select_Charge_Items_query'))
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.select_Charge_Items_query'))


    return render_template('charge_items_delete.html',C=C, form=form, data=session.get('data'),row=row)

# =============================================================================

@main.route('/select/Charge_Items_Query', methods=['GET','POST'])
@login_required
@admin_required
def select_Charge_Items_query():
    """ Select rows handling function for table Charge_Items """

    logger.debug('Enter: select_Charge_Items_query()')
    field =  request.args.get('field',None,type=str)
    value =  request.args.get('value',0,type=str)
    page  =  request.args.get('page',1,type=int)

    if field is not None:
        if   field == 'CU_Id':
            rows =  charge_item.query.filter_by(CU_Id=value)\
               .join(charge_unit,charge_item.CU_Id == charge_unit.CU_Id).add_columns(charge_unit.CU_Description)\
               .join(cit_status,charge_item.CIT_Status == cit_status.CIT_Status).add_columns(cit_status.Value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CIT_Date':
            rows =  charge_item.query.filter_by(CIT_Date=value)\
               .join(charge_unit,charge_item.CU_Id == charge_unit.CU_Id).add_columns(charge_unit.CU_Description)\
               .join(cit_status,charge_item.CIT_Status == cit_status.CIT_Status).add_columns(cit_status.Value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CIT_Time':
            rows =  charge_item.query.filter_by(CIT_Time=value)\
               .join(charge_unit,charge_item.CU_Id == charge_unit.CU_Id).add_columns(charge_unit.CU_Description)\
               .join(cit_status,charge_item.CIT_Status == cit_status.CIT_Status).add_columns(cit_status.Value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CIT_Quantity':
            rows =  charge_item.query.filter_by(CIT_Quantity=value)\
               .join(charge_unit,charge_item.CU_Id == charge_unit.CU_Id).add_columns(charge_unit.CU_Description)\
               .join(cit_status,charge_item.CIT_Status == cit_status.CIT_Status).add_columns(cit_status.Value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CIT_Status':
            rows =  charge_item.query.filter_by(CIT_Status=value)\
               .join(charge_unit,charge_item.CU_Id == charge_unit.CU_Id).add_columns(charge_unit.CU_Description)\
               .join(cit_status,charge_item.CIT_Status == cit_status.CIT_Status).add_columns(cit_status.Value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CIT_Is_Active':
            rows =  charge_item.query.filter_by(CIT_Is_Active=value)\
               .join(charge_unit,charge_item.CU_Id == charge_unit.CU_Id).add_columns(charge_unit.CU_Description)\
               .join(cit_status,charge_item.CIT_Status == cit_status.CIT_Status).add_columns(cit_status.Value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
    else:
       rows =  charge_item.query\
               .join(charge_unit,charge_item.CU_Id == charge_unit.CU_Id).add_columns(charge_unit.CU_Description)\
               .join(cit_status,charge_item.CIT_Status == cit_status.CIT_Status).add_columns(cit_status.Value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)

    next_url = url_for('.select_Charge_Items_query', page=rows.next_num) \
        if rows.has_next else None
    prev_url = url_for('.select_Charge_Items_query', page=rows.prev_num) \
        if rows.has_prev else None

    return render_template('charge_items_All.html',C=C,rows=rows.items,next_url=next_url,prev_url=prev_url)
# =============================================================================

# =============================================================================

# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-11-30 16:47:18
# =============================================================================


@main.route('/forms/Charge_Units', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@permission_required(Permission.MODIFY)
@admin_required
def forms_Charge_Units():
    """ Form handling function for table Charge_Units """

    logger.debug('Enter: forms_Charge_Units()')
    CU_Id  =  request.args.get('CU_Id',0,type=int)
    parent_key  =  request.args.get('parent_key',None,type=str)
    parent_value=  request.args.get('parent_value',0,type=int)

    row =  charge_unit.query.filter(charge_unit.CU_Id == CU_Id).first()
    if row is None:
        row=charge_unit()

    session['data'] =  { 'CU_Id':row.CU_Id, 'CI_Id':row.CI_Id, 'CU_Description':row.CU_Description, 'CU_UUID':row.CU_UUID, 'CU_Is_Billeable':row.CU_Is_Billeable, 'CU_Is_Always_Billeable':row.CU_Is_Always_Billeable, 'CU_Quantity':row.CU_Quantity, 'CU_Operation':row.CU_Operation, 'Typ_Code':row.Typ_Code, 'CC_Id':row.CC_Id, 'CIT_Generation':row.CIT_Generation, 'Rat_Id':row.Rat_Id, 'CU_Reference_1':row.CU_Reference_1, 'CU_Reference_2':row.CU_Reference_2, 'CU_Reference_3':row.CU_Reference_3}
    if parent_key is not None:
       session['data'][parent_key] = parent_value

       print('parent_key  = ',parent_key)
       print('parent_value= ',parent_value)
       print('session["data"][parent_key] = %s'%(parent_key,session['data'][parent_key]))

    form = frm_charge_unit()

    if form.has_FKs:
        form.CI_Id.choices = db.session.query(configuration_item.CI_Id,configuration_item.CI_Name).order_by(configuration_item.CI_Name).all()
        form.CU_Operation.choices = db.session.query(cu_operation.CU_Operation,cu_operation.Value).order_by(cu_operation.Value).all()
        form.Typ_Code.choices = db.session.query(cu_type.Typ_Code,cu_type.Typ_Description).order_by(cu_type.Typ_Description).all()
        form.CC_Id.choices = db.session.query(cost_center.CC_Id,cost_center.CC_Description).order_by(cost_center.CC_Description).all()
        form.CIT_Generation.choices = db.session.query(cit_generation.CIT_Generation,cit_generation.Value).order_by(cit_generation.Value).all()

    if form.validate_on_submit():
        if     form.submit_Save.data:
            row.CI_Id = form.CI_Id.data
            row.CU_Description = form.CU_Description.data
            row.CU_UUID = form.CU_UUID.data
            row.CU_Is_Billeable = form.CU_Is_Billeable.data
            row.CU_Is_Always_Billeable = form.CU_Is_Always_Billeable.data
            row.CU_Quantity = form.CU_Quantity.data
            row.CU_Operation = form.CU_Operation.data
            row.Typ_Code = form.Typ_Code.data
            row.CC_Id = form.CC_Id.data
            row.CIT_Generation = form.CIT_Generation.data
            row.CU_Reference_1 = form.CU_Reference_1.data
            row.CU_Reference_2 = form.CU_Reference_2.data
            row.CU_Reference_3 = form.CU_Reference_3.data
            try:
               db.session.close()
               db.session.add(row)
               db.session.commit()
               db.session.close()
               flash('Record %s saved OK'%(CU_Id))
            except Exception as e:
               db.session.rollback()
               db.session.close()
               flash('ERROR saving record : %s'%(e))
            return redirect(url_for('.select_Charge_Units_query'))
        elif   form.submit_New.data:
            print('New Data Here...')
            db.session.close()
            row=charge_unit()
            pass
            pass
            pass
            pass
            pass
            pass
            pass
            pass
            pass
            pass
            pass
            pass
            pass
            pass
            return redirect(url_for('.forms_Charge_Units',CU_Id=row.CU_Id))

        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.forms_Charge_Units',CU_Id=row.CU_Id))

    form.CI_Id.data = row.CI_Id
    form.CU_Description.data = row.CU_Description
    form.CU_UUID.data = row.CU_UUID
    form.CU_Is_Billeable.data = row.CU_Is_Billeable
    form.CU_Is_Always_Billeable.data = row.CU_Is_Always_Billeable
    form.CU_Quantity.data = row.CU_Quantity
    form.CU_Operation.data = row.CU_Operation
    form.Typ_Code.data = row.Typ_Code
    form.CC_Id.data = row.CC_Id
    form.CIT_Generation.data = row.CIT_Generation
    form.CU_Reference_1.data = row.CU_Reference_1
    form.CU_Reference_2.data = row.CU_Reference_2
    form.CU_Reference_3.data = row.CU_Reference_3
    return render_template('charge_units.html', form=form, row=row)

# =============================================================================

@main.route('/forms/Charge_Units_delete', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@admin_required
def forms_Charge_Units_delete():
    """ Delete record handling function for table Charge_Units """

    logger.debug('Enter: forms_Charge_Units_delete()')
    CU_Id  =  request.args.get('CU_Id',0,type=int)
    row =  charge_unit.query.filter(charge_unit.CU_Id == CU_Id).first()
    if row is None:
        row=charge_unit()
    session['data'] =  { 'CU_Id':row.CU_Id, 'CI_Id':row.CI_Id, 'CU_Description':row.CU_Description, 'CU_UUID':row.CU_UUID, 'CU_Is_Billeable':row.CU_Is_Billeable, 'CU_Is_Always_Billeable':row.CU_Is_Always_Billeable, 'CU_Quantity':row.CU_Quantity, 'CU_Operation':row.CU_Operation, 'Typ_Code':row.Typ_Code, 'CC_Id':row.CC_Id, 'CIT_Generation':row.CIT_Generation, 'Rat_Id':row.Rat_Id, 'CU_Reference_1':row.CU_Reference_1, 'CU_Reference_2':row.CU_Reference_2, 'CU_Reference_3':row.CU_Reference_3}
    form = frm_charge_unit_delete()

    if form.validate_on_submit():
        if  form.submit_Delete.data:
            print('Delete Data Here...')
            print('Delete Data Here...')
            try:
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                flash('Record %s deleted OK'%(CU_Id))
            except exc.IntegrityError as e:
                db.session.rollback()
                flash('INTEGRITY ERROR: Are you sure there are no dependant records in other tables?')
                return redirect(url_for('.forms_Charge_Units_delete',CU_Id=session['data']['CU_Id']))

            return redirect(url_for('.select_Charge_Units_query'))
        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
            return redirect(url_for('.select_Charge_Units_query'))
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.select_Charge_Units_query'))


    return render_template('charge_units_delete.html',C=C, form=form, data=session.get('data'),row=row)

# =============================================================================

@main.route('/select/Charge_Units_Query', methods=['GET','POST'])
@login_required
@admin_required
def select_Charge_Units_query():
    """ Select rows handling function for table Charge_Units """

    logger.debug('Enter: select_Charge_Units_query()')
    field =  request.args.get('field',None,type=str)
    value =  request.args.get('value',0,type=str)
    page  =  request.args.get('page',1,type=int)

    if field is not None:
        if   field == 'CU_Id':
            rows =  charge_unit.query.filter_by(CU_Id=value)\
               .join(configuration_item,charge_unit.CI_Id == configuration_item.CI_Id).add_columns(configuration_item.CI_Name)\
               .join(cu_operation,charge_unit.CU_Operation == cu_operation.CU_Operation).add_columns(cu_operation.Value)\
               .join(cu_type,charge_unit.Typ_Code == cu_type.Typ_Code).add_columns(cu_type.Typ_Description)\
               .join(cost_center,charge_unit.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .join(cit_generation,charge_unit.CIT_Generation == cit_generation.CIT_Generation).add_columns(cit_generation.Value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CI_Id':
            rows =  charge_unit.query.filter_by(CI_Id=value)\
               .join(configuration_item,charge_unit.CI_Id == configuration_item.CI_Id).add_columns(configuration_item.CI_Name)\
               .join(cu_operation,charge_unit.CU_Operation == cu_operation.CU_Operation).add_columns(cu_operation.Value)\
               .join(cu_type,charge_unit.Typ_Code == cu_type.Typ_Code).add_columns(cu_type.Typ_Description)\
               .join(cost_center,charge_unit.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .join(cit_generation,charge_unit.CIT_Generation == cit_generation.CIT_Generation).add_columns(cit_generation.Value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CU_Description':
            rows =  charge_unit.query.filter_by(CU_Description=value)\
               .join(configuration_item,charge_unit.CI_Id == configuration_item.CI_Id).add_columns(configuration_item.CI_Name)\
               .join(cu_operation,charge_unit.CU_Operation == cu_operation.CU_Operation).add_columns(cu_operation.Value)\
               .join(cu_type,charge_unit.Typ_Code == cu_type.Typ_Code).add_columns(cu_type.Typ_Description)\
               .join(cost_center,charge_unit.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .join(cit_generation,charge_unit.CIT_Generation == cit_generation.CIT_Generation).add_columns(cit_generation.Value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CU_UUID':
            rows =  charge_unit.query.filter_by(CU_UUID=value)\
               .join(configuration_item,charge_unit.CI_Id == configuration_item.CI_Id).add_columns(configuration_item.CI_Name)\
               .join(cu_operation,charge_unit.CU_Operation == cu_operation.CU_Operation).add_columns(cu_operation.Value)\
               .join(cu_type,charge_unit.Typ_Code == cu_type.Typ_Code).add_columns(cu_type.Typ_Description)\
               .join(cost_center,charge_unit.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .join(cit_generation,charge_unit.CIT_Generation == cit_generation.CIT_Generation).add_columns(cit_generation.Value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CU_Is_Billeable':
            rows =  charge_unit.query.filter_by(CU_Is_Billeable=value)\
               .join(configuration_item,charge_unit.CI_Id == configuration_item.CI_Id).add_columns(configuration_item.CI_Name)\
               .join(cu_operation,charge_unit.CU_Operation == cu_operation.CU_Operation).add_columns(cu_operation.Value)\
               .join(cu_type,charge_unit.Typ_Code == cu_type.Typ_Code).add_columns(cu_type.Typ_Description)\
               .join(cost_center,charge_unit.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .join(cit_generation,charge_unit.CIT_Generation == cit_generation.CIT_Generation).add_columns(cit_generation.Value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CU_Is_Always_Billeable':
            rows =  charge_unit.query.filter_by(CU_Is_Always_Billeable=value)\
               .join(configuration_item,charge_unit.CI_Id == configuration_item.CI_Id).add_columns(configuration_item.CI_Name)\
               .join(cu_operation,charge_unit.CU_Operation == cu_operation.CU_Operation).add_columns(cu_operation.Value)\
               .join(cu_type,charge_unit.Typ_Code == cu_type.Typ_Code).add_columns(cu_type.Typ_Description)\
               .join(cost_center,charge_unit.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .join(cit_generation,charge_unit.CIT_Generation == cit_generation.CIT_Generation).add_columns(cit_generation.Value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CU_Quantity':
            rows =  charge_unit.query.filter_by(CU_Quantity=value)\
               .join(configuration_item,charge_unit.CI_Id == configuration_item.CI_Id).add_columns(configuration_item.CI_Name)\
               .join(cu_operation,charge_unit.CU_Operation == cu_operation.CU_Operation).add_columns(cu_operation.Value)\
               .join(cu_type,charge_unit.Typ_Code == cu_type.Typ_Code).add_columns(cu_type.Typ_Description)\
               .join(cost_center,charge_unit.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .join(cit_generation,charge_unit.CIT_Generation == cit_generation.CIT_Generation).add_columns(cit_generation.Value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CU_Operation':
            rows =  charge_unit.query.filter_by(CU_Operation=value)\
               .join(configuration_item,charge_unit.CI_Id == configuration_item.CI_Id).add_columns(configuration_item.CI_Name)\
               .join(cu_operation,charge_unit.CU_Operation == cu_operation.CU_Operation).add_columns(cu_operation.Value)\
               .join(cu_type,charge_unit.Typ_Code == cu_type.Typ_Code).add_columns(cu_type.Typ_Description)\
               .join(cost_center,charge_unit.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .join(cit_generation,charge_unit.CIT_Generation == cit_generation.CIT_Generation).add_columns(cit_generation.Value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Typ_Code':
            rows =  charge_unit.query.filter_by(Typ_Code=value)\
               .join(configuration_item,charge_unit.CI_Id == configuration_item.CI_Id).add_columns(configuration_item.CI_Name)\
               .join(cu_operation,charge_unit.CU_Operation == cu_operation.CU_Operation).add_columns(cu_operation.Value)\
               .join(cu_type,charge_unit.Typ_Code == cu_type.Typ_Code).add_columns(cu_type.Typ_Description)\
               .join(cost_center,charge_unit.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .join(cit_generation,charge_unit.CIT_Generation == cit_generation.CIT_Generation).add_columns(cit_generation.Value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CC_Id':
            rows =  charge_unit.query.filter_by(CC_Id=value)\
               .join(configuration_item,charge_unit.CI_Id == configuration_item.CI_Id).add_columns(configuration_item.CI_Name)\
               .join(cu_operation,charge_unit.CU_Operation == cu_operation.CU_Operation).add_columns(cu_operation.Value)\
               .join(cu_type,charge_unit.Typ_Code == cu_type.Typ_Code).add_columns(cu_type.Typ_Description)\
               .join(cost_center,charge_unit.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .join(cit_generation,charge_unit.CIT_Generation == cit_generation.CIT_Generation).add_columns(cit_generation.Value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CIT_Generation':
            rows =  charge_unit.query.filter_by(CIT_Generation=value)\
               .join(configuration_item,charge_unit.CI_Id == configuration_item.CI_Id).add_columns(configuration_item.CI_Name)\
               .join(cu_operation,charge_unit.CU_Operation == cu_operation.CU_Operation).add_columns(cu_operation.Value)\
               .join(cu_type,charge_unit.Typ_Code == cu_type.Typ_Code).add_columns(cu_type.Typ_Description)\
               .join(cost_center,charge_unit.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .join(cit_generation,charge_unit.CIT_Generation == cit_generation.CIT_Generation).add_columns(cit_generation.Value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Rat_Id':
            rows =  charge_unit.query.filter_by(Rat_Id=value)\
               .join(configuration_item,charge_unit.CI_Id == configuration_item.CI_Id).add_columns(configuration_item.CI_Name)\
               .join(cu_operation,charge_unit.CU_Operation == cu_operation.CU_Operation).add_columns(cu_operation.Value)\
               .join(cu_type,charge_unit.Typ_Code == cu_type.Typ_Code).add_columns(cu_type.Typ_Description)\
               .join(cost_center,charge_unit.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .join(cit_generation,charge_unit.CIT_Generation == cit_generation.CIT_Generation).add_columns(cit_generation.Value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CU_Reference_1':
            rows =  charge_unit.query.filter_by(CU_Reference_1=value)\
               .join(configuration_item,charge_unit.CI_Id == configuration_item.CI_Id).add_columns(configuration_item.CI_Name)\
               .join(cu_operation,charge_unit.CU_Operation == cu_operation.CU_Operation).add_columns(cu_operation.Value)\
               .join(cu_type,charge_unit.Typ_Code == cu_type.Typ_Code).add_columns(cu_type.Typ_Description)\
               .join(cost_center,charge_unit.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .join(cit_generation,charge_unit.CIT_Generation == cit_generation.CIT_Generation).add_columns(cit_generation.Value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CU_Reference_2':
            rows =  charge_unit.query.filter_by(CU_Reference_2=value)\
               .join(configuration_item,charge_unit.CI_Id == configuration_item.CI_Id).add_columns(configuration_item.CI_Name)\
               .join(cu_operation,charge_unit.CU_Operation == cu_operation.CU_Operation).add_columns(cu_operation.Value)\
               .join(cu_type,charge_unit.Typ_Code == cu_type.Typ_Code).add_columns(cu_type.Typ_Description)\
               .join(cost_center,charge_unit.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .join(cit_generation,charge_unit.CIT_Generation == cit_generation.CIT_Generation).add_columns(cit_generation.Value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CU_Reference_3':
            rows =  charge_unit.query.filter_by(CU_Reference_3=value)\
               .join(configuration_item,charge_unit.CI_Id == configuration_item.CI_Id).add_columns(configuration_item.CI_Name)\
               .join(cu_operation,charge_unit.CU_Operation == cu_operation.CU_Operation).add_columns(cu_operation.Value)\
               .join(cu_type,charge_unit.Typ_Code == cu_type.Typ_Code).add_columns(cu_type.Typ_Description)\
               .join(cost_center,charge_unit.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .join(cit_generation,charge_unit.CIT_Generation == cit_generation.CIT_Generation).add_columns(cit_generation.Value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
    else:
       rows =  charge_unit.query\
               .join(configuration_item,charge_unit.CI_Id == configuration_item.CI_Id).add_columns(configuration_item.CI_Name)\
               .join(cu_operation,charge_unit.CU_Operation == cu_operation.CU_Operation).add_columns(cu_operation.Value)\
               .join(cu_type,charge_unit.Typ_Code == cu_type.Typ_Code).add_columns(cu_type.Typ_Description)\
               .join(cost_center,charge_unit.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .join(cit_generation,charge_unit.CIT_Generation == cit_generation.CIT_Generation).add_columns(cit_generation.Value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)

    next_url = url_for('.select_Charge_Units_query', page=rows.next_num) \
        if rows.has_next else None
    prev_url = url_for('.select_Charge_Units_query', page=rows.prev_num) \
        if rows.has_prev else None

    return render_template('charge_units_All.html',C=C,rows=rows.items,next_url=next_url,prev_url=prev_url)
# =============================================================================

# =============================================================================

# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-11-30 16:47:18
# =============================================================================


@main.route('/forms/CIT_Generations', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@permission_required(Permission.MODIFY)
@admin_required
def forms_CIT_Generations():
    """ Form handling function for table CIT_Generations """

    logger.debug('Enter: forms_CIT_Generations()')
    CIT_Generation  =  request.args.get('CIT_Generation',0,type=int)
    row =  cit_generation.query.filter(cit_generation.CIT_Generation == CIT_Generation).first()
    if row is None:
        row=cit_generation()

    session['data'] =  { 'CIT_Generation':row.CIT_Generation, 'Value':row.Value}
    form = frm_cit_generation()

    if form.validate_on_submit():
        if     form.submit_Save.data:
            row.CIT_Generation = form.CIT_Generation.data
            row.Value = form.Value.data
            try:
               db.session.close()
               db.session.add(row)
               db.session.commit()
               db.session.close()
               flash('Record %s saved OK'%(CIT_Generation))
            except Exception as e:
               db.session.rollback()
               db.session.close()
               flash('ERROR saving record : %s'%(e))
            return redirect(url_for('.select_CIT_Generations_query'))
        elif   form.submit_New.data:
            print('New Data Here...')
            db.session.close()
            row=cit_generation()
            return redirect(url_for('.forms_CIT_Generations'))

        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.forms_CIT_Generations'))

    form.CIT_Generation.data = row.CIT_Generation
    form.Value.data = row.Value
    return render_template('cit_generations.html', form=form, row=row)

# =============================================================================

@main.route('/forms/CIT_Generations_delete', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@admin_required
def forms_CIT_Generations_delete():
    """ Delete record handling function for table CIT_Generations """

    logger.debug('Enter: forms_CIT_Generations_delete()')
    CIT_Generation  =  request.args.get('CIT_Generation',0,type=int)
    row =  cit_generation.query.filter(cit_generation.CIT_Generation == CIT_Generation).first()
    if row is None:
        row=cit_generation()
    session['data'] =  { 'CIT_Generation':row.CIT_Generation, 'Value':row.Value}
    form = frm_cit_generation_delete()

    if form.validate_on_submit():
        if  form.submit_Delete.data:
            print('Delete Data Here...')
            print('Delete Data Here...')
            try:
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                flash('Record %s deleted OK'%(CIT_Generation))
            except exc.IntegrityError as e:
                db.session.rollback()
                flash('INTEGRITY ERROR: Are you sure there are no dependant records in other tables?')
                return redirect(url_for('.forms_CIT_Generations_delete',CIT_Generation=session['data']['CIT_Generation']))

            return redirect(url_for('.select_CIT_Generations_query'))
        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
            return redirect(url_for('.select_CIT_Generations_query'))
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.select_CIT_Generations_query'))


    return render_template('cit_generations_delete.html',C=C, form=form, data=session.get('data'),row=row)

# =============================================================================

@main.route('/select/CIT_Generations_Query', methods=['GET','POST'])
@login_required
@admin_required
def select_CIT_Generations_query():
    """ Select rows handling function for table CIT_Generations """

    logger.debug('Enter: select_CIT_Generations_query()')
    field =  request.args.get('field',None,type=str)
    value =  request.args.get('value',0,type=str)
    page  =  request.args.get('page',1,type=int)

    if field is not None:
        if   field == 'CIT_Generation':
            rows =  cit_generation.query.filter_by(CIT_Generation=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Value':
            rows =  cit_generation.query.filter_by(Value=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
    else:
       rows =  cit_generation.query\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)

    next_url = url_for('.select_CIT_Generations_query', page=rows.next_num) \
        if rows.has_next else None
    prev_url = url_for('.select_CIT_Generations_query', page=rows.prev_num) \
        if rows.has_prev else None

    return render_template('cit_generations_All.html',C=C,rows=rows.items,next_url=next_url,prev_url=prev_url)
# =============================================================================

# =============================================================================

# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-11-30 16:47:18
# =============================================================================


@main.route('/forms/CIT_Statuses', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@permission_required(Permission.MODIFY)
@admin_required
def forms_CIT_Statuses():
    """ Form handling function for table CIT_Statuses """

    logger.debug('Enter: forms_CIT_Statuses()')
    CIT_Status  =  request.args.get('CIT_Status',0,type=int)
    row =  cit_status.query.filter(cit_status.CIT_Status == CIT_Status).first()
    if row is None:
        row=cit_status()

    session['data'] =  { 'CIT_Status':row.CIT_Status, 'Value':row.Value}
    form = frm_cit_status()

    if form.validate_on_submit():
        if     form.submit_Save.data:
            row.CIT_Status = form.CIT_Status.data
            row.Value = form.Value.data
            try:
               db.session.close()
               db.session.add(row)
               db.session.commit()
               db.session.close()
               flash('Record %s saved OK'%(CIT_Status))
            except Exception as e:
               db.session.rollback()
               db.session.close()
               flash('ERROR saving record : %s'%(e))
            return redirect(url_for('.select_CIT_Statuses_query'))
        elif   form.submit_New.data:
            print('New Data Here...')
            db.session.close()
            row=cit_status()
            return redirect(url_for('.forms_CIT_Statuses'))

        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.forms_CIT_Statuses'))

    form.CIT_Status.data = row.CIT_Status
    form.Value.data = row.Value
    return render_template('cit_statuses.html', form=form, row=row)

# =============================================================================

@main.route('/forms/CIT_Statuses_delete', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@admin_required
def forms_CIT_Statuses_delete():
    """ Delete record handling function for table CIT_Statuses """

    logger.debug('Enter: forms_CIT_Statuses_delete()')
    CIT_Status  =  request.args.get('CIT_Status',0,type=int)
    row =  cit_status.query.filter(cit_status.CIT_Status == CIT_Status).first()
    if row is None:
        row=cit_status()
    session['data'] =  { 'CIT_Status':row.CIT_Status, 'Value':row.Value}
    form = frm_cit_status_delete()

    if form.validate_on_submit():
        if  form.submit_Delete.data:
            print('Delete Data Here...')
            print('Delete Data Here...')
            try:
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                flash('Record %s deleted OK'%(CIT_Status))
            except exc.IntegrityError as e:
                db.session.rollback()
                flash('INTEGRITY ERROR: Are you sure there are no dependant records in other tables?')
                return redirect(url_for('.forms_CIT_Statuses_delete',CIT_Status=session['data']['CIT_Status']))

            return redirect(url_for('.select_CIT_Statuses_query'))
        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
            return redirect(url_for('.select_CIT_Statuses_query'))
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.select_CIT_Statuses_query'))


    return render_template('cit_statuses_delete.html',C=C, form=form, data=session.get('data'),row=row)

# =============================================================================

@main.route('/select/CIT_Statuses_Query', methods=['GET','POST'])
@login_required
@admin_required
def select_CIT_Statuses_query():
    """ Select rows handling function for table CIT_Statuses """

    logger.debug('Enter: select_CIT_Statuses_query()')
    field =  request.args.get('field',None,type=str)
    value =  request.args.get('value',0,type=str)
    page  =  request.args.get('page',1,type=int)

    if field is not None:
        if   field == 'CIT_Status':
            rows =  cit_status.query.filter_by(CIT_Status=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Value':
            rows =  cit_status.query.filter_by(Value=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
    else:
       rows =  cit_status.query\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)

    next_url = url_for('.select_CIT_Statuses_query', page=rows.next_num) \
        if rows.has_next else None
    prev_url = url_for('.select_CIT_Statuses_query', page=rows.prev_num) \
        if rows.has_prev else None

    return render_template('cit_statuses_All.html',C=C,rows=rows.items,next_url=next_url,prev_url=prev_url)
# =============================================================================

# =============================================================================

# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-11-30 16:47:18
# =============================================================================


@main.route('/forms/Configuration_Items', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@permission_required(Permission.MODIFY)
@admin_required
def forms_Configuration_Items():
    """ Form handling function for table Configuration_Items """

    logger.debug('Enter: forms_Configuration_Items()')
    CI_Id  =  request.args.get('CI_Id',0,type=int)
    row =  configuration_item.query.filter(configuration_item.CI_Id == CI_Id).first()
    if row is None:
        row=configuration_item()

    session['data'] =  { 'CI_Id':row.CI_Id, 'CI_Name':row.CI_Name, 'CI_UUID':row.CI_UUID, 'Pla_Id':row.Pla_Id, 'CC_Id':row.CC_Id, 'CIT_Generation':row.CIT_Generation, 'Cus_Id':row.Cus_Id}
    form = frm_configuration_item()

    if form.has_FKs:
        form.Pla_Id.choices = db.session.query(platform.Pla_Id,platform.Pla_Name).order_by(platform.Pla_Name).all()
        form.CC_Id.choices = db.session.query(cost_center.CC_Id,cost_center.CC_Description).order_by(cost_center.CC_Description).all()
        form.CIT_Generation.choices = db.session.query(cit_generation.CIT_Generation,cit_generation.Value).order_by(cit_generation.Value).all()
        form.Cus_Id.choices = db.session.query(customer.Cus_Id,customer.Cus_Name).order_by(customer.Cus_Name).all()

    if form.validate_on_submit():
        if     form.submit_Save.data:
            row.CI_Name = form.CI_Name.data
            row.CI_UUID = form.CI_UUID.data
            row.Pla_Id = form.Pla_Id.data
            row.CC_Id = form.CC_Id.data
            row.CIT_Generation = form.CIT_Generation.data
            row.Cus_Id = form.Cus_Id.data
            try:
               db.session.close()
               db.session.add(row)
               db.session.commit()
               db.session.close()
               flash('Record %s saved OK'%(CI_Id))
            except Exception as e:
               db.session.rollback()
               db.session.close()
               flash('ERROR saving record : %s'%(e))
            return redirect(url_for('.select_Configuration_Items_query'))
        elif   form.submit_New.data:
            print('New Data Here...')
            db.session.close()
            row=configuration_item()
            pass
            pass
            pass
            pass
            pass
            pass
            return redirect(url_for('.forms_Configuration_Items',CI_Id=row.CI_Id))

        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.forms_Configuration_Items',CI_Id=row.CI_Id))

    form.CI_Name.data = row.CI_Name
    form.CI_UUID.data = row.CI_UUID
    form.Pla_Id.data = row.Pla_Id
    form.CC_Id.data = row.CC_Id
    form.CIT_Generation.data = row.CIT_Generation
    form.Cus_Id.data = row.Cus_Id
    return render_template('configuration_items.html', form=form, row=row)

# =============================================================================

@main.route('/forms/Configuration_Items_delete', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@admin_required
def forms_Configuration_Items_delete():
    """ Delete record handling function for table Configuration_Items """

    logger.debug('Enter: forms_Configuration_Items_delete()')
    CI_Id  =  request.args.get('CI_Id',0,type=int)
    row =  configuration_item.query.filter(configuration_item.CI_Id == CI_Id).first()
    if row is None:
        row=configuration_item()
    session['data'] =  { 'CI_Id':row.CI_Id, 'CI_Name':row.CI_Name, 'CI_UUID':row.CI_UUID, 'Pla_Id':row.Pla_Id, 'CC_Id':row.CC_Id, 'CIT_Generation':row.CIT_Generation, 'Cus_Id':row.Cus_Id}
    form = frm_configuration_item_delete()

    if form.validate_on_submit():
        if  form.submit_Delete.data:
            print('Delete Data Here...')
            print('Delete Data Here...')
            try:
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                flash('Record %s deleted OK'%(CI_Id))
            except exc.IntegrityError as e:
                db.session.rollback()
                flash('INTEGRITY ERROR: Are you sure there are no dependant records in other tables?')
                return redirect(url_for('.forms_Configuration_Items_delete',CI_Id=session['data']['CI_Id']))

            return redirect(url_for('.select_Configuration_Items_query'))
        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
            return redirect(url_for('.select_Configuration_Items_query'))
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.select_Configuration_Items_query'))


    return render_template('configuration_items_delete.html',C=C, form=form, data=session.get('data'),row=row)

# =============================================================================

@main.route('/select/Configuration_Items_Query', methods=['GET','POST'])
@login_required
@admin_required
def select_Configuration_Items_query():
    """ Select rows handling function for table Configuration_Items """

    logger.debug('Enter: select_Configuration_Items_query()')
    field =  request.args.get('field',None,type=str)
    value =  request.args.get('value',0,type=str)
    page  =  request.args.get('page',1,type=int)

    if field is not None:
        if   field == 'CI_Id':
            rows =  configuration_item.query.filter_by(CI_Id=value)\
               .join(platform,configuration_item.Pla_Id == platform.Pla_Id).add_columns(platform.Pla_Name)\
               .join(cost_center,configuration_item.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .join(cit_generation,configuration_item.CIT_Generation == cit_generation.CIT_Generation).add_columns(cit_generation.Value)\
               .join(customer,configuration_item.Cus_Id == customer.Cus_Id).add_columns(customer.Cus_Name)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CI_Name':
            rows =  configuration_item.query.filter_by(CI_Name=value)\
               .join(platform,configuration_item.Pla_Id == platform.Pla_Id).add_columns(platform.Pla_Name)\
               .join(cost_center,configuration_item.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .join(cit_generation,configuration_item.CIT_Generation == cit_generation.CIT_Generation).add_columns(cit_generation.Value)\
               .join(customer,configuration_item.Cus_Id == customer.Cus_Id).add_columns(customer.Cus_Name)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CI_UUID':
            rows =  configuration_item.query.filter_by(CI_UUID=value)\
               .join(platform,configuration_item.Pla_Id == platform.Pla_Id).add_columns(platform.Pla_Name)\
               .join(cost_center,configuration_item.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .join(cit_generation,configuration_item.CIT_Generation == cit_generation.CIT_Generation).add_columns(cit_generation.Value)\
               .join(customer,configuration_item.Cus_Id == customer.Cus_Id).add_columns(customer.Cus_Name)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Pla_Id':
            rows =  configuration_item.query.filter_by(Pla_Id=value)\
               .join(platform,configuration_item.Pla_Id == platform.Pla_Id).add_columns(platform.Pla_Name)\
               .join(cost_center,configuration_item.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .join(cit_generation,configuration_item.CIT_Generation == cit_generation.CIT_Generation).add_columns(cit_generation.Value)\
               .join(customer,configuration_item.Cus_Id == customer.Cus_Id).add_columns(customer.Cus_Name)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CC_Id':
            rows =  configuration_item.query.filter_by(CC_Id=value)\
               .join(platform,configuration_item.Pla_Id == platform.Pla_Id).add_columns(platform.Pla_Name)\
               .join(cost_center,configuration_item.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .join(cit_generation,configuration_item.CIT_Generation == cit_generation.CIT_Generation).add_columns(cit_generation.Value)\
               .join(customer,configuration_item.Cus_Id == customer.Cus_Id).add_columns(customer.Cus_Name)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CIT_Generation':
            rows =  configuration_item.query.filter_by(CIT_Generation=value)\
               .join(platform,configuration_item.Pla_Id == platform.Pla_Id).add_columns(platform.Pla_Name)\
               .join(cost_center,configuration_item.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .join(cit_generation,configuration_item.CIT_Generation == cit_generation.CIT_Generation).add_columns(cit_generation.Value)\
               .join(customer,configuration_item.Cus_Id == customer.Cus_Id).add_columns(customer.Cus_Name)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Cus_Id':
            rows =  configuration_item.query.filter_by(Cus_Id=value)\
               .join(platform,configuration_item.Pla_Id == platform.Pla_Id).add_columns(platform.Pla_Name)\
               .join(cost_center,configuration_item.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .join(cit_generation,configuration_item.CIT_Generation == cit_generation.CIT_Generation).add_columns(cit_generation.Value)\
               .join(customer,configuration_item.Cus_Id == customer.Cus_Id).add_columns(customer.Cus_Name)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
    else:
       rows =  configuration_item.query\
               .join(platform,configuration_item.Pla_Id == platform.Pla_Id).add_columns(platform.Pla_Name)\
               .join(cost_center,configuration_item.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .join(cit_generation,configuration_item.CIT_Generation == cit_generation.CIT_Generation).add_columns(cit_generation.Value)\
               .join(customer,configuration_item.Cus_Id == customer.Cus_Id).add_columns(customer.Cus_Name)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)

    next_url = url_for('.select_Configuration_Items_query', page=rows.next_num) \
        if rows.has_next else None
    prev_url = url_for('.select_Configuration_Items_query', page=rows.prev_num) \
        if rows.has_prev else None

    return render_template('configuration_items_All.html',C=C,rows=rows.items,next_url=next_url,prev_url=prev_url)
# =============================================================================

# =============================================================================

# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-11-30 16:47:18
# =============================================================================


@main.route('/forms/Cost_Centers', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@permission_required(Permission.MODIFY)
@admin_required
def forms_Cost_Centers():
    """ Form handling function for table Cost_Centers """

    logger.debug('Enter: forms_Cost_Centers()')
    CC_Id  =  request.args.get('CC_Id',0,type=int)
    row =  cost_center.query.filter(cost_center.CC_Id == CC_Id).first()
    if row is None:
        row=cost_center()

    session['data'] =  { 'CC_Id':row.CC_Id, 'CC_Code':row.CC_Code, 'CC_Description':row.CC_Description, 'Cur_Code':row.Cur_Code}
    form = frm_cost_center()

    if form.has_FKs:
        form.Cur_Code.choices = db.session.query(currency.Cur_Code,currency.Cur_Name).order_by(currency.Cur_Name).all()

    if form.validate_on_submit():
        if     form.submit_Save.data:
            row.CC_Code = form.CC_Code.data
            row.CC_Description = form.CC_Description.data
            row.Cur_Code = form.Cur_Code.data
            try:
               db.session.close()
               db.session.add(row)
               db.session.commit()
               db.session.close()
               flash('Record %s saved OK'%(CC_Id))
            except Exception as e:
               db.session.rollback()
               db.session.close()
               flash('ERROR saving record : %s'%(e))
            return redirect(url_for('.select_Cost_Centers_query'))
        elif   form.submit_New.data:
            print('New Data Here...')
            db.session.close()
            row=cost_center()
            pass
            pass
            pass
            return redirect(url_for('.forms_Cost_Centers',CC_Id=row.CC_Id))

        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.forms_Cost_Centers',CC_Id=row.CC_Id))

    form.CC_Code.data = row.CC_Code
    form.CC_Description.data = row.CC_Description
    form.Cur_Code.data = row.Cur_Code
    return render_template('cost_centers.html', form=form, row=row)

# =============================================================================

@main.route('/forms/Cost_Centers_delete', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@admin_required
def forms_Cost_Centers_delete():
    """ Delete record handling function for table Cost_Centers """

    logger.debug('Enter: forms_Cost_Centers_delete()')
    CC_Id  =  request.args.get('CC_Id',0,type=int)
    row =  cost_center.query.filter(cost_center.CC_Id == CC_Id).first()
    if row is None:
        row=cost_center()
    session['data'] =  { 'CC_Id':row.CC_Id, 'CC_Code':row.CC_Code, 'CC_Description':row.CC_Description, 'Cur_Code':row.Cur_Code}
    form = frm_cost_center_delete()

    if form.validate_on_submit():
        if  form.submit_Delete.data:
            print('Delete Data Here...')
            print('Delete Data Here...')
            try:
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                flash('Record %s deleted OK'%(CC_Id))
            except exc.IntegrityError as e:
                db.session.rollback()
                flash('INTEGRITY ERROR: Are you sure there are no dependant records in other tables?')
                return redirect(url_for('.forms_Cost_Centers_delete',CC_Id=session['data']['CC_Id']))

            return redirect(url_for('.select_Cost_Centers_query'))
        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
            return redirect(url_for('.select_Cost_Centers_query'))
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.select_Cost_Centers_query'))


    return render_template('cost_centers_delete.html',C=C, form=form, data=session.get('data'),row=row)

# =============================================================================

@main.route('/select/Cost_Centers_Query', methods=['GET','POST'])
@login_required
@admin_required
def select_Cost_Centers_query():
    """ Select rows handling function for table Cost_Centers """

    logger.debug('Enter: select_Cost_Centers_query()')
    field =  request.args.get('field',None,type=str)
    value =  request.args.get('value',0,type=str)
    page  =  request.args.get('page',1,type=int)

    if field is not None:
        if   field == 'CC_Id':
            rows =  cost_center.query.filter_by(CC_Id=value)\
               .join(currency,cost_center.Cur_Code == currency.Cur_Code).add_columns(currency.Cur_Name)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CC_Code':
            rows =  cost_center.query.filter_by(CC_Code=value)\
               .join(currency,cost_center.Cur_Code == currency.Cur_Code).add_columns(currency.Cur_Name)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CC_Description':
            rows =  cost_center.query.filter_by(CC_Description=value)\
               .join(currency,cost_center.Cur_Code == currency.Cur_Code).add_columns(currency.Cur_Name)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Cur_Code':
            rows =  cost_center.query.filter_by(Cur_Code=value)\
               .join(currency,cost_center.Cur_Code == currency.Cur_Code).add_columns(currency.Cur_Name)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
    else:
       rows =  cost_center.query\
               .join(currency,cost_center.Cur_Code == currency.Cur_Code).add_columns(currency.Cur_Name)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)

    next_url = url_for('.select_Cost_Centers_query', page=rows.next_num) \
        if rows.has_next else None
    prev_url = url_for('.select_Cost_Centers_query', page=rows.prev_num) \
        if rows.has_prev else None

    return render_template('cost_centers_All.html',C=C,rows=rows.items,next_url=next_url,prev_url=prev_url)
# =============================================================================

# =============================================================================

# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-11-30 16:47:18
# =============================================================================


@main.route('/forms/Countries_Currencies', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@permission_required(Permission.MODIFY)
@admin_required
def forms_Countries_Currencies():
    """ Form handling function for table Countries_Currencies """

    logger.debug('Enter: forms_Countries_Currencies()')
    Cou_Code  =  request.args.get('Cou_Code',0,type=int)
    Cur_Code  =  request.args.get('Cur_Code',0,type=int)
    row =  country_currency.query.filter(country_currency.Cou_Code == Cou_Code,country_currency.Cur_Code == Cur_Code).first()
    if row is None:
        row=country_currency()

    session['data'] =  { 'Cou_Code':row.Cou_Code, 'Cur_Code':row.Cur_Code, 'Cou_Cur_Comment':row.Cou_Cur_Comment}
    form = frm_country_currency()

    if form.has_FKs:
        form.Cou_Code.choices = db.session.query(country.Cou_Code,country.Cou_Name).order_by(country.Cou_Name).all()
        form.Cur_Code.choices = db.session.query(currency.Cur_Code,currency.Cur_Name).order_by(currency.Cur_Name).all()

    if form.validate_on_submit():
        if     form.submit_Save.data:
            row.Cou_Code = form.Cou_Code.data
            row.Cur_Code = form.Cur_Code.data
            row.Cou_Cur_Comment = form.Cou_Cur_Comment.data
            try:
               db.session.close()
               db.session.add(row)
               db.session.commit()
               db.session.close()
               flash('Record %s saved OK'%(Cou_Code,Cur_Code))
            except Exception as e:
               db.session.rollback()
               db.session.close()
               flash('ERROR saving record : %s'%(e))
            return redirect(url_for('.select_Countries_Currencies_query'))
        elif   form.submit_New.data:
            print('New Data Here...')
            db.session.close()
            row=country_currency()
            return redirect(url_for('.forms_Countries_Currencies'))

        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.forms_Countries_Currencies'))

    form.Cou_Code.data = row.Cou_Code
    form.Cur_Code.data = row.Cur_Code
    form.Cou_Cur_Comment.data = row.Cou_Cur_Comment
    return render_template('countries_currencies.html', form=form, row=row)

# =============================================================================

@main.route('/forms/Countries_Currencies_delete', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@admin_required
def forms_Countries_Currencies_delete():
    """ Delete record handling function for table Countries_Currencies """

    logger.debug('Enter: forms_Countries_Currencies_delete()')
    Cou_Code  =  request.args.get('Cou_Code',0,type=int)
    Cur_Code  =  request.args.get('Cur_Code',0,type=int)
    row =  country_currency.query.filter(country_currency.Cou_Code == Cou_Code,country_currency.Cur_Code == Cur_Code).first()
    if row is None:
        row=country_currency()
    session['data'] =  { 'Cou_Code':row.Cou_Code, 'Cur_Code':row.Cur_Code, 'Cou_Cur_Comment':row.Cou_Cur_Comment}
    form = frm_country_currency_delete()

    if form.validate_on_submit():
        if  form.submit_Delete.data:
            print('Delete Data Here...')
            print('Delete Data Here...')
            try:
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                flash('Record %s deleted OK'%(Cou_Code,Cur_Code))
            except exc.IntegrityError as e:
                db.session.rollback()
                flash('INTEGRITY ERROR: Are you sure there are no dependant records in other tables?')
                return redirect(url_for('.forms_Countries_Currencies_delete',Cou_Code=session['data']['Cou_Code'],Cur_Code=session['data']['Cur_Code']))

            return redirect(url_for('.select_Countries_Currencies_query'))
        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
            return redirect(url_for('.select_Countries_Currencies_query'))
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.select_Countries_Currencies_query'))


    return render_template('countries_currencies_delete.html',C=C, form=form, data=session.get('data'),row=row)

# =============================================================================

@main.route('/select/Countries_Currencies_Query', methods=['GET','POST'])
@login_required
@admin_required
def select_Countries_Currencies_query():
    """ Select rows handling function for table Countries_Currencies """

    logger.debug('Enter: select_Countries_Currencies_query()')
    field =  request.args.get('field',None,type=str)
    value =  request.args.get('value',0,type=str)
    page  =  request.args.get('page',1,type=int)

    if field is not None:
        if   field == 'Cou_Code':
            rows =  country_currency.query.filter_by(Cou_Code=value)\
               .join(country,country_currency.Cou_Code == country.Cou_Code).add_columns(country.Cou_Name)\
               .join(currency,country_currency.Cur_Code == currency.Cur_Code).add_columns(currency.Cur_Name)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Cur_Code':
            rows =  country_currency.query.filter_by(Cur_Code=value)\
               .join(country,country_currency.Cou_Code == country.Cou_Code).add_columns(country.Cou_Name)\
               .join(currency,country_currency.Cur_Code == currency.Cur_Code).add_columns(currency.Cur_Name)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Cou_Cur_Comment':
            rows =  country_currency.query.filter_by(Cou_Cur_Comment=value)\
               .join(country,country_currency.Cou_Code == country.Cou_Code).add_columns(country.Cou_Name)\
               .join(currency,country_currency.Cur_Code == currency.Cur_Code).add_columns(currency.Cur_Name)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
    else:
       rows =  country_currency.query\
               .join(country,country_currency.Cou_Code == country.Cou_Code).add_columns(country.Cou_Name)\
               .join(currency,country_currency.Cur_Code == currency.Cur_Code).add_columns(currency.Cur_Name)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)

    next_url = url_for('.select_Countries_Currencies_query', page=rows.next_num) \
        if rows.has_next else None
    prev_url = url_for('.select_Countries_Currencies_query', page=rows.prev_num) \
        if rows.has_prev else None

    return render_template('countries_currencies_All.html',C=C,rows=rows.items,next_url=next_url,prev_url=prev_url)
# =============================================================================

# =============================================================================

# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-11-30 16:47:18
# =============================================================================


@main.route('/forms/Countries', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@permission_required(Permission.MODIFY)
@admin_required
def forms_Countries():
    """ Form handling function for table Countries """

    logger.debug('Enter: forms_Countries()')
    Cou_Code  =  request.args.get('Cou_Code',0,type=int)
    row =  country.query.filter(country.Cou_Code == Cou_Code).first()
    if row is None:
        row=country()

    session['data'] =  { 'Cou_Code':row.Cou_Code, 'Cou_Name':row.Cou_Name, 'Cou_A3':row.Cou_A3, 'Cou_N':row.Cou_N}
    form = frm_country()

    if form.validate_on_submit():
        if     form.submit_Save.data:
            row.Cou_Code = form.Cou_Code.data
            row.Cou_Name = form.Cou_Name.data
            row.Cou_A3 = form.Cou_A3.data
            row.Cou_N = form.Cou_N.data
            try:
               db.session.close()
               db.session.add(row)
               db.session.commit()
               db.session.close()
               flash('Record %s saved OK'%(Cou_Code))
            except Exception as e:
               db.session.rollback()
               db.session.close()
               flash('ERROR saving record : %s'%(e))
            return redirect(url_for('.select_Countries_query'))
        elif   form.submit_New.data:
            print('New Data Here...')
            db.session.close()
            row=country()
            return redirect(url_for('.forms_Countries'))

        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.forms_Countries'))

    form.Cou_Code.data = row.Cou_Code
    form.Cou_Name.data = row.Cou_Name
    form.Cou_A3.data = row.Cou_A3
    form.Cou_N.data = row.Cou_N
    return render_template('countries.html', form=form, row=row)

# =============================================================================

@main.route('/forms/Countries_delete', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@admin_required
def forms_Countries_delete():
    """ Delete record handling function for table Countries """

    logger.debug('Enter: forms_Countries_delete()')
    Cou_Code  =  request.args.get('Cou_Code',0,type=int)
    row =  country.query.filter(country.Cou_Code == Cou_Code).first()
    if row is None:
        row=country()
    session['data'] =  { 'Cou_Code':row.Cou_Code, 'Cou_Name':row.Cou_Name, 'Cou_A3':row.Cou_A3, 'Cou_N':row.Cou_N}
    form = frm_country_delete()

    if form.validate_on_submit():
        if  form.submit_Delete.data:
            print('Delete Data Here...')
            print('Delete Data Here...')
            try:
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                flash('Record %s deleted OK'%(Cou_Code))
            except exc.IntegrityError as e:
                db.session.rollback()
                flash('INTEGRITY ERROR: Are you sure there are no dependant records in other tables?')
                return redirect(url_for('.forms_Countries_delete',Cou_Code=session['data']['Cou_Code']))

            return redirect(url_for('.select_Countries_query'))
        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
            return redirect(url_for('.select_Countries_query'))
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.select_Countries_query'))


    return render_template('countries_delete.html',C=C, form=form, data=session.get('data'),row=row)

# =============================================================================

@main.route('/select/Countries_Query', methods=['GET','POST'])
@login_required
@admin_required
def select_Countries_query():
    """ Select rows handling function for table Countries """

    logger.debug('Enter: select_Countries_query()')
    field =  request.args.get('field',None,type=str)
    value =  request.args.get('value',0,type=str)
    page  =  request.args.get('page',1,type=int)

    if field is not None:
        if   field == 'Cou_Code':
            rows =  country.query.filter_by(Cou_Code=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Cou_Name':
            rows =  country.query.filter_by(Cou_Name=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Cou_A3':
            rows =  country.query.filter_by(Cou_A3=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Cou_N':
            rows =  country.query.filter_by(Cou_N=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
    else:
       rows =  country.query\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)

    next_url = url_for('.select_Countries_query', page=rows.next_num) \
        if rows.has_next else None
    prev_url = url_for('.select_Countries_query', page=rows.prev_num) \
        if rows.has_prev else None

    return render_template('countries_All.html',C=C,rows=rows.items,next_url=next_url,prev_url=prev_url)
# =============================================================================

# =============================================================================

# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-11-30 16:47:18
# =============================================================================


@main.route('/forms/CU_Operations', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@permission_required(Permission.MODIFY)
@admin_required
def forms_CU_Operations():
    """ Form handling function for table CU_Operations """

    logger.debug('Enter: forms_CU_Operations()')
    CU_Operation  =  request.args.get('CU_Operation',0,type=int)
    row =  cu_operation.query.filter(cu_operation.CU_Operation == CU_Operation).first()
    if row is None:
        row=cu_operation()

    session['data'] =  { 'CU_Operation':row.CU_Operation, 'Value':row.Value, 'Is_Multiply':row.Is_Multiply, 'Factor':row.Factor}
    form = frm_cu_operation()

    if form.validate_on_submit():
        if     form.submit_Save.data:
            row.CU_Operation = form.CU_Operation.data
            row.Value = form.Value.data
            row.Is_Multiply = form.Is_Multiply.data
            row.Factor = form.Factor.data
            try:
               db.session.close()
               db.session.add(row)
               db.session.commit()
               db.session.close()
               flash('Record %s saved OK'%(CU_Operation))
            except Exception as e:
               db.session.rollback()
               db.session.close()
               flash('ERROR saving record : %s'%(e))
            return redirect(url_for('.select_CU_Operations_query'))
        elif   form.submit_New.data:
            print('New Data Here...')
            db.session.close()
            row=cu_operation()
            return redirect(url_for('.forms_CU_Operations'))

        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.forms_CU_Operations'))

    form.CU_Operation.data = row.CU_Operation
    form.Value.data = row.Value
    form.Is_Multiply.data = row.Is_Multiply
    form.Factor.data = row.Factor
    return render_template('cu_operations.html', form=form, row=row)

# =============================================================================

@main.route('/forms/CU_Operations_delete', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@admin_required
def forms_CU_Operations_delete():
    """ Delete record handling function for table CU_Operations """

    logger.debug('Enter: forms_CU_Operations_delete()')
    CU_Operation  =  request.args.get('CU_Operation',0,type=int)
    row =  cu_operation.query.filter(cu_operation.CU_Operation == CU_Operation).first()
    if row is None:
        row=cu_operation()
    session['data'] =  { 'CU_Operation':row.CU_Operation, 'Value':row.Value, 'Is_Multiply':row.Is_Multiply, 'Factor':row.Factor}
    form = frm_cu_operation_delete()

    if form.validate_on_submit():
        if  form.submit_Delete.data:
            print('Delete Data Here...')
            print('Delete Data Here...')
            try:
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                flash('Record %s deleted OK'%(CU_Operation))
            except exc.IntegrityError as e:
                db.session.rollback()
                flash('INTEGRITY ERROR: Are you sure there are no dependant records in other tables?')
                return redirect(url_for('.forms_CU_Operations_delete',CU_Operation=session['data']['CU_Operation']))

            return redirect(url_for('.select_CU_Operations_query'))
        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
            return redirect(url_for('.select_CU_Operations_query'))
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.select_CU_Operations_query'))


    return render_template('cu_operations_delete.html',C=C, form=form, data=session.get('data'),row=row)

# =============================================================================

@main.route('/select/CU_Operations_Query', methods=['GET','POST'])
@login_required
@admin_required
def select_CU_Operations_query():
    """ Select rows handling function for table CU_Operations """

    logger.debug('Enter: select_CU_Operations_query()')
    field =  request.args.get('field',None,type=str)
    value =  request.args.get('value',0,type=str)
    page  =  request.args.get('page',1,type=int)

    if field is not None:
        if   field == 'CU_Operation':
            rows =  cu_operation.query.filter_by(CU_Operation=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Value':
            rows =  cu_operation.query.filter_by(Value=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Is_Multiply':
            rows =  cu_operation.query.filter_by(Is_Multiply=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Factor':
            rows =  cu_operation.query.filter_by(Factor=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
    else:
       rows =  cu_operation.query\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)

    next_url = url_for('.select_CU_Operations_query', page=rows.next_num) \
        if rows.has_next else None
    prev_url = url_for('.select_CU_Operations_query', page=rows.prev_num) \
        if rows.has_prev else None

    return render_template('cu_operations_All.html',C=C,rows=rows.items,next_url=next_url,prev_url=prev_url)
# =============================================================================

# =============================================================================

# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-11-30 16:47:18
# =============================================================================


@main.route('/forms/Currencies', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@permission_required(Permission.MODIFY)
@admin_required
def forms_Currencies():
    """ Form handling function for table Currencies """

    logger.debug('Enter: forms_Currencies()')
    Cur_Code  =  request.args.get('Cur_Code',0,type=int)
    row =  currency.query.filter(currency.Cur_Code == Cur_Code).first()
    if row is None:
        row=currency()

    session['data'] =  { 'Cur_Code':row.Cur_Code, 'Cur_Name':row.Cur_Name, 'Cur_Id':row.Cur_Id, 'Cur_Comment':row.Cur_Comment}
    form = frm_currency()

    if form.validate_on_submit():
        if     form.submit_Save.data:
            row.Cur_Code = form.Cur_Code.data
            row.Cur_Name = form.Cur_Name.data
            row.Cur_Id = form.Cur_Id.data
            row.Cur_Comment = form.Cur_Comment.data
            try:
               db.session.close()
               db.session.add(row)
               db.session.commit()
               db.session.close()
               flash('Record %s saved OK'%(Cur_Code))
            except Exception as e:
               db.session.rollback()
               db.session.close()
               flash('ERROR saving record : %s'%(e))
            return redirect(url_for('.select_Currencies_query'))
        elif   form.submit_New.data:
            print('New Data Here...')
            db.session.close()
            row=currency()
            return redirect(url_for('.forms_Currencies'))

        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.forms_Currencies'))

    form.Cur_Code.data = row.Cur_Code
    form.Cur_Name.data = row.Cur_Name
    form.Cur_Id.data = row.Cur_Id
    form.Cur_Comment.data = row.Cur_Comment
    return render_template('currencies.html', form=form, row=row)

# =============================================================================

@main.route('/forms/Currencies_delete', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@admin_required
def forms_Currencies_delete():
    """ Delete record handling function for table Currencies """

    logger.debug('Enter: forms_Currencies_delete()')
    Cur_Code  =  request.args.get('Cur_Code',0,type=int)
    row =  currency.query.filter(currency.Cur_Code == Cur_Code).first()
    if row is None:
        row=currency()
    session['data'] =  { 'Cur_Code':row.Cur_Code, 'Cur_Name':row.Cur_Name, 'Cur_Id':row.Cur_Id, 'Cur_Comment':row.Cur_Comment}
    form = frm_currency_delete()

    if form.validate_on_submit():
        if  form.submit_Delete.data:
            print('Delete Data Here...')
            print('Delete Data Here...')
            try:
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                flash('Record %s deleted OK'%(Cur_Code))
            except exc.IntegrityError as e:
                db.session.rollback()
                flash('INTEGRITY ERROR: Are you sure there are no dependant records in other tables?')
                return redirect(url_for('.forms_Currencies_delete',Cur_Code=session['data']['Cur_Code']))

            return redirect(url_for('.select_Currencies_query'))
        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
            return redirect(url_for('.select_Currencies_query'))
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.select_Currencies_query'))


    return render_template('currencies_delete.html',C=C, form=form, data=session.get('data'),row=row)

# =============================================================================

@main.route('/select/Currencies_Query', methods=['GET','POST'])
@login_required
@admin_required
def select_Currencies_query():
    """ Select rows handling function for table Currencies """

    logger.debug('Enter: select_Currencies_query()')
    field =  request.args.get('field',None,type=str)
    value =  request.args.get('value',0,type=str)
    page  =  request.args.get('page',1,type=int)

    if field is not None:
        if   field == 'Cur_Code':
            rows =  currency.query.filter_by(Cur_Code=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Cur_Name':
            rows =  currency.query.filter_by(Cur_Name=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Cur_Id':
            rows =  currency.query.filter_by(Cur_Id=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Cur_Comment':
            rows =  currency.query.filter_by(Cur_Comment=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
    else:
       rows =  currency.query\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)

    next_url = url_for('.select_Currencies_query', page=rows.next_num) \
        if rows.has_next else None
    prev_url = url_for('.select_Currencies_query', page=rows.prev_num) \
        if rows.has_prev else None

    return render_template('currencies_All.html',C=C,rows=rows.items,next_url=next_url,prev_url=prev_url)
# =============================================================================

# =============================================================================

# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-11-30 16:47:18
# =============================================================================


@main.route('/forms/Customers', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@permission_required(Permission.MODIFY)
@admin_required
def forms_Customers():
    """ Form handling function for table Customers """

    logger.debug('Enter: forms_Customers()')
    Cus_Id  =  request.args.get('Cus_Id',0,type=int)
    row =  customer.query.filter(customer.Cus_Id == Cus_Id).first()
    if row is None:
        row=customer()

    session['data'] =  { 'Cus_Id':row.Cus_Id, 'Cus_Name':row.Cus_Name, 'CC_Id':row.CC_Id}
    form = frm_customer()

    if form.has_FKs:
        form.CC_Id.choices = db.session.query(cost_center.CC_Id,cost_center.CC_Description).order_by(cost_center.CC_Description).all()

    if form.validate_on_submit():
        if     form.submit_Save.data:
            row.Cus_Name = form.Cus_Name.data
            row.CC_Id = form.CC_Id.data
            try:
               db.session.close()
               db.session.add(row)
               db.session.commit()
               db.session.close()
               flash('Record %s saved OK'%(Cus_Id))
            except Exception as e:
               db.session.rollback()
               db.session.close()
               flash('ERROR saving record : %s'%(e))
            return redirect(url_for('.select_Customers_query'))
        elif   form.submit_New.data:
            print('New Data Here...')
            db.session.close()
            row=customer()
            pass
            pass
            return redirect(url_for('.forms_Customers',Cus_Id=row.Cus_Id))

        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.forms_Customers',Cus_Id=row.Cus_Id))

    form.Cus_Name.data = row.Cus_Name
    form.CC_Id.data = row.CC_Id
    return render_template('customers.html', form=form, row=row)

# =============================================================================

@main.route('/forms/Customers_delete', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@admin_required
def forms_Customers_delete():
    """ Delete record handling function for table Customers """

    logger.debug('Enter: forms_Customers_delete()')
    Cus_Id  =  request.args.get('Cus_Id',0,type=int)
    row =  customer.query.filter(customer.Cus_Id == Cus_Id).first()
    if row is None:
        row=customer()
    session['data'] =  { 'Cus_Id':row.Cus_Id, 'Cus_Name':row.Cus_Name, 'CC_Id':row.CC_Id}
    form = frm_customer_delete()

    if form.validate_on_submit():
        if  form.submit_Delete.data:
            print('Delete Data Here...')
            print('Delete Data Here...')
            try:
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                flash('Record %s deleted OK'%(Cus_Id))
            except exc.IntegrityError as e:
                db.session.rollback()
                flash('INTEGRITY ERROR: Are you sure there are no dependant records in other tables?')
                return redirect(url_for('.forms_Customers_delete',Cus_Id=session['data']['Cus_Id']))

            return redirect(url_for('.select_Customers_query'))
        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
            return redirect(url_for('.select_Customers_query'))
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.select_Customers_query'))


    return render_template('customers_delete.html',C=C, form=form, data=session.get('data'),row=row)

# =============================================================================

@main.route('/select/Customers_Query', methods=['GET','POST'])
@login_required
@admin_required
def select_Customers_query():
    """ Select rows handling function for table Customers """

    logger.debug('Enter: select_Customers_query()')
    field =  request.args.get('field',None,type=str)
    value =  request.args.get('value',0,type=str)
    page  =  request.args.get('page',1,type=int)

    if field is not None:
        if   field == 'Cus_Id':
            rows =  customer.query.filter_by(Cus_Id=value)\
               .join(cost_center,customer.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Cus_Name':
            rows =  customer.query.filter_by(Cus_Name=value)\
               .join(cost_center,customer.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CC_Id':
            rows =  customer.query.filter_by(CC_Id=value)\
               .join(cost_center,customer.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
    else:
       rows =  customer.query\
               .join(cost_center,customer.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)

    next_url = url_for('.select_Customers_query', page=rows.next_num) \
        if rows.has_next else None
    prev_url = url_for('.select_Customers_query', page=rows.prev_num) \
        if rows.has_prev else None

    return render_template('customers_All.html',C=C,rows=rows.items,next_url=next_url,prev_url=prev_url)
# =============================================================================

# =============================================================================

# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-11-30 16:47:18
# =============================================================================


@main.route('/forms/CU_Types', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@permission_required(Permission.MODIFY)
@admin_required
def forms_CU_Types():
    """ Form handling function for table CU_Types """

    logger.debug('Enter: forms_CU_Types()')
    Typ_Code  =  request.args.get('Typ_Code',0,type=int)
    row =  cu_type.query.filter(cu_type.Typ_Code == Typ_Code).first()
    if row is None:
        row=cu_type()

    session['data'] =  { 'Typ_Code':row.Typ_Code, 'Typ_Description':row.Typ_Description}
    form = frm_cu_type()

    if form.validate_on_submit():
        if     form.submit_Save.data:
            row.Typ_Code = form.Typ_Code.data
            row.Typ_Description = form.Typ_Description.data
            try:
               db.session.close()
               db.session.add(row)
               db.session.commit()
               db.session.close()
               flash('Record %s saved OK'%(Typ_Code))
            except Exception as e:
               db.session.rollback()
               db.session.close()
               flash('ERROR saving record : %s'%(e))
            return redirect(url_for('.select_CU_Types_query'))
        elif   form.submit_New.data:
            print('New Data Here...')
            db.session.close()
            row=cu_type()
            return redirect(url_for('.forms_CU_Types'))

        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.forms_CU_Types'))

    form.Typ_Code.data = row.Typ_Code
    form.Typ_Description.data = row.Typ_Description
    return render_template('cu_types.html', form=form, row=row)

# =============================================================================

@main.route('/forms/CU_Types_delete', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@admin_required
def forms_CU_Types_delete():
    """ Delete record handling function for table CU_Types """

    logger.debug('Enter: forms_CU_Types_delete()')
    Typ_Code  =  request.args.get('Typ_Code',0,type=int)
    row =  cu_type.query.filter(cu_type.Typ_Code == Typ_Code).first()
    if row is None:
        row=cu_type()
    session['data'] =  { 'Typ_Code':row.Typ_Code, 'Typ_Description':row.Typ_Description}
    form = frm_cu_type_delete()

    if form.validate_on_submit():
        if  form.submit_Delete.data:
            print('Delete Data Here...')
            print('Delete Data Here...')
            try:
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                flash('Record %s deleted OK'%(Typ_Code))
            except exc.IntegrityError as e:
                db.session.rollback()
                flash('INTEGRITY ERROR: Are you sure there are no dependant records in other tables?')
                return redirect(url_for('.forms_CU_Types_delete',Typ_Code=session['data']['Typ_Code']))

            return redirect(url_for('.select_CU_Types_query'))
        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
            return redirect(url_for('.select_CU_Types_query'))
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.select_CU_Types_query'))


    return render_template('cu_types_delete.html',C=C, form=form, data=session.get('data'),row=row)

# =============================================================================

@main.route('/select/CU_Types_Query', methods=['GET','POST'])
@login_required
@admin_required
def select_CU_Types_query():
    """ Select rows handling function for table CU_Types """

    logger.debug('Enter: select_CU_Types_query()')
    field =  request.args.get('field',None,type=str)
    value =  request.args.get('value',0,type=str)
    page  =  request.args.get('page',1,type=int)

    if field is not None:
        if   field == 'Typ_Code':
            rows =  cu_type.query.filter_by(Typ_Code=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Typ_Description':
            rows =  cu_type.query.filter_by(Typ_Description=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
    else:
       rows =  cu_type.query\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)

    next_url = url_for('.select_CU_Types_query', page=rows.next_num) \
        if rows.has_next else None
    prev_url = url_for('.select_CU_Types_query', page=rows.prev_num) \
        if rows.has_prev else None

    return render_template('cu_types_All.html',C=C,rows=rows.items,next_url=next_url,prev_url=prev_url)
# =============================================================================

# =============================================================================

# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-11-30 16:47:18
# =============================================================================


@main.route('/forms/Dev_Forms', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@permission_required(Permission.MODIFY)
@admin_required
def forms_Dev_Forms():
    """ Form handling function for table Dev_Forms """

    logger.debug('Enter: forms_Dev_Forms()')
    Id  =  request.args.get('Id',0,type=int)
    row =  dev_form.query.filter(dev_form.Id == Id).first()
    if row is None:
        row=dev_form()

    session['data'] =  { 'Id':row.Id, 'Table':row.Table, 'Field':row.Field, 'Type':row.Type, 'Null':row.Null, 'Key':row.Key, 'Default':row.Default, 'Extra':row.Extra, 'Foreign_Key':row.Foreign_Key, 'Referenced_Table':row.Referenced_Table, 'Foreign_Field':row.Foreign_Field, 'Foreign_Value':row.Foreign_Value, 'Length':row.Length, 'Validation':row.Validation, 'Validation_Type':row.Validation_Type, 'Validation_String':row.Validation_String, 'Caption_String':row.Caption_String, 'Field_Order':row.Field_Order, 'Field_Format':row.Field_Format, 'Form_Editable':row.Form_Editable}
    form = frm_dev_form()

    if form.validate_on_submit():
        if     form.submit_Save.data:
            row.Table = form.Table.data
            row.Field = form.Field.data
            row.Type = form.Type.data
            row.Null = form.Null.data
            row.Key = form.Key.data
            row.Default = form.Default.data
            row.Extra = form.Extra.data
            row.Foreign_Key = form.Foreign_Key.data
            row.Referenced_Table = form.Referenced_Table.data
            row.Foreign_Field = form.Foreign_Field.data
            row.Foreign_Value = form.Foreign_Value.data
            row.Length = form.Length.data
            row.Validation = form.Validation.data
            row.Validation_Type = form.Validation_Type.data
            row.Validation_String = form.Validation_String.data
            row.Caption_String = form.Caption_String.data
            row.Field_Order = form.Field_Order.data
            row.Field_Format = form.Field_Format.data
            row.Form_Editable = form.Form_Editable.data
            try:
               db.session.close()
               db.session.add(row)
               db.session.commit()
               db.session.close()
               flash('Record %s saved OK'%(Id))
            except Exception as e:
               db.session.rollback()
               db.session.close()
               flash('ERROR saving record : %s'%(e))
            return redirect(url_for('.select_Dev_Forms_query'))
        elif   form.submit_New.data:
            print('New Data Here...')
            db.session.close()
            row=dev_form()
            pass
            pass
            pass
            pass
            pass
            pass
            pass
            pass
            pass
            pass
            pass
            pass
            pass
            pass
            pass
            pass
            pass
            pass
            pass
            return redirect(url_for('.forms_Dev_Forms',Id=row.Id))

        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.forms_Dev_Forms',Id=row.Id))

    form.Table.data = row.Table
    form.Field.data = row.Field
    form.Type.data = row.Type
    form.Null.data = row.Null
    form.Key.data = row.Key
    form.Default.data = row.Default
    form.Extra.data = row.Extra
    form.Foreign_Key.data = row.Foreign_Key
    form.Referenced_Table.data = row.Referenced_Table
    form.Foreign_Field.data = row.Foreign_Field
    form.Foreign_Value.data = row.Foreign_Value
    form.Length.data = row.Length
    form.Validation.data = row.Validation
    form.Validation_Type.data = row.Validation_Type
    form.Validation_String.data = row.Validation_String
    form.Caption_String.data = row.Caption_String
    form.Field_Order.data = row.Field_Order
    form.Field_Format.data = row.Field_Format
    form.Form_Editable.data = row.Form_Editable
    return render_template('dev_forms.html', form=form, row=row)

# =============================================================================

@main.route('/forms/Dev_Forms_delete', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@admin_required
def forms_Dev_Forms_delete():
    """ Delete record handling function for table Dev_Forms """

    logger.debug('Enter: forms_Dev_Forms_delete()')
    Id  =  request.args.get('Id',0,type=int)
    row =  dev_form.query.filter(dev_form.Id == Id).first()
    if row is None:
        row=dev_form()
    session['data'] =  { 'Id':row.Id, 'Table':row.Table, 'Field':row.Field, 'Type':row.Type, 'Null':row.Null, 'Key':row.Key, 'Default':row.Default, 'Extra':row.Extra, 'Foreign_Key':row.Foreign_Key, 'Referenced_Table':row.Referenced_Table, 'Foreign_Field':row.Foreign_Field, 'Foreign_Value':row.Foreign_Value, 'Length':row.Length, 'Validation':row.Validation, 'Validation_Type':row.Validation_Type, 'Validation_String':row.Validation_String, 'Caption_String':row.Caption_String, 'Field_Order':row.Field_Order, 'Field_Format':row.Field_Format, 'Form_Editable':row.Form_Editable}
    form = frm_dev_form_delete()

    if form.validate_on_submit():
        if  form.submit_Delete.data:
            print('Delete Data Here...')
            print('Delete Data Here...')
            try:
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                flash('Record %s deleted OK'%(Id))
            except exc.IntegrityError as e:
                db.session.rollback()
                flash('INTEGRITY ERROR: Are you sure there are no dependant records in other tables?')
                return redirect(url_for('.forms_Dev_Forms_delete',Id=session['data']['Id']))

            return redirect(url_for('.select_Dev_Forms_query'))
        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
            return redirect(url_for('.select_Dev_Forms_query'))
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.select_Dev_Forms_query'))


    return render_template('dev_forms_delete.html',C=C, form=form, data=session.get('data'),row=row)

# =============================================================================

@main.route('/select/Dev_Forms_Query', methods=['GET','POST'])
@login_required
@admin_required
def select_Dev_Forms_query():
    """ Select rows handling function for table Dev_Forms """

    logger.debug('Enter: select_Dev_Forms_query()')
    field =  request.args.get('field',None,type=str)
    value =  request.args.get('value',0,type=str)
    page  =  request.args.get('page',1,type=int)

    if field is not None:
        if   field == 'Id':
            rows =  dev_form.query.filter_by(Id=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Table':
            rows =  dev_form.query.filter_by(Table=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Field':
            rows =  dev_form.query.filter_by(Field=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Type':
            rows =  dev_form.query.filter_by(Type=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Null':
            rows =  dev_form.query.filter_by(Null=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Key':
            rows =  dev_form.query.filter_by(Key=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Default':
            rows =  dev_form.query.filter_by(Default=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Extra':
            rows =  dev_form.query.filter_by(Extra=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Foreign_Key':
            rows =  dev_form.query.filter_by(Foreign_Key=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Referenced_Table':
            rows =  dev_form.query.filter_by(Referenced_Table=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Foreign_Field':
            rows =  dev_form.query.filter_by(Foreign_Field=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Foreign_Value':
            rows =  dev_form.query.filter_by(Foreign_Value=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Length':
            rows =  dev_form.query.filter_by(Length=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Validation':
            rows =  dev_form.query.filter_by(Validation=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Validation_Type':
            rows =  dev_form.query.filter_by(Validation_Type=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Validation_String':
            rows =  dev_form.query.filter_by(Validation_String=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Caption_String':
            rows =  dev_form.query.filter_by(Caption_String=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Field_Order':
            rows =  dev_form.query.filter_by(Field_Order=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Field_Format':
            rows =  dev_form.query.filter_by(Field_Format=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Form_Editable':
            rows =  dev_form.query.filter_by(Form_Editable=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
    else:
       rows =  dev_form.query\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)

    next_url = url_for('.select_Dev_Forms_query', page=rows.next_num) \
        if rows.has_next else None
    prev_url = url_for('.select_Dev_Forms_query', page=rows.prev_num) \
        if rows.has_prev else None

    return render_template('dev_forms_All.html',C=C,rows=rows.items,next_url=next_url,prev_url=prev_url)
# =============================================================================

# =============================================================================

# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-11-30 16:47:18
# =============================================================================


@main.route('/forms/Dev_Tables', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@permission_required(Permission.MODIFY)
@admin_required
def forms_Dev_Tables():
    """ Form handling function for table Dev_Tables """

    logger.debug('Enter: forms_Dev_Tables()')
    Id  =  request.args.get('Id',0,type=int)
    row =  dev_table.query.filter(dev_table.Id == Id).first()
    if row is None:
        row=dev_table()

    session['data'] =  { 'Id':row.Id, 'Name':row.Name, 'Caption':row.Caption, 'Entity':row.Entity, 'Class_Name':row.Class_Name, 'Child_Table':row.Child_Table, 'Parent_Table':row.Parent_Table, 'Use_Pagination':row.Use_Pagination, 'Use_Children_Pagination':row.Use_Children_Pagination, 'Generate_Form_One':row.Generate_Form_One, 'Generate_Form_All':row.Generate_Form_All, 'Generate_Form_Filter':row.Generate_Form_Filter, 'Generate_Children':row.Generate_Children, 'Generate_Foreign_Fields':row.Generate_Foreign_Fields, 'Permission_View':row.Permission_View, 'Permission_Delete':row.Permission_Delete, 'Permission_Modify':row.Permission_Modify, 'Permission_Report':row.Permission_Report, 'Permission_Export':row.Permission_Export, 'Permission_View_Private':row.Permission_View_Private, 'Permission_Modify_Private':row.Permission_Modify_Private, 'Permission_Administer':row.Permission_Administer}
    form = frm_dev_table()

    if form.validate_on_submit():
        if     form.submit_Save.data:
            row.Name = form.Name.data
            row.Caption = form.Caption.data
            row.Entity = form.Entity.data
            row.Class_Name = form.Class_Name.data
            row.Child_Table = form.Child_Table.data
            row.Parent_Table = form.Parent_Table.data
            row.Use_Pagination = form.Use_Pagination.data
            row.Use_Children_Pagination = form.Use_Children_Pagination.data
            row.Generate_Form_One = form.Generate_Form_One.data
            row.Generate_Form_All = form.Generate_Form_All.data
            row.Generate_Form_Filter = form.Generate_Form_Filter.data
            row.Generate_Children = form.Generate_Children.data
            row.Generate_Foreign_Fields = form.Generate_Foreign_Fields.data
            row.Permission_View = form.Permission_View.data
            row.Permission_Delete = form.Permission_Delete.data
            row.Permission_Modify = form.Permission_Modify.data
            row.Permission_Report = form.Permission_Report.data
            row.Permission_Export = form.Permission_Export.data
            row.Permission_View_Private = form.Permission_View_Private.data
            row.Permission_Modify_Private = form.Permission_Modify_Private.data
            row.Permission_Administer = form.Permission_Administer.data
            try:
               db.session.close()
               db.session.add(row)
               db.session.commit()
               db.session.close()
               flash('Record %s saved OK'%(Id))
            except Exception as e:
               db.session.rollback()
               db.session.close()
               flash('ERROR saving record : %s'%(e))
            return redirect(url_for('.select_Dev_Tables_query'))
        elif   form.submit_New.data:
            print('New Data Here...')
            db.session.close()
            row=dev_table()
            pass
            pass
            pass
            pass
            pass
            pass
            pass
            pass
            pass
            pass
            pass
            pass
            pass
            pass
            pass
            pass
            pass
            pass
            pass
            pass
            pass
            return redirect(url_for('.forms_Dev_Tables',Id=row.Id))

        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.forms_Dev_Tables',Id=row.Id))

    form.Name.data = row.Name
    form.Caption.data = row.Caption
    form.Entity.data = row.Entity
    form.Class_Name.data = row.Class_Name
    form.Child_Table.data = row.Child_Table
    form.Parent_Table.data = row.Parent_Table
    form.Use_Pagination.data = row.Use_Pagination
    form.Use_Children_Pagination.data = row.Use_Children_Pagination
    form.Generate_Form_One.data = row.Generate_Form_One
    form.Generate_Form_All.data = row.Generate_Form_All
    form.Generate_Form_Filter.data = row.Generate_Form_Filter
    form.Generate_Children.data = row.Generate_Children
    form.Generate_Foreign_Fields.data = row.Generate_Foreign_Fields
    form.Permission_View.data = row.Permission_View
    form.Permission_Delete.data = row.Permission_Delete
    form.Permission_Modify.data = row.Permission_Modify
    form.Permission_Report.data = row.Permission_Report
    form.Permission_Export.data = row.Permission_Export
    form.Permission_View_Private.data = row.Permission_View_Private
    form.Permission_Modify_Private.data = row.Permission_Modify_Private
    form.Permission_Administer.data = row.Permission_Administer
    return render_template('dev_tables.html', form=form, row=row)

# =============================================================================

@main.route('/forms/Dev_Tables_delete', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@admin_required
def forms_Dev_Tables_delete():
    """ Delete record handling function for table Dev_Tables """

    logger.debug('Enter: forms_Dev_Tables_delete()')
    Id  =  request.args.get('Id',0,type=int)
    row =  dev_table.query.filter(dev_table.Id == Id).first()
    if row is None:
        row=dev_table()
    session['data'] =  { 'Id':row.Id, 'Name':row.Name, 'Caption':row.Caption, 'Entity':row.Entity, 'Class_Name':row.Class_Name, 'Child_Table':row.Child_Table, 'Parent_Table':row.Parent_Table, 'Use_Pagination':row.Use_Pagination, 'Use_Children_Pagination':row.Use_Children_Pagination, 'Generate_Form_One':row.Generate_Form_One, 'Generate_Form_All':row.Generate_Form_All, 'Generate_Form_Filter':row.Generate_Form_Filter, 'Generate_Children':row.Generate_Children, 'Generate_Foreign_Fields':row.Generate_Foreign_Fields, 'Permission_View':row.Permission_View, 'Permission_Delete':row.Permission_Delete, 'Permission_Modify':row.Permission_Modify, 'Permission_Report':row.Permission_Report, 'Permission_Export':row.Permission_Export, 'Permission_View_Private':row.Permission_View_Private, 'Permission_Modify_Private':row.Permission_Modify_Private, 'Permission_Administer':row.Permission_Administer}
    form = frm_dev_table_delete()

    if form.validate_on_submit():
        if  form.submit_Delete.data:
            print('Delete Data Here...')
            print('Delete Data Here...')
            try:
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                flash('Record %s deleted OK'%(Id))
            except exc.IntegrityError as e:
                db.session.rollback()
                flash('INTEGRITY ERROR: Are you sure there are no dependant records in other tables?')
                return redirect(url_for('.forms_Dev_Tables_delete',Id=session['data']['Id']))

            return redirect(url_for('.select_Dev_Tables_query'))
        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
            return redirect(url_for('.select_Dev_Tables_query'))
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.select_Dev_Tables_query'))


    return render_template('dev_tables_delete.html',C=C, form=form, data=session.get('data'),row=row)

# =============================================================================

@main.route('/select/Dev_Tables_Query', methods=['GET','POST'])
@login_required
@admin_required
def select_Dev_Tables_query():
    """ Select rows handling function for table Dev_Tables """

    logger.debug('Enter: select_Dev_Tables_query()')
    field =  request.args.get('field',None,type=str)
    value =  request.args.get('value',0,type=str)
    page  =  request.args.get('page',1,type=int)

    if field is not None:
        if   field == 'Id':
            rows =  dev_table.query.filter_by(Id=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Name':
            rows =  dev_table.query.filter_by(Name=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Caption':
            rows =  dev_table.query.filter_by(Caption=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Entity':
            rows =  dev_table.query.filter_by(Entity=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Class_Name':
            rows =  dev_table.query.filter_by(Class_Name=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Child_Table':
            rows =  dev_table.query.filter_by(Child_Table=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Parent_Table':
            rows =  dev_table.query.filter_by(Parent_Table=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Use_Pagination':
            rows =  dev_table.query.filter_by(Use_Pagination=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Use_Children_Pagination':
            rows =  dev_table.query.filter_by(Use_Children_Pagination=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Generate_Form_One':
            rows =  dev_table.query.filter_by(Generate_Form_One=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Generate_Form_All':
            rows =  dev_table.query.filter_by(Generate_Form_All=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Generate_Form_Filter':
            rows =  dev_table.query.filter_by(Generate_Form_Filter=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Generate_Children':
            rows =  dev_table.query.filter_by(Generate_Children=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Generate_Foreign_Fields':
            rows =  dev_table.query.filter_by(Generate_Foreign_Fields=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Permission_View':
            rows =  dev_table.query.filter_by(Permission_View=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Permission_Delete':
            rows =  dev_table.query.filter_by(Permission_Delete=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Permission_Modify':
            rows =  dev_table.query.filter_by(Permission_Modify=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Permission_Report':
            rows =  dev_table.query.filter_by(Permission_Report=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Permission_Export':
            rows =  dev_table.query.filter_by(Permission_Export=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Permission_View_Private':
            rows =  dev_table.query.filter_by(Permission_View_Private=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Permission_Modify_Private':
            rows =  dev_table.query.filter_by(Permission_Modify_Private=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Permission_Administer':
            rows =  dev_table.query.filter_by(Permission_Administer=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
    else:
       rows =  dev_table.query\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)

    next_url = url_for('.select_Dev_Tables_query', page=rows.next_num) \
        if rows.has_next else None
    prev_url = url_for('.select_Dev_Tables_query', page=rows.prev_num) \
        if rows.has_prev else None

    return render_template('dev_tables_All.html',C=C,rows=rows.items,next_url=next_url,prev_url=prev_url)
# =============================================================================

# =============================================================================

# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-11-30 16:47:18
# =============================================================================


@main.route('/forms/Exchange_Rates', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@permission_required(Permission.MODIFY)
@admin_required
def forms_Exchange_Rates():
    """ Form handling function for table Exchange_Rates """

    logger.debug('Enter: forms_Exchange_Rates()')
    ER_Id  =  request.args.get('ER_Id',0,type=int)
    row =  exchange_rate.query.filter(exchange_rate.ER_Id == ER_Id).first()
    if row is None:
        row=exchange_rate()

    session['data'] =  { 'ER_Id':row.ER_Id, 'Cur_Code':row.Cur_Code, 'ER_Factor':row.ER_Factor, 'ER_Date':row.ER_Date}
    form = frm_exchange_rate()

    if form.has_FKs:
        form.Cur_Code.choices = db.session.query(currency.Cur_Code,currency.Cur_Name).order_by(currency.Cur_Name).all()

    if form.validate_on_submit():
        if     form.submit_Save.data:
            row.Cur_Code = form.Cur_Code.data
            row.ER_Factor = form.ER_Factor.data
            row.ER_Date = form.ER_Date.data
            try:
               db.session.close()
               db.session.add(row)
               db.session.commit()
               db.session.close()
               flash('Record %s saved OK'%(ER_Id))
            except Exception as e:
               db.session.rollback()
               db.session.close()
               flash('ERROR saving record : %s'%(e))
            return redirect(url_for('.select_Exchange_Rates_query'))
        elif   form.submit_New.data:
            print('New Data Here...')
            db.session.close()
            row=exchange_rate()
            pass
            pass
            pass
            return redirect(url_for('.forms_Exchange_Rates',ER_Id=row.ER_Id))

        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.forms_Exchange_Rates',ER_Id=row.ER_Id))

    form.Cur_Code.data = row.Cur_Code
    form.ER_Factor.data = row.ER_Factor
    form.ER_Date.data = row.ER_Date
    return render_template('exchange_rates.html', form=form, row=row)

# =============================================================================

@main.route('/forms/Exchange_Rates_delete', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@admin_required
def forms_Exchange_Rates_delete():
    """ Delete record handling function for table Exchange_Rates """

    logger.debug('Enter: forms_Exchange_Rates_delete()')
    ER_Id  =  request.args.get('ER_Id',0,type=int)
    row =  exchange_rate.query.filter(exchange_rate.ER_Id == ER_Id).first()
    if row is None:
        row=exchange_rate()
    session['data'] =  { 'ER_Id':row.ER_Id, 'Cur_Code':row.Cur_Code, 'ER_Factor':row.ER_Factor, 'ER_Date':row.ER_Date}
    form = frm_exchange_rate_delete()

    if form.validate_on_submit():
        if  form.submit_Delete.data:
            print('Delete Data Here...')
            print('Delete Data Here...')
            try:
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                flash('Record %s deleted OK'%(ER_Id))
            except exc.IntegrityError as e:
                db.session.rollback()
                flash('INTEGRITY ERROR: Are you sure there are no dependant records in other tables?')
                return redirect(url_for('.forms_Exchange_Rates_delete',ER_Id=session['data']['ER_Id']))

            return redirect(url_for('.select_Exchange_Rates_query'))
        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
            return redirect(url_for('.select_Exchange_Rates_query'))
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.select_Exchange_Rates_query'))


    return render_template('exchange_rates_delete.html',C=C, form=form, data=session.get('data'),row=row)

# =============================================================================

@main.route('/select/Exchange_Rates_Query', methods=['GET','POST'])
@login_required
@admin_required
def select_Exchange_Rates_query():
    """ Select rows handling function for table Exchange_Rates """

    logger.debug('Enter: select_Exchange_Rates_query()')
    field =  request.args.get('field',None,type=str)
    value =  request.args.get('value',0,type=str)
    page  =  request.args.get('page',1,type=int)

    if field is not None:
        if   field == 'ER_Id':
            rows =  exchange_rate.query.filter_by(ER_Id=value)\
               .join(currency,exchange_rate.Cur_Code == currency.Cur_Code).add_columns(currency.Cur_Name)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Cur_Code':
            rows =  exchange_rate.query.filter_by(Cur_Code=value)\
               .join(currency,exchange_rate.Cur_Code == currency.Cur_Code).add_columns(currency.Cur_Name)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'ER_Factor':
            rows =  exchange_rate.query.filter_by(ER_Factor=value)\
               .join(currency,exchange_rate.Cur_Code == currency.Cur_Code).add_columns(currency.Cur_Name)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'ER_Date':
            rows =  exchange_rate.query.filter_by(ER_Date=value)\
               .join(currency,exchange_rate.Cur_Code == currency.Cur_Code).add_columns(currency.Cur_Name)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
    else:
       rows =  exchange_rate.query\
               .join(currency,exchange_rate.Cur_Code == currency.Cur_Code).add_columns(currency.Cur_Name)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)

    next_url = url_for('.select_Exchange_Rates_query', page=rows.next_num) \
        if rows.has_next else None
    prev_url = url_for('.select_Exchange_Rates_query', page=rows.prev_num) \
        if rows.has_prev else None

    return render_template('exchange_rates_All.html',C=C,rows=rows.items,next_url=next_url,prev_url=prev_url)
# =============================================================================

# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-11-03 21:56:29
# =============================================================================
@main.route('/forms/Lists/<Type>&<Value>&<Caption>', methods=['GET', 'POST'])
def forms_Lists(Type,Value,Caption):
    logger.debug('Enter: forms_Lists(%s,%s,%s,)'%(Type,Value,Caption))
    lists =  Lists()
    row =  lists.queryone(Type,Value,Caption)
    if row is not None:
        session['data'] =  { 'Type':row.Type, 'Value':row.Value, 'Caption':row.Caption}
    else:
        session['data'] =  { 'Type':None, 'Value':None, 'Caption':None}
    form = frm_Lists()

    if form.has_FKs:
        form.set_FK_list()

        Session=sessionmaker(bind=C.db)
        sess=Session()

    if form.validate_on_submit():
        session['data']['Type'] = form.Type.data
        session['data']['Value'] = form.Value.data
        session['data']['Caption'] = form.Caption.data
        return redirect(url_for('forms_Lists',Type=session['data']['Type'],Value=session['data']['Value'],Caption=session['data']['Caption']))

    form.Type.data = session['data']['Type']
    form.Value.data = session['data']['Value']
    form.Caption.data = session['data']['Caption']

    return render_template('Lists.html',C=C, form=form, data=session.get('data'),row=row)

@main.route('/select/Lists', methods=['GET'])
def select_Lists():
    logger.debug('Enter: select_Lists()')
    lists =  Lists()
    result =  lists.queryall()
    rows = []
    for r in result:
	    row = object_as_dict(r)
	    rows.append(row)
    return render_template('Lists_All.html',C=C,rows=rows)
# =============================================================================
# =============================================================================

# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-11-30 16:47:18
# =============================================================================


@main.route('/forms/Measure_Units', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@permission_required(Permission.MODIFY)
@admin_required
def forms_Measure_Units():
    """ Form handling function for table Measure_Units """

    logger.debug('Enter: forms_Measure_Units()')
    MU_Code  =  request.args.get('MU_Code',0,type=int)
    row =  measure_unit.query.filter(measure_unit.MU_Code == MU_Code).first()
    if row is None:
        row=measure_unit()

    session['data'] =  { 'MU_Code':row.MU_Code, 'MU_Description':row.MU_Description}
    form = frm_measure_unit()

    if form.validate_on_submit():
        if     form.submit_Save.data:
            row.MU_Code = form.MU_Code.data
            row.MU_Description = form.MU_Description.data
            try:
               db.session.close()
               db.session.add(row)
               db.session.commit()
               db.session.close()
               flash('Record %s saved OK'%(MU_Code))
            except Exception as e:
               db.session.rollback()
               db.session.close()
               flash('ERROR saving record : %s'%(e))
            return redirect(url_for('.select_Measure_Units_query'))
        elif   form.submit_New.data:
            print('New Data Here...')
            db.session.close()
            row=measure_unit()
            return redirect(url_for('.forms_Measure_Units'))

        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.forms_Measure_Units'))

    form.MU_Code.data = row.MU_Code
    form.MU_Description.data = row.MU_Description
    return render_template('measure_units.html', form=form, row=row)

# =============================================================================

@main.route('/forms/Measure_Units_delete', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@admin_required
def forms_Measure_Units_delete():
    """ Delete record handling function for table Measure_Units """

    logger.debug('Enter: forms_Measure_Units_delete()')
    MU_Code  =  request.args.get('MU_Code',0,type=int)
    row =  measure_unit.query.filter(measure_unit.MU_Code == MU_Code).first()
    if row is None:
        row=measure_unit()
    session['data'] =  { 'MU_Code':row.MU_Code, 'MU_Description':row.MU_Description}
    form = frm_measure_unit_delete()

    if form.validate_on_submit():
        if  form.submit_Delete.data:
            print('Delete Data Here...')
            print('Delete Data Here...')
            try:
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                flash('Record %s deleted OK'%(MU_Code))
            except exc.IntegrityError as e:
                db.session.rollback()
                flash('INTEGRITY ERROR: Are you sure there are no dependant records in other tables?')
                return redirect(url_for('.forms_Measure_Units_delete',MU_Code=session['data']['MU_Code']))

            return redirect(url_for('.select_Measure_Units_query'))
        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
            return redirect(url_for('.select_Measure_Units_query'))
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.select_Measure_Units_query'))


    return render_template('measure_units_delete.html',C=C, form=form, data=session.get('data'),row=row)

# =============================================================================

@main.route('/select/Measure_Units_Query', methods=['GET','POST'])
@login_required
@admin_required
def select_Measure_Units_query():
    """ Select rows handling function for table Measure_Units """

    logger.debug('Enter: select_Measure_Units_query()')
    field =  request.args.get('field',None,type=str)
    value =  request.args.get('value',0,type=str)
    page  =  request.args.get('page',1,type=int)

    if field is not None:
        if   field == 'MU_Code':
            rows =  measure_unit.query.filter_by(MU_Code=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'MU_Description':
            rows =  measure_unit.query.filter_by(MU_Description=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
    else:
       rows =  measure_unit.query\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)

    next_url = url_for('.select_Measure_Units_query', page=rows.next_num) \
        if rows.has_next else None
    prev_url = url_for('.select_Measure_Units_query', page=rows.prev_num) \
        if rows.has_prev else None

    return render_template('measure_units_All.html',C=C,rows=rows.items,next_url=next_url,prev_url=prev_url)
# =============================================================================

# =============================================================================

# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-11-30 16:47:18
# =============================================================================


@main.route('/forms/Platforms', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@permission_required(Permission.MODIFY)
@admin_required
def forms_Platforms():
    """ Form handling function for table Platforms """

    logger.debug('Enter: forms_Platforms()')
    Pla_Id  =  request.args.get('Pla_Id',0,type=int)
    row =  platform.query.filter(platform.Pla_Id == Pla_Id).first()
    if row is None:
        row=platform()

    session['data'] =  { 'Pla_Id':row.Pla_Id, 'Pla_Name':row.Pla_Name, 'Pla_Host':row.Pla_Host, 'Pla_Port':row.Pla_Port, 'Pla_User':row.Pla_User, 'Pla_Password':row.Pla_Password}
    form = frm_platform()

    if form.validate_on_submit():
        if     form.submit_Save.data:
            row.Pla_Name = form.Pla_Name.data
            row.Pla_Host = form.Pla_Host.data
            row.Pla_Port = form.Pla_Port.data
            row.Pla_User = form.Pla_User.data
            row.Pla_Password = form.Pla_Password.data
            try:
               db.session.close()
               db.session.add(row)
               db.session.commit()
               db.session.close()
               flash('Record %s saved OK'%(Pla_Id))
            except Exception as e:
               db.session.rollback()
               db.session.close()
               flash('ERROR saving record : %s'%(e))
            return redirect(url_for('.select_Platforms_query'))
        elif   form.submit_New.data:
            print('New Data Here...')
            db.session.close()
            row=platform()
            pass
            pass
            pass
            pass
            pass
            return redirect(url_for('.forms_Platforms',Pla_Id=row.Pla_Id))

        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.forms_Platforms',Pla_Id=row.Pla_Id))

    form.Pla_Name.data = row.Pla_Name
    form.Pla_Host.data = row.Pla_Host
    form.Pla_Port.data = row.Pla_Port
    form.Pla_User.data = row.Pla_User
    form.Pla_Password.data = row.Pla_Password
    return render_template('platforms.html', form=form, row=row)

# =============================================================================

@main.route('/forms/Platforms_delete', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@admin_required
def forms_Platforms_delete():
    """ Delete record handling function for table Platforms """

    logger.debug('Enter: forms_Platforms_delete()')
    Pla_Id  =  request.args.get('Pla_Id',0,type=int)
    row =  platform.query.filter(platform.Pla_Id == Pla_Id).first()
    if row is None:
        row=platform()
    session['data'] =  { 'Pla_Id':row.Pla_Id, 'Pla_Name':row.Pla_Name, 'Pla_Host':row.Pla_Host, 'Pla_Port':row.Pla_Port, 'Pla_User':row.Pla_User, 'Pla_Password':row.Pla_Password}
    form = frm_platform_delete()

    if form.validate_on_submit():
        if  form.submit_Delete.data:
            print('Delete Data Here...')
            print('Delete Data Here...')
            try:
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                flash('Record %s deleted OK'%(Pla_Id))
            except exc.IntegrityError as e:
                db.session.rollback()
                flash('INTEGRITY ERROR: Are you sure there are no dependant records in other tables?')
                return redirect(url_for('.forms_Platforms_delete',Pla_Id=session['data']['Pla_Id']))

            return redirect(url_for('.select_Platforms_query'))
        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
            return redirect(url_for('.select_Platforms_query'))
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.select_Platforms_query'))


    return render_template('platforms_delete.html',C=C, form=form, data=session.get('data'),row=row)

# =============================================================================

@main.route('/select/Platforms_Query', methods=['GET','POST'])
@login_required
@admin_required
def select_Platforms_query():
    """ Select rows handling function for table Platforms """

    logger.debug('Enter: select_Platforms_query()')
    field =  request.args.get('field',None,type=str)
    value =  request.args.get('value',0,type=str)
    page  =  request.args.get('page',1,type=int)

    if field is not None:
        if   field == 'Pla_Id':
            rows =  platform.query.filter_by(Pla_Id=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Pla_Name':
            rows =  platform.query.filter_by(Pla_Name=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Pla_Host':
            rows =  platform.query.filter_by(Pla_Host=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Pla_Port':
            rows =  platform.query.filter_by(Pla_Port=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Pla_User':
            rows =  platform.query.filter_by(Pla_User=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Pla_Password':
            rows =  platform.query.filter_by(Pla_Password=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
    else:
       rows =  platform.query\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)

    next_url = url_for('.select_Platforms_query', page=rows.next_num) \
        if rows.has_next else None
    prev_url = url_for('.select_Platforms_query', page=rows.prev_num) \
        if rows.has_prev else None

    return render_template('platforms_All.html',C=C,rows=rows.items,next_url=next_url,prev_url=prev_url)
# =============================================================================

# =============================================================================

# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-11-30 16:47:18
# =============================================================================


@main.route('/forms/Rates', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@permission_required(Permission.MODIFY)
@admin_required
def forms_Rates():
    """ Form handling function for table Rates """

    logger.debug('Enter: forms_Rates()')
    Rat_Id  =  request.args.get('Rat_Id',0,type=int)
    row =  rate.query.filter(rate.Rat_Id == Rat_Id).first()
    if row is None:
        row=rate()

    session['data'] =  { 'Rat_Id':row.Rat_Id, 'Typ_Code':row.Typ_Code, 'Cus_Id':row.Cus_Id, 'Pla_Id':row.Pla_Id, 'CC_Id':row.CC_Id, 'CU_Id':row.CU_Id, 'Rat_Price':row.Rat_Price, 'Cur_Code':row.Cur_Code, 'MU_Code':row.MU_Code, 'Rat_Period':row.Rat_Period, 'Rat_Type':row.Rat_Type}
    form = frm_rate()

    if form.has_FKs:
        form.Typ_Code.choices = db.session.query(cu_type.Typ_Code,cu_type.Typ_Description).order_by(cu_type.Typ_Description).all()
        form.Cus_Id.choices = db.session.query(customer.Cus_Id,customer.Cus_Name).order_by(customer.Cus_Name).all()
        form.Pla_Id.choices = db.session.query(platform.Pla_Id,platform.Pla_Name).order_by(platform.Pla_Name).all()
        form.CC_Id.choices = db.session.query(cost_center.CC_Id,cost_center.CC_Description).order_by(cost_center.CC_Description).all()
        form.CU_Id.choices = db.session.query(charge_unit.CU_Id,charge_unit.CU_Description).order_by(charge_unit.CU_Description).all()
        form.Cur_Code.choices = db.session.query(currency.Cur_Code,currency.Cur_Name).order_by(currency.Cur_Name).all()
        form.MU_Code.choices = db.session.query(measure_unit.MU_Code,measure_unit.MU_Description).order_by(measure_unit.MU_Description).all()
        form.Rat_Period.choices = db.session.query(rat_period.Rat_Period,rat_period.Value).order_by(rat_period.Value).all()

    if form.validate_on_submit():
        if     form.submit_Save.data:
            row.Typ_Code = form.Typ_Code.data
            row.Cus_Id = form.Cus_Id.data
            row.Pla_Id = form.Pla_Id.data
            row.CC_Id = form.CC_Id.data
            row.CU_Id = form.CU_Id.data
            row.Rat_Price = form.Rat_Price.data
            row.Cur_Code = form.Cur_Code.data
            row.MU_Code = form.MU_Code.data
            row.Rat_Period = form.Rat_Period.data
            try:
               db.session.close()
               db.session.add(row)
               db.session.commit()
               db.session.close()
               flash('Record %s saved OK'%(Rat_Id))
            except Exception as e:
               db.session.rollback()
               db.session.close()
               flash('ERROR saving record : %s'%(e))
            return redirect(url_for('.select_Rates_query'))
        elif   form.submit_New.data:
            print('New Data Here...')
            db.session.close()
            row=rate()
            pass
            pass
            pass
            pass
            pass
            pass
            pass
            pass
            pass
            pass
            return redirect(url_for('.forms_Rates',Rat_Id=row.Rat_Id))

        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.forms_Rates',Rat_Id=row.Rat_Id))

    form.Typ_Code.data = row.Typ_Code
    form.Cus_Id.data = row.Cus_Id
    form.Pla_Id.data = row.Pla_Id
    form.CC_Id.data = row.CC_Id
    form.CU_Id.data = row.CU_Id
    form.Rat_Price.data = row.Rat_Price
    form.Cur_Code.data = row.Cur_Code
    form.MU_Code.data = row.MU_Code
    form.Rat_Period.data = row.Rat_Period
    return render_template('rates.html', form=form, row=row)

# =============================================================================

@main.route('/forms/Rates_delete', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@admin_required
def forms_Rates_delete():
    """ Delete record handling function for table Rates """

    logger.debug('Enter: forms_Rates_delete()')
    Rat_Id  =  request.args.get('Rat_Id',0,type=int)
    row =  rate.query.filter(rate.Rat_Id == Rat_Id).first()
    if row is None:
        row=rate()
    session['data'] =  { 'Rat_Id':row.Rat_Id, 'Typ_Code':row.Typ_Code, 'Cus_Id':row.Cus_Id, 'Pla_Id':row.Pla_Id, 'CC_Id':row.CC_Id, 'CU_Id':row.CU_Id, 'Rat_Price':row.Rat_Price, 'Cur_Code':row.Cur_Code, 'MU_Code':row.MU_Code, 'Rat_Period':row.Rat_Period, 'Rat_Type':row.Rat_Type}
    form = frm_rate_delete()

    if form.validate_on_submit():
        if  form.submit_Delete.data:
            print('Delete Data Here...')
            print('Delete Data Here...')
            try:
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                flash('Record %s deleted OK'%(Rat_Id))
            except exc.IntegrityError as e:
                db.session.rollback()
                flash('INTEGRITY ERROR: Are you sure there are no dependant records in other tables?')
                return redirect(url_for('.forms_Rates_delete',Rat_Id=session['data']['Rat_Id']))

            return redirect(url_for('.select_Rates_query'))
        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
            return redirect(url_for('.select_Rates_query'))
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.select_Rates_query'))


    return render_template('rates_delete.html',C=C, form=form, data=session.get('data'),row=row)

# =============================================================================

@main.route('/select/Rates_Query', methods=['GET','POST'])
@login_required
@admin_required
def select_Rates_query():
    """ Select rows handling function for table Rates """

    logger.debug('Enter: select_Rates_query()')
    field =  request.args.get('field',None,type=str)
    value =  request.args.get('value',0,type=str)
    page  =  request.args.get('page',1,type=int)

    if field is not None:
        if   field == 'Rat_Id':
            rows =  rate.query.filter_by(Rat_Id=value)\
               .join(cu_type,rate.Typ_Code == cu_type.Typ_Code).add_columns(cu_type.Typ_Description)\
               .join(customer,rate.Cus_Id == customer.Cus_Id).add_columns(customer.Cus_Name)\
               .join(platform,rate.Pla_Id == platform.Pla_Id).add_columns(platform.Pla_Name)\
               .join(cost_center,rate.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .join(charge_unit,rate.CU_Id == charge_unit.CU_Id).add_columns(charge_unit.CU_Description)\
               .join(currency,rate.Cur_Code == currency.Cur_Code).add_columns(currency.Cur_Name)\
               .join(measure_unit,rate.MU_Code == measure_unit.MU_Code).add_columns(measure_unit.MU_Description)\
               .join(rat_period,rate.Rat_Period == rat_period.Rat_Period).add_columns(rat_period.Value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Typ_Code':
            rows =  rate.query.filter_by(Typ_Code=value)\
               .join(cu_type,rate.Typ_Code == cu_type.Typ_Code).add_columns(cu_type.Typ_Description)\
               .join(customer,rate.Cus_Id == customer.Cus_Id).add_columns(customer.Cus_Name)\
               .join(platform,rate.Pla_Id == platform.Pla_Id).add_columns(platform.Pla_Name)\
               .join(cost_center,rate.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .join(charge_unit,rate.CU_Id == charge_unit.CU_Id).add_columns(charge_unit.CU_Description)\
               .join(currency,rate.Cur_Code == currency.Cur_Code).add_columns(currency.Cur_Name)\
               .join(measure_unit,rate.MU_Code == measure_unit.MU_Code).add_columns(measure_unit.MU_Description)\
               .join(rat_period,rate.Rat_Period == rat_period.Rat_Period).add_columns(rat_period.Value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Cus_Id':
            rows =  rate.query.filter_by(Cus_Id=value)\
               .join(cu_type,rate.Typ_Code == cu_type.Typ_Code).add_columns(cu_type.Typ_Description)\
               .join(customer,rate.Cus_Id == customer.Cus_Id).add_columns(customer.Cus_Name)\
               .join(platform,rate.Pla_Id == platform.Pla_Id).add_columns(platform.Pla_Name)\
               .join(cost_center,rate.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .join(charge_unit,rate.CU_Id == charge_unit.CU_Id).add_columns(charge_unit.CU_Description)\
               .join(currency,rate.Cur_Code == currency.Cur_Code).add_columns(currency.Cur_Name)\
               .join(measure_unit,rate.MU_Code == measure_unit.MU_Code).add_columns(measure_unit.MU_Description)\
               .join(rat_period,rate.Rat_Period == rat_period.Rat_Period).add_columns(rat_period.Value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Pla_Id':
            rows =  rate.query.filter_by(Pla_Id=value)\
               .join(cu_type,rate.Typ_Code == cu_type.Typ_Code).add_columns(cu_type.Typ_Description)\
               .join(customer,rate.Cus_Id == customer.Cus_Id).add_columns(customer.Cus_Name)\
               .join(platform,rate.Pla_Id == platform.Pla_Id).add_columns(platform.Pla_Name)\
               .join(cost_center,rate.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .join(charge_unit,rate.CU_Id == charge_unit.CU_Id).add_columns(charge_unit.CU_Description)\
               .join(currency,rate.Cur_Code == currency.Cur_Code).add_columns(currency.Cur_Name)\
               .join(measure_unit,rate.MU_Code == measure_unit.MU_Code).add_columns(measure_unit.MU_Description)\
               .join(rat_period,rate.Rat_Period == rat_period.Rat_Period).add_columns(rat_period.Value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CC_Id':
            rows =  rate.query.filter_by(CC_Id=value)\
               .join(cu_type,rate.Typ_Code == cu_type.Typ_Code).add_columns(cu_type.Typ_Description)\
               .join(customer,rate.Cus_Id == customer.Cus_Id).add_columns(customer.Cus_Name)\
               .join(platform,rate.Pla_Id == platform.Pla_Id).add_columns(platform.Pla_Name)\
               .join(cost_center,rate.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .join(charge_unit,rate.CU_Id == charge_unit.CU_Id).add_columns(charge_unit.CU_Description)\
               .join(currency,rate.Cur_Code == currency.Cur_Code).add_columns(currency.Cur_Name)\
               .join(measure_unit,rate.MU_Code == measure_unit.MU_Code).add_columns(measure_unit.MU_Description)\
               .join(rat_period,rate.Rat_Period == rat_period.Rat_Period).add_columns(rat_period.Value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CU_Id':
            rows =  rate.query.filter_by(CU_Id=value)\
               .join(cu_type,rate.Typ_Code == cu_type.Typ_Code).add_columns(cu_type.Typ_Description)\
               .join(customer,rate.Cus_Id == customer.Cus_Id).add_columns(customer.Cus_Name)\
               .join(platform,rate.Pla_Id == platform.Pla_Id).add_columns(platform.Pla_Name)\
               .join(cost_center,rate.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .join(charge_unit,rate.CU_Id == charge_unit.CU_Id).add_columns(charge_unit.CU_Description)\
               .join(currency,rate.Cur_Code == currency.Cur_Code).add_columns(currency.Cur_Name)\
               .join(measure_unit,rate.MU_Code == measure_unit.MU_Code).add_columns(measure_unit.MU_Description)\
               .join(rat_period,rate.Rat_Period == rat_period.Rat_Period).add_columns(rat_period.Value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Rat_Price':
            rows =  rate.query.filter_by(Rat_Price=value)\
               .join(cu_type,rate.Typ_Code == cu_type.Typ_Code).add_columns(cu_type.Typ_Description)\
               .join(customer,rate.Cus_Id == customer.Cus_Id).add_columns(customer.Cus_Name)\
               .join(platform,rate.Pla_Id == platform.Pla_Id).add_columns(platform.Pla_Name)\
               .join(cost_center,rate.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .join(charge_unit,rate.CU_Id == charge_unit.CU_Id).add_columns(charge_unit.CU_Description)\
               .join(currency,rate.Cur_Code == currency.Cur_Code).add_columns(currency.Cur_Name)\
               .join(measure_unit,rate.MU_Code == measure_unit.MU_Code).add_columns(measure_unit.MU_Description)\
               .join(rat_period,rate.Rat_Period == rat_period.Rat_Period).add_columns(rat_period.Value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Cur_Code':
            rows =  rate.query.filter_by(Cur_Code=value)\
               .join(cu_type,rate.Typ_Code == cu_type.Typ_Code).add_columns(cu_type.Typ_Description)\
               .join(customer,rate.Cus_Id == customer.Cus_Id).add_columns(customer.Cus_Name)\
               .join(platform,rate.Pla_Id == platform.Pla_Id).add_columns(platform.Pla_Name)\
               .join(cost_center,rate.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .join(charge_unit,rate.CU_Id == charge_unit.CU_Id).add_columns(charge_unit.CU_Description)\
               .join(currency,rate.Cur_Code == currency.Cur_Code).add_columns(currency.Cur_Name)\
               .join(measure_unit,rate.MU_Code == measure_unit.MU_Code).add_columns(measure_unit.MU_Description)\
               .join(rat_period,rate.Rat_Period == rat_period.Rat_Period).add_columns(rat_period.Value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'MU_Code':
            rows =  rate.query.filter_by(MU_Code=value)\
               .join(cu_type,rate.Typ_Code == cu_type.Typ_Code).add_columns(cu_type.Typ_Description)\
               .join(customer,rate.Cus_Id == customer.Cus_Id).add_columns(customer.Cus_Name)\
               .join(platform,rate.Pla_Id == platform.Pla_Id).add_columns(platform.Pla_Name)\
               .join(cost_center,rate.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .join(charge_unit,rate.CU_Id == charge_unit.CU_Id).add_columns(charge_unit.CU_Description)\
               .join(currency,rate.Cur_Code == currency.Cur_Code).add_columns(currency.Cur_Name)\
               .join(measure_unit,rate.MU_Code == measure_unit.MU_Code).add_columns(measure_unit.MU_Description)\
               .join(rat_period,rate.Rat_Period == rat_period.Rat_Period).add_columns(rat_period.Value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Rat_Period':
            rows =  rate.query.filter_by(Rat_Period=value)\
               .join(cu_type,rate.Typ_Code == cu_type.Typ_Code).add_columns(cu_type.Typ_Description)\
               .join(customer,rate.Cus_Id == customer.Cus_Id).add_columns(customer.Cus_Name)\
               .join(platform,rate.Pla_Id == platform.Pla_Id).add_columns(platform.Pla_Name)\
               .join(cost_center,rate.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .join(charge_unit,rate.CU_Id == charge_unit.CU_Id).add_columns(charge_unit.CU_Description)\
               .join(currency,rate.Cur_Code == currency.Cur_Code).add_columns(currency.Cur_Name)\
               .join(measure_unit,rate.MU_Code == measure_unit.MU_Code).add_columns(measure_unit.MU_Description)\
               .join(rat_period,rate.Rat_Period == rat_period.Rat_Period).add_columns(rat_period.Value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Rat_Type':
            rows =  rate.query.filter_by(Rat_Type=value)\
               .join(cu_type,rate.Typ_Code == cu_type.Typ_Code).add_columns(cu_type.Typ_Description)\
               .join(customer,rate.Cus_Id == customer.Cus_Id).add_columns(customer.Cus_Name)\
               .join(platform,rate.Pla_Id == platform.Pla_Id).add_columns(platform.Pla_Name)\
               .join(cost_center,rate.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .join(charge_unit,rate.CU_Id == charge_unit.CU_Id).add_columns(charge_unit.CU_Description)\
               .join(currency,rate.Cur_Code == currency.Cur_Code).add_columns(currency.Cur_Name)\
               .join(measure_unit,rate.MU_Code == measure_unit.MU_Code).add_columns(measure_unit.MU_Description)\
               .join(rat_period,rate.Rat_Period == rat_period.Rat_Period).add_columns(rat_period.Value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
    else:
       rows =  rate.query\
               .join(cu_type,rate.Typ_Code == cu_type.Typ_Code).add_columns(cu_type.Typ_Description)\
               .join(customer,rate.Cus_Id == customer.Cus_Id).add_columns(customer.Cus_Name)\
               .join(platform,rate.Pla_Id == platform.Pla_Id).add_columns(platform.Pla_Name)\
               .join(cost_center,rate.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .join(charge_unit,rate.CU_Id == charge_unit.CU_Id).add_columns(charge_unit.CU_Description)\
               .join(currency,rate.Cur_Code == currency.Cur_Code).add_columns(currency.Cur_Name)\
               .join(measure_unit,rate.MU_Code == measure_unit.MU_Code).add_columns(measure_unit.MU_Description)\
               .join(rat_period,rate.Rat_Period == rat_period.Rat_Period).add_columns(rat_period.Value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)

    next_url = url_for('.select_Rates_query', page=rows.next_num) \
        if rows.has_next else None
    prev_url = url_for('.select_Rates_query', page=rows.prev_num) \
        if rows.has_prev else None

    return render_template('rates_All.html',C=C,rows=rows.items,next_url=next_url,prev_url=prev_url)
# =============================================================================

# =============================================================================

# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-11-30 16:47:18
# =============================================================================


@main.route('/forms/Rat_Periods', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@permission_required(Permission.MODIFY)
@admin_required
def forms_Rat_Periods():
    """ Form handling function for table Rat_Periods """

    logger.debug('Enter: forms_Rat_Periods()')
    Rat_Period  =  request.args.get('Rat_Period',0,type=int)
    row =  rat_period.query.filter(rat_period.Rat_Period == Rat_Period).first()
    if row is None:
        row=rat_period()

    session['data'] =  { 'Rat_Period':row.Rat_Period, 'Value':row.Value}
    form = frm_rat_period()

    if form.validate_on_submit():
        if     form.submit_Save.data:
            row.Rat_Period = form.Rat_Period.data
            row.Value = form.Value.data
            try:
               db.session.close()
               db.session.add(row)
               db.session.commit()
               db.session.close()
               flash('Record %s saved OK'%(Rat_Period))
            except Exception as e:
               db.session.rollback()
               db.session.close()
               flash('ERROR saving record : %s'%(e))
            return redirect(url_for('.select_Rat_Periods_query'))
        elif   form.submit_New.data:
            print('New Data Here...')
            db.session.close()
            row=rat_period()
            return redirect(url_for('.forms_Rat_Periods'))

        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.forms_Rat_Periods'))

    form.Rat_Period.data = row.Rat_Period
    form.Value.data = row.Value
    return render_template('rat_periods.html', form=form, row=row)

# =============================================================================

@main.route('/forms/Rat_Periods_delete', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@admin_required
def forms_Rat_Periods_delete():
    """ Delete record handling function for table Rat_Periods """

    logger.debug('Enter: forms_Rat_Periods_delete()')
    Rat_Period  =  request.args.get('Rat_Period',0,type=int)
    row =  rat_period.query.filter(rat_period.Rat_Period == Rat_Period).first()
    if row is None:
        row=rat_period()
    session['data'] =  { 'Rat_Period':row.Rat_Period, 'Value':row.Value}
    form = frm_rat_period_delete()

    if form.validate_on_submit():
        if  form.submit_Delete.data:
            print('Delete Data Here...')
            print('Delete Data Here...')
            try:
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                flash('Record %s deleted OK'%(Rat_Period))
            except exc.IntegrityError as e:
                db.session.rollback()
                flash('INTEGRITY ERROR: Are you sure there are no dependant records in other tables?')
                return redirect(url_for('.forms_Rat_Periods_delete',Rat_Period=session['data']['Rat_Period']))

            return redirect(url_for('.select_Rat_Periods_query'))
        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
            return redirect(url_for('.select_Rat_Periods_query'))
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.select_Rat_Periods_query'))


    return render_template('rat_periods_delete.html',C=C, form=form, data=session.get('data'),row=row)

# =============================================================================

@main.route('/select/Rat_Periods_Query', methods=['GET','POST'])
@login_required
@admin_required
def select_Rat_Periods_query():
    """ Select rows handling function for table Rat_Periods """

    logger.debug('Enter: select_Rat_Periods_query()')
    field =  request.args.get('field',None,type=str)
    value =  request.args.get('value',0,type=str)
    page  =  request.args.get('page',1,type=int)

    if field is not None:
        if   field == 'Rat_Period':
            rows =  rat_period.query.filter_by(Rat_Period=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Value':
            rows =  rat_period.query.filter_by(Value=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
    else:
       rows =  rat_period.query\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)

    next_url = url_for('.select_Rat_Periods_query', page=rows.next_num) \
        if rows.has_next else None
    prev_url = url_for('.select_Rat_Periods_query', page=rows.prev_num) \
        if rows.has_prev else None

    return render_template('rat_periods_All.html',C=C,rows=rows.items,next_url=next_url,prev_url=prev_url)
# =============================================================================

# =============================================================================

# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-11-30 16:47:18
# =============================================================================


@main.route('/forms/Trace', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@permission_required(Permission.MODIFY)
@admin_required
def forms_Trace():
    """ Form handling function for table Trace """

    logger.debug('Enter: forms_Trace()')
    ID  =  request.args.get('ID',0,type=int)
    row =  trace.query.filter(trace.ID == ID).first()
    if row is None:
        row=trace()

    session['data'] =  { 'ID':row.ID, 'LINE':row.LINE}
    form = frm_trace()

    if form.validate_on_submit():
        if     form.submit_Save.data:
            row.LINE = form.LINE.data
            try:
               db.session.close()
               db.session.add(row)
               db.session.commit()
               db.session.close()
               flash('Record %s saved OK'%(ID))
            except Exception as e:
               db.session.rollback()
               db.session.close()
               flash('ERROR saving record : %s'%(e))
            return redirect(url_for('.select_Trace_query'))
        elif   form.submit_New.data:
            print('New Data Here...')
            db.session.close()
            row=trace()
            pass
            return redirect(url_for('.forms_Trace',ID=row.ID))

        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.forms_Trace',ID=row.ID))

    form.LINE.data = row.LINE
    return render_template('trace.html', form=form, row=row)

# =============================================================================

@main.route('/forms/Trace_delete', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@admin_required
def forms_Trace_delete():
    """ Delete record handling function for table Trace """

    logger.debug('Enter: forms_Trace_delete()')
    ID  =  request.args.get('ID',0,type=int)
    row =  trace.query.filter(trace.ID == ID).first()
    if row is None:
        row=trace()
    session['data'] =  { 'ID':row.ID, 'LINE':row.LINE}
    form = frm_trace_delete()

    if form.validate_on_submit():
        if  form.submit_Delete.data:
            print('Delete Data Here...')
            print('Delete Data Here...')
            try:
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                flash('Record %s deleted OK'%(ID))
            except exc.IntegrityError as e:
                db.session.rollback()
                flash('INTEGRITY ERROR: Are you sure there are no dependant records in other tables?')
                return redirect(url_for('.forms_Trace_delete',ID=session['data']['ID']))

            return redirect(url_for('.select_Trace_query'))
        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
            return redirect(url_for('.select_Trace_query'))
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.select_Trace_query'))


    return render_template('trace_delete.html',C=C, form=form, data=session.get('data'),row=row)

# =============================================================================

@main.route('/select/Trace_Query', methods=['GET','POST'])
@login_required
@admin_required
def select_Trace_query():
    """ Select rows handling function for table Trace """

    logger.debug('Enter: select_Trace_query()')
    field =  request.args.get('field',None,type=str)
    value =  request.args.get('value',0,type=str)
    page  =  request.args.get('page',1,type=int)

    if field is not None:
        if   field == 'ID':
            rows =  trace.query.filter_by(ID=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'LINE':
            rows =  trace.query.filter_by(LINE=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
    else:
       rows =  trace.query\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)

    next_url = url_for('.select_Trace_query', page=rows.next_num) \
        if rows.has_next else None
    prev_url = url_for('.select_Trace_query', page=rows.prev_num) \
        if rows.has_prev else None

    return render_template('trace_All.html',C=C,rows=rows.items,next_url=next_url,prev_url=prev_url)
# =============================================================================

# =============================================================================
# View for Get Billing Resume from DB
# (c) Sertechno 2018
# GLVH @ 2018-11-11
# =============================================================================

from ..models       import frm_billing_resume
from babel.numbers  import format_number, format_decimal, format_percent

@main.route('/forms/Get_Billing_Resume', methods=['GET', 'POST'])
@login_required
def forms_Get_Billing_Resume():
    logger.debug('Enter: forms_Get_Billing_Resume()'%())

    session['data'] =  { 'Cus_Id': None, 'CIT_Date_From':None, 'CIT_Date_To':None, 'CIT_Status':1,'Cur_Code':'USD'}

    form = frm_billing_resume()

    # Will setup filter to consider only Currencies with actual Exchange Rates in DB
    # Prepare query
    query = db.session.query(exchange_rate.Cur_Code.distinct().label('Cur_Code'))
    # Execute query an conver in list for further use in choices selection
    cur_choices = [row.Cur_Code for row in query.all()]

    form.Cus_Id.choices     = db.session.query(customer.Cus_Id,customer.Cus_Name).all()
    form.CIT_Status.choices = db.session.query(cit_status.CIT_Status,cit_status.Value).all()
    form.Cur_Code.choices   = db.session.query(currency.Cur_Code,currency.Cur_Name).filter(currency.Cur_Code.in_(cur_choices)).all()

    if form.validate_on_submit():
        session['data']['Cus_Id'        ] = form.Cus_Id.data
        session['data']['CIT_Date_From' ] = form.CIT_Date_From.data
        session['data']['CIT_Date_To'   ] = form.CIT_Date_To.data
        session['data']['CIT-Status'    ] = form.CIT_Status.data
        session['data']['Cur_Code'      ] = form.Cur_Code.data
        if     form.submit_Report.data:
            # Get the Selected options index for string lists
            for i in range(len(form.Cus_Id.choices)):
                if form.Cus_Id.choices[i][0]==form.Cus_Id.data:
                    cus_index=i
            for i in range(len(form.Cur_Code.choices)):
                if form.Cur_Code.choices[i][0]==form.Cur_Code.data:
                    cur_index=i
            
            return redirect(url_for('.report_Billing_Resume',
                                Cus_Id          = form.Cus_Id.data,
                                Cus_Name        = form.Cus_Id.choices[cus_index][1],
                                CIT_Date_From   = form.CIT_Date_From.data,
                                CIT_Date_To     = form.CIT_Date_To.data,
                                CIT_Status      = form.CIT_Status.data,
                                CIT_Status_Value= form.CIT_Status.choices[form.CIT_Status.data-1][1],
                                Cur_Code        = form.Cur_Code.data,
                                Cur_Name        = form.Cur_Code.choices[cur_index][1]
                                ))

        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Report discarded ...')
        else:
            print('form validated but not submited ???')
        return redirect(url_for('.forms_Get_Billing_Resume'))

    form.Cus_Id.data        = session['data']['Cus_Id']
    form.CIT_Date_From.data = session['data']['CIT_Date_From']
    form.CIT_Date_To.data   = session['data']['CIT_Date_To']
    form.CIT_Status.data    = session['data']['CIT_Status']
    form.Cur_Code.data      = session['data']['Cur_Code']

    return render_template('get_billing_resume.html',form=form, data=session.get('data'))

# =============================================================================

import simplejson as json

@main.route('/report/Billing_Resume', methods=['GET','POST'])
@login_required
def report_Billing_Resume():
    logger.debug('Enter: report_Billing_Resume()')
    Cus_Id          =  request.args.get('Cus_Id',None,type=int)
    Cus_Name        =  request.args.get('Cus_Name',None,type=str)
    CIT_Date_From   =  request.args.get('CIT_Date_From',None,type=str)
    CIT_Date_To     =  request.args.get('CIT_Date_To',None,type=str)
    CIT_Status      =  request.args.get('CIT_Status',None,type=int)
    CIT_Status_Value=  request.args.get('CIT_Status_Value',None,type=str)
    Cur_Code        =  request.args.get('Cur_Code',None,type=str)
    Cur_Name        =  request.args.get('Cur_Name',None,type=str)
    # Get Actual Data from Database
    # NOTE: Here needs some Sand-Clock Message or something in case it takes so long ...
    query="CALL Get_Billing_Resume(%d,'%s','%s',%d,'%s')"%(Cus_Id,CIT_Date_From,CIT_Date_To,CIT_Status,Cur_Code)
    
    rows =  db.engine.execute(query).fetchall()
    
    # ----------------------------------------------------------------------------------------------
    # NOTA AQUI HAY QUE MANEJAR LOS EXTRACTOS ESTATICOS, SON BUENA OPCION, PONERLA COMO ADICIONAL
    # ----------------------------------------------------------------------------------------------
    json_route = "/tmp"
    json_file_name =  "%s/CR001_%s_%s_%s_%s_%s.json"%(json_route,Cus_Id,CIT_Date_From,CIT_Date_To,CIT_Status,Cur_Code)
    
    dict = {}
    dict.update({'header':{}})
    dict['header'].update({'customer':Cus_Id})
    dict['header'].update({'from':CIT_Date_From})
    dict['header'].update({'to':CIT_Date_To})
    dict['header'].update({'status':CIT_Status})
    dict['header'].update({'currency':Cur_Code})
    dict.update({'detail':[]})
    count = 0
    for row in rows:
        dict['detail'].append({})
        dict['detail'][count].update( {    'items':row.ITEMS, 'cu':row.CU, 'price':row.RATE_PRICE, 'q':row.Q, 'subtotal':row.ST_AT_RATE,\
                                    'xr':row.BILLXR, 'total':row.TOTAL_BILL_CUR \
                                })
        count += 1
    dict['header'].update({'count':count})
    
    with open(json_file_name,'w') as fp:
        json.dump(dict,fp)
    
    return render_template('report_billing_resume.html',rows=rows,
                Cus_Id=Cus_Id,
                Cus_Name=Cus_Name,
                CIT_Date_From=CIT_Date_From,
                CIT_Date_To=CIT_Date_To,
                CIT_Status=CIT_Status,
                CIT_Status_Value=CIT_Status_Value,                
                Cur_Code=Cur_Code,
                Cur_Name=Cur_Name
                )

# =============================================================================
# View for Get Charging Resume from DB
# (c) Sertechno 2018
# GLVH @ 2018-11-26
# =============================================================================

from ..models       import frm_charging_resume
from babel.numbers  import format_number, format_decimal, format_percent

@main.route('/forms/Get_Charging_Resume', methods=['GET', 'POST'])
@login_required
def forms_Get_Charging_Resume():
    logger.debug('Enter: forms_Get_Charging_Resume()'%())

    session['data'] =  { 'Cus_Id': None, 'CIT_Date_From':None, 'CIT_Date_To':None, 'CIT_Status':1,'Cur_Code':'USD'}

    form = frm_charging_resume()

    # ------------------------------------------------------------------------------
    # Will setup filter to consider only Currencies with actual Exchange Rates in DB
    # Prepare query
    query = db.session.query(exchange_rate.Cur_Code.distinct().label('Cur_Code'))
    # Execute query and convert in list for further use in choices selection
    cur_choices = [row.Cur_Code for row in query.all()]

    form.Cus_Id.choices     = db.session.query(customer.Cus_Id,customer.Cus_Name).all()
    form.CIT_Status.choices = db.session.query(cit_status.CIT_Status,cit_status.Value).all()
    form.Cur_Code.choices   = db.session.query(currency.Cur_Code,currency.Cur_Name).filter(currency.Cur_Code.in_(cur_choices)).all()

    if form.validate_on_submit():
        session['data']['Cus_Id'        ] = form.Cus_Id.data
        session['data']['CIT_Date_From' ] = form.CIT_Date_From.data
        session['data']['CIT_Date_To'   ] = form.CIT_Date_To.data
        session['data']['CIT-Status'    ] = form.CIT_Status.data
        session['data']['Cur_Code'      ] = form.Cur_Code.data
        if     form.submit_Report.data:
            # Get the Selected options index for string lists
            for i in range(len(form.Cus_Id.choices)):
                if form.Cus_Id.choices[i][0]==form.Cus_Id.data:
                    cus_index=i
            for i in range(len(form.Cur_Code.choices)):
                if form.Cur_Code.choices[i][0]==form.Cur_Code.data:
                    cur_index=i
            return redirect(url_for('.report_Charging_Resume',
                                Cus_Id          = form.Cus_Id.data,
                                Cus_Name        = form.Cus_Id.choices[cus_index][1],
                                CIT_Date_From   = form.CIT_Date_From.data,
                                CIT_Date_To     = form.CIT_Date_To.data,
                                CIT_Status      = form.CIT_Status.data,
                                CIT_Status_Value= form.CIT_Status.choices[form.CIT_Status.data-1][1],
                                Cur_Code        = form.Cur_Code.data,
                                Cur_Name        = form.Cur_Code.choices[cur_index][1],
                                Update          = 0
                                ))
        if     form.submit_Update.data:
            # Get the Selected options index for string lists
            for i in range(len(form.Cus_Id.choices)):
                if form.Cus_Id.choices[i][0]==form.Cus_Id.data:
                    cus_index=i
            for i in range(len(form.Cur_Code.choices)):
                if form.Cur_Code.choices[i][0]==form.Cur_Code.data:
                    cur_index=i
            return redirect(url_for('.report_Charging_Resume',
                                Cus_Id          = form.Cus_Id.data,
                                Cus_Name        = form.Cus_Id.choices[cus_index][1],
                                CIT_Date_From   = form.CIT_Date_From.data,
                                CIT_Date_To     = form.CIT_Date_To.data,
                                CIT_Status      = form.CIT_Status.data,
                                CIT_Status_Value= form.CIT_Status.choices[form.CIT_Status.data-1][1],
                                Cur_Code        = form.Cur_Code.data,
                                Cur_Name        = form.Cur_Code.choices[cur_index][1],
                                Update          = 1
                                ))

        elif   form.submit_Cancel.data:
            #print('Cancel Data Here ... does nothing')
            flash('Report discarded ...')
        else:
            flash('form validated but not submited. Report to Support ...')
            #print('form validated but not submited ???')
        return redirect(url_for('.forms_Get_Charging_Resume'))

    form.Cus_Id.data        = session['data']['Cus_Id']
    form.CIT_Date_From.data = session['data']['CIT_Date_From']
    form.CIT_Date_To.data   = session['data']['CIT_Date_To']
    form.CIT_Status.data    = session['data']['CIT_Status']
    form.Cur_Code.data      = session['data']['Cur_Code']

    return render_template('get_charging_resume.html',form=form, data=session.get('data'))

# =============================================================================

import simplejson as json

@main.route('/report/Charging_Resume', methods=['GET','POST'])
@login_required
def report_Charging_Resume():
    logger.debug('Enter: report_Charging_Resume()')
    Cus_Id          =  request.args.get('Cus_Id',None,type=int)
    Cus_Name        =  request.args.get('Cus_Name',None,type=str)
    CIT_Date_From   =  request.args.get('CIT_Date_From',None,type=str)
    CIT_Date_To     =  request.args.get('CIT_Date_To',None,type=str)
    CIT_Status      =  request.args.get('CIT_Status',None,type=int)
    CIT_Status_Value=  request.args.get('CIT_Status_Value',None,type=str)
    Cur_Code        =  request.args.get('Cur_Code',None,type=str)
    Cur_Name        =  request.args.get('Cur_Name',None,type=str)
    Update          =  request.args.get('Update',0,type=int)
    
    
    # Updated cached data for this specific query if requested 
    if Update == 1:
        # -------------------------------------------------------------------------------------------------------------- #
        # Previous Code faster but requires more memory will be replaced by an by CI loop                                #
        # query="CALL Update_Charge_Resume(%d,'%s','%s',%d,'%s')"%(Cus_Id,CIT_Date_From,CIT_Date_To,CIT_Status,Cur_Code) #
        # resume_records = db.engine.execute(query).scalar()                                                             #
        # -------------------------------------------------------------------------------------------------------------- #
        query = "SELECT DISTINCT CI_Id FROM Configuration_Items WHERE Cus_Id=%d"%(Cus_Id)
        print("query=",query)
        CI = db.engine.execute(query)
        print("%d CI's found for customer %d"%(CI.rowcount,Cus_Id))
        resume_records=0
        for ci in CI:
            query="CALL Update_Charge_Resume_CI(%s,'%s','%s',%s,'%s',%s)"%\
                    (Cus_Id,CIT_Date_From,CIT_Date_To,CIT_Status,Cur_Code,ci.CI_Id)
            print("query=",query)
            records=db.engine.execute(query)
            resume_records += records.scalar()
        print("report_Changing_Resume: resume_records = %s"%resume_records)
        
    # Get Actual Remume Data from Database
    # NOTE: Here needs some Sand-Clock Message or something in case it takes so long ...
    query="CALL Get_Charge_Resume(%d,'%s','%s',%d,'%s')"%(Cus_Id,CIT_Date_From,CIT_Date_To,CIT_Status,Cur_Code)
    #print("2 query=",query)
    
    rows =  db.engine.execute(query).fetchall()
    
    return render_template('report_charging_resume.html',rows=rows,
                Cus_Id=Cus_Id,
                Cus_Name=Cus_Name,
                CIT_Date_From=CIT_Date_From,
                CIT_Date_To=CIT_Date_To,
                CIT_Status=CIT_Status,
                CIT_Status_Value=CIT_Status_Value,                
                Cur_Code=Cur_Code,
                Cur_Name=Cur_Name
                )

# =============================================================================
# View for Get Billing Resume fro DB
# (c) Sertechno 2018
# GLVH @ 2018-11-11
# =============================================================================


# Support Constants, Variables & Functions
RAT_TYPE        =0x01
RAT_PLATFORM    =0x02
RAT_CUSTOMER    =0x04
RAT_CC          =0x08
RAT_CU          =0x10

Valid_Rat_Types = [   RAT_TYPE,
                RAT_TYPE|RAT_PLATFORM,
                RAT_TYPE|RAT_PLATFORM|RAT_CUSTOMER,
                RAT_TYPE|RAT_PLATFORM|RAT_CUSTOMER|RAT_CC,
                RAT_TYPE|RAT_PLATFORM|RAT_CUSTOMER|RAT_CC|RAT_CU
                ]

def Get_Rat_Type(Rate):
    rate_type = 0x00
    if Rate.Typ_Code != 'NUL'   :   rate_type |= RAT_TYPE    
    if Rate.Pla_Id != 1         :   rate_type |= RAT_PLATFORM
    if Rate.Cus_Id != 1         :   rate_type |= RAT_CUSTOMER
    if Rate.CC_Id  != 1         :   rate_type |= RAT_CC
    if Rate.CU_Id  != 1         :   rate_type |= CU
    return rate_type

def is_valid_rate(Rate):
    return Rate in Valid_Rat_Types
    

def Update_Rates_Type():
    #for t in Valid_Rat_Types:
    #    #print("Valid Rat Type ",t)
    
    rate_rows=rate.query.all()
    for rat in rate_rows:
        #print(rat,Get_Rat_Type(rat),is_valid_rate(Get_Rat_Type(rat)))
        rat.Rat_Type=Get_Rat_Type(rat)
        db.session.add(rat)
        db.session.commit()

from babel.numbers  import format_number, format_decimal, format_percent
from sqlalchemy.sql.expression import or_

@main.route('/reports/Data_Consistency', methods=['GET'])
@login_required
def reports_Data_Consistency():
    logger.debug('Enter: reports_Data_Consistency()'%())

    # Prepare query
    version  = db.engine.execute("SELECT VERSION()").fetchall()
    hostname = db.engine.execute("SELECT @@HOSTNAME").fetchall()
    data={}
    data.update({'version': version[0][0]})
    data.update({'hostname': hostname[0][0]})
    
    """
    query = "SELECT * FROM Configuration_Items "\
                "JOIN Customers         USING (Cus_Id) "\
                "JOIN Platforms         USING (Pla_Id) "\
                "JOIN Cost_Centers      ON (Configuration_Items.CC_Id=Cost_Centers.CC_Id) "\
                "JOIN CIT_Generations   USING (CIT_Generation) "\
                "WHERE Configuration_Items.CC_Id = Customers.CC_Id "\
                "OR Configuration_Items.CC_Id = 1"
                
    ci_rows=db.engine.execute(query).fetchall()
    """
    ci_rows=configuration_item.query\
                .join(customer)                                                 .add_column(customer.Cus_Name)\
                .join(platform)                                                 .add_column(platform.Pla_Name)\
                .join(cost_center,cost_center.CC_Id==configuration_item.CC_Id)  .add_column(cost_center.CC_Description)\
                .join(cit_generation)                                           .add_column(cit_generation.Value)\
                .filter(or_(    configuration_item.CC_Id==customer.CC_Id\
                                ,configuration_item.CC_Id==1))\
                .all()
                
                
    data.update({'ci_rows': ci_rows})
    
    Update_Rates_Type()
    
    rate_rows=rate.query\
                .join(customer)                                                 .add_column(customer.Cus_Name)\
                .join(platform)                                                 .add_column(platform.Pla_Name)\
                .join(cost_center,cost_center.CC_Id==rate.CC_Id)                .add_column(cost_center.CC_Description)\
                .join(charge_unit)                                              .add_column(charge_unit.CU_Description)\
                .order_by(rate.Pla_Id,rate.Cus_Id,rate.CC_Id,rate.CU_Id,rate.Typ_Code)\
                .all()
    
    data.update({'rate_rows': rate_rows})

    
    return render_template('report_data_consistency.html',data=data,is_valid_rate=is_valid_rate)

# =============================================================================


# =============================================================================
# View for Get Billing Resume fro DB
# (c) Sertechno 2018
# GLVH @ 2018-11-11
# =============================================================================


from babel.numbers  import format_number, format_decimal, format_percent

@main.route('/reports/DB_Status', methods=['GET'])
@login_required
def reports_DB_Status():
    logger.debug('Enter: reports_DB_Status()'%())


    # Prepare query
    version  = db.engine.execute("SELECT VERSION()").fetchall()
    hostname = db.engine.execute("SELECT @@HOSTNAME").fetchall()
    query=  " SELECT table_schema as `Database`, table_name AS `Table`, round(((data_length + index_length) / 1024 / 1024), 2)" \
            "`Size in MB`  FROM information_schema.TABLES  WHERE table_schema = 'collector' ORDER BY (data_length + index_length) DESC"
    table_usage = db.engine.execute(query).fetchall()
    data={}
    data.update({'version': version[0][0]})
    data.update({'hostname': hostname[0][0]})
    data.update({'table_usage': table_usage})
    data.update({'table_data': {} })
    
    for t in range(len(data['table_usage'])):
        query = "SELECT count(*) FROM %s"%data['table_usage'][t][1]
        count=db.engine.execute(query).fetchall()
        data['table_data'].update({data['table_usage'][t][1]:{}})
        data['table_data'][data['table_usage'][t][1]].update({'count':count[0][0]})
        
    return render_template('report_db_status.html',data=data)

# =============================================================================


# =============================================================================
# View for Get Billing Resume fro DB
# (c) Sertechno 2018
# GLVH @ 2018-11-11
# =============================================================================

from ..models       import frm_export_billing_resume
from babel.numbers  import format_number, format_decimal, format_percent

@main.route('/forms/Export_Billing_Resume', methods=['GET', 'POST'])
@login_required
def forms_Export_Billing_Resume():
    logger.debug('Enter: forms_Get_Billing_Resume()'%())

    session['data'] =  { 'Cus_Id': None, 'CIT_Date_From':None, 'CIT_Date_To':None, 'CIT_Status':1,'Cur_Code':'USD'}

    form = frm_export_billing_resume()

    # Will setup filter to consider only Currencies with actual Exchange Rates in DB
    # Prepare query
    query = db.session.query(exchange_rate.Cur_Code.distinct().label('Cur_Code'))
    # Execute query an conver in list for further use in choices selection
    cur_choices = [row.Cur_Code for row in query.all()]

    form.Cus_Id.choices     = db.session.query(customer.Cus_Id,customer.Cus_Name).all()
    form.CIT_Status.choices = db.session.query(cit_status.CIT_Status,cit_status.Value).all()
    form.Cur_Code.choices   = db.session.query(currency.Cur_Code,currency.Cur_Name).filter(currency.Cur_Code.in_(cur_choices)).all()

    if form.validate_on_submit():
        session['data']['Cus_Id'        ] = form.Cus_Id.data
        session['data']['CIT_Date_From' ] = form.CIT_Date_From.data
        session['data']['CIT_Date_To'   ] = form.CIT_Date_To.data
        session['data']['CIT-Status'    ] = form.CIT_Status.data
        session['data']['Cur_Code'      ] = form.Cur_Code.data
        # Get the Selected options index for string lists
        for i in range(len(form.Cus_Id.choices)):
            if form.Cus_Id.choices[i][0]==form.Cus_Id.data:
                cus_index=i
        for i in range(len(form.Cur_Code.choices)):
            if form.Cur_Code.choices[i][0]==form.Cur_Code.data:
                cur_index=i

        if     form.submit_PDF.data:
            return redirect(url_for('.export_Billing_Resume',
                                Cus_Id          = form.Cus_Id.data,
                                Cus_Name        = form.Cus_Id.choices[cus_index][1],
                                CIT_Date_From   = form.CIT_Date_From.data,
                                CIT_Date_To     = form.CIT_Date_To.data,
                                CIT_Status      = form.CIT_Status.data,
                                CIT_Status_Value= form.CIT_Status.choices[form.CIT_Status.data][1],
                                Cur_Code        = form.Cur_Code.data,
                                Cur_Name        = form.Cur_Code.choices[cur_index][1],
                                Format          = "pdf"
                                ))
        if     form.submit_XLS.data:
            return redirect(url_for('.export_Billing_Resume',
                                Cus_Id          = form.Cus_Id.data,
                                Cus_Name        = form.Cus_Id.choices[cus_index][1],
                                CIT_Date_From   = form.CIT_Date_From.data,
                                CIT_Date_To     = form.CIT_Date_To.data,
                                CIT_Status      = form.CIT_Status.data,
                                CIT_Status_Value= form.CIT_Status.choices[form.CIT_Status.data][1],
                                Cur_Code        = form.Cur_Code.data,
                                Cur_Name        = form.Cur_Code.choices[cur_index][1],
                                Format          = "xlsx"
                                ))
        if     form.submit_CSV.data:
            return redirect(url_for('.export_Billing_Resume',
                                Cus_Id          = form.Cus_Id.data,
                                Cus_Name        = form.Cus_Id.choices[cus_index][1],
                                CIT_Date_From   = form.CIT_Date_From.data,
                                CIT_Date_To     = form.CIT_Date_To.data,
                                CIT_Status      = form.CIT_Status.data,
                                CIT_Status_Value= form.CIT_Status.choices[form.CIT_Status.data][1],
                                Cur_Code        = form.Cur_Code.data,
                                Cur_Name        = form.Cur_Code.choices[cur_index][1],
                                Format          = "csv"
                                ))
        if     form.submit_JSON.data:
            return redirect(url_for('.export_Billing_Resume',
                                Cus_Id          = form.Cus_Id.data,
                                Cus_Name        = form.Cus_Id.choices[cus_index][1],
                                CIT_Date_From   = form.CIT_Date_From.data,
                                CIT_Date_To     = form.CIT_Date_To.data,
                                CIT_Status      = form.CIT_Status.data,
                                CIT_Status_Value= form.CIT_Status.choices[form.CIT_Status.data][1],
                                Cur_Code        = form.Cur_Code.data,
                                Cur_Name        = form.Cur_Code.choices[cur_index][1],
                                Format          = "json"
                                ))
        if     form.submit_FIX.data:
            return redirect(url_for('.export_Billing_Resume',
                                Cus_Id          = form.Cus_Id.data,
                                Cus_Name        = form.Cus_Id.choices[cus_index][1],
                                CIT_Date_From   = form.CIT_Date_From.data,
                                CIT_Date_To     = form.CIT_Date_To.data,
                                CIT_Status      = form.CIT_Status.data,
                                CIT_Status_Value= form.CIT_Status.choices[form.CIT_Status.data][1],
                                Cur_Code        = form.Cur_Code.data,
                                Cur_Name        = form.Cur_Code.choices[cur_index][1],
                                Format          = "fix"
                                ))

        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Report discarded ...')
        else:
            print('form validated but not submited ???')
        #return redirect(url_for('.export_Billing_Resume'))
        return redirect(url_for('.index'))

    form.Cus_Id.data        = session['data']['Cus_Id']
    form.CIT_Date_From.data = session['data']['CIT_Date_From']
    form.CIT_Date_To.data   = session['data']['CIT_Date_To']
    form.CIT_Status.data    = session['data']['CIT_Status']
    form.Cur_Code.data      = session['data']['Cur_Code']

    return render_template('export_billing_resume.html',form=form, data=session.get('data'))

# =============================================================================
from pandas.io.json             import json_normalize
import simplejson as json
import pandas
from reportlab.lib.pagesizes    import letter
from reportlab.pdfgen           import canvas
from reportlab.lib.utils        import ImageReader

def export_to_pdf(output_file,rows,Customer,From,To,Status,Currency):

    from reportlab.lib.pagesizes    import letter
    from reportlab.pdfgen           import canvas
    
    pdf_file    ="%s/%s"%(current_app.root_path,url_for('static',filename='tmp/%s'%(output_file)))
    logo_file   ="%s/%s"%(current_app.root_path,url_for('static',filename='img/logo_emtec.png'))

    canvas = canvas.Canvas(pdf_file, pagesize=letter)
    canvas.setLineWidth(.3)
    canvas.setFont('Helvetica', 12)
  
    h               = 630
    print_header    = True
    page            = 0
    count           = 0
    sum_CI          = 0
    sum_total       = 0
    previo_CI       = ''
    is_first        = True
    
    logo = ImageReader(logo_file)

    for row in rows:
        if print_header:
            page = page +1
            canvas.drawString   ( 30,750,'BILLING RESUME')
            canvas.drawString   (250,750,'SERTECHNO.COM' )
            canvas.drawString   (520,750,'PAGE:'        )
            canvas.drawString   (560,750,'%3d'%(page)   )

            canvas.rect         ( 20, 30,560,710)

            canvas.drawString   ( 30,720,'CUSTOMER:'    )
            canvas.drawString   (120,720,Customer       )
            
            canvas.drawImage(logo, 350, 660, mask='auto')
            
            canvas.drawString   ( 30,705,'FROM    :'    )
            canvas.drawString   (120,705,From)
            canvas.drawString   ( 30,690,'TO      :'    )
            canvas.drawString   (120,690,To)
            canvas.drawString   ( 30,675,'STATUS  :'    )
            canvas.drawString   (120,675,Status)
            canvas.drawString   ( 30,660,'CURRENCY:'    )
            canvas.drawString   (120,660,Currency       )

            canvas.line         ( 20,645,580,645)
            h       = 630
            canvas.drawString        ( 30,h, "ITEMS"         )
            canvas.drawString        ( 80,h, "CU"            )
            canvas.drawRightString   (280,h, "PRICE"         )
            canvas.drawRightString   (350,h, "Q"             )
            canvas.drawRightString   (410,h, "SUBTOT"        )
            canvas.drawRightString   (490,h, "XR"            )
            canvas.drawRightString   (570,h, "TOTAL"         )
            canvas.line         ( 20,615,580,615        )

            h       = 600

            print_header = False

        if row.CI_ID != previo_CI:
            if is_first == False:
                canvas.drawRightString   (570,h, "%12.2f"    % ( sum_CI  )   )
                h -= 15
            canvas.drawString   ( 30,h, "CI : %s"  % ( row.CI           )   )
            previo_CI=row.CI_ID
            sum_CI = 0
            h -= 15

        if h < 70:
            print_header = True
            canvas.line         ( 20,30,580,30)
            canvas.showPage()
            
        canvas.drawCentredString ( 30,h, "%3d"       % ( row.ITEMS           )   )
        canvas.drawString        ( 80,h, "%s"        % ( row.CU              )   )
        canvas.drawRightString   (280,h, "%12.2f"    % ( row.RATE_PRICE      )   )
        canvas.drawRightString   (350,h, "%12.2f"    % ( row.Q               )   )
        canvas.drawRightString   (410,h, "%12.2f"    % ( row.ST_AT_RATE      )   )
        canvas.drawRightString   (490,h, "%20.6f"    % ( row.BILLXR          )   )
        canvas.drawRightString   (570,h, "%12.2f"    % ( row.TOTAL_BILL_CUR  )   )
        sum_CI      += row.TOTAL_BILL_CUR
        sum_total   += row.TOTAL_BILL_CUR
        is_first = False
        
        count   +=  1
        h       -=  15
        if h < 70:
            print_header = True
            canvas.showPage()
            
    h -= 15

    canvas.drawRightString   (570,h, "%12.2f"    % ( sum_CI  )   )
    canvas.drawRightString   (570,h-15, "%12.2f"    % ( sum_total  )   )

    canvas.drawString   ( 30 ,h,'RECORDS :')
    canvas.drawRightString   (120 ,h,"%04d"%( count ) )
 
    canvas.save()


def export_to_xls(output_file,rows,Customer,From,To,Status,Currency):
    json_file="%s.json"%(output_file)
    export_to_json(json_file,rows,Customer,From,To,Status,Currency)
    
    json_file   ="%s/%s"%(current_app.root_path, url_for('static',filename='tmp/%s.json'%(output_file)))
    
    with open(json_file) as data_file:    
        d= json.load(data_file)  

    df1 = json_normalize(d, 'detail').assign(**d['header'])
        
    xlsx_file="%s/%s"%(current_app.root_path,url_for('static',filename='tmp/%s'%(output_file)))
    
    df1.to_excel(xlsx_file,'Sheet 1')    

def export_to_csv(output_file,rows,Customer,From,To,Status,Currency):
    cvs_file="%s/%s"%(current_app.root_path,url_for('static',filename='tmp/%s'%(output_file)))
    f=open(cvs_file,"w")

    f.write("H,Customer,From,To,Status,Currency\n")
    f.write("H,%s,%s,%s,%s,%s\n"%(Customer,From,To,Status,Currency))
    f.write("D,Records,CU,Rate,Q,Subtotal,XR,Total\n")
    count = 0
    for row in rows:
        f.write("D,%s,%s,%s,%s,%s,%s,%s\n"%(row.ITEMS,row.CU,row.RATE_PRICE,row.Q,row.ST_AT_RATE,row.BILLXR,row.TOTAL_BILL_CUR))
        count += 1
    f.write("T,%d\n"%(count))
    f.close()


def export_to_json(output_file,rows,Customer,From,To,Status,Currency):
    json_file="%s/%s"%(current_app.root_path,url_for('static',filename='tmp/%s'%(output_file)))
    f=open(json_file,"w")
    
    dict = {}
    dict.update({'header':{}})
    dict['header'].update({'customer':Customer})
    dict['header'].update({'from':From})
    dict['header'].update({'to':To})
    dict['header'].update({'status':Status})
    dict['header'].update({'currency':Currency})
    dict.update({'detail':[]})
    count = 0
    for row in rows:
        dict['detail'].append({})
        dict['detail'][count].update( {    'items':row.ITEMS, 'cu':row.CU, 'price':row.RATE_PRICE, 'q':row.Q, 'subtotal':row.ST_AT_RATE,\
                                    'xr':row.BILLXR, 'total':row.TOTAL_BILL_CUR \
                                })
        count += 1
    dict['header'].update({'count':count})
    jsonarray = json.dumps(dict)
    
    f.write(jsonarray)

    f.close()

def export_to_fix(output_file,rows,Customer,From,To,Status,Currency):
    fix_file="%s/%s"%(current_app.root_path,url_for('static',filename='tmp/%s'%(output_file)))

    f=open(fix_file,"w")

    f.write("H%06d%-45s%-10s%-10s%-45s%-45s*\n"%(0,Customer,From,To,Status,Currency))
    count = 0
    for row in rows:
        f.write("D%06d%-45s%020.6f%020.6f%020.6f%020.6f%020.6f%010d*\n"%(row.ITEMS,row.CU,row.RATE_PRICE,row.Q,row.ST_AT_RATE,row.BILLXR,row.TOTAL_BILL_CUR,0))
        count += 1
    f.write("T%06d%0155d*\n"%(count,0))
    f.close()

import simplejson as json

@main.route('/export/Billing_Resume', methods=['GET','POST'])
@login_required
def export_Billing_Resume():
    logger.debug('Enter: Export_Billing_Resume()')
    Cus_Id          =  request.args.get('Cus_Id',None,type=int)
    Cus_Name        =  request.args.get('Cus_Name',None,type=str)
    CIT_Date_From   =  request.args.get('CIT_Date_From',None,type=str)
    CIT_Date_To     =  request.args.get('CIT_Date_To',None,type=str)
    CIT_Status      =  request.args.get('CIT_Status',None,type=int)
    CIT_Status_Value=  request.args.get('CIT_Status_Value',None,type=str)
    Cur_Code        =  request.args.get('Cur_Code',None,type=str)
    Cur_Name        =  request.args.get('Cur_Name',None,type=str)
    Format          =  request.args.get('Format',None,type=str)
    # Get Actual Data from Database
    # NOTE: Here needs some Sand-Clock Message or something in case it takes so long ...
    query="CALL Get_Billing_Resume(%d,'%s','%s',%d,'%s')"%(Cus_Id,CIT_Date_From,CIT_Date_To,CIT_Status,Cur_Code)
    
    rows =  db.engine.execute(query).fetchall()

    # Aqui hace la conversion 
    output_file = "Billing_Resume_%d_%s_%s_%s.%s"%(Cus_Id,CIT_Date_From,CIT_Date_To,CIT_Status,Format)
    if      Format == 'pdf':
        export_to_pdf(output_file,rows,Cus_Name,CIT_Date_From,CIT_Date_To,CIT_Status_Value,Cur_Name)
    elif    Format == 'xlsx':
        export_to_xls(output_file,rows,Cus_Name,CIT_Date_From,CIT_Date_To,CIT_Status_Value,Cur_Name)
    elif    Format == 'csv':
        export_to_csv(output_file,rows,Cus_Name,CIT_Date_From,CIT_Date_To,CIT_Status_Value,Cur_Name)
    elif    Format == 'json':
        export_to_json(output_file,rows,Cus_Name,CIT_Date_From,CIT_Date_To,CIT_Status_Value,Cur_Name)
    elif    Format == 'fix':
        export_to_fix(output_file,rows,Cus_Name,CIT_Date_From,CIT_Date_To,CIT_Status_Value,Cur_Name)
    else:
        pass    
    
    # Aqui debe enviar el archivo a la PC
    #return ("<H1>Envio archivo %s a la PC</H1>"%(output_file_name))
    
    href = url_for('static',filename="tmp/%s"%output_file)
    
    return render_template('report_export_billing_resume.html',output_file=output_file,href=href)

# =============================================================================
# View for Get Billing Resume fro DB
# (c) Sertechno 2018
# GLVH @ 2018-11-11
# =============================================================================

from ..models       import frm_export_Charging_Resume
from babel.numbers  import format_number, format_decimal, format_percent

@main.route('/forms/Export_Charging_Resume', methods=['GET', 'POST'])
@login_required
def forms_Export_Charging_Resume():
    logger.debug('Enter: forms_Export_Charging_Resume()'%())

    session['data'] =  { 'Cus_Id': None, 'CIT_Date_From':None, 'CIT_Date_To':None, 'CIT_Status':1,'Cur_Code':'USD'}

    form = frm_export_Charging_Resume()

    query = "SELECT COUNT(*) AS RECORDS,Cus_Id,CR_Date_From,CR_Date_To,CIT_Status,Cur_Code,Cus_Name FROM Charge_Resumes "\
                "GROUP BY Cus_Id,CR_Date_From,CR_Date_To,CIT_Status,Cur_Code,Cus_Name "\
                "ORDER BY Cus_Name,CR_Date_From,CR_Date_To,CIT_Status,Cur_Code"
                
    rows=db.engine.execute(query).fetchall()

    # Load Statuses
    statuses=cit_status.query.all()
    dstatuses={}
    for s in statuses:
        dstatuses[s.CIT_Status]=s.Value
        
    currencies=currency.query.all()
    dcurrencies={}
    for c in currencies:
        dcurrencies[c.Cur_Code]=c.Cur_Name
    
    #print("statuses",statuses)
    #print("currencies",currencies)
    #print("dstatuses",dstatuses)
    #print("dcurrencies",dcurrencies)
    
    
    # Load Currency Names


    export_choices = []
    for row in rows:
        option="%s_%s_%s_%s_%s_%s"%(row.Cus_Id,row.CR_Date_From,row.CR_Date_To,row.CIT_Status,row.Cur_Code,row.Cus_Name)
        print("option split=",option.split("_"))
        value ="%s from %s to %s status=%s currency=%s"%(row.Cus_Name,row.CR_Date_From,row.CR_Date_To,dstatuses[row.CIT_Status],dcurrencies[row.Cur_Code])
        export_choices.append((option,value))
     
     
       

    #print("export_choices=",export_choices)



    # Will setup filter to consider only Currencies with actual Exchange Rates in DB
    # Prepare query
    #query = db.session.query(exchange_rate.Cur_Code.distinct().label('Cur_Code'))
    # Execute query an conver in list for further use in choices selection
    #export_choices = [row.Cur_Code for row in query.all()]

    form.Export.choices   = export_choices

    if form.validate_on_submit():

        data=form.Export.data.split("_")
        print("data=",data)
        if     form.submit_PDF.data:
            return redirect(url_for('.export_Charging_Resume',
                                Cus_Id          = data[0],
                                Cus_Name        = data[5],
                                CIT_Date_From   = data[1],
                                CIT_Date_To     = data[2],
                                CIT_Status      = data[3],
                                CIT_Status_Value= dstatuses[int(data[3])],
                                Cur_Code        = data[4],
                                Cur_Name        = dcurrencies[data[4]],
                                Format          = "pdf"
                                ))
        if     form.submit_XLS.data:
            return redirect(url_for('.export_Charging_Resume',
                                Cus_Id          = data[0],
                                Cus_Name        = data[5],
                                CIT_Date_From   = data[1],
                                CIT_Date_To     = data[2],
                                CIT_Status      = data[3],
                                CIT_Status_Value= dstatuses[int(data[3])],
                                Cur_Code        = data[4],
                                Cur_Name        = dcurrencies[data[4]],
                                Format          = "xlsx"
                                ))
        if     form.submit_CSV.data:
            return redirect(url_for('.export_Charging_Resume',
                                Cus_Id          = data[0],
                                Cus_Name        = data[5],
                                CIT_Date_From   = data[1],
                                CIT_Date_To     = data[2],
                                CIT_Status      = data[3],
                                CIT_Status_Value= dstatuses[int(data[3])],
                                Cur_Code        = data[4],
                                Cur_Name        = dcurrencies[data[4]],
                                Format          = "csv"
                                ))
        if     form.submit_JSON.data:
            return redirect(url_for('.export_Charging_Resume',
                                Cus_Id          = data[0],
                                Cus_Name        = data[5],
                                CIT_Date_From   = data[1],
                                CIT_Date_To     = data[2],
                                CIT_Status      = data[3],
                                CIT_Status_Value= dstatuses[int(data[3])],
                                Cur_Code        = data[4],
                                Cur_Name        = dcurrencies[data[4]],
                                Format          = "json"
                                ))
        if     form.submit_FIX.data:
            return redirect(url_for('.export_Charging_Resume',
                                Cus_Id          = data[0],
                                Cus_Name        = data[5],
                                CIT_Date_From   = data[1],
                                CIT_Date_To     = data[2],
                                CIT_Status      = data[3],
                                CIT_Status_Value= dstatuses[int(data[3])],
                                Cur_Code        = data[4],
                                Cur_Name        = dcurrencies[data[4]],
                                Format          = "fix"
                                ))

        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Report discarded ...')
        else:
            print('form validated but not submited ???')
        return redirect(url_for('.index'))


    return render_template('export_charging_resume.html',form=form)

# =============================================================================
from pandas.io.json             import json_normalize
import simplejson as json
import pandas
from reportlab.lib.pagesizes    import letter
from reportlab.pdfgen           import canvas
from reportlab.lib.utils        import ImageReader

def export_to_pdf(output_file,rows,Customer,From,To,Status,Currency):

    from reportlab.lib.pagesizes    import letter
    from reportlab.pdfgen           import canvas
    
    pdf_file    ="%s/%s"%(current_app.root_path,url_for('static',filename='tmp/%s'%(output_file)))
    logo_file   ="%s/%s"%(current_app.root_path,url_for('static',filename='img/logo_emtec.png'))

    canvas = canvas.Canvas(pdf_file, pagesize=letter)
    canvas.setLineWidth(.3)
    canvas.setFont('Helvetica', 12)
  
    h               = 630
    print_header    = True
    page            = 0
    count           = 0
    sum_CI          = 0
    sum_total       = 0
    previo_CI       = ''
    is_first        = True
    
    logo = ImageReader(logo_file)

    for row in rows:
        if print_header:
            page = page +1
            canvas.drawString   ( 30,750,'BILLING RESUME')
            canvas.drawString   (250,750,'SERTECHNO.COM' )
            canvas.drawString   (520,750,'PAGE:'        )
            canvas.drawString   (560,750,'%3d'%(page)   )

            canvas.rect         ( 20, 30,560,710)

            canvas.drawString   ( 30,720,'CUSTOMER:'    )
            canvas.drawString   (120,720,Customer       )
            
            canvas.drawImage(logo, 350, 660, mask='auto')
            
            canvas.drawString   ( 30,705,'FROM    :'    )
            canvas.drawString   (120,705,From)
            canvas.drawString   ( 30,690,'TO      :'    )
            canvas.drawString   (120,690,To)
            canvas.drawString   ( 30,675,'STATUS  :'    )
            canvas.drawString   (120,675,Status)
            canvas.drawString   ( 30,660,'CURRENCY:'    )
            canvas.drawString   (120,660,Currency       )

            canvas.line         ( 20,645,580,645)
            h       = 630
            canvas.drawString        ( 30,h, "ITEMS"         )
            canvas.drawString        ( 80,h, "CU"            )
            canvas.drawRightString   (280,h, "PRICE"         )
            canvas.drawRightString   (350,h, "Q"             )
            canvas.drawRightString   (410,h, "SUBTOT"        )
            canvas.drawRightString   (490,h, "XR"            )
            canvas.drawRightString   (570,h, "TOTAL"         )
            canvas.line         ( 20,615,580,615        )

            h       = 600

            print_header = False

        if row.CI_Id != previo_CI:
            if is_first == False:
                canvas.drawRightString   (570,h, "%12.2f"    % ( sum_CI  )   )
                h -= 15
            canvas.drawString   ( 30,h, "CI : %s"  % ( row.CI_Name           )   )
            previo_CI=row.CI_Id
            sum_CI = 0
            h -= 15

        if h < 70:
            print_header = True
            canvas.line         ( 20,30,580,30)
            canvas.showPage()
            
        canvas.drawCentredString ( 30,h, "%3d"       % ( row.CIT_Count          )   )
        canvas.drawString        ( 80,h, "%s"        % ( row.CU_Description     )   )
        canvas.drawRightString   (280,h, "%12.2f"    % ( row.Rat_Price          )   )
        canvas.drawRightString   (350,h, "%12.2f"    % ( row.CR_Quantity        )   )
        canvas.drawRightString   (410,h, "%12.2f"    % ( row.CR_ST_at_Rate_Cur  )   )
        canvas.drawRightString   (490,h, "%20.6f"    % ( row.CR_Cur_XR          )   )
        canvas.drawRightString   (570,h, "%12.2f"    % ( row.CR_ST_at_Cur       )   )
        sum_CI      += row.CR_ST_at_Cur
        sum_total   += row.CR_ST_at_Cur
        is_first = False
        
        count   +=  1
        h       -=  15
        if h < 70:
            print_header = True
            canvas.showPage()
            
    h -= 15

    canvas.drawRightString   (570,h, "%12.2f"    % ( sum_CI  )   )
    canvas.drawRightString   (570,h-15, "%12.2f"    % ( sum_total  )   )

    canvas.drawString   ( 30 ,h,'RECORDS :')
    canvas.drawRightString   (120 ,h,"%04d"%( count ) )
 
    canvas.save()
    return pdf_file


def export_to_xls(output_file,rows,Customer,From,To,Status,Currency):
    json_file="%s.json"%(output_file)
    export_to_json(json_file,rows,Customer,From,To,Status,Currency)
    
    json_file   ="%s%s"%(current_app.root_path, url_for('static',filename='tmp/%s.json'%(output_file)))
    
    with open(json_file) as data_file:    
        d= json.load(data_file)  

    df1 = json_normalize(d, 'detail').assign(**d['header'])
        
    xlsx_file="%s/%s"%(current_app.root_path,url_for('static',filename='tmp/%s'%(output_file)))
    
    df1.to_excel(xlsx_file,'Sheet 1')
    
    print("%s: output_file = %s"%('export_to_xlsx',output_file))
    print("%s: json_file   = %s"%('export_to_xlsx',json_file))
    print("%s: xlsx_file   = %s"%('export_to_xlsx',xlsx_file))
       
    return xlsx_file    

def export_to_csv(output_file,rows,Customer,From,To,Status,Currency):
    cvs_file="%s/%s"%(current_app.root_path,url_for('static',filename='tmp/%s'%(output_file)))
    f=open(cvs_file,"w")

    f.write("H,Customer,From,To,Status,Currency\n")
    f.write("H,%s,%s,%s,%s,%s\n"%(Customer,From,To,Status,Currency))
    f.write("D,Records,CU,Rate,Q,Subtotal,XR,Total\n")
    count = 0
    for row in rows:
        f.write ("D,%s,%s,%s,%s,%s,%s,%s\n"%\
                    (row.CIT_Count, row.CU_Description, row.Rat_Price, row.CR_Quantity, row.CR_ST_at_Rate_Cur, row.CR_Cur_XR,row.CR_ST_at_Cur)\
                )
        count += 1
    f.write("T,%d\n"%(count))
    f.close()
    return cvs_file
    
"""
        canvas.drawCentredString ( 30,h, "%3d"       % ( row.CIT_Count          )   )
        canvas.drawString        ( 80,h, "%s"        % ( row.CU_Description     )   )
        canvas.drawRightString   (280,h, "%12.2f"    % ( row.Rat_Price          )   )
        canvas.drawRightString   (350,h, "%12.2f"    % ( row.CR_Quantity        )   )
        canvas.drawRightString   (410,h, "%12.2f"    % ( row.CR_ST_at_Rate_Cur  )   )
        canvas.drawRightString   (490,h, "%20.6f"    % ( row.CR_Cur_XR          )   )
        canvas.drawRightString   (570,h, "%12.2f"    % ( row.CR_ST_at_Cur       )   )    
"""    
    

def export_to_json(output_file,rows,Customer,From,To,Status,Currency):
    json_file="%s/%s"%(current_app.root_path,url_for('static',filename='tmp/%s'%(output_file)))
    f=open(json_file,"w")
    
    dict = {}
    dict.update({'header':{}})
    dict['header'].update({'customer':Customer})
    dict['header'].update({'from':From})
    dict['header'].update({'to':To})
    dict['header'].update({'status':Status})
    dict['header'].update({'currency':Currency})
    dict.update({'detail':[]})
    count = 0
    for row in rows:
        dict['detail'].append({})
        dict['detail'][count].update( {    'items':row.CIT_Count, 'cu':row.CU_Description, 'price':row.Rat_Price, \
                                        'q':row.CR_Quantity, 'subtotal':row.CR_ST_at_Rate_Cur,\
                                        'xr':row.CR_Cur_XR, 'total':row.CR_ST_at_Cur \
                                })
        count += 1
    dict['header'].update({'count':count})
    jsonarray = json.dumps(dict)
    
    f.write(jsonarray)

    f.close()
    return json_file

def export_to_fix(output_file,rows,Customer,From,To,Status,Currency):
    fix_file="%s/%s"%(current_app.root_path,url_for('static',filename='tmp/%s'%(output_file)))

    f=open(fix_file,"w")

    f.write("H%06d%-45s%-10s%-10s%-45s%-45s*\n"%(0,Customer,From,To,Status,Currency))
    count = 0
    for row in rows:
        f.write ("D%06d%-45s%020.6f%020.6f%020.6f%020.6f%020.6f%010d*\n"%\
                    (row.CIT_Count, row.CU_Description, row.Rat_Price, row.CR_Quantity,row.CR_ST_at_Rate_Cur,row.CR_Cur_XR,row.CR_ST_at_Cur,0)\
                )
        count += 1
    f.write("T%06d%0155d*\n"%(count,0))
    f.close()
    return fix_file

import simplejson as json
from flask import send_file

@main.route('/export/Charging_Resume', methods=['GET','POST'])
@login_required
def export_Charging_Resume():
    logger.debug('Enter: Export_Charging_Resume()')
    Cus_Id          =  request.args.get('Cus_Id',None,type=int)
    Cus_Name        =  request.args.get('Cus_Name',None,type=str)
    CIT_Date_From   =  request.args.get('CIT_Date_From',None,type=str)
    CIT_Date_To     =  request.args.get('CIT_Date_To',None,type=str)
    CIT_Status      =  request.args.get('CIT_Status',None,type=int)
    CIT_Status_Value=  request.args.get('CIT_Status_Value',None,type=str)
    Cur_Code        =  request.args.get('Cur_Code',None,type=str)
    Cur_Name        =  request.args.get('Cur_Name',None,type=str)
    Format          =  request.args.get('Format',None,type=str)
    # Get Actual Data from Database
    # NOTE: Here needs some Sand-Clock Message or something in case it takes so long ...
    query="CALL Get_Charge_Resume(%d,'%s','%s',%d,'%s')"%(Cus_Id,CIT_Date_From,CIT_Date_To,CIT_Status,Cur_Code)
    
    rows =  db.engine.execute(query).fetchall()

    # Aqui hace la conversion 
    output_file = "CR_%d_%s_%s_%s_%s.%s"%(Cus_Id,CIT_Date_From,CIT_Date_To,CIT_Status,Cur_Code,Format)
    if      Format == 'pdf':
        return_file=export_to_pdf(output_file,rows,Cus_Name,CIT_Date_From,CIT_Date_To,CIT_Status_Value,Cur_Name)
    elif    Format == 'xlsx':
        return_file=export_to_xls(output_file,rows,Cus_Name,CIT_Date_From,CIT_Date_To,CIT_Status_Value,Cur_Name)
    elif    Format == 'csv':
        return_file=export_to_csv(output_file,rows,Cus_Name,CIT_Date_From,CIT_Date_To,CIT_Status_Value,Cur_Name)
    elif    Format == 'json':
        return_file=export_to_json(output_file,rows,Cus_Name,CIT_Date_From,CIT_Date_To,CIT_Status_Value,Cur_Name)
    elif    Format == 'fix':
        return_file=export_to_fix(output_file,rows,Cus_Name,CIT_Date_From,CIT_Date_To,CIT_Status_Value,Cur_Name)
    else:
        pass    
    
    # Aqui debe enviar el archivo a la PC
    print("%s: return_file   = %s"%('export_Charging_Resume',return_file))
    print("%s: att name      = %s"%('export_Charging_Resume',output_file))
    return send_file(return_file,as_attachment=True,attachment_filename=output_file)

