from time           import strftime
from datetime       import datetime                         
from sqlalchemy     import exc
from flask          import render_template, session, redirect, url_for, current_app, flash
from flask          import request
from flask          import Markup
from flask_login    import login_required
from flask_login    import current_user
#from ..email import send_email

from .              import main

from ..             import db
from ..             import logger

from ..decorators   import admin_required, permission_required

#from ..models       import User
#from ..models       import Permission

from emtec.collector.db.Flask_models       import User
from emtec.collector.db.Flask_models       import Permission

""" Application decorators for routes """
""" Decorators specify main routes to be handled by Collector Solution """

@main.route('/', methods=['GET', 'POST'])
def index():
    
    # Espera a capitulo 3 para mejorar procedimiento de respuesta, hard coding mucho aqui

    data =  {   "name":current_app.name,
                #"app_name":C.app_name,
                "app_name":current_app.name,
                "date_time":strftime('%Y-%m-%d %H:%M:%S'),
                "user_agent":request.headers.get('User-Agent'),
                #"current_time":datetime.utcnow(),
                "db":db,
                "logger":logger,
                #"C":C,
                "current_app.logger":current_app.logger
            }
    name = None
    return render_template('collector.html',data=data)


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


@main.route('/collector_faq', methods=['GET','POST'])
def collector_faq():   
    return render_template('collector_faq.html')

@main.route('/collector_about', methods=['GET','POST'])
def collector_about():   
    return render_template('collector_about.html')

# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-18 18:05:34
# =============================================================================

from emtec.collector.db.Flask_models import cit_generation
from emtec.collector.forms  import frm_cit_generation,frm_cit_generation_delete
from emtec.collector.db.Flask_models import cit_status
from emtec.collector.forms  import frm_cit_status,frm_cit_status_delete
from emtec.collector.db.Flask_models import cu_operation
from emtec.collector.forms  import frm_cu_operation,frm_cu_operation_delete
from emtec.collector.db.Flask_models import cu_type
from emtec.collector.forms  import frm_cu_type,frm_cu_type_delete
from emtec.collector.db.Flask_models import charge_item
from emtec.collector.forms  import frm_charge_item,frm_charge_item_delete
from emtec.collector.db.Flask_models import charge_resume
from emtec.collector.forms  import frm_charge_resume,frm_charge_resume_delete
from emtec.collector.db.Flask_models import charge_unit
from emtec.collector.forms  import frm_charge_unit,frm_charge_unit_delete
from emtec.collector.db.Flask_models import configuration_item
from emtec.collector.forms  import frm_configuration_item,frm_configuration_item_delete
from emtec.collector.db.Flask_models import cost_center
from emtec.collector.forms  import frm_cost_center,frm_cost_center_delete
from emtec.collector.db.Flask_models import country
from emtec.collector.forms  import frm_country,frm_country_delete
from emtec.collector.db.Flask_models import country_currency
from emtec.collector.forms  import frm_country_currency,frm_country_currency_delete
from emtec.collector.db.Flask_models import currency
from emtec.collector.forms  import frm_currency,frm_currency_delete
from emtec.collector.db.Flask_models import customer
from emtec.collector.forms  import frm_customer,frm_customer_delete
from emtec.collector.db.Flask_models import dev_form
from emtec.collector.forms  import frm_dev_form,frm_dev_form_delete
from emtec.collector.db.Flask_models import dev_table
from emtec.collector.forms  import frm_dev_table,frm_dev_table_delete
from emtec.collector.db.Flask_models import exchange_rate
from emtec.collector.forms  import frm_exchange_rate,frm_exchange_rate_delete
from emtec.collector.db.Flask_models import measure_unit
from emtec.collector.forms  import frm_measure_unit,frm_measure_unit_delete
from emtec.collector.db.Flask_models import platform
from emtec.collector.forms  import frm_platform,frm_platform_delete
from emtec.collector.db.Flask_models import rat_period
from emtec.collector.forms  import frm_rat_period,frm_rat_period_delete
from emtec.collector.db.Flask_models import rate
from emtec.collector.forms  import frm_rate,frm_rate_delete
from emtec.collector.db.Flask_models import Role
from emtec.collector.forms  import frm_Role,frm_Role_delete
from emtec.collector.db.Flask_models import st_use_per_cu
from emtec.collector.forms  import frm_st_use_per_cu,frm_st_use_per_cu_delete
from emtec.collector.db.Flask_models import st_use_per_type
from emtec.collector.forms  import frm_st_use_per_type,frm_st_use_per_type_delete
from emtec.collector.db.Flask_models import trace
from emtec.collector.forms  import frm_trace,frm_trace_delete
from emtec.collector.db.Flask_models import User
from emtec.collector.forms  import frm_User,frm_User_delete

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
# GLVH @ 2019-08-18 18:05:34
# =============================================================================

@main.route('/forms/Charge_Items', methods=['GET', 'POST'])
@login_required
@admin_required
def forms_Charge_Items():
    """ Form handling function for table Charge_Items """

    logger.debug('Enter: forms_Charge_Items()')
    CU_Id  =  request.args.get('CU_Id',0,type=int)
    CIT_DateTime  =  request.args.get('CIT_DateTime',0,type=int)
    parent_key  =  request.args.get('parent_key',None,type=str)
    parent_value=  request.args.get('parent_value',0,type=int)

    row =  charge_item.query.filter(charge_item.CU_Id == CU_Id,charge_item.CIT_DateTime == CIT_DateTime).first()
    if row is None:
        row=charge_item()
        session['is_new_row']=True

    session['data'] =  { 'CU_Id':row.CU_Id, 'CIT_Date':row.CIT_Date, 'CIT_Time':str(row.CIT_Time), 'CIT_Quantity':row.CIT_Quantity, 'CIT_Status':row.CIT_Status, 'CIT_Is_Active':row.CIT_Is_Active, 'CIT_DateTime':row.CIT_DateTime}
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
        if     form.submit_Save.data and current_user.role_id>1:
            row.CU_Id = form.CU_Id.data
            row.CIT_Date = form.CIT_Date.data
            row.CIT_Time = form.CIT_Time.data
            row.CIT_Quantity = form.CIT_Quantity.data
            row.CIT_Status = form.CIT_Status.data
            row.CIT_Is_Active = form.CIT_Is_Active.data
            try:
               session['new_row']=str(row)
               db.session.close()
               db.session.add(row)
               db.session.commit()
               if session['is_new_row']==True:
                   logger.audit ( '%s:NEW:%s' % (current_user.username,session['new_row'] ) )
                   flash('New Charge Item created OK')
               else:
                   logger.audit ( '%s:OLD:%s' % (current_user.username,session['prev_row']) )
                   logger.audit ( '%s:UPD:%s' % (current_user.username,session['new_row'] ) )
                   message=Markup('<b>Charge Item %s saved OK</b>'%(CU_Id,CIT_DateTime))
                   flash(message)
               db.session.close()
            except Exception as e:
               db.session.rollback()
               db.session.close()
               message=Markup('ERROR saving Charge Item record : %s'%(e))
               flash(message)
            return redirect(url_for('.select_Charge_Items_query'))
        elif   form.submit_New.data and current_user.role_id>1:
            #print('New Data Here ...')
            session['is_new_row']=True
            db.session.close()
            row=charge_item()
            return redirect(url_for('.forms_Charge_Items'))

        elif   form.submit_Cancel.data:
            #print('Cancel Data Here ... does nothing')
            message=Markup('Charge Item Record modifications discarded ...')
            flash(message)
        else:
            #print('form validated but not submited ???')
            message=Markup('<b>Charge Item data modifications not allowed for user \'%s\'. Please contact Collector\'s Administrator ...</b>'%(current_user.username))
            flash(message)
            return redirect(url_for('.forms_Charge_Items'))

    form.CU_Id.data = row.CU_Id
    form.CIT_Date.data = row.CIT_Date
    form.CIT_Time.data = row.CIT_Time
    form.CIT_Quantity.data = row.CIT_Quantity
    form.CIT_Status.data = row.CIT_Status
    form.CIT_Is_Active.data = row.CIT_Is_Active
    session['prev_row']=str(row)
    session['is_new_row']=False
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
    CIT_DateTime  =  request.args.get('CIT_DateTime',0,type=int)
    row =  charge_item.query.filter(charge_item.CU_Id == CU_Id,charge_item.CIT_DateTime == CIT_DateTime).first()
    if row is None:
        row=charge_item()
    session['data'] =  { 'CU_Id':row.CU_Id, 'CIT_Date':row.CIT_Date, 'CIT_Time':str(row.CIT_Time), 'CIT_Quantity':row.CIT_Quantity, 'CIT_Status':row.CIT_Status, 'CIT_Is_Active':row.CIT_Is_Active, 'CIT_DateTime':row.CIT_DateTime}
    form = frm_charge_item_delete()

    if form.validate_on_submit():
        if  form.submit_Delete.data:
            print('Delete Data Here...')
            try:
                session['deleted_row']=str(row)
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                logger.audit ( '%s:DEL:%s' % (current_user.username,session['deleted_row']) )
                flash('Charge Item %s deleted OK'%(CU_Id,CIT_DateTime))
            except exc.IntegrityError as e:
                db.session.rollback()
                flash('INTEGRITY ERROR: Are you sure there are no dependant records in other tables?')
                return redirect(url_for('.forms_Charge_Items_delete',CU_Id=session['data']['CU_Id'],CIT_DateTime=session['data']['CIT_DateTime']))

            return redirect(url_for('.select_Charge_Items_query'))
        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
            return redirect(url_for('.select_Charge_Items_query'))
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.select_Charge_Items_query'))


    return render_template('charge_items_delete.html', form=form, data=session.get('data'),row=row)

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
        elif field == 'CIT_DateTime':
            rows =  charge_item.query.filter_by(CIT_DateTime=value)\
               .join(charge_unit,charge_item.CU_Id == charge_unit.CU_Id).add_columns(charge_unit.CU_Description)\
               .join(cit_status,charge_item.CIT_Status == cit_status.CIT_Status).add_columns(cit_status.Value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
    else:
       rows =  charge_item.query\
               .join(charge_unit,charge_item.CU_Id == charge_unit.CU_Id).add_columns(charge_unit.CU_Description)\
               .join(cit_status,charge_item.CIT_Status == cit_status.CIT_Status).add_columns(cit_status.Value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)

    if field is not None:
       next_url = url_for('.select_Charge_Items_query', field=field, value=value, page=rows.next_num) \
           if rows.has_next else None
       prev_url = url_for('.select_Charge_Items_query', field=field, value=value, page=rows.prev_num) \
           if rows.has_prev else None

    else:
       next_url = url_for('.select_Charge_Items_query', page=rows.next_num) \
           if rows.has_next else None
       prev_url = url_for('.select_Charge_Items_query', page=rows.prev_num) \
           if rows.has_prev else None

    return render_template('charge_items_All.html',rows=rows)
# =============================================================================
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-18 18:05:34
# =============================================================================

@main.route('/forms/Charge_Resumes', methods=['GET', 'POST'])
@login_required
def forms_Charge_Resumes():
    """ Form handling function for table Charge_Resumes """

    logger.debug('Enter: forms_Charge_Resumes()')
    Cus_Id  =  request.args.get('Cus_Id',0,type=int)
    CR_Date_From  =  request.args.get('CR_Date_From',0,type=int)
    CR_Date_To  =  request.args.get('CR_Date_To',0,type=int)
    CIT_Status  =  request.args.get('CIT_Status',0,type=int)
    Cur_Code  =  request.args.get('Cur_Code',0,type=int)
    CU_Id  =  request.args.get('CU_Id',0,type=int)
    row =  charge_resume.query.filter(charge_resume.Cus_Id == Cus_Id,charge_resume.CR_Date_From == CR_Date_From,charge_resume.CR_Date_To == CR_Date_To,charge_resume.CIT_Status == CIT_Status,charge_resume.Cur_Code == Cur_Code,charge_resume.CU_Id == CU_Id).first()
    if row is None:
        row=charge_resume()
        session['is_new_row']=True

    session['data'] =  { 'Cus_Id':row.Cus_Id, 'CR_Date_From':row.CR_Date_From, 'CR_Date_To':row.CR_Date_To, 'CIT_Status':row.CIT_Status, 'Cur_Code':row.Cur_Code, 'CIT_Count':row.CIT_Count, 'CIT_Quantity':row.CIT_Quantity, 'CIT_Generation':row.CIT_Generation, 'CU_Id':row.CU_Id, 'CI_CC_Id':row.CI_CC_Id, 'CU_Operation':row.CU_Operation, 'Typ_Code':row.Typ_Code, 'CC_Cur_Code':row.CC_Cur_Code, 'CI_Id':row.CI_Id, 'Rat_Id':row.Rat_Id, 'Rat_Price':row.Rat_Price, 'Rat_MU_Code':row.Rat_MU_Code, 'Rat_Cur_Code':row.Rat_Cur_Code, 'Rat_Period':row.Rat_Period, 'Rat_Hourly':row.Rat_Hourly, 'Rat_Daily':row.Rat_Daily, 'Rat_Monthly':row.Rat_Monthly, 'CR_Quantity':row.CR_Quantity, 'CR_Quantity_at_Rate':row.CR_Quantity_at_Rate, 'CC_XR':row.CC_XR, 'CR_Cur_XR':row.CR_Cur_XR, 'CR_ST_at_Rate_Cur':row.CR_ST_at_Rate_Cur, 'CR_ST_at_CC_Cur':row.CR_ST_at_CC_Cur, 'CR_ST_at_Cur':row.CR_ST_at_Cur, 'Cus_Name':row.Cus_Name, 'CI_Name':row.CI_Name, 'CU_Description':row.CU_Description, 'CC_Description':row.CC_Description, 'Rat_Period_Description':row.Rat_Period_Description, 'Pla_Id':row.Pla_Id}
    form = frm_charge_resume()

    if form.validate_on_submit():
        if     form.submit_Save.data and current_user.role_id>1:
            row.Cus_Id = form.Cus_Id.data
            row.CR_Date_From = form.CR_Date_From.data
            row.CR_Date_To = form.CR_Date_To.data
            row.CIT_Status = form.CIT_Status.data
            row.Cur_Code = form.Cur_Code.data
            row.CIT_Count = form.CIT_Count.data
            row.CIT_Quantity = form.CIT_Quantity.data
            row.CIT_Generation = form.CIT_Generation.data
            row.CU_Id = form.CU_Id.data
            row.CI_CC_Id = form.CI_CC_Id.data
            row.CU_Operation = form.CU_Operation.data
            row.Typ_Code = form.Typ_Code.data
            row.CC_Cur_Code = form.CC_Cur_Code.data
            row.CI_Id = form.CI_Id.data
            row.Rat_Id = form.Rat_Id.data
            row.Rat_Price = form.Rat_Price.data
            row.Rat_MU_Code = form.Rat_MU_Code.data
            row.Rat_Cur_Code = form.Rat_Cur_Code.data
            row.Rat_Period = form.Rat_Period.data
            row.Rat_Hourly = form.Rat_Hourly.data
            row.Rat_Daily = form.Rat_Daily.data
            row.Rat_Monthly = form.Rat_Monthly.data
            row.CR_Quantity = form.CR_Quantity.data
            row.CR_Quantity_at_Rate = form.CR_Quantity_at_Rate.data
            row.CC_XR = form.CC_XR.data
            row.CR_Cur_XR = form.CR_Cur_XR.data
            row.CR_ST_at_Rate_Cur = form.CR_ST_at_Rate_Cur.data
            row.CR_ST_at_CC_Cur = form.CR_ST_at_CC_Cur.data
            row.CR_ST_at_Cur = form.CR_ST_at_Cur.data
            row.Cus_Name = form.Cus_Name.data
            row.CI_Name = form.CI_Name.data
            row.CU_Description = form.CU_Description.data
            row.CC_Description = form.CC_Description.data
            row.Rat_Period_Description = form.Rat_Period_Description.data
            row.Pla_Id = form.Pla_Id.data
            try:
               session['new_row']=str(row)
               db.session.close()
               db.session.add(row)
               db.session.commit()
               if session['is_new_row']==True:
                   logger.audit ( '%s:NEW:%s' % (current_user.username,session['new_row'] ) )
                   flash('New Charge Resume created OK')
               else:
                   logger.audit ( '%s:OLD:%s' % (current_user.username,session['prev_row']) )
                   logger.audit ( '%s:UPD:%s' % (current_user.username,session['new_row'] ) )
                   message=Markup('<b>Charge Resume %s saved OK</b>'%(Cus_Id,CR_Date_From,CR_Date_To,CIT_Status,Cur_Code,CU_Id))
                   flash(message)
               db.session.close()
            except Exception as e:
               db.session.rollback()
               db.session.close()
               message=Markup('ERROR saving Charge Resume record : %s'%(e))
               flash(message)
            return redirect(url_for('.select_Charge_Resumes_query'))
        elif   form.submit_New.data and current_user.role_id>1:
            #print('New Data Here ...')
            session['is_new_row']=True
            db.session.close()
            row=charge_resume()
            return redirect(url_for('.forms_Charge_Resumes'))

        elif   form.submit_Cancel.data:
            #print('Cancel Data Here ... does nothing')
            message=Markup('Charge Resume Record modifications discarded ...')
            flash(message)
        else:
            #print('form validated but not submited ???')
            message=Markup('<b>Charge Resume data modifications not allowed for user \'%s\'. Please contact Collector\'s Administrator ...</b>'%(current_user.username))
            flash(message)
            return redirect(url_for('.forms_Charge_Resumes'))

    form.Cus_Id.data = row.Cus_Id
    form.CR_Date_From.data = row.CR_Date_From
    form.CR_Date_To.data = row.CR_Date_To
    form.CIT_Status.data = row.CIT_Status
    form.Cur_Code.data = row.Cur_Code
    form.CIT_Count.data = row.CIT_Count
    form.CIT_Quantity.data = row.CIT_Quantity
    form.CIT_Generation.data = row.CIT_Generation
    form.CU_Id.data = row.CU_Id
    form.CI_CC_Id.data = row.CI_CC_Id
    form.CU_Operation.data = row.CU_Operation
    form.Typ_Code.data = row.Typ_Code
    form.CC_Cur_Code.data = row.CC_Cur_Code
    form.CI_Id.data = row.CI_Id
    form.Rat_Id.data = row.Rat_Id
    form.Rat_Price.data = row.Rat_Price
    form.Rat_MU_Code.data = row.Rat_MU_Code
    form.Rat_Cur_Code.data = row.Rat_Cur_Code
    form.Rat_Period.data = row.Rat_Period
    form.Rat_Hourly.data = row.Rat_Hourly
    form.Rat_Daily.data = row.Rat_Daily
    form.Rat_Monthly.data = row.Rat_Monthly
    form.CR_Quantity.data = row.CR_Quantity
    form.CR_Quantity_at_Rate.data = row.CR_Quantity_at_Rate
    form.CC_XR.data = row.CC_XR
    form.CR_Cur_XR.data = row.CR_Cur_XR
    form.CR_ST_at_Rate_Cur.data = row.CR_ST_at_Rate_Cur
    form.CR_ST_at_CC_Cur.data = row.CR_ST_at_CC_Cur
    form.CR_ST_at_Cur.data = row.CR_ST_at_Cur
    form.Cus_Name.data = row.Cus_Name
    form.CI_Name.data = row.CI_Name
    form.CU_Description.data = row.CU_Description
    form.CC_Description.data = row.CC_Description
    form.Rat_Period_Description.data = row.Rat_Period_Description
    form.Pla_Id.data = row.Pla_Id
    session['prev_row']=str(row)
    session['is_new_row']=False
    return render_template('charge_resumes.html', form=form, row=row)

# =============================================================================
@main.route('/forms/Charge_Resumes_delete', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
def forms_Charge_Resumes_delete():
    """ Delete record handling function for table Charge_Resumes """

    logger.debug('Enter: forms_Charge_Resumes_delete()')
    Cus_Id  =  request.args.get('Cus_Id',0,type=int)
    CR_Date_From  =  request.args.get('CR_Date_From',0,type=int)
    CR_Date_To  =  request.args.get('CR_Date_To',0,type=int)
    CIT_Status  =  request.args.get('CIT_Status',0,type=int)
    Cur_Code  =  request.args.get('Cur_Code',0,type=int)
    CU_Id  =  request.args.get('CU_Id',0,type=int)
    row =  charge_resume.query.filter(charge_resume.Cus_Id == Cus_Id,charge_resume.CR_Date_From == CR_Date_From,charge_resume.CR_Date_To == CR_Date_To,charge_resume.CIT_Status == CIT_Status,charge_resume.Cur_Code == Cur_Code,charge_resume.CU_Id == CU_Id).first()
    if row is None:
        row=charge_resume()
    session['data'] =  { 'Cus_Id':row.Cus_Id, 'CR_Date_From':row.CR_Date_From, 'CR_Date_To':row.CR_Date_To, 'CIT_Status':row.CIT_Status, 'Cur_Code':row.Cur_Code, 'CIT_Count':row.CIT_Count, 'CIT_Quantity':row.CIT_Quantity, 'CIT_Generation':row.CIT_Generation, 'CU_Id':row.CU_Id, 'CI_CC_Id':row.CI_CC_Id, 'CU_Operation':row.CU_Operation, 'Typ_Code':row.Typ_Code, 'CC_Cur_Code':row.CC_Cur_Code, 'CI_Id':row.CI_Id, 'Rat_Id':row.Rat_Id, 'Rat_Price':row.Rat_Price, 'Rat_MU_Code':row.Rat_MU_Code, 'Rat_Cur_Code':row.Rat_Cur_Code, 'Rat_Period':row.Rat_Period, 'Rat_Hourly':row.Rat_Hourly, 'Rat_Daily':row.Rat_Daily, 'Rat_Monthly':row.Rat_Monthly, 'CR_Quantity':row.CR_Quantity, 'CR_Quantity_at_Rate':row.CR_Quantity_at_Rate, 'CC_XR':row.CC_XR, 'CR_Cur_XR':row.CR_Cur_XR, 'CR_ST_at_Rate_Cur':row.CR_ST_at_Rate_Cur, 'CR_ST_at_CC_Cur':row.CR_ST_at_CC_Cur, 'CR_ST_at_Cur':row.CR_ST_at_Cur, 'Cus_Name':row.Cus_Name, 'CI_Name':row.CI_Name, 'CU_Description':row.CU_Description, 'CC_Description':row.CC_Description, 'Rat_Period_Description':row.Rat_Period_Description, 'Pla_Id':row.Pla_Id}
    form = frm_charge_resume_delete()

    if form.validate_on_submit():
        if  form.submit_Delete.data:
            print('Delete Data Here...')
            try:
                session['deleted_row']=str(row)
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                logger.audit ( '%s:DEL:%s' % (current_user.username,session['deleted_row']) )
                flash('Charge Resume %s deleted OK'%(Cus_Id,CR_Date_From,CR_Date_To,CIT_Status,Cur_Code,CU_Id))
            except exc.IntegrityError as e:
                db.session.rollback()
                flash('INTEGRITY ERROR: Are you sure there are no dependant records in other tables?')
                return redirect(url_for('.forms_Charge_Resumes_delete',Cus_Id=session['data']['Cus_Id'],CR_Date_From=session['data']['CR_Date_From'],CR_Date_To=session['data']['CR_Date_To'],CIT_Status=session['data']['CIT_Status'],Cur_Code=session['data']['Cur_Code'],CU_Id=session['data']['CU_Id']))

            return redirect(url_for('.select_Charge_Resumes_query'))
        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
            return redirect(url_for('.select_Charge_Resumes_query'))
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.select_Charge_Resumes_query'))


    return render_template('charge_resumes_delete.html', form=form, data=session.get('data'),row=row)

# =============================================================================
@main.route('/select/Charge_Resumes_Query', methods=['GET','POST'])
@login_required
def select_Charge_Resumes_query():
    """ Select rows handling function for table Charge_Resumes """

    logger.debug('Enter: select_Charge_Resumes_query()')
    field =  request.args.get('field',None,type=str)
    value =  request.args.get('value',0,type=str)
    page  =  request.args.get('page',1,type=int)

    if field is not None:
        if   field == 'Cus_Id':
            rows =  charge_resume.query.filter_by(Cus_Id=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CR_Date_From':
            rows =  charge_resume.query.filter_by(CR_Date_From=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CR_Date_To':
            rows =  charge_resume.query.filter_by(CR_Date_To=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CIT_Status':
            rows =  charge_resume.query.filter_by(CIT_Status=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Cur_Code':
            rows =  charge_resume.query.filter_by(Cur_Code=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CIT_Count':
            rows =  charge_resume.query.filter_by(CIT_Count=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CIT_Quantity':
            rows =  charge_resume.query.filter_by(CIT_Quantity=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CIT_Generation':
            rows =  charge_resume.query.filter_by(CIT_Generation=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CU_Id':
            rows =  charge_resume.query.filter_by(CU_Id=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CI_CC_Id':
            rows =  charge_resume.query.filter_by(CI_CC_Id=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CU_Operation':
            rows =  charge_resume.query.filter_by(CU_Operation=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Typ_Code':
            rows =  charge_resume.query.filter_by(Typ_Code=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CC_Cur_Code':
            rows =  charge_resume.query.filter_by(CC_Cur_Code=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CI_Id':
            rows =  charge_resume.query.filter_by(CI_Id=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Rat_Id':
            rows =  charge_resume.query.filter_by(Rat_Id=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Rat_Price':
            rows =  charge_resume.query.filter_by(Rat_Price=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Rat_MU_Code':
            rows =  charge_resume.query.filter_by(Rat_MU_Code=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Rat_Cur_Code':
            rows =  charge_resume.query.filter_by(Rat_Cur_Code=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Rat_Period':
            rows =  charge_resume.query.filter_by(Rat_Period=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Rat_Hourly':
            rows =  charge_resume.query.filter_by(Rat_Hourly=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Rat_Daily':
            rows =  charge_resume.query.filter_by(Rat_Daily=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Rat_Monthly':
            rows =  charge_resume.query.filter_by(Rat_Monthly=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CR_Quantity':
            rows =  charge_resume.query.filter_by(CR_Quantity=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CR_Quantity_at_Rate':
            rows =  charge_resume.query.filter_by(CR_Quantity_at_Rate=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CC_XR':
            rows =  charge_resume.query.filter_by(CC_XR=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CR_Cur_XR':
            rows =  charge_resume.query.filter_by(CR_Cur_XR=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CR_ST_at_Rate_Cur':
            rows =  charge_resume.query.filter_by(CR_ST_at_Rate_Cur=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CR_ST_at_CC_Cur':
            rows =  charge_resume.query.filter_by(CR_ST_at_CC_Cur=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CR_ST_at_Cur':
            rows =  charge_resume.query.filter_by(CR_ST_at_Cur=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Cus_Name':
            rows =  charge_resume.query.filter_by(Cus_Name=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CI_Name':
            rows =  charge_resume.query.filter_by(CI_Name=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CU_Description':
            rows =  charge_resume.query.filter_by(CU_Description=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CC_Description':
            rows =  charge_resume.query.filter_by(CC_Description=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Rat_Period_Description':
            rows =  charge_resume.query.filter_by(Rat_Period_Description=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Pla_Id':
            rows =  charge_resume.query.filter_by(Pla_Id=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
    else:
       rows =  charge_resume.query\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)

    if field is not None:
       next_url = url_for('.select_Charge_Resumes_query', field=field, value=value, page=rows.next_num) \
           if rows.has_next else None
       prev_url = url_for('.select_Charge_Resumes_query', field=field, value=value, page=rows.prev_num) \
           if rows.has_prev else None

    else:
       next_url = url_for('.select_Charge_Resumes_query', page=rows.next_num) \
           if rows.has_next else None
       prev_url = url_for('.select_Charge_Resumes_query', page=rows.prev_num) \
           if rows.has_prev else None

    return render_template('charge_resumes_All.html',rows=rows)
# =============================================================================
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-18 18:05:34
# =============================================================================

@main.route('/forms/Charge_Units', methods=['GET', 'POST'])
@login_required
def forms_Charge_Units():
    """ Form handling function for table Charge_Units """

    logger.debug('Enter: forms_Charge_Units()')
    CU_Id  =  request.args.get('CU_Id',0,type=int)
    parent_key  =  request.args.get('parent_key',None,type=str)
    parent_value=  request.args.get('parent_value',0,type=int)

    row =  charge_unit.query.filter(charge_unit.CU_Id == CU_Id).first()
    if row is None:
        row=charge_unit()
        session['is_new_row']=True

    session['data'] =  { 'CU_Id':row.CU_Id, 'CI_Id':row.CI_Id, 'CU_Description':row.CU_Description, 'CU_UUID':row.CU_UUID, 'CU_Is_Billeable':row.CU_Is_Billeable, 'CU_Is_Always_Billeable':row.CU_Is_Always_Billeable, 'CU_Quantity':row.CU_Quantity, 'CU_Operation':row.CU_Operation, 'Typ_Code':row.Typ_Code, 'CIT_Generation':row.CIT_Generation, 'Rat_Id':row.Rat_Id, 'CU_Reference_1':row.CU_Reference_1, 'CU_Reference_2':row.CU_Reference_2, 'CU_Reference_3':row.CU_Reference_3}
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
        form.CIT_Generation.choices = db.session.query(cit_generation.CIT_Generation,cit_generation.Value).order_by(cit_generation.Value).all()

    if form.validate_on_submit():
        if     form.submit_Save.data and current_user.role_id>1:
            row.CI_Id = form.CI_Id.data
            row.CU_Description = form.CU_Description.data
            row.CU_UUID = form.CU_UUID.data
            row.CU_Is_Billeable = form.CU_Is_Billeable.data
            row.CU_Is_Always_Billeable = form.CU_Is_Always_Billeable.data
            row.CU_Quantity = form.CU_Quantity.data
            row.CU_Operation = form.CU_Operation.data
            row.Typ_Code = form.Typ_Code.data
            row.CIT_Generation = form.CIT_Generation.data
            row.CU_Reference_1 = form.CU_Reference_1.data
            row.CU_Reference_2 = form.CU_Reference_2.data
            row.CU_Reference_3 = form.CU_Reference_3.data
            try:
               session['new_row']=str(row)
               db.session.close()
               db.session.add(row)
               db.session.commit()
               if session['is_new_row']==True:
                   logger.audit ( '%s:NEW:%s' % (current_user.username,session['new_row'] ) )
                   flash('New Charge Unit created OK')
               else:
                   logger.audit ( '%s:OLD:%s' % (current_user.username,session['prev_row']) )
                   logger.audit ( '%s:UPD:%s' % (current_user.username,session['new_row'] ) )
                   message=Markup('<b>Charge Unit %s saved OK</b>'%(CU_Id))
                   flash(message)
               db.session.close()
            except Exception as e:
               db.session.rollback()
               db.session.close()
               message=Markup('ERROR saving Charge Unit record : %s'%(e))
               flash(message)
            return redirect(url_for('.select_Charge_Units_query'))
        elif   form.submit_New.data and current_user.role_id>1:
            #print('New Data Here ...')
            session['is_new_row']=True
            db.session.close()
            row=charge_unit()
            return redirect(url_for('.forms_Charge_Units',CU_Id=row.CU_Id))

        elif   form.submit_Cancel.data:
            #print('Cancel Data Here ... does nothing')
            message=Markup('Charge Unit Record modifications discarded ...')
            flash(message)
        else:
            #print('form validated but not submited ???')
            message=Markup('<b>Charge Unit data modifications not allowed for user \'%s\'. Please contact Collector\'s Administrator ...</b>'%(current_user.username))
            flash(message)
            return redirect(url_for('.forms_Charge_Units',CU_Id=row.CU_Id))

    form.CI_Id.data = row.CI_Id
    form.CU_Description.data = row.CU_Description
    form.CU_UUID.data = row.CU_UUID
    form.CU_Is_Billeable.data = row.CU_Is_Billeable
    form.CU_Is_Always_Billeable.data = row.CU_Is_Always_Billeable
    form.CU_Quantity.data = row.CU_Quantity
    form.CU_Operation.data = row.CU_Operation
    form.Typ_Code.data = row.Typ_Code
    form.CIT_Generation.data = row.CIT_Generation
    form.CU_Reference_1.data = row.CU_Reference_1
    form.CU_Reference_2.data = row.CU_Reference_2
    form.CU_Reference_3.data = row.CU_Reference_3
    session['prev_row']=str(row)
    session['is_new_row']=False
    return render_template('charge_units.html', form=form, row=row)

# =============================================================================
@main.route('/forms/Charge_Units_delete', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
def forms_Charge_Units_delete():
    """ Delete record handling function for table Charge_Units """

    logger.debug('Enter: forms_Charge_Units_delete()')
    CU_Id  =  request.args.get('CU_Id',0,type=int)
    row =  charge_unit.query.filter(charge_unit.CU_Id == CU_Id).first()
    if row is None:
        row=charge_unit()
    session['data'] =  { 'CU_Id':row.CU_Id, 'CI_Id':row.CI_Id, 'CU_Description':row.CU_Description, 'CU_UUID':row.CU_UUID, 'CU_Is_Billeable':row.CU_Is_Billeable, 'CU_Is_Always_Billeable':row.CU_Is_Always_Billeable, 'CU_Quantity':row.CU_Quantity, 'CU_Operation':row.CU_Operation, 'Typ_Code':row.Typ_Code, 'CIT_Generation':row.CIT_Generation, 'Rat_Id':row.Rat_Id, 'CU_Reference_1':row.CU_Reference_1, 'CU_Reference_2':row.CU_Reference_2, 'CU_Reference_3':row.CU_Reference_3}
    form = frm_charge_unit_delete()

    if form.validate_on_submit():
        if  form.submit_Delete.data:
            print('Delete Data Here...')
            try:
                session['deleted_row']=str(row)
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                logger.audit ( '%s:DEL:%s' % (current_user.username,session['deleted_row']) )
                flash('Charge Unit %s deleted OK'%(CU_Id))
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


    return render_template('charge_units_delete.html', form=form, data=session.get('data'),row=row)

# =============================================================================
@main.route('/select/Charge_Units_Query', methods=['GET','POST'])
@login_required
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
               .join(cit_generation,charge_unit.CIT_Generation == cit_generation.CIT_Generation).add_columns(cit_generation.Value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CI_Id':
            rows =  charge_unit.query.filter_by(CI_Id=value)\
               .join(configuration_item,charge_unit.CI_Id == configuration_item.CI_Id).add_columns(configuration_item.CI_Name)\
               .join(cu_operation,charge_unit.CU_Operation == cu_operation.CU_Operation).add_columns(cu_operation.Value)\
               .join(cu_type,charge_unit.Typ_Code == cu_type.Typ_Code).add_columns(cu_type.Typ_Description)\
               .join(cit_generation,charge_unit.CIT_Generation == cit_generation.CIT_Generation).add_columns(cit_generation.Value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CU_Description':
            rows =  charge_unit.query.filter_by(CU_Description=value)\
               .join(configuration_item,charge_unit.CI_Id == configuration_item.CI_Id).add_columns(configuration_item.CI_Name)\
               .join(cu_operation,charge_unit.CU_Operation == cu_operation.CU_Operation).add_columns(cu_operation.Value)\
               .join(cu_type,charge_unit.Typ_Code == cu_type.Typ_Code).add_columns(cu_type.Typ_Description)\
               .join(cit_generation,charge_unit.CIT_Generation == cit_generation.CIT_Generation).add_columns(cit_generation.Value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CU_UUID':
            rows =  charge_unit.query.filter_by(CU_UUID=value)\
               .join(configuration_item,charge_unit.CI_Id == configuration_item.CI_Id).add_columns(configuration_item.CI_Name)\
               .join(cu_operation,charge_unit.CU_Operation == cu_operation.CU_Operation).add_columns(cu_operation.Value)\
               .join(cu_type,charge_unit.Typ_Code == cu_type.Typ_Code).add_columns(cu_type.Typ_Description)\
               .join(cit_generation,charge_unit.CIT_Generation == cit_generation.CIT_Generation).add_columns(cit_generation.Value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CU_Is_Billeable':
            rows =  charge_unit.query.filter_by(CU_Is_Billeable=value)\
               .join(configuration_item,charge_unit.CI_Id == configuration_item.CI_Id).add_columns(configuration_item.CI_Name)\
               .join(cu_operation,charge_unit.CU_Operation == cu_operation.CU_Operation).add_columns(cu_operation.Value)\
               .join(cu_type,charge_unit.Typ_Code == cu_type.Typ_Code).add_columns(cu_type.Typ_Description)\
               .join(cit_generation,charge_unit.CIT_Generation == cit_generation.CIT_Generation).add_columns(cit_generation.Value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CU_Is_Always_Billeable':
            rows =  charge_unit.query.filter_by(CU_Is_Always_Billeable=value)\
               .join(configuration_item,charge_unit.CI_Id == configuration_item.CI_Id).add_columns(configuration_item.CI_Name)\
               .join(cu_operation,charge_unit.CU_Operation == cu_operation.CU_Operation).add_columns(cu_operation.Value)\
               .join(cu_type,charge_unit.Typ_Code == cu_type.Typ_Code).add_columns(cu_type.Typ_Description)\
               .join(cit_generation,charge_unit.CIT_Generation == cit_generation.CIT_Generation).add_columns(cit_generation.Value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CU_Quantity':
            rows =  charge_unit.query.filter_by(CU_Quantity=value)\
               .join(configuration_item,charge_unit.CI_Id == configuration_item.CI_Id).add_columns(configuration_item.CI_Name)\
               .join(cu_operation,charge_unit.CU_Operation == cu_operation.CU_Operation).add_columns(cu_operation.Value)\
               .join(cu_type,charge_unit.Typ_Code == cu_type.Typ_Code).add_columns(cu_type.Typ_Description)\
               .join(cit_generation,charge_unit.CIT_Generation == cit_generation.CIT_Generation).add_columns(cit_generation.Value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CU_Operation':
            rows =  charge_unit.query.filter_by(CU_Operation=value)\
               .join(configuration_item,charge_unit.CI_Id == configuration_item.CI_Id).add_columns(configuration_item.CI_Name)\
               .join(cu_operation,charge_unit.CU_Operation == cu_operation.CU_Operation).add_columns(cu_operation.Value)\
               .join(cu_type,charge_unit.Typ_Code == cu_type.Typ_Code).add_columns(cu_type.Typ_Description)\
               .join(cit_generation,charge_unit.CIT_Generation == cit_generation.CIT_Generation).add_columns(cit_generation.Value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Typ_Code':
            rows =  charge_unit.query.filter_by(Typ_Code=value)\
               .join(configuration_item,charge_unit.CI_Id == configuration_item.CI_Id).add_columns(configuration_item.CI_Name)\
               .join(cu_operation,charge_unit.CU_Operation == cu_operation.CU_Operation).add_columns(cu_operation.Value)\
               .join(cu_type,charge_unit.Typ_Code == cu_type.Typ_Code).add_columns(cu_type.Typ_Description)\
               .join(cit_generation,charge_unit.CIT_Generation == cit_generation.CIT_Generation).add_columns(cit_generation.Value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CIT_Generation':
            rows =  charge_unit.query.filter_by(CIT_Generation=value)\
               .join(configuration_item,charge_unit.CI_Id == configuration_item.CI_Id).add_columns(configuration_item.CI_Name)\
               .join(cu_operation,charge_unit.CU_Operation == cu_operation.CU_Operation).add_columns(cu_operation.Value)\
               .join(cu_type,charge_unit.Typ_Code == cu_type.Typ_Code).add_columns(cu_type.Typ_Description)\
               .join(cit_generation,charge_unit.CIT_Generation == cit_generation.CIT_Generation).add_columns(cit_generation.Value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Rat_Id':
            rows =  charge_unit.query.filter_by(Rat_Id=value)\
               .join(configuration_item,charge_unit.CI_Id == configuration_item.CI_Id).add_columns(configuration_item.CI_Name)\
               .join(cu_operation,charge_unit.CU_Operation == cu_operation.CU_Operation).add_columns(cu_operation.Value)\
               .join(cu_type,charge_unit.Typ_Code == cu_type.Typ_Code).add_columns(cu_type.Typ_Description)\
               .join(cit_generation,charge_unit.CIT_Generation == cit_generation.CIT_Generation).add_columns(cit_generation.Value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CU_Reference_1':
            rows =  charge_unit.query.filter_by(CU_Reference_1=value)\
               .join(configuration_item,charge_unit.CI_Id == configuration_item.CI_Id).add_columns(configuration_item.CI_Name)\
               .join(cu_operation,charge_unit.CU_Operation == cu_operation.CU_Operation).add_columns(cu_operation.Value)\
               .join(cu_type,charge_unit.Typ_Code == cu_type.Typ_Code).add_columns(cu_type.Typ_Description)\
               .join(cit_generation,charge_unit.CIT_Generation == cit_generation.CIT_Generation).add_columns(cit_generation.Value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CU_Reference_2':
            rows =  charge_unit.query.filter_by(CU_Reference_2=value)\
               .join(configuration_item,charge_unit.CI_Id == configuration_item.CI_Id).add_columns(configuration_item.CI_Name)\
               .join(cu_operation,charge_unit.CU_Operation == cu_operation.CU_Operation).add_columns(cu_operation.Value)\
               .join(cu_type,charge_unit.Typ_Code == cu_type.Typ_Code).add_columns(cu_type.Typ_Description)\
               .join(cit_generation,charge_unit.CIT_Generation == cit_generation.CIT_Generation).add_columns(cit_generation.Value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CU_Reference_3':
            rows =  charge_unit.query.filter_by(CU_Reference_3=value)\
               .join(configuration_item,charge_unit.CI_Id == configuration_item.CI_Id).add_columns(configuration_item.CI_Name)\
               .join(cu_operation,charge_unit.CU_Operation == cu_operation.CU_Operation).add_columns(cu_operation.Value)\
               .join(cu_type,charge_unit.Typ_Code == cu_type.Typ_Code).add_columns(cu_type.Typ_Description)\
               .join(cit_generation,charge_unit.CIT_Generation == cit_generation.CIT_Generation).add_columns(cit_generation.Value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
    else:
       rows =  charge_unit.query\
               .join(configuration_item,charge_unit.CI_Id == configuration_item.CI_Id).add_columns(configuration_item.CI_Name)\
               .join(cu_operation,charge_unit.CU_Operation == cu_operation.CU_Operation).add_columns(cu_operation.Value)\
               .join(cu_type,charge_unit.Typ_Code == cu_type.Typ_Code).add_columns(cu_type.Typ_Description)\
               .join(cit_generation,charge_unit.CIT_Generation == cit_generation.CIT_Generation).add_columns(cit_generation.Value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)

    if field is not None:
       next_url = url_for('.select_Charge_Units_query', field=field, value=value, page=rows.next_num) \
           if rows.has_next else None
       prev_url = url_for('.select_Charge_Units_query', field=field, value=value, page=rows.prev_num) \
           if rows.has_prev else None

    else:
       next_url = url_for('.select_Charge_Units_query', page=rows.next_num) \
           if rows.has_next else None
       prev_url = url_for('.select_Charge_Units_query', page=rows.prev_num) \
           if rows.has_prev else None

    return render_template('charge_units_All.html',rows=rows)
# =============================================================================
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-18 18:05:34
# =============================================================================

@main.route('/forms/CIT_Generations', methods=['GET', 'POST'])
@login_required
@admin_required
def forms_CIT_Generations():
    """ Form handling function for table CIT_Generations """

    logger.debug('Enter: forms_CIT_Generations()')
    CIT_Generation  =  request.args.get('CIT_Generation',0,type=int)
    row =  cit_generation.query.filter(cit_generation.CIT_Generation == CIT_Generation).first()
    if row is None:
        row=cit_generation()
        session['is_new_row']=True

    session['data'] =  { 'CIT_Generation':row.CIT_Generation, 'Value':row.Value}
    form = frm_cit_generation()

    if form.validate_on_submit():
        if     form.submit_Save.data and current_user.role_id>1:
            row.CIT_Generation = form.CIT_Generation.data
            row.Value = form.Value.data
            try:
               session['new_row']=str(row)
               db.session.close()
               db.session.add(row)
               db.session.commit()
               if session['is_new_row']==True:
                   logger.audit ( '%s:NEW:%s' % (current_user.username,session['new_row'] ) )
                   flash('New Configuration Item Generation Type created OK')
               else:
                   logger.audit ( '%s:OLD:%s' % (current_user.username,session['prev_row']) )
                   logger.audit ( '%s:UPD:%s' % (current_user.username,session['new_row'] ) )
                   message=Markup('<b>Configuration Item Generation Type %s saved OK</b>'%(CIT_Generation))
                   flash(message)
               db.session.close()
            except Exception as e:
               db.session.rollback()
               db.session.close()
               message=Markup('ERROR saving Configuration Item Generation Type record : %s'%(e))
               flash(message)
            return redirect(url_for('.select_CIT_Generations_query'))
        elif   form.submit_New.data and current_user.role_id>1:
            #print('New Data Here ...')
            session['is_new_row']=True
            db.session.close()
            row=cit_generation()
            return redirect(url_for('.forms_CIT_Generations'))

        elif   form.submit_Cancel.data:
            #print('Cancel Data Here ... does nothing')
            message=Markup('Configuration Item Generation Type Record modifications discarded ...')
            flash(message)
        else:
            #print('form validated but not submited ???')
            message=Markup('<b>Configuration Item Generation Type data modifications not allowed for user \'%s\'. Please contact Collector\'s Administrator ...</b>'%(current_user.username))
            flash(message)
            return redirect(url_for('.forms_CIT_Generations'))

    form.CIT_Generation.data = row.CIT_Generation
    form.Value.data = row.Value
    session['prev_row']=str(row)
    session['is_new_row']=False
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
            try:
                session['deleted_row']=str(row)
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                logger.audit ( '%s:DEL:%s' % (current_user.username,session['deleted_row']) )
                flash('Configuration Item Generation Type %s deleted OK'%(CIT_Generation))
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


    return render_template('cit_generations_delete.html', form=form, data=session.get('data'),row=row)

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

    if field is not None:
       next_url = url_for('.select_CIT_Generations_query', field=field, value=value, page=rows.next_num) \
           if rows.has_next else None
       prev_url = url_for('.select_CIT_Generations_query', field=field, value=value, page=rows.prev_num) \
           if rows.has_prev else None

    else:
       next_url = url_for('.select_CIT_Generations_query', page=rows.next_num) \
           if rows.has_next else None
       prev_url = url_for('.select_CIT_Generations_query', page=rows.prev_num) \
           if rows.has_prev else None

    return render_template('cit_generations_All.html',rows=rows)
# =============================================================================
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-18 18:05:34
# =============================================================================

@main.route('/forms/CIT_Statuses', methods=['GET', 'POST'])
@login_required
@admin_required
def forms_CIT_Statuses():
    """ Form handling function for table CIT_Statuses """

    logger.debug('Enter: forms_CIT_Statuses()')
    CIT_Status  =  request.args.get('CIT_Status',0,type=int)
    row =  cit_status.query.filter(cit_status.CIT_Status == CIT_Status).first()
    if row is None:
        row=cit_status()
        session['is_new_row']=True

    session['data'] =  { 'CIT_Status':row.CIT_Status, 'Value':row.Value}
    form = frm_cit_status()

    if form.validate_on_submit():
        if     form.submit_Save.data and current_user.role_id>1:
            row.CIT_Status = form.CIT_Status.data
            row.Value = form.Value.data
            try:
               session['new_row']=str(row)
               db.session.close()
               db.session.add(row)
               db.session.commit()
               if session['is_new_row']==True:
                   logger.audit ( '%s:NEW:%s' % (current_user.username,session['new_row'] ) )
                   flash('New Configuration Item Status Type created OK')
               else:
                   logger.audit ( '%s:OLD:%s' % (current_user.username,session['prev_row']) )
                   logger.audit ( '%s:UPD:%s' % (current_user.username,session['new_row'] ) )
                   message=Markup('<b>Configuration Item Status Type %s saved OK</b>'%(CIT_Status))
                   flash(message)
               db.session.close()
            except Exception as e:
               db.session.rollback()
               db.session.close()
               message=Markup('ERROR saving Configuration Item Status Type record : %s'%(e))
               flash(message)
            return redirect(url_for('.select_CIT_Statuses_query'))
        elif   form.submit_New.data and current_user.role_id>1:
            #print('New Data Here ...')
            session['is_new_row']=True
            db.session.close()
            row=cit_status()
            return redirect(url_for('.forms_CIT_Statuses'))

        elif   form.submit_Cancel.data:
            #print('Cancel Data Here ... does nothing')
            message=Markup('Configuration Item Status Type Record modifications discarded ...')
            flash(message)
        else:
            #print('form validated but not submited ???')
            message=Markup('<b>Configuration Item Status Type data modifications not allowed for user \'%s\'. Please contact Collector\'s Administrator ...</b>'%(current_user.username))
            flash(message)
            return redirect(url_for('.forms_CIT_Statuses'))

    form.CIT_Status.data = row.CIT_Status
    form.Value.data = row.Value
    session['prev_row']=str(row)
    session['is_new_row']=False
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
            try:
                session['deleted_row']=str(row)
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                logger.audit ( '%s:DEL:%s' % (current_user.username,session['deleted_row']) )
                flash('Configuration Item Status Type %s deleted OK'%(CIT_Status))
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


    return render_template('cit_statuses_delete.html', form=form, data=session.get('data'),row=row)

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

    if field is not None:
       next_url = url_for('.select_CIT_Statuses_query', field=field, value=value, page=rows.next_num) \
           if rows.has_next else None
       prev_url = url_for('.select_CIT_Statuses_query', field=field, value=value, page=rows.prev_num) \
           if rows.has_prev else None

    else:
       next_url = url_for('.select_CIT_Statuses_query', page=rows.next_num) \
           if rows.has_next else None
       prev_url = url_for('.select_CIT_Statuses_query', page=rows.prev_num) \
           if rows.has_prev else None

    return render_template('cit_statuses_All.html',rows=rows)
# =============================================================================
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-18 18:05:34
# =============================================================================

@main.route('/forms/Configuration_Items', methods=['GET', 'POST'])
@login_required
def forms_Configuration_Items():
    """ Form handling function for table Configuration_Items """

    logger.debug('Enter: forms_Configuration_Items()')
    CI_Id  =  request.args.get('CI_Id',0,type=int)
    row =  configuration_item.query.filter(configuration_item.CI_Id == CI_Id).first()
    if row is None:
        row=configuration_item()
        session['is_new_row']=True

    session['data'] =  { 'CI_Id':row.CI_Id, 'CI_Name':row.CI_Name, 'CI_UUID':row.CI_UUID, 'Pla_Id':row.Pla_Id, 'CC_Id':row.CC_Id, 'Cus_Id':row.Cus_Id, 'CI_Commissioning_DateTime':row.CI_Commissioning_DateTime, 'CI_Decommissioning_DateTime':row.CI_Decommissioning_DateTime}
    form = frm_configuration_item()

    if form.has_FKs:
        form.Pla_Id.choices = db.session.query(platform.Pla_Id,platform.Pla_Name).order_by(platform.Pla_Name).all()
        form.CC_Id.choices = db.session.query(cost_center.CC_Id,cost_center.CC_Description).order_by(cost_center.CC_Description).all()
        form.Cus_Id.choices = db.session.query(customer.Cus_Id,customer.Cus_Name).order_by(customer.Cus_Name).all()

    if form.validate_on_submit():
        if     form.submit_Save.data and current_user.role_id>1:
            row.CI_Name = form.CI_Name.data
            row.CI_UUID = form.CI_UUID.data
            row.Pla_Id = form.Pla_Id.data
            row.CC_Id = form.CC_Id.data
            row.Cus_Id = form.Cus_Id.data
            row.CI_Commissioning_DateTime = form.CI_Commissioning_DateTime.data
            row.CI_Decommissioning_DateTime = form.CI_Decommissioning_DateTime.data
            try:
               session['new_row']=str(row)
               db.session.close()
               db.session.add(row)
               db.session.commit()
               if session['is_new_row']==True:
                   logger.audit ( '%s:NEW:%s' % (current_user.username,session['new_row'] ) )
                   flash('New Configuration Item created OK')
               else:
                   logger.audit ( '%s:OLD:%s' % (current_user.username,session['prev_row']) )
                   logger.audit ( '%s:UPD:%s' % (current_user.username,session['new_row'] ) )
                   message=Markup('<b>Configuration Item %s saved OK</b>'%(CI_Id))
                   flash(message)
               db.session.close()
            except Exception as e:
               db.session.rollback()
               db.session.close()
               message=Markup('ERROR saving Configuration Item record : %s'%(e))
               flash(message)
            return redirect(url_for('.select_Configuration_Items_query'))
        elif   form.submit_New.data and current_user.role_id>1:
            #print('New Data Here ...')
            session['is_new_row']=True
            db.session.close()
            row=configuration_item()
            return redirect(url_for('.forms_Configuration_Items',CI_Id=row.CI_Id))

        elif   form.submit_Cancel.data:
            #print('Cancel Data Here ... does nothing')
            message=Markup('Configuration Item Record modifications discarded ...')
            flash(message)
        else:
            #print('form validated but not submited ???')
            message=Markup('<b>Configuration Item data modifications not allowed for user \'%s\'. Please contact Collector\'s Administrator ...</b>'%(current_user.username))
            flash(message)
            return redirect(url_for('.forms_Configuration_Items',CI_Id=row.CI_Id))

    form.CI_Name.data = row.CI_Name
    form.CI_UUID.data = row.CI_UUID
    form.Pla_Id.data = row.Pla_Id
    form.CC_Id.data = row.CC_Id
    form.Cus_Id.data = row.Cus_Id
    form.CI_Commissioning_DateTime.data = row.CI_Commissioning_DateTime
    form.CI_Decommissioning_DateTime.data = row.CI_Decommissioning_DateTime
    session['prev_row']=str(row)
    session['is_new_row']=False
    return render_template('configuration_items.html', form=form, row=row)

# =============================================================================
@main.route('/forms/Configuration_Items_delete', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
def forms_Configuration_Items_delete():
    """ Delete record handling function for table Configuration_Items """

    logger.debug('Enter: forms_Configuration_Items_delete()')
    CI_Id  =  request.args.get('CI_Id',0,type=int)
    row =  configuration_item.query.filter(configuration_item.CI_Id == CI_Id).first()
    if row is None:
        row=configuration_item()
    session['data'] =  { 'CI_Id':row.CI_Id, 'CI_Name':row.CI_Name, 'CI_UUID':row.CI_UUID, 'Pla_Id':row.Pla_Id, 'CC_Id':row.CC_Id, 'Cus_Id':row.Cus_Id, 'CI_Commissioning_DateTime':row.CI_Commissioning_DateTime, 'CI_Decommissioning_DateTime':row.CI_Decommissioning_DateTime}
    form = frm_configuration_item_delete()

    if form.validate_on_submit():
        if  form.submit_Delete.data:
            print('Delete Data Here...')
            try:
                session['deleted_row']=str(row)
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                logger.audit ( '%s:DEL:%s' % (current_user.username,session['deleted_row']) )
                flash('Configuration Item %s deleted OK'%(CI_Id))
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


    return render_template('configuration_items_delete.html', form=form, data=session.get('data'),row=row)

# =============================================================================
@main.route('/select/Configuration_Items_Query', methods=['GET','POST'])
@login_required
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
               .join(customer,configuration_item.Cus_Id == customer.Cus_Id).add_columns(customer.Cus_Name)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CI_Name':
            rows =  configuration_item.query.filter_by(CI_Name=value)\
               .join(platform,configuration_item.Pla_Id == platform.Pla_Id).add_columns(platform.Pla_Name)\
               .join(cost_center,configuration_item.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .join(customer,configuration_item.Cus_Id == customer.Cus_Id).add_columns(customer.Cus_Name)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CI_UUID':
            rows =  configuration_item.query.filter_by(CI_UUID=value)\
               .join(platform,configuration_item.Pla_Id == platform.Pla_Id).add_columns(platform.Pla_Name)\
               .join(cost_center,configuration_item.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .join(customer,configuration_item.Cus_Id == customer.Cus_Id).add_columns(customer.Cus_Name)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Pla_Id':
            rows =  configuration_item.query.filter_by(Pla_Id=value)\
               .join(platform,configuration_item.Pla_Id == platform.Pla_Id).add_columns(platform.Pla_Name)\
               .join(cost_center,configuration_item.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .join(customer,configuration_item.Cus_Id == customer.Cus_Id).add_columns(customer.Cus_Name)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CC_Id':
            rows =  configuration_item.query.filter_by(CC_Id=value)\
               .join(platform,configuration_item.Pla_Id == platform.Pla_Id).add_columns(platform.Pla_Name)\
               .join(cost_center,configuration_item.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .join(customer,configuration_item.Cus_Id == customer.Cus_Id).add_columns(customer.Cus_Name)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Cus_Id':
            rows =  configuration_item.query.filter_by(Cus_Id=value)\
               .join(platform,configuration_item.Pla_Id == platform.Pla_Id).add_columns(platform.Pla_Name)\
               .join(cost_center,configuration_item.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .join(customer,configuration_item.Cus_Id == customer.Cus_Id).add_columns(customer.Cus_Name)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CI_Commissioning_DateTime':
            rows =  configuration_item.query.filter_by(CI_Commissioning_DateTime=value)\
               .join(platform,configuration_item.Pla_Id == platform.Pla_Id).add_columns(platform.Pla_Name)\
               .join(cost_center,configuration_item.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .join(customer,configuration_item.Cus_Id == customer.Cus_Id).add_columns(customer.Cus_Name)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CI_Decommissioning_DateTime':
            rows =  configuration_item.query.filter_by(CI_Decommissioning_DateTime=value)\
               .join(platform,configuration_item.Pla_Id == platform.Pla_Id).add_columns(platform.Pla_Name)\
               .join(cost_center,configuration_item.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .join(customer,configuration_item.Cus_Id == customer.Cus_Id).add_columns(customer.Cus_Name)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
    else:
       rows =  configuration_item.query\
               .join(platform,configuration_item.Pla_Id == platform.Pla_Id).add_columns(platform.Pla_Name)\
               .join(cost_center,configuration_item.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .join(customer,configuration_item.Cus_Id == customer.Cus_Id).add_columns(customer.Cus_Name)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)

    if field is not None:
       next_url = url_for('.select_Configuration_Items_query', field=field, value=value, page=rows.next_num) \
           if rows.has_next else None
       prev_url = url_for('.select_Configuration_Items_query', field=field, value=value, page=rows.prev_num) \
           if rows.has_prev else None

    else:
       next_url = url_for('.select_Configuration_Items_query', page=rows.next_num) \
           if rows.has_next else None
       prev_url = url_for('.select_Configuration_Items_query', page=rows.prev_num) \
           if rows.has_prev else None

    return render_template('configuration_items_All.html',rows=rows)
# =============================================================================
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-18 18:05:34
# =============================================================================

@main.route('/forms/Cost_Centers', methods=['GET', 'POST'])
@login_required
def forms_Cost_Centers():
    """ Form handling function for table Cost_Centers """

    logger.debug('Enter: forms_Cost_Centers()')
    CC_Id  =  request.args.get('CC_Id',0,type=int)
    row =  cost_center.query.filter(cost_center.CC_Id == CC_Id).first()
    if row is None:
        row=cost_center()
        session['is_new_row']=True

    session['data'] =  { 'CC_Id':row.CC_Id, 'CC_Code':row.CC_Code, 'CC_Description':row.CC_Description, 'Cur_Code':row.Cur_Code, 'CC_Parent_Code':row.CC_Parent_Code}
    form = frm_cost_center()

    if form.has_FKs:
        form.Cur_Code.choices = db.session.query(currency.Cur_Code,currency.Cur_Name).order_by(currency.Cur_Name).all()

    if form.validate_on_submit():
        if     form.submit_Save.data and current_user.role_id>1:
            row.CC_Code = form.CC_Code.data
            row.CC_Description = form.CC_Description.data
            row.Cur_Code = form.Cur_Code.data
            row.CC_Parent_Code = form.CC_Parent_Code.data
            try:
               session['new_row']=str(row)
               db.session.close()
               db.session.add(row)
               db.session.commit()
               if session['is_new_row']==True:
                   logger.audit ( '%s:NEW:%s' % (current_user.username,session['new_row'] ) )
                   flash('New Cost Center created OK')
               else:
                   logger.audit ( '%s:OLD:%s' % (current_user.username,session['prev_row']) )
                   logger.audit ( '%s:UPD:%s' % (current_user.username,session['new_row'] ) )
                   message=Markup('<b>Cost Center %s saved OK</b>'%(CC_Id))
                   flash(message)
               db.session.close()
            except Exception as e:
               db.session.rollback()
               db.session.close()
               message=Markup('ERROR saving Cost Center record : %s'%(e))
               flash(message)
            return redirect(url_for('.select_Cost_Centers_query'))
        elif   form.submit_New.data and current_user.role_id>1:
            #print('New Data Here ...')
            session['is_new_row']=True
            db.session.close()
            row=cost_center()
            return redirect(url_for('.forms_Cost_Centers',CC_Id=row.CC_Id))

        elif   form.submit_Cancel.data:
            #print('Cancel Data Here ... does nothing')
            message=Markup('Cost Center Record modifications discarded ...')
            flash(message)
        else:
            #print('form validated but not submited ???')
            message=Markup('<b>Cost Center data modifications not allowed for user \'%s\'. Please contact Collector\'s Administrator ...</b>'%(current_user.username))
            flash(message)
            return redirect(url_for('.forms_Cost_Centers',CC_Id=row.CC_Id))

    form.CC_Code.data = row.CC_Code
    form.CC_Description.data = row.CC_Description
    form.Cur_Code.data = row.Cur_Code
    form.CC_Parent_Code.data = row.CC_Parent_Code
    session['prev_row']=str(row)
    session['is_new_row']=False
    return render_template('cost_centers.html', form=form, row=row)

# =============================================================================
@main.route('/forms/Cost_Centers_delete', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
def forms_Cost_Centers_delete():
    """ Delete record handling function for table Cost_Centers """

    logger.debug('Enter: forms_Cost_Centers_delete()')
    CC_Id  =  request.args.get('CC_Id',0,type=int)
    row =  cost_center.query.filter(cost_center.CC_Id == CC_Id).first()
    if row is None:
        row=cost_center()
    session['data'] =  { 'CC_Id':row.CC_Id, 'CC_Code':row.CC_Code, 'CC_Description':row.CC_Description, 'Cur_Code':row.Cur_Code, 'CC_Parent_Code':row.CC_Parent_Code}
    form = frm_cost_center_delete()

    if form.validate_on_submit():
        if  form.submit_Delete.data:
            print('Delete Data Here...')
            try:
                session['deleted_row']=str(row)
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                logger.audit ( '%s:DEL:%s' % (current_user.username,session['deleted_row']) )
                flash('Cost Center %s deleted OK'%(CC_Id))
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


    return render_template('cost_centers_delete.html', form=form, data=session.get('data'),row=row)

# =============================================================================
@main.route('/select/Cost_Centers_Query', methods=['GET','POST'])
@login_required
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
        elif field == 'CC_Parent_Code':
            rows =  cost_center.query.filter_by(CC_Parent_Code=value)\
               .join(currency,cost_center.Cur_Code == currency.Cur_Code).add_columns(currency.Cur_Name)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
    else:
       rows =  cost_center.query\
               .join(currency,cost_center.Cur_Code == currency.Cur_Code).add_columns(currency.Cur_Name)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)

    if field is not None:
       next_url = url_for('.select_Cost_Centers_query', field=field, value=value, page=rows.next_num) \
           if rows.has_next else None
       prev_url = url_for('.select_Cost_Centers_query', field=field, value=value, page=rows.prev_num) \
           if rows.has_prev else None

    else:
       next_url = url_for('.select_Cost_Centers_query', page=rows.next_num) \
           if rows.has_next else None
       prev_url = url_for('.select_Cost_Centers_query', page=rows.prev_num) \
           if rows.has_prev else None

    return render_template('cost_centers_All.html',rows=rows)
# =============================================================================
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-18 18:05:34
# =============================================================================

@main.route('/forms/Countries_Currencies', methods=['GET', 'POST'])
@login_required
@admin_required
def forms_Countries_Currencies():
    """ Form handling function for table Countries_Currencies """

    logger.debug('Enter: forms_Countries_Currencies()')
    Cou_Code  =  request.args.get('Cou_Code',0,type=int)
    Cur_Code  =  request.args.get('Cur_Code',0,type=int)
    row =  country_currency.query.filter(country_currency.Cou_Code == Cou_Code,country_currency.Cur_Code == Cur_Code).first()
    if row is None:
        row=country_currency()
        session['is_new_row']=True

    session['data'] =  { 'Cou_Code':row.Cou_Code, 'Cur_Code':row.Cur_Code, 'Cou_Cur_Comment':row.Cou_Cur_Comment}
    form = frm_country_currency()

    if form.has_FKs:
        form.Cou_Code.choices = db.session.query(country.Cou_Code,country.Cou_Name).order_by(country.Cou_Name).all()
        form.Cur_Code.choices = db.session.query(currency.Cur_Code,currency.Cur_Name).order_by(currency.Cur_Name).all()

    if form.validate_on_submit():
        if     form.submit_Save.data and current_user.role_id>1:
            row.Cou_Code = form.Cou_Code.data
            row.Cur_Code = form.Cur_Code.data
            row.Cou_Cur_Comment = form.Cou_Cur_Comment.data
            try:
               session['new_row']=str(row)
               db.session.close()
               db.session.add(row)
               db.session.commit()
               if session['is_new_row']==True:
                   logger.audit ( '%s:NEW:%s' % (current_user.username,session['new_row'] ) )
                   flash('New Country vs Currency created OK')
               else:
                   logger.audit ( '%s:OLD:%s' % (current_user.username,session['prev_row']) )
                   logger.audit ( '%s:UPD:%s' % (current_user.username,session['new_row'] ) )
                   message=Markup('<b>Country vs Currency %s saved OK</b>'%(Cou_Code,Cur_Code))
                   flash(message)
               db.session.close()
            except Exception as e:
               db.session.rollback()
               db.session.close()
               message=Markup('ERROR saving Country vs Currency record : %s'%(e))
               flash(message)
            return redirect(url_for('.select_Countries_Currencies_query'))
        elif   form.submit_New.data and current_user.role_id>1:
            #print('New Data Here ...')
            session['is_new_row']=True
            db.session.close()
            row=country_currency()
            return redirect(url_for('.forms_Countries_Currencies'))

        elif   form.submit_Cancel.data:
            #print('Cancel Data Here ... does nothing')
            message=Markup('Country vs Currency Record modifications discarded ...')
            flash(message)
        else:
            #print('form validated but not submited ???')
            message=Markup('<b>Country vs Currency data modifications not allowed for user \'%s\'. Please contact Collector\'s Administrator ...</b>'%(current_user.username))
            flash(message)
            return redirect(url_for('.forms_Countries_Currencies'))

    form.Cou_Code.data = row.Cou_Code
    form.Cur_Code.data = row.Cur_Code
    form.Cou_Cur_Comment.data = row.Cou_Cur_Comment
    session['prev_row']=str(row)
    session['is_new_row']=False
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
            try:
                session['deleted_row']=str(row)
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                logger.audit ( '%s:DEL:%s' % (current_user.username,session['deleted_row']) )
                flash('Country vs Currency %s deleted OK'%(Cou_Code,Cur_Code))
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


    return render_template('countries_currencies_delete.html', form=form, data=session.get('data'),row=row)

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

    if field is not None:
       next_url = url_for('.select_Countries_Currencies_query', field=field, value=value, page=rows.next_num) \
           if rows.has_next else None
       prev_url = url_for('.select_Countries_Currencies_query', field=field, value=value, page=rows.prev_num) \
           if rows.has_prev else None

    else:
       next_url = url_for('.select_Countries_Currencies_query', page=rows.next_num) \
           if rows.has_next else None
       prev_url = url_for('.select_Countries_Currencies_query', page=rows.prev_num) \
           if rows.has_prev else None

    return render_template('countries_currencies_All.html',rows=rows)
# =============================================================================
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-18 18:05:34
# =============================================================================

@main.route('/forms/Countries', methods=['GET', 'POST'])
@login_required
@admin_required
def forms_Countries():
    """ Form handling function for table Countries """

    logger.debug('Enter: forms_Countries()')
    Cou_Code  =  request.args.get('Cou_Code',0,type=int)
    row =  country.query.filter(country.Cou_Code == Cou_Code).first()
    if row is None:
        row=country()
        session['is_new_row']=True

    session['data'] =  { 'Cou_Code':row.Cou_Code, 'Cou_Name':row.Cou_Name, 'Cou_A3':row.Cou_A3, 'Cou_N':row.Cou_N}
    form = frm_country()

    if form.validate_on_submit():
        if     form.submit_Save.data and current_user.role_id>1:
            row.Cou_Code = form.Cou_Code.data
            row.Cou_Name = form.Cou_Name.data
            row.Cou_A3 = form.Cou_A3.data
            row.Cou_N = form.Cou_N.data
            try:
               session['new_row']=str(row)
               db.session.close()
               db.session.add(row)
               db.session.commit()
               if session['is_new_row']==True:
                   logger.audit ( '%s:NEW:%s' % (current_user.username,session['new_row'] ) )
                   flash('New Country created OK')
               else:
                   logger.audit ( '%s:OLD:%s' % (current_user.username,session['prev_row']) )
                   logger.audit ( '%s:UPD:%s' % (current_user.username,session['new_row'] ) )
                   message=Markup('<b>Country %s saved OK</b>'%(Cou_Code))
                   flash(message)
               db.session.close()
            except Exception as e:
               db.session.rollback()
               db.session.close()
               message=Markup('ERROR saving Country record : %s'%(e))
               flash(message)
            return redirect(url_for('.select_Countries_query'))
        elif   form.submit_New.data and current_user.role_id>1:
            #print('New Data Here ...')
            session['is_new_row']=True
            db.session.close()
            row=country()
            return redirect(url_for('.forms_Countries'))

        elif   form.submit_Cancel.data:
            #print('Cancel Data Here ... does nothing')
            message=Markup('Country Record modifications discarded ...')
            flash(message)
        else:
            #print('form validated but not submited ???')
            message=Markup('<b>Country data modifications not allowed for user \'%s\'. Please contact Collector\'s Administrator ...</b>'%(current_user.username))
            flash(message)
            return redirect(url_for('.forms_Countries'))

    form.Cou_Code.data = row.Cou_Code
    form.Cou_Name.data = row.Cou_Name
    form.Cou_A3.data = row.Cou_A3
    form.Cou_N.data = row.Cou_N
    session['prev_row']=str(row)
    session['is_new_row']=False
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
            try:
                session['deleted_row']=str(row)
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                logger.audit ( '%s:DEL:%s' % (current_user.username,session['deleted_row']) )
                flash('Country %s deleted OK'%(Cou_Code))
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


    return render_template('countries_delete.html', form=form, data=session.get('data'),row=row)

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

    if field is not None:
       next_url = url_for('.select_Countries_query', field=field, value=value, page=rows.next_num) \
           if rows.has_next else None
       prev_url = url_for('.select_Countries_query', field=field, value=value, page=rows.prev_num) \
           if rows.has_prev else None

    else:
       next_url = url_for('.select_Countries_query', page=rows.next_num) \
           if rows.has_next else None
       prev_url = url_for('.select_Countries_query', page=rows.prev_num) \
           if rows.has_prev else None

    return render_template('countries_All.html',rows=rows)
# =============================================================================
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-18 18:05:34
# =============================================================================

@main.route('/forms/CU_Operations', methods=['GET', 'POST'])
@login_required
@admin_required
def forms_CU_Operations():
    """ Form handling function for table CU_Operations """

    logger.debug('Enter: forms_CU_Operations()')
    CU_Operation  =  request.args.get('CU_Operation',0,type=int)
    row =  cu_operation.query.filter(cu_operation.CU_Operation == CU_Operation).first()
    if row is None:
        row=cu_operation()
        session['is_new_row']=True

    session['data'] =  { 'CU_Operation':row.CU_Operation, 'Value':row.Value, 'Is_Multiply':row.Is_Multiply, 'Factor':row.Factor}
    form = frm_cu_operation()

    if form.validate_on_submit():
        if     form.submit_Save.data and current_user.role_id>1:
            row.CU_Operation = form.CU_Operation.data
            row.Value = form.Value.data
            row.Is_Multiply = form.Is_Multiply.data
            row.Factor = form.Factor.data
            try:
               session['new_row']=str(row)
               db.session.close()
               db.session.add(row)
               db.session.commit()
               if session['is_new_row']==True:
                   logger.audit ( '%s:NEW:%s' % (current_user.username,session['new_row'] ) )
                   flash('New Charge Unit Conversion Operation created OK')
               else:
                   logger.audit ( '%s:OLD:%s' % (current_user.username,session['prev_row']) )
                   logger.audit ( '%s:UPD:%s' % (current_user.username,session['new_row'] ) )
                   message=Markup('<b>Charge Unit Conversion Operation %s saved OK</b>'%(CU_Operation))
                   flash(message)
               db.session.close()
            except Exception as e:
               db.session.rollback()
               db.session.close()
               message=Markup('ERROR saving Charge Unit Conversion Operation record : %s'%(e))
               flash(message)
            return redirect(url_for('.select_CU_Operations_query'))
        elif   form.submit_New.data and current_user.role_id>1:
            #print('New Data Here ...')
            session['is_new_row']=True
            db.session.close()
            row=cu_operation()
            return redirect(url_for('.forms_CU_Operations'))

        elif   form.submit_Cancel.data:
            #print('Cancel Data Here ... does nothing')
            message=Markup('Charge Unit Conversion Operation Record modifications discarded ...')
            flash(message)
        else:
            #print('form validated but not submited ???')
            message=Markup('<b>Charge Unit Conversion Operation data modifications not allowed for user \'%s\'. Please contact Collector\'s Administrator ...</b>'%(current_user.username))
            flash(message)
            return redirect(url_for('.forms_CU_Operations'))

    form.CU_Operation.data = row.CU_Operation
    form.Value.data = row.Value
    form.Is_Multiply.data = row.Is_Multiply
    form.Factor.data = row.Factor
    session['prev_row']=str(row)
    session['is_new_row']=False
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
            try:
                session['deleted_row']=str(row)
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                logger.audit ( '%s:DEL:%s' % (current_user.username,session['deleted_row']) )
                flash('Charge Unit Conversion Operation %s deleted OK'%(CU_Operation))
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


    return render_template('cu_operations_delete.html', form=form, data=session.get('data'),row=row)

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

    if field is not None:
       next_url = url_for('.select_CU_Operations_query', field=field, value=value, page=rows.next_num) \
           if rows.has_next else None
       prev_url = url_for('.select_CU_Operations_query', field=field, value=value, page=rows.prev_num) \
           if rows.has_prev else None

    else:
       next_url = url_for('.select_CU_Operations_query', page=rows.next_num) \
           if rows.has_next else None
       prev_url = url_for('.select_CU_Operations_query', page=rows.prev_num) \
           if rows.has_prev else None

    return render_template('cu_operations_All.html',rows=rows)
# =============================================================================
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-18 18:05:34
# =============================================================================

@main.route('/forms/Currencies', methods=['GET', 'POST'])
@login_required
@admin_required
def forms_Currencies():
    """ Form handling function for table Currencies """

    logger.debug('Enter: forms_Currencies()')
    Cur_Code  =  request.args.get('Cur_Code',0,type=int)
    row =  currency.query.filter(currency.Cur_Code == Cur_Code).first()
    if row is None:
        row=currency()
        session['is_new_row']=True

    session['data'] =  { 'Cur_Code':row.Cur_Code, 'Cur_Name':row.Cur_Name, 'Cur_Id':row.Cur_Id, 'Cur_Comment':row.Cur_Comment}
    form = frm_currency()

    if form.validate_on_submit():
        if     form.submit_Save.data and current_user.role_id>1:
            row.Cur_Code = form.Cur_Code.data
            row.Cur_Name = form.Cur_Name.data
            row.Cur_Id = form.Cur_Id.data
            row.Cur_Comment = form.Cur_Comment.data
            try:
               session['new_row']=str(row)
               db.session.close()
               db.session.add(row)
               db.session.commit()
               if session['is_new_row']==True:
                   logger.audit ( '%s:NEW:%s' % (current_user.username,session['new_row'] ) )
                   flash('New Currency created OK')
               else:
                   logger.audit ( '%s:OLD:%s' % (current_user.username,session['prev_row']) )
                   logger.audit ( '%s:UPD:%s' % (current_user.username,session['new_row'] ) )
                   message=Markup('<b>Currency %s saved OK</b>'%(Cur_Code))
                   flash(message)
               db.session.close()
            except Exception as e:
               db.session.rollback()
               db.session.close()
               message=Markup('ERROR saving Currency record : %s'%(e))
               flash(message)
            return redirect(url_for('.select_Currencies_query'))
        elif   form.submit_New.data and current_user.role_id>1:
            #print('New Data Here ...')
            session['is_new_row']=True
            db.session.close()
            row=currency()
            return redirect(url_for('.forms_Currencies'))

        elif   form.submit_Cancel.data:
            #print('Cancel Data Here ... does nothing')
            message=Markup('Currency Record modifications discarded ...')
            flash(message)
        else:
            #print('form validated but not submited ???')
            message=Markup('<b>Currency data modifications not allowed for user \'%s\'. Please contact Collector\'s Administrator ...</b>'%(current_user.username))
            flash(message)
            return redirect(url_for('.forms_Currencies'))

    form.Cur_Code.data = row.Cur_Code
    form.Cur_Name.data = row.Cur_Name
    form.Cur_Id.data = row.Cur_Id
    form.Cur_Comment.data = row.Cur_Comment
    session['prev_row']=str(row)
    session['is_new_row']=False
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
            try:
                session['deleted_row']=str(row)
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                logger.audit ( '%s:DEL:%s' % (current_user.username,session['deleted_row']) )
                flash('Currency %s deleted OK'%(Cur_Code))
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


    return render_template('currencies_delete.html', form=form, data=session.get('data'),row=row)

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

    if field is not None:
       next_url = url_for('.select_Currencies_query', field=field, value=value, page=rows.next_num) \
           if rows.has_next else None
       prev_url = url_for('.select_Currencies_query', field=field, value=value, page=rows.prev_num) \
           if rows.has_prev else None

    else:
       next_url = url_for('.select_Currencies_query', page=rows.next_num) \
           if rows.has_next else None
       prev_url = url_for('.select_Currencies_query', page=rows.prev_num) \
           if rows.has_prev else None

    return render_template('currencies_All.html',rows=rows)
# =============================================================================
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-18 18:05:34
# =============================================================================

@main.route('/forms/Customers', methods=['GET', 'POST'])
@login_required
@admin_required
def forms_Customers():
    """ Form handling function for table Customers """

    logger.debug('Enter: forms_Customers()')
    Cus_Id  =  request.args.get('Cus_Id',0,type=int)
    row =  customer.query.filter(customer.Cus_Id == Cus_Id).first()
    if row is None:
        row=customer()
        session['is_new_row']=True

    session['data'] =  { 'Cus_Id':row.Cus_Id, 'Cus_Name':row.Cus_Name, 'CC_Id':row.CC_Id}
    form = frm_customer()

    if form.has_FKs:
        form.CC_Id.choices = db.session.query(cost_center.CC_Id,cost_center.CC_Description).order_by(cost_center.CC_Description).all()

    if form.validate_on_submit():
        if     form.submit_Save.data and current_user.role_id>1:
            row.Cus_Name = form.Cus_Name.data
            row.CC_Id = form.CC_Id.data
            try:
               session['new_row']=str(row)
               db.session.close()
               db.session.add(row)
               db.session.commit()
               if session['is_new_row']==True:
                   logger.audit ( '%s:NEW:%s' % (current_user.username,session['new_row'] ) )
                   flash('New Customer created OK')
               else:
                   logger.audit ( '%s:OLD:%s' % (current_user.username,session['prev_row']) )
                   logger.audit ( '%s:UPD:%s' % (current_user.username,session['new_row'] ) )
                   message=Markup('<b>Customer %s saved OK</b>'%(Cus_Id))
                   flash(message)
               db.session.close()
            except Exception as e:
               db.session.rollback()
               db.session.close()
               message=Markup('ERROR saving Customer record : %s'%(e))
               flash(message)
            return redirect(url_for('.select_Customers_query'))
        elif   form.submit_New.data and current_user.role_id>1:
            #print('New Data Here ...')
            session['is_new_row']=True
            db.session.close()
            row=customer()
            return redirect(url_for('.forms_Customers',Cus_Id=row.Cus_Id))

        elif   form.submit_Cancel.data:
            #print('Cancel Data Here ... does nothing')
            message=Markup('Customer Record modifications discarded ...')
            flash(message)
        else:
            #print('form validated but not submited ???')
            message=Markup('<b>Customer data modifications not allowed for user \'%s\'. Please contact Collector\'s Administrator ...</b>'%(current_user.username))
            flash(message)
            return redirect(url_for('.forms_Customers',Cus_Id=row.Cus_Id))

    form.Cus_Name.data = row.Cus_Name
    form.CC_Id.data = row.CC_Id
    session['prev_row']=str(row)
    session['is_new_row']=False
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
            try:
                session['deleted_row']=str(row)
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                logger.audit ( '%s:DEL:%s' % (current_user.username,session['deleted_row']) )
                flash('Customer %s deleted OK'%(Cus_Id))
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


    return render_template('customers_delete.html', form=form, data=session.get('data'),row=row)

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

    if field is not None:
       next_url = url_for('.select_Customers_query', field=field, value=value, page=rows.next_num) \
           if rows.has_next else None
       prev_url = url_for('.select_Customers_query', field=field, value=value, page=rows.prev_num) \
           if rows.has_prev else None

    else:
       next_url = url_for('.select_Customers_query', page=rows.next_num) \
           if rows.has_next else None
       prev_url = url_for('.select_Customers_query', page=rows.prev_num) \
           if rows.has_prev else None

    return render_template('customers_All.html',rows=rows)
# =============================================================================
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-18 18:05:34
# =============================================================================

@main.route('/forms/CU_Types', methods=['GET', 'POST'])
@login_required
@admin_required
def forms_CU_Types():
    """ Form handling function for table CU_Types """

    logger.debug('Enter: forms_CU_Types()')
    Typ_Code  =  request.args.get('Typ_Code',0,type=int)
    row =  cu_type.query.filter(cu_type.Typ_Code == Typ_Code).first()
    if row is None:
        row=cu_type()
        session['is_new_row']=True

    session['data'] =  { 'Typ_Code':row.Typ_Code, 'Typ_Description':row.Typ_Description}
    form = frm_cu_type()

    if form.validate_on_submit():
        if     form.submit_Save.data and current_user.role_id>1:
            row.Typ_Code = form.Typ_Code.data
            row.Typ_Description = form.Typ_Description.data
            try:
               session['new_row']=str(row)
               db.session.close()
               db.session.add(row)
               db.session.commit()
               if session['is_new_row']==True:
                   logger.audit ( '%s:NEW:%s' % (current_user.username,session['new_row'] ) )
                   flash('New Configuration Unit Type created OK')
               else:
                   logger.audit ( '%s:OLD:%s' % (current_user.username,session['prev_row']) )
                   logger.audit ( '%s:UPD:%s' % (current_user.username,session['new_row'] ) )
                   message=Markup('<b>Configuration Unit Type %s saved OK</b>'%(Typ_Code))
                   flash(message)
               db.session.close()
            except Exception as e:
               db.session.rollback()
               db.session.close()
               message=Markup('ERROR saving Configuration Unit Type record : %s'%(e))
               flash(message)
            return redirect(url_for('.select_CU_Types_query'))
        elif   form.submit_New.data and current_user.role_id>1:
            #print('New Data Here ...')
            session['is_new_row']=True
            db.session.close()
            row=cu_type()
            return redirect(url_for('.forms_CU_Types'))

        elif   form.submit_Cancel.data:
            #print('Cancel Data Here ... does nothing')
            message=Markup('Configuration Unit Type Record modifications discarded ...')
            flash(message)
        else:
            #print('form validated but not submited ???')
            message=Markup('<b>Configuration Unit Type data modifications not allowed for user \'%s\'. Please contact Collector\'s Administrator ...</b>'%(current_user.username))
            flash(message)
            return redirect(url_for('.forms_CU_Types'))

    form.Typ_Code.data = row.Typ_Code
    form.Typ_Description.data = row.Typ_Description
    session['prev_row']=str(row)
    session['is_new_row']=False
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
            try:
                session['deleted_row']=str(row)
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                logger.audit ( '%s:DEL:%s' % (current_user.username,session['deleted_row']) )
                flash('Configuration Unit Type %s deleted OK'%(Typ_Code))
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


    return render_template('cu_types_delete.html', form=form, data=session.get('data'),row=row)

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

    if field is not None:
       next_url = url_for('.select_CU_Types_query', field=field, value=value, page=rows.next_num) \
           if rows.has_next else None
       prev_url = url_for('.select_CU_Types_query', field=field, value=value, page=rows.prev_num) \
           if rows.has_prev else None

    else:
       next_url = url_for('.select_CU_Types_query', page=rows.next_num) \
           if rows.has_next else None
       prev_url = url_for('.select_CU_Types_query', page=rows.prev_num) \
           if rows.has_prev else None

    return render_template('cu_types_All.html',rows=rows)
# =============================================================================
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-18 18:05:34
# =============================================================================

@main.route('/forms/Dev_Forms', methods=['GET', 'POST'])
@login_required
@admin_required
def forms_Dev_Forms():
    """ Form handling function for table Dev_Forms """

    logger.debug('Enter: forms_Dev_Forms()')
    Id  =  request.args.get('Id',0,type=int)
    row =  dev_form.query.filter(dev_form.Id == Id).first()
    if row is None:
        row=dev_form()
        session['is_new_row']=True

    session['data'] =  { 'Id':row.Id, 'Table':row.Table, 'Field':row.Field, 'Type':row.Type, 'Null':row.Null, 'Key':row.Key, 'Default':row.Default, 'Extra':row.Extra, 'Foreign_Key':row.Foreign_Key, 'Referenced_Table':row.Referenced_Table, 'Foreign_Field':row.Foreign_Field, 'Foreign_Value':row.Foreign_Value, 'Length':row.Length, 'Validation':row.Validation, 'Validation_Type':row.Validation_Type, 'Validation_String':row.Validation_String, 'Caption_String':row.Caption_String, 'Field_Order':row.Field_Order, 'Field_Format':row.Field_Format, 'Form_Editable':row.Form_Editable, 'ORM_Schema':row.ORM_Schema}
    form = frm_dev_form()

    if form.validate_on_submit():
        if     form.submit_Save.data and current_user.role_id>1:
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
            row.ORM_Schema = form.ORM_Schema.data
            try:
               session['new_row']=str(row)
               db.session.close()
               db.session.add(row)
               db.session.commit()
               if session['is_new_row']==True:
                   logger.audit ( '%s:NEW:%s' % (current_user.username,session['new_row'] ) )
                   flash('New Form created OK')
               else:
                   logger.audit ( '%s:OLD:%s' % (current_user.username,session['prev_row']) )
                   logger.audit ( '%s:UPD:%s' % (current_user.username,session['new_row'] ) )
                   message=Markup('<b>Form %s saved OK</b>'%(Id))
                   flash(message)
               db.session.close()
            except Exception as e:
               db.session.rollback()
               db.session.close()
               message=Markup('ERROR saving Form record : %s'%(e))
               flash(message)
            return redirect(url_for('.select_Dev_Forms_query'))
        elif   form.submit_New.data and current_user.role_id>1:
            #print('New Data Here ...')
            session['is_new_row']=True
            db.session.close()
            row=dev_form()
            return redirect(url_for('.forms_Dev_Forms',Id=row.Id))

        elif   form.submit_Cancel.data:
            #print('Cancel Data Here ... does nothing')
            message=Markup('Form Record modifications discarded ...')
            flash(message)
        else:
            #print('form validated but not submited ???')
            message=Markup('<b>Form data modifications not allowed for user \'%s\'. Please contact Collector\'s Administrator ...</b>'%(current_user.username))
            flash(message)
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
    form.ORM_Schema.data = row.ORM_Schema
    session['prev_row']=str(row)
    session['is_new_row']=False
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
    session['data'] =  { 'Id':row.Id, 'Table':row.Table, 'Field':row.Field, 'Type':row.Type, 'Null':row.Null, 'Key':row.Key, 'Default':row.Default, 'Extra':row.Extra, 'Foreign_Key':row.Foreign_Key, 'Referenced_Table':row.Referenced_Table, 'Foreign_Field':row.Foreign_Field, 'Foreign_Value':row.Foreign_Value, 'Length':row.Length, 'Validation':row.Validation, 'Validation_Type':row.Validation_Type, 'Validation_String':row.Validation_String, 'Caption_String':row.Caption_String, 'Field_Order':row.Field_Order, 'Field_Format':row.Field_Format, 'Form_Editable':row.Form_Editable, 'ORM_Schema':row.ORM_Schema}
    form = frm_dev_form_delete()

    if form.validate_on_submit():
        if  form.submit_Delete.data:
            print('Delete Data Here...')
            try:
                session['deleted_row']=str(row)
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                logger.audit ( '%s:DEL:%s' % (current_user.username,session['deleted_row']) )
                flash('Form %s deleted OK'%(Id))
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


    return render_template('dev_forms_delete.html', form=form, data=session.get('data'),row=row)

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
        elif field == 'ORM_Schema':
            rows =  dev_form.query.filter_by(ORM_Schema=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
    else:
       rows =  dev_form.query\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)

    if field is not None:
       next_url = url_for('.select_Dev_Forms_query', field=field, value=value, page=rows.next_num) \
           if rows.has_next else None
       prev_url = url_for('.select_Dev_Forms_query', field=field, value=value, page=rows.prev_num) \
           if rows.has_prev else None

    else:
       next_url = url_for('.select_Dev_Forms_query', page=rows.next_num) \
           if rows.has_next else None
       prev_url = url_for('.select_Dev_Forms_query', page=rows.prev_num) \
           if rows.has_prev else None

    return render_template('dev_forms_All.html',rows=rows)
# =============================================================================
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-18 18:05:34
# =============================================================================

@main.route('/forms/Dev_Tables', methods=['GET', 'POST'])
@login_required
@admin_required
def forms_Dev_Tables():
    """ Form handling function for table Dev_Tables """

    logger.debug('Enter: forms_Dev_Tables()')
    Id  =  request.args.get('Id',0,type=int)
    row =  dev_table.query.filter(dev_table.Id == Id).first()
    if row is None:
        row=dev_table()
        session['is_new_row']=True

    session['data'] =  { 'Id':row.Id, 'Name':row.Name, 'Caption':row.Caption, 'Entity':row.Entity, 'Class_Name':row.Class_Name, 'Child_Table':row.Child_Table, 'Parent_Table':row.Parent_Table, 'Use_Pagination':row.Use_Pagination, 'Use_Children_Pagination':row.Use_Children_Pagination, 'Generate_Form_One':row.Generate_Form_One, 'Generate_Form_All':row.Generate_Form_All, 'Generate_Form_Filter':row.Generate_Form_Filter, 'Generate_Children':row.Generate_Children, 'Generate_Foreign_Fields':row.Generate_Foreign_Fields, 'Permission_View':row.Permission_View, 'Permission_Delete':row.Permission_Delete, 'Permission_Modify':row.Permission_Modify, 'Permission_Report':row.Permission_Report, 'Permission_Export':row.Permission_Export, 'Permission_View_Private':row.Permission_View_Private, 'Permission_Modify_Private':row.Permission_Modify_Private, 'Permission_Administer':row.Permission_Administer}
    form = frm_dev_table()

    if form.validate_on_submit():
        if     form.submit_Save.data and current_user.role_id>1:
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
               session['new_row']=str(row)
               db.session.close()
               db.session.add(row)
               db.session.commit()
               if session['is_new_row']==True:
                   logger.audit ( '%s:NEW:%s' % (current_user.username,session['new_row'] ) )
                   flash('New Table created OK')
               else:
                   logger.audit ( '%s:OLD:%s' % (current_user.username,session['prev_row']) )
                   logger.audit ( '%s:UPD:%s' % (current_user.username,session['new_row'] ) )
                   message=Markup('<b>Table %s saved OK</b>'%(Id))
                   flash(message)
               db.session.close()
            except Exception as e:
               db.session.rollback()
               db.session.close()
               message=Markup('ERROR saving Table record : %s'%(e))
               flash(message)
            return redirect(url_for('.select_Dev_Tables_query'))
        elif   form.submit_New.data and current_user.role_id>1:
            #print('New Data Here ...')
            session['is_new_row']=True
            db.session.close()
            row=dev_table()
            return redirect(url_for('.forms_Dev_Tables',Id=row.Id))

        elif   form.submit_Cancel.data:
            #print('Cancel Data Here ... does nothing')
            message=Markup('Table Record modifications discarded ...')
            flash(message)
        else:
            #print('form validated but not submited ???')
            message=Markup('<b>Table data modifications not allowed for user \'%s\'. Please contact Collector\'s Administrator ...</b>'%(current_user.username))
            flash(message)
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
    session['prev_row']=str(row)
    session['is_new_row']=False
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
            try:
                session['deleted_row']=str(row)
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                logger.audit ( '%s:DEL:%s' % (current_user.username,session['deleted_row']) )
                flash('Table %s deleted OK'%(Id))
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


    return render_template('dev_tables_delete.html', form=form, data=session.get('data'),row=row)

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

    if field is not None:
       next_url = url_for('.select_Dev_Tables_query', field=field, value=value, page=rows.next_num) \
           if rows.has_next else None
       prev_url = url_for('.select_Dev_Tables_query', field=field, value=value, page=rows.prev_num) \
           if rows.has_prev else None

    else:
       next_url = url_for('.select_Dev_Tables_query', page=rows.next_num) \
           if rows.has_next else None
       prev_url = url_for('.select_Dev_Tables_query', page=rows.prev_num) \
           if rows.has_prev else None

    return render_template('dev_tables_All.html',rows=rows)
# =============================================================================
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-18 18:05:34
# =============================================================================

@main.route('/forms/Exchange_Rates', methods=['GET', 'POST'])
@login_required
@admin_required
def forms_Exchange_Rates():
    """ Form handling function for table Exchange_Rates """

    logger.debug('Enter: forms_Exchange_Rates()')
    ER_Id  =  request.args.get('ER_Id',0,type=int)
    row =  exchange_rate.query.filter(exchange_rate.ER_Id == ER_Id).first()
    if row is None:
        row=exchange_rate()
        session['is_new_row']=True

    session['data'] =  { 'ER_Id':row.ER_Id, 'Cur_Code':row.Cur_Code, 'ER_Factor':row.ER_Factor, 'ER_Date':row.ER_Date}
    form = frm_exchange_rate()

    if form.has_FKs:
        form.Cur_Code.choices = db.session.query(currency.Cur_Code,currency.Cur_Name).order_by(currency.Cur_Name).all()

    if form.validate_on_submit():
        if     form.submit_Save.data and current_user.role_id>1:
            row.Cur_Code = form.Cur_Code.data
            row.ER_Factor = form.ER_Factor.data
            row.ER_Date = form.ER_Date.data
            try:
               session['new_row']=str(row)
               db.session.close()
               db.session.add(row)
               db.session.commit()
               if session['is_new_row']==True:
                   logger.audit ( '%s:NEW:%s' % (current_user.username,session['new_row'] ) )
                   flash('New Exchange Rate created OK')
               else:
                   logger.audit ( '%s:OLD:%s' % (current_user.username,session['prev_row']) )
                   logger.audit ( '%s:UPD:%s' % (current_user.username,session['new_row'] ) )
                   message=Markup('<b>Exchange Rate %s saved OK</b>'%(ER_Id))
                   flash(message)
               db.session.close()
            except Exception as e:
               db.session.rollback()
               db.session.close()
               message=Markup('ERROR saving Exchange Rate record : %s'%(e))
               flash(message)
            return redirect(url_for('.select_Exchange_Rates_query'))
        elif   form.submit_New.data and current_user.role_id>1:
            #print('New Data Here ...')
            session['is_new_row']=True
            db.session.close()
            row=exchange_rate()
            return redirect(url_for('.forms_Exchange_Rates',ER_Id=row.ER_Id))

        elif   form.submit_Cancel.data:
            #print('Cancel Data Here ... does nothing')
            message=Markup('Exchange Rate Record modifications discarded ...')
            flash(message)
        else:
            #print('form validated but not submited ???')
            message=Markup('<b>Exchange Rate data modifications not allowed for user \'%s\'. Please contact Collector\'s Administrator ...</b>'%(current_user.username))
            flash(message)
            return redirect(url_for('.forms_Exchange_Rates',ER_Id=row.ER_Id))

    form.Cur_Code.data = row.Cur_Code
    form.ER_Factor.data = row.ER_Factor
    form.ER_Date.data = row.ER_Date
    session['prev_row']=str(row)
    session['is_new_row']=False
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
            try:
                session['deleted_row']=str(row)
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                logger.audit ( '%s:DEL:%s' % (current_user.username,session['deleted_row']) )
                flash('Exchange Rate %s deleted OK'%(ER_Id))
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


    return render_template('exchange_rates_delete.html', form=form, data=session.get('data'),row=row)

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

    if field is not None:
       next_url = url_for('.select_Exchange_Rates_query', field=field, value=value, page=rows.next_num) \
           if rows.has_next else None
       prev_url = url_for('.select_Exchange_Rates_query', field=field, value=value, page=rows.prev_num) \
           if rows.has_prev else None

    else:
       next_url = url_for('.select_Exchange_Rates_query', page=rows.next_num) \
           if rows.has_next else None
       prev_url = url_for('.select_Exchange_Rates_query', page=rows.prev_num) \
           if rows.has_prev else None

    return render_template('exchange_rates_All.html',rows=rows)
# =============================================================================
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-18 18:05:34
# =============================================================================

@main.route('/forms/Measure_Units', methods=['GET', 'POST'])
@login_required
@admin_required
def forms_Measure_Units():
    """ Form handling function for table Measure_Units """

    logger.debug('Enter: forms_Measure_Units()')
    MU_Code  =  request.args.get('MU_Code',0,type=int)
    row =  measure_unit.query.filter(measure_unit.MU_Code == MU_Code).first()
    if row is None:
        row=measure_unit()
        session['is_new_row']=True

    session['data'] =  { 'MU_Code':row.MU_Code, 'MU_Description':row.MU_Description}
    form = frm_measure_unit()

    if form.validate_on_submit():
        if     form.submit_Save.data and current_user.role_id>1:
            row.MU_Code = form.MU_Code.data
            row.MU_Description = form.MU_Description.data
            try:
               session['new_row']=str(row)
               db.session.close()
               db.session.add(row)
               db.session.commit()
               if session['is_new_row']==True:
                   logger.audit ( '%s:NEW:%s' % (current_user.username,session['new_row'] ) )
                   flash('New Measure Unit created OK')
               else:
                   logger.audit ( '%s:OLD:%s' % (current_user.username,session['prev_row']) )
                   logger.audit ( '%s:UPD:%s' % (current_user.username,session['new_row'] ) )
                   message=Markup('<b>Measure Unit %s saved OK</b>'%(MU_Code))
                   flash(message)
               db.session.close()
            except Exception as e:
               db.session.rollback()
               db.session.close()
               message=Markup('ERROR saving Measure Unit record : %s'%(e))
               flash(message)
            return redirect(url_for('.select_Measure_Units_query'))
        elif   form.submit_New.data and current_user.role_id>1:
            #print('New Data Here ...')
            session['is_new_row']=True
            db.session.close()
            row=measure_unit()
            return redirect(url_for('.forms_Measure_Units'))

        elif   form.submit_Cancel.data:
            #print('Cancel Data Here ... does nothing')
            message=Markup('Measure Unit Record modifications discarded ...')
            flash(message)
        else:
            #print('form validated but not submited ???')
            message=Markup('<b>Measure Unit data modifications not allowed for user \'%s\'. Please contact Collector\'s Administrator ...</b>'%(current_user.username))
            flash(message)
            return redirect(url_for('.forms_Measure_Units'))

    form.MU_Code.data = row.MU_Code
    form.MU_Description.data = row.MU_Description
    session['prev_row']=str(row)
    session['is_new_row']=False
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
            try:
                session['deleted_row']=str(row)
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                logger.audit ( '%s:DEL:%s' % (current_user.username,session['deleted_row']) )
                flash('Measure Unit %s deleted OK'%(MU_Code))
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


    return render_template('measure_units_delete.html', form=form, data=session.get('data'),row=row)

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

    if field is not None:
       next_url = url_for('.select_Measure_Units_query', field=field, value=value, page=rows.next_num) \
           if rows.has_next else None
       prev_url = url_for('.select_Measure_Units_query', field=field, value=value, page=rows.prev_num) \
           if rows.has_prev else None

    else:
       next_url = url_for('.select_Measure_Units_query', page=rows.next_num) \
           if rows.has_next else None
       prev_url = url_for('.select_Measure_Units_query', page=rows.prev_num) \
           if rows.has_prev else None

    return render_template('measure_units_All.html',rows=rows)
# =============================================================================
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-18 18:05:34
# =============================================================================

@main.route('/forms/Platforms', methods=['GET', 'POST'])
@login_required
@admin_required
def forms_Platforms():
    """ Form handling function for table Platforms """

    logger.debug('Enter: forms_Platforms()')
    Pla_Id  =  request.args.get('Pla_Id',0,type=int)
    row =  platform.query.filter(platform.Pla_Id == Pla_Id).first()
    if row is None:
        row=platform()
        session['is_new_row']=True

    session['data'] =  { 'Pla_Id':row.Pla_Id, 'Pla_Name':row.Pla_Name, 'Pla_Host':row.Pla_Host, 'Pla_Port':row.Pla_Port, 'Pla_User':row.Pla_User, 'Pla_Password':row.Pla_Password}
    form = frm_platform()

    if form.validate_on_submit():
        if     form.submit_Save.data and current_user.role_id>1:
            row.Pla_Name = form.Pla_Name.data
            row.Pla_Host = form.Pla_Host.data
            row.Pla_Port = form.Pla_Port.data
            row.Pla_User = form.Pla_User.data
            row.Pla_Password = form.Pla_Password.data
            try:
               session['new_row']=str(row)
               db.session.close()
               db.session.add(row)
               db.session.commit()
               if session['is_new_row']==True:
                   logger.audit ( '%s:NEW:%s' % (current_user.username,session['new_row'] ) )
                   flash('New Platform created OK')
               else:
                   logger.audit ( '%s:OLD:%s' % (current_user.username,session['prev_row']) )
                   logger.audit ( '%s:UPD:%s' % (current_user.username,session['new_row'] ) )
                   message=Markup('<b>Platform %s saved OK</b>'%(Pla_Id))
                   flash(message)
               db.session.close()
            except Exception as e:
               db.session.rollback()
               db.session.close()
               message=Markup('ERROR saving Platform record : %s'%(e))
               flash(message)
            return redirect(url_for('.select_Platforms_query'))
        elif   form.submit_New.data and current_user.role_id>1:
            #print('New Data Here ...')
            session['is_new_row']=True
            db.session.close()
            row=platform()
            return redirect(url_for('.forms_Platforms',Pla_Id=row.Pla_Id))

        elif   form.submit_Cancel.data:
            #print('Cancel Data Here ... does nothing')
            message=Markup('Platform Record modifications discarded ...')
            flash(message)
        else:
            #print('form validated but not submited ???')
            message=Markup('<b>Platform data modifications not allowed for user \'%s\'. Please contact Collector\'s Administrator ...</b>'%(current_user.username))
            flash(message)
            return redirect(url_for('.forms_Platforms',Pla_Id=row.Pla_Id))

    form.Pla_Name.data = row.Pla_Name
    form.Pla_Host.data = row.Pla_Host
    form.Pla_Port.data = row.Pla_Port
    form.Pla_User.data = row.Pla_User
    form.Pla_Password.data = row.Pla_Password
    session['prev_row']=str(row)
    session['is_new_row']=False
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
            try:
                session['deleted_row']=str(row)
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                logger.audit ( '%s:DEL:%s' % (current_user.username,session['deleted_row']) )
                flash('Platform %s deleted OK'%(Pla_Id))
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


    return render_template('platforms_delete.html', form=form, data=session.get('data'),row=row)

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

    if field is not None:
       next_url = url_for('.select_Platforms_query', field=field, value=value, page=rows.next_num) \
           if rows.has_next else None
       prev_url = url_for('.select_Platforms_query', field=field, value=value, page=rows.prev_num) \
           if rows.has_prev else None

    else:
       next_url = url_for('.select_Platforms_query', page=rows.next_num) \
           if rows.has_next else None
       prev_url = url_for('.select_Platforms_query', page=rows.prev_num) \
           if rows.has_prev else None

    return render_template('platforms_All.html',rows=rows)
# =============================================================================
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-18 18:05:34
# =============================================================================

@main.route('/forms/Rates', methods=['GET', 'POST'])
@login_required
@admin_required
def forms_Rates():
    """ Form handling function for table Rates """

    logger.debug('Enter: forms_Rates()')
    Rat_Id  =  request.args.get('Rat_Id',0,type=int)
    row =  rate.query.filter(rate.Rat_Id == Rat_Id).first()
    if row is None:
        row=rate()
        session['is_new_row']=True

    session['data'] =  { 'Rat_Id':row.Rat_Id, 'Typ_Code':row.Typ_Code, 'Cus_Id':row.Cus_Id, 'Pla_Id':row.Pla_Id, 'CC_Id':row.CC_Id, 'CI_Id':row.CI_Id, 'Rat_Price':row.Rat_Price, 'Cur_Code':row.Cur_Code, 'MU_Code':row.MU_Code, 'Rat_Period':row.Rat_Period, 'Rat_Type':row.Rat_Type}
    form = frm_rate()

    if form.has_FKs:
        form.Typ_Code.choices = db.session.query(cu_type.Typ_Code,cu_type.Typ_Description).order_by(cu_type.Typ_Description).all()
        form.Cus_Id.choices = db.session.query(customer.Cus_Id,customer.Cus_Name).order_by(customer.Cus_Name).all()
        form.Pla_Id.choices = db.session.query(platform.Pla_Id,platform.Pla_Name).order_by(platform.Pla_Name).all()
        form.CC_Id.choices = db.session.query(cost_center.CC_Id,cost_center.CC_Description).order_by(cost_center.CC_Description).all()
        form.CI_Id.choices = db.session.query(configuration_item.CI_Id,configuration_item.CI_Name).order_by(configuration_item.CI_Name).all()
        form.Cur_Code.choices = db.session.query(currency.Cur_Code,currency.Cur_Name).order_by(currency.Cur_Name).all()
        form.MU_Code.choices = db.session.query(measure_unit.MU_Code,measure_unit.MU_Description).order_by(measure_unit.MU_Description).all()
        form.Rat_Period.choices = db.session.query(rat_period.Rat_Period,rat_period.Value).order_by(rat_period.Value).all()

    if form.validate_on_submit():
        if     form.submit_Save.data and current_user.role_id>1:
            row.Typ_Code = form.Typ_Code.data
            row.Cus_Id = form.Cus_Id.data
            row.Pla_Id = form.Pla_Id.data
            row.CC_Id = form.CC_Id.data
            row.CI_Id = form.CI_Id.data
            row.Rat_Price = form.Rat_Price.data
            row.Cur_Code = form.Cur_Code.data
            row.MU_Code = form.MU_Code.data
            row.Rat_Period = form.Rat_Period.data
            try:
               session['new_row']=str(row)
               db.session.close()
               db.session.add(row)
               db.session.commit()
               if session['is_new_row']==True:
                   logger.audit ( '%s:NEW:%s' % (current_user.username,session['new_row'] ) )
                   flash('New Rate created OK')
               else:
                   logger.audit ( '%s:OLD:%s' % (current_user.username,session['prev_row']) )
                   logger.audit ( '%s:UPD:%s' % (current_user.username,session['new_row'] ) )
                   message=Markup('<b>Rate %s saved OK</b>'%(Rat_Id))
                   flash(message)
               db.session.close()
            except Exception as e:
               db.session.rollback()
               db.session.close()
               message=Markup('ERROR saving Rate record : %s'%(e))
               flash(message)
            return redirect(url_for('.select_Rates_query'))
        elif   form.submit_New.data and current_user.role_id>1:
            #print('New Data Here ...')
            session['is_new_row']=True
            db.session.close()
            row=rate()
            return redirect(url_for('.forms_Rates',Rat_Id=row.Rat_Id))

        elif   form.submit_Cancel.data:
            #print('Cancel Data Here ... does nothing')
            message=Markup('Rate Record modifications discarded ...')
            flash(message)
        else:
            #print('form validated but not submited ???')
            message=Markup('<b>Rate data modifications not allowed for user \'%s\'. Please contact Collector\'s Administrator ...</b>'%(current_user.username))
            flash(message)
            return redirect(url_for('.forms_Rates',Rat_Id=row.Rat_Id))

    form.Typ_Code.data = row.Typ_Code
    form.Cus_Id.data = row.Cus_Id
    form.Pla_Id.data = row.Pla_Id
    form.CC_Id.data = row.CC_Id
    form.CI_Id.data = row.CI_Id
    form.Rat_Price.data = row.Rat_Price
    form.Cur_Code.data = row.Cur_Code
    form.MU_Code.data = row.MU_Code
    form.Rat_Period.data = row.Rat_Period
    session['prev_row']=str(row)
    session['is_new_row']=False
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
    session['data'] =  { 'Rat_Id':row.Rat_Id, 'Typ_Code':row.Typ_Code, 'Cus_Id':row.Cus_Id, 'Pla_Id':row.Pla_Id, 'CC_Id':row.CC_Id, 'CI_Id':row.CI_Id, 'Rat_Price':row.Rat_Price, 'Cur_Code':row.Cur_Code, 'MU_Code':row.MU_Code, 'Rat_Period':row.Rat_Period, 'Rat_Type':row.Rat_Type}
    form = frm_rate_delete()

    if form.validate_on_submit():
        if  form.submit_Delete.data:
            print('Delete Data Here...')
            try:
                session['deleted_row']=str(row)
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                logger.audit ( '%s:DEL:%s' % (current_user.username,session['deleted_row']) )
                flash('Rate %s deleted OK'%(Rat_Id))
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


    return render_template('rates_delete.html', form=form, data=session.get('data'),row=row)

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
               .join(configuration_item,rate.CI_Id == configuration_item.CI_Id).add_columns(configuration_item.CI_Name)\
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
               .join(configuration_item,rate.CI_Id == configuration_item.CI_Id).add_columns(configuration_item.CI_Name)\
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
               .join(configuration_item,rate.CI_Id == configuration_item.CI_Id).add_columns(configuration_item.CI_Name)\
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
               .join(configuration_item,rate.CI_Id == configuration_item.CI_Id).add_columns(configuration_item.CI_Name)\
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
               .join(configuration_item,rate.CI_Id == configuration_item.CI_Id).add_columns(configuration_item.CI_Name)\
               .join(currency,rate.Cur_Code == currency.Cur_Code).add_columns(currency.Cur_Name)\
               .join(measure_unit,rate.MU_Code == measure_unit.MU_Code).add_columns(measure_unit.MU_Description)\
               .join(rat_period,rate.Rat_Period == rat_period.Rat_Period).add_columns(rat_period.Value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CI_Id':
            rows =  rate.query.filter_by(CI_Id=value)\
               .join(cu_type,rate.Typ_Code == cu_type.Typ_Code).add_columns(cu_type.Typ_Description)\
               .join(customer,rate.Cus_Id == customer.Cus_Id).add_columns(customer.Cus_Name)\
               .join(platform,rate.Pla_Id == platform.Pla_Id).add_columns(platform.Pla_Name)\
               .join(cost_center,rate.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .join(configuration_item,rate.CI_Id == configuration_item.CI_Id).add_columns(configuration_item.CI_Name)\
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
               .join(configuration_item,rate.CI_Id == configuration_item.CI_Id).add_columns(configuration_item.CI_Name)\
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
               .join(configuration_item,rate.CI_Id == configuration_item.CI_Id).add_columns(configuration_item.CI_Name)\
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
               .join(configuration_item,rate.CI_Id == configuration_item.CI_Id).add_columns(configuration_item.CI_Name)\
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
               .join(configuration_item,rate.CI_Id == configuration_item.CI_Id).add_columns(configuration_item.CI_Name)\
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
               .join(configuration_item,rate.CI_Id == configuration_item.CI_Id).add_columns(configuration_item.CI_Name)\
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
               .join(configuration_item,rate.CI_Id == configuration_item.CI_Id).add_columns(configuration_item.CI_Name)\
               .join(currency,rate.Cur_Code == currency.Cur_Code).add_columns(currency.Cur_Name)\
               .join(measure_unit,rate.MU_Code == measure_unit.MU_Code).add_columns(measure_unit.MU_Description)\
               .join(rat_period,rate.Rat_Period == rat_period.Rat_Period).add_columns(rat_period.Value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)

    if field is not None:
       next_url = url_for('.select_Rates_query', field=field, value=value, page=rows.next_num) \
           if rows.has_next else None
       prev_url = url_for('.select_Rates_query', field=field, value=value, page=rows.prev_num) \
           if rows.has_prev else None

    else:
       next_url = url_for('.select_Rates_query', page=rows.next_num) \
           if rows.has_next else None
       prev_url = url_for('.select_Rates_query', page=rows.prev_num) \
           if rows.has_prev else None

    return render_template('rates_All.html',rows=rows)
# =============================================================================
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-18 18:05:34
# =============================================================================

@main.route('/forms/Rat_Periods', methods=['GET', 'POST'])
@login_required
@admin_required
def forms_Rat_Periods():
    """ Form handling function for table Rat_Periods """

    logger.debug('Enter: forms_Rat_Periods()')
    Rat_Period  =  request.args.get('Rat_Period',0,type=int)
    row =  rat_period.query.filter(rat_period.Rat_Period == Rat_Period).first()
    if row is None:
        row=rat_period()
        session['is_new_row']=True

    session['data'] =  { 'Rat_Period':row.Rat_Period, 'Value':row.Value}
    form = frm_rat_period()

    if form.validate_on_submit():
        if     form.submit_Save.data and current_user.role_id>1:
            row.Rat_Period = form.Rat_Period.data
            row.Value = form.Value.data
            try:
               session['new_row']=str(row)
               db.session.close()
               db.session.add(row)
               db.session.commit()
               if session['is_new_row']==True:
                   logger.audit ( '%s:NEW:%s' % (current_user.username,session['new_row'] ) )
                   flash('New Rate Period created OK')
               else:
                   logger.audit ( '%s:OLD:%s' % (current_user.username,session['prev_row']) )
                   logger.audit ( '%s:UPD:%s' % (current_user.username,session['new_row'] ) )
                   message=Markup('<b>Rate Period %s saved OK</b>'%(Rat_Period))
                   flash(message)
               db.session.close()
            except Exception as e:
               db.session.rollback()
               db.session.close()
               message=Markup('ERROR saving Rate Period record : %s'%(e))
               flash(message)
            return redirect(url_for('.select_Rat_Periods_query'))
        elif   form.submit_New.data and current_user.role_id>1:
            #print('New Data Here ...')
            session['is_new_row']=True
            db.session.close()
            row=rat_period()
            return redirect(url_for('.forms_Rat_Periods'))

        elif   form.submit_Cancel.data:
            #print('Cancel Data Here ... does nothing')
            message=Markup('Rate Period Record modifications discarded ...')
            flash(message)
        else:
            #print('form validated but not submited ???')
            message=Markup('<b>Rate Period data modifications not allowed for user \'%s\'. Please contact Collector\'s Administrator ...</b>'%(current_user.username))
            flash(message)
            return redirect(url_for('.forms_Rat_Periods'))

    form.Rat_Period.data = row.Rat_Period
    form.Value.data = row.Value
    session['prev_row']=str(row)
    session['is_new_row']=False
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
            try:
                session['deleted_row']=str(row)
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                logger.audit ( '%s:DEL:%s' % (current_user.username,session['deleted_row']) )
                flash('Rate Period %s deleted OK'%(Rat_Period))
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


    return render_template('rat_periods_delete.html', form=form, data=session.get('data'),row=row)

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

    if field is not None:
       next_url = url_for('.select_Rat_Periods_query', field=field, value=value, page=rows.next_num) \
           if rows.has_next else None
       prev_url = url_for('.select_Rat_Periods_query', field=field, value=value, page=rows.prev_num) \
           if rows.has_prev else None

    else:
       next_url = url_for('.select_Rat_Periods_query', page=rows.next_num) \
           if rows.has_next else None
       prev_url = url_for('.select_Rat_Periods_query', page=rows.prev_num) \
           if rows.has_prev else None

    return render_template('rat_periods_All.html',rows=rows)
# =============================================================================
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-18 18:05:34
# =============================================================================

@main.route('/forms/Roles', methods=['GET', 'POST'])
@login_required
@admin_required
def forms_Roles():
    """ Form handling function for table Roles """

    logger.debug('Enter: forms_Roles()')
    id  =  request.args.get('id',0,type=int)
    row =  Role.query.filter(Role.id == id).first()
    if row is None:
        row=Role()
        session['is_new_row']=True

    session['data'] =  { 'id':row.id, 'name':row.name, 'default':row.default, 'permissions':row.permissions}
    form = frm_Role()

    if form.validate_on_submit():
        if     form.submit_Save.data and current_user.role_id>1:
            row.id = form.id.data
            row.name = form.name.data
            row.default = form.default.data
            row.permissions = form.permissions.data
            try:
               session['new_row']=str(row)
               db.session.close()
               db.session.add(row)
               db.session.commit()
               if session['is_new_row']==True:
                   logger.audit ( '%s:NEW:%s' % (current_user.username,session['new_row'] ) )
                   flash('New Role created OK')
               else:
                   logger.audit ( '%s:OLD:%s' % (current_user.username,session['prev_row']) )
                   logger.audit ( '%s:UPD:%s' % (current_user.username,session['new_row'] ) )
                   message=Markup('<b>Role %s saved OK</b>'%(id))
                   flash(message)
               db.session.close()
            except Exception as e:
               db.session.rollback()
               db.session.close()
               message=Markup('ERROR saving Role record : %s'%(e))
               flash(message)
            return redirect(url_for('.select_Roles_query'))
        elif   form.submit_New.data and current_user.role_id>1:
            #print('New Data Here ...')
            session['is_new_row']=True
            db.session.close()
            row=Role()
            return redirect(url_for('.forms_Roles'))

        elif   form.submit_Cancel.data:
            #print('Cancel Data Here ... does nothing')
            message=Markup('Role Record modifications discarded ...')
            flash(message)
        else:
            #print('form validated but not submited ???')
            message=Markup('<b>Role data modifications not allowed for user \'%s\'. Please contact Collector\'s Administrator ...</b>'%(current_user.username))
            flash(message)
            return redirect(url_for('.forms_Roles'))

    form.id.data = row.id
    form.name.data = row.name
    form.default.data = row.default
    form.permissions.data = row.permissions
    session['prev_row']=str(row)
    session['is_new_row']=False
    return render_template('roles.html', form=form, row=row)

# =============================================================================
@main.route('/forms/Roles_delete', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@admin_required
def forms_Roles_delete():
    """ Delete record handling function for table Roles """

    logger.debug('Enter: forms_Roles_delete()')
    id  =  request.args.get('id',0,type=int)
    row =  Role.query.filter(Role.id == id).first()
    if row is None:
        row=Role()
    session['data'] =  { 'id':row.id, 'name':row.name, 'default':row.default, 'permissions':row.permissions}
    form = frm_Role_delete()

    if form.validate_on_submit():
        if  form.submit_Delete.data:
            print('Delete Data Here...')
            try:
                session['deleted_row']=str(row)
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                logger.audit ( '%s:DEL:%s' % (current_user.username,session['deleted_row']) )
                flash('Role %s deleted OK'%(id))
            except exc.IntegrityError as e:
                db.session.rollback()
                flash('INTEGRITY ERROR: Are you sure there are no dependant records in other tables?')
                return redirect(url_for('.forms_Roles_delete',id=session['data']['id']))

            return redirect(url_for('.select_Roles_query'))
        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
            return redirect(url_for('.select_Roles_query'))
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.select_Roles_query'))


    return render_template('roles_delete.html', form=form, data=session.get('data'),row=row)

# =============================================================================
@main.route('/select/Roles_Query', methods=['GET','POST'])
@login_required
@admin_required
def select_Roles_query():
    """ Select rows handling function for table Roles """

    logger.debug('Enter: select_Roles_query()')
    field =  request.args.get('field',None,type=str)
    value =  request.args.get('value',0,type=str)
    page  =  request.args.get('page',1,type=int)

    if field is not None:
        if   field == 'id':
            rows =  Role.query.filter_by(id=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'name':
            rows =  Role.query.filter_by(name=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'default':
            rows =  Role.query.filter_by(default=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'permissions':
            rows =  Role.query.filter_by(permissions=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
    else:
       rows =  Role.query\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)

    if field is not None:
       next_url = url_for('.select_Roles_query', field=field, value=value, page=rows.next_num) \
           if rows.has_next else None
       prev_url = url_for('.select_Roles_query', field=field, value=value, page=rows.prev_num) \
           if rows.has_prev else None

    else:
       next_url = url_for('.select_Roles_query', page=rows.next_num) \
           if rows.has_next else None
       prev_url = url_for('.select_Roles_query', page=rows.prev_num) \
           if rows.has_prev else None

    return render_template('roles_All.html',rows=rows)
# =============================================================================
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-18 18:05:34
# =============================================================================

@main.route('/forms/ST_Use_Per_CU', methods=['GET', 'POST'])
@login_required
@admin_required
def forms_ST_Use_Per_CU():
    """ Form handling function for table ST_Use_Per_CU """

    logger.debug('Enter: forms_ST_Use_Per_CU()')
    CU_Id  =  request.args.get('CU_Id',0,type=int)
    From  =  request.args.get('From',0,type=int)
    To  =  request.args.get('To',0,type=int)
    row =  st_use_per_cu.query.filter(st_use_per_cu.CU_Id == CU_Id,st_use_per_cu.From == From,st_use_per_cu.To == To).first()
    if row is None:
        row=st_use_per_cu()
        session['is_new_row']=True

    session['data'] =  { 'CU_Id':row.CU_Id, 'From':row.From, 'To':row.To, 'Total_Slices':row.Total_Slices, 'Found_Slices':row.Found_Slices, 'Not_Found_Slices':row.Not_Found_Slices, 'Period_Initial_Q':row.Period_Initial_Q, 'Period_Increase':row.Period_Increase, 'Period_Increase_Count':row.Period_Increase_Count, 'Period_Reduction':row.Period_Reduction, 'Period_Reduction_Count':row.Period_Reduction_Count, 'Period_Final_Q':row.Period_Final_Q, 'CI_Id':row.CI_Id, 'CC_Id':row.CC_Id, 'Cus_Id':row.Cus_Id, 'Rat_Id':row.Rat_Id, 'Typ_Code':row.Typ_Code, 'Pla_Id':row.Pla_Id, 'Mean':row.Mean, 'Variance':row.Variance, 'StdDev':row.StdDev, 'Min':row.Min, 'Max':row.Max}
    form = frm_st_use_per_cu()

    if form.validate_on_submit():
        if     form.submit_Save.data and current_user.role_id>1:
            row.CU_Id = form.CU_Id.data
            row.From = form.From.data
            row.To = form.To.data
            row.Total_Slices = form.Total_Slices.data
            row.Found_Slices = form.Found_Slices.data
            row.Not_Found_Slices = form.Not_Found_Slices.data
            row.Period_Initial_Q = form.Period_Initial_Q.data
            row.Period_Increase = form.Period_Increase.data
            row.Period_Increase_Count = form.Period_Increase_Count.data
            row.Period_Reduction = form.Period_Reduction.data
            row.Period_Reduction_Count = form.Period_Reduction_Count.data
            row.Period_Final_Q = form.Period_Final_Q.data
            row.CI_Id = form.CI_Id.data
            row.CC_Id = form.CC_Id.data
            row.Cus_Id = form.Cus_Id.data
            row.Rat_Id = form.Rat_Id.data
            row.Typ_Code = form.Typ_Code.data
            row.Pla_Id = form.Pla_Id.data
            row.Mean = form.Mean.data
            row.Variance = form.Variance.data
            row.StdDev = form.StdDev.data
            row.Min = form.Min.data
            row.Max = form.Max.data
            try:
               session['new_row']=str(row)
               db.session.close()
               db.session.add(row)
               db.session.commit()
               if session['is_new_row']==True:
                   logger.audit ( '%s:NEW:%s' % (current_user.username,session['new_row'] ) )
                   flash('New ST_Use_Per_CU created OK')
               else:
                   logger.audit ( '%s:OLD:%s' % (current_user.username,session['prev_row']) )
                   logger.audit ( '%s:UPD:%s' % (current_user.username,session['new_row'] ) )
                   message=Markup('<b>ST_Use_Per_CU %s saved OK</b>'%(CU_Id,From,To))
                   flash(message)
               db.session.close()
            except Exception as e:
               db.session.rollback()
               db.session.close()
               message=Markup('ERROR saving ST_Use_Per_CU record : %s'%(e))
               flash(message)
            return redirect(url_for('.select_ST_Use_Per_CU_query'))
        elif   form.submit_New.data and current_user.role_id>1:
            #print('New Data Here ...')
            session['is_new_row']=True
            db.session.close()
            row=st_use_per_cu()
            return redirect(url_for('.forms_ST_Use_Per_CU'))

        elif   form.submit_Cancel.data:
            #print('Cancel Data Here ... does nothing')
            message=Markup('ST_Use_Per_CU Record modifications discarded ...')
            flash(message)
        else:
            #print('form validated but not submited ???')
            message=Markup('<b>ST_Use_Per_CU data modifications not allowed for user \'%s\'. Please contact Collector\'s Administrator ...</b>'%(current_user.username))
            flash(message)
            return redirect(url_for('.forms_ST_Use_Per_CU'))

    form.CU_Id.data = row.CU_Id
    form.From.data = row.From
    form.To.data = row.To
    form.Total_Slices.data = row.Total_Slices
    form.Found_Slices.data = row.Found_Slices
    form.Not_Found_Slices.data = row.Not_Found_Slices
    form.Period_Initial_Q.data = row.Period_Initial_Q
    form.Period_Increase.data = row.Period_Increase
    form.Period_Increase_Count.data = row.Period_Increase_Count
    form.Period_Reduction.data = row.Period_Reduction
    form.Period_Reduction_Count.data = row.Period_Reduction_Count
    form.Period_Final_Q.data = row.Period_Final_Q
    form.CI_Id.data = row.CI_Id
    form.CC_Id.data = row.CC_Id
    form.Cus_Id.data = row.Cus_Id
    form.Rat_Id.data = row.Rat_Id
    form.Typ_Code.data = row.Typ_Code
    form.Pla_Id.data = row.Pla_Id
    form.Mean.data = row.Mean
    form.Variance.data = row.Variance
    form.StdDev.data = row.StdDev
    form.Min.data = row.Min
    form.Max.data = row.Max
    session['prev_row']=str(row)
    session['is_new_row']=False
    return render_template('st_use_per_cu.html', form=form, row=row)

# =============================================================================
@main.route('/forms/ST_Use_Per_CU_delete', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@admin_required
def forms_ST_Use_Per_CU_delete():
    """ Delete record handling function for table ST_Use_Per_CU """

    logger.debug('Enter: forms_ST_Use_Per_CU_delete()')
    CU_Id  =  request.args.get('CU_Id',0,type=int)
    From  =  request.args.get('From',0,type=int)
    To  =  request.args.get('To',0,type=int)
    row =  st_use_per_cu.query.filter(st_use_per_cu.CU_Id == CU_Id,st_use_per_cu.From == From,st_use_per_cu.To == To).first()
    if row is None:
        row=st_use_per_cu()
    session['data'] =  { 'CU_Id':row.CU_Id, 'From':row.From, 'To':row.To, 'Total_Slices':row.Total_Slices, 'Found_Slices':row.Found_Slices, 'Not_Found_Slices':row.Not_Found_Slices, 'Period_Initial_Q':row.Period_Initial_Q, 'Period_Increase':row.Period_Increase, 'Period_Increase_Count':row.Period_Increase_Count, 'Period_Reduction':row.Period_Reduction, 'Period_Reduction_Count':row.Period_Reduction_Count, 'Period_Final_Q':row.Period_Final_Q, 'CI_Id':row.CI_Id, 'CC_Id':row.CC_Id, 'Cus_Id':row.Cus_Id, 'Rat_Id':row.Rat_Id, 'Typ_Code':row.Typ_Code, 'Pla_Id':row.Pla_Id, 'Mean':row.Mean, 'Variance':row.Variance, 'StdDev':row.StdDev, 'Min':row.Min, 'Max':row.Max}
    form = frm_st_use_per_cu_delete()

    if form.validate_on_submit():
        if  form.submit_Delete.data:
            print('Delete Data Here...')
            try:
                session['deleted_row']=str(row)
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                logger.audit ( '%s:DEL:%s' % (current_user.username,session['deleted_row']) )
                flash('ST_Use_Per_CU %s deleted OK'%(CU_Id,From,To))
            except exc.IntegrityError as e:
                db.session.rollback()
                flash('INTEGRITY ERROR: Are you sure there are no dependant records in other tables?')
                return redirect(url_for('.forms_ST_Use_Per_CU_delete',CU_Id=session['data']['CU_Id'],From=session['data']['From'],To=session['data']['To']))

            return redirect(url_for('.select_ST_Use_Per_CU_query'))
        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
            return redirect(url_for('.select_ST_Use_Per_CU_query'))
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.select_ST_Use_Per_CU_query'))


    return render_template('st_use_per_cu_delete.html', form=form, data=session.get('data'),row=row)

# =============================================================================
@main.route('/select/ST_Use_Per_CU_Query', methods=['GET','POST'])
@login_required
@admin_required
def select_ST_Use_Per_CU_query():
    """ Select rows handling function for table ST_Use_Per_CU """

    logger.debug('Enter: select_ST_Use_Per_CU_query()')
    field =  request.args.get('field',None,type=str)
    value =  request.args.get('value',0,type=str)
    page  =  request.args.get('page',1,type=int)

    if field is not None:
        if   field == 'CU_Id':
            rows =  st_use_per_cu.query.filter_by(CU_Id=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'From':
            rows =  st_use_per_cu.query.filter_by(From=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'To':
            rows =  st_use_per_cu.query.filter_by(To=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Total_Slices':
            rows =  st_use_per_cu.query.filter_by(Total_Slices=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Found_Slices':
            rows =  st_use_per_cu.query.filter_by(Found_Slices=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Not_Found_Slices':
            rows =  st_use_per_cu.query.filter_by(Not_Found_Slices=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Period_Initial_Q':
            rows =  st_use_per_cu.query.filter_by(Period_Initial_Q=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Period_Increase':
            rows =  st_use_per_cu.query.filter_by(Period_Increase=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Period_Increase_Count':
            rows =  st_use_per_cu.query.filter_by(Period_Increase_Count=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Period_Reduction':
            rows =  st_use_per_cu.query.filter_by(Period_Reduction=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Period_Reduction_Count':
            rows =  st_use_per_cu.query.filter_by(Period_Reduction_Count=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Period_Final_Q':
            rows =  st_use_per_cu.query.filter_by(Period_Final_Q=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CI_Id':
            rows =  st_use_per_cu.query.filter_by(CI_Id=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CC_Id':
            rows =  st_use_per_cu.query.filter_by(CC_Id=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Cus_Id':
            rows =  st_use_per_cu.query.filter_by(Cus_Id=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Rat_Id':
            rows =  st_use_per_cu.query.filter_by(Rat_Id=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Typ_Code':
            rows =  st_use_per_cu.query.filter_by(Typ_Code=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Pla_Id':
            rows =  st_use_per_cu.query.filter_by(Pla_Id=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Mean':
            rows =  st_use_per_cu.query.filter_by(Mean=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Variance':
            rows =  st_use_per_cu.query.filter_by(Variance=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'StdDev':
            rows =  st_use_per_cu.query.filter_by(StdDev=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Min':
            rows =  st_use_per_cu.query.filter_by(Min=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Max':
            rows =  st_use_per_cu.query.filter_by(Max=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
    else:
       rows =  st_use_per_cu.query\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)

    if field is not None:
       next_url = url_for('.select_ST_Use_Per_CU_query', field=field, value=value, page=rows.next_num) \
           if rows.has_next else None
       prev_url = url_for('.select_ST_Use_Per_CU_query', field=field, value=value, page=rows.prev_num) \
           if rows.has_prev else None

    else:
       next_url = url_for('.select_ST_Use_Per_CU_query', page=rows.next_num) \
           if rows.has_next else None
       prev_url = url_for('.select_ST_Use_Per_CU_query', page=rows.prev_num) \
           if rows.has_prev else None

    return render_template('st_use_per_cu_All.html',rows=rows)
# =============================================================================
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-18 18:05:34
# =============================================================================

@main.route('/forms/ST_Use_Per_Type', methods=['GET', 'POST'])
@login_required
@admin_required
def forms_ST_Use_Per_Type():
    """ Form handling function for table ST_Use_Per_Type """

    logger.debug('Enter: forms_ST_Use_Per_Type()')
    Typ_Code  =  request.args.get('Typ_Code',0,type=int)
    Cus_Id  =  request.args.get('Cus_Id',0,type=int)
    Pla_Id  =  request.args.get('Pla_Id',0,type=int)
    CC_Id  =  request.args.get('CC_Id',0,type=int)
    CI_Id  =  request.args.get('CI_Id',0,type=int)
    Year  =  request.args.get('Year',0,type=int)
    Month  =  request.args.get('Month',0,type=int)
    row =  st_use_per_type.query.filter(st_use_per_type.Typ_Code == Typ_Code,st_use_per_type.Cus_Id == Cus_Id,st_use_per_type.Pla_Id == Pla_Id,st_use_per_type.CC_Id == CC_Id,st_use_per_type.CI_Id == CI_Id,st_use_per_type.Year == Year,st_use_per_type.Month == Month).first()
    if row is None:
        row=st_use_per_type()
        session['is_new_row']=True

    session['data'] =  { 'Typ_Code':row.Typ_Code, 'Cus_Id':row.Cus_Id, 'Pla_Id':row.Pla_Id, 'CC_Id':row.CC_Id, 'CI_Id':row.CI_Id, 'Year':row.Year, 'Month':row.Month, 'Count':row.Count, 'Mean':row.Mean, 'Variance':row.Variance, 'StdDev':row.StdDev, 'Min':row.Min, 'Max':row.Max}
    form = frm_st_use_per_type()

    if form.validate_on_submit():
        if     form.submit_Save.data and current_user.role_id>1:
            row.Typ_Code = form.Typ_Code.data
            row.Cus_Id = form.Cus_Id.data
            row.Pla_Id = form.Pla_Id.data
            row.CC_Id = form.CC_Id.data
            row.CI_Id = form.CI_Id.data
            row.Year = form.Year.data
            row.Month = form.Month.data
            row.Count = form.Count.data
            row.Mean = form.Mean.data
            row.Variance = form.Variance.data
            row.StdDev = form.StdDev.data
            row.Min = form.Min.data
            row.Max = form.Max.data
            try:
               session['new_row']=str(row)
               db.session.close()
               db.session.add(row)
               db.session.commit()
               if session['is_new_row']==True:
                   logger.audit ( '%s:NEW:%s' % (current_user.username,session['new_row'] ) )
                   flash('New ST_Use_Per_Type created OK')
               else:
                   logger.audit ( '%s:OLD:%s' % (current_user.username,session['prev_row']) )
                   logger.audit ( '%s:UPD:%s' % (current_user.username,session['new_row'] ) )
                   message=Markup('<b>ST_Use_Per_Type %s saved OK</b>'%(Typ_Code,Cus_Id,Pla_Id,CC_Id,CI_Id,Year,Month))
                   flash(message)
               db.session.close()
            except Exception as e:
               db.session.rollback()
               db.session.close()
               message=Markup('ERROR saving ST_Use_Per_Type record : %s'%(e))
               flash(message)
            return redirect(url_for('.select_ST_Use_Per_Type_query'))
        elif   form.submit_New.data and current_user.role_id>1:
            #print('New Data Here ...')
            session['is_new_row']=True
            db.session.close()
            row=st_use_per_type()
            return redirect(url_for('.forms_ST_Use_Per_Type'))

        elif   form.submit_Cancel.data:
            #print('Cancel Data Here ... does nothing')
            message=Markup('ST_Use_Per_Type Record modifications discarded ...')
            flash(message)
        else:
            #print('form validated but not submited ???')
            message=Markup('<b>ST_Use_Per_Type data modifications not allowed for user \'%s\'. Please contact Collector\'s Administrator ...</b>'%(current_user.username))
            flash(message)
            return redirect(url_for('.forms_ST_Use_Per_Type'))

    form.Typ_Code.data = row.Typ_Code
    form.Cus_Id.data = row.Cus_Id
    form.Pla_Id.data = row.Pla_Id
    form.CC_Id.data = row.CC_Id
    form.CI_Id.data = row.CI_Id
    form.Year.data = row.Year
    form.Month.data = row.Month
    form.Count.data = row.Count
    form.Mean.data = row.Mean
    form.Variance.data = row.Variance
    form.StdDev.data = row.StdDev
    form.Min.data = row.Min
    form.Max.data = row.Max
    session['prev_row']=str(row)
    session['is_new_row']=False
    return render_template('st_use_per_type.html', form=form, row=row)

# =============================================================================
@main.route('/forms/ST_Use_Per_Type_delete', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@admin_required
def forms_ST_Use_Per_Type_delete():
    """ Delete record handling function for table ST_Use_Per_Type """

    logger.debug('Enter: forms_ST_Use_Per_Type_delete()')
    Typ_Code  =  request.args.get('Typ_Code',0,type=int)
    Cus_Id  =  request.args.get('Cus_Id',0,type=int)
    Pla_Id  =  request.args.get('Pla_Id',0,type=int)
    CC_Id  =  request.args.get('CC_Id',0,type=int)
    CI_Id  =  request.args.get('CI_Id',0,type=int)
    Year  =  request.args.get('Year',0,type=int)
    Month  =  request.args.get('Month',0,type=int)
    row =  st_use_per_type.query.filter(st_use_per_type.Typ_Code == Typ_Code,st_use_per_type.Cus_Id == Cus_Id,st_use_per_type.Pla_Id == Pla_Id,st_use_per_type.CC_Id == CC_Id,st_use_per_type.CI_Id == CI_Id,st_use_per_type.Year == Year,st_use_per_type.Month == Month).first()
    if row is None:
        row=st_use_per_type()
    session['data'] =  { 'Typ_Code':row.Typ_Code, 'Cus_Id':row.Cus_Id, 'Pla_Id':row.Pla_Id, 'CC_Id':row.CC_Id, 'CI_Id':row.CI_Id, 'Year':row.Year, 'Month':row.Month, 'Count':row.Count, 'Mean':row.Mean, 'Variance':row.Variance, 'StdDev':row.StdDev, 'Min':row.Min, 'Max':row.Max}
    form = frm_st_use_per_type_delete()

    if form.validate_on_submit():
        if  form.submit_Delete.data:
            print('Delete Data Here...')
            try:
                session['deleted_row']=str(row)
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                logger.audit ( '%s:DEL:%s' % (current_user.username,session['deleted_row']) )
                flash('ST_Use_Per_Type %s deleted OK'%(Typ_Code,Cus_Id,Pla_Id,CC_Id,CI_Id,Year,Month))
            except exc.IntegrityError as e:
                db.session.rollback()
                flash('INTEGRITY ERROR: Are you sure there are no dependant records in other tables?')
                return redirect(url_for('.forms_ST_Use_Per_Type_delete',Typ_Code=session['data']['Typ_Code'],Cus_Id=session['data']['Cus_Id'],Pla_Id=session['data']['Pla_Id'],CC_Id=session['data']['CC_Id'],CI_Id=session['data']['CI_Id'],Year=session['data']['Year'],Month=session['data']['Month']))

            return redirect(url_for('.select_ST_Use_Per_Type_query'))
        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
            return redirect(url_for('.select_ST_Use_Per_Type_query'))
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.select_ST_Use_Per_Type_query'))


    return render_template('st_use_per_type_delete.html', form=form, data=session.get('data'),row=row)

# =============================================================================
@main.route('/select/ST_Use_Per_Type_Query', methods=['GET','POST'])
@login_required
@admin_required
def select_ST_Use_Per_Type_query():
    """ Select rows handling function for table ST_Use_Per_Type """

    logger.debug('Enter: select_ST_Use_Per_Type_query()')
    field =  request.args.get('field',None,type=str)
    value =  request.args.get('value',0,type=str)
    page  =  request.args.get('page',1,type=int)

    if field is not None:
        if   field == 'Typ_Code':
            rows =  st_use_per_type.query.filter_by(Typ_Code=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Cus_Id':
            rows =  st_use_per_type.query.filter_by(Cus_Id=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Pla_Id':
            rows =  st_use_per_type.query.filter_by(Pla_Id=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CC_Id':
            rows =  st_use_per_type.query.filter_by(CC_Id=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CI_Id':
            rows =  st_use_per_type.query.filter_by(CI_Id=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Year':
            rows =  st_use_per_type.query.filter_by(Year=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Month':
            rows =  st_use_per_type.query.filter_by(Month=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Count':
            rows =  st_use_per_type.query.filter_by(Count=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Mean':
            rows =  st_use_per_type.query.filter_by(Mean=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Variance':
            rows =  st_use_per_type.query.filter_by(Variance=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'StdDev':
            rows =  st_use_per_type.query.filter_by(StdDev=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Min':
            rows =  st_use_per_type.query.filter_by(Min=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Max':
            rows =  st_use_per_type.query.filter_by(Max=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
    else:
       rows =  st_use_per_type.query\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)

    if field is not None:
       next_url = url_for('.select_ST_Use_Per_Type_query', field=field, value=value, page=rows.next_num) \
           if rows.has_next else None
       prev_url = url_for('.select_ST_Use_Per_Type_query', field=field, value=value, page=rows.prev_num) \
           if rows.has_prev else None

    else:
       next_url = url_for('.select_ST_Use_Per_Type_query', page=rows.next_num) \
           if rows.has_next else None
       prev_url = url_for('.select_ST_Use_Per_Type_query', page=rows.prev_num) \
           if rows.has_prev else None

    return render_template('st_use_per_type_All.html',rows=rows)
# =============================================================================
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-18 18:05:34
# =============================================================================

@main.route('/forms/Trace', methods=['GET', 'POST'])
@login_required
@admin_required
def forms_Trace():
    """ Form handling function for table Trace """

    logger.debug('Enter: forms_Trace()')
    ID  =  request.args.get('ID',0,type=int)
    row =  trace.query.filter(trace.ID == ID).first()
    if row is None:
        row=trace()
        session['is_new_row']=True

    session['data'] =  { 'ID':row.ID, 'LINE':row.LINE}
    form = frm_trace()

    if form.validate_on_submit():
        if     form.submit_Save.data and current_user.role_id>1:
            row.LINE = form.LINE.data
            try:
               session['new_row']=str(row)
               db.session.close()
               db.session.add(row)
               db.session.commit()
               if session['is_new_row']==True:
                   logger.audit ( '%s:NEW:%s' % (current_user.username,session['new_row'] ) )
                   flash('New Trace line created OK')
               else:
                   logger.audit ( '%s:OLD:%s' % (current_user.username,session['prev_row']) )
                   logger.audit ( '%s:UPD:%s' % (current_user.username,session['new_row'] ) )
                   message=Markup('<b>Trace line %s saved OK</b>'%(ID))
                   flash(message)
               db.session.close()
            except Exception as e:
               db.session.rollback()
               db.session.close()
               message=Markup('ERROR saving Trace line record : %s'%(e))
               flash(message)
            return redirect(url_for('.select_Trace_query'))
        elif   form.submit_New.data and current_user.role_id>1:
            #print('New Data Here ...')
            session['is_new_row']=True
            db.session.close()
            row=trace()
            return redirect(url_for('.forms_Trace',ID=row.ID))

        elif   form.submit_Cancel.data:
            #print('Cancel Data Here ... does nothing')
            message=Markup('Trace line Record modifications discarded ...')
            flash(message)
        else:
            #print('form validated but not submited ???')
            message=Markup('<b>Trace line data modifications not allowed for user \'%s\'. Please contact Collector\'s Administrator ...</b>'%(current_user.username))
            flash(message)
            return redirect(url_for('.forms_Trace',ID=row.ID))

    form.LINE.data = row.LINE
    session['prev_row']=str(row)
    session['is_new_row']=False
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
            try:
                session['deleted_row']=str(row)
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                logger.audit ( '%s:DEL:%s' % (current_user.username,session['deleted_row']) )
                flash('Trace line %s deleted OK'%(ID))
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


    return render_template('trace_delete.html', form=form, data=session.get('data'),row=row)

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

    if field is not None:
       next_url = url_for('.select_Trace_query', field=field, value=value, page=rows.next_num) \
           if rows.has_next else None
       prev_url = url_for('.select_Trace_query', field=field, value=value, page=rows.prev_num) \
           if rows.has_prev else None

    else:
       next_url = url_for('.select_Trace_query', page=rows.next_num) \
           if rows.has_next else None
       prev_url = url_for('.select_Trace_query', page=rows.prev_num) \
           if rows.has_prev else None

    return render_template('trace_All.html',rows=rows)
# =============================================================================
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-18 18:05:34
# =============================================================================

@main.route('/forms/Users', methods=['GET', 'POST'])
@login_required
@admin_required
def forms_Users():
    """ Form handling function for table Users """

    logger.debug('Enter: forms_Users()')
    id  =  request.args.get('id',0,type=int)
    row =  User.query.filter(User.id == id).first()
    if row is None:
        row=User()
        session['is_new_row']=True

    session['data'] =  { 'id':row.id, 'username':row.username, 'role_id':row.role_id, 'email':row.email, 'password_hash':row.password_hash, 'confirmed':row.confirmed, 'CC_Id':row.CC_Id}
    form = frm_User()

    if form.has_FKs:
        form.role_id.choices = db.session.query(Role.id,Role.name).order_by(Role.name).all()
        form.CC_Id.choices = db.session.query(cost_center.CC_Id,cost_center.CC_Description).order_by(cost_center.CC_Description).all()

    if form.validate_on_submit():
        if     form.submit_Save.data and current_user.role_id>1:
            row.username = form.username.data
            row.role_id = form.role_id.data
            row.email = form.email.data
            row.password_hash = form.password_hash.data
            row.confirmed = form.confirmed.data
            row.CC_Id = form.CC_Id.data
            try:
               session['new_row']=str(row)
               db.session.close()
               db.session.add(row)
               db.session.commit()
               if session['is_new_row']==True:
                   logger.audit ( '%s:NEW:%s' % (current_user.username,session['new_row'] ) )
                   flash('New User created OK')
               else:
                   logger.audit ( '%s:OLD:%s' % (current_user.username,session['prev_row']) )
                   logger.audit ( '%s:UPD:%s' % (current_user.username,session['new_row'] ) )
                   message=Markup('<b>User %s saved OK</b>'%(id))
                   flash(message)
               db.session.close()
            except Exception as e:
               db.session.rollback()
               db.session.close()
               message=Markup('ERROR saving User record : %s'%(e))
               flash(message)
            return redirect(url_for('.select_Users_query'))
        elif   form.submit_New.data and current_user.role_id>1:
            #print('New Data Here ...')
            session['is_new_row']=True
            db.session.close()
            row=User()
            return redirect(url_for('.forms_Users',Id=row.Id))

        elif   form.submit_Cancel.data:
            #print('Cancel Data Here ... does nothing')
            message=Markup('User Record modifications discarded ...')
            flash(message)
        else:
            #print('form validated but not submited ???')
            message=Markup('<b>User data modifications not allowed for user \'%s\'. Please contact Collector\'s Administrator ...</b>'%(current_user.username))
            flash(message)
            return redirect(url_for('.forms_Users',Id=row.Id))

    form.username.data = row.username
    form.role_id.data = row.role_id
    form.email.data = row.email
    form.password_hash.data = row.password_hash
    form.confirmed.data = row.confirmed
    form.CC_Id.data = row.CC_Id
    session['prev_row']=str(row)
    session['is_new_row']=False
    return render_template('users.html', form=form, row=row)

# =============================================================================
@main.route('/forms/Users_delete', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@admin_required
def forms_Users_delete():
    """ Delete record handling function for table Users """

    logger.debug('Enter: forms_Users_delete()')
    id  =  request.args.get('id',0,type=int)
    row =  User.query.filter(User.id == id).first()
    if row is None:
        row=User()
    session['data'] =  { 'id':row.id, 'username':row.username, 'role_id':row.role_id, 'email':row.email, 'password_hash':row.password_hash, 'confirmed':row.confirmed, 'CC_Id':row.CC_Id}
    form = frm_User_delete()

    if form.validate_on_submit():
        if  form.submit_Delete.data:
            print('Delete Data Here...')
            try:
                session['deleted_row']=str(row)
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                logger.audit ( '%s:DEL:%s' % (current_user.username,session['deleted_row']) )
                flash('User %s deleted OK'%(id))
            except exc.IntegrityError as e:
                db.session.rollback()
                flash('INTEGRITY ERROR: Are you sure there are no dependant records in other tables?')
                return redirect(url_for('.forms_Users_delete',id=session['data']['id']))

            return redirect(url_for('.select_Users_query'))
        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
            return redirect(url_for('.select_Users_query'))
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.select_Users_query'))


    return render_template('users_delete.html', form=form, data=session.get('data'),row=row)

# =============================================================================
@main.route('/select/Users_Query', methods=['GET','POST'])
@login_required
@admin_required
def select_Users_query():
    """ Select rows handling function for table Users """

    logger.debug('Enter: select_Users_query()')
    field =  request.args.get('field',None,type=str)
    value =  request.args.get('value',0,type=str)
    page  =  request.args.get('page',1,type=int)

    if field is not None:
        if   field == 'id':
            rows =  User.query.filter_by(id=value)\
               .join(Role,User.role_id == Role.role_id).add_columns(Role.name)\
               .join(cost_center,User.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'username':
            rows =  User.query.filter_by(username=value)\
               .join(Role,User.role_id == Role.role_id).add_columns(Role.name)\
               .join(cost_center,User.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'role_id':
            rows =  User.query.filter_by(role_id=value)\
               .join(Role,User.role_id == Role.role_id).add_columns(Role.name)\
               .join(cost_center,User.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'email':
            rows =  User.query.filter_by(email=value)\
               .join(Role,User.role_id == Role.role_id).add_columns(Role.name)\
               .join(cost_center,User.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'password_hash':
            rows =  User.query.filter_by(password_hash=value)\
               .join(Role,User.role_id == Role.role_id).add_columns(Role.name)\
               .join(cost_center,User.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'confirmed':
            rows =  User.query.filter_by(confirmed=value)\
               .join(Role,User.role_id == Role.role_id).add_columns(Role.name)\
               .join(cost_center,User.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CC_Id':
            rows =  User.query.filter_by(CC_Id=value)\
               .join(Role,User.role_id == Role.role_id).add_columns(Role.name)\
               .join(cost_center,User.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
    else:
       rows =  User.query\
               .join(Role,User.role_id == Role.role_id).add_columns(Role.name)\
               .join(cost_center,User.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)

    if field is not None:
       next_url = url_for('.select_Users_query', field=field, value=value, page=rows.next_num) \
           if rows.has_next else None
       prev_url = url_for('.select_Users_query', field=field, value=value, page=rows.prev_num) \
           if rows.has_prev else None

    else:
       next_url = url_for('.select_Users_query', page=rows.next_num) \
           if rows.has_next else None
       prev_url = url_for('.select_Users_query', page=rows.prev_num) \
           if rows.has_prev else None

    return render_template('users_All.html',rows=rows)
# =============================================================================
# =============================================================================
# View for Change_CIT_State
# (c) Sertechno 2018
# GLVH @ 2019-08-16
# =============================================================================

from emtec.collector.forms       import frm_change_cit_state,frm_change_cit_state_confirm
from babel.numbers  import format_number, format_decimal, format_percent
from sqlalchemy     import and_

@main.route('/forms/Change_CIT_State', methods=['GET', 'POST'])
@login_required
def forms_Change_CIT_State():
    logger.debug('Enter: forms_Change_CIT_State()'%())

    session['data'] =  {    'CU_Id': None, 
                            'CIT_Date_From':None, 
                            'CIT_Time_From':'00:00:00', 
                            'CIT_Date_To':None, 
                            'CIT_Time_To':'23:00:00', 
                            'CIT_Status':1,
                            'CIT_Status_To':1
                       }

    form = frm_change_cit_state()

    hours=[]
    for h in range(0,24):
        hh="%02d:00:00"%h
        hours.append((hh,hh))

    form.CU_Id.choices = db.session.query(charge_unit.CU_Id,charge_unit.CU_Description).order_by(charge_unit.CU_Description).all()
    form.CIT_Status.choices = db.session.query(cit_status.CIT_Status,cit_status.Value).all()
    form.CIT_Status_To.choices = db.session.query(cit_status.CIT_Status,cit_status.Value).all()
    form.CIT_Time_From.choices = hours
    form.CIT_Time_To.choices = hours
 
    if form.validate_on_submit():
        session['data']['CU_Id'         ] = form.CU_Id.data
        session['data']['CIT_Date_From' ] = form.CIT_Date_From.data
        session['data']['CIT_Time_From' ] = form.CIT_Time_From.data
        session['data']['CIT_Date_To'   ] = form.CIT_Date_To.data
        session['data']['CIT_Time_To'   ] = form.CIT_Time_To.data
        session['data']['CIT-Status'    ] = form.CIT_Status.data
        session['data']['CIT-Status_To' ] = form.CIT_Status_To.data
        if     form.submit_Search.data:
            # Get the Selected options index for string lists
            for i in range(len(form.CU_Id.choices)):
                if form.CU_Id.choices[i][0]==form.CU_Id.data:
                    cu_index=i
            return redirect(url_for('.report_Change_CIT_State_Confirm',
                                CU_Id           = form.CU_Id.data,
                                CU_Description        = form.CU_Id.choices[cu_index][1],
                                CIT_Date_From   = form.CIT_Date_From.data,
                                CIT_Time_From   = form.CIT_Time_From.data,
                                CIT_Date_To     = form.CIT_Date_To.data,
                                CIT_Time_To     = form.CIT_Time_To.data,
                                CIT_Status      = form.CIT_Status.data,
                                CIT_Status_Value= form.CIT_Status.choices[form.CIT_Status.data-1][1],
                                CIT_Status_To      = form.CIT_Status_To.data,
                                CIT_Status_To_Value= form.CIT_Status.choices[form.CIT_Status_To.data-1][1],
                                ))
        elif   form.submit_Cancel.data:
            flash('Search discarded ...')
        else:
            flash('form validated but not submited. Report to Support ...')
        return redirect(url_for('.forms_Change_CIT_State'))

    form.CU_Id.data        = session['data']['CU_Id']
    form.CIT_Date_From.data = session['data']['CIT_Date_From']
    form.CIT_Time_From.data = session['data']['CIT_Time_From']
    form.CIT_Date_To.data   = session['data']['CIT_Date_To']
    form.CIT_Time_To.data   = session['data']['CIT_Time_To']
    form.CIT_Status.data    = session['data']['CIT_Status']
    form.CIT_Status_To.data    = session['data']['CIT_Status_To']

    return render_template('change_cit_state.html',form=form, data=session.get('data'))

# =============================================================================

import simplejson as json
import datetime

@main.route('/report/Change_CIT_State_Confirm', methods=['GET','POST'])
@login_required
def report_Change_CIT_State_Confirm():
    logger.debug('Enter: report_Charging_Resume()')
    CU_Id          =  request.args.get('CU_Id',None,type=int)
    CU_Description        =  request.args.get('CU_Description',None,type=str)
    CIT_Date_From   =  request.args.get('CIT_Date_From',None,type=str)
    CIT_Time_From   =  request.args.get('CIT_Time_From',None,type=str)
    CIT_Date_To     =  request.args.get('CIT_Date_To',None,type=str)
    CIT_Time_To     =  request.args.get('CIT_Time_To',None,type=str)
    CIT_Status      =  request.args.get('CIT_Status',None,type=int)
    CIT_Status_Value=  request.args.get('CIT_Status_Value',None,type=str)
    CIT_Status_To      =  request.args.get('CIT_Status_To',None,type=int)
    CIT_Status_To_Value=  request.args.get('CIT_Status_To_Value',None,type=str)    

    # DateTime fields are required for correct searches & updates
    CIT_DateTime_From   =  '%s %s'%(CIT_Date_From,CIT_Time_From)
    CIT_DateTime_To     =  '%s %s'%(CIT_Date_To,CIT_Time_To)
    
    query = db.session.query(charge_item)\
                    .join(charge_unit).add_column(charge_unit.CU_UUID)\
                    .join(configuration_item)\
                    .filter(charge_item.CU_Id == CU_Id)\
                    .filter(charge_item.CIT_Status == CIT_Status)\
                    .filter(and_(   charge_item.CIT_DateTime >= CIT_DateTime_From,
                                    charge_item.CIT_DateTime <= CIT_DateTime_To
                                )
                            )
        
    rows=query.all()

    form = frm_change_cit_state_confirm()

    if form.validate_on_submit():
        if     form.submit_Change.data:
            # Aqui cambia efectivamente los datos
            query = db.session.query(charge_item)\
                    .filter(charge_item.CU_Id == CU_Id)\
                    .filter(charge_item.CIT_Status == CIT_Status)\
                    .filter(and_(   charge_item.CIT_DateTime >= CIT_DateTime_From,
                                    charge_item.CIT_DateTime <= CIT_DateTime_To
                                )
                            )
            rows=query.all()
                        
            try:
                count=0
                audit_records=[]
                for row in rows:
                    previous=str(row)
                    row.CIT_Status = CIT_Status_To
                    updated=str(row)
                    audit_records.append([previous,updated])
                    count += 1
                db.session.commit()
                flash("Charge Items status modified OK from '%s' to '%s' for %d records"%(CIT_Status_Value,CIT_Status_To_Value,count))
                for record in audit_records:
                    logger.audit("%s:OLD:%s"%(current_user.username,record[0]))
                    logger.audit("%s:UPD:%s"%(current_user.username,record[1]))
            except Exception as e:
                flash("Exception updating Charge Items: %s"%e)            
            return redirect(url_for('.forms_Change_CIT_State'))
        elif   form.submit_Cancel.data:
            flash('Change discarded ...')
        else:
            flash('form validated but not submited. Report to Support ...')
        return redirect(url_for('.forms_Change_CIT_State'))
    
    return render_template('change_cit_state_confirm.html',rows=rows,form=form,
                CU_Id=CU_Id,
                CU_Description=CU_Description,
                CIT_Date_From=CIT_Date_From,
                CIT_Time_From=CIT_Time_From,
                CIT_Date_To=CIT_Date_To,
                CIT_Time_To=CIT_Time_To,
                CIT_Status=CIT_Status,
                CIT_Status_Value=CIT_Status_Value,                
                CIT_Status_To=CIT_Status_To,
                CIT_Status_To_Value=CIT_Status_To_Value 
                )


# =============================================================================
# View for Get Charging Resume from DB
# (c) Sertechno 2018
# GLVH @ 2019-08-16
# =============================================================================

from emtec.collector.forms       import frm_charging_resume_all
from babel.numbers  import format_number, format_decimal, format_percent

@main.route('/forms/Get_Charging_Resume_All', methods=['GET', 'POST'])
@login_required
def forms_Get_Charging_Resume_All():
    logger.debug('Enter: forms_Get_Charging_Resume_All()')

    session['data'] =  { 'CIT_Date_From':None, 'CIT_Date_To':None, 'CIT_Status':1,'Cur_Code':'USD'}

    form = frm_charging_resume_all()

    # ------------------------------------------------------------------------------
    # Will setup filter to consider only Currencies with actual Exchange Rates in DB
    # Prepare query
    query = db.session.query(exchange_rate.Cur_Code.distinct().label('Cur_Code'))
    # Execute query and convert in list for further use in choices selection
    cur_choices = [row.Cur_Code for row in query.all()]

    form.CIT_Status.choices = db.session.query(cit_status.CIT_Status,cit_status.Value).all()
    form.Cur_Code.choices   = db.session.query(currency.Cur_Code,currency.Cur_Name).filter(currency.Cur_Code.in_(cur_choices)).all()

    if form.validate_on_submit():
        session['data']['CIT_Date_From' ] = form.CIT_Date_From.data
        session['data']['CIT_Date_To'   ] = form.CIT_Date_To.data
        session['data']['CIT-Status'    ] = form.CIT_Status.data
        session['data']['Cur_Code'      ] = form.Cur_Code.data
        if     form.submit_Report.data:
            # Get the Selected options index for string lists
            for i in range(len(form.Cur_Code.choices)):
                if form.Cur_Code.choices[i][0]==form.Cur_Code.data:
                    cur_index=i
            return redirect(url_for('.report_Charging_Resume_All',
                                Pla_Name        = form.Pla_Id.choices[pla_index][1],
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
            for i in range(len(form.Cur_Code.choices)):
                if form.Cur_Code.choices[i][0]==form.Cur_Code.data:
                    cur_index=i
            return redirect(url_for('.report_Charging_Resume_All',
                                Pla_Name        = form.Pla_Id.choices[pla_index][1],
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
        return redirect(url_for('.forms_Get_Charging_Resume_All'))

    form.CIT_Date_From.data = session['data']['CIT_Date_From']
    form.CIT_Date_To.data   = session['data']['CIT_Date_To']
    form.CIT_Status.data    = session['data']['CIT_Status']
    form.Cur_Code.data      = session['data']['Cur_Code']

    return render_template('get_charging_resume_all.html',form=form, data=session.get('data'))

# =============================================================================

import simplejson as json

@main.route('/report/Charging_Resume_All', methods=['GET','POST'])
@login_required
def report_Charging_Resume_All():
    logger.debug('Enter: report_Charging_Resume_All()')
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
        # query="CALL Update_Charge_Resume(%d,'%s','%s',%d,'%s')"%(Pla_Id,CIT_Date_From,CIT_Date_To,CIT_Status,Cur_Code) #
        # resume_records = db.engine.execute(query).scalar()                                                             #
        # -------------------------------------------------------------------------------------------------------------- #
        # 20181228 GV query = "SELECT DISTINCT CI_Id FROM Configuration_Items WHERE Pla_Id=%d"%(Pla_Id)
        query = "SELECT CI_Id FROM Configuration_Items ORDER BY CC_Id,CI_Id"
        
        logger.debug ("report_Changing_Resume_All: query: %s"%(query))

        CI = db.engine.execute(query)

        logger.debug ("report_Changing_Resume_All: %d CI's found "%(CI.rowcount))
        
        resume_records=0

        for ci in CI:
            query="CALL Update_Charge_Resume_CI2('%s','%s',%s,'%s',%s)"%\
                    (CIT_Date_From,CIT_Date_To,CIT_Status,Cur_Code,ci.CI_Id)
            logger.debug ("report_Changing_Resume_All: query: %s"%query)
            records=db.engine.execute(query)
            resume_records += records.scalar()

        logger.debug ("report_Changing_Resume_All: resume_records = %s"%resume_records)
        
    # Get Actual Remume Data from Database
    # NOTE: Here needs some Sand-Clock Message or something in case it takes so long ...
    query="CALL Get_Charge_Resume2(4,%d,'%s','%s',%d,'%s')"%(0,CIT_Date_From,CIT_Date_To,CIT_Status,Cur_Code)
    
    logger.debug ("report_Changing_Resume_All: query: %s"%query)
    
    rows =  db.engine.execute(query).fetchall()
    
    return render_template('report_charging_resume_all.html',rows=rows,
                CIT_Date_From=CIT_Date_From,
                CIT_Date_To=CIT_Date_To,
                CIT_Status=CIT_Status,
                CIT_Status_Value=CIT_Status_Value,                
                Cur_Code=Cur_Code,
                Cur_Name=Cur_Name
                )

# =============================================================================
# View for Get Charging Resume from DB per CC
# (c) Sertechno 2019
# GLVH @ 2019-08-16
# =============================================================================

from emtec.collector.forms       import frm_charging_resume_cc
from babel.numbers  import format_number, format_decimal, format_percent

@main.route('/forms/Get_Charging_Resume_CC', methods=['GET', 'POST'])
@login_required
def forms_Get_Charging_Resume_CC():
    logger.debug('Enter: forms_Get_Charging_Resume_CC()'%())

    session['data'] =  { 'CC_Id': None, 'CIT_Date_From':None, 'CIT_Date_To':None, 'CIT_Status':1,'Cur_Code':'USD'}

    form = frm_charging_resume_cc()

    # ------------------------------------------------------------------------------
    # Will setup filter to consider only Currencies with actual Exchange Rates in DB
    # Prepare query
    query = db.session.query(exchange_rate.Cur_Code.distinct().label('Cur_Code'))
    # Execute query and convert in list for further use in choices selection
    cur_choices = [row.Cur_Code for row in query.all()]

    form.CC_Id.choices      = db.session.query(cost_center.CC_Id,cost_center.CC_Description).all()
    form.CIT_Status.choices = db.session.query(cit_status.CIT_Status,cit_status.Value).all()
    form.Cur_Code.choices   = db.session.query(currency.Cur_Code,currency.Cur_Name).filter(currency.Cur_Code.in_(cur_choices)).all()

    if form.validate_on_submit():
        session['data']['CC_Id'         ] = form.CC_Id.data
        session['data']['CIT_Date_From' ] = form.CIT_Date_From.data
        session['data']['CIT_Date_To'   ] = form.CIT_Date_To.data
        session['data']['CIT-Status'    ] = form.CIT_Status.data
        session['data']['Cur_Code'      ] = form.Cur_Code.data
        if     form.submit_Report.data:
            # Get the Selected options index for string lists
            for i in range(len(form.CC_Id.choices)):
                if form.CC_Id.choices[i][0]==form.CC_Id.data:
                    cc_index=i
            for i in range(len(form.Cur_Code.choices)):
                if form.Cur_Code.choices[i][0]==form.Cur_Code.data:
                    cur_index=i
            return redirect(url_for('.report_Charging_Resume',
                                CC_Id           = form.CC_Id.data,
                                CC_Description  = form.CC_Id.choices[cc_index][1],
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
            for i in range(len(form.CC_Id.choices)):
                if form.CC_Id.choices[i][0]==form.CC_Id.data:
                    cc_index=i
            for i in range(len(form.Cur_Code.choices)):
                if form.Cur_Code.choices[i][0]==form.Cur_Code.data:
                    cur_index=i
            return redirect(url_for('.report_Charging_Resume_CC',
                                CC_Id           = form.CC_Id.data,
                                CC_Description  = form.CC_Id.choices[cc_index][1],
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

    form.CC_Id.data         = session['data']['CC_Id']
    form.CIT_Date_From.data = session['data']['CIT_Date_From']
    form.CIT_Date_To.data   = session['data']['CIT_Date_To']
    form.CIT_Status.data    = session['data']['CIT_Status']
    form.Cur_Code.data      = session['data']['Cur_Code']

    return render_template('charging_resume_cc.html',form=form, data=session.get('data'))

# =============================================================================

import simplejson as json

@main.route('/report/Charging_Resume_CC', methods=['GET','POST'])
@login_required
def report_Charging_Resume_CC():
    logger.debug('Enter: report_Charging_Resume()')
    CC_Id           =  request.args.get('CC_Id',None,type=int)
    CC_Description  =  request.args.get('CC_Description',None,type=str)
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
        # query="CALL Update_Charge_Resume(%d,'%s','%s',%d,'%s')"%(CC_Id,CIT_Date_From,CIT_Date_To,CIT_Status,Cur_Code) #
        # resume_records = db.engine.execute(query).scalar()                                                             #
        # -------------------------------------------------------------------------------------------------------------- #
        # 20181228 GV query = "SELECT DISTINCT CI_Id FROM Configuration_Items WHERE CC_Id=%d"%(CC_Id)
        query = "SELECT CI_Id "\
                    "FROM Configuration_Items "\
                        "WHERE CC_Id IN (SELECT CC_Id FROM Cost_Centers WHERE ccisbelow(CC_Id,%d)) "\
                        "ORDER BY CC_Id,CI_Id"%(CC_Id)
        
        logger.debug ("report_Changing_Resume: query: %s"%(query))

        CI = db.engine.execute(query)

        logger.debug ("report_Changing_Resume: %d CI's found for cost center %d"%(CI.rowcount,CC_Id))
        
        resume_records=0

        for ci in CI:
            query="CALL Update_Charge_Resume_CI2('%s','%s',%s,'%s',%s)"%\
                    (CIT_Date_From,CIT_Date_To,CIT_Status,Cur_Code,ci.CI_Id)
            logger.debug ("report_Changing_Resume: query: %s"%query)
            records=db.engine.execute(query)
            resume_records += records.scalar()

        logger.debug ("report_Changing_Resume: resume_records = %s"%resume_records)
        
    # Get Actual Remume Data from Database
    # NOTE: Here needs some Sand-Clock Message or something in case it takes so long ...
    query="CALL Get_Charge_Resume2(2,%d,'%s','%s',%d,'%s')"%(CC_Id,CIT_Date_From,CIT_Date_To,CIT_Status,Cur_Code)
    
    logger.debug ("report_Changing_Resume: query: %s"%query)
    
    rows =  db.engine.execute(query).fetchall()
    
    return render_template('report_charging_resume_cc.html',rows=rows,
                CC_Id=CC_Id,
                CC_Description=CC_Description,
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
# GLVH @ 2019-08-16
# =============================================================================

from emtec.collector.forms       import frm_charging_resume_level
from babel.numbers  import format_number, format_decimal, format_percent

@main.route('/forms/Get_Charging_Resume_Level', methods=['GET', 'POST'])
@login_required
def forms_Get_Charging_Resume_Level():
    logger.debug('Enter: forms_Get_Charging_Resume()'%())

    session['data'] =  { 'Cus_Id': None, 'CIT_Date_From':None, 'CIT_Date_To':None, 'CIT_Status':1,'Cur_Code':'USD','Level':1}

    form = frm_charging_resume_level()

    # ------------------------------------------------------------------------------
    # Will setup filter to consider only Currencies with actual Exchange Rates in DB
    # Prepare query
    query = db.session.query(exchange_rate.Cur_Code.distinct().label('Cur_Code'))
    # Execute query and convert in list for further use in choices selection
    cur_choices = [row.Cur_Code for row in query.all()]

    form.Cus_Id.choices     = db.session.query(customer.Cus_Id,customer.Cus_Name).all()
    form.CIT_Status.choices = db.session.query(cit_status.CIT_Status,cit_status.Value).all()
    form.Cur_Code.choices   = db.session.query(currency.Cur_Code,currency.Cur_Name).filter(currency.Cur_Code.in_(cur_choices)).all()
    form.Level.choices      = [(1,"Cost Center"),(2,"Device"),(3,"Component")]

    if form.validate_on_submit():
        session['data']['Cus_Id'        ] = form.Cus_Id.data
        session['data']['CIT_Date_From' ] = form.CIT_Date_From.data
        session['data']['CIT_Date_To'   ] = form.CIT_Date_To.data
        session['data']['CIT-Status'    ] = form.CIT_Status.data
        session['data']['Cur_Code'      ] = form.Cur_Code.data
        session['data']['Level'         ] = form.Level.data
        
        if     form.submit_Report.data:
            # Get the Selected options index for string lists
            for i in range(len(form.Cus_Id.choices)):
                if form.Cus_Id.choices[i][0]==form.Cus_Id.data:
                    cus_index=i
            for i in range(len(form.Cur_Code.choices)):
                if form.Cur_Code.choices[i][0]==form.Cur_Code.data:
                    cur_index=i
            for i in range(len(form.Level.choices)):
                if form.Level.choices[i][0]==form.Level.data:
                    level_index=i
            return redirect(url_for('.report_Charging_Resume_Level',
                                Cus_Id          = form.Cus_Id.data,
                                Cus_Name        = form.Cus_Id.choices[cus_index][1],
                                CIT_Date_From   = form.CIT_Date_From.data,
                                CIT_Date_To     = form.CIT_Date_To.data,
                                CIT_Status      = form.CIT_Status.data,
                                CIT_Status_Value= form.CIT_Status.choices[form.CIT_Status.data-1][1],
                                Cur_Code        = form.Cur_Code.data,
                                Cur_Name        = form.Cur_Code.choices[cur_index][1],
                                Level           = form.Level.choices[level_index][1],
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
            for i in range(len(form.Level.choices)):
                if form.Level.choices[i][0]==form.Level.data:
                    level_index=i
            return redirect(url_for('.report_Charging_Resume_Level',
                                Cus_Id          = form.Cus_Id.data,
                                Cus_Name        = form.Cus_Id.choices[cus_index][1],
                                CIT_Date_From   = form.CIT_Date_From.data,
                                CIT_Date_To     = form.CIT_Date_To.data,
                                CIT_Status      = form.CIT_Status.data,
                                CIT_Status_Value= form.CIT_Status.choices[form.CIT_Status.data-1][1],
                                Cur_Code        = form.Cur_Code.data,
                                Cur_Name        = form.Cur_Code.choices[cur_index][1],
                                Level           = form.Level.choices[level_index][1],
                                Update          = 1
                                ))

        elif   form.submit_Cancel.data:
            #print('Cancel Data Here ... does nothing')
            flash('Report discarded ...')
        else:
            flash('form validated but not submited. Report to Support ...')
            #print('form validated but not submited ???')
        return redirect(url_for('.forms_Get_Charging_Resume_Level'))

    form.Cus_Id.data        = session['data']['Cus_Id']
    form.CIT_Date_From.data = session['data']['CIT_Date_From']
    form.CIT_Date_To.data   = session['data']['CIT_Date_To']
    form.CIT_Status.data    = session['data']['CIT_Status']
    form.Cur_Code.data      = session['data']['Cur_Code']
    form.Level.data         = session['data']['Level']

    return render_template('charging_resume_level.html',form=form, data=session.get('data'))

# =============================================================================

import simplejson as json

@main.route('/report/Charging_Resume_Level', methods=['GET','POST'])
@login_required
def report_Charging_Resume_Level():
    logger.debug('Enter: report_Charging_Resume_Level()')
    Cus_Id          =  request.args.get('Cus_Id',None,type=int)
    Cus_Name        =  request.args.get('Cus_Name',None,type=str)
    CIT_Date_From   =  request.args.get('CIT_Date_From',None,type=str)
    CIT_Date_To     =  request.args.get('CIT_Date_To',None,type=str)
    CIT_Status      =  request.args.get('CIT_Status',None,type=int)
    CIT_Status_Value=  request.args.get('CIT_Status_Value',None,type=str)
    Cur_Code        =  request.args.get('Cur_Code',None,type=str)
    Cur_Name        =  request.args.get('Cur_Name',None,type=str)
    Level           =  request.args.get('Level',None,type=str)
    Update          =  request.args.get('Update',0,type=int)
    
    
    # Updated cached data for this specific query if requested 
    if Update == 1:
        # -------------------------------------------------------------------------------------------------------------- #
        # Previous Code faster but requires more memory will be replaced by an by CI loop                                #
        # query="CALL Update_Charge_Resume(%d,'%s','%s',%d,'%s')"%(Cus_Id,CIT_Date_From,CIT_Date_To,CIT_Status,Cur_Code) #
        # resume_records = db.engine.execute(query).scalar()                                                             #
        # -------------------------------------------------------------------------------------------------------------- #
        # 20181228 GV query = "SELECT DISTINCT CI_Id FROM Configuration_Items WHERE Cus_Id=%d"%(Cus_Id)
        query = "SELECT CI_Id FROM Configuration_Items WHERE Cus_Id=%d ORDER BY CC_Id,CI_Id"%(Cus_Id)
        
        logger.debug ("report_Changing_Resume_Level: query: %s"%(query))

        CI = db.engine.execute(query)

        logger.debug ("report_Changing_Resume_Level: %d CI's found for customer %d"%(CI.rowcount,Cus_Id))
        
        resume_records=0

        for ci in CI:
            query="CALL Update_Charge_Resume_CI(%s,'%s','%s',%s,'%s',%s)"%\
                    (Cus_Id,CIT_Date_From,CIT_Date_To,CIT_Status,Cur_Code,ci.CI_Id)
            logger.debug ("report_Changing_Resume_Level: query: %s"%query)
            records=db.engine.execute(query)
            resume_records += records.scalar()

        logger.debug ("report_Changing_Resume_Level: resume_records = %s"%resume_records)
        
    # Get Actual Remume Data from Database
    # NOTE: Here needs some Sand-Clock Message or something in case it takes so long ...
    query="CALL Get_Charge_Resume(%d,'%s','%s',%d,'%s')"%(Cus_Id,CIT_Date_From,CIT_Date_To,CIT_Status,Cur_Code)
    
    logger.debug ("report_Changing_Resume_Level: query: %s"%query)
    
    rows =  db.engine.execute(query).fetchall()
    
    return render_template('report_charging_resume_level.html',rows=rows,
                Cus_Id=Cus_Id,
                Cus_Name=Cus_Name,
                CIT_Date_From=CIT_Date_From,
                CIT_Date_To=CIT_Date_To,
                CIT_Status=CIT_Status,
                CIT_Status_Value=CIT_Status_Value,                
                Cur_Code=Cur_Code,
                Cur_Name=Cur_Name,
                Level=Level
                )

# =============================================================================
# View for Get Charging Resume from DB
# (c) Sertechno 2018
# GLVH @ 2019-08-16
# =============================================================================

from emtec.collector.forms       import frm_charging_resume_platform
from babel.numbers  import format_number, format_decimal, format_percent

@main.route('/forms/Get_Charging_Resume_Platform', methods=['GET', 'POST'])
@login_required
def forms_Get_Charging_Resume_Platform():
    logger.debug('Enter: forms_Get_Charging_Resume_Platform()')

    session['data'] =  { 'Pla_Id': None, 'CIT_Date_From':None, 'CIT_Date_To':None, 'CIT_Status':1,'Cur_Code':'USD'}

    form = frm_charging_resume_platform()

    # ------------------------------------------------------------------------------
    # Will setup filter to consider only Currencies with actual Exchange Rates in DB
    # Prepare query
    query = db.session.query(exchange_rate.Cur_Code.distinct().label('Cur_Code'))
    # Execute query and convert in list for further use in choices selection
    cur_choices = [row.Cur_Code for row in query.all()]

    form.Pla_Id.choices     = db.session.query(platform.Pla_Id,platform.Pla_Name).all()
    form.CIT_Status.choices = db.session.query(cit_status.CIT_Status,cit_status.Value).all()
    form.Cur_Code.choices   = db.session.query(currency.Cur_Code,currency.Cur_Name).filter(currency.Cur_Code.in_(cur_choices)).all()

    if form.validate_on_submit():
        session['data']['Pla_Id'        ] = form.Pla_Id.data
        session['data']['CIT_Date_From' ] = form.CIT_Date_From.data
        session['data']['CIT_Date_To'   ] = form.CIT_Date_To.data
        session['data']['CIT-Status'    ] = form.CIT_Status.data
        session['data']['Cur_Code'      ] = form.Cur_Code.data
        if     form.submit_Report.data:
            # Get the Selected options index for string lists
            for i in range(len(form.Pla_Id.choices)):
                if form.Pla_Id.choices[i][0]==form.Pla_Id.data:
                    pla_index=i
            for i in range(len(form.Cur_Code.choices)):
                if form.Cur_Code.choices[i][0]==form.Cur_Code.data:
                    cur_index=i
            return redirect(url_for('.report_Charging_Resume_Platform',
                                Pla_Id          = form.Pla_Id.data,
                                Pla_Name        = form.Pla_Id.choices[pla_index][1],
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
            for i in range(len(form.Pla_Id.choices)):
                if form.Pla_Id.choices[i][0]==form.Pla_Id.data:
                    pla_index=i
            for i in range(len(form.Cur_Code.choices)):
                if form.Cur_Code.choices[i][0]==form.Cur_Code.data:
                    cur_index=i
            return redirect(url_for('.report_Charging_Resume_Platform',
                                Pla_Id          = form.Pla_Id.data,
                                Pla_Name        = form.Pla_Id.choices[pla_index][1],
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
        return redirect(url_for('.forms_Get_Charging_Resume_Platform'))

    form.Pla_Id.data        = session['data']['Pla_Id']
    form.CIT_Date_From.data = session['data']['CIT_Date_From']
    form.CIT_Date_To.data   = session['data']['CIT_Date_To']
    form.CIT_Status.data    = session['data']['CIT_Status']
    form.Cur_Code.data      = session['data']['Cur_Code']

    return render_template('get_charging_resume.html',form=form, data=session.get('data'))

# =============================================================================

import simplejson as json

@main.route('/report/Charging_Resume_Platform', methods=['GET','POST'])
@login_required
def report_Charging_Resume_Platform():
    logger.debug('Enter: report_Charging_Resume_Platform()')
    Pla_Id          =  request.args.get('Pla_Id',None,type=int)
    Pla_Name        =  request.args.get('Pla_Name',None,type=str)
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
        # query="CALL Update_Charge_Resume(%d,'%s','%s',%d,'%s')"%(Pla_Id,CIT_Date_From,CIT_Date_To,CIT_Status,Cur_Code) #
        # resume_records = db.engine.execute(query).scalar()                                                             #
        # -------------------------------------------------------------------------------------------------------------- #
        # 20181228 GV query = "SELECT DISTINCT CI_Id FROM Configuration_Items WHERE Pla_Id=%d"%(Pla_Id)
        query = "SELECT CI_Id FROM Configuration_Items WHERE Pla_Id=%d ORDER BY CC_Id,CI_Id"%(Pla_Id)
        
        logger.debug ("report_Changing_Resume_Platform: query: %s"%(query))

        CI = db.engine.execute(query)

        logger.debug ("report_Changing_Resume_Platform: %d CI's found for platform %d"%(CI.rowcount,Pla_Id))
        
        resume_records=0

        for ci in CI:
            query="CALL Update_Charge_Resume_CI2('%s','%s',%s,'%s',%s)"%\
                    (CIT_Date_From,CIT_Date_To,CIT_Status,Cur_Code,ci.CI_Id)
            logger.debug ("report_Changing_Resume_Platform: query: %s"%query)
            records=db.engine.execute(query)
            resume_records += records.scalar()

        logger.debug ("report_Changing_Resume_Platform: resume_records = %s"%resume_records)
        
    # Get Actual Remume Data from Database
    # NOTE: Here needs some Sand-Clock Message or something in case it takes so long ...
    query="CALL Get_Charge_Resume2(3,%d,'%s','%s',%d,'%s')"%(Pla_Id,CIT_Date_From,CIT_Date_To,CIT_Status,Cur_Code)
    
    logger.debug ("report_Changing_Resume: query: %s"%query)
    
    rows =  db.engine.execute(query).fetchall()
    
    return render_template('report_charging_resume_platform.html',rows=rows,
                Pla_Id=Pla_Id,
                Pla_Name=Pla_Name,
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
# GLVH @ 2019-08-16
# =============================================================================

from emtec.collector.forms       import frm_charging_resume
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

    #return render_template('get_charging_resume.html',form=form, data=session.get('data'))
    return render_template('charging_resume.html',form=form, data=session.get('data'))

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
        # 20181228 GV query = "SELECT DISTINCT CI_Id FROM Configuration_Items WHERE Cus_Id=%d"%(Cus_Id)
        query = "SELECT CI_Id FROM Configuration_Items WHERE Cus_Id=%d ORDER BY CC_Id,CI_Id"%(Cus_Id)
        
        logger.debug ("report_Changing_Resume: query: %s"%(query))

        CI = db.engine.execute(query)

        logger.debug ("report_Changing_Resume: %d CI's found for customer %d"%(CI.rowcount,Cus_Id))
        
        resume_records=0

        for ci in CI:
            query="CALL Update_Charge_Resume_CI(%s,'%s','%s',%s,'%s',%s)"%\
                    (Cus_Id,CIT_Date_From,CIT_Date_To,CIT_Status,Cur_Code,ci.CI_Id)
            logger.debug ("report_Changing_Resume: query: %s"%query)
            records=db.engine.execute(query)
            resume_records += records.scalar()

        logger.debug ("report_Changing_Resume: resume_records = %s"%resume_records)
        
    # Get Actual Remume Data from Database
    # NOTE: Here needs some Sand-Clock Message or something in case it takes so long ...
    query="CALL Get_Charge_Resume(%d,'%s','%s',%d,'%s')"%(Cus_Id,CIT_Date_From,CIT_Date_To,CIT_Status,Cur_Code)
    
    logger.debug ("report_Changing_Resume: query: %s"%query)
    
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
# (c) Sertechno 2018,2019
# GLVH @ 2019-03-11
# =============================================================================


# Support Constants, Variables & Functions
RAT_TYPE        =0x01
RAT_PLATFORM    =0x02
RAT_CUSTOMER    =0x04
RAT_CC          =0x08
RAT_CI          =0x10

Valid_Rat_Types = [     RAT_TYPE,
                        RAT_TYPE|RAT_PLATFORM,
                        RAT_TYPE|RAT_PLATFORM|RAT_CUSTOMER,
                        RAT_TYPE|RAT_PLATFORM|RAT_CUSTOMER|RAT_CC,
                        RAT_TYPE|RAT_PLATFORM|RAT_CUSTOMER|RAT_CC|RAT_CI
                ]

def Get_Rat_Type(Rate):
    rate_type           =  0x00
    if Rate.Typ_Code    != 'NUL'   :   rate_type |= RAT_TYPE    
    if Rate.Pla_Id      != 1         :   rate_type |= RAT_PLATFORM
    if Rate.Cus_Id      != 1         :   rate_type |= RAT_CUSTOMER
    if Rate.CC_Id       != 1         :   rate_type |= RAT_CC
    if Rate.CI_Id       != 1         :   rate_type |= RAT_CI
    return rate_type

def is_valid_rate(Rate):
    return Rate in Valid_Rat_Types
    

def Update_Rates_Type():
    
    rate_rows=rate.query.all()
    for rat in rate_rows:
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
    
    ci_rows=db.session.query(configuration_item)\
                .join(customer)                                                 .add_column(customer.Cus_Name)\
                .join(platform)                                                 .add_column(platform.Pla_Name)\
                .join(cost_center,cost_center.CC_Id==configuration_item.CC_Id)  .add_column(cost_center.CC_Description)\
                .filter(or_(    configuration_item.CC_Id==customer.CC_Id\
                                ,configuration_item.CC_Id==1))\
                .all()
                
    data.update({'ci_rows': ci_rows})
    
    # Updates Rate Types in Rates Table in order to validate them in report
    Update_Rates_Type()
    
    """
    query=db.session.query(rate)\
                .join(customer)                                                 .add_column(customer.Cus_Name)\
                .join(platform)                                                 .add_column(platform.Pla_Name)\
                .join(configuration_item)                                       .add_column(configuration_item.CI_Name)\
                .join(cost_center,cost_center.CC_Id==rate.CC_Id)                .add_column(cost_center.CC_Description)\
                .order_by(rate.Pla_Id,rate.Cus_Id,rate.CC_Id,rate.CI_Id,rate.Typ_Code)
    
    flash(query)
    """
    """
    rate_rows=None
    rate_rows=db.session.query(rate)\
                .join(customer)                                                 .add_column(customer.Cus_Name)\
                .join(platform)                                                 .add_column(platform.Pla_Name)\
                .join(configuration_item)                                       .add_column(configuration_item.CI_Name)\
                .join(cost_center,cost_center.CC_Id==rate.CC_Id)                .add_column(cost_center.CC_Description)\
                .order_by(rate.Pla_Id,rate.Cus_Id,rate.CC_Id,rate.CI_Id,rate.Typ_Code)\
                .all()
    """
    query = "SELECT * "\
                "FROM Rates "\
                    "JOIN Customers             USING   (Cus_Id) "\
                    "JOIN Platforms             USING   (Pla_Id) "\
                    "JOIN Configuration_Items   USING   (CI_Id) "\
                    "JOIN Cost_Centers          ON      Cost_Centers.CC_Id=Rates.CC_id "\
                "ORDER BY Typ_Code,Rates.Pla_Id,Rates.Cus_Id,Rates.CC_Id,Rates.CI_Id"
    
    rate_rows=[]

    try:
        rate_rows = db.session.execute(query).fetchall()
    except Exception as e:
        print("**************************************")
        print(e)
        print("**************************************")

    data.update({'rate_rows': rate_rows})

    query = "SELECT CU_Id,CU_Description,Typ_Code,Pla_Id,Cus_Id,CI.CC_Id AS CC_ID,Rat_Id,"\
                    "Get_Rate_Id (Typ_Code,Pla_Id,Cus_Id,CI.CC_Id,CU_Id) AS RATE, "\
                    "Pla_Name,Cus_Name,CC_Description,CI_Name "\
                "FROM Charge_Units AS CU "\
                    "JOIN Configuration_Items AS CI  USING (CI_Id) "\
                    "JOIN Platforms           AS PLA USING (Pla_Id) "\
                    "JOIN Customers           AS CUS USING (Cus_Id) "\
                    "JOIN Cost_Centers        AS CC  ON CC.CC_Id = CI.CC_Id "\
                "WHERE Rat_Id != Get_Rate_Id(Typ_Code,Pla_Id,Cus_Id,CI.CC_Id,CU_Id)"

    cu_rows = []
    
    try:
        cu_rows = db.session.execute(query).fetchall()
    except Exception as e:
        print("**************************************")
        print(e)
        print("**************************************")

    data.update({'cu_rows': cu_rows})

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
# GLVH @ 2019-08-16
# =============================================================================

from emtec.collector.forms       import frm_export_Charging_Resume
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

# =============================================================================
# View for Get Billing Resume from DB
# (c) Sertechno 2019
# GLVH @ 2019-08-16
# =============================================================================

from emtec.collector.forms       import frm_export_User_Resume
from babel.numbers  import format_number, format_decimal, format_percent

@main.route('/forms/Export_User_Resume', methods=['GET', 'POST'])
@login_required
def forms_Export_User_Resume():
    logger.debug('Enter: forms_Export_User_Resume()'%())

    session['data'] =  { 'Cus_Id': None, 'CIT_Date_From':None, 'CIT_Date_To':None, 'CIT_Status':1,'Cur_Code':'USD'}

    form = frm_export_User_Resume()
    """
    query = "SELECT COUNT(*) AS RECORDS,Cus_Id,CR_Date_From,CR_Date_To,CIT_Status,Cur_Code,Cus_Name FROM User_Resumes "\
                "WHERE CI_CC_Id IN (SELECT CC_Id from Cost_Centers WHERE usercancc(%s,CC_Id)) "\
                "GROUP BY Cus_Id,CR_Date_From,CR_Date_To,CIT_Status,Cur_Code,Cus_Name "\
                "ORDER BY Cus_Id,CR_Date_From,CR_Date_To,CIT_Status,Cur_Code"%current_user.id
    """
    query = "SELECT COUNT(*) AS RECORDS,CI_CC_Id,CR_Date_From,CR_Date_To,CIT_Status,Cur_Code,CC_Description FROM User_Resumes "\
                "WHERE CI_CC_Id IN (SELECT CC_Id from Cost_Centers WHERE usercancc(%s,CC_Id)) "\
                "GROUP BY CI_CC_Id,CR_Date_From,CR_Date_To,CIT_Status,Cur_Code,CC_Description "\
                "ORDER BY CI_CC_Id,CR_Date_From,CR_Date_To,CIT_Status,Cur_Code"%current_user.id



    """
select count(*),CC_Description,CR_Date_From,CR_Date_To,CIT_Status,Cur_Code
from User_Resumes
group by CC_Description,CR_Date_From,CR_Date_To,CIT_Status,Cur_Code;
    """                
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
    """
    for row in rows:
        option="%s_%s_%s_%s_%s_%s"%(row.Cus_Id,row.CR_Date_From,row.CR_Date_To,row.CIT_Status,row.Cur_Code,row.Cus_Name)
        print("option split=",option.split("_"))
        value ="%s from %s to %s status=%s currency=%s"%(row.Cus_Name,row.CR_Date_From,row.CR_Date_To,dstatuses[row.CIT_Status],dcurrencies[row.Cur_Code])
        export_choices.append((option,value))
    """
    for row in rows:
        option="%s_%s_%s_%s_%s_%s"%(row.CI_CC_Id,row.CR_Date_From,row.CR_Date_To,row.CIT_Status,row.Cur_Code,row.CC_Description)
        print("option split=",option.split("_"))
        value ="%s from %s to %s status=%s currency=%s"%(row.CC_Description,row.CR_Date_From,row.CR_Date_To,dstatuses[row.CIT_Status],dcurrencies[row.Cur_Code])
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
        
        CC_Code=db.session.query(cost_center.CC_Code).filter(cost_center.CC_Id==data[0]).one()
        
        if     form.submit_PDF.data:
            return redirect(url_for('.export_User_Resume',
                                #Cus_Id          = data[0],
                                #Cus_Name        = data[5],
                                CC_Id           = data[0],
                                CC_Code         = CC_Code,
                                CC_Description  = data[5],
                                CIT_Date_From   = data[1],
                                CIT_Date_To     = data[2],
                                CIT_Status      = data[3],
                                CIT_Status_Value= dstatuses[int(data[3])],
                                Cur_Code        = data[4],
                                Cur_Name        = dcurrencies[data[4]],
                                Format          = "pdf"
                                ))
        if     form.submit_XLS.data:
            return redirect(url_for('.export_User_Resume',
                                #Cus_Id          = data[0],
                                #Cus_Name        = data[5],
                                CC_Id           = data[0],
                                CC_Code         = CC_Code,
                                CC_Description  = data[5],
                                CIT_Date_From   = data[1],
                                CIT_Date_To     = data[2],
                                CIT_Status      = data[3],
                                CIT_Status_Value= dstatuses[int(data[3])],
                                Cur_Code        = data[4],
                                Cur_Name        = dcurrencies[data[4]],
                                Format          = "xlsx"
                                ))
        if     form.submit_CSV.data:
            return redirect(url_for('.export_User_Resume',
                                #Cus_Id          = data[0],
                                #Cus_Name        = data[5],
                                CC_Id           = data[0],
                                CC_Code         = CC_Code,
                                CC_Description  = data[5],
                                CIT_Date_From   = data[1],
                                CIT_Date_To     = data[2],
                                CIT_Status      = data[3],
                                CIT_Status_Value= dstatuses[int(data[3])],
                                Cur_Code        = data[4],
                                Cur_Name        = dcurrencies[data[4]],
                                Format          = "csv"
                                ))
        if     form.submit_JSON.data:
            return redirect(url_for('.export_User_Resume',
                                #Cus_Id          = data[0],
                                #Cus_Name        = data[5],
                                CC_Id           = data[0],
                                CC_Code         = CC_Code,
                                CC_Description  = data[5],
                                CIT_Date_From   = data[1],
                                CIT_Date_To     = data[2],
                                CIT_Status      = data[3],
                                CIT_Status_Value= dstatuses[int(data[3])],
                                Cur_Code        = data[4],
                                Cur_Name        = dcurrencies[data[4]],
                                Format          = "json"
                                ))
        if     form.submit_FIX.data:
            return redirect(url_for('.export_User_Resume',
                                #Cus_Id          = data[0],
                                #Cus_Name        = data[5],
                                CC_Id           = data[0],
                                CC_Code         = CC_Code,
                                CC_Description  = data[5],
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


    return render_template('export_user_resume.html',form=form)

# =============================================================================
from pandas.io.json             import json_normalize
import simplejson as json
import pandas
from reportlab.lib.pagesizes    import letter
from reportlab.pdfgen           import canvas
from reportlab.lib.utils        import ImageReader

def export_user_resume_to_pdf(output_file,rows,Customer,From,To,Status,Currency):

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


def export_user_resume_to_xls(output_file,rows,Customer,From,To,Status,Currency):
    json_file="%s.json"%(output_file)
    export_user_resume_to_json(json_file,rows,Customer,From,To,Status,Currency)
    
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

def export_user_resume_to_csv(output_file,rows,Customer,From,To,Status,Currency):
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
    

def export_user_resume_to_json(output_file,rows,Customer,From,To,Status,Currency):
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

def export_user_resume_to_fix(output_file,rows,Customer,From,To,Status,Currency):
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

@main.route('/export/User_Resume', methods=['GET','POST'])
@login_required
def export_User_Resume():
    logger.debug('Enter: Export_User_Resume()')
    #Cus_Id          =  request.args.get('Cus_Id',None,type=int)
    #Cus_Name        =  request.args.get('Cus_Name',None,type=str)
    CC_Id           =  request.args.get('CC_Id',None,type=int)
    CC_Code         =  request.args.get('CC_Code',None,type=str)
    CC_Description  =  request.args.get('CC_Description',None,type=str)
    CIT_Date_From   =  request.args.get('CIT_Date_From',None,type=str)
    CIT_Date_To     =  request.args.get('CIT_Date_To',None,type=str)
    CIT_Status      =  request.args.get('CIT_Status',None,type=int)
    CIT_Status_Value=  request.args.get('CIT_Status_Value',None,type=str)
    Cur_Code        =  request.args.get('Cur_Code',None,type=str)
    Cur_Name        =  request.args.get('Cur_Name',None,type=str)
    Format          =  request.args.get('Format',None,type=str)
    # Get Actual Data from Database
    # NOTE: Here needs some Sand-Clock Message or something in case it takes so long ...
    query="CALL Get_User_Resume(%d,'%s','%s',%d,'%s','%d')"%(current_user.id,CIT_Date_From,CIT_Date_To,CIT_Status,Cur_Code,CC_Id)
    
    rows =  db.engine.execute(query).fetchall()

    # Aqui hace la conversion 
    output_file = "CR_%s_%s_%s_%s_%s.%s"%(CC_Code,CIT_Date_From,CIT_Date_To,CIT_Status,Cur_Code,Format)
    if      Format == 'pdf':
        return_file=export_user_resume_to_pdf(output_file,rows,CC_Description,CIT_Date_From,CIT_Date_To,CIT_Status_Value,Cur_Name)
    elif    Format == 'xlsx':
        return_file=export_user_resume_to_xls(output_file,rows,CC_Description,CIT_Date_From,CIT_Date_To,CIT_Status_Value,Cur_Name)
    elif    Format == 'csv':
        return_file=export_user_resume_to_csv(output_file,rows,CC_Description,CIT_Date_From,CIT_Date_To,CIT_Status_Value,Cur_Name)
    elif    Format == 'json':
        return_file=export_user_resume_to_json(output_file,rows,CC_Description,CIT_Date_From,CIT_Date_To,CIT_Status_Value,Cur_Name)
    elif    Format == 'fix':
        return_file=export_user_resume_to_fix(output_file,rows,CC_Description,CIT_Date_From,CIT_Date_To,CIT_Status_Value,Cur_Name)
    else:
        pass    
    
    # Aqui debe enviar el archivo a la PC
    print("%s: return_file   = %s"%('export_User_Resume',return_file))
    print("%s: att name      = %s"%('export_User_Resume',output_file))
    return send_file(return_file,as_attachment=True,attachment_filename=output_file)

# =============================================================================
# View for Graphic os Use per Type
# (c) Sertechno 2019
# GLVH @ 2019-08-16
# =============================================================================

from emtec.collector.forms       import frm_graph_use_per_type_filter
from babel.numbers  import format_number, format_decimal, format_percent
from emtec.collector.common.stats_functions    import RunningStats

@main.route('/forms/Get_Graph_Stats_Per_Type_Filter', methods=['GET', 'POST'])
@login_required
@admin_required
def forms_Get_Graph_Stats_Per_Type_Filter():
    logger.debug('Enter: forms_Get_Graph_Stats_Per_Type_Filter()'%())

    form = frm_graph_use_per_type_filter()
    
    form.Graph.choices      = [ (1,"Lineal"), (2,"Bars"), (3,"Min Max") ]
    form.Type.choices       = db.session.query(cu_type.Typ_Code,cu_type.Typ_Description).order_by(cu_type.Typ_Description).all()
    form.Field.choices      = [ (1,"Count"), (2,"Mean"), (3,"Use") ]

    form.Customer.choices   = db.session.query(customer.Cus_Id,customer.Cus_Name).order_by(customer.Cus_Name).all()
    form.Platform.choices   = db.session.query(platform.Pla_Id,platform.Pla_Name).order_by(platform.Pla_Name).all()
    form.CC.choices         = db.session.query(cost_center.CC_Id,cost_center.CC_Description).order_by(cost_center.CC_Description).all()
    form.CI.choices         = db.session.query(configuration_item.CI_Id,configuration_item.CI_Name).order_by(configuration_item.CI_Name).all()

    form.Estimation.choices = [ (0,"None"),
                                (1,"Lineal"),
                                (2,"Season"),
                                (3,"Lineal Adjusted by Season"),
                                (4,"Lineal Adjusted by Season w/RLs")
                              ]
   
       
    if form.validate_on_submit():
        if     form.submit_Report.data:
            #print("CU Type=",form.Type.data,"len",len(form.Type.data))
            session['data'] = { 'graph':form.Graph.data,
                        'year':form.Year.data,
                        'from':form.From.data,
                        'to':form.To.data,
                        'type':form.Type.data,
                        'field':form.Field.data,
                        'customer':form.Customer.data,
                        'platform':form.Platform.data,
                        'cc':form.CC.data,
                        'ci':form.CI.data,
                        'estimation':form.Estimation.data }
            return redirect(url_for('.report_Graph_Use_Per_Type_Filter'
                                ))

        elif   form.submit_Cancel.data:
            flash('Report discarded ...')
        else:
            flash('form validated but not submited. Report to Support ...')
        return redirect(url_for('.forms_Get_User_Resume'))


    return render_template('graph_use_per_type_filter.html',form=form)

# =============================================================================

import simplejson as json
import matplotlib.pyplot as plt
import numpy as np
import calendar
import tempfile
from   emtec.collector.common.stats_functions import Regression_Line

@main.route('/report/Graph_Use_Per_Type_Filter', methods=['GET','POST'])
@login_required
@admin_required
def report_Graph_Use_Per_Type_Filter():
    logger.debug('Enter: report_Stats_Use_Per_Type_Filter()')
    
    tmp_name="tmp_name"
    tmp_path="tmp_path"
    actual=[]
    estimate=[]
    months=0

    query = db.session.query(st_use_per_type).filter(\
                st_use_per_type.Year    ==session['data']['year'],
                st_use_per_type.Month   >=session['data']['from'],
                st_use_per_type.Month   <=session['data']['to'],
                st_use_per_type.Typ_Code==session['data']['type'],
                st_use_per_type.Cus_Id  ==session['data']['customer'],
                st_use_per_type.Pla_Id  ==session['data']['platform'],
                st_use_per_type.CC_Id   ==session['data']['cc'],
                st_use_per_type.CI_Id   ==session['data']['ci']                
                )\
                .order_by(st_use_per_type.Year,st_use_per_type.Month)

    try:
        rows=query.all()
    except Exception as e:
        flash(e)
        rows=None
         
    # Initialize data vectors
    actual=[]
    estimate=[]
    for i in range(12):
        actual.append(0)
        
    # Load Actual Data vector with selected field
    session['data']['afield']='Count'
    session['data']['rs']=RunningStats()   # This will be use to captyre running statistics 
    for row in rows:
        if session['data']['field'] == 1:
            actual[row.Month-1] = row.Count
            session['data']['afield']='Count' 
        elif session['data']['field'] == 2:
            actual[row.Month-1] = float(row.Mean)
            session['data']['afield']='Mean' 
        elif session['data']['field'] == 3:
            actual[row.Month-1] = float(row.Count*row.Mean) 
            session['data']['afield']='Use' 
        else:
            actual[row.Month-1]=row.Count
            session['data']['afield']='Count' 
        session['data']['rs'].push(actual[row.Month-1])
    
    # Appropiate try/except blocks should be include here, any error should be reported and defaults considered
            
    session['data']['cutype']  = db.session.query(cu_type.Typ_Description).filter(cu_type.Typ_Code==session['data']['type']).scalar()
    session['data']['cusname'] = db.session.query(customer.Cus_Name).filter(customer.Cus_Id==session['data']['customer']).scalar()
    session['data']['planame'] = db.session.query(platform.Pla_Name).filter(platform.Pla_Id==session['data']['platform']).scalar()
    session['data']['ccname']  = db.session.query(cost_center.CC_Description).filter(cost_center.CC_Id==session['data']['cc']).scalar()
    session['data']['ciname']  = db.session.query(configuration_item.CI_Name).filter(configuration_item.CI_Id==session['data']['ci']).scalar()
 
    # MU defaults to Unit, should be repleced with variable MU depending on DB
    # MU will be allways UNT for field Count
    # MU will depend on DB for fields Mean & Use
    session['data']['mu']='UNT'
    # special cases follows
    if (session['data']['type'] in ('DSK','RAM')) and (session['data']['afield'] in ('Mean','Use')):
            session['data']['mu']='GB'
    
    # Prepare some presentation parameters
    dias = [np.array(calendar.mdays)[0:i].sum() + 1 for i in np.arange(12)+1]  # Para generar el lugar del primer días de cada mes en un año
    months = calendar.month_abbr[1:13]  # Creamos una lista con los nombres abreviados de los meses
    months12=months
    months24=months+months
    """
    for i in range(0,len(months12)):
        months12[i]=months12[i][0:3]
    for i in range(0,len(months24)):
        months24[i]=months24[i][0:3]
    """    
       
    # Ge Data here from parameters
    
    # Force Demo Data

    suptitle = "%s of %s (%s/%s-%s/%s)"%(session['data']['afield'],session['data']['cutype'],
                                months12[session['data']['from']-1],
                                session['data']['year'],
                                months12[session['data']['to']-1],
                                session['data']['year'],
                                )

    title=''
    
    estimate=[]
    session['data']['coeficients_yx']=None
    session['data']['coeficients_yx2']=None
    # As Data is Know, diferent graphic and forecasts can be generated, defaults to Lineal Regression Proyection

    if session['data']['estimation']==1:
        RL          =   Regression_Line(actual)
        estimate    =   RL.estimate_y(12,23)    # Calculates regression line for next year (12 months period)
        session['data']['coeficients_yx']=RL.get_yx_coeficients()
        title='Lineal proyection for %s'%(session['data']['year']+1)
    elif session['data']['estimation']==2:
        var=[]
        sum_var=0
        var.append(0)
        for i in range(1,len(actual)):
            if actual[i-1] != 0:
                v=(actual[i]-actual[i-1])/actual[i-1]
            else:
                v=0
            var.append(v)
            sum_var+=v
        var_mean=sum_var/11
        var[0]=var_mean
        previous=actual[11]
        for i in range(0,len(actual)):
            estimate.append(previous*(1+var[i]))
            previous=estimate[i]
            
        title='Season proyection for %s'%(session['data']['year']+1)
    elif session['data']['estimation']==3:
        var=[]
        sum_var=0
        var.append(0)
        for i in range(1,len(actual)):
            if actual[i-1] != 0:
                v=(actual[i]-actual[i-1])/actual[i-1]
            else:
                v=0
            var.append(v)
            sum_var+=v
        var_mean=sum_var/11
        var[0]=var_mean
        
        RL          =   Regression_Line(actual)
        estimate    =   RL.estimate_y(12,23)    # Calculates regression line for next year (12 months period)
        session['data']['coeficients_yx']=RL.get_yx_coeficients()

        for i in range(0,len(actual)):
            estimate[i]=estimate[i]*(1+var[i])
            
        title='Lineal proyection adjusted by season for %s'%(session['data']['year']+1)
    elif session['data']['estimation']==4:
        var=[]
        sum_var=0
        var.append(0)
        for i in range(1,len(actual)):
            if actual[i-1] != 0:
                v=(actual[i]-actual[i-1])/actual[i-1]
            else:
                v=0
            var.append(v)
            sum_var+=v
        var_mean=sum_var/11
        var[0]=var_mean
        
        RL          =   Regression_Line(actual)
        estimate    =   RL.estimate_y(12,23)    # Calculates regression line for next year (12 months period)
        session['data']['coeficients_yx']=RL.get_yx_coeficients()

        for i in range(0,len(actual)):
            estimate[i]=estimate[i]*(1+var[i])
            
        title='Lineal proyection adjusted by season w/RLs for %s'%(session['data']['year']+1)
        Data=actual+estimate
        RLLine1=RL.estimate_y(0,23)
        RL2         =   Regression_Line(Data)
        RLLine2=RL2.estimate_y(0,23)
        session['data']['coeficients_yx2']=RL2.get_yx_coeficients()
        
         
    else:
        pass
        #estimate    =   RL.estimate_y(12,23)    # Calculates regression line for next year (12 months period)
        #title='MV durante 2018'
    
    #print("Data 2018",actual)
    #print("Data 2019",estimate)

    
    # Variation to use auto-deletable temporary file names
    
    fp = tempfile.mkstemp(   suffix='.png',
                            dir='%s%s'%(    current_app.root_path,
                                            url_for('static',filename='tmp')
                                        )
                        )
                        
    tmp_path    =   fp[1]
    tmp_name    =   fp[1].split('/app/static/tmp/')[1]
        
    
    # Plot Data here to temporary file
    # Generate Graphic here    

    # Data is designed to report estimation for next year as a continuation of actual 2018's data
    Data=actual+estimate
    for i in range(0,len(actual)-1):
        Data[i]=None

    # Creates Figura: https://matplotlib.org/api/_as_gen/matplotlib.pyplot.figure.html
    fig = plt.figure(figsize=[12,9])
    
    # Get current size
    #fig_size = plt.rcParams["figure.figsize"]
    # Prints: [8.0, 6.0]
    #print ("Current size:", fig_size)
 
    # Set figure width to 12 and height to 9
    #fig_size=[12,9]
    #fig_size[0] = 12
    #fig_size[1] = 9
    #plt.rcParams["figure.figsize"] = fig_size

    # Get current size
    fig_size = plt.rcParams["figure.figsize"]
    # Prints: [8.0, 6.0]
    #print ("Current size:", fig_size)
    
    ax=fig.gca()
    ax.clear()
    
    if session['data']['graph']==1:
        ax.plot(actual,'b',label='Actual')
    elif session['data']['graph']==2:
        #index = np.arange(n_groups)
        index = np.arange(len(actual))
        bar_width = 0.70
        opacity = 0.4
        error_config = {'ecolor': '0.3'}
        #std_actual = (0,1,2,3,4,5,6,7,8,9,10,11)
        ax.bar( index,actual,bar_width,
                alpha=opacity, color='b',
                #yerr=std_actual, error_kw=error_config,
                label='Actual')

    else:
        ax.plot(actual,'b')
    
    
    if session['data']['estimation'] > 0: 
        ax.plot(Data,'r:',label="Estimation")
    
    if session['data']['estimation']==4:
        ax.plot(RLLine1,'b-',linewidth='0.5') 
        ax.plot(RLLine2,'r--',linewidth='0.5')
    
    # Customize the grid

    # Turn on the minor TICKS, which are required for the minor GRID
    ax.minorticks_on()

    # Customize the major grid
    ax.grid(which='major', linestyle='--', linewidth='0.5', color='gray')
    # Customize the minor grid
    ax.grid(which='minor', linestyle=':', linewidth='0.25', color='gray')    

    ax.legend()
    #fig.tight_layout()

    plt.suptitle(suptitle)
    plt.title(title)
    plt.xlabel('Period')
    plt.ylabel('%s of %s (%s)'%(session['data']['afield'],session['data']['cutype'],session['data']['mu']))
    
        
    if session['data']['estimation'] > 0: 
        xticks=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
        plt.xticks(xticks, months24, size = 'small', color = 'b', rotation = 45)  # Etiquetas, meses, en las posiciones, dias, con color azul y rotadas 45º
    else:
        xticks=[0,1,2,3,4,5,6,7,8,9,10,11]
        plt.xticks(xticks, months12, size = 'small', color = 'b', rotation = 45)  # Etiquetas, meses, en las posiciones, dias, con color azul y rotadas 45º

    #plt.show()
    
    plt.savefig(tmp_path)
    plt.close
    return render_template('show_graph_use_per_type_filter.html',
                        filename=tmp_name,
                        actual=actual,
                        estimate=estimate,
                        #Year=Year,
                        months=months,
                        Data=session['data']
                )

# =============================================================================
# View for Graphic os Use per Type
# (c) Sertechno 2019
# GLVH @ 2019-08-16
# =============================================================================

from emtec.collector.forms       import frm_graph_use_per_type
from babel.numbers  import format_number, format_decimal, format_percent

@main.route('/forms/Get_Graph_Stats_Per_Type', methods=['GET', 'POST'])
@login_required
@admin_required
def forms_Get_Graph_Stats_Per_type():
    logger.debug('Enter: forms_Get_Graph_Stats_Per_Type()'%())

    form = frm_graph_use_per_type()
    
    form.Graph.choices   = [(1,"# de Máquinas Virtuales Anual y Proyección Lineal"),
                            (2,"# de Máquinas Virtuales Anual y Proyección estacional"),
                            (3,"# de Máquinas Virtuales Anual y Proyección lineal ajustada estacionalmente"),
                            (4,"# de Máquinas Virtuales Anual y Proyección lineal ajustada estacionalmente (c/LR)")
                           ]

    if form.validate_on_submit():
        if     form.submit_Report.data:

            return redirect(url_for('.report_Graph_Use_Per_Type',
                                Year            = form.Year.data,
                                Graph           = form.Graph.data
                                ))

        elif   form.submit_Cancel.data:
            #print('Cancel Data Here ... does nothing')
            flash('Report discarded ...')
        else:
            flash('form validated but not submited. Report to Support ...')
            #print('form validated but not submited ???')
        return redirect(url_for('.forms_Get_User_Resume'))


    return render_template('stats_use_per_type.html',form=form)

# =============================================================================

import simplejson as json
import matplotlib.pyplot as plt
import numpy as np
import calendar
from   emtec.collector.common.stats_functions import Regression_Line

@main.route('/report/Graph_Use_Per_Type', methods=['GET','POST'])
@login_required
@admin_required
def report_Graph_Use_Per_Type():
    logger.debug('Enter: report_Stats_Use_Per_Type()')
    
    Year            =  request.args.get('Year',None,type=int)
    Graph           =  request.args.get('Graph',None,type=int)
        
    # Ge Data here from parameters
    
    # Force Demo Data
    actual      =   [170,210,223,285,301,285,310,260,280,240,320,260]
    estimate=[]


    # As Data is Know, diferent graphic and forecasts can be generated, defaults to Lineal Regression Proyection
    if Graph==1:
        RL          =   Regression_Line(actual)
        estimate    =   RL.estimate_y(12,23)    # Calculates regression line for next year (12 months period)
        print("Coeficientes y/x =",RL.get_yx_coeficients())
        title='MV durante 2018 y proyección lineal para 2019'
    elif Graph==2:
        var=[]
        sum_var=0
        var.append(0)
        for i in range(1,len(actual)):
            v=(actual[i]-actual[i-1])/actual[i-1]
            var.append(v)
            sum_var+=v
        var_mean=sum_var/11
        var[0]=var_mean
        previous=actual[11]
        print("var=",var,"len(var)=",len(var))
        for i in range(0,len(actual)):
            estimate.append(previous*(1+var[i]))
            previous=estimate[i]
            
        title='MV durante 2018 y proyección estacional para 2019'
    elif Graph==3:
        var=[]
        sum_var=0
        var.append(0)
        for i in range(1,len(actual)):
            v=(actual[i]-actual[i-1])/actual[i-1]
            var.append(v)
            sum_var+=v
        var_mean=sum_var/11
        var[0]=var_mean
        
        RL          =   Regression_Line(actual)
        estimate    =   RL.estimate_y(12,23)    # Calculates regression line for next year (12 months period)

        for i in range(0,len(actual)):
            estimate[i]=estimate[i]*(1+var[i])
            
        title='MV durante 2018 y proyección lineal ajustada estacionalmente para 2019'
    elif Graph==4:
        var=[]
        sum_var=0
        var.append(0)
        for i in range(1,len(actual)):
            v=(actual[i]-actual[i-1])/actual[i-1]
            var.append(v)
            sum_var+=v
        var_mean=sum_var/11
        var[0]=var_mean
        
        RL          =   Regression_Line(actual)
        estimate    =   RL.estimate_y(12,23)    # Calculates regression line for next year (12 months period)

        for i in range(0,len(actual)):
            estimate[i]=estimate[i]*(1+var[i])
            
        title='MV durante 2018 y proyección lineal ajustada estacionalmente para 2019'
        Data=actual+estimate
        RLLine1=RL.estimate_y(0,23)
        RL2         =   Regression_Line(Data)
        RLLine2=RL2.estimate_y(0,23)
        
         
    else:
        RL          =   Regression_Line(actual)
        estimate    =   RL.estimate_y(12,23)    # Calculates regression line for next year (12 months period)
        title='MV durante 2018 y proyección lineal para 2019'
    
    print("Data 2018",actual)
    print("Data 2019",estimate)

    filename       =   "%s_stats_per_use_type_%s.png"%(current_user.id,id(actual))
    tmp_filename    =   "%s%s"%(current_app.root_path,url_for('static',filename='tmp/%s'%(filename)))
    
    print("filename=",filename)
    print("tmp_name=",tmp_filename)
    
    
    # Plot Data here to temporary file
    # Generate Graphic here    

    # Data is designed to report estimation for next year as a continuation of actual 2018's data
    Data=actual+estimate
    for i in range(0,len(actual)-1):
        Data[i]=None

    
    fig = plt.figure()
    ax=fig.gca()
    ax.clear()
    ax.plot(actual,'b') 
    ax.plot(Data,'r:')
    if Graph==4:
        ax.plot(RLLine1,'b-',linewidth='0.5') 
        ax.plot(RLLine2,'r--',linewidth='0.5')
    
    # Customize the grid

    # Turn on the minor TICKS, which are required for the minor GRID
    ax.minorticks_on()

    # Customize the major grid
    ax.grid(which='major', linestyle='--', linewidth='0.5', color='gray')
    # Customize the minor grid
    ax.grid(which='minor', linestyle=':', linewidth='0.25', color='gray')    

    plt.suptitle('Collector')
    plt.title(title)
    plt.xlabel('Periodo')
    plt.ylabel('# de Máquinas Virtuales')

    dias = [np.array(calendar.mdays)[0:i].sum() + 1 for i in np.arange(12)+1]  # Para generar el lugar del primer días de cada mes en un año
    months = calendar.month_name[1:13]  # Creamos una lista con los nombres de los meses
    months24=months+months
    for i in range(0,len(months24)):
        months24[i]=months24[i][0:3]
    xticks=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]

    plt.xticks(xticks, months24, size = 'small', color = 'b', rotation = 45)  # Colocamos las etiquetas, meses, en las posiciones, dias, con color azul y   rotadas 45º

    #plt.show()
    plt.savefig(tmp_filename)
    plt.close
    return render_template('show_graph_use_per_type.html',
                        filename=filename,
                        actual=actual,
                        estimate=estimate,
                        Year=Year,
                        months=months
                )

# =============================================================================
# View for Import Cost Centers
# (c) Sertechno 2019
# GLVH @ 2019-08-16
# =============================================================================

import os
from emtec.collector.forms       import frm_import_cost_centers
from werkzeug.utils import secure_filename
from flask_wtf.file import FileField

#UPLOAD_FOLDER = '/path/to/the/uploads'
UPLOAD_FOLDER = '/tmp'
#ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
ALLOWED_EXTENSIONS=set(['xls'])

#app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

#--------------------------------------------------------------------------
#from openpyxl import load_workbook
import os
import json
# Libreria para leer formato XLS
from xlrd import open_workbook
from time import strptime,strftime
# Import create_engine function
from sqlalchemy import create_engine
from sqlalchemy import text

def load_columns(sheet):
    columns={}
    for col in range(sheet.ncols):
        columns.update({sheet.cell(0,col).value:col})
    return columns
    
def load_Cost_Centers_from_XLS(file):
    updates=0
    additions=0
    errors=0

    DATA={}
    DATA.update({'metadata':{},'entities':[]})
    
    name = file.split('.')
    
    wb = open_workbook(file)
    nsheets=0

    DATA['metadata'] = {'name':name}
    for s in wb.sheets():
        COLUMNS={}
        COLUMNS=load_columns(s)

        if 'Cost_Centers' in s.name:
            for row in range(1,s.nrows):
                DATA['entities'].append({ 
                            'CC_Id':            int(s.cell(row,COLUMNS['CC_Id']).value),
                            'CC_Code':          s.cell(row,COLUMNS['CC_Code']).value,
                            'CC_Description':   s.cell(row,COLUMNS['CC_Description']).value,
                            'Cur_Code':         s.cell(row,COLUMNS['Cur_Code']).value,
                            'CC_Parent_Code':   s.cell(row,COLUMNS['CC_Parent_Code']).value,
                            })
    #print("CCs = %d"%len(DATA['entities']))
    
    DATA['metadata'].update({'count':len(DATA['entities'])})

    for cc in DATA['entities']:    
        #print("Importing CC: %s %s"%(cc['CC_Code'],cc['CC_Description']))
        try:
            id = db.session.query(cost_center.CC_Id).filter(cost_center.CC_Code==cc['CC_Code']).scalar()
            if id:
                #print("Existent CC",id,"will be updated");
                c=cost_center(id,cc['CC_Code'],cc['CC_Description'],cc['Cur_Code'],cc['CC_Parent_Code'])
                try:
                    db.session.merge(c)
                    db.session.commit()
                    updates+=1
                except Exception as e:
                    errors+=1              
                    flash("fail updatinging CC:",e)
                #print("c=",c)                
            else:
                #print("Add new CC")
                c=cost_center(0,cc['CC_Code'],cc['CC_Description'],cc['Cur_Code'],cc['CC_Parent_Code'])
                
                #print("c=",c)                
                try:
                    db.session.add(c)
                    db.session.commit()
                    additions+=1
                except Exception as e:                
                    errors+=1              
                    flash("fail updating CC:",e)
        except Exception as e:
            errors+=1              
            flash("fail queryng for CC:",e)
        
    return (len(DATA['entities']),additions,updates,errors)

#--------------------------------------------------------------------------
@main.route('/forms/Import_Cost_Centers', methods=['GET', 'POST'])
@login_required
def forms_Import_Cost_Centers():
    logger.debug('Enter: forms_Import_Cost_Centers()'%())

    session['data'] =  { }

    form = frm_import_cost_centers()
    
    if form.validate_on_submit():
        #print("************")
        #print("form.Import.data",form.Import.data);
        #flash("form.Import.data=%s"%form.Import.data);
        #print("************")
        f=form.Import.data
        filename=secure_filename(f.filename)
        f.save(os.path.join(
            UPLOAD_FOLDER,  filename
        ))        
        #return redirect(url_for('index'))
        
        result=load_Cost_Centers_from_XLS("%s/%s"%(UPLOAD_FOLDER,filename))
        return render_template('import_cost_centers_execution.html',filename=filename,result=result)
        """
        if     form.submit_Import.data:
            print("************")
            print("form.submit_Import.data",form.submit_import.data);
            flash("form.submit_Import.data="%form.submit_import.data);
            print("************")
            return redirect(url_for('.import_Cost_Centers'))
        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Report discarded ...')
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.index'))
        """
    return render_template('import_cost_centers.html',form=form)
    
    
"""    
@main.route('/import/Cost_Centers', methods=['GET','POST'])
@login_required
def import_Cost_Centers():
    #return send_file(return_file,as_attachment=True,attachment_filename=output_file)
    return '<H1>export_User_Resume</H1>'
"""    
"""    
@main.route('/import/Cost_Centers', methods=['GET','POST'])
#def upload_file():
def import_Cost_Centers():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            
            #file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return
" ""
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''    
"""    
"""
from flask import send_from_directory

#@app.route('/uploads/<filename>')
@main.route('/uploads/<filename>')
def uploaded_file(filename):
    #return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
    return send_from_directory(UPLOAD_FOLDER, filename)
"""    
# =============================================================================
# View for Get Charging Resume from DB
# (c) Sertechno 2018
# GLVH @ 2018-08-16
# =============================================================================

from emtec.collector.forms       import frm_stats_use_per_type
from babel.numbers  import format_number, format_decimal, format_percent

@main.route('/forms/Get_Stats_Per_Type', methods=['GET', 'POST'])
@login_required
@admin_required
def forms_Get_Stats_Per_type():
    logger.debug('Enter: forms_Get_Stats_Per_Type()'%())

    form = frm_stats_use_per_type()

    if form.validate_on_submit():
        if     form.submit_Report.data:

            print("form=",form)
            print("form.Year=",form.Year)
            Year=form.Year
            print("Year=",Year)
            print("Year.data=",Year.data)

            return redirect(url_for('.report_Stats_Use_Per_Type',
                                Year            = form.Year.data
                                ))

        elif   form.submit_Cancel.data:
            #print('Cancel Data Here ... does nothing')
            flash('Report discarded ...')
        else:
            flash('form validated but not submited. Report to Support ...')
            #print('form validated but not submited ???')
        return redirect(url_for('.forms_Get_User_Resume'))


    return render_template('stats_use_per_type.html',form=form)

# =============================================================================

import simplejson as json

@main.route('/report/Stats_Use_Per_Type', methods=['GET','POST'])
@login_required
@admin_required
def report_Stats_Use_Per_Type():
    logger.debug('Enter: report_Stats_Use_Per_Type()')
    
    Year            =  request.args.get('Year',None,type=int)
    
    print("Year=",Year)
    
    rows= db.session.query(st_use_per_type)\
                    .filter(st_use_per_type.Year==Year)\
                    .order_by(st_use_per_type.Typ_Code)\
                    .all()
    
    return render_template('report_stats_use_per_type.html',
                        rows=rows,
                        Year=Year
                )

# =============================================================================
# View for Get Charging Resume from DB
# (c) Sertechno 2018
# GLVH @ 2018-11-26
# =============================================================================

from emtec.collector.forms       import frm_user_resume
from babel.numbers  import format_number, format_decimal, format_percent

@main.route('/forms/Get_User_Resume', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.CUSTOMER)
def forms_Get_User_Resume():
    logger.debug('Enter: forms_Get_User_Resume()'%())

    session['data'] =  { 'CIT_Date_From':None, 'CIT_Date_To':None, 'CIT_Status':1,'Cur_Code':'USD','CC_Id':current_user.CC_Id}

    form = frm_user_resume()

    # ------------------------------------------------------------------------------
    # Will setup filter to consider only Currencies with actual Exchange Rates in DB
    # Prepare query
    query = db.session.query(exchange_rate.Cur_Code.distinct().label('Cur_Code'))
    # Execute query and convert in list for further use in choices selection
    cur_choices = [row.Cur_Code for row in query.all()]
    # ------------------------------------------------------------------------------
    # Will setup filter to consider only User's visible Cost Centers
    # Prepare query
    if current_user.CC_Id == 1:
        query = db.session.execute("SELECT CC_Id FROM Cost_Centers WHERE CC_Parent_Code='DEFAULT-CC-CODE' AND CC_Id>1")
    else:
        query = db.session.execute("SELECT CC_Id FROM Cost_Centers WHERE usercancc(%s,CC_Id)"%current_user.id)
    # Execute query and convert in list for further use in choices selection
    cc_choices = [row.CC_Id for row in query]

    CC_Description     = db.session.query(cost_center.CC_Description).filter(cost_center.CC_Id==current_user.CC_Id).one()
    form.CIT_Status.choices = db.session.query(cit_status.CIT_Status,cit_status.Value).all()
    form.Cur_Code.choices   = db.session.query(currency.Cur_Code,currency.Cur_Name).filter(currency.Cur_Code.in_(cur_choices)).all()
    form.CC_Id.choices   = db.session.query(cost_center.CC_Id,cost_center.CC_Description).filter(cost_center.CC_Id.in_(cc_choices)).all()

    if form.validate_on_submit():
        session['data']['CIT_Date_From' ] = form.CIT_Date_From.data
        session['data']['CIT_Date_To'   ] = form.CIT_Date_To.data
        session['data']['CIT-Status'    ] = form.CIT_Status.data
        session['data']['Cur_Code'      ] = form.Cur_Code.data
        session['data']['CC_Id   '      ] = form.CC_Id.data
        if     form.submit_Report.data:
            # Get the Selected options index for string lists
            for i in range(len(form.Cur_Code.choices)):
                if form.Cur_Code.choices[i][0]==form.Cur_Code.data:
                    cur_index=i
            for i in range(len(form.CC_Id.choices)):
                if form.CC_Id.choices[i][0]==form.CC_Id.data:
                    cc_index=i
            return redirect(url_for('.report_User_Resume',
                                #CC_Description  = CC_Description,
                                CIT_Date_From   = form.CIT_Date_From.data,
                                CIT_Date_To     = form.CIT_Date_To.data,
                                CIT_Status      = form.CIT_Status.data,
                                CIT_Status_Value= form.CIT_Status.choices[form.CIT_Status.data-1][1],
                                Cur_Code        = form.Cur_Code.data,
                                Cur_Name        = form.Cur_Code.choices[cur_index][1],
                                CC_Id           = form.CC_Id.data,
                                CC_Description  = form.CC_Id.choices[cc_index][1],
                                Update          = 0
                                ))
        if     form.submit_Update.data:
            # Get the Selected options index for string lists
            for i in range(len(form.Cur_Code.choices)):
                if form.Cur_Code.choices[i][0]==form.Cur_Code.data:
                    cur_index=i
            for i in range(len(form.CC_Id.choices)):
                if form.CC_Id.choices[i][0]==form.CC_Id.data:
                    cc_index=i
            return redirect(url_for('.report_User_Resume',
                                #CC_Description  = CC_Description,
                                CIT_Date_From   = form.CIT_Date_From.data,
                                CIT_Date_To     = form.CIT_Date_To.data,
                                CIT_Status      = form.CIT_Status.data,
                                CIT_Status_Value= form.CIT_Status.choices[form.CIT_Status.data-1][1],
                                Cur_Code        = form.Cur_Code.data,
                                Cur_Name        = form.Cur_Code.choices[cur_index][1],
                                CC_Id           = form.CC_Id.data,
                                CC_Description  = form.CC_Id.choices[cc_index][1],
                                Update          = 1
                                ))

        elif   form.submit_Cancel.data:
            #print('Cancel Data Here ... does nothing')
            flash('Report discarded ...')
        else:
            flash('form validated but not submited. Report to Support ...')
            #print('form validated but not submited ???')
        return redirect(url_for('.forms_Get_User_Resume'))

    form.CIT_Date_From.data = session['data']['CIT_Date_From']
    form.CIT_Date_To.data   = session['data']['CIT_Date_To']
    form.CIT_Status.data    = session['data']['CIT_Status']
    form.Cur_Code.data      = session['data']['Cur_Code']

    return render_template('get_user_resume.html',form=form, data=session.get('data'))

# =============================================================================

import simplejson as json

@main.route('/report/User_Resume', methods=['GET','POST'])
@login_required
@permission_required(Permission.CUSTOMER)
def report_User_Resume():
    logger.debug('Enter: report_User_Resume()')
    CC_Id           =  request.args.get('CC_Id',current_user.id,type=int)
    CC_Description  =  request.args.get('CC_Description',None,type=str)
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
        # 20181228 GV query = "SELECT DISTINCT CI_Id FROM Configuration_Items WHERE Cus_Id=%d"%(Cus_Id)
        if current_user.CC_Id == 1:        
            query = "SELECT CI_Id FROM Configuration_Items WHERE CC_Id IN (SELECT CC_Id FROM Cost_Centers WHERE ccisbelow(CC_Id,%d)) ORDER BY CC_Id,CI_Id"%(CC_Id)
            print("query=",query)
        else:
            query = "SELECT CI_Id FROM Configuration_Items WHERE CC_Id IN (SELECT CC_Id FROM Cost_Centers WHERE usercancc(%d,CC_Id) AND ccisbelow(CC_Id,%d)) ORDER BY CC_Id,CI_Id"%(current_user.id,CC_Id)
        
        logger.debug ("report_User_Resume: query: %s"%(query))

        CI = db.engine.execute(query)

        print ("report_User_Resume: %d CI's found for user %d"%(CI.rowcount,current_user.id))
        logger.debug ("report_User_Resume: %d CI's found for user %d"%(CI.rowcount,current_user.id))
        
        resume_records=0

        for ci in CI:
            query="CALL Update_User_Resume_CI('%s','%s',%s,'%s',%s)"%\
                    (CIT_Date_From,CIT_Date_To,CIT_Status,Cur_Code,ci.CI_Id)
            logger.debug ("report_User_Resume: query: %s"%query)
            records=db.engine.execute(query)
            resume_records += records.scalar()

        logger.debug ("report_User_Resume: resume_records = %s"%resume_records)
        
    # Get Actual Resume Data from Database
    # NOTE: Here needs some Sand-Clock Message or something in case it takes so long ...
    if current_user.CC_Id == 1:
        user_id=db.session.query(User.id).filter(User.CC_Id==CC_Id).one()      
        #query="CALL Get_User_Resume(%d,'%s','%s',%d,'%s',%d)"%(current_user.id,CIT_Date_From,CIT_Date_To,CIT_Status,Cur_Code,CC_Id)
        query="CALL Get_User_Resume(%d,'%s','%s',%d,'%s',%d)"%(user_id.id,CIT_Date_From,CIT_Date_To,CIT_Status,Cur_Code,CC_Id)
    else:
        query="CALL Get_User_Resume(%d,'%s','%s',%d,'%s',%d)"%(current_user.id,CIT_Date_From,CIT_Date_To,CIT_Status,Cur_Code,CC_Id)
    
    logger.debug ("report_User_Resume: query: %s"%query)
    print ("report_User_Resume: query: %s"%query)
    
    rows =  db.engine.execute(query).fetchall()
    
    return render_template('report_user_resume.html',rows=rows,
                #Cus_Id=Cus_Id,
                #Cus_Name=Cus_Name,
                CC_Description=CC_Description,
                CIT_Date_From=CIT_Date_From,
                CIT_Date_To=CIT_Date_To,
                CIT_Status=CIT_Status,
                CIT_Status_Value=CIT_Status_Value,                
                Cur_Code=Cur_Code,
                Cur_Name=Cur_Name
                )

