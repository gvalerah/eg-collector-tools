from time           import strftime
from datetime       import datetime                         
from sqlalchemy     import exc
from sqlalchemy     import func
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

from emtec                                 import *
from emtec.collector.db.flask_models       import User
from emtec.collector.db.flask_models       import Permission

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
# GLVH @ 2020-02-20 16:44:35
# =============================================================================

from emtec.collector.db.flask_models import cit_generation
from emtec.collector.forms import frm_cit_generation,frm_cit_generation_delete
from emtec.collector.db.flask_models import cit_status
from emtec.collector.forms import frm_cit_status,frm_cit_status_delete
from emtec.collector.db.flask_models import cu_operation
from emtec.collector.forms import frm_cu_operation,frm_cu_operation_delete
from emtec.collector.db.flask_models import cu_type
from emtec.collector.forms import frm_cu_type,frm_cu_type_delete
from emtec.collector.db.flask_models import charge_item
from emtec.collector.forms import frm_charge_item,frm_charge_item_delete
from emtec.collector.db.flask_models import charge_resume
from emtec.collector.forms import frm_charge_resume,frm_charge_resume_delete
from emtec.collector.db.flask_models import charge_unit_egm
from emtec.collector.forms import frm_charge_unit_egm,frm_charge_unit_egm_delete
from emtec.collector.db.flask_models import charge_unit
from emtec.collector.forms import frm_charge_unit,frm_charge_unit_delete
from emtec.collector.db.flask_models import configuration_item
from emtec.collector.forms import frm_configuration_item,frm_configuration_item_delete
from emtec.collector.db.flask_models import cost_center
from emtec.collector.forms import frm_cost_center,frm_cost_center_delete
from emtec.collector.db.flask_models import country
from emtec.collector.forms import frm_country,frm_country_delete
from emtec.collector.db.flask_models import country_currency
from emtec.collector.forms import frm_country_currency,frm_country_currency_delete
from emtec.collector.db.flask_models import currency
from emtec.collector.forms import frm_currency,frm_currency_delete
from emtec.collector.db.flask_models import customer
from emtec.collector.forms import frm_customer,frm_customer_delete
from emtec.collector.db.flask_models import exchange_rate
from emtec.collector.forms import frm_exchange_rate,frm_exchange_rate_delete
from emtec.collector.db.flask_models import interface
from emtec.collector.forms import frm_interface,frm_interface_delete
from emtec.collector.db.flask_models import measure_unit
from emtec.collector.forms import frm_measure_unit,frm_measure_unit_delete
from emtec.collector.db.flask_models import platform
from emtec.collector.forms import frm_platform,frm_platform_delete
from emtec.collector.db.flask_models import rat_period
from emtec.collector.forms import frm_rat_period,frm_rat_period_delete
from emtec.collector.db.flask_models import rate
from emtec.collector.forms import frm_rate,frm_rate_delete
from emtec.collector.db.flask_models import Role
from emtec.collector.forms import frm_Role,frm_Role_delete
from emtec.collector.db.flask_models import st_use_per_cu
from emtec.collector.forms import frm_st_use_per_cu,frm_st_use_per_cu_delete
from emtec.collector.db.flask_models import st_use_per_type
from emtec.collector.forms import frm_st_use_per_type,frm_st_use_per_type_delete
from emtec.collector.db.flask_models import trace
from emtec.collector.forms import frm_trace,frm_trace_delete
from emtec.collector.db.flask_models import user_resumes
from emtec.collector.forms import frm_user_resumes,frm_user_resumes_delete
from emtec.collector.db.flask_models import User
from emtec.collector.forms import frm_User,frm_User_delete

# NOTE: HARDCODE. TO REMOVE --------------------------------------------
def chk_c000001(*args,**kwargs):
    pass
    
from emtec.common.interface import *
from emtec.collector.db.orm_model          import Interface
from emtec.collector.db.flask_models       import interface
#-----------------------------------------------------------------------
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2020-02-20 16:44:35
# =============================================================================

# ======================================================================
#  Auto-Generated code. Do not modify 
#  (C) Sertechno/Emtec Group (2018,2019)
#  GLVH @ 2020-02-20 16:44:39.183397
# ======================================================================
        
# gen_views_form.html:AG 2020-02-20 16:44:39.183421
@main.route('/forms/Charge_Items', methods=['GET', 'POST'])
@login_required

def forms_Charge_Items():
    """ Form handling function for table Charge_Items """
    logger.debug('forms_Charge_Items(): Enter')
    CU_Id  =  request.args.get('CU_Id',0,type=int)
    CIT_DateTime  =  request.args.get('CIT_DateTime',0,type=int)
    parent_key   = request.args.get('parent_key',None,type=str)
    parent_value = request.args.get('parent_value',0,type=int)
    row =  charge_item.query.filter(charge_item.CU_Id == CU_Id,charge_item.CIT_DateTime == CIT_DateTime).first()
    if row is None:
        row=charge_item()
        session['is_new_row']=True
    session['data'] =  {  'CU_Id':row.CU_Id, 'CIT_Date':row.CIT_Date, 'CIT_Time':str(row.CIT_Time), 'CIT_Quantity':row.CIT_Quantity, 'CIT_Status':row.CIT_Status, 'CIT_Is_Active':row.CIT_Is_Active, 'CIT_DateTime':row.CIT_DateTime }
    
    if parent_key is not None:
       session['data'][parent_key] = parent_value
       print('parent_key  = ',parent_key)
       print('parent_value= ',parent_value)    
       print('session["data"][parent_key] = %s'%(parent_key,session['data'][parent_key]))
    
    form = frm_charge_item()
    
    if form.has_FKs:
        form.CU_Id.choices = db.session.query(charge_unit.CU_Id,charge_unit.CU_Description).order_by(charge_unit.CU_Description).all()
        form.CIT_Status.choices = db.session.query(cit_status.CIT_Status,cit_status.Value).order_by(cit_status.Value).all()

    
    # Actual Form activation here
    if form.validate_on_submit():
    # Code for SAVE option
        if form.submit_Save.data and current_user.role_id > 1:
    
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
                   message=Markup('<b>Charge Item CU_Id,CIT_DateTime saved OK</b>')
                   flash(message)
               db.session.close()
            except Exception as e:
               db.session.rollback()
               db.session.close()
               message=Markup('ERROR saving Charge Item record : %s'%(e))
               flash(message)
            return redirect(url_for('.select_Charge_Items_query'))    
    # Code for NEW option
    # GV 20190109 f.write(        "        elif   form.submit_New.data:\n")
        elif   form.submit_New.data and current_user.role_id>1:
            #print('New Data Here ...')
            session['is_new_row']=True
            db.session.close()
            row=charge_item()
    
            return redirect(url_for('.forms_Charge_Items'))    
    
    # Code for CANCEL option 
        elif   form.submit_Cancel.data:
            #print('Cancel Data Here ... does nothing')
            message=Markup('Charge Item Record modifications discarded ...')
            flash(message)
    # Code for ANY OTHER option should never get here
        else:
            #print('form validated but not submited ???')
            message=Markup("<b>Charge Item data modifications not allowed for user '%s'. Please contact EG Suite's Administrator ...</b>"%(current_user.username))    
            flash(message)
    
            return redirect(url_for('.forms_'))    
    
    
    form.CU_Id.data = row.CU_Id
    form.CIT_Date.data = row.CIT_Date
    form.CIT_Time.data = row.CIT_Time
    form.CIT_Quantity.data = row.CIT_Quantity
    form.CIT_Status.data = row.CIT_Status
    form.CIT_Is_Active.data = row.CIT_Is_Active
    session['prev_row'] = str(row)
    session['is_new_row'] = False
    logger.debug('forms_Charge_Items(): Exit')
    # Generates pagination data here
    P=[]
    # Tab Relations = []
    
    # Generation of pagination data completed       
    return render_template('charge_items.html', form=form, row=row, P=P)    
# ======================================================================



# ======================================================================
#  Auto-Generated code. Do not modify 
#  (C) Sertechno/Emtec Group (2018,2019)
#  GLVH @ 2020-02-20 16:44:39.206306
# ======================================================================
        
# gen_views_delete.html:AG 2020-02-20 16:44:39.206329
@main.route('/forms/Charge_Items_delete', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@admin_required
def forms_Charge_Items_delete():
    """ Delete record handling function for table Charge_Items """
    logger.debug('forms_Charge_Items_delete(): Enter')
    CU_Id  =  request.args.get('CU_Id',0,type=int)
    CIT_DateTime  =  request.args.get('CIT_DateTime',0,type=int)
    row =  charge_item.query.filter(charge_item.CU_Id == CU_Id,charge_item.CIT_DateTime == CIT_DateTime).first()

    if row is None:
        row=charge_item()
    session['data'] =  {  'CU_Id':row.CU_Id, 'CIT_Date':row.CIT_Date, 'CIT_Time':str(row.CIT_Time), 'CIT_Quantity':row.CIT_Quantity, 'CIT_Status':row.CIT_Status, 'CIT_Is_Active':row.CIT_Is_Active, 'CIT_DateTime':row.CIT_DateTime }
                       
    form = frm_charge_item_delete()

    # Tab['has_fks'] True
    
    pass # Tab['has_fks'] True
    
            
    # Actual Form activation here
    if form.validate_on_submit():
    
    # Code for SAVE option
        if  form.submit_Delete.data:
            print('Delete Data Here...')

    
    #f.write(        "            print('Delete Data Here...')
            try:
                session['deleted_row']=str(row)
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                logger.audit ( '%s:DEL:%s' % (current_user.username,session['deleted_row']) )
                flash('Charge Item CU_Id,CIT_DateTime deleted OK')
            except exc.IntegrityError as e:
                db.session.rollback()    
                flash('INTEGRITY ERROR: Are you sure there are no dependant records in other tables?')
                return redirect(url_for('.forms_Charge_Items_delete',CU_Id=session['data']['CU_Id'],CIT_DateTime=session['data']['CIT_DateTime']))    
    
            return redirect(url_for('.select_Charge_Items_query'))    
    # Code for CANCEL option 
        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
            return redirect(url_for('.select_Charge_Items_query'))    
    # Code for ANY OTHER option should never get here
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.select_Charge_Items_query'))    
    
    logger.debug('forms_Charge_Items_delete(): Exit')
    return render_template('charge_items_delete.html', form=form, data=session.get('data'),row=row)
#===============================================================================

# ======================================================================
#  Auto-Generated code. Do not modify 
#  (C) Sertechno/Emtec Group (2018,2019)
#  GLVH @ 2020-02-20 16:44:39.253322
# ======================================================================


from pprint import pprint, pformat

# gen_views_select_query.html:AG 2020-02-20 16:44:39.253345        
@main.route('/select/Charge_Items_Query', methods=['GET','POST'])
@login_required
@admin_required
def select_Charge_Items_query():
    """ Select rows handling function for table 'Charge_Items' """
    logger.debug('select_Charge_Items_query(): Enter')
    chk_c000001(filename=os.path.join(current_app.root_path, '.c000001'),request=request,db=db,logger=logger)
    # Get parameters from URL call
    ia       =  request.args.get('ia',     None,type=str)
    if ia is not None:
        ia=ia.split(',')
        if ia[0]=='ORDER':
            set_query_option(engine=db.engine,Interface=Interface,User_Id=current_user.id,Table_name='charge_item',Option_Type=OPTION_ORDER_BY,Argument_1=ia[1],Argument_2=ia[2])
        elif ia[0]=='GROUP':
            set_query_option(engine=db.engine,Interface=Interface,User_Id=current_user.id,Table_name='charge_item',Option_Type=OPTION_GROUP_BY,Argument_1=ia[1])
        elif ia[0]=='LIMIT':
            set_query_option(engine=db.engine,Interface=Interface,User_Id=current_user.id,Table_name='charge_item',Option_Type=OPTION_LIMIT,Argument_1=ia[1])

    iad      =  request.args.get('iad',     None,type=int)
    if iad is not None: delete_query_option(engine=db.engine,Interface=Interface,Id=iad) 
    
    field    =  request.args.get('field',   None,type=str)
    value    =  request.args.get('value',   None,type=str)
    
    # Populates a list of foreign keys used for advanced filtering
    # ------------------------------------------------------------------
    foreign_keys={}
    
    foreign_keys.update({'CU_Id':(charge_unit,'charge_unit','CU_Id','CU_Description','Charge Unit Id')})
    foreign_keys.update({'CIT_Status':(cit_status,'cit_status','CIT_Status','Value','Status')})
    # ------------------------------------------------------------------
    
    if field is not None:
        reset_query_options(    engine=db.engine,Interface=Interface,
                                User_Id=current_user.id,
                                Table_name='charge_item'
                                )

        
        if field in foreign_keys.keys():
            Class,referenced_classname,referenced_Field,referenced_Value,column_Header=foreign_keys[field]
            foreign_field='%s.%s:%s'%(referenced_classname,referenced_Value,column_Header)
            foreign_record=Class.query.get(value)
            foreign_description="'%s'"%getattr(foreign_record,referenced_Value)
        set_query_option(   engine=db.engine,Interface=Interface,
                        User_Id=current_user.id,
                        Table_name='charge_item',
                        Option_Type=OPTION_FILTER,
                        Argument_1=foreign_field,
                        Argument_2='==',
                        Argument_3=foreign_description
                        )
    page     =  request.args.get('page',    1   ,type=int)
    addx     =  request.args.get('add.x',   None,type=int)
    addy     =  request.args.get('add.y',   None,type=int)
    exportx  =  request.args.get('export.x',None,type=int)
    exporty  =  request.args.get('export.y',None,type=int)
    filterx  =  request.args.get('filter.x',None,type=int)
    filtery  =  request.args.get('filter.y',None,type=int)
    # Select excluyent view mode
    if   addx    is not None: mode = 'add'
    elif exportx is not None: mode = 'export'
    elif filterx is not None: mode = 'filter'
    else:                     mode = 'select'
    CU_Id =  request.args.get('CU_Id',None,type=str)
    CIT_Date =  request.args.get('CIT_Date',None,type=str)
    CIT_Time =  request.args.get('CIT_Time',None,type=str)
    CIT_Quantity =  request.args.get('CIT_Quantity',None,type=str)
    CIT_Status =  request.args.get('CIT_Status',None,type=str)
    CIT_Is_Active =  request.args.get('CIT_Is_Active',None,type=str)
    CIT_DateTime =  request.args.get('CIT_DateTime',None,type=str)
    
    
    # Build default query all fields from table
    
    if CU_Id is not None and len(CU_Id)>0:
            Class,referenced_classname,referenced_Field,referenced_Value,column_Header=foreign_keys['CU_Id']
            foreign_field='%s.%s:%s'%(referenced_classname,referenced_Value,column_Header)            
            set_query_option(   engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='charge_item',
                Option_Type=OPTION_FILTER,
                Argument_1=foreign_field,
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%CU_Id
                )
                                
    
    
    if CIT_Date is not None and len(CIT_Date)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='charge_item',
                Option_Type=OPTION_FILTER,
                Argument_1='CIT_Date:Date',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%CIT_Date
                )
    
    
    if CIT_Time is not None and len(CIT_Time)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='charge_item',
                Option_Type=OPTION_FILTER,
                Argument_1='CIT_Time:Time',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%CIT_Time
                )
    
    
    if CIT_Quantity is not None and len(CIT_Quantity)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='charge_item',
                Option_Type=OPTION_FILTER,
                Argument_1='CIT_Quantity:Quantity',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%CIT_Quantity
                )
    
    
    if CIT_Status is not None and len(CIT_Status)>0:
            Class,referenced_classname,referenced_Field,referenced_Value,column_Header=foreign_keys['CIT_Status']
            foreign_field='%s.%s:%s'%(referenced_classname,referenced_Value,column_Header)            
            set_query_option(   engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='charge_item',
                Option_Type=OPTION_FILTER,
                Argument_1=foreign_field,
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%CIT_Status
                )
                                
    
    
    if CIT_Is_Active is not None and len(CIT_Is_Active)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='charge_item',
                Option_Type=OPTION_FILTER,
                Argument_1='CIT_Is_Active:Is Active',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%CIT_Is_Active
                )
    
    
    if CIT_DateTime is not None and len(CIT_DateTime)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='charge_item',
                Option_Type=OPTION_FILTER,
                Argument_1='CIT_DateTime:CIT_DateTime',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%CIT_DateTime
                )
    
    
    
    statement_query,options=get_query_options(engine=db.engine,Interface=Interface,Table_name='charge_item',User_Id=current_user.id)
    query=eval(statement_query)
    filtered_query = query    
    if mode == 'filter':
        query=filtered_query
    elif mode == 'export':
        query=filtered_query
        fh,output_file = tempfile.mkstemp(suffix='', prefix='Charge_Items_', dir=None, text=False)
        dict = {'header':{},'detail':[]}
        count = 0
        rows = query.all()
        for row in rows:
            dict['detail'].append({})
            for column in ['CU_Id', 'CIT_Date', 'CIT_Time', 'CIT_Quantity', 'CIT_Status', 'CIT_Is_Active', 'CIT_DateTime']:
                dict['detail'][count].update( { column:str(row.__getattribute__(column))})
                
            count += 1
        dict['header'].update({'count':count})
        jsonarray      = json.dumps(dict)
        data           = json.loads(jsonarray)  
        dataframe      = json_normalize(data, 'detail').assign(**data['header'])
        fh,output_file = tempfile.mkstemp(suffix='', prefix='Charge_Items_', dir='/tmp', text=False)
        xlsx_file      = '%s/%s'%(current_app.root_path,url_for('static',filename='%s.xls'%(output_file)))
        dataframe.to_excel(xlsx_file,sheet_name='Charge_Items',columns=['CU_Id', 'CIT_Date', 'CIT_Time', 'CIT_Quantity', 'CIT_Status', 'CIT_Is_Active', 'CIT_DateTime'])
        return send_file(xlsx_file,as_attachment=True,attachment_filename=output_file.replace('/','_')+'.xls')
    elif mode == 'add':
        return redirect(url_for('.forms_Charge_Items'))
    elif mode == 'select':
        pass
        # if some filter is required
        if field is not None:
            if field == 'CU_Id':
                if value is not None:
                    query = query.filter_by(CU_Id=value)
            if field == 'CIT_Date':
                if value is not None:
                    query = query.filter_by(CIT_Date=value)
            if field == 'CIT_Time':
                if value is not None:
                    query = query.filter_by(CIT_Time=value)
            if field == 'CIT_Quantity':
                if value is not None:
                    query = query.filter_by(CIT_Quantity=value)
            if field == 'CIT_Status':
                if value is not None:
                    query = query.filter_by(CIT_Status=value)
            if field == 'CIT_Is_Active':
                if value is not None:
                    query = query.filter_by(CIT_Is_Active=value)
            if field == 'CIT_DateTime':
                if value is not None:
                    query = query.filter_by(CIT_DateTime=value)
            # JOIN other tables and generate foreign fields
    query = query.join(charge_unit,charge_item.CU_Id == charge_unit.CU_Id).add_columns(charge_unit.CU_Description).join(cit_status,charge_item.CIT_Status == cit_status.CIT_Status).add_columns(cit_status.Value)
    
    # Actual request from DB follows
    tracebox_log(query,logger,length=50)
    rows = query.paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
    # Setting pagination variables ...
    if field is not None:
       next_url = url_for('.select_Charge_Items_query', field=field, value=value, page=rows.next_num) if rows.has_next else None
       prev_url = url_for('.select_Charge_Items_query', field=field, value=value, page=rows.prev_num) if rows.has_prev else None
    else:
       next_url = url_for('.select_Charge_Items_query', page=rows.next_num) if rows.has_next else None
       prev_url = url_for('.select_Charge_Items_query', page=rows.prev_num) if rows.has_prev else None
    # Actual rendering ...
    if request.headers.get('Content-Type') is not None or request.args.get('JSON',None,type=str) is not None:
        if "JSON" in request.headers.get('Content-Type') or request.args.get('JSON',None,type=str) is not None:
            logger.debug('select_Charge_Items_query(): will render: JSON rows')
            logger.debug('select_Charge_Items_query(): Exit')
            return json.dumps(serialize_object(rows.__dict__))
    logger.debug('select_Charge_Items_query(): will render: charge_items_All.html')
    logger.debug('select_Charge_Items_query(): Exit')
    return render_template('charge_items_select_All.html',rows=rows,options=options)
#===============================================================================
   # NOTE: HARDCODE. TO REMOVE --------------------------------------------
def chk_c000001(*args,**kwargs):
    pass
    
from emtec.common.interface import *
from emtec.collector.db.orm_model          import Interface
from emtec.collector.db.flask_models       import interface
#-----------------------------------------------------------------------
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2020-02-20 16:44:35
# =============================================================================

# ======================================================================
#  Auto-Generated code. Do not modify 
#  (C) Sertechno/Emtec Group (2018,2019)
#  GLVH @ 2020-02-20 16:44:39.675137
# ======================================================================
        
# gen_views_form.html:AG 2020-02-20 16:44:39.675160
@main.route('/forms/Charge_Resumes', methods=['GET', 'POST'])
@login_required

def forms_Charge_Resumes():
    """ Form handling function for table Charge_Resumes """
    logger.debug('forms_Charge_Resumes(): Enter')
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
    session['data'] =  {  'Cus_Id':row.Cus_Id, 'CR_Date_From':row.CR_Date_From, 'CR_Date_To':row.CR_Date_To, 'CIT_Status':row.CIT_Status, 'Cur_Code':row.Cur_Code, 'CIT_Count':row.CIT_Count, 'CIT_Quantity':row.CIT_Quantity, 'CIT_Generation':row.CIT_Generation, 'CU_Id':row.CU_Id, 'CI_CC_Id':row.CI_CC_Id, 'CU_Operation':row.CU_Operation, 'Typ_Code':row.Typ_Code, 'CC_Cur_Code':row.CC_Cur_Code, 'CI_Id':row.CI_Id, 'Rat_Id':row.Rat_Id, 'Rat_Price':row.Rat_Price, 'Rat_MU_Code':row.Rat_MU_Code, 'Rat_Cur_Code':row.Rat_Cur_Code, 'Rat_Period':row.Rat_Period, 'Rat_Hourly':row.Rat_Hourly, 'Rat_Daily':row.Rat_Daily, 'Rat_Monthly':row.Rat_Monthly, 'CR_Quantity':row.CR_Quantity, 'CR_Quantity_at_Rate':row.CR_Quantity_at_Rate, 'CC_XR':row.CC_XR, 'CR_Cur_XR':row.CR_Cur_XR, 'CR_ST_at_Rate_Cur':row.CR_ST_at_Rate_Cur, 'CR_ST_at_CC_Cur':row.CR_ST_at_CC_Cur, 'CR_ST_at_Cur':row.CR_ST_at_Cur, 'Cus_Name':row.Cus_Name, 'CI_Name':row.CI_Name, 'CU_Description':row.CU_Description, 'CC_Description':row.CC_Description, 'Rat_Period_Description':row.Rat_Period_Description, 'CC_Code':row.CC_Code, 'Pla_Id':row.Pla_Id, 'Pla_Name':row.Pla_Name }
    
    form = frm_charge_resume()
    
    # Actual Form activation here
    if form.validate_on_submit():
    # Code for SAVE option
        if form.submit_Save.data and current_user.role_id > 1:
    
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
            row.CC_Code = form.CC_Code.data
            row.Pla_Id = form.Pla_Id.data
            row.Pla_Name = form.Pla_Name.data  
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
                   message=Markup('<b>Charge Resume Cus_Id,CR_Date_From,CR_Date_To,CIT_Status,Cur_Code,CU_Id saved OK</b>')
                   flash(message)
               db.session.close()
            except Exception as e:
               db.session.rollback()
               db.session.close()
               message=Markup('ERROR saving Charge Resume record : %s'%(e))
               flash(message)
            return redirect(url_for('.select_Charge_Resumes_query'))    
    # Code for NEW option
    # GV 20190109 f.write(        "        elif   form.submit_New.data:\n")
        elif   form.submit_New.data and current_user.role_id>1:
            #print('New Data Here ...')
            session['is_new_row']=True
            db.session.close()
            row=charge_resume()
    
            return redirect(url_for('.forms_Charge_Resumes'))    
    
    # Code for CANCEL option 
        elif   form.submit_Cancel.data:
            #print('Cancel Data Here ... does nothing')
            message=Markup('Charge Resume Record modifications discarded ...')
            flash(message)
    # Code for ANY OTHER option should never get here
        else:
            #print('form validated but not submited ???')
            message=Markup("<b>Charge Resume data modifications not allowed for user '%s'. Please contact EG Suite's Administrator ...</b>"%(current_user.username))    
            flash(message)
    
            return redirect(url_for('.forms_'))    
    
    
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
    form.CC_Code.data = row.CC_Code
    form.Pla_Id.data = row.Pla_Id
    form.Pla_Name.data = row.Pla_Name
    session['prev_row'] = str(row)
    session['is_new_row'] = False
    logger.debug('forms_Charge_Resumes(): Exit')
    # Generates pagination data here
    P=[]
    # Tab Relations = []
    
    # Generation of pagination data completed       
    return render_template('charge_resumes.html', form=form, row=row, P=P)    
# ======================================================================



# ======================================================================
#  Auto-Generated code. Do not modify 
#  (C) Sertechno/Emtec Group (2018,2019)
#  GLVH @ 2020-02-20 16:44:39.699725
# ======================================================================
        
# gen_views_delete.html:AG 2020-02-20 16:44:39.699756
@main.route('/forms/Charge_Resumes_delete', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)

def forms_Charge_Resumes_delete():
    """ Delete record handling function for table Charge_Resumes """
    logger.debug('forms_Charge_Resumes_delete(): Enter')
    Cus_Id  =  request.args.get('Cus_Id',0,type=int)
    CR_Date_From  =  request.args.get('CR_Date_From',0,type=int)
    CR_Date_To  =  request.args.get('CR_Date_To',0,type=int)
    CIT_Status  =  request.args.get('CIT_Status',0,type=int)
    Cur_Code  =  request.args.get('Cur_Code',0,type=int)
    CU_Id  =  request.args.get('CU_Id',0,type=int)
    row =  charge_resume.query.filter(charge_resume.Cus_Id == Cus_Id,charge_resume.CR_Date_From == CR_Date_From,charge_resume.CR_Date_To == CR_Date_To,charge_resume.CIT_Status == CIT_Status,charge_resume.Cur_Code == Cur_Code,charge_resume.CU_Id == CU_Id).first()

    if row is None:
        row=charge_resume()
    session['data'] =  {  'Cus_Id':row.Cus_Id, 'CR_Date_From':row.CR_Date_From, 'CR_Date_To':row.CR_Date_To, 'CIT_Status':row.CIT_Status, 'Cur_Code':row.Cur_Code, 'CIT_Count':row.CIT_Count, 'CIT_Quantity':row.CIT_Quantity, 'CIT_Generation':row.CIT_Generation, 'CU_Id':row.CU_Id, 'CI_CC_Id':row.CI_CC_Id, 'CU_Operation':row.CU_Operation, 'Typ_Code':row.Typ_Code, 'CC_Cur_Code':row.CC_Cur_Code, 'CI_Id':row.CI_Id, 'Rat_Id':row.Rat_Id, 'Rat_Price':row.Rat_Price, 'Rat_MU_Code':row.Rat_MU_Code, 'Rat_Cur_Code':row.Rat_Cur_Code, 'Rat_Period':row.Rat_Period, 'Rat_Hourly':row.Rat_Hourly, 'Rat_Daily':row.Rat_Daily, 'Rat_Monthly':row.Rat_Monthly, 'CR_Quantity':row.CR_Quantity, 'CR_Quantity_at_Rate':row.CR_Quantity_at_Rate, 'CC_XR':row.CC_XR, 'CR_Cur_XR':row.CR_Cur_XR, 'CR_ST_at_Rate_Cur':row.CR_ST_at_Rate_Cur, 'CR_ST_at_CC_Cur':row.CR_ST_at_CC_Cur, 'CR_ST_at_Cur':row.CR_ST_at_Cur, 'Cus_Name':row.Cus_Name, 'CI_Name':row.CI_Name, 'CU_Description':row.CU_Description, 'CC_Description':row.CC_Description, 'Rat_Period_Description':row.Rat_Period_Description, 'CC_Code':row.CC_Code, 'Pla_Id':row.Pla_Id, 'Pla_Name':row.Pla_Name }
                       
    form = frm_charge_resume_delete()

    # Tab['has_fks'] False
    
            
    # Actual Form activation here
    if form.validate_on_submit():
    
    # Code for SAVE option
        if  form.submit_Delete.data:
            print('Delete Data Here...')

    
    #f.write(        "            print('Delete Data Here...')
            try:
                session['deleted_row']=str(row)
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                logger.audit ( '%s:DEL:%s' % (current_user.username,session['deleted_row']) )
                flash('Charge Resume Cus_Id,CR_Date_From,CR_Date_To,CIT_Status,Cur_Code,CU_Id deleted OK')
            except exc.IntegrityError as e:
                db.session.rollback()    
                flash('INTEGRITY ERROR: Are you sure there are no dependant records in other tables?')
                return redirect(url_for('.forms_Charge_Resumes_delete',Cus_Id=session['data']['Cus_Id'],CR_Date_From=session['data']['CR_Date_From'],CR_Date_To=session['data']['CR_Date_To'],CIT_Status=session['data']['CIT_Status'],Cur_Code=session['data']['Cur_Code'],CU_Id=session['data']['CU_Id']))    
    
            return redirect(url_for('.select_Charge_Resumes_query'))    
    # Code for CANCEL option 
        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
            return redirect(url_for('.select_Charge_Resumes_query'))    
    # Code for ANY OTHER option should never get here
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.select_Charge_Resumes_query'))    
    
    logger.debug('forms_Charge_Resumes_delete(): Exit')
    return render_template('charge_resumes_delete.html', form=form, data=session.get('data'),row=row)
#===============================================================================

# ======================================================================
#  Auto-Generated code. Do not modify 
#  (C) Sertechno/Emtec Group (2018,2019)
#  GLVH @ 2020-02-20 16:44:39.760362
# ======================================================================


from pprint import pprint, pformat

# gen_views_select_query.html:AG 2020-02-20 16:44:39.760385        
@main.route('/select/Charge_Resumes_Query', methods=['GET','POST'])
@login_required

def select_Charge_Resumes_query():
    """ Select rows handling function for table 'Charge_Resumes' """
    logger.debug('select_Charge_Resumes_query(): Enter')
    chk_c000001(filename=os.path.join(current_app.root_path, '.c000001'),request=request,db=db,logger=logger)
    # Get parameters from URL call
    ia       =  request.args.get('ia',     None,type=str)
    if ia is not None:
        ia=ia.split(',')
        if ia[0]=='ORDER':
            set_query_option(engine=db.engine,Interface=Interface,User_Id=current_user.id,Table_name='charge_resume',Option_Type=OPTION_ORDER_BY,Argument_1=ia[1],Argument_2=ia[2])
        elif ia[0]=='GROUP':
            set_query_option(engine=db.engine,Interface=Interface,User_Id=current_user.id,Table_name='charge_resume',Option_Type=OPTION_GROUP_BY,Argument_1=ia[1])
        elif ia[0]=='LIMIT':
            set_query_option(engine=db.engine,Interface=Interface,User_Id=current_user.id,Table_name='charge_resume',Option_Type=OPTION_LIMIT,Argument_1=ia[1])

    iad      =  request.args.get('iad',     None,type=int)
    if iad is not None: delete_query_option(engine=db.engine,Interface=Interface,Id=iad) 
    
    field    =  request.args.get('field',   None,type=str)
    value    =  request.args.get('value',   None,type=str)
    
    # Populates a list of foreign keys used for advanced filtering
    # ------------------------------------------------------------------
    foreign_keys={}
    
    # ------------------------------------------------------------------
    
    if field is not None:
        reset_query_options(    engine=db.engine,Interface=Interface,
                                User_Id=current_user.id,
                                Table_name='charge_resume'
                                )

        
        if field in foreign_keys.keys():
            Class,referenced_classname,referenced_Field,referenced_Value,column_Header=foreign_keys[field]
            foreign_field='%s.%s:%s'%(referenced_classname,referenced_Value,column_Header)
            foreign_record=Class.query.get(value)
            foreign_description="'%s'"%getattr(foreign_record,referenced_Value)
        set_query_option(   engine=db.engine,Interface=Interface,
                        User_Id=current_user.id,
                        Table_name='charge_resume',
                        Option_Type=OPTION_FILTER,
                        Argument_1=foreign_field,
                        Argument_2='==',
                        Argument_3=foreign_description
                        )
    page     =  request.args.get('page',    1   ,type=int)
    addx     =  request.args.get('add.x',   None,type=int)
    addy     =  request.args.get('add.y',   None,type=int)
    exportx  =  request.args.get('export.x',None,type=int)
    exporty  =  request.args.get('export.y',None,type=int)
    filterx  =  request.args.get('filter.x',None,type=int)
    filtery  =  request.args.get('filter.y',None,type=int)
    # Select excluyent view mode
    if   addx    is not None: mode = 'add'
    elif exportx is not None: mode = 'export'
    elif filterx is not None: mode = 'filter'
    else:                     mode = 'select'
    Cus_Id =  request.args.get('Cus_Id',None,type=str)
    CR_Date_From =  request.args.get('CR_Date_From',None,type=str)
    CR_Date_To =  request.args.get('CR_Date_To',None,type=str)
    CIT_Status =  request.args.get('CIT_Status',None,type=str)
    Cur_Code =  request.args.get('Cur_Code',None,type=str)
    CIT_Count =  request.args.get('CIT_Count',None,type=str)
    CIT_Quantity =  request.args.get('CIT_Quantity',None,type=str)
    CIT_Generation =  request.args.get('CIT_Generation',None,type=str)
    CU_Id =  request.args.get('CU_Id',None,type=str)
    CI_CC_Id =  request.args.get('CI_CC_Id',None,type=str)
    CU_Operation =  request.args.get('CU_Operation',None,type=str)
    Typ_Code =  request.args.get('Typ_Code',None,type=str)
    CC_Cur_Code =  request.args.get('CC_Cur_Code',None,type=str)
    CI_Id =  request.args.get('CI_Id',None,type=str)
    Rat_Id =  request.args.get('Rat_Id',None,type=str)
    Rat_Price =  request.args.get('Rat_Price',None,type=str)
    Rat_MU_Code =  request.args.get('Rat_MU_Code',None,type=str)
    Rat_Cur_Code =  request.args.get('Rat_Cur_Code',None,type=str)
    Rat_Period =  request.args.get('Rat_Period',None,type=str)
    Rat_Hourly =  request.args.get('Rat_Hourly',None,type=str)
    Rat_Daily =  request.args.get('Rat_Daily',None,type=str)
    Rat_Monthly =  request.args.get('Rat_Monthly',None,type=str)
    CR_Quantity =  request.args.get('CR_Quantity',None,type=str)
    CR_Quantity_at_Rate =  request.args.get('CR_Quantity_at_Rate',None,type=str)
    CC_XR =  request.args.get('CC_XR',None,type=str)
    CR_Cur_XR =  request.args.get('CR_Cur_XR',None,type=str)
    CR_ST_at_Rate_Cur =  request.args.get('CR_ST_at_Rate_Cur',None,type=str)
    CR_ST_at_CC_Cur =  request.args.get('CR_ST_at_CC_Cur',None,type=str)
    CR_ST_at_Cur =  request.args.get('CR_ST_at_Cur',None,type=str)
    Cus_Name =  request.args.get('Cus_Name',None,type=str)
    CI_Name =  request.args.get('CI_Name',None,type=str)
    CU_Description =  request.args.get('CU_Description',None,type=str)
    CC_Description =  request.args.get('CC_Description',None,type=str)
    Rat_Period_Description =  request.args.get('Rat_Period_Description',None,type=str)
    CC_Code =  request.args.get('CC_Code',None,type=str)
    Pla_Id =  request.args.get('Pla_Id',None,type=str)
    Pla_Name =  request.args.get('Pla_Name',None,type=str)
    
    
    # Build default query all fields from table
    
    if Cus_Id is not None and len(Cus_Id)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='charge_resume',
                Option_Type=OPTION_FILTER,
                Argument_1='Cus_Id:Cus_Id',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Cus_Id
                )
    
    
    if CR_Date_From is not None and len(CR_Date_From)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='charge_resume',
                Option_Type=OPTION_FILTER,
                Argument_1='CR_Date_From:CR_Date_From',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%CR_Date_From
                )
    
    
    if CR_Date_To is not None and len(CR_Date_To)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='charge_resume',
                Option_Type=OPTION_FILTER,
                Argument_1='CR_Date_To:CR_Date_To',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%CR_Date_To
                )
    
    
    if CIT_Status is not None and len(CIT_Status)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='charge_resume',
                Option_Type=OPTION_FILTER,
                Argument_1='CIT_Status:CIT_Status',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%CIT_Status
                )
    
    
    if Cur_Code is not None and len(Cur_Code)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='charge_resume',
                Option_Type=OPTION_FILTER,
                Argument_1='Cur_Code:Cur_Code',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Cur_Code
                )
    
    
    if CIT_Count is not None and len(CIT_Count)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='charge_resume',
                Option_Type=OPTION_FILTER,
                Argument_1='CIT_Count:CIT_Count',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%CIT_Count
                )
    
    
    if CIT_Quantity is not None and len(CIT_Quantity)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='charge_resume',
                Option_Type=OPTION_FILTER,
                Argument_1='CIT_Quantity:CIT_Quantity',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%CIT_Quantity
                )
    
    
    if CIT_Generation is not None and len(CIT_Generation)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='charge_resume',
                Option_Type=OPTION_FILTER,
                Argument_1='CIT_Generation:CIT_Generation',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%CIT_Generation
                )
    
    
    if CU_Id is not None and len(CU_Id)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='charge_resume',
                Option_Type=OPTION_FILTER,
                Argument_1='CU_Id:CU_Id',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%CU_Id
                )
    
    
    if CI_CC_Id is not None and len(CI_CC_Id)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='charge_resume',
                Option_Type=OPTION_FILTER,
                Argument_1='CI_CC_Id:CI_CC_Id',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%CI_CC_Id
                )
    
    
    if CU_Operation is not None and len(CU_Operation)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='charge_resume',
                Option_Type=OPTION_FILTER,
                Argument_1='CU_Operation:CU_Operation',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%CU_Operation
                )
    
    
    if Typ_Code is not None and len(Typ_Code)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='charge_resume',
                Option_Type=OPTION_FILTER,
                Argument_1='Typ_Code:Typ_Code',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Typ_Code
                )
    
    
    if CC_Cur_Code is not None and len(CC_Cur_Code)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='charge_resume',
                Option_Type=OPTION_FILTER,
                Argument_1='CC_Cur_Code:CC_Cur_Code',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%CC_Cur_Code
                )
    
    
    if CI_Id is not None and len(CI_Id)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='charge_resume',
                Option_Type=OPTION_FILTER,
                Argument_1='CI_Id:CI_Id',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%CI_Id
                )
    
    
    if Rat_Id is not None and len(Rat_Id)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='charge_resume',
                Option_Type=OPTION_FILTER,
                Argument_1='Rat_Id:Rat_Id',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Rat_Id
                )
    
    
    if Rat_Price is not None and len(Rat_Price)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='charge_resume',
                Option_Type=OPTION_FILTER,
                Argument_1='Rat_Price:Rat_Price',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Rat_Price
                )
    
    
    if Rat_MU_Code is not None and len(Rat_MU_Code)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='charge_resume',
                Option_Type=OPTION_FILTER,
                Argument_1='Rat_MU_Code:Rat_MU_Code',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Rat_MU_Code
                )
    
    
    if Rat_Cur_Code is not None and len(Rat_Cur_Code)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='charge_resume',
                Option_Type=OPTION_FILTER,
                Argument_1='Rat_Cur_Code:Rat_Cur_Code',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Rat_Cur_Code
                )
    
    
    if Rat_Period is not None and len(Rat_Period)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='charge_resume',
                Option_Type=OPTION_FILTER,
                Argument_1='Rat_Period:Rat_Period',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Rat_Period
                )
    
    
    if Rat_Hourly is not None and len(Rat_Hourly)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='charge_resume',
                Option_Type=OPTION_FILTER,
                Argument_1='Rat_Hourly:Rat_Hourly',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Rat_Hourly
                )
    
    
    if Rat_Daily is not None and len(Rat_Daily)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='charge_resume',
                Option_Type=OPTION_FILTER,
                Argument_1='Rat_Daily:Rat_Daily',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Rat_Daily
                )
    
    
    if Rat_Monthly is not None and len(Rat_Monthly)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='charge_resume',
                Option_Type=OPTION_FILTER,
                Argument_1='Rat_Monthly:Rat_Monthly',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Rat_Monthly
                )
    
    
    if CR_Quantity is not None and len(CR_Quantity)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='charge_resume',
                Option_Type=OPTION_FILTER,
                Argument_1='CR_Quantity:CR_Quantity',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%CR_Quantity
                )
    
    
    if CR_Quantity_at_Rate is not None and len(CR_Quantity_at_Rate)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='charge_resume',
                Option_Type=OPTION_FILTER,
                Argument_1='CR_Quantity_at_Rate:CR_Quantity_at_Rate',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%CR_Quantity_at_Rate
                )
    
    
    if CC_XR is not None and len(CC_XR)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='charge_resume',
                Option_Type=OPTION_FILTER,
                Argument_1='CC_XR:CC_XR',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%CC_XR
                )
    
    
    if CR_Cur_XR is not None and len(CR_Cur_XR)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='charge_resume',
                Option_Type=OPTION_FILTER,
                Argument_1='CR_Cur_XR:CR_Cur_XR',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%CR_Cur_XR
                )
    
    
    if CR_ST_at_Rate_Cur is not None and len(CR_ST_at_Rate_Cur)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='charge_resume',
                Option_Type=OPTION_FILTER,
                Argument_1='CR_ST_at_Rate_Cur:CR_ST_at_Rate_Cur',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%CR_ST_at_Rate_Cur
                )
    
    
    if CR_ST_at_CC_Cur is not None and len(CR_ST_at_CC_Cur)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='charge_resume',
                Option_Type=OPTION_FILTER,
                Argument_1='CR_ST_at_CC_Cur:CR_ST_at_CC_Cur',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%CR_ST_at_CC_Cur
                )
    
    
    if CR_ST_at_Cur is not None and len(CR_ST_at_Cur)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='charge_resume',
                Option_Type=OPTION_FILTER,
                Argument_1='CR_ST_at_Cur:CR_ST_at_Cur',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%CR_ST_at_Cur
                )
    
    
    if Cus_Name is not None and len(Cus_Name)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='charge_resume',
                Option_Type=OPTION_FILTER,
                Argument_1='Cus_Name:Cus_Name',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Cus_Name
                )
    
    
    if CI_Name is not None and len(CI_Name)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='charge_resume',
                Option_Type=OPTION_FILTER,
                Argument_1='CI_Name:CI_Name',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%CI_Name
                )
    
    
    if CU_Description is not None and len(CU_Description)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='charge_resume',
                Option_Type=OPTION_FILTER,
                Argument_1='CU_Description:CU_Description',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%CU_Description
                )
    
    
    if CC_Description is not None and len(CC_Description)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='charge_resume',
                Option_Type=OPTION_FILTER,
                Argument_1='CC_Description:CC_Description',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%CC_Description
                )
    
    
    if Rat_Period_Description is not None and len(Rat_Period_Description)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='charge_resume',
                Option_Type=OPTION_FILTER,
                Argument_1='Rat_Period_Description:Rat_Period_Description',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Rat_Period_Description
                )
    
    
    if CC_Code is not None and len(CC_Code)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='charge_resume',
                Option_Type=OPTION_FILTER,
                Argument_1='CC_Code:CC_Code',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%CC_Code
                )
    
    
    if Pla_Id is not None and len(Pla_Id)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='charge_resume',
                Option_Type=OPTION_FILTER,
                Argument_1='Pla_Id:Pla_Id',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Pla_Id
                )
    
    
    if Pla_Name is not None and len(Pla_Name)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='charge_resume',
                Option_Type=OPTION_FILTER,
                Argument_1='Pla_Name:Pla_Name',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Pla_Name
                )
    
    
    
    statement_query,options=get_query_options(engine=db.engine,Interface=Interface,Table_name='charge_resume',User_Id=current_user.id)
    query=eval(statement_query)
    filtered_query = query    
    if mode == 'filter':
        query=filtered_query
    elif mode == 'export':
        query=filtered_query
        fh,output_file = tempfile.mkstemp(suffix='', prefix='Charge_Resumes_', dir=None, text=False)
        dict = {'header':{},'detail':[]}
        count = 0
        rows = query.all()
        for row in rows:
            dict['detail'].append({})
            for column in ['Cus_Id', 'CR_Date_From', 'CR_Date_To', 'CIT_Status', 'Cur_Code', 'CIT_Count', 'CIT_Quantity', 'CIT_Generation', 'CU_Id', 'CI_CC_Id', 'CU_Operation', 'Typ_Code', 'CC_Cur_Code', 'CI_Id', 'Rat_Id', 'Rat_Price', 'Rat_MU_Code', 'Rat_Cur_Code', 'Rat_Period', 'Rat_Hourly', 'Rat_Daily', 'Rat_Monthly', 'CR_Quantity', 'CR_Quantity_at_Rate', 'CC_XR', 'CR_Cur_XR', 'CR_ST_at_Rate_Cur', 'CR_ST_at_CC_Cur', 'CR_ST_at_Cur', 'Cus_Name', 'CI_Name', 'CU_Description', 'CC_Description', 'Rat_Period_Description', 'CC_Code', 'Pla_Id', 'Pla_Name']:
                dict['detail'][count].update( { column:str(row.__getattribute__(column))})
                
            count += 1
        dict['header'].update({'count':count})
        jsonarray      = json.dumps(dict)
        data           = json.loads(jsonarray)  
        dataframe      = json_normalize(data, 'detail').assign(**data['header'])
        fh,output_file = tempfile.mkstemp(suffix='', prefix='Charge_Resumes_', dir='/tmp', text=False)
        xlsx_file      = '%s/%s'%(current_app.root_path,url_for('static',filename='%s.xls'%(output_file)))
        dataframe.to_excel(xlsx_file,sheet_name='Charge_Resumes',columns=['Cus_Id', 'CR_Date_From', 'CR_Date_To', 'CIT_Status', 'Cur_Code', 'CIT_Count', 'CIT_Quantity', 'CIT_Generation', 'CU_Id', 'CI_CC_Id', 'CU_Operation', 'Typ_Code', 'CC_Cur_Code', 'CI_Id', 'Rat_Id', 'Rat_Price', 'Rat_MU_Code', 'Rat_Cur_Code', 'Rat_Period', 'Rat_Hourly', 'Rat_Daily', 'Rat_Monthly', 'CR_Quantity', 'CR_Quantity_at_Rate', 'CC_XR', 'CR_Cur_XR', 'CR_ST_at_Rate_Cur', 'CR_ST_at_CC_Cur', 'CR_ST_at_Cur', 'Cus_Name', 'CI_Name', 'CU_Description', 'CC_Description', 'Rat_Period_Description', 'CC_Code', 'Pla_Id', 'Pla_Name'])
        return send_file(xlsx_file,as_attachment=True,attachment_filename=output_file.replace('/','_')+'.xls')
    elif mode == 'add':
        return redirect(url_for('.forms_Charge_Resumes'))
    elif mode == 'select':
        pass
        # if some filter is required
        if field is not None:
            if field == 'Cus_Id':
                if value is not None:
                    query = query.filter_by(Cus_Id=value)
            if field == 'CR_Date_From':
                if value is not None:
                    query = query.filter_by(CR_Date_From=value)
            if field == 'CR_Date_To':
                if value is not None:
                    query = query.filter_by(CR_Date_To=value)
            if field == 'CIT_Status':
                if value is not None:
                    query = query.filter_by(CIT_Status=value)
            if field == 'Cur_Code':
                if value is not None:
                    query = query.filter_by(Cur_Code=value)
            if field == 'CIT_Count':
                if value is not None:
                    query = query.filter_by(CIT_Count=value)
            if field == 'CIT_Quantity':
                if value is not None:
                    query = query.filter_by(CIT_Quantity=value)
            if field == 'CIT_Generation':
                if value is not None:
                    query = query.filter_by(CIT_Generation=value)
            if field == 'CU_Id':
                if value is not None:
                    query = query.filter_by(CU_Id=value)
            if field == 'CI_CC_Id':
                if value is not None:
                    query = query.filter_by(CI_CC_Id=value)
            if field == 'CU_Operation':
                if value is not None:
                    query = query.filter_by(CU_Operation=value)
            if field == 'Typ_Code':
                if value is not None:
                    query = query.filter_by(Typ_Code=value)
            if field == 'CC_Cur_Code':
                if value is not None:
                    query = query.filter_by(CC_Cur_Code=value)
            if field == 'CI_Id':
                if value is not None:
                    query = query.filter_by(CI_Id=value)
            if field == 'Rat_Id':
                if value is not None:
                    query = query.filter_by(Rat_Id=value)
            if field == 'Rat_Price':
                if value is not None:
                    query = query.filter_by(Rat_Price=value)
            if field == 'Rat_MU_Code':
                if value is not None:
                    query = query.filter_by(Rat_MU_Code=value)
            if field == 'Rat_Cur_Code':
                if value is not None:
                    query = query.filter_by(Rat_Cur_Code=value)
            if field == 'Rat_Period':
                if value is not None:
                    query = query.filter_by(Rat_Period=value)
            if field == 'Rat_Hourly':
                if value is not None:
                    query = query.filter_by(Rat_Hourly=value)
            if field == 'Rat_Daily':
                if value is not None:
                    query = query.filter_by(Rat_Daily=value)
            if field == 'Rat_Monthly':
                if value is not None:
                    query = query.filter_by(Rat_Monthly=value)
            if field == 'CR_Quantity':
                if value is not None:
                    query = query.filter_by(CR_Quantity=value)
            if field == 'CR_Quantity_at_Rate':
                if value is not None:
                    query = query.filter_by(CR_Quantity_at_Rate=value)
            if field == 'CC_XR':
                if value is not None:
                    query = query.filter_by(CC_XR=value)
            if field == 'CR_Cur_XR':
                if value is not None:
                    query = query.filter_by(CR_Cur_XR=value)
            if field == 'CR_ST_at_Rate_Cur':
                if value is not None:
                    query = query.filter_by(CR_ST_at_Rate_Cur=value)
            if field == 'CR_ST_at_CC_Cur':
                if value is not None:
                    query = query.filter_by(CR_ST_at_CC_Cur=value)
            if field == 'CR_ST_at_Cur':
                if value is not None:
                    query = query.filter_by(CR_ST_at_Cur=value)
            if field == 'Cus_Name':
                if value is not None:
                    query = query.filter_by(Cus_Name=value)
            if field == 'CI_Name':
                if value is not None:
                    query = query.filter_by(CI_Name=value)
            if field == 'CU_Description':
                if value is not None:
                    query = query.filter_by(CU_Description=value)
            if field == 'CC_Description':
                if value is not None:
                    query = query.filter_by(CC_Description=value)
            if field == 'Rat_Period_Description':
                if value is not None:
                    query = query.filter_by(Rat_Period_Description=value)
            if field == 'CC_Code':
                if value is not None:
                    query = query.filter_by(CC_Code=value)
            if field == 'Pla_Id':
                if value is not None:
                    query = query.filter_by(Pla_Id=value)
            if field == 'Pla_Name':
                if value is not None:
                    query = query.filter_by(Pla_Name=value)
            
    # Actual request from DB follows
    tracebox_log(query,logger,length=50)
    rows = query.paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
    # Setting pagination variables ...
    if field is not None:
       next_url = url_for('.select_Charge_Resumes_query', field=field, value=value, page=rows.next_num) if rows.has_next else None
       prev_url = url_for('.select_Charge_Resumes_query', field=field, value=value, page=rows.prev_num) if rows.has_prev else None
    else:
       next_url = url_for('.select_Charge_Resumes_query', page=rows.next_num) if rows.has_next else None
       prev_url = url_for('.select_Charge_Resumes_query', page=rows.prev_num) if rows.has_prev else None
    # Actual rendering ...
    if request.headers.get('Content-Type') is not None or request.args.get('JSON',None,type=str) is not None:
        if "JSON" in request.headers.get('Content-Type') or request.args.get('JSON',None,type=str) is not None:
            logger.debug('select_Charge_Resumes_query(): will render: JSON rows')
            logger.debug('select_Charge_Resumes_query(): Exit')
            return json.dumps(serialize_object(rows.__dict__))
    logger.debug('select_Charge_Resumes_query(): will render: charge_resumes_All.html')
    logger.debug('select_Charge_Resumes_query(): Exit')
    return render_template('charge_resumes_select_All.html',rows=rows,options=options)
#===============================================================================
   # NOTE: HARDCODE. TO REMOVE --------------------------------------------
def chk_c000001(*args,**kwargs):
    pass
    
from emtec.common.interface import *
from emtec.collector.db.orm_model          import Interface
from emtec.collector.db.flask_models       import interface
#-----------------------------------------------------------------------
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2020-02-20 16:44:35
# =============================================================================

# ======================================================================
#  Auto-Generated code. Do not modify 
#  (C) Sertechno/Emtec Group (2018,2019)
#  GLVH @ 2020-02-20 16:44:40.050365
# ======================================================================
        
# gen_views_form.html:AG 2020-02-20 16:44:40.050388
@main.route('/forms/Charge_Unit_EGM', methods=['GET', 'POST'])
@login_required

def forms_Charge_Unit_EGM():
    """ Form handling function for table Charge_Unit_EGM """
    logger.debug('forms_Charge_Unit_EGM(): Enter')
    CU_Id  =  request.args.get('CU_Id',0,type=int)
    parent_key   = request.args.get('parent_key',None,type=str)
    parent_value = request.args.get('parent_value',0,type=int)
    row =  charge_unit_egm.query.filter(charge_unit_egm.CU_Id == CU_Id).first()
    if row is None:
        row=charge_unit_egm()
        session['is_new_row']=True
    session['data'] =  {  'CU_Id':row.CU_Id, 'Archive':row.Archive, 'Path':row.Path, 'Metric':row.Metric, 'Host':row.Host, 'Port':row.Port, 'User':row.User, 'Password':row.Password, 'Public_Key_File':row.Public_Key_File, 'Passphrase':row.Passphrase }
    
    if parent_key is not None:
       session['data'][parent_key] = parent_value
       print('parent_key  = ',parent_key)
       print('parent_value= ',parent_value)    
       print('session["data"][parent_key] = %s'%(parent_key,session['data'][parent_key]))
    
    form = frm_charge_unit_egm()
    
    if form.has_FKs:
        form.CU_Id.choices = db.session.query(charge_unit.CU_Id,charge_unit.CU_Description).order_by(charge_unit.CU_Description).all()

    
    # Actual Form activation here
    if form.validate_on_submit():
    # Code for SAVE option
        if form.submit_Save.data and current_user.role_id > 1:
    
            row.CU_Id = form.CU_Id.data
            row.Archive = form.Archive.data
            row.Path = form.Path.data
            row.Metric = form.Metric.data
            row.Host = form.Host.data
            row.Port = form.Port.data
            row.User = form.User.data
            row.Password = form.Password.data
            row.Public_Key_File = form.Public_Key_File.data
            row.Passphrase = form.Passphrase.data  
            try:
               session['new_row']=str(row)
               db.session.close()
               db.session.add(row)
               db.session.commit()
               if session['is_new_row']==True:
                   logger.audit ( '%s:NEW:%s' % (current_user.username,session['new_row'] ) )
                   flash('New Charge Unit EGM created OK')
               else:
                   logger.audit ( '%s:OLD:%s' % (current_user.username,session['prev_row']) )
                   logger.audit ( '%s:UPD:%s' % (current_user.username,session['new_row'] ) )    
                   message=Markup('<b>Charge Unit EGM CU_Id saved OK</b>')
                   flash(message)
               db.session.close()
            except Exception as e:
               db.session.rollback()
               db.session.close()
               message=Markup('ERROR saving Charge Unit EGM record : %s'%(e))
               flash(message)
            return redirect(url_for('.select_Charge_Unit_EGM_query'))    
    # Code for NEW option
    # GV 20190109 f.write(        "        elif   form.submit_New.data:\n")
        elif   form.submit_New.data and current_user.role_id>1:
            #print('New Data Here ...')
            session['is_new_row']=True
            db.session.close()
            row=charge_unit_egm()
    
            return redirect(url_for('.forms_Charge_Unit_EGM'))    
    
    # Code for CANCEL option 
        elif   form.submit_Cancel.data:
            #print('Cancel Data Here ... does nothing')
            message=Markup('Charge Unit EGM Record modifications discarded ...')
            flash(message)
    # Code for ANY OTHER option should never get here
        else:
            #print('form validated but not submited ???')
            message=Markup("<b>Charge Unit EGM data modifications not allowed for user '%s'. Please contact EG Suite's Administrator ...</b>"%(current_user.username))    
            flash(message)
    
            return redirect(url_for('.forms_'))    
    
    
    form.CU_Id.data = row.CU_Id
    form.Archive.data = row.Archive
    form.Path.data = row.Path
    form.Metric.data = row.Metric
    form.Host.data = row.Host
    form.Port.data = row.Port
    form.User.data = row.User
    form.Password.data = row.Password
    form.Public_Key_File.data = row.Public_Key_File
    form.Passphrase.data = row.Passphrase
    session['prev_row'] = str(row)
    session['is_new_row'] = False
    logger.debug('forms_Charge_Unit_EGM(): Exit')
    # Generates pagination data here
    P=[]
    # Tab Relations = []
    
    # Generation of pagination data completed       
    return render_template('charge_unit_egm.html', form=form, row=row, P=P)    
# ======================================================================



# ======================================================================
#  Auto-Generated code. Do not modify 
#  (C) Sertechno/Emtec Group (2018,2019)
#  GLVH @ 2020-02-20 16:44:40.073165
# ======================================================================
        
# gen_views_delete.html:AG 2020-02-20 16:44:40.073188
@main.route('/forms/Charge_Unit_EGM_delete', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)

def forms_Charge_Unit_EGM_delete():
    """ Delete record handling function for table Charge_Unit_EGM """
    logger.debug('forms_Charge_Unit_EGM_delete(): Enter')
    CU_Id  =  request.args.get('CU_Id',0,type=int)
    row =  charge_unit_egm.query.filter(charge_unit_egm.CU_Id == CU_Id).first()

    if row is None:
        row=charge_unit_egm()
    session['data'] =  {  'CU_Id':row.CU_Id, 'Archive':row.Archive, 'Path':row.Path, 'Metric':row.Metric, 'Host':row.Host, 'Port':row.Port, 'User':row.User, 'Password':row.Password, 'Public_Key_File':row.Public_Key_File, 'Passphrase':row.Passphrase }
                       
    form = frm_charge_unit_egm_delete()

    # Tab['has_fks'] True
    
    pass # Tab['has_fks'] True
    
            
    # Actual Form activation here
    if form.validate_on_submit():
    
    # Code for SAVE option
        if  form.submit_Delete.data:
            print('Delete Data Here...')

    
    #f.write(        "            print('Delete Data Here...')
            try:
                session['deleted_row']=str(row)
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                logger.audit ( '%s:DEL:%s' % (current_user.username,session['deleted_row']) )
                flash('Charge Unit EGM CU_Id deleted OK')
            except exc.IntegrityError as e:
                db.session.rollback()    
                flash('INTEGRITY ERROR: Are you sure there are no dependant records in other tables?')
                return redirect(url_for('.forms_Charge_Unit_EGM_delete',CU_Id=session['data']['CU_Id']))    
    
            return redirect(url_for('.select_Charge_Unit_EGM_query'))    
    # Code for CANCEL option 
        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
            return redirect(url_for('.select_Charge_Unit_EGM_query'))    
    # Code for ANY OTHER option should never get here
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.select_Charge_Unit_EGM_query'))    
    
    logger.debug('forms_Charge_Unit_EGM_delete(): Exit')
    return render_template('charge_unit_egm_delete.html', form=form, data=session.get('data'),row=row)
#===============================================================================

# ======================================================================
#  Auto-Generated code. Do not modify 
#  (C) Sertechno/Emtec Group (2018,2019)
#  GLVH @ 2020-02-20 16:44:40.126501
# ======================================================================


from pprint import pprint, pformat

# gen_views_select_query.html:AG 2020-02-20 16:44:40.126524        
@main.route('/select/Charge_Unit_EGM_Query', methods=['GET','POST'])
@login_required

def select_Charge_Unit_EGM_query():
    """ Select rows handling function for table 'Charge_Unit_EGM' """
    logger.debug('select_Charge_Unit_EGM_query(): Enter')
    chk_c000001(filename=os.path.join(current_app.root_path, '.c000001'),request=request,db=db,logger=logger)
    # Get parameters from URL call
    ia       =  request.args.get('ia',     None,type=str)
    if ia is not None:
        ia=ia.split(',')
        if ia[0]=='ORDER':
            set_query_option(engine=db.engine,Interface=Interface,User_Id=current_user.id,Table_name='charge_unit_egm',Option_Type=OPTION_ORDER_BY,Argument_1=ia[1],Argument_2=ia[2])
        elif ia[0]=='GROUP':
            set_query_option(engine=db.engine,Interface=Interface,User_Id=current_user.id,Table_name='charge_unit_egm',Option_Type=OPTION_GROUP_BY,Argument_1=ia[1])
        elif ia[0]=='LIMIT':
            set_query_option(engine=db.engine,Interface=Interface,User_Id=current_user.id,Table_name='charge_unit_egm',Option_Type=OPTION_LIMIT,Argument_1=ia[1])

    iad      =  request.args.get('iad',     None,type=int)
    if iad is not None: delete_query_option(engine=db.engine,Interface=Interface,Id=iad) 
    
    field    =  request.args.get('field',   None,type=str)
    value    =  request.args.get('value',   None,type=str)
    
    # Populates a list of foreign keys used for advanced filtering
    # ------------------------------------------------------------------
    foreign_keys={}
    
    foreign_keys.update({'CU_Id':(charge_unit,'charge_unit','CU_Id','CU_Description','Charge Unit Id')})
    # ------------------------------------------------------------------
    
    if field is not None:
        reset_query_options(    engine=db.engine,Interface=Interface,
                                User_Id=current_user.id,
                                Table_name='charge_unit_egm'
                                )

        
        if field in foreign_keys.keys():
            Class,referenced_classname,referenced_Field,referenced_Value,column_Header=foreign_keys[field]
            foreign_field='%s.%s:%s'%(referenced_classname,referenced_Value,column_Header)
            foreign_record=Class.query.get(value)
            foreign_description="'%s'"%getattr(foreign_record,referenced_Value)
        set_query_option(   engine=db.engine,Interface=Interface,
                        User_Id=current_user.id,
                        Table_name='charge_unit_egm',
                        Option_Type=OPTION_FILTER,
                        Argument_1=foreign_field,
                        Argument_2='==',
                        Argument_3=foreign_description
                        )
    page     =  request.args.get('page',    1   ,type=int)
    addx     =  request.args.get('add.x',   None,type=int)
    addy     =  request.args.get('add.y',   None,type=int)
    exportx  =  request.args.get('export.x',None,type=int)
    exporty  =  request.args.get('export.y',None,type=int)
    filterx  =  request.args.get('filter.x',None,type=int)
    filtery  =  request.args.get('filter.y',None,type=int)
    # Select excluyent view mode
    if   addx    is not None: mode = 'add'
    elif exportx is not None: mode = 'export'
    elif filterx is not None: mode = 'filter'
    else:                     mode = 'select'
    CU_Id =  request.args.get('CU_Id',None,type=str)
    Archive =  request.args.get('Archive',None,type=str)
    Path =  request.args.get('Path',None,type=str)
    Metric =  request.args.get('Metric',None,type=str)
    Host =  request.args.get('Host',None,type=str)
    Port =  request.args.get('Port',None,type=str)
    User =  request.args.get('User',None,type=str)
    Password =  request.args.get('Password',None,type=str)
    Public_Key_File =  request.args.get('Public_Key_File',None,type=str)
    Passphrase =  request.args.get('Passphrase',None,type=str)
    
    
    # Build default query all fields from table
    
    if CU_Id is not None and len(CU_Id)>0:
            Class,referenced_classname,referenced_Field,referenced_Value,column_Header=foreign_keys['CU_Id']
            foreign_field='%s.%s:%s'%(referenced_classname,referenced_Value,column_Header)            
            set_query_option(   engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='charge_unit_egm',
                Option_Type=OPTION_FILTER,
                Argument_1=foreign_field,
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%CU_Id
                )
                                
    
    
    if Archive is not None and len(Archive)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='charge_unit_egm',
                Option_Type=OPTION_FILTER,
                Argument_1='Archive:Archive',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Archive
                )
    
    
    if Path is not None and len(Path)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='charge_unit_egm',
                Option_Type=OPTION_FILTER,
                Argument_1='Path:Path',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Path
                )
    
    
    if Metric is not None and len(Metric)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='charge_unit_egm',
                Option_Type=OPTION_FILTER,
                Argument_1='Metric:Metric',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Metric
                )
    
    
    if Host is not None and len(Host)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='charge_unit_egm',
                Option_Type=OPTION_FILTER,
                Argument_1='Host:Host',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Host
                )
    
    
    if Port is not None and len(Port)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='charge_unit_egm',
                Option_Type=OPTION_FILTER,
                Argument_1='Port:Port',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Port
                )
    
    
    if User is not None and len(User)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='charge_unit_egm',
                Option_Type=OPTION_FILTER,
                Argument_1='User:User',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%User
                )
    
    
    if Password is not None and len(Password)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='charge_unit_egm',
                Option_Type=OPTION_FILTER,
                Argument_1='Password:Password',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Password
                )
    
    
    if Public_Key_File is not None and len(Public_Key_File)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='charge_unit_egm',
                Option_Type=OPTION_FILTER,
                Argument_1='Public_Key_File:Public_Key_File',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Public_Key_File
                )
    
    
    if Passphrase is not None and len(Passphrase)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='charge_unit_egm',
                Option_Type=OPTION_FILTER,
                Argument_1='Passphrase:Passphrase',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Passphrase
                )
    
    
    
    statement_query,options=get_query_options(engine=db.engine,Interface=Interface,Table_name='charge_unit_egm',User_Id=current_user.id)
    query=eval(statement_query)
    filtered_query = query    
    if mode == 'filter':
        query=filtered_query
    elif mode == 'export':
        query=filtered_query
        fh,output_file = tempfile.mkstemp(suffix='', prefix='Charge_Unit_EGM_', dir=None, text=False)
        dict = {'header':{},'detail':[]}
        count = 0
        rows = query.all()
        for row in rows:
            dict['detail'].append({})
            for column in ['CU_Id', 'Archive', 'Path', 'Metric', 'Host', 'Port', 'User', 'Password', 'Public_Key_File', 'Passphrase']:
                dict['detail'][count].update( { column:str(row.__getattribute__(column))})
                
            count += 1
        dict['header'].update({'count':count})
        jsonarray      = json.dumps(dict)
        data           = json.loads(jsonarray)  
        dataframe      = json_normalize(data, 'detail').assign(**data['header'])
        fh,output_file = tempfile.mkstemp(suffix='', prefix='Charge_Unit_EGM_', dir='/tmp', text=False)
        xlsx_file      = '%s/%s'%(current_app.root_path,url_for('static',filename='%s.xls'%(output_file)))
        dataframe.to_excel(xlsx_file,sheet_name='Charge_Unit_EGM',columns=['CU_Id', 'Archive', 'Path', 'Metric', 'Host', 'Port', 'User', 'Password', 'Public_Key_File', 'Passphrase'])
        return send_file(xlsx_file,as_attachment=True,attachment_filename=output_file.replace('/','_')+'.xls')
    elif mode == 'add':
        return redirect(url_for('.forms_Charge_Unit_EGM'))
    elif mode == 'select':
        pass
        # if some filter is required
        if field is not None:
            if field == 'CU_Id':
                if value is not None:
                    query = query.filter_by(CU_Id=value)
            if field == 'Archive':
                if value is not None:
                    query = query.filter_by(Archive=value)
            if field == 'Path':
                if value is not None:
                    query = query.filter_by(Path=value)
            if field == 'Metric':
                if value is not None:
                    query = query.filter_by(Metric=value)
            if field == 'Host':
                if value is not None:
                    query = query.filter_by(Host=value)
            if field == 'Port':
                if value is not None:
                    query = query.filter_by(Port=value)
            if field == 'User':
                if value is not None:
                    query = query.filter_by(User=value)
            if field == 'Password':
                if value is not None:
                    query = query.filter_by(Password=value)
            if field == 'Public_Key_File':
                if value is not None:
                    query = query.filter_by(Public_Key_File=value)
            if field == 'Passphrase':
                if value is not None:
                    query = query.filter_by(Passphrase=value)
            # JOIN other tables and generate foreign fields
    query = query.join(charge_unit,charge_unit_egm.CU_Id == charge_unit.CU_Id).add_columns(charge_unit.CU_Description)
    
    # Actual request from DB follows
    tracebox_log(query,logger,length=50)
    rows = query.paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
    # Setting pagination variables ...
    if field is not None:
       next_url = url_for('.select_Charge_Unit_EGM_query', field=field, value=value, page=rows.next_num) if rows.has_next else None
       prev_url = url_for('.select_Charge_Unit_EGM_query', field=field, value=value, page=rows.prev_num) if rows.has_prev else None
    else:
       next_url = url_for('.select_Charge_Unit_EGM_query', page=rows.next_num) if rows.has_next else None
       prev_url = url_for('.select_Charge_Unit_EGM_query', page=rows.prev_num) if rows.has_prev else None
    # Actual rendering ...
    if request.headers.get('Content-Type') is not None or request.args.get('JSON',None,type=str) is not None:
        if "JSON" in request.headers.get('Content-Type') or request.args.get('JSON',None,type=str) is not None:
            logger.debug('select_Charge_Unit_EGM_query(): will render: JSON rows')
            logger.debug('select_Charge_Unit_EGM_query(): Exit')
            return json.dumps(serialize_object(rows.__dict__))
    logger.debug('select_Charge_Unit_EGM_query(): will render: charge_unit_egm_All.html')
    logger.debug('select_Charge_Unit_EGM_query(): Exit')
    return render_template('charge_unit_egm_select_All.html',rows=rows,options=options)
#===============================================================================
   # NOTE: HARDCODE. TO REMOVE --------------------------------------------
def chk_c000001(*args,**kwargs):
    pass
    
from emtec.common.interface import *
from emtec.collector.db.orm_model          import Interface
from emtec.collector.db.flask_models       import interface
#-----------------------------------------------------------------------
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2020-02-20 16:44:35
# =============================================================================

# ======================================================================
#  Auto-Generated code. Do not modify 
#  (C) Sertechno/Emtec Group (2018,2019)
#  GLVH @ 2020-02-20 16:44:40.438012
# ======================================================================
        
# gen_views_form.html:AG 2020-02-20 16:44:40.438035
@main.route('/forms/Charge_Units', methods=['GET', 'POST'])
@login_required

def forms_Charge_Units():
    """ Form handling function for table Charge_Units """
    logger.debug('forms_Charge_Units(): Enter')
    CU_Id  =  request.args.get('CU_Id',0,type=int)
    parent_key   = request.args.get('parent_key',None,type=str)
    parent_value = request.args.get('parent_value',0,type=int)
    row =  charge_unit.query.filter(charge_unit.CU_Id == CU_Id).first()
    if row is None:
        row=charge_unit()
        session['is_new_row']=True
    session['data'] =  {  'CU_Id':row.CU_Id, 'CI_Id':row.CI_Id, 'CU_Description':row.CU_Description, 'CU_UUID':row.CU_UUID, 'CU_Is_Billeable':row.CU_Is_Billeable, 'CU_Is_Always_Billeable':row.CU_Is_Always_Billeable, 'CU_Quantity':row.CU_Quantity, 'CU_Operation':row.CU_Operation, 'Typ_Code':row.Typ_Code, 'CIT_Generation':row.CIT_Generation, 'Rat_Id':row.Rat_Id, 'CU_Reference_1':row.CU_Reference_1, 'CU_Reference_2':row.CU_Reference_2, 'CU_Reference_3':row.CU_Reference_3 }
    
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

    
    # Actual Form activation here
    if form.validate_on_submit():
    # Code for SAVE option
        if form.submit_Save.data and current_user.role_id > 1:
    
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
                   message=Markup('<b>Charge Unit CU_Id saved OK</b>')
                   flash(message)
               db.session.close()
            except Exception as e:
               db.session.rollback()
               db.session.close()
               message=Markup('ERROR saving Charge Unit record : %s'%(e))
               flash(message)
            return redirect(url_for('.select_Charge_Units_query'))    
    # Code for NEW option
    # GV 20190109 f.write(        "        elif   form.submit_New.data:\n")
        elif   form.submit_New.data and current_user.role_id>1:
            #print('New Data Here ...')
            session['is_new_row']=True
            db.session.close()
            row=charge_unit()
    
            return redirect(url_for('.forms_Charge_Units',CU_Id=row.CU_Id))
    
    # Code for CANCEL option 
        elif   form.submit_Cancel.data:
            #print('Cancel Data Here ... does nothing')
            message=Markup('Charge Unit Record modifications discarded ...')
            flash(message)
    # Code for ANY OTHER option should never get here
        else:
            #print('form validated but not submited ???')
            message=Markup("<b>Charge Unit data modifications not allowed for user '%s'. Please contact EG Suite's Administrator ...</b>"%(current_user.username))    
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
    session['prev_row'] = str(row)
    session['is_new_row'] = False
    logger.debug('forms_Charge_Units(): Exit')
    # Generates pagination data here
    P=[]
    # Tab Relations = [{'name': 'charge_items', 'class': 'charge_item', 'backref': 'charge_unit', 'caption': 'Charge Items', 'table': 'Charge_Items'}, {'name': 'charge_unit_egm', 'class': 'charge_unit_egm', 'backref': 'charge_unit', 'caption': 'Charge Unit EGM', 'table': 'Charge_Unit_EGM'}]
    
    from flask_sqlalchemy import Pagination
    # [{'name': 'charge_items', 'class': 'charge_item', 'backref': 'charge_unit', 'caption': 'Charge Items', 'table': 'Charge_Items'}, {'name': 'charge_unit_egm', 'class': 'charge_unit_egm', 'backref': 'charge_unit', 'caption': 'Charge Unit EGM', 'table': 'Charge_Unit_EGM'}]
    P.append(({'name': 'charge_items', 'class': 'charge_item', 'backref': 'charge_unit', 'caption': 'Charge Items', 'table': 'Charge_Items'},row.charge_items.paginate()))
    P.append(({'name': 'charge_unit_egm', 'class': 'charge_unit_egm', 'backref': 'charge_unit', 'caption': 'Charge Unit EGM', 'table': 'Charge_Unit_EGM'},row.charge_unit_egm.paginate()))
    
    """
    print("P=",P,type(P))
    for relation,p in P:
        print("relation=",relation)
        print("p.query=",p.query)
        print("p.has_next=",p.has_next,p.next,p.next_num)
        print("p.has_prev=",p.has_prev,p.prev,p.prev_num)
        print("p.pages=",p.pages)
        print("p.iter_pages=",p.iter_pages)
        print("p.per_page=",p.per_page)
        print("p.total=",p.total)
        print("p.items type=",type(p.items),len(p.items))
    """
    
    # Generation of pagination data completed       
    return render_template('charge_units.html', form=form, row=row, P=P)    
# ======================================================================



# ======================================================================
#  Auto-Generated code. Do not modify 
#  (C) Sertechno/Emtec Group (2018,2019)
#  GLVH @ 2020-02-20 16:44:40.460757
# ======================================================================
        
# gen_views_delete.html:AG 2020-02-20 16:44:40.460778
@main.route('/forms/Charge_Units_delete', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@admin_required
def forms_Charge_Units_delete():
    """ Delete record handling function for table Charge_Units """
    logger.debug('forms_Charge_Units_delete(): Enter')
    CU_Id  =  request.args.get('CU_Id',0,type=int)
    row =  charge_unit.query.filter(charge_unit.CU_Id == CU_Id).first()

    if row is None:
        row=charge_unit()
    session['data'] =  {  'CU_Id':row.CU_Id, 'CI_Id':row.CI_Id, 'CU_Description':row.CU_Description, 'CU_UUID':row.CU_UUID, 'CU_Is_Billeable':row.CU_Is_Billeable, 'CU_Is_Always_Billeable':row.CU_Is_Always_Billeable, 'CU_Quantity':row.CU_Quantity, 'CU_Operation':row.CU_Operation, 'Typ_Code':row.Typ_Code, 'CIT_Generation':row.CIT_Generation, 'Rat_Id':row.Rat_Id, 'CU_Reference_1':row.CU_Reference_1, 'CU_Reference_2':row.CU_Reference_2, 'CU_Reference_3':row.CU_Reference_3 }
                       
    form = frm_charge_unit_delete()

    # Tab['has_fks'] True
    
    pass # Tab['has_fks'] True
    
            
    # Actual Form activation here
    if form.validate_on_submit():
    
    # Code for SAVE option
        if  form.submit_Delete.data:
            print('Delete Data Here...')

    
    #f.write(        "            print('Delete Data Here...')
            try:
                session['deleted_row']=str(row)
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                logger.audit ( '%s:DEL:%s' % (current_user.username,session['deleted_row']) )
                flash('Charge Unit CU_Id deleted OK')
            except exc.IntegrityError as e:
                db.session.rollback()    
                flash('INTEGRITY ERROR: Are you sure there are no dependant records in other tables?')
                return redirect(url_for('.forms_Charge_Units_delete',CU_Id=session['data']['CU_Id']))    
    
            return redirect(url_for('.select_Charge_Units_query'))    
    # Code for CANCEL option 
        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
            return redirect(url_for('.select_Charge_Units_query'))    
    # Code for ANY OTHER option should never get here
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.select_Charge_Units_query'))    
    
    logger.debug('forms_Charge_Units_delete(): Exit')
    return render_template('charge_units_delete.html', form=form, data=session.get('data'),row=row)
#===============================================================================

# ======================================================================
#  Auto-Generated code. Do not modify 
#  (C) Sertechno/Emtec Group (2018,2019)
#  GLVH @ 2020-02-20 16:44:40.508369
# ======================================================================


from pprint import pprint, pformat

# gen_views_select_query.html:AG 2020-02-20 16:44:40.508392        
@main.route('/select/Charge_Units_Query', methods=['GET','POST'])
@login_required
@admin_required
def select_Charge_Units_query():
    """ Select rows handling function for table 'Charge_Units' """
    logger.debug('select_Charge_Units_query(): Enter')
    chk_c000001(filename=os.path.join(current_app.root_path, '.c000001'),request=request,db=db,logger=logger)
    # Get parameters from URL call
    ia       =  request.args.get('ia',     None,type=str)
    if ia is not None:
        ia=ia.split(',')
        if ia[0]=='ORDER':
            set_query_option(engine=db.engine,Interface=Interface,User_Id=current_user.id,Table_name='charge_unit',Option_Type=OPTION_ORDER_BY,Argument_1=ia[1],Argument_2=ia[2])
        elif ia[0]=='GROUP':
            set_query_option(engine=db.engine,Interface=Interface,User_Id=current_user.id,Table_name='charge_unit',Option_Type=OPTION_GROUP_BY,Argument_1=ia[1])
        elif ia[0]=='LIMIT':
            set_query_option(engine=db.engine,Interface=Interface,User_Id=current_user.id,Table_name='charge_unit',Option_Type=OPTION_LIMIT,Argument_1=ia[1])

    iad      =  request.args.get('iad',     None,type=int)
    if iad is not None: delete_query_option(engine=db.engine,Interface=Interface,Id=iad) 
    
    field    =  request.args.get('field',   None,type=str)
    value    =  request.args.get('value',   None,type=str)
    
    # Populates a list of foreign keys used for advanced filtering
    # ------------------------------------------------------------------
    foreign_keys={}
    
    foreign_keys.update({'CI_Id':(configuration_item,'configuration_item','CI_Id','CI_Name','Configuration Item Id')})
    foreign_keys.update({'CU_Operation':(cu_operation,'cu_operation','CU_Operation','Value','Conversion Operation')})
    foreign_keys.update({'Typ_Code':(cu_type,'cu_type','Typ_Code','Typ_Description','Type')})
    foreign_keys.update({'CIT_Generation':(cit_generation,'cit_generation','CIT_Generation','Value','Item Generation Type')})
    # ------------------------------------------------------------------
    
    if field is not None:
        reset_query_options(    engine=db.engine,Interface=Interface,
                                User_Id=current_user.id,
                                Table_name='charge_unit'
                                )

        
        if field in foreign_keys.keys():
            Class,referenced_classname,referenced_Field,referenced_Value,column_Header=foreign_keys[field]
            foreign_field='%s.%s:%s'%(referenced_classname,referenced_Value,column_Header)
            foreign_record=Class.query.get(value)
            foreign_description="'%s'"%getattr(foreign_record,referenced_Value)
        set_query_option(   engine=db.engine,Interface=Interface,
                        User_Id=current_user.id,
                        Table_name='charge_unit',
                        Option_Type=OPTION_FILTER,
                        Argument_1=foreign_field,
                        Argument_2='==',
                        Argument_3=foreign_description
                        )
    page     =  request.args.get('page',    1   ,type=int)
    addx     =  request.args.get('add.x',   None,type=int)
    addy     =  request.args.get('add.y',   None,type=int)
    exportx  =  request.args.get('export.x',None,type=int)
    exporty  =  request.args.get('export.y',None,type=int)
    filterx  =  request.args.get('filter.x',None,type=int)
    filtery  =  request.args.get('filter.y',None,type=int)
    # Select excluyent view mode
    if   addx    is not None: mode = 'add'
    elif exportx is not None: mode = 'export'
    elif filterx is not None: mode = 'filter'
    else:                     mode = 'select'
    CU_Id =  request.args.get('CU_Id',None,type=str)
    CI_Id =  request.args.get('CI_Id',None,type=str)
    CU_Description =  request.args.get('CU_Description',None,type=str)
    CU_UUID =  request.args.get('CU_UUID',None,type=str)
    CU_Is_Billeable =  request.args.get('CU_Is_Billeable',None,type=str)
    CU_Is_Always_Billeable =  request.args.get('CU_Is_Always_Billeable',None,type=str)
    CU_Quantity =  request.args.get('CU_Quantity',None,type=str)
    CU_Operation =  request.args.get('CU_Operation',None,type=str)
    Typ_Code =  request.args.get('Typ_Code',None,type=str)
    CIT_Generation =  request.args.get('CIT_Generation',None,type=str)
    Rat_Id =  request.args.get('Rat_Id',None,type=str)
    CU_Reference_1 =  request.args.get('CU_Reference_1',None,type=str)
    CU_Reference_2 =  request.args.get('CU_Reference_2',None,type=str)
    CU_Reference_3 =  request.args.get('CU_Reference_3',None,type=str)
    
    
    # Build default query all fields from table
    
    if CU_Id is not None and len(CU_Id)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='charge_unit',
                Option_Type=OPTION_FILTER,
                Argument_1='CU_Id:Id',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%CU_Id
                )
    
    
    if CI_Id is not None and len(CI_Id)>0:
            Class,referenced_classname,referenced_Field,referenced_Value,column_Header=foreign_keys['CI_Id']
            foreign_field='%s.%s:%s'%(referenced_classname,referenced_Value,column_Header)            
            set_query_option(   engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='charge_unit',
                Option_Type=OPTION_FILTER,
                Argument_1=foreign_field,
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%CI_Id
                )
                                
    
    
    if CU_Description is not None and len(CU_Description)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='charge_unit',
                Option_Type=OPTION_FILTER,
                Argument_1='CU_Description:Description',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%CU_Description
                )
    
    
    if CU_UUID is not None and len(CU_UUID)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='charge_unit',
                Option_Type=OPTION_FILTER,
                Argument_1='CU_UUID:UUID',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%CU_UUID
                )
    
    
    if CU_Is_Billeable is not None and len(CU_Is_Billeable)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='charge_unit',
                Option_Type=OPTION_FILTER,
                Argument_1='CU_Is_Billeable:Is Billeable',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%CU_Is_Billeable
                )
    
    
    if CU_Is_Always_Billeable is not None and len(CU_Is_Always_Billeable)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='charge_unit',
                Option_Type=OPTION_FILTER,
                Argument_1='CU_Is_Always_Billeable:Is Always Billeable',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%CU_Is_Always_Billeable
                )
    
    
    if CU_Quantity is not None and len(CU_Quantity)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='charge_unit',
                Option_Type=OPTION_FILTER,
                Argument_1='CU_Quantity:Quantity',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%CU_Quantity
                )
    
    
    if CU_Operation is not None and len(CU_Operation)>0:
            Class,referenced_classname,referenced_Field,referenced_Value,column_Header=foreign_keys['CU_Operation']
            foreign_field='%s.%s:%s'%(referenced_classname,referenced_Value,column_Header)            
            set_query_option(   engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='charge_unit',
                Option_Type=OPTION_FILTER,
                Argument_1=foreign_field,
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%CU_Operation
                )
                                
    
    
    if Typ_Code is not None and len(Typ_Code)>0:
            Class,referenced_classname,referenced_Field,referenced_Value,column_Header=foreign_keys['Typ_Code']
            foreign_field='%s.%s:%s'%(referenced_classname,referenced_Value,column_Header)            
            set_query_option(   engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='charge_unit',
                Option_Type=OPTION_FILTER,
                Argument_1=foreign_field,
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Typ_Code
                )
                                
    
    
    if CIT_Generation is not None and len(CIT_Generation)>0:
            Class,referenced_classname,referenced_Field,referenced_Value,column_Header=foreign_keys['CIT_Generation']
            foreign_field='%s.%s:%s'%(referenced_classname,referenced_Value,column_Header)            
            set_query_option(   engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='charge_unit',
                Option_Type=OPTION_FILTER,
                Argument_1=foreign_field,
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%CIT_Generation
                )
                                
    
    
    if Rat_Id is not None and len(Rat_Id)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='charge_unit',
                Option_Type=OPTION_FILTER,
                Argument_1='Rat_Id:Rate Id',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Rat_Id
                )
    
    
    if CU_Reference_1 is not None and len(CU_Reference_1)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='charge_unit',
                Option_Type=OPTION_FILTER,
                Argument_1='CU_Reference_1:Reference 1',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%CU_Reference_1
                )
    
    
    if CU_Reference_2 is not None and len(CU_Reference_2)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='charge_unit',
                Option_Type=OPTION_FILTER,
                Argument_1='CU_Reference_2:Reference 2',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%CU_Reference_2
                )
    
    
    if CU_Reference_3 is not None and len(CU_Reference_3)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='charge_unit',
                Option_Type=OPTION_FILTER,
                Argument_1='CU_Reference_3:Reference 3',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%CU_Reference_3
                )
    
    
    
    statement_query,options=get_query_options(engine=db.engine,Interface=Interface,Table_name='charge_unit',User_Id=current_user.id)
    query=eval(statement_query)
    filtered_query = query    
    if mode == 'filter':
        query=filtered_query
    elif mode == 'export':
        query=filtered_query
        fh,output_file = tempfile.mkstemp(suffix='', prefix='Charge_Units_', dir=None, text=False)
        dict = {'header':{},'detail':[]}
        count = 0
        rows = query.all()
        for row in rows:
            dict['detail'].append({})
            for column in ['CU_Id', 'CI_Id', 'CU_Description', 'CU_UUID', 'CU_Is_Billeable', 'CU_Is_Always_Billeable', 'CU_Quantity', 'CU_Operation', 'Typ_Code', 'CIT_Generation', 'Rat_Id', 'CU_Reference_1', 'CU_Reference_2', 'CU_Reference_3']:
                dict['detail'][count].update( { column:str(row.__getattribute__(column))})
                
            count += 1
        dict['header'].update({'count':count})
        jsonarray      = json.dumps(dict)
        data           = json.loads(jsonarray)  
        dataframe      = json_normalize(data, 'detail').assign(**data['header'])
        fh,output_file = tempfile.mkstemp(suffix='', prefix='Charge_Units_', dir='/tmp', text=False)
        xlsx_file      = '%s/%s'%(current_app.root_path,url_for('static',filename='%s.xls'%(output_file)))
        dataframe.to_excel(xlsx_file,sheet_name='Charge_Units',columns=['CU_Id', 'CI_Id', 'CU_Description', 'CU_UUID', 'CU_Is_Billeable', 'CU_Is_Always_Billeable', 'CU_Quantity', 'CU_Operation', 'Typ_Code', 'CIT_Generation', 'Rat_Id', 'CU_Reference_1', 'CU_Reference_2', 'CU_Reference_3'])
        return send_file(xlsx_file,as_attachment=True,attachment_filename=output_file.replace('/','_')+'.xls')
    elif mode == 'add':
        return redirect(url_for('.forms_Charge_Units'))
    elif mode == 'select':
        pass
        # if some filter is required
        if field is not None:
            if field == 'CU_Id':
                if value is not None:
                    query = query.filter_by(CU_Id=value)
            if field == 'CI_Id':
                if value is not None:
                    query = query.filter_by(CI_Id=value)
            if field == 'CU_Description':
                if value is not None:
                    query = query.filter_by(CU_Description=value)
            if field == 'CU_UUID':
                if value is not None:
                    query = query.filter_by(CU_UUID=value)
            if field == 'CU_Is_Billeable':
                if value is not None:
                    query = query.filter_by(CU_Is_Billeable=value)
            if field == 'CU_Is_Always_Billeable':
                if value is not None:
                    query = query.filter_by(CU_Is_Always_Billeable=value)
            if field == 'CU_Quantity':
                if value is not None:
                    query = query.filter_by(CU_Quantity=value)
            if field == 'CU_Operation':
                if value is not None:
                    query = query.filter_by(CU_Operation=value)
            if field == 'Typ_Code':
                if value is not None:
                    query = query.filter_by(Typ_Code=value)
            if field == 'CIT_Generation':
                if value is not None:
                    query = query.filter_by(CIT_Generation=value)
            if field == 'Rat_Id':
                if value is not None:
                    query = query.filter_by(Rat_Id=value)
            if field == 'CU_Reference_1':
                if value is not None:
                    query = query.filter_by(CU_Reference_1=value)
            if field == 'CU_Reference_2':
                if value is not None:
                    query = query.filter_by(CU_Reference_2=value)
            if field == 'CU_Reference_3':
                if value is not None:
                    query = query.filter_by(CU_Reference_3=value)
            # JOIN other tables and generate foreign fields
    query = query.join(configuration_item,charge_unit.CI_Id == configuration_item.CI_Id).add_columns(configuration_item.CI_Name).join(cu_operation,charge_unit.CU_Operation == cu_operation.CU_Operation).add_columns(cu_operation.Value).join(cu_type,charge_unit.Typ_Code == cu_type.Typ_Code).add_columns(cu_type.Typ_Description).join(cit_generation,charge_unit.CIT_Generation == cit_generation.CIT_Generation).add_columns(cit_generation.Value)
    
    # Actual request from DB follows
    tracebox_log(query,logger,length=50)
    rows = query.paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
    # Setting pagination variables ...
    if field is not None:
       next_url = url_for('.select_Charge_Units_query', field=field, value=value, page=rows.next_num) if rows.has_next else None
       prev_url = url_for('.select_Charge_Units_query', field=field, value=value, page=rows.prev_num) if rows.has_prev else None
    else:
       next_url = url_for('.select_Charge_Units_query', page=rows.next_num) if rows.has_next else None
       prev_url = url_for('.select_Charge_Units_query', page=rows.prev_num) if rows.has_prev else None
    # Actual rendering ...
    if request.headers.get('Content-Type') is not None or request.args.get('JSON',None,type=str) is not None:
        if "JSON" in request.headers.get('Content-Type') or request.args.get('JSON',None,type=str) is not None:
            logger.debug('select_Charge_Units_query(): will render: JSON rows')
            logger.debug('select_Charge_Units_query(): Exit')
            return json.dumps(serialize_object(rows.__dict__))
    logger.debug('select_Charge_Units_query(): will render: charge_units_All.html')
    logger.debug('select_Charge_Units_query(): Exit')
    return render_template('charge_units_select_All.html',rows=rows,options=options)
#===============================================================================
   # NOTE: HARDCODE. TO REMOVE --------------------------------------------
def chk_c000001(*args,**kwargs):
    pass
    
from emtec.common.interface import *
from emtec.collector.db.orm_model          import Interface
from emtec.collector.db.flask_models       import interface
#-----------------------------------------------------------------------
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2020-02-20 16:44:35
# =============================================================================

# ======================================================================
#  Auto-Generated code. Do not modify 
#  (C) Sertechno/Emtec Group (2018,2019)
#  GLVH @ 2020-02-20 16:44:37.808919
# ======================================================================
        
# gen_views_form.html:AG 2020-02-20 16:44:37.808951
@main.route('/forms/CIT_Generations', methods=['GET', 'POST'])
@login_required

def forms_CIT_Generations():
    """ Form handling function for table CIT_Generations """
    logger.debug('forms_CIT_Generations(): Enter')
    CIT_Generation  =  request.args.get('CIT_Generation',0,type=int)
    
    row =  cit_generation.query.filter(cit_generation.CIT_Generation == CIT_Generation).first()
    if row is None:
        row=cit_generation()
        session['is_new_row']=True
    session['data'] =  {  'CIT_Generation':row.CIT_Generation, 'Value':row.Value }
    
    form = frm_cit_generation()
    
    # Actual Form activation here
    if form.validate_on_submit():
    # Code for SAVE option
        if form.submit_Save.data and current_user.role_id > 1:
    
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
                   message=Markup('<b>Configuration Item Generation Type CIT_Generation saved OK</b>')
                   flash(message)
               db.session.close()
            except Exception as e:
               db.session.rollback()
               db.session.close()
               message=Markup('ERROR saving Configuration Item Generation Type record : %s'%(e))
               flash(message)
            return redirect(url_for('.select_CIT_Generations_query'))    
    # Code for NEW option
    # GV 20190109 f.write(        "        elif   form.submit_New.data:\n")
        elif   form.submit_New.data and current_user.role_id>1:
            #print('New Data Here ...')
            session['is_new_row']=True
            db.session.close()
            row=cit_generation()
    
            return redirect(url_for('.forms_CIT_Generations'))    
    
    # Code for CANCEL option 
        elif   form.submit_Cancel.data:
            #print('Cancel Data Here ... does nothing')
            message=Markup('Configuration Item Generation Type Record modifications discarded ...')
            flash(message)
    # Code for ANY OTHER option should never get here
        else:
            #print('form validated but not submited ???')
            message=Markup("<b>Configuration Item Generation Type data modifications not allowed for user '%s'. Please contact EG Suite's Administrator ...</b>"%(current_user.username))    
            flash(message)
    
            return redirect(url_for('.forms_'))    
    
    
    form.CIT_Generation.data = row.CIT_Generation
    form.Value.data = row.Value
    session['prev_row'] = str(row)
    session['is_new_row'] = False
    logger.debug('forms_CIT_Generations(): Exit')
    # Generates pagination data here
    P=[]
    # Tab Relations = [{'name': 'charge_units', 'class': 'charge_unit', 'backref': 'cit_generation', 'caption': 'Charge Units', 'table': 'Charge_Units'}]
    
    from flask_sqlalchemy import Pagination
    # [{'name': 'charge_units', 'class': 'charge_unit', 'backref': 'cit_generation', 'caption': 'Charge Units', 'table': 'Charge_Units'}]
    P.append(({'name': 'charge_units', 'class': 'charge_unit', 'backref': 'cit_generation', 'caption': 'Charge Units', 'table': 'Charge_Units'},row.charge_units.paginate()))
    
    """
    print("P=",P,type(P))
    for relation,p in P:
        print("relation=",relation)
        print("p.query=",p.query)
        print("p.has_next=",p.has_next,p.next,p.next_num)
        print("p.has_prev=",p.has_prev,p.prev,p.prev_num)
        print("p.pages=",p.pages)
        print("p.iter_pages=",p.iter_pages)
        print("p.per_page=",p.per_page)
        print("p.total=",p.total)
        print("p.items type=",type(p.items),len(p.items))
    """
    
    # Generation of pagination data completed       
    return render_template('cit_generations.html', form=form, row=row, P=P)    
# ======================================================================



# ======================================================================
#  Auto-Generated code. Do not modify 
#  (C) Sertechno/Emtec Group (2018,2019)
#  GLVH @ 2020-02-20 16:44:37.835406
# ======================================================================
        
# gen_views_delete.html:AG 2020-02-20 16:44:37.835431
@main.route('/forms/CIT_Generations_delete', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@admin_required
def forms_CIT_Generations_delete():
    """ Delete record handling function for table CIT_Generations """
    logger.debug('forms_CIT_Generations_delete(): Enter')
    CIT_Generation  =  request.args.get('CIT_Generation',0,type=int)
    row =  cit_generation.query.filter(cit_generation.CIT_Generation == CIT_Generation).first()

    if row is None:
        row=cit_generation()
    session['data'] =  {  'CIT_Generation':row.CIT_Generation, 'Value':row.Value }
                       
    form = frm_cit_generation_delete()

    # Tab['has_fks'] False
    
            
    # Actual Form activation here
    if form.validate_on_submit():
    
    # Code for SAVE option
        if  form.submit_Delete.data:
            print('Delete Data Here...')

    
    #f.write(        "            print('Delete Data Here...')
            try:
                session['deleted_row']=str(row)
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                logger.audit ( '%s:DEL:%s' % (current_user.username,session['deleted_row']) )
                flash('Configuration Item Generation Type CIT_Generation deleted OK')
            except exc.IntegrityError as e:
                db.session.rollback()    
                flash('INTEGRITY ERROR: Are you sure there are no dependant records in other tables?')
                return redirect(url_for('.forms_CIT_Generations_delete',CIT_Generation=session['data']['CIT_Generation']))    
    
            return redirect(url_for('.select_CIT_Generations_query'))    
    # Code for CANCEL option 
        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
            return redirect(url_for('.select_CIT_Generations_query'))    
    # Code for ANY OTHER option should never get here
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.select_CIT_Generations_query'))    
    
    logger.debug('forms_CIT_Generations_delete(): Exit')
    return render_template('cit_generations_delete.html', form=form, data=session.get('data'),row=row)
#===============================================================================

# ======================================================================
#  Auto-Generated code. Do not modify 
#  (C) Sertechno/Emtec Group (2018,2019)
#  GLVH @ 2020-02-20 16:44:37.890874
# ======================================================================


from pprint import pprint, pformat

# gen_views_select_query.html:AG 2020-02-20 16:44:37.890900        
@main.route('/select/CIT_Generations_Query', methods=['GET','POST'])
@login_required
@admin_required
def select_CIT_Generations_query():
    """ Select rows handling function for table 'CIT_Generations' """
    logger.debug('select_CIT_Generations_query(): Enter')
    chk_c000001(filename=os.path.join(current_app.root_path, '.c000001'),request=request,db=db,logger=logger)
    # Get parameters from URL call
    ia       =  request.args.get('ia',     None,type=str)
    if ia is not None:
        ia=ia.split(',')
        if ia[0]=='ORDER':
            set_query_option(engine=db.engine,Interface=Interface,User_Id=current_user.id,Table_name='cit_generation',Option_Type=OPTION_ORDER_BY,Argument_1=ia[1],Argument_2=ia[2])
        elif ia[0]=='GROUP':
            set_query_option(engine=db.engine,Interface=Interface,User_Id=current_user.id,Table_name='cit_generation',Option_Type=OPTION_GROUP_BY,Argument_1=ia[1])
        elif ia[0]=='LIMIT':
            set_query_option(engine=db.engine,Interface=Interface,User_Id=current_user.id,Table_name='cit_generation',Option_Type=OPTION_LIMIT,Argument_1=ia[1])

    iad      =  request.args.get('iad',     None,type=int)
    if iad is not None: delete_query_option(engine=db.engine,Interface=Interface,Id=iad) 
    
    field    =  request.args.get('field',   None,type=str)
    value    =  request.args.get('value',   None,type=str)
    
    # Populates a list of foreign keys used for advanced filtering
    # ------------------------------------------------------------------
    foreign_keys={}
    
    # ------------------------------------------------------------------
    
    if field is not None:
        reset_query_options(    engine=db.engine,Interface=Interface,
                                User_Id=current_user.id,
                                Table_name='cit_generation'
                                )

        
        if field in foreign_keys.keys():
            Class,referenced_classname,referenced_Field,referenced_Value,column_Header=foreign_keys[field]
            foreign_field='%s.%s:%s'%(referenced_classname,referenced_Value,column_Header)
            foreign_record=Class.query.get(value)
            foreign_description="'%s'"%getattr(foreign_record,referenced_Value)
        set_query_option(   engine=db.engine,Interface=Interface,
                        User_Id=current_user.id,
                        Table_name='cit_generation',
                        Option_Type=OPTION_FILTER,
                        Argument_1=foreign_field,
                        Argument_2='==',
                        Argument_3=foreign_description
                        )
    page     =  request.args.get('page',    1   ,type=int)
    addx     =  request.args.get('add.x',   None,type=int)
    addy     =  request.args.get('add.y',   None,type=int)
    exportx  =  request.args.get('export.x',None,type=int)
    exporty  =  request.args.get('export.y',None,type=int)
    filterx  =  request.args.get('filter.x',None,type=int)
    filtery  =  request.args.get('filter.y',None,type=int)
    # Select excluyent view mode
    if   addx    is not None: mode = 'add'
    elif exportx is not None: mode = 'export'
    elif filterx is not None: mode = 'filter'
    else:                     mode = 'select'
    CIT_Generation =  request.args.get('CIT_Generation',None,type=str)
    Value =  request.args.get('Value',None,type=str)
    
    
    # Build default query all fields from table
    
    if CIT_Generation is not None and len(CIT_Generation)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='cit_generation',
                Option_Type=OPTION_FILTER,
                Argument_1='CIT_Generation:CIT_Generation',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%CIT_Generation
                )
    
    
    if Value is not None and len(Value)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='cit_generation',
                Option_Type=OPTION_FILTER,
                Argument_1='Value:Value',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Value
                )
    
    
    
    statement_query,options=get_query_options(engine=db.engine,Interface=Interface,Table_name='cit_generation',User_Id=current_user.id)
    query=eval(statement_query)
    filtered_query = query    
    if mode == 'filter':
        query=filtered_query
    elif mode == 'export':
        query=filtered_query
        fh,output_file = tempfile.mkstemp(suffix='', prefix='CIT_Generations_', dir=None, text=False)
        dict = {'header':{},'detail':[]}
        count = 0
        rows = query.all()
        for row in rows:
            dict['detail'].append({})
            for column in ['CIT_Generation', 'Value']:
                dict['detail'][count].update( { column:str(row.__getattribute__(column))})
                
            count += 1
        dict['header'].update({'count':count})
        jsonarray      = json.dumps(dict)
        data           = json.loads(jsonarray)  
        dataframe      = json_normalize(data, 'detail').assign(**data['header'])
        fh,output_file = tempfile.mkstemp(suffix='', prefix='CIT_Generations_', dir='/tmp', text=False)
        xlsx_file      = '%s/%s'%(current_app.root_path,url_for('static',filename='%s.xls'%(output_file)))
        dataframe.to_excel(xlsx_file,sheet_name='CIT_Generations',columns=['CIT_Generation', 'Value'])
        return send_file(xlsx_file,as_attachment=True,attachment_filename=output_file.replace('/','_')+'.xls')
    elif mode == 'add':
        return redirect(url_for('.forms_CIT_Generations'))
    elif mode == 'select':
        pass
        # if some filter is required
        if field is not None:
            if field == 'CIT_Generation':
                if value is not None:
                    query = query.filter_by(CIT_Generation=value)
            if field == 'Value':
                if value is not None:
                    query = query.filter_by(Value=value)
            
    # Actual request from DB follows
    tracebox_log(query,logger,length=50)
    rows = query.paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
    # Setting pagination variables ...
    if field is not None:
       next_url = url_for('.select_CIT_Generations_query', field=field, value=value, page=rows.next_num) if rows.has_next else None
       prev_url = url_for('.select_CIT_Generations_query', field=field, value=value, page=rows.prev_num) if rows.has_prev else None
    else:
       next_url = url_for('.select_CIT_Generations_query', page=rows.next_num) if rows.has_next else None
       prev_url = url_for('.select_CIT_Generations_query', page=rows.prev_num) if rows.has_prev else None
    # Actual rendering ...
    if request.headers.get('Content-Type') is not None or request.args.get('JSON',None,type=str) is not None:
        if "JSON" in request.headers.get('Content-Type') or request.args.get('JSON',None,type=str) is not None:
            logger.debug('select_CIT_Generations_query(): will render: JSON rows')
            logger.debug('select_CIT_Generations_query(): Exit')
            return json.dumps(serialize_object(rows.__dict__))
    logger.debug('select_CIT_Generations_query(): will render: cit_generations_All.html')
    logger.debug('select_CIT_Generations_query(): Exit')
    return render_template('cit_generations_select_All.html',rows=rows,options=options)
#===============================================================================
   # NOTE: HARDCODE. TO REMOVE --------------------------------------------
def chk_c000001(*args,**kwargs):
    pass
    
from emtec.common.interface import *
from emtec.collector.db.orm_model          import Interface
from emtec.collector.db.flask_models       import interface
#-----------------------------------------------------------------------
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2020-02-20 16:44:35
# =============================================================================

# ======================================================================
#  Auto-Generated code. Do not modify 
#  (C) Sertechno/Emtec Group (2018,2019)
#  GLVH @ 2020-02-20 16:44:38.147426
# ======================================================================
        
# gen_views_form.html:AG 2020-02-20 16:44:38.147449
@main.route('/forms/CIT_Statuses', methods=['GET', 'POST'])
@login_required

def forms_CIT_Statuses():
    """ Form handling function for table CIT_Statuses """
    logger.debug('forms_CIT_Statuses(): Enter')
    CIT_Status  =  request.args.get('CIT_Status',0,type=int)
    
    row =  cit_status.query.filter(cit_status.CIT_Status == CIT_Status).first()
    if row is None:
        row=cit_status()
        session['is_new_row']=True
    session['data'] =  {  'CIT_Status':row.CIT_Status, 'Value':row.Value }
    
    form = frm_cit_status()
    
    # Actual Form activation here
    if form.validate_on_submit():
    # Code for SAVE option
        if form.submit_Save.data and current_user.role_id > 1:
    
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
                   message=Markup('<b>Configuration Item Status Type CIT_Status saved OK</b>')
                   flash(message)
               db.session.close()
            except Exception as e:
               db.session.rollback()
               db.session.close()
               message=Markup('ERROR saving Configuration Item Status Type record : %s'%(e))
               flash(message)
            return redirect(url_for('.select_CIT_Statuses_query'))    
    # Code for NEW option
    # GV 20190109 f.write(        "        elif   form.submit_New.data:\n")
        elif   form.submit_New.data and current_user.role_id>1:
            #print('New Data Here ...')
            session['is_new_row']=True
            db.session.close()
            row=cit_status()
    
            return redirect(url_for('.forms_CIT_Statuses'))    
    
    # Code for CANCEL option 
        elif   form.submit_Cancel.data:
            #print('Cancel Data Here ... does nothing')
            message=Markup('Configuration Item Status Type Record modifications discarded ...')
            flash(message)
    # Code for ANY OTHER option should never get here
        else:
            #print('form validated but not submited ???')
            message=Markup("<b>Configuration Item Status Type data modifications not allowed for user '%s'. Please contact EG Suite's Administrator ...</b>"%(current_user.username))    
            flash(message)
    
            return redirect(url_for('.forms_'))    
    
    
    form.CIT_Status.data = row.CIT_Status
    form.Value.data = row.Value
    session['prev_row'] = str(row)
    session['is_new_row'] = False
    logger.debug('forms_CIT_Statuses(): Exit')
    # Generates pagination data here
    P=[]
    # Tab Relations = [{'name': 'charge_items', 'class': 'charge_item', 'backref': 'cit_status', 'caption': 'Charge Items', 'table': 'Charge_Items'}]
    
    from flask_sqlalchemy import Pagination
    # [{'name': 'charge_items', 'class': 'charge_item', 'backref': 'cit_status', 'caption': 'Charge Items', 'table': 'Charge_Items'}]
    P.append(({'name': 'charge_items', 'class': 'charge_item', 'backref': 'cit_status', 'caption': 'Charge Items', 'table': 'Charge_Items'},row.charge_items.paginate()))
    
    """
    print("P=",P,type(P))
    for relation,p in P:
        print("relation=",relation)
        print("p.query=",p.query)
        print("p.has_next=",p.has_next,p.next,p.next_num)
        print("p.has_prev=",p.has_prev,p.prev,p.prev_num)
        print("p.pages=",p.pages)
        print("p.iter_pages=",p.iter_pages)
        print("p.per_page=",p.per_page)
        print("p.total=",p.total)
        print("p.items type=",type(p.items),len(p.items))
    """
    
    # Generation of pagination data completed       
    return render_template('cit_statuses.html', form=form, row=row, P=P)    
# ======================================================================



# ======================================================================
#  Auto-Generated code. Do not modify 
#  (C) Sertechno/Emtec Group (2018,2019)
#  GLVH @ 2020-02-20 16:44:38.170963
# ======================================================================
        
# gen_views_delete.html:AG 2020-02-20 16:44:38.170986
@main.route('/forms/CIT_Statuses_delete', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@admin_required
def forms_CIT_Statuses_delete():
    """ Delete record handling function for table CIT_Statuses """
    logger.debug('forms_CIT_Statuses_delete(): Enter')
    CIT_Status  =  request.args.get('CIT_Status',0,type=int)
    row =  cit_status.query.filter(cit_status.CIT_Status == CIT_Status).first()

    if row is None:
        row=cit_status()
    session['data'] =  {  'CIT_Status':row.CIT_Status, 'Value':row.Value }
                       
    form = frm_cit_status_delete()

    # Tab['has_fks'] False
    
            
    # Actual Form activation here
    if form.validate_on_submit():
    
    # Code for SAVE option
        if  form.submit_Delete.data:
            print('Delete Data Here...')

    
    #f.write(        "            print('Delete Data Here...')
            try:
                session['deleted_row']=str(row)
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                logger.audit ( '%s:DEL:%s' % (current_user.username,session['deleted_row']) )
                flash('Configuration Item Status Type CIT_Status deleted OK')
            except exc.IntegrityError as e:
                db.session.rollback()    
                flash('INTEGRITY ERROR: Are you sure there are no dependant records in other tables?')
                return redirect(url_for('.forms_CIT_Statuses_delete',CIT_Status=session['data']['CIT_Status']))    
    
            return redirect(url_for('.select_CIT_Statuses_query'))    
    # Code for CANCEL option 
        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
            return redirect(url_for('.select_CIT_Statuses_query'))    
    # Code for ANY OTHER option should never get here
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.select_CIT_Statuses_query'))    
    
    logger.debug('forms_CIT_Statuses_delete(): Exit')
    return render_template('cit_statuses_delete.html', form=form, data=session.get('data'),row=row)
#===============================================================================

# ======================================================================
#  Auto-Generated code. Do not modify 
#  (C) Sertechno/Emtec Group (2018,2019)
#  GLVH @ 2020-02-20 16:44:38.223976
# ======================================================================


from pprint import pprint, pformat

# gen_views_select_query.html:AG 2020-02-20 16:44:38.223999        
@main.route('/select/CIT_Statuses_Query', methods=['GET','POST'])
@login_required
@admin_required
def select_CIT_Statuses_query():
    """ Select rows handling function for table 'CIT_Statuses' """
    logger.debug('select_CIT_Statuses_query(): Enter')
    chk_c000001(filename=os.path.join(current_app.root_path, '.c000001'),request=request,db=db,logger=logger)
    # Get parameters from URL call
    ia       =  request.args.get('ia',     None,type=str)
    if ia is not None:
        ia=ia.split(',')
        if ia[0]=='ORDER':
            set_query_option(engine=db.engine,Interface=Interface,User_Id=current_user.id,Table_name='cit_status',Option_Type=OPTION_ORDER_BY,Argument_1=ia[1],Argument_2=ia[2])
        elif ia[0]=='GROUP':
            set_query_option(engine=db.engine,Interface=Interface,User_Id=current_user.id,Table_name='cit_status',Option_Type=OPTION_GROUP_BY,Argument_1=ia[1])
        elif ia[0]=='LIMIT':
            set_query_option(engine=db.engine,Interface=Interface,User_Id=current_user.id,Table_name='cit_status',Option_Type=OPTION_LIMIT,Argument_1=ia[1])

    iad      =  request.args.get('iad',     None,type=int)
    if iad is not None: delete_query_option(engine=db.engine,Interface=Interface,Id=iad) 
    
    field    =  request.args.get('field',   None,type=str)
    value    =  request.args.get('value',   None,type=str)
    
    # Populates a list of foreign keys used for advanced filtering
    # ------------------------------------------------------------------
    foreign_keys={}
    
    # ------------------------------------------------------------------
    
    if field is not None:
        reset_query_options(    engine=db.engine,Interface=Interface,
                                User_Id=current_user.id,
                                Table_name='cit_status'
                                )

        
        if field in foreign_keys.keys():
            Class,referenced_classname,referenced_Field,referenced_Value,column_Header=foreign_keys[field]
            foreign_field='%s.%s:%s'%(referenced_classname,referenced_Value,column_Header)
            foreign_record=Class.query.get(value)
            foreign_description="'%s'"%getattr(foreign_record,referenced_Value)
        set_query_option(   engine=db.engine,Interface=Interface,
                        User_Id=current_user.id,
                        Table_name='cit_status',
                        Option_Type=OPTION_FILTER,
                        Argument_1=foreign_field,
                        Argument_2='==',
                        Argument_3=foreign_description
                        )
    page     =  request.args.get('page',    1   ,type=int)
    addx     =  request.args.get('add.x',   None,type=int)
    addy     =  request.args.get('add.y',   None,type=int)
    exportx  =  request.args.get('export.x',None,type=int)
    exporty  =  request.args.get('export.y',None,type=int)
    filterx  =  request.args.get('filter.x',None,type=int)
    filtery  =  request.args.get('filter.y',None,type=int)
    # Select excluyent view mode
    if   addx    is not None: mode = 'add'
    elif exportx is not None: mode = 'export'
    elif filterx is not None: mode = 'filter'
    else:                     mode = 'select'
    CIT_Status =  request.args.get('CIT_Status',None,type=str)
    Value =  request.args.get('Value',None,type=str)
    
    
    # Build default query all fields from table
    
    if CIT_Status is not None and len(CIT_Status)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='cit_status',
                Option_Type=OPTION_FILTER,
                Argument_1='CIT_Status:CIT Status',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%CIT_Status
                )
    
    
    if Value is not None and len(Value)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='cit_status',
                Option_Type=OPTION_FILTER,
                Argument_1='Value:Vallue',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Value
                )
    
    
    
    statement_query,options=get_query_options(engine=db.engine,Interface=Interface,Table_name='cit_status',User_Id=current_user.id)
    query=eval(statement_query)
    filtered_query = query    
    if mode == 'filter':
        query=filtered_query
    elif mode == 'export':
        query=filtered_query
        fh,output_file = tempfile.mkstemp(suffix='', prefix='CIT_Statuses_', dir=None, text=False)
        dict = {'header':{},'detail':[]}
        count = 0
        rows = query.all()
        for row in rows:
            dict['detail'].append({})
            for column in ['CIT_Status', 'Value']:
                dict['detail'][count].update( { column:str(row.__getattribute__(column))})
                
            count += 1
        dict['header'].update({'count':count})
        jsonarray      = json.dumps(dict)
        data           = json.loads(jsonarray)  
        dataframe      = json_normalize(data, 'detail').assign(**data['header'])
        fh,output_file = tempfile.mkstemp(suffix='', prefix='CIT_Statuses_', dir='/tmp', text=False)
        xlsx_file      = '%s/%s'%(current_app.root_path,url_for('static',filename='%s.xls'%(output_file)))
        dataframe.to_excel(xlsx_file,sheet_name='CIT_Statuses',columns=['CIT_Status', 'Value'])
        return send_file(xlsx_file,as_attachment=True,attachment_filename=output_file.replace('/','_')+'.xls')
    elif mode == 'add':
        return redirect(url_for('.forms_CIT_Statuses'))
    elif mode == 'select':
        pass
        # if some filter is required
        if field is not None:
            if field == 'CIT_Status':
                if value is not None:
                    query = query.filter_by(CIT_Status=value)
            if field == 'Value':
                if value is not None:
                    query = query.filter_by(Value=value)
            
    # Actual request from DB follows
    tracebox_log(query,logger,length=50)
    rows = query.paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
    # Setting pagination variables ...
    if field is not None:
       next_url = url_for('.select_CIT_Statuses_query', field=field, value=value, page=rows.next_num) if rows.has_next else None
       prev_url = url_for('.select_CIT_Statuses_query', field=field, value=value, page=rows.prev_num) if rows.has_prev else None
    else:
       next_url = url_for('.select_CIT_Statuses_query', page=rows.next_num) if rows.has_next else None
       prev_url = url_for('.select_CIT_Statuses_query', page=rows.prev_num) if rows.has_prev else None
    # Actual rendering ...
    if request.headers.get('Content-Type') is not None or request.args.get('JSON',None,type=str) is not None:
        if "JSON" in request.headers.get('Content-Type') or request.args.get('JSON',None,type=str) is not None:
            logger.debug('select_CIT_Statuses_query(): will render: JSON rows')
            logger.debug('select_CIT_Statuses_query(): Exit')
            return json.dumps(serialize_object(rows.__dict__))
    logger.debug('select_CIT_Statuses_query(): will render: cit_statuses_All.html')
    logger.debug('select_CIT_Statuses_query(): Exit')
    return render_template('cit_statuses_select_All.html',rows=rows,options=options)
#===============================================================================
   # NOTE: HARDCODE. TO REMOVE --------------------------------------------
def chk_c000001(*args,**kwargs):
    pass
    
from emtec.common.interface import *
from emtec.collector.db.orm_model          import Interface
from emtec.collector.db.flask_models       import interface
#-----------------------------------------------------------------------
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2020-02-20 16:44:35
# =============================================================================

# ======================================================================
#  Auto-Generated code. Do not modify 
#  (C) Sertechno/Emtec Group (2018,2019)
#  GLVH @ 2020-02-20 16:44:40.810093
# ======================================================================
        
# gen_views_form.html:AG 2020-02-20 16:44:40.810117
@main.route('/forms/Configuration_Items', methods=['GET', 'POST'])
@login_required

def forms_Configuration_Items():
    """ Form handling function for table Configuration_Items """
    logger.debug('forms_Configuration_Items(): Enter')
    CI_Id  =  request.args.get('CI_Id',0,type=int)
    
    row =  configuration_item.query.filter(configuration_item.CI_Id == CI_Id).first()
    if row is None:
        row=configuration_item()
        session['is_new_row']=True
    session['data'] =  {  'CI_Id':row.CI_Id, 'CI_Name':row.CI_Name, 'CI_UUID':row.CI_UUID, 'Pla_Id':row.Pla_Id, 'CC_Id':row.CC_Id, 'Cus_Id':row.Cus_Id, 'CI_Commissioning_DateTime':row.CI_Commissioning_DateTime, 'CI_Decommissioning_DateTime':row.CI_Decommissioning_DateTime }
    
    form = frm_configuration_item()
    
    if form.has_FKs:
        form.Pla_Id.choices = db.session.query(platform.Pla_Id,platform.Pla_Name).order_by(platform.Pla_Name).all()
        form.CC_Id.choices = db.session.query(cost_center.CC_Id,cost_center.CC_Description).order_by(cost_center.CC_Description).all()
        form.Cus_Id.choices = db.session.query(customer.Cus_Id,customer.Cus_Name).order_by(customer.Cus_Name).all()

    
    # Actual Form activation here
    if form.validate_on_submit():
    # Code for SAVE option
        if form.submit_Save.data and current_user.role_id > 1:
    
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
                   message=Markup('<b>Configuration Item CI_Id saved OK</b>')
                   flash(message)
               db.session.close()
            except Exception as e:
               db.session.rollback()
               db.session.close()
               message=Markup('ERROR saving Configuration Item record : %s'%(e))
               flash(message)
            return redirect(url_for('.select_Configuration_Items_query'))    
    # Code for NEW option
    # GV 20190109 f.write(        "        elif   form.submit_New.data:\n")
        elif   form.submit_New.data and current_user.role_id>1:
            #print('New Data Here ...')
            session['is_new_row']=True
            db.session.close()
            row=configuration_item()
    
            return redirect(url_for('.forms_Configuration_Items',CI_Id=row.CI_Id))
    
    # Code for CANCEL option 
        elif   form.submit_Cancel.data:
            #print('Cancel Data Here ... does nothing')
            message=Markup('Configuration Item Record modifications discarded ...')
            flash(message)
    # Code for ANY OTHER option should never get here
        else:
            #print('form validated but not submited ???')
            message=Markup("<b>Configuration Item data modifications not allowed for user '%s'. Please contact EG Suite's Administrator ...</b>"%(current_user.username))    
            flash(message)
    
            return redirect(url_for('.forms_Configuration_Items',CI_Id=row.CI_Id))
    
    
    form.CI_Name.data = row.CI_Name
    form.CI_UUID.data = row.CI_UUID
    form.Pla_Id.data = row.Pla_Id
    form.CC_Id.data = row.CC_Id
    form.Cus_Id.data = row.Cus_Id
    form.CI_Commissioning_DateTime.data = row.CI_Commissioning_DateTime
    form.CI_Decommissioning_DateTime.data = row.CI_Decommissioning_DateTime
    session['prev_row'] = str(row)
    session['is_new_row'] = False
    logger.debug('forms_Configuration_Items(): Exit')
    # Generates pagination data here
    P=[]
    # Tab Relations = [{'name': 'charge_units', 'class': 'charge_unit', 'backref': 'configuration_item', 'caption': 'Charge Units', 'table': 'Charge_Units'}, {'name': 'rates', 'class': 'rate', 'backref': 'configuration_item', 'caption': 'Rates', 'table': 'Rates'}]
    
    from flask_sqlalchemy import Pagination
    # [{'name': 'charge_units', 'class': 'charge_unit', 'backref': 'configuration_item', 'caption': 'Charge Units', 'table': 'Charge_Units'}, {'name': 'rates', 'class': 'rate', 'backref': 'configuration_item', 'caption': 'Rates', 'table': 'Rates'}]
    P.append(({'name': 'charge_units', 'class': 'charge_unit', 'backref': 'configuration_item', 'caption': 'Charge Units', 'table': 'Charge_Units'},row.charge_units.paginate()))
    P.append(({'name': 'rates', 'class': 'rate', 'backref': 'configuration_item', 'caption': 'Rates', 'table': 'Rates'},row.rates.paginate()))
    
    """
    print("P=",P,type(P))
    for relation,p in P:
        print("relation=",relation)
        print("p.query=",p.query)
        print("p.has_next=",p.has_next,p.next,p.next_num)
        print("p.has_prev=",p.has_prev,p.prev,p.prev_num)
        print("p.pages=",p.pages)
        print("p.iter_pages=",p.iter_pages)
        print("p.per_page=",p.per_page)
        print("p.total=",p.total)
        print("p.items type=",type(p.items),len(p.items))
    """
    
    # Generation of pagination data completed       
    return render_template('configuration_items.html', form=form, row=row, P=P)    
# ======================================================================



# ======================================================================
#  Auto-Generated code. Do not modify 
#  (C) Sertechno/Emtec Group (2018,2019)
#  GLVH @ 2020-02-20 16:44:40.834599
# ======================================================================
        
# gen_views_delete.html:AG 2020-02-20 16:44:40.834622
@main.route('/forms/Configuration_Items_delete', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@admin_required
def forms_Configuration_Items_delete():
    """ Delete record handling function for table Configuration_Items """
    logger.debug('forms_Configuration_Items_delete(): Enter')
    CI_Id  =  request.args.get('CI_Id',0,type=int)
    row =  configuration_item.query.filter(configuration_item.CI_Id == CI_Id).first()

    if row is None:
        row=configuration_item()
    session['data'] =  {  'CI_Id':row.CI_Id, 'CI_Name':row.CI_Name, 'CI_UUID':row.CI_UUID, 'Pla_Id':row.Pla_Id, 'CC_Id':row.CC_Id, 'Cus_Id':row.Cus_Id, 'CI_Commissioning_DateTime':row.CI_Commissioning_DateTime, 'CI_Decommissioning_DateTime':row.CI_Decommissioning_DateTime }
                       
    form = frm_configuration_item_delete()

    # Tab['has_fks'] True
    
    pass # Tab['has_fks'] True
    
            
    # Actual Form activation here
    if form.validate_on_submit():
    
    # Code for SAVE option
        if  form.submit_Delete.data:
            print('Delete Data Here...')

    
    #f.write(        "            print('Delete Data Here...')
            try:
                session['deleted_row']=str(row)
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                logger.audit ( '%s:DEL:%s' % (current_user.username,session['deleted_row']) )
                flash('Configuration Item CI_Id deleted OK')
            except exc.IntegrityError as e:
                db.session.rollback()    
                flash('INTEGRITY ERROR: Are you sure there are no dependant records in other tables?')
                return redirect(url_for('.forms_Configuration_Items_delete',CI_Id=session['data']['CI_Id']))    
    
            return redirect(url_for('.select_Configuration_Items_query'))    
    # Code for CANCEL option 
        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
            return redirect(url_for('.select_Configuration_Items_query'))    
    # Code for ANY OTHER option should never get here
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.select_Configuration_Items_query'))    
    
    logger.debug('forms_Configuration_Items_delete(): Exit')
    return render_template('configuration_items_delete.html', form=form, data=session.get('data'),row=row)
#===============================================================================

# ======================================================================
#  Auto-Generated code. Do not modify 
#  (C) Sertechno/Emtec Group (2018,2019)
#  GLVH @ 2020-02-20 16:44:40.908699
# ======================================================================


from pprint import pprint, pformat

# gen_views_select_query.html:AG 2020-02-20 16:44:40.908722        
@main.route('/select/Configuration_Items_Query', methods=['GET','POST'])
@login_required
@admin_required
def select_Configuration_Items_query():
    """ Select rows handling function for table 'Configuration_Items' """
    logger.debug('select_Configuration_Items_query(): Enter')
    chk_c000001(filename=os.path.join(current_app.root_path, '.c000001'),request=request,db=db,logger=logger)
    # Get parameters from URL call
    ia       =  request.args.get('ia',     None,type=str)
    if ia is not None:
        ia=ia.split(',')
        if ia[0]=='ORDER':
            set_query_option(engine=db.engine,Interface=Interface,User_Id=current_user.id,Table_name='configuration_item',Option_Type=OPTION_ORDER_BY,Argument_1=ia[1],Argument_2=ia[2])
        elif ia[0]=='GROUP':
            set_query_option(engine=db.engine,Interface=Interface,User_Id=current_user.id,Table_name='configuration_item',Option_Type=OPTION_GROUP_BY,Argument_1=ia[1])
        elif ia[0]=='LIMIT':
            set_query_option(engine=db.engine,Interface=Interface,User_Id=current_user.id,Table_name='configuration_item',Option_Type=OPTION_LIMIT,Argument_1=ia[1])

    iad      =  request.args.get('iad',     None,type=int)
    if iad is not None: delete_query_option(engine=db.engine,Interface=Interface,Id=iad) 
    
    field    =  request.args.get('field',   None,type=str)
    value    =  request.args.get('value',   None,type=str)
    
    # Populates a list of foreign keys used for advanced filtering
    # ------------------------------------------------------------------
    foreign_keys={}
    
    foreign_keys.update({'Pla_Id':(platform,'platform','Pla_Id','Pla_Name','Platform Id')})
    foreign_keys.update({'CC_Id':(cost_center,'cost_center','CC_Id','CC_Description','Cost Center Id')})
    foreign_keys.update({'Cus_Id':(customer,'customer','Cus_Id','Cus_Name','Customer Id')})
    # ------------------------------------------------------------------
    
    if field is not None:
        reset_query_options(    engine=db.engine,Interface=Interface,
                                User_Id=current_user.id,
                                Table_name='configuration_item'
                                )

        
        if field in foreign_keys.keys():
            Class,referenced_classname,referenced_Field,referenced_Value,column_Header=foreign_keys[field]
            foreign_field='%s.%s:%s'%(referenced_classname,referenced_Value,column_Header)
            foreign_record=Class.query.get(value)
            foreign_description="'%s'"%getattr(foreign_record,referenced_Value)
        set_query_option(   engine=db.engine,Interface=Interface,
                        User_Id=current_user.id,
                        Table_name='configuration_item',
                        Option_Type=OPTION_FILTER,
                        Argument_1=foreign_field,
                        Argument_2='==',
                        Argument_3=foreign_description
                        )
    page     =  request.args.get('page',    1   ,type=int)
    addx     =  request.args.get('add.x',   None,type=int)
    addy     =  request.args.get('add.y',   None,type=int)
    exportx  =  request.args.get('export.x',None,type=int)
    exporty  =  request.args.get('export.y',None,type=int)
    filterx  =  request.args.get('filter.x',None,type=int)
    filtery  =  request.args.get('filter.y',None,type=int)
    # Select excluyent view mode
    if   addx    is not None: mode = 'add'
    elif exportx is not None: mode = 'export'
    elif filterx is not None: mode = 'filter'
    else:                     mode = 'select'
    CI_Id =  request.args.get('CI_Id',None,type=str)
    CI_Name =  request.args.get('CI_Name',None,type=str)
    CI_UUID =  request.args.get('CI_UUID',None,type=str)
    Pla_Id =  request.args.get('Pla_Id',None,type=str)
    CC_Id =  request.args.get('CC_Id',None,type=str)
    Cus_Id =  request.args.get('Cus_Id',None,type=str)
    CI_Commissioning_DateTime =  request.args.get('CI_Commissioning_DateTime',None,type=str)
    CI_Decommissioning_DateTime =  request.args.get('CI_Decommissioning_DateTime',None,type=str)
    
    
    # Build default query all fields from table
    
    if CI_Id is not None and len(CI_Id)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='configuration_item',
                Option_Type=OPTION_FILTER,
                Argument_1='CI_Id:Id',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%CI_Id
                )
    
    
    if CI_Name is not None and len(CI_Name)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='configuration_item',
                Option_Type=OPTION_FILTER,
                Argument_1='CI_Name:Name',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%CI_Name
                )
    
    
    if CI_UUID is not None and len(CI_UUID)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='configuration_item',
                Option_Type=OPTION_FILTER,
                Argument_1='CI_UUID:UUID',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%CI_UUID
                )
    
    
    if Pla_Id is not None and len(Pla_Id)>0:
            Class,referenced_classname,referenced_Field,referenced_Value,column_Header=foreign_keys['Pla_Id']
            foreign_field='%s.%s:%s'%(referenced_classname,referenced_Value,column_Header)            
            set_query_option(   engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='configuration_item',
                Option_Type=OPTION_FILTER,
                Argument_1=foreign_field,
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Pla_Id
                )
                                
    
    
    if CC_Id is not None and len(CC_Id)>0:
            Class,referenced_classname,referenced_Field,referenced_Value,column_Header=foreign_keys['CC_Id']
            foreign_field='%s.%s:%s'%(referenced_classname,referenced_Value,column_Header)            
            set_query_option(   engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='configuration_item',
                Option_Type=OPTION_FILTER,
                Argument_1=foreign_field,
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%CC_Id
                )
                                
    
    
    if Cus_Id is not None and len(Cus_Id)>0:
            Class,referenced_classname,referenced_Field,referenced_Value,column_Header=foreign_keys['Cus_Id']
            foreign_field='%s.%s:%s'%(referenced_classname,referenced_Value,column_Header)            
            set_query_option(   engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='configuration_item',
                Option_Type=OPTION_FILTER,
                Argument_1=foreign_field,
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Cus_Id
                )
                                
    
    
    if CI_Commissioning_DateTime is not None and len(CI_Commissioning_DateTime)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='configuration_item',
                Option_Type=OPTION_FILTER,
                Argument_1='CI_Commissioning_DateTime:Commissioning Date and Time',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%CI_Commissioning_DateTime
                )
    
    
    if CI_Decommissioning_DateTime is not None and len(CI_Decommissioning_DateTime)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='configuration_item',
                Option_Type=OPTION_FILTER,
                Argument_1='CI_Decommissioning_DateTime:Decommissioning Date and Time',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%CI_Decommissioning_DateTime
                )
    
    
    
    statement_query,options=get_query_options(engine=db.engine,Interface=Interface,Table_name='configuration_item',User_Id=current_user.id)
    query=eval(statement_query)
    filtered_query = query    
    if mode == 'filter':
        query=filtered_query
    elif mode == 'export':
        query=filtered_query
        fh,output_file = tempfile.mkstemp(suffix='', prefix='Configuration_Items_', dir=None, text=False)
        dict = {'header':{},'detail':[]}
        count = 0
        rows = query.all()
        for row in rows:
            dict['detail'].append({})
            for column in ['CI_Id', 'CI_Name', 'CI_UUID', 'Pla_Id', 'CC_Id', 'Cus_Id', 'CI_Commissioning_DateTime', 'CI_Decommissioning_DateTime']:
                dict['detail'][count].update( { column:str(row.__getattribute__(column))})
                
            count += 1
        dict['header'].update({'count':count})
        jsonarray      = json.dumps(dict)
        data           = json.loads(jsonarray)  
        dataframe      = json_normalize(data, 'detail').assign(**data['header'])
        fh,output_file = tempfile.mkstemp(suffix='', prefix='Configuration_Items_', dir='/tmp', text=False)
        xlsx_file      = '%s/%s'%(current_app.root_path,url_for('static',filename='%s.xls'%(output_file)))
        dataframe.to_excel(xlsx_file,sheet_name='Configuration_Items',columns=['CI_Id', 'CI_Name', 'CI_UUID', 'Pla_Id', 'CC_Id', 'Cus_Id', 'CI_Commissioning_DateTime', 'CI_Decommissioning_DateTime'])
        return send_file(xlsx_file,as_attachment=True,attachment_filename=output_file.replace('/','_')+'.xls')
    elif mode == 'add':
        return redirect(url_for('.forms_Configuration_Items'))
    elif mode == 'select':
        pass
        # if some filter is required
        if field is not None:
            if field == 'CI_Id':
                if value is not None:
                    query = query.filter_by(CI_Id=value)
            if field == 'CI_Name':
                if value is not None:
                    query = query.filter_by(CI_Name=value)
            if field == 'CI_UUID':
                if value is not None:
                    query = query.filter_by(CI_UUID=value)
            if field == 'Pla_Id':
                if value is not None:
                    query = query.filter_by(Pla_Id=value)
            if field == 'CC_Id':
                if value is not None:
                    query = query.filter_by(CC_Id=value)
            if field == 'Cus_Id':
                if value is not None:
                    query = query.filter_by(Cus_Id=value)
            if field == 'CI_Commissioning_DateTime':
                if value is not None:
                    query = query.filter_by(CI_Commissioning_DateTime=value)
            if field == 'CI_Decommissioning_DateTime':
                if value is not None:
                    query = query.filter_by(CI_Decommissioning_DateTime=value)
            # JOIN other tables and generate foreign fields
    query = query.join(platform,configuration_item.Pla_Id == platform.Pla_Id).add_columns(platform.Pla_Name).join(cost_center,configuration_item.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description).join(customer,configuration_item.Cus_Id == customer.Cus_Id).add_columns(customer.Cus_Name)
    
    # Actual request from DB follows
    tracebox_log(query,logger,length=50)
    rows = query.paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
    # Setting pagination variables ...
    if field is not None:
       next_url = url_for('.select_Configuration_Items_query', field=field, value=value, page=rows.next_num) if rows.has_next else None
       prev_url = url_for('.select_Configuration_Items_query', field=field, value=value, page=rows.prev_num) if rows.has_prev else None
    else:
       next_url = url_for('.select_Configuration_Items_query', page=rows.next_num) if rows.has_next else None
       prev_url = url_for('.select_Configuration_Items_query', page=rows.prev_num) if rows.has_prev else None
    # Actual rendering ...
    if request.headers.get('Content-Type') is not None or request.args.get('JSON',None,type=str) is not None:
        if "JSON" in request.headers.get('Content-Type') or request.args.get('JSON',None,type=str) is not None:
            logger.debug('select_Configuration_Items_query(): will render: JSON rows')
            logger.debug('select_Configuration_Items_query(): Exit')
            return json.dumps(serialize_object(rows.__dict__))
    logger.debug('select_Configuration_Items_query(): will render: configuration_items_All.html')
    logger.debug('select_Configuration_Items_query(): Exit')
    return render_template('configuration_items_select_All.html',rows=rows,options=options)
#===============================================================================
   # NOTE: HARDCODE. TO REMOVE --------------------------------------------
def chk_c000001(*args,**kwargs):
    pass
    
from emtec.common.interface import *
from emtec.collector.db.orm_model          import Interface
from emtec.collector.db.flask_models       import interface
#-----------------------------------------------------------------------
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2020-02-20 16:44:35
# =============================================================================

# ======================================================================
#  Auto-Generated code. Do not modify 
#  (C) Sertechno/Emtec Group (2018,2019)
#  GLVH @ 2020-02-20 16:44:41.200165
# ======================================================================
        
# gen_views_form.html:AG 2020-02-20 16:44:41.200188
@main.route('/forms/Cost_Centers', methods=['GET', 'POST'])
@login_required

def forms_Cost_Centers():
    """ Form handling function for table Cost_Centers """
    logger.debug('forms_Cost_Centers(): Enter')
    CC_Id  =  request.args.get('CC_Id',0,type=int)
    
    row =  cost_center.query.filter(cost_center.CC_Id == CC_Id).first()
    if row is None:
        row=cost_center()
        session['is_new_row']=True
    session['data'] =  {  'CC_Id':row.CC_Id, 'CC_Code':row.CC_Code, 'CC_Description':row.CC_Description, 'Cur_Code':row.Cur_Code, 'CC_Parent_Code':row.CC_Parent_Code, 'CC_Reg_Exp':row.CC_Reg_Exp, 'CC_Reference':row.CC_Reference }
    
    form = frm_cost_center()
    
    if form.has_FKs:
        form.Cur_Code.choices = db.session.query(currency.Cur_Code,currency.Cur_Name).order_by(currency.Cur_Name).all()

    
    # Actual Form activation here
    if form.validate_on_submit():
    # Code for SAVE option
        if form.submit_Save.data and current_user.role_id > 1:
    
            row.CC_Code = form.CC_Code.data
            row.CC_Description = form.CC_Description.data
            row.Cur_Code = form.Cur_Code.data
            row.CC_Parent_Code = form.CC_Parent_Code.data
            row.CC_Reg_Exp = form.CC_Reg_Exp.data
            row.CC_Reference = form.CC_Reference.data  
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
                   message=Markup('<b>Cost Center CC_Id saved OK</b>')
                   flash(message)
               db.session.close()
            except Exception as e:
               db.session.rollback()
               db.session.close()
               message=Markup('ERROR saving Cost Center record : %s'%(e))
               flash(message)
            return redirect(url_for('.select_Cost_Centers_query'))    
    # Code for NEW option
    # GV 20190109 f.write(        "        elif   form.submit_New.data:\n")
        elif   form.submit_New.data and current_user.role_id>1:
            #print('New Data Here ...')
            session['is_new_row']=True
            db.session.close()
            row=cost_center()
    
            return redirect(url_for('.forms_Cost_Centers',CC_Id=row.CC_Id))
    
    # Code for CANCEL option 
        elif   form.submit_Cancel.data:
            #print('Cancel Data Here ... does nothing')
            message=Markup('Cost Center Record modifications discarded ...')
            flash(message)
    # Code for ANY OTHER option should never get here
        else:
            #print('form validated but not submited ???')
            message=Markup("<b>Cost Center data modifications not allowed for user '%s'. Please contact EG Suite's Administrator ...</b>"%(current_user.username))    
            flash(message)
    
            return redirect(url_for('.forms_Cost_Centers',CC_Id=row.CC_Id))
    
    
    form.CC_Code.data = row.CC_Code
    form.CC_Description.data = row.CC_Description
    form.Cur_Code.data = row.Cur_Code
    form.CC_Parent_Code.data = row.CC_Parent_Code
    form.CC_Reg_Exp.data = row.CC_Reg_Exp
    form.CC_Reference.data = row.CC_Reference
    session['prev_row'] = str(row)
    session['is_new_row'] = False
    logger.debug('forms_Cost_Centers(): Exit')
    # Generates pagination data here
    P=[]
    # Tab Relations = [{'name': 'configuration_items', 'class': 'configuration_item', 'backref': 'cost_center', 'caption': 'Configuration Items', 'table': 'Configuration_Items'}, {'name': 'customers', 'class': 'customer', 'backref': 'cost_center', 'caption': 'Customers', 'table': 'Customers'}, {'name': 'rates', 'class': 'rate', 'backref': 'cost_center', 'caption': 'Rates', 'table': 'Rates'}, {'name': 'users', 'class': 'User', 'backref': 'cost_center', 'caption': 'Users', 'table': 'Users'}]
    
    from flask_sqlalchemy import Pagination
    # [{'name': 'configuration_items', 'class': 'configuration_item', 'backref': 'cost_center', 'caption': 'Configuration Items', 'table': 'Configuration_Items'}, {'name': 'customers', 'class': 'customer', 'backref': 'cost_center', 'caption': 'Customers', 'table': 'Customers'}, {'name': 'rates', 'class': 'rate', 'backref': 'cost_center', 'caption': 'Rates', 'table': 'Rates'}, {'name': 'users', 'class': 'User', 'backref': 'cost_center', 'caption': 'Users', 'table': 'Users'}]
    P.append(({'name': 'configuration_items', 'class': 'configuration_item', 'backref': 'cost_center', 'caption': 'Configuration Items', 'table': 'Configuration_Items'},row.configuration_items.paginate()))
    P.append(({'name': 'customers', 'class': 'customer', 'backref': 'cost_center', 'caption': 'Customers', 'table': 'Customers'},row.customers.paginate()))
    P.append(({'name': 'rates', 'class': 'rate', 'backref': 'cost_center', 'caption': 'Rates', 'table': 'Rates'},row.rates.paginate()))
    P.append(({'name': 'users', 'class': 'User', 'backref': 'cost_center', 'caption': 'Users', 'table': 'Users'},row.users.paginate()))
    
    """
    print("P=",P,type(P))
    for relation,p in P:
        print("relation=",relation)
        print("p.query=",p.query)
        print("p.has_next=",p.has_next,p.next,p.next_num)
        print("p.has_prev=",p.has_prev,p.prev,p.prev_num)
        print("p.pages=",p.pages)
        print("p.iter_pages=",p.iter_pages)
        print("p.per_page=",p.per_page)
        print("p.total=",p.total)
        print("p.items type=",type(p.items),len(p.items))
    """
    
    # Generation of pagination data completed       
    return render_template('cost_centers.html', form=form, row=row, P=P)    
# ======================================================================



# ======================================================================
#  Auto-Generated code. Do not modify 
#  (C) Sertechno/Emtec Group (2018,2019)
#  GLVH @ 2020-02-20 16:44:41.223092
# ======================================================================
        
# gen_views_delete.html:AG 2020-02-20 16:44:41.223114
@main.route('/forms/Cost_Centers_delete', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@admin_required
def forms_Cost_Centers_delete():
    """ Delete record handling function for table Cost_Centers """
    logger.debug('forms_Cost_Centers_delete(): Enter')
    CC_Id  =  request.args.get('CC_Id',0,type=int)
    row =  cost_center.query.filter(cost_center.CC_Id == CC_Id).first()

    if row is None:
        row=cost_center()
    session['data'] =  {  'CC_Id':row.CC_Id, 'CC_Code':row.CC_Code, 'CC_Description':row.CC_Description, 'Cur_Code':row.Cur_Code, 'CC_Parent_Code':row.CC_Parent_Code, 'CC_Reg_Exp':row.CC_Reg_Exp, 'CC_Reference':row.CC_Reference }
                       
    form = frm_cost_center_delete()

    # Tab['has_fks'] True
    
    pass # Tab['has_fks'] True
    
            
    # Actual Form activation here
    if form.validate_on_submit():
    
    # Code for SAVE option
        if  form.submit_Delete.data:
            print('Delete Data Here...')

    
    #f.write(        "            print('Delete Data Here...')
            try:
                session['deleted_row']=str(row)
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                logger.audit ( '%s:DEL:%s' % (current_user.username,session['deleted_row']) )
                flash('Cost Center CC_Id deleted OK')
            except exc.IntegrityError as e:
                db.session.rollback()    
                flash('INTEGRITY ERROR: Are you sure there are no dependant records in other tables?')
                return redirect(url_for('.forms_Cost_Centers_delete',CC_Id=session['data']['CC_Id']))    
    
            return redirect(url_for('.select_Cost_Centers_query'))    
    # Code for CANCEL option 
        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
            return redirect(url_for('.select_Cost_Centers_query'))    
    # Code for ANY OTHER option should never get here
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.select_Cost_Centers_query'))    
    
    logger.debug('forms_Cost_Centers_delete(): Exit')
    return render_template('cost_centers_delete.html', form=form, data=session.get('data'),row=row)
#===============================================================================

# ======================================================================
#  Auto-Generated code. Do not modify 
#  (C) Sertechno/Emtec Group (2018,2019)
#  GLVH @ 2020-02-20 16:44:41.269509
# ======================================================================


from pprint import pprint, pformat

# gen_views_select_query.html:AG 2020-02-20 16:44:41.269531        
@main.route('/select/Cost_Centers_Query', methods=['GET','POST'])
@login_required
@admin_required
def select_Cost_Centers_query():
    """ Select rows handling function for table 'Cost_Centers' """
    logger.debug('select_Cost_Centers_query(): Enter')
    chk_c000001(filename=os.path.join(current_app.root_path, '.c000001'),request=request,db=db,logger=logger)
    # Get parameters from URL call
    ia       =  request.args.get('ia',     None,type=str)
    if ia is not None:
        ia=ia.split(',')
        if ia[0]=='ORDER':
            set_query_option(engine=db.engine,Interface=Interface,User_Id=current_user.id,Table_name='cost_center',Option_Type=OPTION_ORDER_BY,Argument_1=ia[1],Argument_2=ia[2])
        elif ia[0]=='GROUP':
            set_query_option(engine=db.engine,Interface=Interface,User_Id=current_user.id,Table_name='cost_center',Option_Type=OPTION_GROUP_BY,Argument_1=ia[1])
        elif ia[0]=='LIMIT':
            set_query_option(engine=db.engine,Interface=Interface,User_Id=current_user.id,Table_name='cost_center',Option_Type=OPTION_LIMIT,Argument_1=ia[1])

    iad      =  request.args.get('iad',     None,type=int)
    if iad is not None: delete_query_option(engine=db.engine,Interface=Interface,Id=iad) 
    
    field    =  request.args.get('field',   None,type=str)
    value    =  request.args.get('value',   None,type=str)
    
    # Populates a list of foreign keys used for advanced filtering
    # ------------------------------------------------------------------
    foreign_keys={}
    
    foreign_keys.update({'Cur_Code':(currency,'currency','Cur_Code','Cur_Name','Currency Code')})
    # ------------------------------------------------------------------
    
    if field is not None:
        reset_query_options(    engine=db.engine,Interface=Interface,
                                User_Id=current_user.id,
                                Table_name='cost_center'
                                )

        
        if field in foreign_keys.keys():
            Class,referenced_classname,referenced_Field,referenced_Value,column_Header=foreign_keys[field]
            foreign_field='%s.%s:%s'%(referenced_classname,referenced_Value,column_Header)
            foreign_record=Class.query.get(value)
            foreign_description="'%s'"%getattr(foreign_record,referenced_Value)
        set_query_option(   engine=db.engine,Interface=Interface,
                        User_Id=current_user.id,
                        Table_name='cost_center',
                        Option_Type=OPTION_FILTER,
                        Argument_1=foreign_field,
                        Argument_2='==',
                        Argument_3=foreign_description
                        )
    page     =  request.args.get('page',    1   ,type=int)
    addx     =  request.args.get('add.x',   None,type=int)
    addy     =  request.args.get('add.y',   None,type=int)
    exportx  =  request.args.get('export.x',None,type=int)
    exporty  =  request.args.get('export.y',None,type=int)
    filterx  =  request.args.get('filter.x',None,type=int)
    filtery  =  request.args.get('filter.y',None,type=int)
    # Select excluyent view mode
    if   addx    is not None: mode = 'add'
    elif exportx is not None: mode = 'export'
    elif filterx is not None: mode = 'filter'
    else:                     mode = 'select'
    CC_Id =  request.args.get('CC_Id',None,type=str)
    CC_Code =  request.args.get('CC_Code',None,type=str)
    CC_Description =  request.args.get('CC_Description',None,type=str)
    Cur_Code =  request.args.get('Cur_Code',None,type=str)
    CC_Parent_Code =  request.args.get('CC_Parent_Code',None,type=str)
    CC_Reference =  request.args.get('CC_Reference',None,type=str)
    
    
    # Build default query all fields from table
    
    if CC_Id is not None and len(CC_Id)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='cost_center',
                Option_Type=OPTION_FILTER,
                Argument_1='CC_Id:Cost Center Id',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%CC_Id
                )
    
    
    if CC_Code is not None and len(CC_Code)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='cost_center',
                Option_Type=OPTION_FILTER,
                Argument_1='CC_Code:Code',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%CC_Code
                )
    
    
    if CC_Description is not None and len(CC_Description)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='cost_center',
                Option_Type=OPTION_FILTER,
                Argument_1='CC_Description:Description',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%CC_Description
                )
    
    
    if Cur_Code is not None and len(Cur_Code)>0:
            Class,referenced_classname,referenced_Field,referenced_Value,column_Header=foreign_keys['Cur_Code']
            foreign_field='%s.%s:%s'%(referenced_classname,referenced_Value,column_Header)            
            set_query_option(   engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='cost_center',
                Option_Type=OPTION_FILTER,
                Argument_1=foreign_field,
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Cur_Code
                )
                                
    
    
    if CC_Parent_Code is not None and len(CC_Parent_Code)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='cost_center',
                Option_Type=OPTION_FILTER,
                Argument_1='CC_Parent_Code:Parent Code',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%CC_Parent_Code
                )
    
    
    
    if CC_Reference is not None and len(CC_Reference)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='cost_center',
                Option_Type=OPTION_FILTER,
                Argument_1='CC_Reference:Reference',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%CC_Reference
                )
    
    
    
    statement_query,options=get_query_options(engine=db.engine,Interface=Interface,Table_name='cost_center',User_Id=current_user.id)
    query=eval(statement_query)
    filtered_query = query    
    if mode == 'filter':
        query=filtered_query
    elif mode == 'export':
        query=filtered_query
        fh,output_file = tempfile.mkstemp(suffix='', prefix='Cost_Centers_', dir=None, text=False)
        dict = {'header':{},'detail':[]}
        count = 0
        rows = query.all()
        for row in rows:
            dict['detail'].append({})
            for column in ['CC_Id', 'CC_Code', 'CC_Description', 'Cur_Code', 'CC_Parent_Code', 'CC_Reg_Exp', 'CC_Reference']:
                dict['detail'][count].update( { column:str(row.__getattribute__(column))})
                
            count += 1
        dict['header'].update({'count':count})
        jsonarray      = json.dumps(dict)
        data           = json.loads(jsonarray)  
        dataframe      = json_normalize(data, 'detail').assign(**data['header'])
        fh,output_file = tempfile.mkstemp(suffix='', prefix='Cost_Centers_', dir='/tmp', text=False)
        xlsx_file      = '%s/%s'%(current_app.root_path,url_for('static',filename='%s.xls'%(output_file)))
        dataframe.to_excel(xlsx_file,sheet_name='Cost_Centers',columns=['CC_Id', 'CC_Code', 'CC_Description', 'Cur_Code', 'CC_Parent_Code', 'CC_Reg_Exp', 'CC_Reference'])
        return send_file(xlsx_file,as_attachment=True,attachment_filename=output_file.replace('/','_')+'.xls')
    elif mode == 'add':
        return redirect(url_for('.forms_Cost_Centers'))
    elif mode == 'select':
        pass
        # if some filter is required
        if field is not None:
            if field == 'CC_Id':
                if value is not None:
                    query = query.filter_by(CC_Id=value)
            if field == 'CC_Code':
                if value is not None:
                    query = query.filter_by(CC_Code=value)
            if field == 'CC_Description':
                if value is not None:
                    query = query.filter_by(CC_Description=value)
            if field == 'Cur_Code':
                if value is not None:
                    query = query.filter_by(Cur_Code=value)
            if field == 'CC_Parent_Code':
                if value is not None:
                    query = query.filter_by(CC_Parent_Code=value)
            if field == 'CC_Reg_Exp':
                if value is not None:
                    query = query.filter_by(CC_Reg_Exp=value)
            if field == 'CC_Reference':
                if value is not None:
                    query = query.filter_by(CC_Reference=value)
            # JOIN other tables and generate foreign fields
    query = query.join(currency,cost_center.Cur_Code == currency.Cur_Code).add_columns(currency.Cur_Name)
    
    # Actual request from DB follows
    tracebox_log(query,logger,length=50)
    rows = query.paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
    # Setting pagination variables ...
    if field is not None:
       next_url = url_for('.select_Cost_Centers_query', field=field, value=value, page=rows.next_num) if rows.has_next else None
       prev_url = url_for('.select_Cost_Centers_query', field=field, value=value, page=rows.prev_num) if rows.has_prev else None
    else:
       next_url = url_for('.select_Cost_Centers_query', page=rows.next_num) if rows.has_next else None
       prev_url = url_for('.select_Cost_Centers_query', page=rows.prev_num) if rows.has_prev else None
    # Actual rendering ...
    if request.headers.get('Content-Type') is not None or request.args.get('JSON',None,type=str) is not None:
        if "JSON" in request.headers.get('Content-Type') or request.args.get('JSON',None,type=str) is not None:
            logger.debug('select_Cost_Centers_query(): will render: JSON rows')
            logger.debug('select_Cost_Centers_query(): Exit')
            return json.dumps(serialize_object(rows.__dict__))
    logger.debug('select_Cost_Centers_query(): will render: cost_centers_All.html')
    logger.debug('select_Cost_Centers_query(): Exit')
    return render_template('cost_centers_select_All.html',rows=rows,options=options)
#===============================================================================
   # NOTE: HARDCODE. TO REMOVE --------------------------------------------
def chk_c000001(*args,**kwargs):
    pass
    
from emtec.common.interface import *
from emtec.collector.db.orm_model          import Interface
from emtec.collector.db.flask_models       import interface
#-----------------------------------------------------------------------
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2020-02-20 16:44:35
# =============================================================================

# ======================================================================
#  Auto-Generated code. Do not modify 
#  (C) Sertechno/Emtec Group (2018,2019)
#  GLVH @ 2020-02-20 16:44:41.854011
# ======================================================================
        
# gen_views_form.html:AG 2020-02-20 16:44:41.854034
@main.route('/forms/Countries_Currencies', methods=['GET', 'POST'])
@login_required

def forms_Countries_Currencies():
    """ Form handling function for table Countries_Currencies """
    logger.debug('forms_Countries_Currencies(): Enter')
    Cou_Code  =  request.args.get('Cou_Code',0,type=int)
    Cur_Code  =  request.args.get('Cur_Code',0,type=int)
    
    row =  country_currency.query.filter(country_currency.Cou_Code == Cou_Code,country_currency.Cur_Code == Cur_Code).first()
    if row is None:
        row=country_currency()
        session['is_new_row']=True
    session['data'] =  {  'Cou_Code':row.Cou_Code, 'Cur_Code':row.Cur_Code, 'Cou_Cur_Comment':row.Cou_Cur_Comment }
    
    form = frm_country_currency()
    
    if form.has_FKs:
        form.Cou_Code.choices = db.session.query(country.Cou_Code,country.Cou_Name).order_by(country.Cou_Name).all()
        form.Cur_Code.choices = db.session.query(currency.Cur_Code,currency.Cur_Name).order_by(currency.Cur_Name).all()

    
    # Actual Form activation here
    if form.validate_on_submit():
    # Code for SAVE option
        if form.submit_Save.data and current_user.role_id > 1:
    
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
                   message=Markup('<b>Country vs Currency Cou_Code,Cur_Code saved OK</b>')
                   flash(message)
               db.session.close()
            except Exception as e:
               db.session.rollback()
               db.session.close()
               message=Markup('ERROR saving Country vs Currency record : %s'%(e))
               flash(message)
            return redirect(url_for('.select_Countries_Currencies_query'))    
    # Code for NEW option
    # GV 20190109 f.write(        "        elif   form.submit_New.data:\n")
        elif   form.submit_New.data and current_user.role_id>1:
            #print('New Data Here ...')
            session['is_new_row']=True
            db.session.close()
            row=country_currency()
    
            return redirect(url_for('.forms_Countries_Currencies'))    
    
    # Code for CANCEL option 
        elif   form.submit_Cancel.data:
            #print('Cancel Data Here ... does nothing')
            message=Markup('Country vs Currency Record modifications discarded ...')
            flash(message)
    # Code for ANY OTHER option should never get here
        else:
            #print('form validated but not submited ???')
            message=Markup("<b>Country vs Currency data modifications not allowed for user '%s'. Please contact EG Suite's Administrator ...</b>"%(current_user.username))    
            flash(message)
    
            return redirect(url_for('.forms_'))    
    
    
    form.Cou_Code.data = row.Cou_Code
    form.Cur_Code.data = row.Cur_Code
    form.Cou_Cur_Comment.data = row.Cou_Cur_Comment
    session['prev_row'] = str(row)
    session['is_new_row'] = False
    logger.debug('forms_Countries_Currencies(): Exit')
    # Generates pagination data here
    P=[]
    # Tab Relations = []
    
    # Generation of pagination data completed       
    return render_template('countries_currencies.html', form=form, row=row, P=P)    
# ======================================================================



# ======================================================================
#  Auto-Generated code. Do not modify 
#  (C) Sertechno/Emtec Group (2018,2019)
#  GLVH @ 2020-02-20 16:44:41.881608
# ======================================================================
        
# gen_views_delete.html:AG 2020-02-20 16:44:41.881641
@main.route('/forms/Countries_Currencies_delete', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@admin_required
def forms_Countries_Currencies_delete():
    """ Delete record handling function for table Countries_Currencies """
    logger.debug('forms_Countries_Currencies_delete(): Enter')
    Cou_Code  =  request.args.get('Cou_Code',0,type=int)
    Cur_Code  =  request.args.get('Cur_Code',0,type=int)
    row =  country_currency.query.filter(country_currency.Cou_Code == Cou_Code,country_currency.Cur_Code == Cur_Code).first()

    if row is None:
        row=country_currency()
    session['data'] =  {  'Cou_Code':row.Cou_Code, 'Cur_Code':row.Cur_Code, 'Cou_Cur_Comment':row.Cou_Cur_Comment }
                       
    form = frm_country_currency_delete()

    # Tab['has_fks'] True
    
    pass # Tab['has_fks'] True
    
            
    # Actual Form activation here
    if form.validate_on_submit():
    
    # Code for SAVE option
        if  form.submit_Delete.data:
            print('Delete Data Here...')

    
    #f.write(        "            print('Delete Data Here...')
            try:
                session['deleted_row']=str(row)
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                logger.audit ( '%s:DEL:%s' % (current_user.username,session['deleted_row']) )
                flash('Country vs Currency Cou_Code,Cur_Code deleted OK')
            except exc.IntegrityError as e:
                db.session.rollback()    
                flash('INTEGRITY ERROR: Are you sure there are no dependant records in other tables?')
                return redirect(url_for('.forms_Countries_Currencies_delete',Cou_Code=session['data']['Cou_Code'],Cur_Code=session['data']['Cur_Code']))    
    
            return redirect(url_for('.select_Countries_Currencies_query'))    
    # Code for CANCEL option 
        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
            return redirect(url_for('.select_Countries_Currencies_query'))    
    # Code for ANY OTHER option should never get here
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.select_Countries_Currencies_query'))    
    
    logger.debug('forms_Countries_Currencies_delete(): Exit')
    return render_template('countries_currencies_delete.html', form=form, data=session.get('data'),row=row)
#===============================================================================

# ======================================================================
#  Auto-Generated code. Do not modify 
#  (C) Sertechno/Emtec Group (2018,2019)
#  GLVH @ 2020-02-20 16:44:41.935202
# ======================================================================


from pprint import pprint, pformat

# gen_views_select_query.html:AG 2020-02-20 16:44:41.935225        
@main.route('/select/Countries_Currencies_Query', methods=['GET','POST'])
@login_required
@admin_required
def select_Countries_Currencies_query():
    """ Select rows handling function for table 'Countries_Currencies' """
    logger.debug('select_Countries_Currencies_query(): Enter')
    chk_c000001(filename=os.path.join(current_app.root_path, '.c000001'),request=request,db=db,logger=logger)
    # Get parameters from URL call
    ia       =  request.args.get('ia',     None,type=str)
    if ia is not None:
        ia=ia.split(',')
        if ia[0]=='ORDER':
            set_query_option(engine=db.engine,Interface=Interface,User_Id=current_user.id,Table_name='country_currency',Option_Type=OPTION_ORDER_BY,Argument_1=ia[1],Argument_2=ia[2])
        elif ia[0]=='GROUP':
            set_query_option(engine=db.engine,Interface=Interface,User_Id=current_user.id,Table_name='country_currency',Option_Type=OPTION_GROUP_BY,Argument_1=ia[1])
        elif ia[0]=='LIMIT':
            set_query_option(engine=db.engine,Interface=Interface,User_Id=current_user.id,Table_name='country_currency',Option_Type=OPTION_LIMIT,Argument_1=ia[1])

    iad      =  request.args.get('iad',     None,type=int)
    if iad is not None: delete_query_option(engine=db.engine,Interface=Interface,Id=iad) 
    
    field    =  request.args.get('field',   None,type=str)
    value    =  request.args.get('value',   None,type=str)
    
    # Populates a list of foreign keys used for advanced filtering
    # ------------------------------------------------------------------
    foreign_keys={}
    
    foreign_keys.update({'Cou_Code':(country,'country','Cou_Code','Cou_Name','Country Code')})
    foreign_keys.update({'Cur_Code':(currency,'currency','Cur_Code','Cur_Name','Currency Code')})
    # ------------------------------------------------------------------
    
    if field is not None:
        reset_query_options(    engine=db.engine,Interface=Interface,
                                User_Id=current_user.id,
                                Table_name='country_currency'
                                )

        
        if field in foreign_keys.keys():
            Class,referenced_classname,referenced_Field,referenced_Value,column_Header=foreign_keys[field]
            foreign_field='%s.%s:%s'%(referenced_classname,referenced_Value,column_Header)
            foreign_record=Class.query.get(value)
            foreign_description="'%s'"%getattr(foreign_record,referenced_Value)
        set_query_option(   engine=db.engine,Interface=Interface,
                        User_Id=current_user.id,
                        Table_name='country_currency',
                        Option_Type=OPTION_FILTER,
                        Argument_1=foreign_field,
                        Argument_2='==',
                        Argument_3=foreign_description
                        )
    page     =  request.args.get('page',    1   ,type=int)
    addx     =  request.args.get('add.x',   None,type=int)
    addy     =  request.args.get('add.y',   None,type=int)
    exportx  =  request.args.get('export.x',None,type=int)
    exporty  =  request.args.get('export.y',None,type=int)
    filterx  =  request.args.get('filter.x',None,type=int)
    filtery  =  request.args.get('filter.y',None,type=int)
    # Select excluyent view mode
    if   addx    is not None: mode = 'add'
    elif exportx is not None: mode = 'export'
    elif filterx is not None: mode = 'filter'
    else:                     mode = 'select'
    Cou_Code =  request.args.get('Cou_Code',None,type=str)
    Cur_Code =  request.args.get('Cur_Code',None,type=str)
    Cou_Cur_Comment =  request.args.get('Cou_Cur_Comment',None,type=str)
    
    
    # Build default query all fields from table
    
    if Cou_Code is not None and len(Cou_Code)>0:
            Class,referenced_classname,referenced_Field,referenced_Value,column_Header=foreign_keys['Cou_Code']
            foreign_field='%s.%s:%s'%(referenced_classname,referenced_Value,column_Header)            
            set_query_option(   engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='country_currency',
                Option_Type=OPTION_FILTER,
                Argument_1=foreign_field,
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Cou_Code
                )
                                
    
    
    if Cur_Code is not None and len(Cur_Code)>0:
            Class,referenced_classname,referenced_Field,referenced_Value,column_Header=foreign_keys['Cur_Code']
            foreign_field='%s.%s:%s'%(referenced_classname,referenced_Value,column_Header)            
            set_query_option(   engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='country_currency',
                Option_Type=OPTION_FILTER,
                Argument_1=foreign_field,
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Cur_Code
                )
                                
    
    
    if Cou_Cur_Comment is not None and len(Cou_Cur_Comment)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='country_currency',
                Option_Type=OPTION_FILTER,
                Argument_1='Cou_Cur_Comment:Comment',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Cou_Cur_Comment
                )
    
    
    
    statement_query,options=get_query_options(engine=db.engine,Interface=Interface,Table_name='country_currency',User_Id=current_user.id)
    query=eval(statement_query)
    filtered_query = query    
    if mode == 'filter':
        query=filtered_query
    elif mode == 'export':
        query=filtered_query
        fh,output_file = tempfile.mkstemp(suffix='', prefix='Countries_Currencies_', dir=None, text=False)
        dict = {'header':{},'detail':[]}
        count = 0
        rows = query.all()
        for row in rows:
            dict['detail'].append({})
            for column in ['Cou_Code', 'Cur_Code', 'Cou_Cur_Comment']:
                dict['detail'][count].update( { column:str(row.__getattribute__(column))})
                
            count += 1
        dict['header'].update({'count':count})
        jsonarray      = json.dumps(dict)
        data           = json.loads(jsonarray)  
        dataframe      = json_normalize(data, 'detail').assign(**data['header'])
        fh,output_file = tempfile.mkstemp(suffix='', prefix='Countries_Currencies_', dir='/tmp', text=False)
        xlsx_file      = '%s/%s'%(current_app.root_path,url_for('static',filename='%s.xls'%(output_file)))
        dataframe.to_excel(xlsx_file,sheet_name='Countries_Currencies',columns=['Cou_Code', 'Cur_Code', 'Cou_Cur_Comment'])
        return send_file(xlsx_file,as_attachment=True,attachment_filename=output_file.replace('/','_')+'.xls')
    elif mode == 'add':
        return redirect(url_for('.forms_Countries_Currencies'))
    elif mode == 'select':
        pass
        # if some filter is required
        if field is not None:
            if field == 'Cou_Code':
                if value is not None:
                    query = query.filter_by(Cou_Code=value)
            if field == 'Cur_Code':
                if value is not None:
                    query = query.filter_by(Cur_Code=value)
            if field == 'Cou_Cur_Comment':
                if value is not None:
                    query = query.filter_by(Cou_Cur_Comment=value)
            # JOIN other tables and generate foreign fields
    query = query.join(country,country_currency.Cou_Code == country.Cou_Code).add_columns(country.Cou_Name).join(currency,country_currency.Cur_Code == currency.Cur_Code).add_columns(currency.Cur_Name)
    
    # Actual request from DB follows
    tracebox_log(query,logger,length=50)
    rows = query.paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
    # Setting pagination variables ...
    if field is not None:
       next_url = url_for('.select_Countries_Currencies_query', field=field, value=value, page=rows.next_num) if rows.has_next else None
       prev_url = url_for('.select_Countries_Currencies_query', field=field, value=value, page=rows.prev_num) if rows.has_prev else None
    else:
       next_url = url_for('.select_Countries_Currencies_query', page=rows.next_num) if rows.has_next else None
       prev_url = url_for('.select_Countries_Currencies_query', page=rows.prev_num) if rows.has_prev else None
    # Actual rendering ...
    if request.headers.get('Content-Type') is not None or request.args.get('JSON',None,type=str) is not None:
        if "JSON" in request.headers.get('Content-Type') or request.args.get('JSON',None,type=str) is not None:
            logger.debug('select_Countries_Currencies_query(): will render: JSON rows')
            logger.debug('select_Countries_Currencies_query(): Exit')
            return json.dumps(serialize_object(rows.__dict__))
    logger.debug('select_Countries_Currencies_query(): will render: countries_currencies_All.html')
    logger.debug('select_Countries_Currencies_query(): Exit')
    return render_template('countries_currencies_select_All.html',rows=rows,options=options)
#===============================================================================
   # NOTE: HARDCODE. TO REMOVE --------------------------------------------
def chk_c000001(*args,**kwargs):
    pass
    
from emtec.common.interface import *
from emtec.collector.db.orm_model          import Interface
from emtec.collector.db.flask_models       import interface
#-----------------------------------------------------------------------
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2020-02-20 16:44:35
# =============================================================================

# ======================================================================
#  Auto-Generated code. Do not modify 
#  (C) Sertechno/Emtec Group (2018,2019)
#  GLVH @ 2020-02-20 16:44:41.507934
# ======================================================================
        
# gen_views_form.html:AG 2020-02-20 16:44:41.507957
@main.route('/forms/Countries', methods=['GET', 'POST'])
@login_required

def forms_Countries():
    """ Form handling function for table Countries """
    logger.debug('forms_Countries(): Enter')
    Cou_Code  =  request.args.get('Cou_Code',0,type=int)
    
    row =  country.query.filter(country.Cou_Code == Cou_Code).first()
    if row is None:
        row=country()
        session['is_new_row']=True
    session['data'] =  {  'Cou_Code':row.Cou_Code, 'Cou_Name':row.Cou_Name, 'Cou_A3':row.Cou_A3, 'Cou_N':row.Cou_N }
    
    form = frm_country()
    
    # Actual Form activation here
    if form.validate_on_submit():
    # Code for SAVE option
        if form.submit_Save.data and current_user.role_id > 1:
    
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
                   message=Markup('<b>Country Cou_Code saved OK</b>')
                   flash(message)
               db.session.close()
            except Exception as e:
               db.session.rollback()
               db.session.close()
               message=Markup('ERROR saving Country record : %s'%(e))
               flash(message)
            return redirect(url_for('.select_Countries_query'))    
    # Code for NEW option
    # GV 20190109 f.write(        "        elif   form.submit_New.data:\n")
        elif   form.submit_New.data and current_user.role_id>1:
            #print('New Data Here ...')
            session['is_new_row']=True
            db.session.close()
            row=country()
    
            return redirect(url_for('.forms_Countries'))    
    
    # Code for CANCEL option 
        elif   form.submit_Cancel.data:
            #print('Cancel Data Here ... does nothing')
            message=Markup('Country Record modifications discarded ...')
            flash(message)
    # Code for ANY OTHER option should never get here
        else:
            #print('form validated but not submited ???')
            message=Markup("<b>Country data modifications not allowed for user '%s'. Please contact EG Suite's Administrator ...</b>"%(current_user.username))    
            flash(message)
    
            return redirect(url_for('.forms_'))    
    
    
    form.Cou_Code.data = row.Cou_Code
    form.Cou_Name.data = row.Cou_Name
    form.Cou_A3.data = row.Cou_A3
    form.Cou_N.data = row.Cou_N
    session['prev_row'] = str(row)
    session['is_new_row'] = False
    logger.debug('forms_Countries(): Exit')
    # Generates pagination data here
    P=[]
    # Tab Relations = [{'name': 'countries_currencies', 'class': 'country_currency', 'backref': 'country', 'caption': 'Countries vs Currencies', 'table': 'Countries_Currencies'}]
    
    from flask_sqlalchemy import Pagination
    # [{'name': 'countries_currencies', 'class': 'country_currency', 'backref': 'country', 'caption': 'Countries vs Currencies', 'table': 'Countries_Currencies'}]
    P.append(({'name': 'countries_currencies', 'class': 'country_currency', 'backref': 'country', 'caption': 'Countries vs Currencies', 'table': 'Countries_Currencies'},row.countries_currencies.paginate()))
    
    """
    print("P=",P,type(P))
    for relation,p in P:
        print("relation=",relation)
        print("p.query=",p.query)
        print("p.has_next=",p.has_next,p.next,p.next_num)
        print("p.has_prev=",p.has_prev,p.prev,p.prev_num)
        print("p.pages=",p.pages)
        print("p.iter_pages=",p.iter_pages)
        print("p.per_page=",p.per_page)
        print("p.total=",p.total)
        print("p.items type=",type(p.items),len(p.items))
    """
    
    # Generation of pagination data completed       
    return render_template('countries.html', form=form, row=row, P=P)    
# ======================================================================



# ======================================================================
#  Auto-Generated code. Do not modify 
#  (C) Sertechno/Emtec Group (2018,2019)
#  GLVH @ 2020-02-20 16:44:41.530253
# ======================================================================
        
# gen_views_delete.html:AG 2020-02-20 16:44:41.530274
@main.route('/forms/Countries_delete', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@admin_required
def forms_Countries_delete():
    """ Delete record handling function for table Countries """
    logger.debug('forms_Countries_delete(): Enter')
    Cou_Code  =  request.args.get('Cou_Code',0,type=int)
    row =  country.query.filter(country.Cou_Code == Cou_Code).first()

    if row is None:
        row=country()
    session['data'] =  {  'Cou_Code':row.Cou_Code, 'Cou_Name':row.Cou_Name, 'Cou_A3':row.Cou_A3, 'Cou_N':row.Cou_N }
                       
    form = frm_country_delete()

    # Tab['has_fks'] False
    
            
    # Actual Form activation here
    if form.validate_on_submit():
    
    # Code for SAVE option
        if  form.submit_Delete.data:
            print('Delete Data Here...')

    
    #f.write(        "            print('Delete Data Here...')
            try:
                session['deleted_row']=str(row)
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                logger.audit ( '%s:DEL:%s' % (current_user.username,session['deleted_row']) )
                flash('Country Cou_Code deleted OK')
            except exc.IntegrityError as e:
                db.session.rollback()    
                flash('INTEGRITY ERROR: Are you sure there are no dependant records in other tables?')
                return redirect(url_for('.forms_Countries_delete',Cou_Code=session['data']['Cou_Code']))    
    
            return redirect(url_for('.select_Countries_query'))    
    # Code for CANCEL option 
        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
            return redirect(url_for('.select_Countries_query'))    
    # Code for ANY OTHER option should never get here
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.select_Countries_query'))    
    
    logger.debug('forms_Countries_delete(): Exit')
    return render_template('countries_delete.html', form=form, data=session.get('data'),row=row)
#===============================================================================

# ======================================================================
#  Auto-Generated code. Do not modify 
#  (C) Sertechno/Emtec Group (2018,2019)
#  GLVH @ 2020-02-20 16:44:41.577214
# ======================================================================


from pprint import pprint, pformat

# gen_views_select_query.html:AG 2020-02-20 16:44:41.577236        
@main.route('/select/Countries_Query', methods=['GET','POST'])
@login_required
@admin_required
def select_Countries_query():
    """ Select rows handling function for table 'Countries' """
    logger.debug('select_Countries_query(): Enter')
    chk_c000001(filename=os.path.join(current_app.root_path, '.c000001'),request=request,db=db,logger=logger)
    # Get parameters from URL call
    ia       =  request.args.get('ia',     None,type=str)
    if ia is not None:
        ia=ia.split(',')
        if ia[0]=='ORDER':
            set_query_option(engine=db.engine,Interface=Interface,User_Id=current_user.id,Table_name='country',Option_Type=OPTION_ORDER_BY,Argument_1=ia[1],Argument_2=ia[2])
        elif ia[0]=='GROUP':
            set_query_option(engine=db.engine,Interface=Interface,User_Id=current_user.id,Table_name='country',Option_Type=OPTION_GROUP_BY,Argument_1=ia[1])
        elif ia[0]=='LIMIT':
            set_query_option(engine=db.engine,Interface=Interface,User_Id=current_user.id,Table_name='country',Option_Type=OPTION_LIMIT,Argument_1=ia[1])

    iad      =  request.args.get('iad',     None,type=int)
    if iad is not None: delete_query_option(engine=db.engine,Interface=Interface,Id=iad) 
    
    field    =  request.args.get('field',   None,type=str)
    value    =  request.args.get('value',   None,type=str)
    
    # Populates a list of foreign keys used for advanced filtering
    # ------------------------------------------------------------------
    foreign_keys={}
    
    # ------------------------------------------------------------------
    
    if field is not None:
        reset_query_options(    engine=db.engine,Interface=Interface,
                                User_Id=current_user.id,
                                Table_name='country'
                                )

        
        if field in foreign_keys.keys():
            Class,referenced_classname,referenced_Field,referenced_Value,column_Header=foreign_keys[field]
            foreign_field='%s.%s:%s'%(referenced_classname,referenced_Value,column_Header)
            foreign_record=Class.query.get(value)
            foreign_description="'%s'"%getattr(foreign_record,referenced_Value)
        set_query_option(   engine=db.engine,Interface=Interface,
                        User_Id=current_user.id,
                        Table_name='country',
                        Option_Type=OPTION_FILTER,
                        Argument_1=foreign_field,
                        Argument_2='==',
                        Argument_3=foreign_description
                        )
    page     =  request.args.get('page',    1   ,type=int)
    addx     =  request.args.get('add.x',   None,type=int)
    addy     =  request.args.get('add.y',   None,type=int)
    exportx  =  request.args.get('export.x',None,type=int)
    exporty  =  request.args.get('export.y',None,type=int)
    filterx  =  request.args.get('filter.x',None,type=int)
    filtery  =  request.args.get('filter.y',None,type=int)
    # Select excluyent view mode
    if   addx    is not None: mode = 'add'
    elif exportx is not None: mode = 'export'
    elif filterx is not None: mode = 'filter'
    else:                     mode = 'select'
    Cou_Code =  request.args.get('Cou_Code',None,type=str)
    Cou_Name =  request.args.get('Cou_Name',None,type=str)
    Cou_A3 =  request.args.get('Cou_A3',None,type=str)
    Cou_N =  request.args.get('Cou_N',None,type=str)
    
    
    # Build default query all fields from table
    
    if Cou_Code is not None and len(Cou_Code)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='country',
                Option_Type=OPTION_FILTER,
                Argument_1='Cou_Code:Code',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Cou_Code
                )
    
    
    if Cou_Name is not None and len(Cou_Name)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='country',
                Option_Type=OPTION_FILTER,
                Argument_1='Cou_Name:Name',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Cou_Name
                )
    
    
    if Cou_A3 is not None and len(Cou_A3)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='country',
                Option_Type=OPTION_FILTER,
                Argument_1='Cou_A3:Alphanum Code',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Cou_A3
                )
    
    
    if Cou_N is not None and len(Cou_N)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='country',
                Option_Type=OPTION_FILTER,
                Argument_1='Cou_N:ISO Numeric Code',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Cou_N
                )
    
    
    
    statement_query,options=get_query_options(engine=db.engine,Interface=Interface,Table_name='country',User_Id=current_user.id)
    query=eval(statement_query)
    filtered_query = query    
    if mode == 'filter':
        query=filtered_query
    elif mode == 'export':
        query=filtered_query
        fh,output_file = tempfile.mkstemp(suffix='', prefix='Countries_', dir=None, text=False)
        dict = {'header':{},'detail':[]}
        count = 0
        rows = query.all()
        for row in rows:
            dict['detail'].append({})
            for column in ['Cou_Code', 'Cou_Name', 'Cou_A3', 'Cou_N']:
                dict['detail'][count].update( { column:str(row.__getattribute__(column))})
                
            count += 1
        dict['header'].update({'count':count})
        jsonarray      = json.dumps(dict)
        data           = json.loads(jsonarray)  
        dataframe      = json_normalize(data, 'detail').assign(**data['header'])
        fh,output_file = tempfile.mkstemp(suffix='', prefix='Countries_', dir='/tmp', text=False)
        xlsx_file      = '%s/%s'%(current_app.root_path,url_for('static',filename='%s.xls'%(output_file)))
        dataframe.to_excel(xlsx_file,sheet_name='Countries',columns=['Cou_Code', 'Cou_Name', 'Cou_A3', 'Cou_N'])
        return send_file(xlsx_file,as_attachment=True,attachment_filename=output_file.replace('/','_')+'.xls')
    elif mode == 'add':
        return redirect(url_for('.forms_Countries'))
    elif mode == 'select':
        pass
        # if some filter is required
        if field is not None:
            if field == 'Cou_Code':
                if value is not None:
                    query = query.filter_by(Cou_Code=value)
            if field == 'Cou_Name':
                if value is not None:
                    query = query.filter_by(Cou_Name=value)
            if field == 'Cou_A3':
                if value is not None:
                    query = query.filter_by(Cou_A3=value)
            if field == 'Cou_N':
                if value is not None:
                    query = query.filter_by(Cou_N=value)
            
    # Actual request from DB follows
    tracebox_log(query,logger,length=50)
    rows = query.paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
    # Setting pagination variables ...
    if field is not None:
       next_url = url_for('.select_Countries_query', field=field, value=value, page=rows.next_num) if rows.has_next else None
       prev_url = url_for('.select_Countries_query', field=field, value=value, page=rows.prev_num) if rows.has_prev else None
    else:
       next_url = url_for('.select_Countries_query', page=rows.next_num) if rows.has_next else None
       prev_url = url_for('.select_Countries_query', page=rows.prev_num) if rows.has_prev else None
    # Actual rendering ...
    if request.headers.get('Content-Type') is not None or request.args.get('JSON',None,type=str) is not None:
        if "JSON" in request.headers.get('Content-Type') or request.args.get('JSON',None,type=str) is not None:
            logger.debug('select_Countries_query(): will render: JSON rows')
            logger.debug('select_Countries_query(): Exit')
            return json.dumps(serialize_object(rows.__dict__))
    logger.debug('select_Countries_query(): will render: countries_All.html')
    logger.debug('select_Countries_query(): Exit')
    return render_template('countries_select_All.html',rows=rows,options=options)
#===============================================================================
   # NOTE: HARDCODE. TO REMOVE --------------------------------------------
def chk_c000001(*args,**kwargs):
    pass
    
from emtec.common.interface import *
from emtec.collector.db.orm_model          import Interface
from emtec.collector.db.flask_models       import interface
#-----------------------------------------------------------------------
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2020-02-20 16:44:35
# =============================================================================

# ======================================================================
#  Auto-Generated code. Do not modify 
#  (C) Sertechno/Emtec Group (2018,2019)
#  GLVH @ 2020-02-20 16:44:38.487628
# ======================================================================
        
# gen_views_form.html:AG 2020-02-20 16:44:38.487651
@main.route('/forms/CU_Operations', methods=['GET', 'POST'])
@login_required

def forms_CU_Operations():
    """ Form handling function for table CU_Operations """
    logger.debug('forms_CU_Operations(): Enter')
    CU_Operation  =  request.args.get('CU_Operation',0,type=int)
    
    row =  cu_operation.query.filter(cu_operation.CU_Operation == CU_Operation).first()
    if row is None:
        row=cu_operation()
        session['is_new_row']=True
    session['data'] =  {  'CU_Operation':row.CU_Operation, 'Value':row.Value, 'Is_Multiply':row.Is_Multiply, 'Factor':row.Factor }
    
    form = frm_cu_operation()
    
    # Actual Form activation here
    if form.validate_on_submit():
    # Code for SAVE option
        if form.submit_Save.data and current_user.role_id > 1:
    
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
                   message=Markup('<b>Charge Unit Conversion Operation CU_Operation saved OK</b>')
                   flash(message)
               db.session.close()
            except Exception as e:
               db.session.rollback()
               db.session.close()
               message=Markup('ERROR saving Charge Unit Conversion Operation record : %s'%(e))
               flash(message)
            return redirect(url_for('.select_CU_Operations_query'))    
    # Code for NEW option
    # GV 20190109 f.write(        "        elif   form.submit_New.data:\n")
        elif   form.submit_New.data and current_user.role_id>1:
            #print('New Data Here ...')
            session['is_new_row']=True
            db.session.close()
            row=cu_operation()
    
            return redirect(url_for('.forms_CU_Operations'))    
    
    # Code for CANCEL option 
        elif   form.submit_Cancel.data:
            #print('Cancel Data Here ... does nothing')
            message=Markup('Charge Unit Conversion Operation Record modifications discarded ...')
            flash(message)
    # Code for ANY OTHER option should never get here
        else:
            #print('form validated but not submited ???')
            message=Markup("<b>Charge Unit Conversion Operation data modifications not allowed for user '%s'. Please contact EG Suite's Administrator ...</b>"%(current_user.username))    
            flash(message)
    
            return redirect(url_for('.forms_'))    
    
    
    form.CU_Operation.data = row.CU_Operation
    form.Value.data = row.Value
    form.Is_Multiply.data = row.Is_Multiply
    form.Factor.data = row.Factor
    session['prev_row'] = str(row)
    session['is_new_row'] = False
    logger.debug('forms_CU_Operations(): Exit')
    # Generates pagination data here
    P=[]
    # Tab Relations = [{'name': 'charge_units', 'class': 'charge_unit', 'backref': 'cu_operation', 'caption': 'Charge Units', 'table': 'Charge_Units'}]
    
    from flask_sqlalchemy import Pagination
    # [{'name': 'charge_units', 'class': 'charge_unit', 'backref': 'cu_operation', 'caption': 'Charge Units', 'table': 'Charge_Units'}]
    P.append(({'name': 'charge_units', 'class': 'charge_unit', 'backref': 'cu_operation', 'caption': 'Charge Units', 'table': 'Charge_Units'},row.charge_units.paginate()))
    
    """
    print("P=",P,type(P))
    for relation,p in P:
        print("relation=",relation)
        print("p.query=",p.query)
        print("p.has_next=",p.has_next,p.next,p.next_num)
        print("p.has_prev=",p.has_prev,p.prev,p.prev_num)
        print("p.pages=",p.pages)
        print("p.iter_pages=",p.iter_pages)
        print("p.per_page=",p.per_page)
        print("p.total=",p.total)
        print("p.items type=",type(p.items),len(p.items))
    """
    
    # Generation of pagination data completed       
    return render_template('cu_operations.html', form=form, row=row, P=P)    
# ======================================================================



# ======================================================================
#  Auto-Generated code. Do not modify 
#  (C) Sertechno/Emtec Group (2018,2019)
#  GLVH @ 2020-02-20 16:44:38.511295
# ======================================================================
        
# gen_views_delete.html:AG 2020-02-20 16:44:38.511317
@main.route('/forms/CU_Operations_delete', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@admin_required
def forms_CU_Operations_delete():
    """ Delete record handling function for table CU_Operations """
    logger.debug('forms_CU_Operations_delete(): Enter')
    CU_Operation  =  request.args.get('CU_Operation',0,type=int)
    row =  cu_operation.query.filter(cu_operation.CU_Operation == CU_Operation).first()

    if row is None:
        row=cu_operation()
    session['data'] =  {  'CU_Operation':row.CU_Operation, 'Value':row.Value, 'Is_Multiply':row.Is_Multiply, 'Factor':row.Factor }
                       
    form = frm_cu_operation_delete()

    # Tab['has_fks'] False
    
            
    # Actual Form activation here
    if form.validate_on_submit():
    
    # Code for SAVE option
        if  form.submit_Delete.data:
            print('Delete Data Here...')

    
    #f.write(        "            print('Delete Data Here...')
            try:
                session['deleted_row']=str(row)
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                logger.audit ( '%s:DEL:%s' % (current_user.username,session['deleted_row']) )
                flash('Charge Unit Conversion Operation CU_Operation deleted OK')
            except exc.IntegrityError as e:
                db.session.rollback()    
                flash('INTEGRITY ERROR: Are you sure there are no dependant records in other tables?')
                return redirect(url_for('.forms_CU_Operations_delete',CU_Operation=session['data']['CU_Operation']))    
    
            return redirect(url_for('.select_CU_Operations_query'))    
    # Code for CANCEL option 
        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
            return redirect(url_for('.select_CU_Operations_query'))    
    # Code for ANY OTHER option should never get here
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.select_CU_Operations_query'))    
    
    logger.debug('forms_CU_Operations_delete(): Exit')
    return render_template('cu_operations_delete.html', form=form, data=session.get('data'),row=row)
#===============================================================================

# ======================================================================
#  Auto-Generated code. Do not modify 
#  (C) Sertechno/Emtec Group (2018,2019)
#  GLVH @ 2020-02-20 16:44:38.572727
# ======================================================================


from pprint import pprint, pformat

# gen_views_select_query.html:AG 2020-02-20 16:44:38.572750        
@main.route('/select/CU_Operations_Query', methods=['GET','POST'])
@login_required
@admin_required
def select_CU_Operations_query():
    """ Select rows handling function for table 'CU_Operations' """
    logger.debug('select_CU_Operations_query(): Enter')
    chk_c000001(filename=os.path.join(current_app.root_path, '.c000001'),request=request,db=db,logger=logger)
    # Get parameters from URL call
    ia       =  request.args.get('ia',     None,type=str)
    if ia is not None:
        ia=ia.split(',')
        if ia[0]=='ORDER':
            set_query_option(engine=db.engine,Interface=Interface,User_Id=current_user.id,Table_name='cu_operation',Option_Type=OPTION_ORDER_BY,Argument_1=ia[1],Argument_2=ia[2])
        elif ia[0]=='GROUP':
            set_query_option(engine=db.engine,Interface=Interface,User_Id=current_user.id,Table_name='cu_operation',Option_Type=OPTION_GROUP_BY,Argument_1=ia[1])
        elif ia[0]=='LIMIT':
            set_query_option(engine=db.engine,Interface=Interface,User_Id=current_user.id,Table_name='cu_operation',Option_Type=OPTION_LIMIT,Argument_1=ia[1])

    iad      =  request.args.get('iad',     None,type=int)
    if iad is not None: delete_query_option(engine=db.engine,Interface=Interface,Id=iad) 
    
    field    =  request.args.get('field',   None,type=str)
    value    =  request.args.get('value',   None,type=str)
    
    # Populates a list of foreign keys used for advanced filtering
    # ------------------------------------------------------------------
    foreign_keys={}
    
    # ------------------------------------------------------------------
    
    if field is not None:
        reset_query_options(    engine=db.engine,Interface=Interface,
                                User_Id=current_user.id,
                                Table_name='cu_operation'
                                )

        
        if field in foreign_keys.keys():
            Class,referenced_classname,referenced_Field,referenced_Value,column_Header=foreign_keys[field]
            foreign_field='%s.%s:%s'%(referenced_classname,referenced_Value,column_Header)
            foreign_record=Class.query.get(value)
            foreign_description="'%s'"%getattr(foreign_record,referenced_Value)
        set_query_option(   engine=db.engine,Interface=Interface,
                        User_Id=current_user.id,
                        Table_name='cu_operation',
                        Option_Type=OPTION_FILTER,
                        Argument_1=foreign_field,
                        Argument_2='==',
                        Argument_3=foreign_description
                        )
    page     =  request.args.get('page',    1   ,type=int)
    addx     =  request.args.get('add.x',   None,type=int)
    addy     =  request.args.get('add.y',   None,type=int)
    exportx  =  request.args.get('export.x',None,type=int)
    exporty  =  request.args.get('export.y',None,type=int)
    filterx  =  request.args.get('filter.x',None,type=int)
    filtery  =  request.args.get('filter.y',None,type=int)
    # Select excluyent view mode
    if   addx    is not None: mode = 'add'
    elif exportx is not None: mode = 'export'
    elif filterx is not None: mode = 'filter'
    else:                     mode = 'select'
    CU_Operation =  request.args.get('CU_Operation',None,type=str)
    Value =  request.args.get('Value',None,type=str)
    Is_Multiply =  request.args.get('Is_Multiply',None,type=str)
    Factor =  request.args.get('Factor',None,type=str)
    
    
    # Build default query all fields from table
    
    if CU_Operation is not None and len(CU_Operation)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='cu_operation',
                Option_Type=OPTION_FILTER,
                Argument_1='CU_Operation:Operation',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%CU_Operation
                )
    
    
    if Value is not None and len(Value)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='cu_operation',
                Option_Type=OPTION_FILTER,
                Argument_1='Value:Value',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Value
                )
    
    
    if Is_Multiply is not None and len(Is_Multiply)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='cu_operation',
                Option_Type=OPTION_FILTER,
                Argument_1='Is_Multiply:Is Multiply',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Is_Multiply
                )
    
    
    if Factor is not None and len(Factor)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='cu_operation',
                Option_Type=OPTION_FILTER,
                Argument_1='Factor:Factor',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Factor
                )
    
    
    
    statement_query,options=get_query_options(engine=db.engine,Interface=Interface,Table_name='cu_operation',User_Id=current_user.id)
    query=eval(statement_query)
    filtered_query = query    
    if mode == 'filter':
        query=filtered_query
    elif mode == 'export':
        query=filtered_query
        fh,output_file = tempfile.mkstemp(suffix='', prefix='CU_Operations_', dir=None, text=False)
        dict = {'header':{},'detail':[]}
        count = 0
        rows = query.all()
        for row in rows:
            dict['detail'].append({})
            for column in ['CU_Operation', 'Value', 'Is_Multiply', 'Factor']:
                dict['detail'][count].update( { column:str(row.__getattribute__(column))})
                
            count += 1
        dict['header'].update({'count':count})
        jsonarray      = json.dumps(dict)
        data           = json.loads(jsonarray)  
        dataframe      = json_normalize(data, 'detail').assign(**data['header'])
        fh,output_file = tempfile.mkstemp(suffix='', prefix='CU_Operations_', dir='/tmp', text=False)
        xlsx_file      = '%s/%s'%(current_app.root_path,url_for('static',filename='%s.xls'%(output_file)))
        dataframe.to_excel(xlsx_file,sheet_name='CU_Operations',columns=['CU_Operation', 'Value', 'Is_Multiply', 'Factor'])
        return send_file(xlsx_file,as_attachment=True,attachment_filename=output_file.replace('/','_')+'.xls')
    elif mode == 'add':
        return redirect(url_for('.forms_CU_Operations'))
    elif mode == 'select':
        pass
        # if some filter is required
        if field is not None:
            if field == 'CU_Operation':
                if value is not None:
                    query = query.filter_by(CU_Operation=value)
            if field == 'Value':
                if value is not None:
                    query = query.filter_by(Value=value)
            if field == 'Is_Multiply':
                if value is not None:
                    query = query.filter_by(Is_Multiply=value)
            if field == 'Factor':
                if value is not None:
                    query = query.filter_by(Factor=value)
            
    # Actual request from DB follows
    tracebox_log(query,logger,length=50)
    rows = query.paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
    # Setting pagination variables ...
    if field is not None:
       next_url = url_for('.select_CU_Operations_query', field=field, value=value, page=rows.next_num) if rows.has_next else None
       prev_url = url_for('.select_CU_Operations_query', field=field, value=value, page=rows.prev_num) if rows.has_prev else None
    else:
       next_url = url_for('.select_CU_Operations_query', page=rows.next_num) if rows.has_next else None
       prev_url = url_for('.select_CU_Operations_query', page=rows.prev_num) if rows.has_prev else None
    # Actual rendering ...
    if request.headers.get('Content-Type') is not None or request.args.get('JSON',None,type=str) is not None:
        if "JSON" in request.headers.get('Content-Type') or request.args.get('JSON',None,type=str) is not None:
            logger.debug('select_CU_Operations_query(): will render: JSON rows')
            logger.debug('select_CU_Operations_query(): Exit')
            return json.dumps(serialize_object(rows.__dict__))
    logger.debug('select_CU_Operations_query(): will render: cu_operations_All.html')
    logger.debug('select_CU_Operations_query(): Exit')
    return render_template('cu_operations_select_All.html',rows=rows,options=options)
#===============================================================================
   # NOTE: HARDCODE. TO REMOVE --------------------------------------------
def chk_c000001(*args,**kwargs):
    pass
    
from emtec.common.interface import *
from emtec.collector.db.orm_model          import Interface
from emtec.collector.db.flask_models       import interface
#-----------------------------------------------------------------------
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2020-02-20 16:44:35
# =============================================================================

# ======================================================================
#  Auto-Generated code. Do not modify 
#  (C) Sertechno/Emtec Group (2018,2019)
#  GLVH @ 2020-02-20 16:44:42.196007
# ======================================================================
        
# gen_views_form.html:AG 2020-02-20 16:44:42.196041
@main.route('/forms/Currencies', methods=['GET', 'POST'])
@login_required

def forms_Currencies():
    """ Form handling function for table Currencies """
    logger.debug('forms_Currencies(): Enter')
    Cur_Code  =  request.args.get('Cur_Code',0,type=int)
    
    row =  currency.query.filter(currency.Cur_Code == Cur_Code).first()
    if row is None:
        row=currency()
        session['is_new_row']=True
    session['data'] =  {  'Cur_Code':row.Cur_Code, 'Cur_Name':row.Cur_Name, 'Cur_Id':row.Cur_Id, 'Cur_Comment':row.Cur_Comment }
    
    form = frm_currency()
    
    # Actual Form activation here
    if form.validate_on_submit():
    # Code for SAVE option
        if form.submit_Save.data and current_user.role_id > 1:
    
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
                   message=Markup('<b>Currency Cur_Code saved OK</b>')
                   flash(message)
               db.session.close()
            except Exception as e:
               db.session.rollback()
               db.session.close()
               message=Markup('ERROR saving Currency record : %s'%(e))
               flash(message)
            return redirect(url_for('.select_Currencies_query'))    
    # Code for NEW option
    # GV 20190109 f.write(        "        elif   form.submit_New.data:\n")
        elif   form.submit_New.data and current_user.role_id>1:
            #print('New Data Here ...')
            session['is_new_row']=True
            db.session.close()
            row=currency()
    
            return redirect(url_for('.forms_Currencies'))    
    
    # Code for CANCEL option 
        elif   form.submit_Cancel.data:
            #print('Cancel Data Here ... does nothing')
            message=Markup('Currency Record modifications discarded ...')
            flash(message)
    # Code for ANY OTHER option should never get here
        else:
            #print('form validated but not submited ???')
            message=Markup("<b>Currency data modifications not allowed for user '%s'. Please contact EG Suite's Administrator ...</b>"%(current_user.username))    
            flash(message)
    
            return redirect(url_for('.forms_'))    
    
    
    form.Cur_Code.data = row.Cur_Code
    form.Cur_Name.data = row.Cur_Name
    form.Cur_Id.data = row.Cur_Id
    form.Cur_Comment.data = row.Cur_Comment
    session['prev_row'] = str(row)
    session['is_new_row'] = False
    logger.debug('forms_Currencies(): Exit')
    # Generates pagination data here
    P=[]
    # Tab Relations = [{'name': 'cost_centers', 'class': 'cost_center', 'backref': 'currency', 'caption': 'Cost Centers', 'table': 'Cost_Centers'}, {'name': 'countries_currencies', 'class': 'country_currency', 'backref': 'currency', 'caption': 'Countries vs Currencies', 'table': 'Countries_Currencies'}, {'name': 'exchange_rates', 'class': 'exchange_rate', 'backref': 'currency', 'caption': 'Exchange Rates', 'table': 'Exchange_Rates'}, {'name': 'rates', 'class': 'rate', 'backref': 'currency', 'caption': 'Rates', 'table': 'Rates'}]
    
    from flask_sqlalchemy import Pagination
    # [{'name': 'cost_centers', 'class': 'cost_center', 'backref': 'currency', 'caption': 'Cost Centers', 'table': 'Cost_Centers'}, {'name': 'countries_currencies', 'class': 'country_currency', 'backref': 'currency', 'caption': 'Countries vs Currencies', 'table': 'Countries_Currencies'}, {'name': 'exchange_rates', 'class': 'exchange_rate', 'backref': 'currency', 'caption': 'Exchange Rates', 'table': 'Exchange_Rates'}, {'name': 'rates', 'class': 'rate', 'backref': 'currency', 'caption': 'Rates', 'table': 'Rates'}]
    P.append(({'name': 'cost_centers', 'class': 'cost_center', 'backref': 'currency', 'caption': 'Cost Centers', 'table': 'Cost_Centers'},row.cost_centers.paginate()))
    P.append(({'name': 'countries_currencies', 'class': 'country_currency', 'backref': 'currency', 'caption': 'Countries vs Currencies', 'table': 'Countries_Currencies'},row.countries_currencies.paginate()))
    P.append(({'name': 'exchange_rates', 'class': 'exchange_rate', 'backref': 'currency', 'caption': 'Exchange Rates', 'table': 'Exchange_Rates'},row.exchange_rates.paginate()))
    P.append(({'name': 'rates', 'class': 'rate', 'backref': 'currency', 'caption': 'Rates', 'table': 'Rates'},row.rates.paginate()))
    
    """
    print("P=",P,type(P))
    for relation,p in P:
        print("relation=",relation)
        print("p.query=",p.query)
        print("p.has_next=",p.has_next,p.next,p.next_num)
        print("p.has_prev=",p.has_prev,p.prev,p.prev_num)
        print("p.pages=",p.pages)
        print("p.iter_pages=",p.iter_pages)
        print("p.per_page=",p.per_page)
        print("p.total=",p.total)
        print("p.items type=",type(p.items),len(p.items))
    """
    
    # Generation of pagination data completed       
    return render_template('currencies.html', form=form, row=row, P=P)    
# ======================================================================



# ======================================================================
#  Auto-Generated code. Do not modify 
#  (C) Sertechno/Emtec Group (2018,2019)
#  GLVH @ 2020-02-20 16:44:42.219204
# ======================================================================
        
# gen_views_delete.html:AG 2020-02-20 16:44:42.219236
@main.route('/forms/Currencies_delete', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@admin_required
def forms_Currencies_delete():
    """ Delete record handling function for table Currencies """
    logger.debug('forms_Currencies_delete(): Enter')
    Cur_Code  =  request.args.get('Cur_Code',0,type=int)
    row =  currency.query.filter(currency.Cur_Code == Cur_Code).first()

    if row is None:
        row=currency()
    session['data'] =  {  'Cur_Code':row.Cur_Code, 'Cur_Name':row.Cur_Name, 'Cur_Id':row.Cur_Id, 'Cur_Comment':row.Cur_Comment }
                       
    form = frm_currency_delete()

    # Tab['has_fks'] False
    
            
    # Actual Form activation here
    if form.validate_on_submit():
    
    # Code for SAVE option
        if  form.submit_Delete.data:
            print('Delete Data Here...')

    
    #f.write(        "            print('Delete Data Here...')
            try:
                session['deleted_row']=str(row)
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                logger.audit ( '%s:DEL:%s' % (current_user.username,session['deleted_row']) )
                flash('Currency Cur_Code deleted OK')
            except exc.IntegrityError as e:
                db.session.rollback()    
                flash('INTEGRITY ERROR: Are you sure there are no dependant records in other tables?')
                return redirect(url_for('.forms_Currencies_delete',Cur_Code=session['data']['Cur_Code']))    
    
            return redirect(url_for('.select_Currencies_query'))    
    # Code for CANCEL option 
        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
            return redirect(url_for('.select_Currencies_query'))    
    # Code for ANY OTHER option should never get here
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.select_Currencies_query'))    
    
    logger.debug('forms_Currencies_delete(): Exit')
    return render_template('currencies_delete.html', form=form, data=session.get('data'),row=row)
#===============================================================================

# ======================================================================
#  Auto-Generated code. Do not modify 
#  (C) Sertechno/Emtec Group (2018,2019)
#  GLVH @ 2020-02-20 16:44:42.268283
# ======================================================================


from pprint import pprint, pformat

# gen_views_select_query.html:AG 2020-02-20 16:44:42.268409        
@main.route('/select/Currencies_Query', methods=['GET','POST'])
@login_required
@admin_required
def select_Currencies_query():
    """ Select rows handling function for table 'Currencies' """
    logger.debug('select_Currencies_query(): Enter')
    chk_c000001(filename=os.path.join(current_app.root_path, '.c000001'),request=request,db=db,logger=logger)
    # Get parameters from URL call
    ia       =  request.args.get('ia',     None,type=str)
    if ia is not None:
        ia=ia.split(',')
        if ia[0]=='ORDER':
            set_query_option(engine=db.engine,Interface=Interface,User_Id=current_user.id,Table_name='currency',Option_Type=OPTION_ORDER_BY,Argument_1=ia[1],Argument_2=ia[2])
        elif ia[0]=='GROUP':
            set_query_option(engine=db.engine,Interface=Interface,User_Id=current_user.id,Table_name='currency',Option_Type=OPTION_GROUP_BY,Argument_1=ia[1])
        elif ia[0]=='LIMIT':
            set_query_option(engine=db.engine,Interface=Interface,User_Id=current_user.id,Table_name='currency',Option_Type=OPTION_LIMIT,Argument_1=ia[1])

    iad      =  request.args.get('iad',     None,type=int)
    if iad is not None: delete_query_option(engine=db.engine,Interface=Interface,Id=iad) 
    
    field    =  request.args.get('field',   None,type=str)
    value    =  request.args.get('value',   None,type=str)
    
    # Populates a list of foreign keys used for advanced filtering
    # ------------------------------------------------------------------
    foreign_keys={}
    
    # ------------------------------------------------------------------
    
    if field is not None:
        reset_query_options(    engine=db.engine,Interface=Interface,
                                User_Id=current_user.id,
                                Table_name='currency'
                                )

        
        if field in foreign_keys.keys():
            Class,referenced_classname,referenced_Field,referenced_Value,column_Header=foreign_keys[field]
            foreign_field='%s.%s:%s'%(referenced_classname,referenced_Value,column_Header)
            foreign_record=Class.query.get(value)
            foreign_description="'%s'"%getattr(foreign_record,referenced_Value)
        set_query_option(   engine=db.engine,Interface=Interface,
                        User_Id=current_user.id,
                        Table_name='currency',
                        Option_Type=OPTION_FILTER,
                        Argument_1=foreign_field,
                        Argument_2='==',
                        Argument_3=foreign_description
                        )
    page     =  request.args.get('page',    1   ,type=int)
    addx     =  request.args.get('add.x',   None,type=int)
    addy     =  request.args.get('add.y',   None,type=int)
    exportx  =  request.args.get('export.x',None,type=int)
    exporty  =  request.args.get('export.y',None,type=int)
    filterx  =  request.args.get('filter.x',None,type=int)
    filtery  =  request.args.get('filter.y',None,type=int)
    # Select excluyent view mode
    if   addx    is not None: mode = 'add'
    elif exportx is not None: mode = 'export'
    elif filterx is not None: mode = 'filter'
    else:                     mode = 'select'
    Cur_Code =  request.args.get('Cur_Code',None,type=str)
    Cur_Name =  request.args.get('Cur_Name',None,type=str)
    Cur_Id =  request.args.get('Cur_Id',None,type=str)
    Cur_Comment =  request.args.get('Cur_Comment',None,type=str)
    
    
    # Build default query all fields from table
    
    if Cur_Code is not None and len(Cur_Code)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='currency',
                Option_Type=OPTION_FILTER,
                Argument_1='Cur_Code:Code',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Cur_Code
                )
    
    
    if Cur_Name is not None and len(Cur_Name)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='currency',
                Option_Type=OPTION_FILTER,
                Argument_1='Cur_Name:Name',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Cur_Name
                )
    
    
    if Cur_Id is not None and len(Cur_Id)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='currency',
                Option_Type=OPTION_FILTER,
                Argument_1='Cur_Id:Id',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Cur_Id
                )
    
    
    if Cur_Comment is not None and len(Cur_Comment)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='currency',
                Option_Type=OPTION_FILTER,
                Argument_1='Cur_Comment:Comment',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Cur_Comment
                )
    
    
    
    statement_query,options=get_query_options(engine=db.engine,Interface=Interface,Table_name='currency',User_Id=current_user.id)
    query=eval(statement_query)
    filtered_query = query    
    if mode == 'filter':
        query=filtered_query
    elif mode == 'export':
        query=filtered_query
        fh,output_file = tempfile.mkstemp(suffix='', prefix='Currencies_', dir=None, text=False)
        dict = {'header':{},'detail':[]}
        count = 0
        rows = query.all()
        for row in rows:
            dict['detail'].append({})
            for column in ['Cur_Code', 'Cur_Name', 'Cur_Id', 'Cur_Comment']:
                dict['detail'][count].update( { column:str(row.__getattribute__(column))})
                
            count += 1
        dict['header'].update({'count':count})
        jsonarray      = json.dumps(dict)
        data           = json.loads(jsonarray)  
        dataframe      = json_normalize(data, 'detail').assign(**data['header'])
        fh,output_file = tempfile.mkstemp(suffix='', prefix='Currencies_', dir='/tmp', text=False)
        xlsx_file      = '%s/%s'%(current_app.root_path,url_for('static',filename='%s.xls'%(output_file)))
        dataframe.to_excel(xlsx_file,sheet_name='Currencies',columns=['Cur_Code', 'Cur_Name', 'Cur_Id', 'Cur_Comment'])
        return send_file(xlsx_file,as_attachment=True,attachment_filename=output_file.replace('/','_')+'.xls')
    elif mode == 'add':
        return redirect(url_for('.forms_Currencies'))
    elif mode == 'select':
        pass
        # if some filter is required
        if field is not None:
            if field == 'Cur_Code':
                if value is not None:
                    query = query.filter_by(Cur_Code=value)
            if field == 'Cur_Name':
                if value is not None:
                    query = query.filter_by(Cur_Name=value)
            if field == 'Cur_Id':
                if value is not None:
                    query = query.filter_by(Cur_Id=value)
            if field == 'Cur_Comment':
                if value is not None:
                    query = query.filter_by(Cur_Comment=value)
            
    # Actual request from DB follows
    tracebox_log(query,logger,length=50)
    rows = query.paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
    # Setting pagination variables ...
    if field is not None:
       next_url = url_for('.select_Currencies_query', field=field, value=value, page=rows.next_num) if rows.has_next else None
       prev_url = url_for('.select_Currencies_query', field=field, value=value, page=rows.prev_num) if rows.has_prev else None
    else:
       next_url = url_for('.select_Currencies_query', page=rows.next_num) if rows.has_next else None
       prev_url = url_for('.select_Currencies_query', page=rows.prev_num) if rows.has_prev else None
    # Actual rendering ...
    if request.headers.get('Content-Type') is not None or request.args.get('JSON',None,type=str) is not None:
        if "JSON" in request.headers.get('Content-Type') or request.args.get('JSON',None,type=str) is not None:
            logger.debug('select_Currencies_query(): will render: JSON rows')
            logger.debug('select_Currencies_query(): Exit')
            return json.dumps(serialize_object(rows.__dict__))
    logger.debug('select_Currencies_query(): will render: currencies_All.html')
    logger.debug('select_Currencies_query(): Exit')
    return render_template('currencies_select_All.html',rows=rows,options=options)
#===============================================================================
   # NOTE: HARDCODE. TO REMOVE --------------------------------------------
def chk_c000001(*args,**kwargs):
    pass
    
from emtec.common.interface import *
from emtec.collector.db.orm_model          import Interface
from emtec.collector.db.flask_models       import interface
#-----------------------------------------------------------------------
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2020-02-20 16:44:35
# =============================================================================

# ======================================================================
#  Auto-Generated code. Do not modify 
#  (C) Sertechno/Emtec Group (2018,2019)
#  GLVH @ 2020-02-20 16:44:42.529115
# ======================================================================
        
# gen_views_form.html:AG 2020-02-20 16:44:42.529138
@main.route('/forms/Customers', methods=['GET', 'POST'])
@login_required

def forms_Customers():
    """ Form handling function for table Customers """
    logger.debug('forms_Customers(): Enter')
    Cus_Id  =  request.args.get('Cus_Id',0,type=int)
    
    row =  customer.query.filter(customer.Cus_Id == Cus_Id).first()
    if row is None:
        row=customer()
        session['is_new_row']=True
    session['data'] =  {  'Cus_Id':row.Cus_Id, 'Cus_Name':row.Cus_Name, 'CC_Id':row.CC_Id }
    
    form = frm_customer()
    
    if form.has_FKs:
        form.CC_Id.choices = db.session.query(cost_center.CC_Id,cost_center.CC_Description).order_by(cost_center.CC_Description).all()

    
    # Actual Form activation here
    if form.validate_on_submit():
    # Code for SAVE option
        if form.submit_Save.data and current_user.role_id > 1:
    
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
                   message=Markup('<b>Customer Cus_Id saved OK</b>')
                   flash(message)
               db.session.close()
            except Exception as e:
               db.session.rollback()
               db.session.close()
               message=Markup('ERROR saving Customer record : %s'%(e))
               flash(message)
            return redirect(url_for('.select_Customers_query'))    
    # Code for NEW option
    # GV 20190109 f.write(        "        elif   form.submit_New.data:\n")
        elif   form.submit_New.data and current_user.role_id>1:
            #print('New Data Here ...')
            session['is_new_row']=True
            db.session.close()
            row=customer()
    
            return redirect(url_for('.forms_Customers',Cus_Id=row.Cus_Id))
    
    # Code for CANCEL option 
        elif   form.submit_Cancel.data:
            #print('Cancel Data Here ... does nothing')
            message=Markup('Customer Record modifications discarded ...')
            flash(message)
    # Code for ANY OTHER option should never get here
        else:
            #print('form validated but not submited ???')
            message=Markup("<b>Customer data modifications not allowed for user '%s'. Please contact EG Suite's Administrator ...</b>"%(current_user.username))    
            flash(message)
    
            return redirect(url_for('.forms_Customers',Cus_Id=row.Cus_Id))
    
    
    form.Cus_Name.data = row.Cus_Name
    form.CC_Id.data = row.CC_Id
    session['prev_row'] = str(row)
    session['is_new_row'] = False
    logger.debug('forms_Customers(): Exit')
    # Generates pagination data here
    P=[]
    # Tab Relations = [{'name': 'configuration_items', 'class': 'configuration_item', 'backref': 'customer', 'caption': 'Configuration Items', 'table': 'Configuration_Items'}, {'name': 'rates', 'class': 'rate', 'backref': 'customer', 'caption': 'Rates', 'table': 'Rates'}]
    
    from flask_sqlalchemy import Pagination
    # [{'name': 'configuration_items', 'class': 'configuration_item', 'backref': 'customer', 'caption': 'Configuration Items', 'table': 'Configuration_Items'}, {'name': 'rates', 'class': 'rate', 'backref': 'customer', 'caption': 'Rates', 'table': 'Rates'}]
    P.append(({'name': 'configuration_items', 'class': 'configuration_item', 'backref': 'customer', 'caption': 'Configuration Items', 'table': 'Configuration_Items'},row.configuration_items.paginate()))
    P.append(({'name': 'rates', 'class': 'rate', 'backref': 'customer', 'caption': 'Rates', 'table': 'Rates'},row.rates.paginate()))
    
    """
    print("P=",P,type(P))
    for relation,p in P:
        print("relation=",relation)
        print("p.query=",p.query)
        print("p.has_next=",p.has_next,p.next,p.next_num)
        print("p.has_prev=",p.has_prev,p.prev,p.prev_num)
        print("p.pages=",p.pages)
        print("p.iter_pages=",p.iter_pages)
        print("p.per_page=",p.per_page)
        print("p.total=",p.total)
        print("p.items type=",type(p.items),len(p.items))
    """
    
    # Generation of pagination data completed       
    return render_template('customers.html', form=form, row=row, P=P)    
# ======================================================================



# ======================================================================
#  Auto-Generated code. Do not modify 
#  (C) Sertechno/Emtec Group (2018,2019)
#  GLVH @ 2020-02-20 16:44:42.552350
# ======================================================================
        
# gen_views_delete.html:AG 2020-02-20 16:44:42.552374
@main.route('/forms/Customers_delete', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@admin_required
def forms_Customers_delete():
    """ Delete record handling function for table Customers """
    logger.debug('forms_Customers_delete(): Enter')
    Cus_Id  =  request.args.get('Cus_Id',0,type=int)
    row =  customer.query.filter(customer.Cus_Id == Cus_Id).first()

    if row is None:
        row=customer()
    session['data'] =  {  'Cus_Id':row.Cus_Id, 'Cus_Name':row.Cus_Name, 'CC_Id':row.CC_Id }
                       
    form = frm_customer_delete()

    # Tab['has_fks'] True
    
    pass # Tab['has_fks'] True
    
            
    # Actual Form activation here
    if form.validate_on_submit():
    
    # Code for SAVE option
        if  form.submit_Delete.data:
            print('Delete Data Here...')

    
    #f.write(        "            print('Delete Data Here...')
            try:
                session['deleted_row']=str(row)
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                logger.audit ( '%s:DEL:%s' % (current_user.username,session['deleted_row']) )
                flash('Customer Cus_Id deleted OK')
            except exc.IntegrityError as e:
                db.session.rollback()    
                flash('INTEGRITY ERROR: Are you sure there are no dependant records in other tables?')
                return redirect(url_for('.forms_Customers_delete',Cus_Id=session['data']['Cus_Id']))    
    
            return redirect(url_for('.select_Customers_query'))    
    # Code for CANCEL option 
        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
            return redirect(url_for('.select_Customers_query'))    
    # Code for ANY OTHER option should never get here
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.select_Customers_query'))    
    
    logger.debug('forms_Customers_delete(): Exit')
    return render_template('customers_delete.html', form=form, data=session.get('data'),row=row)
#===============================================================================

# ======================================================================
#  Auto-Generated code. Do not modify 
#  (C) Sertechno/Emtec Group (2018,2019)
#  GLVH @ 2020-02-20 16:44:42.602977
# ======================================================================


from pprint import pprint, pformat

# gen_views_select_query.html:AG 2020-02-20 16:44:42.603006        
@main.route('/select/Customers_Query', methods=['GET','POST'])
@login_required
@admin_required
def select_Customers_query():
    """ Select rows handling function for table 'Customers' """
    logger.debug('select_Customers_query(): Enter')
    chk_c000001(filename=os.path.join(current_app.root_path, '.c000001'),request=request,db=db,logger=logger)
    # Get parameters from URL call
    ia       =  request.args.get('ia',     None,type=str)
    if ia is not None:
        ia=ia.split(',')
        if ia[0]=='ORDER':
            set_query_option(engine=db.engine,Interface=Interface,User_Id=current_user.id,Table_name='customer',Option_Type=OPTION_ORDER_BY,Argument_1=ia[1],Argument_2=ia[2])
        elif ia[0]=='GROUP':
            set_query_option(engine=db.engine,Interface=Interface,User_Id=current_user.id,Table_name='customer',Option_Type=OPTION_GROUP_BY,Argument_1=ia[1])
        elif ia[0]=='LIMIT':
            set_query_option(engine=db.engine,Interface=Interface,User_Id=current_user.id,Table_name='customer',Option_Type=OPTION_LIMIT,Argument_1=ia[1])

    iad      =  request.args.get('iad',     None,type=int)
    if iad is not None: delete_query_option(engine=db.engine,Interface=Interface,Id=iad) 
    
    field    =  request.args.get('field',   None,type=str)
    value    =  request.args.get('value',   None,type=str)
    
    # Populates a list of foreign keys used for advanced filtering
    # ------------------------------------------------------------------
    foreign_keys={}
    
    foreign_keys.update({'CC_Id':(cost_center,'cost_center','CC_Id','CC_Description','Cost Center Id')})
    # ------------------------------------------------------------------
    
    if field is not None:
        reset_query_options(    engine=db.engine,Interface=Interface,
                                User_Id=current_user.id,
                                Table_name='customer'
                                )

        
        if field in foreign_keys.keys():
            Class,referenced_classname,referenced_Field,referenced_Value,column_Header=foreign_keys[field]
            foreign_field='%s.%s:%s'%(referenced_classname,referenced_Value,column_Header)
            foreign_record=Class.query.get(value)
            foreign_description="'%s'"%getattr(foreign_record,referenced_Value)
        set_query_option(   engine=db.engine,Interface=Interface,
                        User_Id=current_user.id,
                        Table_name='customer',
                        Option_Type=OPTION_FILTER,
                        Argument_1=foreign_field,
                        Argument_2='==',
                        Argument_3=foreign_description
                        )
    page     =  request.args.get('page',    1   ,type=int)
    addx     =  request.args.get('add.x',   None,type=int)
    addy     =  request.args.get('add.y',   None,type=int)
    exportx  =  request.args.get('export.x',None,type=int)
    exporty  =  request.args.get('export.y',None,type=int)
    filterx  =  request.args.get('filter.x',None,type=int)
    filtery  =  request.args.get('filter.y',None,type=int)
    # Select excluyent view mode
    if   addx    is not None: mode = 'add'
    elif exportx is not None: mode = 'export'
    elif filterx is not None: mode = 'filter'
    else:                     mode = 'select'
    Cus_Id =  request.args.get('Cus_Id',None,type=str)
    Cus_Name =  request.args.get('Cus_Name',None,type=str)
    CC_Id =  request.args.get('CC_Id',None,type=str)
    
    
    # Build default query all fields from table
    
    if Cus_Id is not None and len(Cus_Id)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='customer',
                Option_Type=OPTION_FILTER,
                Argument_1='Cus_Id:Id',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Cus_Id
                )
    
    
    if Cus_Name is not None and len(Cus_Name)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='customer',
                Option_Type=OPTION_FILTER,
                Argument_1='Cus_Name:Name',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Cus_Name
                )
    
    
    if CC_Id is not None and len(CC_Id)>0:
            Class,referenced_classname,referenced_Field,referenced_Value,column_Header=foreign_keys['CC_Id']
            foreign_field='%s.%s:%s'%(referenced_classname,referenced_Value,column_Header)            
            set_query_option(   engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='customer',
                Option_Type=OPTION_FILTER,
                Argument_1=foreign_field,
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%CC_Id
                )
                                
    
    
    
    statement_query,options=get_query_options(engine=db.engine,Interface=Interface,Table_name='customer',User_Id=current_user.id)
    query=eval(statement_query)
    filtered_query = query    
    if mode == 'filter':
        query=filtered_query
    elif mode == 'export':
        query=filtered_query
        fh,output_file = tempfile.mkstemp(suffix='', prefix='Customers_', dir=None, text=False)
        dict = {'header':{},'detail':[]}
        count = 0
        rows = query.all()
        for row in rows:
            dict['detail'].append({})
            for column in ['Cus_Id', 'Cus_Name', 'CC_Id']:
                dict['detail'][count].update( { column:str(row.__getattribute__(column))})
                
            count += 1
        dict['header'].update({'count':count})
        jsonarray      = json.dumps(dict)
        data           = json.loads(jsonarray)  
        dataframe      = json_normalize(data, 'detail').assign(**data['header'])
        fh,output_file = tempfile.mkstemp(suffix='', prefix='Customers_', dir='/tmp', text=False)
        xlsx_file      = '%s/%s'%(current_app.root_path,url_for('static',filename='%s.xls'%(output_file)))
        dataframe.to_excel(xlsx_file,sheet_name='Customers',columns=['Cus_Id', 'Cus_Name', 'CC_Id'])
        return send_file(xlsx_file,as_attachment=True,attachment_filename=output_file.replace('/','_')+'.xls')
    elif mode == 'add':
        return redirect(url_for('.forms_Customers'))
    elif mode == 'select':
        pass
        # if some filter is required
        if field is not None:
            if field == 'Cus_Id':
                if value is not None:
                    query = query.filter_by(Cus_Id=value)
            if field == 'Cus_Name':
                if value is not None:
                    query = query.filter_by(Cus_Name=value)
            if field == 'CC_Id':
                if value is not None:
                    query = query.filter_by(CC_Id=value)
            # JOIN other tables and generate foreign fields
    query = query.join(cost_center,customer.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)
    
    # Actual request from DB follows
    tracebox_log(query,logger,length=50)
    rows = query.paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
    # Setting pagination variables ...
    if field is not None:
       next_url = url_for('.select_Customers_query', field=field, value=value, page=rows.next_num) if rows.has_next else None
       prev_url = url_for('.select_Customers_query', field=field, value=value, page=rows.prev_num) if rows.has_prev else None
    else:
       next_url = url_for('.select_Customers_query', page=rows.next_num) if rows.has_next else None
       prev_url = url_for('.select_Customers_query', page=rows.prev_num) if rows.has_prev else None
    # Actual rendering ...
    if request.headers.get('Content-Type') is not None or request.args.get('JSON',None,type=str) is not None:
        if "JSON" in request.headers.get('Content-Type') or request.args.get('JSON',None,type=str) is not None:
            logger.debug('select_Customers_query(): will render: JSON rows')
            logger.debug('select_Customers_query(): Exit')
            return json.dumps(serialize_object(rows.__dict__))
    logger.debug('select_Customers_query(): will render: customers_All.html')
    logger.debug('select_Customers_query(): Exit')
    return render_template('customers_select_All.html',rows=rows,options=options)
#===============================================================================
   # NOTE: HARDCODE. TO REMOVE --------------------------------------------
def chk_c000001(*args,**kwargs):
    pass
    
from emtec.common.interface import *
from emtec.collector.db.orm_model          import Interface
from emtec.collector.db.flask_models       import interface
#-----------------------------------------------------------------------
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2020-02-20 16:44:35
# =============================================================================

# ======================================================================
#  Auto-Generated code. Do not modify 
#  (C) Sertechno/Emtec Group (2018,2019)
#  GLVH @ 2020-02-20 16:44:38.828747
# ======================================================================
        
# gen_views_form.html:AG 2020-02-20 16:44:38.828770
@main.route('/forms/CU_Types', methods=['GET', 'POST'])
@login_required

def forms_CU_Types():
    """ Form handling function for table CU_Types """
    logger.debug('forms_CU_Types(): Enter')
    Typ_Code  =  request.args.get('Typ_Code',0,type=int)
    
    row =  cu_type.query.filter(cu_type.Typ_Code == Typ_Code).first()
    if row is None:
        row=cu_type()
        session['is_new_row']=True
    session['data'] =  {  'Typ_Code':row.Typ_Code, 'Typ_Description':row.Typ_Description }
    
    form = frm_cu_type()
    
    # Actual Form activation here
    if form.validate_on_submit():
    # Code for SAVE option
        if form.submit_Save.data and current_user.role_id > 1:
    
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
                   message=Markup('<b>Configuration Unit Type Typ_Code saved OK</b>')
                   flash(message)
               db.session.close()
            except Exception as e:
               db.session.rollback()
               db.session.close()
               message=Markup('ERROR saving Configuration Unit Type record : %s'%(e))
               flash(message)
            return redirect(url_for('.select_CU_Types_query'))    
    # Code for NEW option
    # GV 20190109 f.write(        "        elif   form.submit_New.data:\n")
        elif   form.submit_New.data and current_user.role_id>1:
            #print('New Data Here ...')
            session['is_new_row']=True
            db.session.close()
            row=cu_type()
    
            return redirect(url_for('.forms_CU_Types'))    
    
    # Code for CANCEL option 
        elif   form.submit_Cancel.data:
            #print('Cancel Data Here ... does nothing')
            message=Markup('Configuration Unit Type Record modifications discarded ...')
            flash(message)
    # Code for ANY OTHER option should never get here
        else:
            #print('form validated but not submited ???')
            message=Markup("<b>Configuration Unit Type data modifications not allowed for user '%s'. Please contact EG Suite's Administrator ...</b>"%(current_user.username))    
            flash(message)
    
            return redirect(url_for('.forms_'))    
    
    
    form.Typ_Code.data = row.Typ_Code
    form.Typ_Description.data = row.Typ_Description
    session['prev_row'] = str(row)
    session['is_new_row'] = False
    logger.debug('forms_CU_Types(): Exit')
    # Generates pagination data here
    P=[]
    # Tab Relations = [{'name': 'charge_units', 'class': 'charge_unit', 'backref': 'cu_type', 'caption': 'Charge Units', 'table': 'Charge_Units'}, {'name': 'rates', 'class': 'rate', 'backref': 'cu_type', 'caption': 'Rates', 'table': 'Rates'}]
    
    from flask_sqlalchemy import Pagination
    # [{'name': 'charge_units', 'class': 'charge_unit', 'backref': 'cu_type', 'caption': 'Charge Units', 'table': 'Charge_Units'}, {'name': 'rates', 'class': 'rate', 'backref': 'cu_type', 'caption': 'Rates', 'table': 'Rates'}]
    P.append(({'name': 'charge_units', 'class': 'charge_unit', 'backref': 'cu_type', 'caption': 'Charge Units', 'table': 'Charge_Units'},row.charge_units.paginate()))
    P.append(({'name': 'rates', 'class': 'rate', 'backref': 'cu_type', 'caption': 'Rates', 'table': 'Rates'},row.rates.paginate()))
    
    """
    print("P=",P,type(P))
    for relation,p in P:
        print("relation=",relation)
        print("p.query=",p.query)
        print("p.has_next=",p.has_next,p.next,p.next_num)
        print("p.has_prev=",p.has_prev,p.prev,p.prev_num)
        print("p.pages=",p.pages)
        print("p.iter_pages=",p.iter_pages)
        print("p.per_page=",p.per_page)
        print("p.total=",p.total)
        print("p.items type=",type(p.items),len(p.items))
    """
    
    # Generation of pagination data completed       
    return render_template('cu_types.html', form=form, row=row, P=P)    
# ======================================================================



# ======================================================================
#  Auto-Generated code. Do not modify 
#  (C) Sertechno/Emtec Group (2018,2019)
#  GLVH @ 2020-02-20 16:44:38.852996
# ======================================================================
        
# gen_views_delete.html:AG 2020-02-20 16:44:38.853019
@main.route('/forms/CU_Types_delete', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@admin_required
def forms_CU_Types_delete():
    """ Delete record handling function for table CU_Types """
    logger.debug('forms_CU_Types_delete(): Enter')
    Typ_Code  =  request.args.get('Typ_Code',0,type=int)
    row =  cu_type.query.filter(cu_type.Typ_Code == Typ_Code).first()

    if row is None:
        row=cu_type()
    session['data'] =  {  'Typ_Code':row.Typ_Code, 'Typ_Description':row.Typ_Description }
                       
    form = frm_cu_type_delete()

    # Tab['has_fks'] False
    
            
    # Actual Form activation here
    if form.validate_on_submit():
    
    # Code for SAVE option
        if  form.submit_Delete.data:
            print('Delete Data Here...')

    
    #f.write(        "            print('Delete Data Here...')
            try:
                session['deleted_row']=str(row)
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                logger.audit ( '%s:DEL:%s' % (current_user.username,session['deleted_row']) )
                flash('Configuration Unit Type Typ_Code deleted OK')
            except exc.IntegrityError as e:
                db.session.rollback()    
                flash('INTEGRITY ERROR: Are you sure there are no dependant records in other tables?')
                return redirect(url_for('.forms_CU_Types_delete',Typ_Code=session['data']['Typ_Code']))    
    
            return redirect(url_for('.select_CU_Types_query'))    
    # Code for CANCEL option 
        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
            return redirect(url_for('.select_CU_Types_query'))    
    # Code for ANY OTHER option should never get here
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.select_CU_Types_query'))    
    
    logger.debug('forms_CU_Types_delete(): Exit')
    return render_template('cu_types_delete.html', form=form, data=session.get('data'),row=row)
#===============================================================================

# ======================================================================
#  Auto-Generated code. Do not modify 
#  (C) Sertechno/Emtec Group (2018,2019)
#  GLVH @ 2020-02-20 16:44:38.901706
# ======================================================================


from pprint import pprint, pformat

# gen_views_select_query.html:AG 2020-02-20 16:44:38.901730        
@main.route('/select/CU_Types_Query', methods=['GET','POST'])
@login_required
@admin_required
def select_CU_Types_query():
    """ Select rows handling function for table 'CU_Types' """
    logger.debug('select_CU_Types_query(): Enter')
    chk_c000001(filename=os.path.join(current_app.root_path, '.c000001'),request=request,db=db,logger=logger)
    # Get parameters from URL call
    ia       =  request.args.get('ia',     None,type=str)
    if ia is not None:
        ia=ia.split(',')
        if ia[0]=='ORDER':
            set_query_option(engine=db.engine,Interface=Interface,User_Id=current_user.id,Table_name='cu_type',Option_Type=OPTION_ORDER_BY,Argument_1=ia[1],Argument_2=ia[2])
        elif ia[0]=='GROUP':
            set_query_option(engine=db.engine,Interface=Interface,User_Id=current_user.id,Table_name='cu_type',Option_Type=OPTION_GROUP_BY,Argument_1=ia[1])
        elif ia[0]=='LIMIT':
            set_query_option(engine=db.engine,Interface=Interface,User_Id=current_user.id,Table_name='cu_type',Option_Type=OPTION_LIMIT,Argument_1=ia[1])

    iad      =  request.args.get('iad',     None,type=int)
    if iad is not None: delete_query_option(engine=db.engine,Interface=Interface,Id=iad) 
    
    field    =  request.args.get('field',   None,type=str)
    value    =  request.args.get('value',   None,type=str)
    
    # Populates a list of foreign keys used for advanced filtering
    # ------------------------------------------------------------------
    foreign_keys={}
    
    # ------------------------------------------------------------------
    
    if field is not None:
        reset_query_options(    engine=db.engine,Interface=Interface,
                                User_Id=current_user.id,
                                Table_name='cu_type'
                                )

        
        if field in foreign_keys.keys():
            Class,referenced_classname,referenced_Field,referenced_Value,column_Header=foreign_keys[field]
            foreign_field='%s.%s:%s'%(referenced_classname,referenced_Value,column_Header)
            foreign_record=Class.query.get(value)
            foreign_description="'%s'"%getattr(foreign_record,referenced_Value)
        set_query_option(   engine=db.engine,Interface=Interface,
                        User_Id=current_user.id,
                        Table_name='cu_type',
                        Option_Type=OPTION_FILTER,
                        Argument_1=foreign_field,
                        Argument_2='==',
                        Argument_3=foreign_description
                        )
    page     =  request.args.get('page',    1   ,type=int)
    addx     =  request.args.get('add.x',   None,type=int)
    addy     =  request.args.get('add.y',   None,type=int)
    exportx  =  request.args.get('export.x',None,type=int)
    exporty  =  request.args.get('export.y',None,type=int)
    filterx  =  request.args.get('filter.x',None,type=int)
    filtery  =  request.args.get('filter.y',None,type=int)
    # Select excluyent view mode
    if   addx    is not None: mode = 'add'
    elif exportx is not None: mode = 'export'
    elif filterx is not None: mode = 'filter'
    else:                     mode = 'select'
    Typ_Code =  request.args.get('Typ_Code',None,type=str)
    Typ_Description =  request.args.get('Typ_Description',None,type=str)
    
    
    # Build default query all fields from table
    
    if Typ_Code is not None and len(Typ_Code)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='cu_type',
                Option_Type=OPTION_FILTER,
                Argument_1='Typ_Code:Type',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Typ_Code
                )
    
    
    if Typ_Description is not None and len(Typ_Description)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='cu_type',
                Option_Type=OPTION_FILTER,
                Argument_1='Typ_Description:Description',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Typ_Description
                )
    
    
    
    statement_query,options=get_query_options(engine=db.engine,Interface=Interface,Table_name='cu_type',User_Id=current_user.id)
    query=eval(statement_query)
    filtered_query = query    
    if mode == 'filter':
        query=filtered_query
    elif mode == 'export':
        query=filtered_query
        fh,output_file = tempfile.mkstemp(suffix='', prefix='CU_Types_', dir=None, text=False)
        dict = {'header':{},'detail':[]}
        count = 0
        rows = query.all()
        for row in rows:
            dict['detail'].append({})
            for column in ['Typ_Code', 'Typ_Description']:
                dict['detail'][count].update( { column:str(row.__getattribute__(column))})
                
            count += 1
        dict['header'].update({'count':count})
        jsonarray      = json.dumps(dict)
        data           = json.loads(jsonarray)  
        dataframe      = json_normalize(data, 'detail').assign(**data['header'])
        fh,output_file = tempfile.mkstemp(suffix='', prefix='CU_Types_', dir='/tmp', text=False)
        xlsx_file      = '%s/%s'%(current_app.root_path,url_for('static',filename='%s.xls'%(output_file)))
        dataframe.to_excel(xlsx_file,sheet_name='CU_Types',columns=['Typ_Code', 'Typ_Description'])
        return send_file(xlsx_file,as_attachment=True,attachment_filename=output_file.replace('/','_')+'.xls')
    elif mode == 'add':
        return redirect(url_for('.forms_CU_Types'))
    elif mode == 'select':
        pass
        # if some filter is required
        if field is not None:
            if field == 'Typ_Code':
                if value is not None:
                    query = query.filter_by(Typ_Code=value)
            if field == 'Typ_Description':
                if value is not None:
                    query = query.filter_by(Typ_Description=value)
            
    # Actual request from DB follows
    tracebox_log(query,logger,length=50)
    rows = query.paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
    # Setting pagination variables ...
    if field is not None:
       next_url = url_for('.select_CU_Types_query', field=field, value=value, page=rows.next_num) if rows.has_next else None
       prev_url = url_for('.select_CU_Types_query', field=field, value=value, page=rows.prev_num) if rows.has_prev else None
    else:
       next_url = url_for('.select_CU_Types_query', page=rows.next_num) if rows.has_next else None
       prev_url = url_for('.select_CU_Types_query', page=rows.prev_num) if rows.has_prev else None
    # Actual rendering ...
    if request.headers.get('Content-Type') is not None or request.args.get('JSON',None,type=str) is not None:
        if "JSON" in request.headers.get('Content-Type') or request.args.get('JSON',None,type=str) is not None:
            logger.debug('select_CU_Types_query(): will render: JSON rows')
            logger.debug('select_CU_Types_query(): Exit')
            return json.dumps(serialize_object(rows.__dict__))
    logger.debug('select_CU_Types_query(): will render: cu_types_All.html')
    logger.debug('select_CU_Types_query(): Exit')
    return render_template('cu_types_select_All.html',rows=rows,options=options)
#===============================================================================
   # NOTE: HARDCODE. TO REMOVE --------------------------------------------
def chk_c000001(*args,**kwargs):
    pass
    
from emtec.common.interface import *
from emtec.collector.db.orm_model          import Interface
from emtec.collector.db.flask_models       import interface
#-----------------------------------------------------------------------
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2020-02-20 16:44:35
# =============================================================================

# ======================================================================
#  Auto-Generated code. Do not modify 
#  (C) Sertechno/Emtec Group (2018,2019)
#  GLVH @ 2020-02-20 16:44:42.854221
# ======================================================================
        
# gen_views_form.html:AG 2020-02-20 16:44:42.854245
@main.route('/forms/Exchange_Rates', methods=['GET', 'POST'])
@login_required

def forms_Exchange_Rates():
    """ Form handling function for table Exchange_Rates """
    logger.debug('forms_Exchange_Rates(): Enter')
    ER_Id  =  request.args.get('ER_Id',0,type=int)
    
    row =  exchange_rate.query.filter(exchange_rate.ER_Id == ER_Id).first()
    if row is None:
        row=exchange_rate()
        session['is_new_row']=True
    session['data'] =  {  'ER_Id':row.ER_Id, 'Cur_Code':row.Cur_Code, 'ER_Factor':row.ER_Factor, 'ER_Date':row.ER_Date }
    
    form = frm_exchange_rate()
    
    if form.has_FKs:
        form.Cur_Code.choices = db.session.query(currency.Cur_Code,currency.Cur_Name).order_by(currency.Cur_Name).all()

    
    # Actual Form activation here
    if form.validate_on_submit():
    # Code for SAVE option
        if form.submit_Save.data and current_user.role_id > 1:
    
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
                   message=Markup('<b>Exchange Rate ER_Id saved OK</b>')
                   flash(message)
               db.session.close()
            except Exception as e:
               db.session.rollback()
               db.session.close()
               message=Markup('ERROR saving Exchange Rate record : %s'%(e))
               flash(message)
            return redirect(url_for('.select_Exchange_Rates_query'))    
    # Code for NEW option
    # GV 20190109 f.write(        "        elif   form.submit_New.data:\n")
        elif   form.submit_New.data and current_user.role_id>1:
            #print('New Data Here ...')
            session['is_new_row']=True
            db.session.close()
            row=exchange_rate()
    
            return redirect(url_for('.forms_Exchange_Rates',ER_Id=row.ER_Id))
    
    # Code for CANCEL option 
        elif   form.submit_Cancel.data:
            #print('Cancel Data Here ... does nothing')
            message=Markup('Exchange Rate Record modifications discarded ...')
            flash(message)
    # Code for ANY OTHER option should never get here
        else:
            #print('form validated but not submited ???')
            message=Markup("<b>Exchange Rate data modifications not allowed for user '%s'. Please contact EG Suite's Administrator ...</b>"%(current_user.username))    
            flash(message)
    
            return redirect(url_for('.forms_Exchange_Rates',ER_Id=row.ER_Id))
    
    
    form.Cur_Code.data = row.Cur_Code
    form.ER_Factor.data = row.ER_Factor
    form.ER_Date.data = row.ER_Date
    session['prev_row'] = str(row)
    session['is_new_row'] = False
    logger.debug('forms_Exchange_Rates(): Exit')
    # Generates pagination data here
    P=[]
    # Tab Relations = []
    
    # Generation of pagination data completed       
    return render_template('exchange_rates.html', form=form, row=row, P=P)    
# ======================================================================



# ======================================================================
#  Auto-Generated code. Do not modify 
#  (C) Sertechno/Emtec Group (2018,2019)
#  GLVH @ 2020-02-20 16:44:42.877777
# ======================================================================
        
# gen_views_delete.html:AG 2020-02-20 16:44:42.877800
@main.route('/forms/Exchange_Rates_delete', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@admin_required
def forms_Exchange_Rates_delete():
    """ Delete record handling function for table Exchange_Rates """
    logger.debug('forms_Exchange_Rates_delete(): Enter')
    ER_Id  =  request.args.get('ER_Id',0,type=int)
    row =  exchange_rate.query.filter(exchange_rate.ER_Id == ER_Id).first()

    if row is None:
        row=exchange_rate()
    session['data'] =  {  'ER_Id':row.ER_Id, 'Cur_Code':row.Cur_Code, 'ER_Factor':row.ER_Factor, 'ER_Date':row.ER_Date }
                       
    form = frm_exchange_rate_delete()

    # Tab['has_fks'] True
    
    pass # Tab['has_fks'] True
    
            
    # Actual Form activation here
    if form.validate_on_submit():
    
    # Code for SAVE option
        if  form.submit_Delete.data:
            print('Delete Data Here...')

    
    #f.write(        "            print('Delete Data Here...')
            try:
                session['deleted_row']=str(row)
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                logger.audit ( '%s:DEL:%s' % (current_user.username,session['deleted_row']) )
                flash('Exchange Rate ER_Id deleted OK')
            except exc.IntegrityError as e:
                db.session.rollback()    
                flash('INTEGRITY ERROR: Are you sure there are no dependant records in other tables?')
                return redirect(url_for('.forms_Exchange_Rates_delete',ER_Id=session['data']['ER_Id']))    
    
            return redirect(url_for('.select_Exchange_Rates_query'))    
    # Code for CANCEL option 
        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
            return redirect(url_for('.select_Exchange_Rates_query'))    
    # Code for ANY OTHER option should never get here
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.select_Exchange_Rates_query'))    
    
    logger.debug('forms_Exchange_Rates_delete(): Exit')
    return render_template('exchange_rates_delete.html', form=form, data=session.get('data'),row=row)
#===============================================================================

# ======================================================================
#  Auto-Generated code. Do not modify 
#  (C) Sertechno/Emtec Group (2018,2019)
#  GLVH @ 2020-02-20 16:44:42.928506
# ======================================================================


from pprint import pprint, pformat

# gen_views_select_query.html:AG 2020-02-20 16:44:42.928531        
@main.route('/select/Exchange_Rates_Query', methods=['GET','POST'])
@login_required
@admin_required
def select_Exchange_Rates_query():
    """ Select rows handling function for table 'Exchange_Rates' """
    logger.debug('select_Exchange_Rates_query(): Enter')
    chk_c000001(filename=os.path.join(current_app.root_path, '.c000001'),request=request,db=db,logger=logger)
    # Get parameters from URL call
    ia       =  request.args.get('ia',     None,type=str)
    if ia is not None:
        ia=ia.split(',')
        if ia[0]=='ORDER':
            set_query_option(engine=db.engine,Interface=Interface,User_Id=current_user.id,Table_name='exchange_rate',Option_Type=OPTION_ORDER_BY,Argument_1=ia[1],Argument_2=ia[2])
        elif ia[0]=='GROUP':
            set_query_option(engine=db.engine,Interface=Interface,User_Id=current_user.id,Table_name='exchange_rate',Option_Type=OPTION_GROUP_BY,Argument_1=ia[1])
        elif ia[0]=='LIMIT':
            set_query_option(engine=db.engine,Interface=Interface,User_Id=current_user.id,Table_name='exchange_rate',Option_Type=OPTION_LIMIT,Argument_1=ia[1])

    iad      =  request.args.get('iad',     None,type=int)
    if iad is not None: delete_query_option(engine=db.engine,Interface=Interface,Id=iad) 
    
    field    =  request.args.get('field',   None,type=str)
    value    =  request.args.get('value',   None,type=str)
    
    # Populates a list of foreign keys used for advanced filtering
    # ------------------------------------------------------------------
    foreign_keys={}
    
    foreign_keys.update({'Cur_Code':(currency,'currency','Cur_Code','Cur_Name','Currency Code')})
    # ------------------------------------------------------------------
    
    if field is not None:
        reset_query_options(    engine=db.engine,Interface=Interface,
                                User_Id=current_user.id,
                                Table_name='exchange_rate'
                                )

        
        if field in foreign_keys.keys():
            Class,referenced_classname,referenced_Field,referenced_Value,column_Header=foreign_keys[field]
            foreign_field='%s.%s:%s'%(referenced_classname,referenced_Value,column_Header)
            foreign_record=Class.query.get(value)
            foreign_description="'%s'"%getattr(foreign_record,referenced_Value)
        set_query_option(   engine=db.engine,Interface=Interface,
                        User_Id=current_user.id,
                        Table_name='exchange_rate',
                        Option_Type=OPTION_FILTER,
                        Argument_1=foreign_field,
                        Argument_2='==',
                        Argument_3=foreign_description
                        )
    page     =  request.args.get('page',    1   ,type=int)
    addx     =  request.args.get('add.x',   None,type=int)
    addy     =  request.args.get('add.y',   None,type=int)
    exportx  =  request.args.get('export.x',None,type=int)
    exporty  =  request.args.get('export.y',None,type=int)
    filterx  =  request.args.get('filter.x',None,type=int)
    filtery  =  request.args.get('filter.y',None,type=int)
    # Select excluyent view mode
    if   addx    is not None: mode = 'add'
    elif exportx is not None: mode = 'export'
    elif filterx is not None: mode = 'filter'
    else:                     mode = 'select'
    ER_Id =  request.args.get('ER_Id',None,type=str)
    Cur_Code =  request.args.get('Cur_Code',None,type=str)
    ER_Factor =  request.args.get('ER_Factor',None,type=str)
    ER_Date =  request.args.get('ER_Date',None,type=str)
    
    
    # Build default query all fields from table
    
    if ER_Id is not None and len(ER_Id)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='exchange_rate',
                Option_Type=OPTION_FILTER,
                Argument_1='ER_Id:Id',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%ER_Id
                )
    
    
    if Cur_Code is not None and len(Cur_Code)>0:
            Class,referenced_classname,referenced_Field,referenced_Value,column_Header=foreign_keys['Cur_Code']
            foreign_field='%s.%s:%s'%(referenced_classname,referenced_Value,column_Header)            
            set_query_option(   engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='exchange_rate',
                Option_Type=OPTION_FILTER,
                Argument_1=foreign_field,
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Cur_Code
                )
                                
    
    
    if ER_Factor is not None and len(ER_Factor)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='exchange_rate',
                Option_Type=OPTION_FILTER,
                Argument_1='ER_Factor:Factor',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%ER_Factor
                )
    
    
    if ER_Date is not None and len(ER_Date)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='exchange_rate',
                Option_Type=OPTION_FILTER,
                Argument_1='ER_Date:Date',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%ER_Date
                )
    
    
    
    statement_query,options=get_query_options(engine=db.engine,Interface=Interface,Table_name='exchange_rate',User_Id=current_user.id)
    query=eval(statement_query)
    filtered_query = query    
    if mode == 'filter':
        query=filtered_query
    elif mode == 'export':
        query=filtered_query
        fh,output_file = tempfile.mkstemp(suffix='', prefix='Exchange_Rates_', dir=None, text=False)
        dict = {'header':{},'detail':[]}
        count = 0
        rows = query.all()
        for row in rows:
            dict['detail'].append({})
            for column in ['ER_Id', 'Cur_Code', 'ER_Factor', 'ER_Date']:
                dict['detail'][count].update( { column:str(row.__getattribute__(column))})
                
            count += 1
        dict['header'].update({'count':count})
        jsonarray      = json.dumps(dict)
        data           = json.loads(jsonarray)  
        dataframe      = json_normalize(data, 'detail').assign(**data['header'])
        fh,output_file = tempfile.mkstemp(suffix='', prefix='Exchange_Rates_', dir='/tmp', text=False)
        xlsx_file      = '%s/%s'%(current_app.root_path,url_for('static',filename='%s.xls'%(output_file)))
        dataframe.to_excel(xlsx_file,sheet_name='Exchange_Rates',columns=['ER_Id', 'Cur_Code', 'ER_Factor', 'ER_Date'])
        return send_file(xlsx_file,as_attachment=True,attachment_filename=output_file.replace('/','_')+'.xls')
    elif mode == 'add':
        return redirect(url_for('.forms_Exchange_Rates'))
    elif mode == 'select':
        pass
        # if some filter is required
        if field is not None:
            if field == 'ER_Id':
                if value is not None:
                    query = query.filter_by(ER_Id=value)
            if field == 'Cur_Code':
                if value is not None:
                    query = query.filter_by(Cur_Code=value)
            if field == 'ER_Factor':
                if value is not None:
                    query = query.filter_by(ER_Factor=value)
            if field == 'ER_Date':
                if value is not None:
                    query = query.filter_by(ER_Date=value)
            # JOIN other tables and generate foreign fields
    query = query.join(currency,exchange_rate.Cur_Code == currency.Cur_Code).add_columns(currency.Cur_Name)
    
    # Actual request from DB follows
    tracebox_log(query,logger,length=50)
    rows = query.paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
    # Setting pagination variables ...
    if field is not None:
       next_url = url_for('.select_Exchange_Rates_query', field=field, value=value, page=rows.next_num) if rows.has_next else None
       prev_url = url_for('.select_Exchange_Rates_query', field=field, value=value, page=rows.prev_num) if rows.has_prev else None
    else:
       next_url = url_for('.select_Exchange_Rates_query', page=rows.next_num) if rows.has_next else None
       prev_url = url_for('.select_Exchange_Rates_query', page=rows.prev_num) if rows.has_prev else None
    # Actual rendering ...
    if request.headers.get('Content-Type') is not None or request.args.get('JSON',None,type=str) is not None:
        if "JSON" in request.headers.get('Content-Type') or request.args.get('JSON',None,type=str) is not None:
            logger.debug('select_Exchange_Rates_query(): will render: JSON rows')
            logger.debug('select_Exchange_Rates_query(): Exit')
            return json.dumps(serialize_object(rows.__dict__))
    logger.debug('select_Exchange_Rates_query(): will render: exchange_rates_All.html')
    logger.debug('select_Exchange_Rates_query(): Exit')
    return render_template('exchange_rates_select_All.html',rows=rows,options=options)
#===============================================================================
   # NOTE: HARDCODE. TO REMOVE --------------------------------------------
def chk_c000001(*args,**kwargs):
    pass
    
from emtec.common.interface import *
from emtec.collector.db.orm_model          import Interface
from emtec.collector.db.flask_models       import interface
#-----------------------------------------------------------------------
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2020-02-20 16:44:35
# =============================================================================

# ======================================================================
#  Auto-Generated code. Do not modify 
#  (C) Sertechno/Emtec Group (2018,2019)
#  GLVH @ 2020-02-20 16:44:43.221242
# ======================================================================
        
# gen_views_form.html:AG 2020-02-20 16:44:43.221265
@main.route('/forms/Interface', methods=['GET', 'POST'])
@login_required

def forms_Interface():
    """ Form handling function for table Interface """
    logger.debug('forms_Interface(): Enter')
    Id  =  request.args.get('Id',0,type=int)
    
    row =  interface.query.filter(interface.Id == Id).first()
    if row is None:
        row=interface()
        session['is_new_row']=True
    session['data'] =  {  'Id':row.Id, 'User_Id':row.User_Id, 'Table_name':row.Table_name, 'Option_Type':row.Option_Type, 'Argument_1':row.Argument_1, 'Argument_2':row.Argument_2, 'Argument_3':row.Argument_3, 'Is_Active':row.Is_Active }
    
    form = frm_interface()
    
    # Actual Form activation here
    if form.validate_on_submit():
    # Code for SAVE option
        if form.submit_Save.data and current_user.role_id > 1:
    
            row.User_Id = form.User_Id.data
            row.Table_name = form.Table_name.data
            row.Option_Type = form.Option_Type.data
            row.Argument_1 = form.Argument_1.data
            row.Argument_2 = form.Argument_2.data
            row.Argument_3 = form.Argument_3.data
            row.Is_Active = form.Is_Active.data  
            try:
               session['new_row']=str(row)
               db.session.close()
               db.session.add(row)
               db.session.commit()
               if session['is_new_row']==True:
                   logger.audit ( '%s:NEW:%s' % (current_user.username,session['new_row'] ) )
                   flash('New Interface created OK')
               else:
                   logger.audit ( '%s:OLD:%s' % (current_user.username,session['prev_row']) )
                   logger.audit ( '%s:UPD:%s' % (current_user.username,session['new_row'] ) )    
                   message=Markup('<b>Interface Id saved OK</b>')
                   flash(message)
               db.session.close()
            except Exception as e:
               db.session.rollback()
               db.session.close()
               message=Markup('ERROR saving Interface record : %s'%(e))
               flash(message)
            return redirect(url_for('.select_Interface_query'))    
    # Code for NEW option
    # GV 20190109 f.write(        "        elif   form.submit_New.data:\n")
        elif   form.submit_New.data and current_user.role_id>1:
            #print('New Data Here ...')
            session['is_new_row']=True
            db.session.close()
            row=interface()
    
            return redirect(url_for('.forms_Interface',Id=row.Id))
    
    # Code for CANCEL option 
        elif   form.submit_Cancel.data:
            #print('Cancel Data Here ... does nothing')
            message=Markup('Interface Record modifications discarded ...')
            flash(message)
    # Code for ANY OTHER option should never get here
        else:
            #print('form validated but not submited ???')
            message=Markup("<b>Interface data modifications not allowed for user '%s'. Please contact EG Suite's Administrator ...</b>"%(current_user.username))    
            flash(message)
    
            return redirect(url_for('.forms_Interface',Id=row.Id))
    
    
    form.User_Id.data = row.User_Id
    form.Table_name.data = row.Table_name
    form.Option_Type.data = row.Option_Type
    form.Argument_1.data = row.Argument_1
    form.Argument_2.data = row.Argument_2
    form.Argument_3.data = row.Argument_3
    form.Is_Active.data = row.Is_Active
    session['prev_row'] = str(row)
    session['is_new_row'] = False
    logger.debug('forms_Interface(): Exit')
    # Generates pagination data here
    P=[]
    # Tab Relations = []
    
    # Generation of pagination data completed       
    return render_template('interface.html', form=form, row=row, P=P)    
# ======================================================================



# ======================================================================
#  Auto-Generated code. Do not modify 
#  (C) Sertechno/Emtec Group (2018,2019)
#  GLVH @ 2020-02-20 16:44:43.244928
# ======================================================================
        
# gen_views_delete.html:AG 2020-02-20 16:44:43.244951
@main.route('/forms/Interface_delete', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@admin_required
def forms_Interface_delete():
    """ Delete record handling function for table Interface """
    logger.debug('forms_Interface_delete(): Enter')
    Id  =  request.args.get('Id',0,type=int)
    row =  interface.query.filter(interface.Id == Id).first()

    if row is None:
        row=interface()
    session['data'] =  {  'Id':row.Id, 'User_Id':row.User_Id, 'Table_name':row.Table_name, 'Option_Type':row.Option_Type, 'Argument_1':row.Argument_1, 'Argument_2':row.Argument_2, 'Argument_3':row.Argument_3, 'Is_Active':row.Is_Active }
                       
    form = frm_interface_delete()

    # Tab['has_fks'] False
    
            
    # Actual Form activation here
    if form.validate_on_submit():
    
    # Code for SAVE option
        if  form.submit_Delete.data:
            print('Delete Data Here...')

    
    #f.write(        "            print('Delete Data Here...')
            try:
                session['deleted_row']=str(row)
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                logger.audit ( '%s:DEL:%s' % (current_user.username,session['deleted_row']) )
                flash('Interface Id deleted OK')
            except exc.IntegrityError as e:
                db.session.rollback()    
                flash('INTEGRITY ERROR: Are you sure there are no dependant records in other tables?')
                return redirect(url_for('.forms_Interface_delete',Id=session['data']['Id']))    
    
            return redirect(url_for('.select_Interface_query'))    
    # Code for CANCEL option 
        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
            return redirect(url_for('.select_Interface_query'))    
    # Code for ANY OTHER option should never get here
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.select_Interface_query'))    
    
    logger.debug('forms_Interface_delete(): Exit')
    return render_template('interface_delete.html', form=form, data=session.get('data'),row=row)
#===============================================================================

# ======================================================================
#  Auto-Generated code. Do not modify 
#  (C) Sertechno/Emtec Group (2018,2019)
#  GLVH @ 2020-02-20 16:44:43.293857
# ======================================================================


from pprint import pprint, pformat

# gen_views_select_query.html:AG 2020-02-20 16:44:43.293880        
@main.route('/select/Interface_Query', methods=['GET','POST'])
@login_required
@admin_required
def select_Interface_query():
    """ Select rows handling function for table 'Interface' """
    logger.debug('select_Interface_query(): Enter')
    chk_c000001(filename=os.path.join(current_app.root_path, '.c000001'),request=request,db=db,logger=logger)
    # Get parameters from URL call
    ia       =  request.args.get('ia',     None,type=str)
    if ia is not None:
        ia=ia.split(',')
        if ia[0]=='ORDER':
            set_query_option(engine=db.engine,Interface=Interface,User_Id=current_user.id,Table_name='interface',Option_Type=OPTION_ORDER_BY,Argument_1=ia[1],Argument_2=ia[2])
        elif ia[0]=='GROUP':
            set_query_option(engine=db.engine,Interface=Interface,User_Id=current_user.id,Table_name='interface',Option_Type=OPTION_GROUP_BY,Argument_1=ia[1])
        elif ia[0]=='LIMIT':
            set_query_option(engine=db.engine,Interface=Interface,User_Id=current_user.id,Table_name='interface',Option_Type=OPTION_LIMIT,Argument_1=ia[1])

    iad      =  request.args.get('iad',     None,type=int)
    if iad is not None: delete_query_option(engine=db.engine,Interface=Interface,Id=iad) 
    
    field    =  request.args.get('field',   None,type=str)
    value    =  request.args.get('value',   None,type=str)
    
    # Populates a list of foreign keys used for advanced filtering
    # ------------------------------------------------------------------
    foreign_keys={}
    
    # ------------------------------------------------------------------
    
    if field is not None:
        reset_query_options(    engine=db.engine,Interface=Interface,
                                User_Id=current_user.id,
                                Table_name='interface'
                                )

        
        if field in foreign_keys.keys():
            Class,referenced_classname,referenced_Field,referenced_Value,column_Header=foreign_keys[field]
            foreign_field='%s.%s:%s'%(referenced_classname,referenced_Value,column_Header)
            foreign_record=Class.query.get(value)
            foreign_description="'%s'"%getattr(foreign_record,referenced_Value)
        set_query_option(   engine=db.engine,Interface=Interface,
                        User_Id=current_user.id,
                        Table_name='interface',
                        Option_Type=OPTION_FILTER,
                        Argument_1=foreign_field,
                        Argument_2='==',
                        Argument_3=foreign_description
                        )
    page     =  request.args.get('page',    1   ,type=int)
    addx     =  request.args.get('add.x',   None,type=int)
    addy     =  request.args.get('add.y',   None,type=int)
    exportx  =  request.args.get('export.x',None,type=int)
    exporty  =  request.args.get('export.y',None,type=int)
    filterx  =  request.args.get('filter.x',None,type=int)
    filtery  =  request.args.get('filter.y',None,type=int)
    # Select excluyent view mode
    if   addx    is not None: mode = 'add'
    elif exportx is not None: mode = 'export'
    elif filterx is not None: mode = 'filter'
    else:                     mode = 'select'
    Id =  request.args.get('Id',None,type=str)
    User_Id =  request.args.get('User_Id',None,type=str)
    Table_name =  request.args.get('Table_name',None,type=str)
    Option_Type =  request.args.get('Option_Type',None,type=str)
    Argument_1 =  request.args.get('Argument_1',None,type=str)
    Argument_2 =  request.args.get('Argument_2',None,type=str)
    Argument_3 =  request.args.get('Argument_3',None,type=str)
    Is_Active =  request.args.get('Is_Active',None,type=str)
    
    
    # Build default query all fields from table
    
    if Id is not None and len(Id)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='interface',
                Option_Type=OPTION_FILTER,
                Argument_1='Id:Id',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Id
                )
    
    
    if User_Id is not None and len(User_Id)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='interface',
                Option_Type=OPTION_FILTER,
                Argument_1='User_Id:User_Id',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%User_Id
                )
    
    
    if Table_name is not None and len(Table_name)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='interface',
                Option_Type=OPTION_FILTER,
                Argument_1='Table_name:Table_name',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Table_name
                )
    
    
    if Option_Type is not None and len(Option_Type)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='interface',
                Option_Type=OPTION_FILTER,
                Argument_1='Option_Type:Option_Type',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Option_Type
                )
    
    
    if Argument_1 is not None and len(Argument_1)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='interface',
                Option_Type=OPTION_FILTER,
                Argument_1='Argument_1:Argument_1',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Argument_1
                )
    
    
    if Argument_2 is not None and len(Argument_2)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='interface',
                Option_Type=OPTION_FILTER,
                Argument_1='Argument_2:Argument_2',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Argument_2
                )
    
    
    if Argument_3 is not None and len(Argument_3)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='interface',
                Option_Type=OPTION_FILTER,
                Argument_1='Argument_3:Argument_3',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Argument_3
                )
    
    
    if Is_Active is not None and len(Is_Active)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='interface',
                Option_Type=OPTION_FILTER,
                Argument_1='Is_Active:Is_Active',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Is_Active
                )
    
    
    
    statement_query,options=get_query_options(engine=db.engine,Interface=Interface,Table_name='interface',User_Id=current_user.id)
    query=eval(statement_query)
    filtered_query = query    
    if mode == 'filter':
        query=filtered_query
    elif mode == 'export':
        query=filtered_query
        fh,output_file = tempfile.mkstemp(suffix='', prefix='Interface_', dir=None, text=False)
        dict = {'header':{},'detail':[]}
        count = 0
        rows = query.all()
        for row in rows:
            dict['detail'].append({})
            for column in ['Id', 'User_Id', 'Table_name', 'Option_Type', 'Argument_1', 'Argument_2', 'Argument_3', 'Is_Active']:
                dict['detail'][count].update( { column:str(row.__getattribute__(column))})
                
            count += 1
        dict['header'].update({'count':count})
        jsonarray      = json.dumps(dict)
        data           = json.loads(jsonarray)  
        dataframe      = json_normalize(data, 'detail').assign(**data['header'])
        fh,output_file = tempfile.mkstemp(suffix='', prefix='Interface_', dir='/tmp', text=False)
        xlsx_file      = '%s/%s'%(current_app.root_path,url_for('static',filename='%s.xls'%(output_file)))
        dataframe.to_excel(xlsx_file,sheet_name='Interface',columns=['Id', 'User_Id', 'Table_name', 'Option_Type', 'Argument_1', 'Argument_2', 'Argument_3', 'Is_Active'])
        return send_file(xlsx_file,as_attachment=True,attachment_filename=output_file.replace('/','_')+'.xls')
    elif mode == 'add':
        return redirect(url_for('.forms_Interface'))
    elif mode == 'select':
        pass
        # if some filter is required
        if field is not None:
            if field == 'Id':
                if value is not None:
                    query = query.filter_by(Id=value)
            if field == 'User_Id':
                if value is not None:
                    query = query.filter_by(User_Id=value)
            if field == 'Table_name':
                if value is not None:
                    query = query.filter_by(Table_name=value)
            if field == 'Option_Type':
                if value is not None:
                    query = query.filter_by(Option_Type=value)
            if field == 'Argument_1':
                if value is not None:
                    query = query.filter_by(Argument_1=value)
            if field == 'Argument_2':
                if value is not None:
                    query = query.filter_by(Argument_2=value)
            if field == 'Argument_3':
                if value is not None:
                    query = query.filter_by(Argument_3=value)
            if field == 'Is_Active':
                if value is not None:
                    query = query.filter_by(Is_Active=value)
            
    # Actual request from DB follows
    tracebox_log(query,logger,length=50)
    rows = query.paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
    # Setting pagination variables ...
    if field is not None:
       next_url = url_for('.select_Interface_query', field=field, value=value, page=rows.next_num) if rows.has_next else None
       prev_url = url_for('.select_Interface_query', field=field, value=value, page=rows.prev_num) if rows.has_prev else None
    else:
       next_url = url_for('.select_Interface_query', page=rows.next_num) if rows.has_next else None
       prev_url = url_for('.select_Interface_query', page=rows.prev_num) if rows.has_prev else None
    # Actual rendering ...
    if request.headers.get('Content-Type') is not None or request.args.get('JSON',None,type=str) is not None:
        if "JSON" in request.headers.get('Content-Type') or request.args.get('JSON',None,type=str) is not None:
            logger.debug('select_Interface_query(): will render: JSON rows')
            logger.debug('select_Interface_query(): Exit')
            return json.dumps(serialize_object(rows.__dict__))
    logger.debug('select_Interface_query(): will render: interface_All.html')
    logger.debug('select_Interface_query(): Exit')
    return render_template('interface_select_All.html',rows=rows,options=options)
#===============================================================================
   # NOTE: HARDCODE. TO REMOVE --------------------------------------------
def chk_c000001(*args,**kwargs):
    pass
    
from emtec.common.interface import *
from emtec.collector.db.orm_model          import Interface
from emtec.collector.db.flask_models       import interface
#-----------------------------------------------------------------------
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2020-02-20 16:44:35
# =============================================================================

# ======================================================================
#  Auto-Generated code. Do not modify 
#  (C) Sertechno/Emtec Group (2018,2019)
#  GLVH @ 2020-02-20 16:44:43.543705
# ======================================================================
        
# gen_views_form.html:AG 2020-02-20 16:44:43.543737
@main.route('/forms/Measure_Units', methods=['GET', 'POST'])
@login_required

def forms_Measure_Units():
    """ Form handling function for table Measure_Units """
    logger.debug('forms_Measure_Units(): Enter')
    MU_Code  =  request.args.get('MU_Code',0,type=int)
    
    row =  measure_unit.query.filter(measure_unit.MU_Code == MU_Code).first()
    if row is None:
        row=measure_unit()
        session['is_new_row']=True
    session['data'] =  {  'MU_Code':row.MU_Code, 'MU_Description':row.MU_Description }
    
    form = frm_measure_unit()
    
    # Actual Form activation here
    if form.validate_on_submit():
    # Code for SAVE option
        if form.submit_Save.data and current_user.role_id > 1:
    
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
                   message=Markup('<b>Measure Unit MU_Code saved OK</b>')
                   flash(message)
               db.session.close()
            except Exception as e:
               db.session.rollback()
               db.session.close()
               message=Markup('ERROR saving Measure Unit record : %s'%(e))
               flash(message)
            return redirect(url_for('.select_Measure_Units_query'))    
    # Code for NEW option
    # GV 20190109 f.write(        "        elif   form.submit_New.data:\n")
        elif   form.submit_New.data and current_user.role_id>1:
            #print('New Data Here ...')
            session['is_new_row']=True
            db.session.close()
            row=measure_unit()
    
            return redirect(url_for('.forms_Measure_Units'))    
    
    # Code for CANCEL option 
        elif   form.submit_Cancel.data:
            #print('Cancel Data Here ... does nothing')
            message=Markup('Measure Unit Record modifications discarded ...')
            flash(message)
    # Code for ANY OTHER option should never get here
        else:
            #print('form validated but not submited ???')
            message=Markup("<b>Measure Unit data modifications not allowed for user '%s'. Please contact EG Suite's Administrator ...</b>"%(current_user.username))    
            flash(message)
    
            return redirect(url_for('.forms_'))    
    
    
    form.MU_Code.data = row.MU_Code
    form.MU_Description.data = row.MU_Description
    session['prev_row'] = str(row)
    session['is_new_row'] = False
    logger.debug('forms_Measure_Units(): Exit')
    # Generates pagination data here
    P=[]
    # Tab Relations = [{'name': 'rates', 'class': 'rate', 'backref': 'measure_unit', 'caption': 'Rates', 'table': 'Rates'}]
    
    from flask_sqlalchemy import Pagination
    # [{'name': 'rates', 'class': 'rate', 'backref': 'measure_unit', 'caption': 'Rates', 'table': 'Rates'}]
    P.append(({'name': 'rates', 'class': 'rate', 'backref': 'measure_unit', 'caption': 'Rates', 'table': 'Rates'},row.rates.paginate()))
    
    """
    print("P=",P,type(P))
    for relation,p in P:
        print("relation=",relation)
        print("p.query=",p.query)
        print("p.has_next=",p.has_next,p.next,p.next_num)
        print("p.has_prev=",p.has_prev,p.prev,p.prev_num)
        print("p.pages=",p.pages)
        print("p.iter_pages=",p.iter_pages)
        print("p.per_page=",p.per_page)
        print("p.total=",p.total)
        print("p.items type=",type(p.items),len(p.items))
    """
    
    # Generation of pagination data completed       
    return render_template('measure_units.html', form=form, row=row, P=P)    
# ======================================================================



# ======================================================================
#  Auto-Generated code. Do not modify 
#  (C) Sertechno/Emtec Group (2018,2019)
#  GLVH @ 2020-02-20 16:44:43.570926
# ======================================================================
        
# gen_views_delete.html:AG 2020-02-20 16:44:43.571003
@main.route('/forms/Measure_Units_delete', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@admin_required
def forms_Measure_Units_delete():
    """ Delete record handling function for table Measure_Units """
    logger.debug('forms_Measure_Units_delete(): Enter')
    MU_Code  =  request.args.get('MU_Code',0,type=int)
    row =  measure_unit.query.filter(measure_unit.MU_Code == MU_Code).first()

    if row is None:
        row=measure_unit()
    session['data'] =  {  'MU_Code':row.MU_Code, 'MU_Description':row.MU_Description }
                       
    form = frm_measure_unit_delete()

    # Tab['has_fks'] False
    
            
    # Actual Form activation here
    if form.validate_on_submit():
    
    # Code for SAVE option
        if  form.submit_Delete.data:
            print('Delete Data Here...')

    
    #f.write(        "            print('Delete Data Here...')
            try:
                session['deleted_row']=str(row)
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                logger.audit ( '%s:DEL:%s' % (current_user.username,session['deleted_row']) )
                flash('Measure Unit MU_Code deleted OK')
            except exc.IntegrityError as e:
                db.session.rollback()    
                flash('INTEGRITY ERROR: Are you sure there are no dependant records in other tables?')
                return redirect(url_for('.forms_Measure_Units_delete',MU_Code=session['data']['MU_Code']))    
    
            return redirect(url_for('.select_Measure_Units_query'))    
    # Code for CANCEL option 
        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
            return redirect(url_for('.select_Measure_Units_query'))    
    # Code for ANY OTHER option should never get here
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.select_Measure_Units_query'))    
    
    logger.debug('forms_Measure_Units_delete(): Exit')
    return render_template('measure_units_delete.html', form=form, data=session.get('data'),row=row)
#===============================================================================

# ======================================================================
#  Auto-Generated code. Do not modify 
#  (C) Sertechno/Emtec Group (2018,2019)
#  GLVH @ 2020-02-20 16:44:43.618902
# ======================================================================


from pprint import pprint, pformat

# gen_views_select_query.html:AG 2020-02-20 16:44:43.618926        
@main.route('/select/Measure_Units_Query', methods=['GET','POST'])
@login_required
@admin_required
def select_Measure_Units_query():
    """ Select rows handling function for table 'Measure_Units' """
    logger.debug('select_Measure_Units_query(): Enter')
    chk_c000001(filename=os.path.join(current_app.root_path, '.c000001'),request=request,db=db,logger=logger)
    # Get parameters from URL call
    ia       =  request.args.get('ia',     None,type=str)
    if ia is not None:
        ia=ia.split(',')
        if ia[0]=='ORDER':
            set_query_option(engine=db.engine,Interface=Interface,User_Id=current_user.id,Table_name='measure_unit',Option_Type=OPTION_ORDER_BY,Argument_1=ia[1],Argument_2=ia[2])
        elif ia[0]=='GROUP':
            set_query_option(engine=db.engine,Interface=Interface,User_Id=current_user.id,Table_name='measure_unit',Option_Type=OPTION_GROUP_BY,Argument_1=ia[1])
        elif ia[0]=='LIMIT':
            set_query_option(engine=db.engine,Interface=Interface,User_Id=current_user.id,Table_name='measure_unit',Option_Type=OPTION_LIMIT,Argument_1=ia[1])

    iad      =  request.args.get('iad',     None,type=int)
    if iad is not None: delete_query_option(engine=db.engine,Interface=Interface,Id=iad) 
    
    field    =  request.args.get('field',   None,type=str)
    value    =  request.args.get('value',   None,type=str)
    
    # Populates a list of foreign keys used for advanced filtering
    # ------------------------------------------------------------------
    foreign_keys={}
    
    # ------------------------------------------------------------------
    
    if field is not None:
        reset_query_options(    engine=db.engine,Interface=Interface,
                                User_Id=current_user.id,
                                Table_name='measure_unit'
                                )

        
        if field in foreign_keys.keys():
            Class,referenced_classname,referenced_Field,referenced_Value,column_Header=foreign_keys[field]
            foreign_field='%s.%s:%s'%(referenced_classname,referenced_Value,column_Header)
            foreign_record=Class.query.get(value)
            foreign_description="'%s'"%getattr(foreign_record,referenced_Value)
        set_query_option(   engine=db.engine,Interface=Interface,
                        User_Id=current_user.id,
                        Table_name='measure_unit',
                        Option_Type=OPTION_FILTER,
                        Argument_1=foreign_field,
                        Argument_2='==',
                        Argument_3=foreign_description
                        )
    page     =  request.args.get('page',    1   ,type=int)
    addx     =  request.args.get('add.x',   None,type=int)
    addy     =  request.args.get('add.y',   None,type=int)
    exportx  =  request.args.get('export.x',None,type=int)
    exporty  =  request.args.get('export.y',None,type=int)
    filterx  =  request.args.get('filter.x',None,type=int)
    filtery  =  request.args.get('filter.y',None,type=int)
    # Select excluyent view mode
    if   addx    is not None: mode = 'add'
    elif exportx is not None: mode = 'export'
    elif filterx is not None: mode = 'filter'
    else:                     mode = 'select'
    MU_Code =  request.args.get('MU_Code',None,type=str)
    MU_Description =  request.args.get('MU_Description',None,type=str)
    
    
    # Build default query all fields from table
    
    if MU_Code is not None and len(MU_Code)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='measure_unit',
                Option_Type=OPTION_FILTER,
                Argument_1='MU_Code:Code',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%MU_Code
                )
    
    
    if MU_Description is not None and len(MU_Description)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='measure_unit',
                Option_Type=OPTION_FILTER,
                Argument_1='MU_Description:Description',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%MU_Description
                )
    
    
    
    statement_query,options=get_query_options(engine=db.engine,Interface=Interface,Table_name='measure_unit',User_Id=current_user.id)
    query=eval(statement_query)
    filtered_query = query    
    if mode == 'filter':
        query=filtered_query
    elif mode == 'export':
        query=filtered_query
        fh,output_file = tempfile.mkstemp(suffix='', prefix='Measure_Units_', dir=None, text=False)
        dict = {'header':{},'detail':[]}
        count = 0
        rows = query.all()
        for row in rows:
            dict['detail'].append({})
            for column in ['MU_Code', 'MU_Description']:
                dict['detail'][count].update( { column:str(row.__getattribute__(column))})
                
            count += 1
        dict['header'].update({'count':count})
        jsonarray      = json.dumps(dict)
        data           = json.loads(jsonarray)  
        dataframe      = json_normalize(data, 'detail').assign(**data['header'])
        fh,output_file = tempfile.mkstemp(suffix='', prefix='Measure_Units_', dir='/tmp', text=False)
        xlsx_file      = '%s/%s'%(current_app.root_path,url_for('static',filename='%s.xls'%(output_file)))
        dataframe.to_excel(xlsx_file,sheet_name='Measure_Units',columns=['MU_Code', 'MU_Description'])
        return send_file(xlsx_file,as_attachment=True,attachment_filename=output_file.replace('/','_')+'.xls')
    elif mode == 'add':
        return redirect(url_for('.forms_Measure_Units'))
    elif mode == 'select':
        pass
        # if some filter is required
        if field is not None:
            if field == 'MU_Code':
                if value is not None:
                    query = query.filter_by(MU_Code=value)
            if field == 'MU_Description':
                if value is not None:
                    query = query.filter_by(MU_Description=value)
            
    # Actual request from DB follows
    tracebox_log(query,logger,length=50)
    rows = query.paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
    # Setting pagination variables ...
    if field is not None:
       next_url = url_for('.select_Measure_Units_query', field=field, value=value, page=rows.next_num) if rows.has_next else None
       prev_url = url_for('.select_Measure_Units_query', field=field, value=value, page=rows.prev_num) if rows.has_prev else None
    else:
       next_url = url_for('.select_Measure_Units_query', page=rows.next_num) if rows.has_next else None
       prev_url = url_for('.select_Measure_Units_query', page=rows.prev_num) if rows.has_prev else None
    # Actual rendering ...
    if request.headers.get('Content-Type') is not None or request.args.get('JSON',None,type=str) is not None:
        if "JSON" in request.headers.get('Content-Type') or request.args.get('JSON',None,type=str) is not None:
            logger.debug('select_Measure_Units_query(): will render: JSON rows')
            logger.debug('select_Measure_Units_query(): Exit')
            return json.dumps(serialize_object(rows.__dict__))
    logger.debug('select_Measure_Units_query(): will render: measure_units_All.html')
    logger.debug('select_Measure_Units_query(): Exit')
    return render_template('measure_units_select_All.html',rows=rows,options=options)
#===============================================================================
   # NOTE: HARDCODE. TO REMOVE --------------------------------------------
def chk_c000001(*args,**kwargs):
    pass
    
from emtec.common.interface import *
from emtec.collector.db.orm_model          import Interface
from emtec.collector.db.flask_models       import interface
#-----------------------------------------------------------------------
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2020-02-20 16:44:35
# =============================================================================

# ======================================================================
#  Auto-Generated code. Do not modify 
#  (C) Sertechno/Emtec Group (2018,2019)
#  GLVH @ 2020-02-20 16:44:43.875610
# ======================================================================
        
# gen_views_form.html:AG 2020-02-20 16:44:43.875638
@main.route('/forms/Platforms', methods=['GET', 'POST'])
@login_required

def forms_Platforms():
    """ Form handling function for table Platforms """
    logger.debug('forms_Platforms(): Enter')
    Pla_Id  =  request.args.get('Pla_Id',0,type=int)
    
    row =  platform.query.filter(platform.Pla_Id == Pla_Id).first()
    if row is None:
        row=platform()
        session['is_new_row']=True
    session['data'] =  {  'Pla_Id':row.Pla_Id, 'Pla_Name':row.Pla_Name, 'Pla_Host':row.Pla_Host, 'Pla_Port':row.Pla_Port, 'Pla_User':row.Pla_User, 'Pla_Password':row.Pla_Password }
    
    form = frm_platform()
    
    # Actual Form activation here
    if form.validate_on_submit():
    # Code for SAVE option
        if form.submit_Save.data and current_user.role_id > 1:
    
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
                   message=Markup('<b>Platform Pla_Id saved OK</b>')
                   flash(message)
               db.session.close()
            except Exception as e:
               db.session.rollback()
               db.session.close()
               message=Markup('ERROR saving Platform record : %s'%(e))
               flash(message)
            return redirect(url_for('.select_Platforms_query'))    
    # Code for NEW option
    # GV 20190109 f.write(        "        elif   form.submit_New.data:\n")
        elif   form.submit_New.data and current_user.role_id>1:
            #print('New Data Here ...')
            session['is_new_row']=True
            db.session.close()
            row=platform()
    
            return redirect(url_for('.forms_Platforms',Pla_Id=row.Pla_Id))
    
    # Code for CANCEL option 
        elif   form.submit_Cancel.data:
            #print('Cancel Data Here ... does nothing')
            message=Markup('Platform Record modifications discarded ...')
            flash(message)
    # Code for ANY OTHER option should never get here
        else:
            #print('form validated but not submited ???')
            message=Markup("<b>Platform data modifications not allowed for user '%s'. Please contact EG Suite's Administrator ...</b>"%(current_user.username))    
            flash(message)
    
            return redirect(url_for('.forms_Platforms',Pla_Id=row.Pla_Id))
    
    
    form.Pla_Name.data = row.Pla_Name
    form.Pla_Host.data = row.Pla_Host
    form.Pla_Port.data = row.Pla_Port
    form.Pla_User.data = row.Pla_User
    form.Pla_Password.data = row.Pla_Password
    session['prev_row'] = str(row)
    session['is_new_row'] = False
    logger.debug('forms_Platforms(): Exit')
    # Generates pagination data here
    P=[]
    # Tab Relations = [{'name': 'configuration_items', 'class': 'configuration_item', 'backref': 'platform', 'caption': 'Configuration Items', 'table': 'Configuration_Items'}, {'name': 'rates', 'class': 'rate', 'backref': 'platform', 'caption': 'Rates', 'table': 'Rates'}]
    
    from flask_sqlalchemy import Pagination
    # [{'name': 'configuration_items', 'class': 'configuration_item', 'backref': 'platform', 'caption': 'Configuration Items', 'table': 'Configuration_Items'}, {'name': 'rates', 'class': 'rate', 'backref': 'platform', 'caption': 'Rates', 'table': 'Rates'}]
    P.append(({'name': 'configuration_items', 'class': 'configuration_item', 'backref': 'platform', 'caption': 'Configuration Items', 'table': 'Configuration_Items'},row.configuration_items.paginate()))
    P.append(({'name': 'rates', 'class': 'rate', 'backref': 'platform', 'caption': 'Rates', 'table': 'Rates'},row.rates.paginate()))
    
    """
    print("P=",P,type(P))
    for relation,p in P:
        print("relation=",relation)
        print("p.query=",p.query)
        print("p.has_next=",p.has_next,p.next,p.next_num)
        print("p.has_prev=",p.has_prev,p.prev,p.prev_num)
        print("p.pages=",p.pages)
        print("p.iter_pages=",p.iter_pages)
        print("p.per_page=",p.per_page)
        print("p.total=",p.total)
        print("p.items type=",type(p.items),len(p.items))
    """
    
    # Generation of pagination data completed       
    return render_template('platforms.html', form=form, row=row, P=P)    
# ======================================================================



# ======================================================================
#  Auto-Generated code. Do not modify 
#  (C) Sertechno/Emtec Group (2018,2019)
#  GLVH @ 2020-02-20 16:44:43.907060
# ======================================================================
        
# gen_views_delete.html:AG 2020-02-20 16:44:43.907091
@main.route('/forms/Platforms_delete', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@admin_required
def forms_Platforms_delete():
    """ Delete record handling function for table Platforms """
    logger.debug('forms_Platforms_delete(): Enter')
    Pla_Id  =  request.args.get('Pla_Id',0,type=int)
    row =  platform.query.filter(platform.Pla_Id == Pla_Id).first()

    if row is None:
        row=platform()
    session['data'] =  {  'Pla_Id':row.Pla_Id, 'Pla_Name':row.Pla_Name, 'Pla_Host':row.Pla_Host, 'Pla_Port':row.Pla_Port, 'Pla_User':row.Pla_User, 'Pla_Password':row.Pla_Password }
                       
    form = frm_platform_delete()

    # Tab['has_fks'] False
    
            
    # Actual Form activation here
    if form.validate_on_submit():
    
    # Code for SAVE option
        if  form.submit_Delete.data:
            print('Delete Data Here...')

    
    #f.write(        "            print('Delete Data Here...')
            try:
                session['deleted_row']=str(row)
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                logger.audit ( '%s:DEL:%s' % (current_user.username,session['deleted_row']) )
                flash('Platform Pla_Id deleted OK')
            except exc.IntegrityError as e:
                db.session.rollback()    
                flash('INTEGRITY ERROR: Are you sure there are no dependant records in other tables?')
                return redirect(url_for('.forms_Platforms_delete',Pla_Id=session['data']['Pla_Id']))    
    
            return redirect(url_for('.select_Platforms_query'))    
    # Code for CANCEL option 
        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
            return redirect(url_for('.select_Platforms_query'))    
    # Code for ANY OTHER option should never get here
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.select_Platforms_query'))    
    
    logger.debug('forms_Platforms_delete(): Exit')
    return render_template('platforms_delete.html', form=form, data=session.get('data'),row=row)
#===============================================================================

# ======================================================================
#  Auto-Generated code. Do not modify 
#  (C) Sertechno/Emtec Group (2018,2019)
#  GLVH @ 2020-02-20 16:44:43.958379
# ======================================================================


from pprint import pprint, pformat

# gen_views_select_query.html:AG 2020-02-20 16:44:43.958401        
@main.route('/select/Platforms_Query', methods=['GET','POST'])
@login_required
@admin_required
def select_Platforms_query():
    """ Select rows handling function for table 'Platforms' """
    logger.debug('select_Platforms_query(): Enter')
    chk_c000001(filename=os.path.join(current_app.root_path, '.c000001'),request=request,db=db,logger=logger)
    # Get parameters from URL call
    ia       =  request.args.get('ia',     None,type=str)
    if ia is not None:
        ia=ia.split(',')
        if ia[0]=='ORDER':
            set_query_option(engine=db.engine,Interface=Interface,User_Id=current_user.id,Table_name='platform',Option_Type=OPTION_ORDER_BY,Argument_1=ia[1],Argument_2=ia[2])
        elif ia[0]=='GROUP':
            set_query_option(engine=db.engine,Interface=Interface,User_Id=current_user.id,Table_name='platform',Option_Type=OPTION_GROUP_BY,Argument_1=ia[1])
        elif ia[0]=='LIMIT':
            set_query_option(engine=db.engine,Interface=Interface,User_Id=current_user.id,Table_name='platform',Option_Type=OPTION_LIMIT,Argument_1=ia[1])

    iad      =  request.args.get('iad',     None,type=int)
    if iad is not None: delete_query_option(engine=db.engine,Interface=Interface,Id=iad) 
    
    field    =  request.args.get('field',   None,type=str)
    value    =  request.args.get('value',   None,type=str)
    
    # Populates a list of foreign keys used for advanced filtering
    # ------------------------------------------------------------------
    foreign_keys={}
    
    # ------------------------------------------------------------------
    
    if field is not None:
        reset_query_options(    engine=db.engine,Interface=Interface,
                                User_Id=current_user.id,
                                Table_name='platform'
                                )

        
        if field in foreign_keys.keys():
            Class,referenced_classname,referenced_Field,referenced_Value,column_Header=foreign_keys[field]
            foreign_field='%s.%s:%s'%(referenced_classname,referenced_Value,column_Header)
            foreign_record=Class.query.get(value)
            foreign_description="'%s'"%getattr(foreign_record,referenced_Value)
        set_query_option(   engine=db.engine,Interface=Interface,
                        User_Id=current_user.id,
                        Table_name='platform',
                        Option_Type=OPTION_FILTER,
                        Argument_1=foreign_field,
                        Argument_2='==',
                        Argument_3=foreign_description
                        )
    page     =  request.args.get('page',    1   ,type=int)
    addx     =  request.args.get('add.x',   None,type=int)
    addy     =  request.args.get('add.y',   None,type=int)
    exportx  =  request.args.get('export.x',None,type=int)
    exporty  =  request.args.get('export.y',None,type=int)
    filterx  =  request.args.get('filter.x',None,type=int)
    filtery  =  request.args.get('filter.y',None,type=int)
    # Select excluyent view mode
    if   addx    is not None: mode = 'add'
    elif exportx is not None: mode = 'export'
    elif filterx is not None: mode = 'filter'
    else:                     mode = 'select'
    Pla_Id =  request.args.get('Pla_Id',None,type=str)
    Pla_Name =  request.args.get('Pla_Name',None,type=str)
    Pla_Host =  request.args.get('Pla_Host',None,type=str)
    Pla_Port =  request.args.get('Pla_Port',None,type=str)
    Pla_User =  request.args.get('Pla_User',None,type=str)
    Pla_Password =  request.args.get('Pla_Password',None,type=str)
    
    
    # Build default query all fields from table
    
    if Pla_Id is not None and len(Pla_Id)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='platform',
                Option_Type=OPTION_FILTER,
                Argument_1='Pla_Id:Id',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Pla_Id
                )
    
    
    if Pla_Name is not None and len(Pla_Name)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='platform',
                Option_Type=OPTION_FILTER,
                Argument_1='Pla_Name:Name',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Pla_Name
                )
    
    
    if Pla_Host is not None and len(Pla_Host)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='platform',
                Option_Type=OPTION_FILTER,
                Argument_1='Pla_Host:Host',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Pla_Host
                )
    
    
    if Pla_Port is not None and len(Pla_Port)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='platform',
                Option_Type=OPTION_FILTER,
                Argument_1='Pla_Port:Port',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Pla_Port
                )
    
    
    if Pla_User is not None and len(Pla_User)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='platform',
                Option_Type=OPTION_FILTER,
                Argument_1='Pla_User:User',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Pla_User
                )
    
    
    if Pla_Password is not None and len(Pla_Password)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='platform',
                Option_Type=OPTION_FILTER,
                Argument_1='Pla_Password:Password',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Pla_Password
                )
    
    
    
    statement_query,options=get_query_options(engine=db.engine,Interface=Interface,Table_name='platform',User_Id=current_user.id)
    query=eval(statement_query)
    filtered_query = query    
    if mode == 'filter':
        query=filtered_query
    elif mode == 'export':
        query=filtered_query
        fh,output_file = tempfile.mkstemp(suffix='', prefix='Platforms_', dir=None, text=False)
        dict = {'header':{},'detail':[]}
        count = 0
        rows = query.all()
        for row in rows:
            dict['detail'].append({})
            for column in ['Pla_Id', 'Pla_Name', 'Pla_Host', 'Pla_Port', 'Pla_User', 'Pla_Password']:
                dict['detail'][count].update( { column:str(row.__getattribute__(column))})
                
            count += 1
        dict['header'].update({'count':count})
        jsonarray      = json.dumps(dict)
        data           = json.loads(jsonarray)  
        dataframe      = json_normalize(data, 'detail').assign(**data['header'])
        fh,output_file = tempfile.mkstemp(suffix='', prefix='Platforms_', dir='/tmp', text=False)
        xlsx_file      = '%s/%s'%(current_app.root_path,url_for('static',filename='%s.xls'%(output_file)))
        dataframe.to_excel(xlsx_file,sheet_name='Platforms',columns=['Pla_Id', 'Pla_Name', 'Pla_Host', 'Pla_Port', 'Pla_User', 'Pla_Password'])
        return send_file(xlsx_file,as_attachment=True,attachment_filename=output_file.replace('/','_')+'.xls')
    elif mode == 'add':
        return redirect(url_for('.forms_Platforms'))
    elif mode == 'select':
        pass
        # if some filter is required
        if field is not None:
            if field == 'Pla_Id':
                if value is not None:
                    query = query.filter_by(Pla_Id=value)
            if field == 'Pla_Name':
                if value is not None:
                    query = query.filter_by(Pla_Name=value)
            if field == 'Pla_Host':
                if value is not None:
                    query = query.filter_by(Pla_Host=value)
            if field == 'Pla_Port':
                if value is not None:
                    query = query.filter_by(Pla_Port=value)
            if field == 'Pla_User':
                if value is not None:
                    query = query.filter_by(Pla_User=value)
            if field == 'Pla_Password':
                if value is not None:
                    query = query.filter_by(Pla_Password=value)
            
    # Actual request from DB follows
    tracebox_log(query,logger,length=50)
    rows = query.paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
    # Setting pagination variables ...
    if field is not None:
       next_url = url_for('.select_Platforms_query', field=field, value=value, page=rows.next_num) if rows.has_next else None
       prev_url = url_for('.select_Platforms_query', field=field, value=value, page=rows.prev_num) if rows.has_prev else None
    else:
       next_url = url_for('.select_Platforms_query', page=rows.next_num) if rows.has_next else None
       prev_url = url_for('.select_Platforms_query', page=rows.prev_num) if rows.has_prev else None
    # Actual rendering ...
    if request.headers.get('Content-Type') is not None or request.args.get('JSON',None,type=str) is not None:
        if "JSON" in request.headers.get('Content-Type') or request.args.get('JSON',None,type=str) is not None:
            logger.debug('select_Platforms_query(): will render: JSON rows')
            logger.debug('select_Platforms_query(): Exit')
            return json.dumps(serialize_object(rows.__dict__))
    logger.debug('select_Platforms_query(): will render: platforms_All.html')
    logger.debug('select_Platforms_query(): Exit')
    return render_template('platforms_select_All.html',rows=rows,options=options)
#===============================================================================
   # NOTE: HARDCODE. TO REMOVE --------------------------------------------
def chk_c000001(*args,**kwargs):
    pass
    
from emtec.common.interface import *
from emtec.collector.db.orm_model          import Interface
from emtec.collector.db.flask_models       import interface
#-----------------------------------------------------------------------
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2020-02-20 16:44:35
# =============================================================================

# ======================================================================
#  Auto-Generated code. Do not modify 
#  (C) Sertechno/Emtec Group (2018,2019)
#  GLVH @ 2020-02-20 16:44:44.648750
# ======================================================================
        
# gen_views_form.html:AG 2020-02-20 16:44:44.648775
@main.route('/forms/Rates', methods=['GET', 'POST'])
@login_required

def forms_Rates():
    """ Form handling function for table Rates """
    logger.debug('forms_Rates(): Enter')
    Rat_Id  =  request.args.get('Rat_Id',0,type=int)
    
    row =  rate.query.filter(rate.Rat_Id == Rat_Id).first()
    if row is None:
        row=rate()
        session['is_new_row']=True
    session['data'] =  {  'Rat_Id':row.Rat_Id, 'Typ_Code':row.Typ_Code, 'Cus_Id':row.Cus_Id, 'Pla_Id':row.Pla_Id, 'CC_Id':row.CC_Id, 'CI_Id':row.CI_Id, 'Rat_Price':row.Rat_Price, 'Cur_Code':row.Cur_Code, 'MU_Code':row.MU_Code, 'Rat_Period':row.Rat_Period, 'Rat_Type':row.Rat_Type }
    
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

    
    # Actual Form activation here
    if form.validate_on_submit():
    # Code for SAVE option
        if form.submit_Save.data and current_user.role_id > 1:
    
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
                   message=Markup('<b>Rate Rat_Id saved OK</b>')
                   flash(message)
               db.session.close()
            except Exception as e:
               db.session.rollback()
               db.session.close()
               message=Markup('ERROR saving Rate record : %s'%(e))
               flash(message)
            return redirect(url_for('.select_Rates_query'))    
    # Code for NEW option
    # GV 20190109 f.write(        "        elif   form.submit_New.data:\n")
        elif   form.submit_New.data and current_user.role_id>1:
            #print('New Data Here ...')
            session['is_new_row']=True
            db.session.close()
            row=rate()
    
            return redirect(url_for('.forms_Rates',Rat_Id=row.Rat_Id))
    
    # Code for CANCEL option 
        elif   form.submit_Cancel.data:
            #print('Cancel Data Here ... does nothing')
            message=Markup('Rate Record modifications discarded ...')
            flash(message)
    # Code for ANY OTHER option should never get here
        else:
            #print('form validated but not submited ???')
            message=Markup("<b>Rate data modifications not allowed for user '%s'. Please contact EG Suite's Administrator ...</b>"%(current_user.username))    
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
    session['prev_row'] = str(row)
    session['is_new_row'] = False
    logger.debug('forms_Rates(): Exit')
    # Generates pagination data here
    P=[]
    # Tab Relations = []
    
    # Generation of pagination data completed       
    return render_template('rates.html', form=form, row=row, P=P)    
# ======================================================================



# ======================================================================
#  Auto-Generated code. Do not modify 
#  (C) Sertechno/Emtec Group (2018,2019)
#  GLVH @ 2020-02-20 16:44:44.672546
# ======================================================================
        
# gen_views_delete.html:AG 2020-02-20 16:44:44.672568
@main.route('/forms/Rates_delete', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@admin_required
def forms_Rates_delete():
    """ Delete record handling function for table Rates """
    logger.debug('forms_Rates_delete(): Enter')
    Rat_Id  =  request.args.get('Rat_Id',0,type=int)
    row =  rate.query.filter(rate.Rat_Id == Rat_Id).first()

    if row is None:
        row=rate()
    session['data'] =  {  'Rat_Id':row.Rat_Id, 'Typ_Code':row.Typ_Code, 'Cus_Id':row.Cus_Id, 'Pla_Id':row.Pla_Id, 'CC_Id':row.CC_Id, 'CI_Id':row.CI_Id, 'Rat_Price':row.Rat_Price, 'Cur_Code':row.Cur_Code, 'MU_Code':row.MU_Code, 'Rat_Period':row.Rat_Period, 'Rat_Type':row.Rat_Type }
                       
    form = frm_rate_delete()

    # Tab['has_fks'] True
    
    pass # Tab['has_fks'] True
    
            
    # Actual Form activation here
    if form.validate_on_submit():
    
    # Code for SAVE option
        if  form.submit_Delete.data:
            print('Delete Data Here...')

    
    #f.write(        "            print('Delete Data Here...')
            try:
                session['deleted_row']=str(row)
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                logger.audit ( '%s:DEL:%s' % (current_user.username,session['deleted_row']) )
                flash('Rate Rat_Id deleted OK')
            except exc.IntegrityError as e:
                db.session.rollback()    
                flash('INTEGRITY ERROR: Are you sure there are no dependant records in other tables?')
                return redirect(url_for('.forms_Rates_delete',Rat_Id=session['data']['Rat_Id']))    
    
            return redirect(url_for('.select_Rates_query'))    
    # Code for CANCEL option 
        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
            return redirect(url_for('.select_Rates_query'))    
    # Code for ANY OTHER option should never get here
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.select_Rates_query'))    
    
    logger.debug('forms_Rates_delete(): Exit')
    return render_template('rates_delete.html', form=form, data=session.get('data'),row=row)
#===============================================================================

# ======================================================================
#  Auto-Generated code. Do not modify 
#  (C) Sertechno/Emtec Group (2018,2019)
#  GLVH @ 2020-02-20 16:44:44.723271
# ======================================================================


from pprint import pprint, pformat

# gen_views_select_query.html:AG 2020-02-20 16:44:44.723294        
@main.route('/select/Rates_Query', methods=['GET','POST'])
@login_required
@admin_required
def select_Rates_query():
    """ Select rows handling function for table 'Rates' """
    logger.debug('select_Rates_query(): Enter')
    chk_c000001(filename=os.path.join(current_app.root_path, '.c000001'),request=request,db=db,logger=logger)
    # Get parameters from URL call
    ia       =  request.args.get('ia',     None,type=str)
    if ia is not None:
        ia=ia.split(',')
        if ia[0]=='ORDER':
            set_query_option(engine=db.engine,Interface=Interface,User_Id=current_user.id,Table_name='rate',Option_Type=OPTION_ORDER_BY,Argument_1=ia[1],Argument_2=ia[2])
        elif ia[0]=='GROUP':
            set_query_option(engine=db.engine,Interface=Interface,User_Id=current_user.id,Table_name='rate',Option_Type=OPTION_GROUP_BY,Argument_1=ia[1])
        elif ia[0]=='LIMIT':
            set_query_option(engine=db.engine,Interface=Interface,User_Id=current_user.id,Table_name='rate',Option_Type=OPTION_LIMIT,Argument_1=ia[1])

    iad      =  request.args.get('iad',     None,type=int)
    if iad is not None: delete_query_option(engine=db.engine,Interface=Interface,Id=iad) 
    
    field    =  request.args.get('field',   None,type=str)
    value    =  request.args.get('value',   None,type=str)
    
    # Populates a list of foreign keys used for advanced filtering
    # ------------------------------------------------------------------
    foreign_keys={}
    
    foreign_keys.update({'Typ_Code':(cu_type,'cu_type','Typ_Code','Typ_Description','Charge Unit Type')})
    foreign_keys.update({'Cus_Id':(customer,'customer','Cus_Id','Cus_Name','Customer Id')})
    foreign_keys.update({'Pla_Id':(platform,'platform','Pla_Id','Pla_Name','Platform Id')})
    foreign_keys.update({'CC_Id':(cost_center,'cost_center','CC_Id','CC_Description','Cost Center Id')})
    foreign_keys.update({'CI_Id':(configuration_item,'configuration_item','CI_Id','CI_Name','Configuration Item')})
    foreign_keys.update({'Cur_Code':(currency,'currency','Cur_Code','Cur_Name','Currency Code')})
    foreign_keys.update({'MU_Code':(measure_unit,'measure_unit','MU_Code','MU_Description','Measure Unit')})
    foreign_keys.update({'Rat_Period':(rat_period,'rat_period','Rat_Period','Value','Period')})
    # ------------------------------------------------------------------
    
    if field is not None:
        reset_query_options(    engine=db.engine,Interface=Interface,
                                User_Id=current_user.id,
                                Table_name='rate'
                                )

        
        if field in foreign_keys.keys():
            Class,referenced_classname,referenced_Field,referenced_Value,column_Header=foreign_keys[field]
            foreign_field='%s.%s:%s'%(referenced_classname,referenced_Value,column_Header)
            foreign_record=Class.query.get(value)
            foreign_description="'%s'"%getattr(foreign_record,referenced_Value)
        set_query_option(   engine=db.engine,Interface=Interface,
                        User_Id=current_user.id,
                        Table_name='rate',
                        Option_Type=OPTION_FILTER,
                        Argument_1=foreign_field,
                        Argument_2='==',
                        Argument_3=foreign_description
                        )
    page     =  request.args.get('page',    1   ,type=int)
    addx     =  request.args.get('add.x',   None,type=int)
    addy     =  request.args.get('add.y',   None,type=int)
    exportx  =  request.args.get('export.x',None,type=int)
    exporty  =  request.args.get('export.y',None,type=int)
    filterx  =  request.args.get('filter.x',None,type=int)
    filtery  =  request.args.get('filter.y',None,type=int)
    # Select excluyent view mode
    if   addx    is not None: mode = 'add'
    elif exportx is not None: mode = 'export'
    elif filterx is not None: mode = 'filter'
    else:                     mode = 'select'
    Rat_Id =  request.args.get('Rat_Id',None,type=str)
    Typ_Code =  request.args.get('Typ_Code',None,type=str)
    Cus_Id =  request.args.get('Cus_Id',None,type=str)
    Pla_Id =  request.args.get('Pla_Id',None,type=str)
    CC_Id =  request.args.get('CC_Id',None,type=str)
    CI_Id =  request.args.get('CI_Id',None,type=str)
    Rat_Price =  request.args.get('Rat_Price',None,type=str)
    Cur_Code =  request.args.get('Cur_Code',None,type=str)
    MU_Code =  request.args.get('MU_Code',None,type=str)
    Rat_Period =  request.args.get('Rat_Period',None,type=str)
    Rat_Type =  request.args.get('Rat_Type',None,type=str)
    
    
    # Build default query all fields from table
    
    if Rat_Id is not None and len(Rat_Id)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='rate',
                Option_Type=OPTION_FILTER,
                Argument_1='Rat_Id:Id',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Rat_Id
                )
    
    
    if Typ_Code is not None and len(Typ_Code)>0:
            Class,referenced_classname,referenced_Field,referenced_Value,column_Header=foreign_keys['Typ_Code']
            foreign_field='%s.%s:%s'%(referenced_classname,referenced_Value,column_Header)            
            set_query_option(   engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='rate',
                Option_Type=OPTION_FILTER,
                Argument_1=foreign_field,
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Typ_Code
                )
                                
    
    
    if Cus_Id is not None and len(Cus_Id)>0:
            Class,referenced_classname,referenced_Field,referenced_Value,column_Header=foreign_keys['Cus_Id']
            foreign_field='%s.%s:%s'%(referenced_classname,referenced_Value,column_Header)            
            set_query_option(   engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='rate',
                Option_Type=OPTION_FILTER,
                Argument_1=foreign_field,
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Cus_Id
                )
                                
    
    
    if Pla_Id is not None and len(Pla_Id)>0:
            Class,referenced_classname,referenced_Field,referenced_Value,column_Header=foreign_keys['Pla_Id']
            foreign_field='%s.%s:%s'%(referenced_classname,referenced_Value,column_Header)            
            set_query_option(   engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='rate',
                Option_Type=OPTION_FILTER,
                Argument_1=foreign_field,
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Pla_Id
                )
                                
    
    
    if CC_Id is not None and len(CC_Id)>0:
            Class,referenced_classname,referenced_Field,referenced_Value,column_Header=foreign_keys['CC_Id']
            foreign_field='%s.%s:%s'%(referenced_classname,referenced_Value,column_Header)            
            set_query_option(   engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='rate',
                Option_Type=OPTION_FILTER,
                Argument_1=foreign_field,
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%CC_Id
                )
                                
    
    
    if CI_Id is not None and len(CI_Id)>0:
            Class,referenced_classname,referenced_Field,referenced_Value,column_Header=foreign_keys['CI_Id']
            foreign_field='%s.%s:%s'%(referenced_classname,referenced_Value,column_Header)            
            set_query_option(   engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='rate',
                Option_Type=OPTION_FILTER,
                Argument_1=foreign_field,
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%CI_Id
                )
                                
    
    
    if Rat_Price is not None and len(Rat_Price)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='rate',
                Option_Type=OPTION_FILTER,
                Argument_1='Rat_Price:Rate Price',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Rat_Price
                )
    
    
    if Cur_Code is not None and len(Cur_Code)>0:
            Class,referenced_classname,referenced_Field,referenced_Value,column_Header=foreign_keys['Cur_Code']
            foreign_field='%s.%s:%s'%(referenced_classname,referenced_Value,column_Header)            
            set_query_option(   engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='rate',
                Option_Type=OPTION_FILTER,
                Argument_1=foreign_field,
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Cur_Code
                )
                                
    
    
    if MU_Code is not None and len(MU_Code)>0:
            Class,referenced_classname,referenced_Field,referenced_Value,column_Header=foreign_keys['MU_Code']
            foreign_field='%s.%s:%s'%(referenced_classname,referenced_Value,column_Header)            
            set_query_option(   engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='rate',
                Option_Type=OPTION_FILTER,
                Argument_1=foreign_field,
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%MU_Code
                )
                                
    
    
    if Rat_Period is not None and len(Rat_Period)>0:
            Class,referenced_classname,referenced_Field,referenced_Value,column_Header=foreign_keys['Rat_Period']
            foreign_field='%s.%s:%s'%(referenced_classname,referenced_Value,column_Header)            
            set_query_option(   engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='rate',
                Option_Type=OPTION_FILTER,
                Argument_1=foreign_field,
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Rat_Period
                )
                                
    
    
    if Rat_Type is not None and len(Rat_Type)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='rate',
                Option_Type=OPTION_FILTER,
                Argument_1='Rat_Type:Rate Type',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Rat_Type
                )
    
    
    
    statement_query,options=get_query_options(engine=db.engine,Interface=Interface,Table_name='rate',User_Id=current_user.id)
    query=eval(statement_query)
    filtered_query = query    
    if mode == 'filter':
        query=filtered_query
    elif mode == 'export':
        query=filtered_query
        fh,output_file = tempfile.mkstemp(suffix='', prefix='Rates_', dir=None, text=False)
        dict = {'header':{},'detail':[]}
        count = 0
        rows = query.all()
        for row in rows:
            dict['detail'].append({})
            for column in ['Rat_Id', 'Typ_Code', 'Cus_Id', 'Pla_Id', 'CC_Id', 'CI_Id', 'Rat_Price', 'Cur_Code', 'MU_Code', 'Rat_Period', 'Rat_Type']:
                dict['detail'][count].update( { column:str(row.__getattribute__(column))})
                
            count += 1
        dict['header'].update({'count':count})
        jsonarray      = json.dumps(dict)
        data           = json.loads(jsonarray)  
        dataframe      = json_normalize(data, 'detail').assign(**data['header'])
        fh,output_file = tempfile.mkstemp(suffix='', prefix='Rates_', dir='/tmp', text=False)
        xlsx_file      = '%s/%s'%(current_app.root_path,url_for('static',filename='%s.xls'%(output_file)))
        dataframe.to_excel(xlsx_file,sheet_name='Rates',columns=['Rat_Id', 'Typ_Code', 'Cus_Id', 'Pla_Id', 'CC_Id', 'CI_Id', 'Rat_Price', 'Cur_Code', 'MU_Code', 'Rat_Period', 'Rat_Type'])
        return send_file(xlsx_file,as_attachment=True,attachment_filename=output_file.replace('/','_')+'.xls')
    elif mode == 'add':
        return redirect(url_for('.forms_Rates'))
    elif mode == 'select':
        pass
        # if some filter is required
        if field is not None:
            if field == 'Rat_Id':
                if value is not None:
                    query = query.filter_by(Rat_Id=value)
            if field == 'Typ_Code':
                if value is not None:
                    query = query.filter_by(Typ_Code=value)
            if field == 'Cus_Id':
                if value is not None:
                    query = query.filter_by(Cus_Id=value)
            if field == 'Pla_Id':
                if value is not None:
                    query = query.filter_by(Pla_Id=value)
            if field == 'CC_Id':
                if value is not None:
                    query = query.filter_by(CC_Id=value)
            if field == 'CI_Id':
                if value is not None:
                    query = query.filter_by(CI_Id=value)
            if field == 'Rat_Price':
                if value is not None:
                    query = query.filter_by(Rat_Price=value)
            if field == 'Cur_Code':
                if value is not None:
                    query = query.filter_by(Cur_Code=value)
            if field == 'MU_Code':
                if value is not None:
                    query = query.filter_by(MU_Code=value)
            if field == 'Rat_Period':
                if value is not None:
                    query = query.filter_by(Rat_Period=value)
            if field == 'Rat_Type':
                if value is not None:
                    query = query.filter_by(Rat_Type=value)
            # JOIN other tables and generate foreign fields
    query = query.join(cu_type,rate.Typ_Code == cu_type.Typ_Code).add_columns(cu_type.Typ_Description).join(customer,rate.Cus_Id == customer.Cus_Id).add_columns(customer.Cus_Name).join(platform,rate.Pla_Id == platform.Pla_Id).add_columns(platform.Pla_Name).join(cost_center,rate.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description).join(configuration_item,rate.CI_Id == configuration_item.CI_Id).add_columns(configuration_item.CI_Name).join(currency,rate.Cur_Code == currency.Cur_Code).add_columns(currency.Cur_Name).join(measure_unit,rate.MU_Code == measure_unit.MU_Code).add_columns(measure_unit.MU_Description).join(rat_period,rate.Rat_Period == rat_period.Rat_Period).add_columns(rat_period.Value)
    
    # Actual request from DB follows
    tracebox_log(query,logger,length=50)
    rows = query.paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
    # Setting pagination variables ...
    if field is not None:
       next_url = url_for('.select_Rates_query', field=field, value=value, page=rows.next_num) if rows.has_next else None
       prev_url = url_for('.select_Rates_query', field=field, value=value, page=rows.prev_num) if rows.has_prev else None
    else:
       next_url = url_for('.select_Rates_query', page=rows.next_num) if rows.has_next else None
       prev_url = url_for('.select_Rates_query', page=rows.prev_num) if rows.has_prev else None
    # Actual rendering ...
    if request.headers.get('Content-Type') is not None or request.args.get('JSON',None,type=str) is not None:
        if "JSON" in request.headers.get('Content-Type') or request.args.get('JSON',None,type=str) is not None:
            logger.debug('select_Rates_query(): will render: JSON rows')
            logger.debug('select_Rates_query(): Exit')
            return json.dumps(serialize_object(rows.__dict__))
    logger.debug('select_Rates_query(): will render: rates_All.html')
    logger.debug('select_Rates_query(): Exit')
    return render_template('rates_select_All.html',rows=rows,options=options)
#===============================================================================
   # NOTE: HARDCODE. TO REMOVE --------------------------------------------
def chk_c000001(*args,**kwargs):
    pass
    
from emtec.common.interface import *
from emtec.collector.db.orm_model          import Interface
from emtec.collector.db.flask_models       import interface
#-----------------------------------------------------------------------
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2020-02-20 16:44:35
# =============================================================================

# ======================================================================
#  Auto-Generated code. Do not modify 
#  (C) Sertechno/Emtec Group (2018,2019)
#  GLVH @ 2020-02-20 16:44:44.234650
# ======================================================================
        
# gen_views_form.html:AG 2020-02-20 16:44:44.234743
@main.route('/forms/Rat_Periods', methods=['GET', 'POST'])
@login_required

def forms_Rat_Periods():
    """ Form handling function for table Rat_Periods """
    logger.debug('forms_Rat_Periods(): Enter')
    Rat_Period  =  request.args.get('Rat_Period',0,type=int)
    
    row =  rat_period.query.filter(rat_period.Rat_Period == Rat_Period).first()
    if row is None:
        row=rat_period()
        session['is_new_row']=True
    session['data'] =  {  'Rat_Period':row.Rat_Period, 'Value':row.Value }
    
    form = frm_rat_period()
    
    # Actual Form activation here
    if form.validate_on_submit():
    # Code for SAVE option
        if form.submit_Save.data and current_user.role_id > 1:
    
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
                   message=Markup('<b>Rate Period Rat_Period saved OK</b>')
                   flash(message)
               db.session.close()
            except Exception as e:
               db.session.rollback()
               db.session.close()
               message=Markup('ERROR saving Rate Period record : %s'%(e))
               flash(message)
            return redirect(url_for('.select_Rat_Periods_query'))    
    # Code for NEW option
    # GV 20190109 f.write(        "        elif   form.submit_New.data:\n")
        elif   form.submit_New.data and current_user.role_id>1:
            #print('New Data Here ...')
            session['is_new_row']=True
            db.session.close()
            row=rat_period()
    
            return redirect(url_for('.forms_Rat_Periods'))    
    
    # Code for CANCEL option 
        elif   form.submit_Cancel.data:
            #print('Cancel Data Here ... does nothing')
            message=Markup('Rate Period Record modifications discarded ...')
            flash(message)
    # Code for ANY OTHER option should never get here
        else:
            #print('form validated but not submited ???')
            message=Markup("<b>Rate Period data modifications not allowed for user '%s'. Please contact EG Suite's Administrator ...</b>"%(current_user.username))    
            flash(message)
    
            return redirect(url_for('.forms_'))    
    
    
    form.Rat_Period.data = row.Rat_Period
    form.Value.data = row.Value
    session['prev_row'] = str(row)
    session['is_new_row'] = False
    logger.debug('forms_Rat_Periods(): Exit')
    # Generates pagination data here
    P=[]
    # Tab Relations = [{'name': 'rates', 'class': 'rate', 'backref': 'rat_period', 'caption': 'Rates', 'table': 'Rates'}]
    
    from flask_sqlalchemy import Pagination
    # [{'name': 'rates', 'class': 'rate', 'backref': 'rat_period', 'caption': 'Rates', 'table': 'Rates'}]
    P.append(({'name': 'rates', 'class': 'rate', 'backref': 'rat_period', 'caption': 'Rates', 'table': 'Rates'},row.rates.paginate()))
    
    """
    print("P=",P,type(P))
    for relation,p in P:
        print("relation=",relation)
        print("p.query=",p.query)
        print("p.has_next=",p.has_next,p.next,p.next_num)
        print("p.has_prev=",p.has_prev,p.prev,p.prev_num)
        print("p.pages=",p.pages)
        print("p.iter_pages=",p.iter_pages)
        print("p.per_page=",p.per_page)
        print("p.total=",p.total)
        print("p.items type=",type(p.items),len(p.items))
    """
    
    # Generation of pagination data completed       
    return render_template('rat_periods.html', form=form, row=row, P=P)    
# ======================================================================



# ======================================================================
#  Auto-Generated code. Do not modify 
#  (C) Sertechno/Emtec Group (2018,2019)
#  GLVH @ 2020-02-20 16:44:44.259671
# ======================================================================
        
# gen_views_delete.html:AG 2020-02-20 16:44:44.259696
@main.route('/forms/Rat_Periods_delete', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@admin_required
def forms_Rat_Periods_delete():
    """ Delete record handling function for table Rat_Periods """
    logger.debug('forms_Rat_Periods_delete(): Enter')
    Rat_Period  =  request.args.get('Rat_Period',0,type=int)
    row =  rat_period.query.filter(rat_period.Rat_Period == Rat_Period).first()

    if row is None:
        row=rat_period()
    session['data'] =  {  'Rat_Period':row.Rat_Period, 'Value':row.Value }
                       
    form = frm_rat_period_delete()

    # Tab['has_fks'] False
    
            
    # Actual Form activation here
    if form.validate_on_submit():
    
    # Code for SAVE option
        if  form.submit_Delete.data:
            print('Delete Data Here...')

    
    #f.write(        "            print('Delete Data Here...')
            try:
                session['deleted_row']=str(row)
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                logger.audit ( '%s:DEL:%s' % (current_user.username,session['deleted_row']) )
                flash('Rate Period Rat_Period deleted OK')
            except exc.IntegrityError as e:
                db.session.rollback()    
                flash('INTEGRITY ERROR: Are you sure there are no dependant records in other tables?')
                return redirect(url_for('.forms_Rat_Periods_delete',Rat_Period=session['data']['Rat_Period']))    
    
            return redirect(url_for('.select_Rat_Periods_query'))    
    # Code for CANCEL option 
        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
            return redirect(url_for('.select_Rat_Periods_query'))    
    # Code for ANY OTHER option should never get here
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.select_Rat_Periods_query'))    
    
    logger.debug('forms_Rat_Periods_delete(): Exit')
    return render_template('rat_periods_delete.html', form=form, data=session.get('data'),row=row)
#===============================================================================

# ======================================================================
#  Auto-Generated code. Do not modify 
#  (C) Sertechno/Emtec Group (2018,2019)
#  GLVH @ 2020-02-20 16:44:44.311262
# ======================================================================


from pprint import pprint, pformat

# gen_views_select_query.html:AG 2020-02-20 16:44:44.311285        
@main.route('/select/Rat_Periods_Query', methods=['GET','POST'])
@login_required
@admin_required
def select_Rat_Periods_query():
    """ Select rows handling function for table 'Rat_Periods' """
    logger.debug('select_Rat_Periods_query(): Enter')
    chk_c000001(filename=os.path.join(current_app.root_path, '.c000001'),request=request,db=db,logger=logger)
    # Get parameters from URL call
    ia       =  request.args.get('ia',     None,type=str)
    if ia is not None:
        ia=ia.split(',')
        if ia[0]=='ORDER':
            set_query_option(engine=db.engine,Interface=Interface,User_Id=current_user.id,Table_name='rat_period',Option_Type=OPTION_ORDER_BY,Argument_1=ia[1],Argument_2=ia[2])
        elif ia[0]=='GROUP':
            set_query_option(engine=db.engine,Interface=Interface,User_Id=current_user.id,Table_name='rat_period',Option_Type=OPTION_GROUP_BY,Argument_1=ia[1])
        elif ia[0]=='LIMIT':
            set_query_option(engine=db.engine,Interface=Interface,User_Id=current_user.id,Table_name='rat_period',Option_Type=OPTION_LIMIT,Argument_1=ia[1])

    iad      =  request.args.get('iad',     None,type=int)
    if iad is not None: delete_query_option(engine=db.engine,Interface=Interface,Id=iad) 
    
    field    =  request.args.get('field',   None,type=str)
    value    =  request.args.get('value',   None,type=str)
    
    # Populates a list of foreign keys used for advanced filtering
    # ------------------------------------------------------------------
    foreign_keys={}
    
    # ------------------------------------------------------------------
    
    if field is not None:
        reset_query_options(    engine=db.engine,Interface=Interface,
                                User_Id=current_user.id,
                                Table_name='rat_period'
                                )

        
        if field in foreign_keys.keys():
            Class,referenced_classname,referenced_Field,referenced_Value,column_Header=foreign_keys[field]
            foreign_field='%s.%s:%s'%(referenced_classname,referenced_Value,column_Header)
            foreign_record=Class.query.get(value)
            foreign_description="'%s'"%getattr(foreign_record,referenced_Value)
        set_query_option(   engine=db.engine,Interface=Interface,
                        User_Id=current_user.id,
                        Table_name='rat_period',
                        Option_Type=OPTION_FILTER,
                        Argument_1=foreign_field,
                        Argument_2='==',
                        Argument_3=foreign_description
                        )
    page     =  request.args.get('page',    1   ,type=int)
    addx     =  request.args.get('add.x',   None,type=int)
    addy     =  request.args.get('add.y',   None,type=int)
    exportx  =  request.args.get('export.x',None,type=int)
    exporty  =  request.args.get('export.y',None,type=int)
    filterx  =  request.args.get('filter.x',None,type=int)
    filtery  =  request.args.get('filter.y',None,type=int)
    # Select excluyent view mode
    if   addx    is not None: mode = 'add'
    elif exportx is not None: mode = 'export'
    elif filterx is not None: mode = 'filter'
    else:                     mode = 'select'
    Rat_Period =  request.args.get('Rat_Period',None,type=str)
    Value =  request.args.get('Value',None,type=str)
    
    
    # Build default query all fields from table
    
    if Rat_Period is not None and len(Rat_Period)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='rat_period',
                Option_Type=OPTION_FILTER,
                Argument_1='Rat_Period:Rate Period',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Rat_Period
                )
    
    
    if Value is not None and len(Value)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='rat_period',
                Option_Type=OPTION_FILTER,
                Argument_1='Value:Value',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Value
                )
    
    
    
    statement_query,options=get_query_options(engine=db.engine,Interface=Interface,Table_name='rat_period',User_Id=current_user.id)
    query=eval(statement_query)
    filtered_query = query    
    if mode == 'filter':
        query=filtered_query
    elif mode == 'export':
        query=filtered_query
        fh,output_file = tempfile.mkstemp(suffix='', prefix='Rat_Periods_', dir=None, text=False)
        dict = {'header':{},'detail':[]}
        count = 0
        rows = query.all()
        for row in rows:
            dict['detail'].append({})
            for column in ['Rat_Period', 'Value']:
                dict['detail'][count].update( { column:str(row.__getattribute__(column))})
                
            count += 1
        dict['header'].update({'count':count})
        jsonarray      = json.dumps(dict)
        data           = json.loads(jsonarray)  
        dataframe      = json_normalize(data, 'detail').assign(**data['header'])
        fh,output_file = tempfile.mkstemp(suffix='', prefix='Rat_Periods_', dir='/tmp', text=False)
        xlsx_file      = '%s/%s'%(current_app.root_path,url_for('static',filename='%s.xls'%(output_file)))
        dataframe.to_excel(xlsx_file,sheet_name='Rat_Periods',columns=['Rat_Period', 'Value'])
        return send_file(xlsx_file,as_attachment=True,attachment_filename=output_file.replace('/','_')+'.xls')
    elif mode == 'add':
        return redirect(url_for('.forms_Rat_Periods'))
    elif mode == 'select':
        pass
        # if some filter is required
        if field is not None:
            if field == 'Rat_Period':
                if value is not None:
                    query = query.filter_by(Rat_Period=value)
            if field == 'Value':
                if value is not None:
                    query = query.filter_by(Value=value)
            
    # Actual request from DB follows
    tracebox_log(query,logger,length=50)
    rows = query.paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
    # Setting pagination variables ...
    if field is not None:
       next_url = url_for('.select_Rat_Periods_query', field=field, value=value, page=rows.next_num) if rows.has_next else None
       prev_url = url_for('.select_Rat_Periods_query', field=field, value=value, page=rows.prev_num) if rows.has_prev else None
    else:
       next_url = url_for('.select_Rat_Periods_query', page=rows.next_num) if rows.has_next else None
       prev_url = url_for('.select_Rat_Periods_query', page=rows.prev_num) if rows.has_prev else None
    # Actual rendering ...
    if request.headers.get('Content-Type') is not None or request.args.get('JSON',None,type=str) is not None:
        if "JSON" in request.headers.get('Content-Type') or request.args.get('JSON',None,type=str) is not None:
            logger.debug('select_Rat_Periods_query(): will render: JSON rows')
            logger.debug('select_Rat_Periods_query(): Exit')
            return json.dumps(serialize_object(rows.__dict__))
    logger.debug('select_Rat_Periods_query(): will render: rat_periods_All.html')
    logger.debug('select_Rat_Periods_query(): Exit')
    return render_template('rat_periods_select_All.html',rows=rows,options=options)
#===============================================================================
   # NOTE: HARDCODE. TO REMOVE --------------------------------------------
def chk_c000001(*args,**kwargs):
    pass
    
from emtec.common.interface import *
from emtec.collector.db.orm_model          import Interface
from emtec.collector.db.flask_models       import interface
#-----------------------------------------------------------------------
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2020-02-20 16:44:35
# =============================================================================

# ======================================================================
#  Auto-Generated code. Do not modify 
#  (C) Sertechno/Emtec Group (2018,2019)
#  GLVH @ 2020-02-20 16:44:44.969533
# ======================================================================
        
# gen_views_form.html:AG 2020-02-20 16:44:44.969570
@main.route('/forms/Roles', methods=['GET', 'POST'])
@login_required

def forms_Roles():
    """ Form handling function for table Roles """
    logger.debug('forms_Roles(): Enter')
    id  =  request.args.get('id',0,type=int)
    
    row =  Role.query.filter(Role.id == id).first()
    if row is None:
        row=Role()
        session['is_new_row']=True
    session['data'] =  {  'id':row.id, 'name':row.name, 'default':row.default, 'permissions':row.permissions }
    
    form = frm_Role()
    
    # Actual Form activation here
    if form.validate_on_submit():
    # Code for SAVE option
        if form.submit_Save.data and current_user.role_id > 1:
    
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
                   message=Markup('<b>Role id saved OK</b>')
                   flash(message)
               db.session.close()
            except Exception as e:
               db.session.rollback()
               db.session.close()
               message=Markup('ERROR saving Role record : %s'%(e))
               flash(message)
            return redirect(url_for('.select_Roles_query'))    
    # Code for NEW option
    # GV 20190109 f.write(        "        elif   form.submit_New.data:\n")
        elif   form.submit_New.data and current_user.role_id>1:
            #print('New Data Here ...')
            session['is_new_row']=True
            db.session.close()
            row=Role()
    
            return redirect(url_for('.forms_Roles'))    
    
    # Code for CANCEL option 
        elif   form.submit_Cancel.data:
            #print('Cancel Data Here ... does nothing')
            message=Markup('Role Record modifications discarded ...')
            flash(message)
    # Code for ANY OTHER option should never get here
        else:
            #print('form validated but not submited ???')
            message=Markup("<b>Role data modifications not allowed for user '%s'. Please contact EG Suite's Administrator ...</b>"%(current_user.username))    
            flash(message)
    
            return redirect(url_for('.forms_'))    
    
    
    form.id.data = row.id
    form.name.data = row.name
    form.default.data = row.default
    form.permissions.data = row.permissions
    session['prev_row'] = str(row)
    session['is_new_row'] = False
    logger.debug('forms_Roles(): Exit')
    # Generates pagination data here
    P=[]
    # Tab Relations = [{'name': 'users', 'class': 'User', 'backref': 'Role', 'caption': 'Users', 'table': 'Users'}]
    
    from flask_sqlalchemy import Pagination
    # [{'name': 'users', 'class': 'User', 'backref': 'Role', 'caption': 'Users', 'table': 'Users'}]
    P.append(({'name': 'users', 'class': 'User', 'backref': 'Role', 'caption': 'Users', 'table': 'Users'},row.users.paginate()))
    
    """
    print("P=",P,type(P))
    for relation,p in P:
        print("relation=",relation)
        print("p.query=",p.query)
        print("p.has_next=",p.has_next,p.next,p.next_num)
        print("p.has_prev=",p.has_prev,p.prev,p.prev_num)
        print("p.pages=",p.pages)
        print("p.iter_pages=",p.iter_pages)
        print("p.per_page=",p.per_page)
        print("p.total=",p.total)
        print("p.items type=",type(p.items),len(p.items))
    """
    
    # Generation of pagination data completed       
    return render_template('roles.html', form=form, row=row, P=P)    
# ======================================================================



# ======================================================================
#  Auto-Generated code. Do not modify 
#  (C) Sertechno/Emtec Group (2018,2019)
#  GLVH @ 2020-02-20 16:44:44.996961
# ======================================================================
        
# gen_views_delete.html:AG 2020-02-20 16:44:44.996986
@main.route('/forms/Roles_delete', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@admin_required
def forms_Roles_delete():
    """ Delete record handling function for table Roles """
    logger.debug('forms_Roles_delete(): Enter')
    id  =  request.args.get('id',0,type=int)
    row =  Role.query.filter(Role.id == id).first()

    if row is None:
        row=Role()
    session['data'] =  {  'id':row.id, 'name':row.name, 'default':row.default, 'permissions':row.permissions }
                       
    form = frm_Role_delete()

    # Tab['has_fks'] False
    
            
    # Actual Form activation here
    if form.validate_on_submit():
    
    # Code for SAVE option
        if  form.submit_Delete.data:
            print('Delete Data Here...')

    
    #f.write(        "            print('Delete Data Here...')
            try:
                session['deleted_row']=str(row)
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                logger.audit ( '%s:DEL:%s' % (current_user.username,session['deleted_row']) )
                flash('Role id deleted OK')
            except exc.IntegrityError as e:
                db.session.rollback()    
                flash('INTEGRITY ERROR: Are you sure there are no dependant records in other tables?')
                return redirect(url_for('.forms_Roles_delete',id=session['data']['id']))    
    
            return redirect(url_for('.select_Roles_query'))    
    # Code for CANCEL option 
        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
            return redirect(url_for('.select_Roles_query'))    
    # Code for ANY OTHER option should never get here
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.select_Roles_query'))    
    
    logger.debug('forms_Roles_delete(): Exit')
    return render_template('roles_delete.html', form=form, data=session.get('data'),row=row)
#===============================================================================

# ======================================================================
#  Auto-Generated code. Do not modify 
#  (C) Sertechno/Emtec Group (2018,2019)
#  GLVH @ 2020-02-20 16:44:45.045963
# ======================================================================


from pprint import pprint, pformat

# gen_views_select_query.html:AG 2020-02-20 16:44:45.046037        
@main.route('/select/Roles_Query', methods=['GET','POST'])
@login_required
@admin_required
def select_Roles_query():
    """ Select rows handling function for table 'Roles' """
    logger.debug('select_Roles_query(): Enter')
    chk_c000001(filename=os.path.join(current_app.root_path, '.c000001'),request=request,db=db,logger=logger)
    # Get parameters from URL call
    ia       =  request.args.get('ia',     None,type=str)
    if ia is not None:
        ia=ia.split(',')
        if ia[0]=='ORDER':
            set_query_option(engine=db.engine,Interface=Interface,User_Id=current_user.id,Table_name='Role',Option_Type=OPTION_ORDER_BY,Argument_1=ia[1],Argument_2=ia[2])
        elif ia[0]=='GROUP':
            set_query_option(engine=db.engine,Interface=Interface,User_Id=current_user.id,Table_name='Role',Option_Type=OPTION_GROUP_BY,Argument_1=ia[1])
        elif ia[0]=='LIMIT':
            set_query_option(engine=db.engine,Interface=Interface,User_Id=current_user.id,Table_name='Role',Option_Type=OPTION_LIMIT,Argument_1=ia[1])

    iad      =  request.args.get('iad',     None,type=int)
    if iad is not None: delete_query_option(engine=db.engine,Interface=Interface,Id=iad) 
    
    field    =  request.args.get('field',   None,type=str)
    value    =  request.args.get('value',   None,type=str)
    
    # Populates a list of foreign keys used for advanced filtering
    # ------------------------------------------------------------------
    foreign_keys={}
    
    # ------------------------------------------------------------------
    
    if field is not None:
        reset_query_options(    engine=db.engine,Interface=Interface,
                                User_Id=current_user.id,
                                Table_name='Role'
                                )

        
        if field in foreign_keys.keys():
            Class,referenced_classname,referenced_Field,referenced_Value,column_Header=foreign_keys[field]
            foreign_field='%s.%s:%s'%(referenced_classname,referenced_Value,column_Header)
            foreign_record=Class.query.get(value)
            foreign_description="'%s'"%getattr(foreign_record,referenced_Value)
        set_query_option(   engine=db.engine,Interface=Interface,
                        User_Id=current_user.id,
                        Table_name='Role',
                        Option_Type=OPTION_FILTER,
                        Argument_1=foreign_field,
                        Argument_2='==',
                        Argument_3=foreign_description
                        )
    page     =  request.args.get('page',    1   ,type=int)
    addx     =  request.args.get('add.x',   None,type=int)
    addy     =  request.args.get('add.y',   None,type=int)
    exportx  =  request.args.get('export.x',None,type=int)
    exporty  =  request.args.get('export.y',None,type=int)
    filterx  =  request.args.get('filter.x',None,type=int)
    filtery  =  request.args.get('filter.y',None,type=int)
    # Select excluyent view mode
    if   addx    is not None: mode = 'add'
    elif exportx is not None: mode = 'export'
    elif filterx is not None: mode = 'filter'
    else:                     mode = 'select'
    id =  request.args.get('id',None,type=str)
    name =  request.args.get('name',None,type=str)
    default =  request.args.get('default',None,type=str)
    permissions =  request.args.get('permissions',None,type=str)
    
    
    # Build default query all fields from table
    
    if id is not None and len(id)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='Role',
                Option_Type=OPTION_FILTER,
                Argument_1='id:id',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%id
                )
    
    
    if name is not None and len(name)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='Role',
                Option_Type=OPTION_FILTER,
                Argument_1='name:name',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%name
                )
    
    
    if default is not None and len(default)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='Role',
                Option_Type=OPTION_FILTER,
                Argument_1='default:default',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%default
                )
    
    
    if permissions is not None and len(permissions)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='Role',
                Option_Type=OPTION_FILTER,
                Argument_1='permissions:permissions',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%permissions
                )
    
    
    
    statement_query,options=get_query_options(engine=db.engine,Interface=Interface,Table_name='Role',User_Id=current_user.id)
    query=eval(statement_query)
    filtered_query = query    
    if mode == 'filter':
        query=filtered_query
    elif mode == 'export':
        query=filtered_query
        fh,output_file = tempfile.mkstemp(suffix='', prefix='Roles_', dir=None, text=False)
        dict = {'header':{},'detail':[]}
        count = 0
        rows = query.all()
        for row in rows:
            dict['detail'].append({})
            for column in ['id', 'name', 'default', 'permissions']:
                dict['detail'][count].update( { column:str(row.__getattribute__(column))})
                
            count += 1
        dict['header'].update({'count':count})
        jsonarray      = json.dumps(dict)
        data           = json.loads(jsonarray)  
        dataframe      = json_normalize(data, 'detail').assign(**data['header'])
        fh,output_file = tempfile.mkstemp(suffix='', prefix='Roles_', dir='/tmp', text=False)
        xlsx_file      = '%s/%s'%(current_app.root_path,url_for('static',filename='%s.xls'%(output_file)))
        dataframe.to_excel(xlsx_file,sheet_name='Roles',columns=['id', 'name', 'default', 'permissions'])
        return send_file(xlsx_file,as_attachment=True,attachment_filename=output_file.replace('/','_')+'.xls')
    elif mode == 'add':
        return redirect(url_for('.forms_Roles'))
    elif mode == 'select':
        pass
        # if some filter is required
        if field is not None:
            if field == 'id':
                if value is not None:
                    query = query.filter_by(id=value)
            if field == 'name':
                if value is not None:
                    query = query.filter_by(name=value)
            if field == 'default':
                if value is not None:
                    query = query.filter_by(default=value)
            if field == 'permissions':
                if value is not None:
                    query = query.filter_by(permissions=value)
            
    # Actual request from DB follows
    tracebox_log(query,logger,length=50)
    rows = query.paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
    # Setting pagination variables ...
    if field is not None:
       next_url = url_for('.select_Roles_query', field=field, value=value, page=rows.next_num) if rows.has_next else None
       prev_url = url_for('.select_Roles_query', field=field, value=value, page=rows.prev_num) if rows.has_prev else None
    else:
       next_url = url_for('.select_Roles_query', page=rows.next_num) if rows.has_next else None
       prev_url = url_for('.select_Roles_query', page=rows.prev_num) if rows.has_prev else None
    # Actual rendering ...
    if request.headers.get('Content-Type') is not None or request.args.get('JSON',None,type=str) is not None:
        if "JSON" in request.headers.get('Content-Type') or request.args.get('JSON',None,type=str) is not None:
            logger.debug('select_Roles_query(): will render: JSON rows')
            logger.debug('select_Roles_query(): Exit')
            return json.dumps(serialize_object(rows.__dict__))
    logger.debug('select_Roles_query(): will render: roles_All.html')
    logger.debug('select_Roles_query(): Exit')
    return render_template('roles_select_All.html',rows=rows,options=options)
#===============================================================================
   # NOTE: HARDCODE. TO REMOVE --------------------------------------------
def chk_c000001(*args,**kwargs):
    pass
    
from emtec.common.interface import *
from emtec.collector.db.orm_model          import Interface
from emtec.collector.db.flask_models       import interface
#-----------------------------------------------------------------------
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2020-02-20 16:44:35
# =============================================================================

# ======================================================================
#  Auto-Generated code. Do not modify 
#  (C) Sertechno/Emtec Group (2018,2019)
#  GLVH @ 2020-02-20 16:44:45.428406
# ======================================================================
        
# gen_views_form.html:AG 2020-02-20 16:44:45.428429
@main.route('/forms/ST_Use_Per_CU', methods=['GET', 'POST'])
@login_required

def forms_ST_Use_Per_CU():
    """ Form handling function for table ST_Use_Per_CU """
    logger.debug('forms_ST_Use_Per_CU(): Enter')
    CU_Id  =  request.args.get('CU_Id',0,type=int)
    From  =  request.args.get('From',0,type=int)
    To  =  request.args.get('To',0,type=int)
    
    row =  st_use_per_cu.query.filter(st_use_per_cu.CU_Id == CU_Id,st_use_per_cu.From == From,st_use_per_cu.To == To).first()
    if row is None:
        row=st_use_per_cu()
        session['is_new_row']=True
    session['data'] =  {  'CU_Id':row.CU_Id, 'From':row.From, 'To':row.To, 'Total_Slices':row.Total_Slices, 'Found_Slices':row.Found_Slices, 'Not_Found_Slices':row.Not_Found_Slices, 'Period_Initial_Q':row.Period_Initial_Q, 'Period_Increase':row.Period_Increase, 'Period_Increase_Count':row.Period_Increase_Count, 'Period_Reduction':row.Period_Reduction, 'Period_Reduction_Count':row.Period_Reduction_Count, 'Period_Final_Q':row.Period_Final_Q, 'CI_Id':row.CI_Id, 'CC_Id':row.CC_Id, 'Cus_Id':row.Cus_Id, 'Rat_Id':row.Rat_Id, 'Typ_Code':row.Typ_Code, 'Pla_Id':row.Pla_Id, 'Mean':row.Mean, 'Variance':row.Variance, 'StdDev':row.StdDev, 'Min':row.Min, 'Max':row.Max }
    
    form = frm_st_use_per_cu()
    
    # Actual Form activation here
    if form.validate_on_submit():
    # Code for SAVE option
        if form.submit_Save.data and current_user.role_id > 1:
    
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
                   flash('New ST Use Per CU created OK')
               else:
                   logger.audit ( '%s:OLD:%s' % (current_user.username,session['prev_row']) )
                   logger.audit ( '%s:UPD:%s' % (current_user.username,session['new_row'] ) )    
                   message=Markup('<b>ST Use Per CU CU_Id,From,To saved OK</b>')
                   flash(message)
               db.session.close()
            except Exception as e:
               db.session.rollback()
               db.session.close()
               message=Markup('ERROR saving ST Use Per CU record : %s'%(e))
               flash(message)
            return redirect(url_for('.select_ST_Use_Per_CU_query'))    
    # Code for NEW option
    # GV 20190109 f.write(        "        elif   form.submit_New.data:\n")
        elif   form.submit_New.data and current_user.role_id>1:
            #print('New Data Here ...')
            session['is_new_row']=True
            db.session.close()
            row=st_use_per_cu()
    
            return redirect(url_for('.forms_ST_Use_Per_CU'))    
    
    # Code for CANCEL option 
        elif   form.submit_Cancel.data:
            #print('Cancel Data Here ... does nothing')
            message=Markup('ST Use Per CU Record modifications discarded ...')
            flash(message)
    # Code for ANY OTHER option should never get here
        else:
            #print('form validated but not submited ???')
            message=Markup("<b>ST Use Per CU data modifications not allowed for user '%s'. Please contact EG Suite's Administrator ...</b>"%(current_user.username))    
            flash(message)
    
            return redirect(url_for('.forms_'))    
    
    
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
    session['prev_row'] = str(row)
    session['is_new_row'] = False
    logger.debug('forms_ST_Use_Per_CU(): Exit')
    # Generates pagination data here
    P=[]
    # Tab Relations = []
    
    # Generation of pagination data completed       
    return render_template('st_use_per_cu.html', form=form, row=row, P=P)    
# ======================================================================



# ======================================================================
#  Auto-Generated code. Do not modify 
#  (C) Sertechno/Emtec Group (2018,2019)
#  GLVH @ 2020-02-20 16:44:45.457048
# ======================================================================
        
# gen_views_delete.html:AG 2020-02-20 16:44:45.457073
@main.route('/forms/ST_Use_Per_CU_delete', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)

def forms_ST_Use_Per_CU_delete():
    """ Delete record handling function for table ST_Use_Per_CU """
    logger.debug('forms_ST_Use_Per_CU_delete(): Enter')
    CU_Id  =  request.args.get('CU_Id',0,type=int)
    From  =  request.args.get('From',0,type=int)
    To  =  request.args.get('To',0,type=int)
    row =  st_use_per_cu.query.filter(st_use_per_cu.CU_Id == CU_Id,st_use_per_cu.From == From,st_use_per_cu.To == To).first()

    if row is None:
        row=st_use_per_cu()
    session['data'] =  {  'CU_Id':row.CU_Id, 'From':row.From, 'To':row.To, 'Total_Slices':row.Total_Slices, 'Found_Slices':row.Found_Slices, 'Not_Found_Slices':row.Not_Found_Slices, 'Period_Initial_Q':row.Period_Initial_Q, 'Period_Increase':row.Period_Increase, 'Period_Increase_Count':row.Period_Increase_Count, 'Period_Reduction':row.Period_Reduction, 'Period_Reduction_Count':row.Period_Reduction_Count, 'Period_Final_Q':row.Period_Final_Q, 'CI_Id':row.CI_Id, 'CC_Id':row.CC_Id, 'Cus_Id':row.Cus_Id, 'Rat_Id':row.Rat_Id, 'Typ_Code':row.Typ_Code, 'Pla_Id':row.Pla_Id, 'Mean':row.Mean, 'Variance':row.Variance, 'StdDev':row.StdDev, 'Min':row.Min, 'Max':row.Max }
                       
    form = frm_st_use_per_cu_delete()

    # Tab['has_fks'] False
    
            
    # Actual Form activation here
    if form.validate_on_submit():
    
    # Code for SAVE option
        if  form.submit_Delete.data:
            print('Delete Data Here...')

    
    #f.write(        "            print('Delete Data Here...')
            try:
                session['deleted_row']=str(row)
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                logger.audit ( '%s:DEL:%s' % (current_user.username,session['deleted_row']) )
                flash('ST Use Per CU CU_Id,From,To deleted OK')
            except exc.IntegrityError as e:
                db.session.rollback()    
                flash('INTEGRITY ERROR: Are you sure there are no dependant records in other tables?')
                return redirect(url_for('.forms_ST_Use_Per_CU_delete',CU_Id=session['data']['CU_Id'],From=session['data']['From'],To=session['data']['To']))    
    
            return redirect(url_for('.select_ST_Use_Per_CU_query'))    
    # Code for CANCEL option 
        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
            return redirect(url_for('.select_ST_Use_Per_CU_query'))    
    # Code for ANY OTHER option should never get here
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.select_ST_Use_Per_CU_query'))    
    
    logger.debug('forms_ST_Use_Per_CU_delete(): Exit')
    return render_template('st_use_per_cu_delete.html', form=form, data=session.get('data'),row=row)
#===============================================================================

# ======================================================================
#  Auto-Generated code. Do not modify 
#  (C) Sertechno/Emtec Group (2018,2019)
#  GLVH @ 2020-02-20 16:44:45.511005
# ======================================================================


from pprint import pprint, pformat

# gen_views_select_query.html:AG 2020-02-20 16:44:45.511030        
@main.route('/select/ST_Use_Per_CU_Query', methods=['GET','POST'])
@login_required

def select_ST_Use_Per_CU_query():
    """ Select rows handling function for table 'ST_Use_Per_CU' """
    logger.debug('select_ST_Use_Per_CU_query(): Enter')
    chk_c000001(filename=os.path.join(current_app.root_path, '.c000001'),request=request,db=db,logger=logger)
    # Get parameters from URL call
    ia       =  request.args.get('ia',     None,type=str)
    if ia is not None:
        ia=ia.split(',')
        if ia[0]=='ORDER':
            set_query_option(engine=db.engine,Interface=Interface,User_Id=current_user.id,Table_name='st_use_per_cu',Option_Type=OPTION_ORDER_BY,Argument_1=ia[1],Argument_2=ia[2])
        elif ia[0]=='GROUP':
            set_query_option(engine=db.engine,Interface=Interface,User_Id=current_user.id,Table_name='st_use_per_cu',Option_Type=OPTION_GROUP_BY,Argument_1=ia[1])
        elif ia[0]=='LIMIT':
            set_query_option(engine=db.engine,Interface=Interface,User_Id=current_user.id,Table_name='st_use_per_cu',Option_Type=OPTION_LIMIT,Argument_1=ia[1])

    iad      =  request.args.get('iad',     None,type=int)
    if iad is not None: delete_query_option(engine=db.engine,Interface=Interface,Id=iad) 
    
    field    =  request.args.get('field',   None,type=str)
    value    =  request.args.get('value',   None,type=str)
    
    # Populates a list of foreign keys used for advanced filtering
    # ------------------------------------------------------------------
    foreign_keys={}
    
    # ------------------------------------------------------------------
    
    if field is not None:
        reset_query_options(    engine=db.engine,Interface=Interface,
                                User_Id=current_user.id,
                                Table_name='st_use_per_cu'
                                )

        
        if field in foreign_keys.keys():
            Class,referenced_classname,referenced_Field,referenced_Value,column_Header=foreign_keys[field]
            foreign_field='%s.%s:%s'%(referenced_classname,referenced_Value,column_Header)
            foreign_record=Class.query.get(value)
            foreign_description="'%s'"%getattr(foreign_record,referenced_Value)
        set_query_option(   engine=db.engine,Interface=Interface,
                        User_Id=current_user.id,
                        Table_name='st_use_per_cu',
                        Option_Type=OPTION_FILTER,
                        Argument_1=foreign_field,
                        Argument_2='==',
                        Argument_3=foreign_description
                        )
    page     =  request.args.get('page',    1   ,type=int)
    addx     =  request.args.get('add.x',   None,type=int)
    addy     =  request.args.get('add.y',   None,type=int)
    exportx  =  request.args.get('export.x',None,type=int)
    exporty  =  request.args.get('export.y',None,type=int)
    filterx  =  request.args.get('filter.x',None,type=int)
    filtery  =  request.args.get('filter.y',None,type=int)
    # Select excluyent view mode
    if   addx    is not None: mode = 'add'
    elif exportx is not None: mode = 'export'
    elif filterx is not None: mode = 'filter'
    else:                     mode = 'select'
    CU_Id =  request.args.get('CU_Id',None,type=str)
    From =  request.args.get('From',None,type=str)
    To =  request.args.get('To',None,type=str)
    Total_Slices =  request.args.get('Total_Slices',None,type=str)
    Found_Slices =  request.args.get('Found_Slices',None,type=str)
    Not_Found_Slices =  request.args.get('Not_Found_Slices',None,type=str)
    Period_Initial_Q =  request.args.get('Period_Initial_Q',None,type=str)
    Period_Increase =  request.args.get('Period_Increase',None,type=str)
    Period_Increase_Count =  request.args.get('Period_Increase_Count',None,type=str)
    Period_Reduction =  request.args.get('Period_Reduction',None,type=str)
    Period_Reduction_Count =  request.args.get('Period_Reduction_Count',None,type=str)
    Period_Final_Q =  request.args.get('Period_Final_Q',None,type=str)
    CI_Id =  request.args.get('CI_Id',None,type=str)
    CC_Id =  request.args.get('CC_Id',None,type=str)
    Cus_Id =  request.args.get('Cus_Id',None,type=str)
    Rat_Id =  request.args.get('Rat_Id',None,type=str)
    Typ_Code =  request.args.get('Typ_Code',None,type=str)
    Pla_Id =  request.args.get('Pla_Id',None,type=str)
    Mean =  request.args.get('Mean',None,type=str)
    Variance =  request.args.get('Variance',None,type=str)
    StdDev =  request.args.get('StdDev',None,type=str)
    Min =  request.args.get('Min',None,type=str)
    Max =  request.args.get('Max',None,type=str)
    
    
    # Build default query all fields from table
    
    if CU_Id is not None and len(CU_Id)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='st_use_per_cu',
                Option_Type=OPTION_FILTER,
                Argument_1='CU_Id:CU_Id',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%CU_Id
                )
    
    
    if From is not None and len(From)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='st_use_per_cu',
                Option_Type=OPTION_FILTER,
                Argument_1='From:From',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%From
                )
    
    
    if To is not None and len(To)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='st_use_per_cu',
                Option_Type=OPTION_FILTER,
                Argument_1='To:To',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%To
                )
    
    
    if Total_Slices is not None and len(Total_Slices)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='st_use_per_cu',
                Option_Type=OPTION_FILTER,
                Argument_1='Total_Slices:Total_Slices',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Total_Slices
                )
    
    
    if Found_Slices is not None and len(Found_Slices)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='st_use_per_cu',
                Option_Type=OPTION_FILTER,
                Argument_1='Found_Slices:Found_Slices',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Found_Slices
                )
    
    
    if Not_Found_Slices is not None and len(Not_Found_Slices)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='st_use_per_cu',
                Option_Type=OPTION_FILTER,
                Argument_1='Not_Found_Slices:Not_Found_Slices',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Not_Found_Slices
                )
    
    
    if Period_Initial_Q is not None and len(Period_Initial_Q)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='st_use_per_cu',
                Option_Type=OPTION_FILTER,
                Argument_1='Period_Initial_Q:Period_Initial_Q',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Period_Initial_Q
                )
    
    
    if Period_Increase is not None and len(Period_Increase)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='st_use_per_cu',
                Option_Type=OPTION_FILTER,
                Argument_1='Period_Increase:Period_Increase',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Period_Increase
                )
    
    
    if Period_Increase_Count is not None and len(Period_Increase_Count)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='st_use_per_cu',
                Option_Type=OPTION_FILTER,
                Argument_1='Period_Increase_Count:Period_Increase_Count',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Period_Increase_Count
                )
    
    
    if Period_Reduction is not None and len(Period_Reduction)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='st_use_per_cu',
                Option_Type=OPTION_FILTER,
                Argument_1='Period_Reduction:Period_Reduction',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Period_Reduction
                )
    
    
    if Period_Reduction_Count is not None and len(Period_Reduction_Count)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='st_use_per_cu',
                Option_Type=OPTION_FILTER,
                Argument_1='Period_Reduction_Count:Period_Reduction_Count',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Period_Reduction_Count
                )
    
    
    if Period_Final_Q is not None and len(Period_Final_Q)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='st_use_per_cu',
                Option_Type=OPTION_FILTER,
                Argument_1='Period_Final_Q:Period_Final_Q',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Period_Final_Q
                )
    
    
    if CI_Id is not None and len(CI_Id)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='st_use_per_cu',
                Option_Type=OPTION_FILTER,
                Argument_1='CI_Id:CI_Id',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%CI_Id
                )
    
    
    if CC_Id is not None and len(CC_Id)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='st_use_per_cu',
                Option_Type=OPTION_FILTER,
                Argument_1='CC_Id:CC_Id',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%CC_Id
                )
    
    
    if Cus_Id is not None and len(Cus_Id)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='st_use_per_cu',
                Option_Type=OPTION_FILTER,
                Argument_1='Cus_Id:Cus_Id',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Cus_Id
                )
    
    
    if Rat_Id is not None and len(Rat_Id)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='st_use_per_cu',
                Option_Type=OPTION_FILTER,
                Argument_1='Rat_Id:Rat_id',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Rat_Id
                )
    
    
    if Typ_Code is not None and len(Typ_Code)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='st_use_per_cu',
                Option_Type=OPTION_FILTER,
                Argument_1='Typ_Code:Typ_Code',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Typ_Code
                )
    
    
    if Pla_Id is not None and len(Pla_Id)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='st_use_per_cu',
                Option_Type=OPTION_FILTER,
                Argument_1='Pla_Id:Pla_Id',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Pla_Id
                )
    
    
    if Mean is not None and len(Mean)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='st_use_per_cu',
                Option_Type=OPTION_FILTER,
                Argument_1='Mean:Mean',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Mean
                )
    
    
    if Variance is not None and len(Variance)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='st_use_per_cu',
                Option_Type=OPTION_FILTER,
                Argument_1='Variance:Variance',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Variance
                )
    
    
    if StdDev is not None and len(StdDev)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='st_use_per_cu',
                Option_Type=OPTION_FILTER,
                Argument_1='StdDev:StdDev',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%StdDev
                )
    
    
    if Min is not None and len(Min)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='st_use_per_cu',
                Option_Type=OPTION_FILTER,
                Argument_1='Min:Min',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Min
                )
    
    
    if Max is not None and len(Max)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='st_use_per_cu',
                Option_Type=OPTION_FILTER,
                Argument_1='Max:Max',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Max
                )
    
    
    
    statement_query,options=get_query_options(engine=db.engine,Interface=Interface,Table_name='st_use_per_cu',User_Id=current_user.id)
    query=eval(statement_query)
    filtered_query = query    
    if mode == 'filter':
        query=filtered_query
    elif mode == 'export':
        query=filtered_query
        fh,output_file = tempfile.mkstemp(suffix='', prefix='ST_Use_Per_CU_', dir=None, text=False)
        dict = {'header':{},'detail':[]}
        count = 0
        rows = query.all()
        for row in rows:
            dict['detail'].append({})
            for column in ['CU_Id', 'From', 'To', 'Total_Slices', 'Found_Slices', 'Not_Found_Slices', 'Period_Initial_Q', 'Period_Increase', 'Period_Increase_Count', 'Period_Reduction', 'Period_Reduction_Count', 'Period_Final_Q', 'CI_Id', 'CC_Id', 'Cus_Id', 'Rat_Id', 'Typ_Code', 'Pla_Id', 'Mean', 'Variance', 'StdDev', 'Min', 'Max']:
                dict['detail'][count].update( { column:str(row.__getattribute__(column))})
                
            count += 1
        dict['header'].update({'count':count})
        jsonarray      = json.dumps(dict)
        data           = json.loads(jsonarray)  
        dataframe      = json_normalize(data, 'detail').assign(**data['header'])
        fh,output_file = tempfile.mkstemp(suffix='', prefix='ST_Use_Per_CU_', dir='/tmp', text=False)
        xlsx_file      = '%s/%s'%(current_app.root_path,url_for('static',filename='%s.xls'%(output_file)))
        dataframe.to_excel(xlsx_file,sheet_name='ST_Use_Per_CU',columns=['CU_Id', 'From', 'To', 'Total_Slices', 'Found_Slices', 'Not_Found_Slices', 'Period_Initial_Q', 'Period_Increase', 'Period_Increase_Count', 'Period_Reduction', 'Period_Reduction_Count', 'Period_Final_Q', 'CI_Id', 'CC_Id', 'Cus_Id', 'Rat_Id', 'Typ_Code', 'Pla_Id', 'Mean', 'Variance', 'StdDev', 'Min', 'Max'])
        return send_file(xlsx_file,as_attachment=True,attachment_filename=output_file.replace('/','_')+'.xls')
    elif mode == 'add':
        return redirect(url_for('.forms_ST_Use_Per_CU'))
    elif mode == 'select':
        pass
        # if some filter is required
        if field is not None:
            if field == 'CU_Id':
                if value is not None:
                    query = query.filter_by(CU_Id=value)
            if field == 'From':
                if value is not None:
                    query = query.filter_by(From=value)
            if field == 'To':
                if value is not None:
                    query = query.filter_by(To=value)
            if field == 'Total_Slices':
                if value is not None:
                    query = query.filter_by(Total_Slices=value)
            if field == 'Found_Slices':
                if value is not None:
                    query = query.filter_by(Found_Slices=value)
            if field == 'Not_Found_Slices':
                if value is not None:
                    query = query.filter_by(Not_Found_Slices=value)
            if field == 'Period_Initial_Q':
                if value is not None:
                    query = query.filter_by(Period_Initial_Q=value)
            if field == 'Period_Increase':
                if value is not None:
                    query = query.filter_by(Period_Increase=value)
            if field == 'Period_Increase_Count':
                if value is not None:
                    query = query.filter_by(Period_Increase_Count=value)
            if field == 'Period_Reduction':
                if value is not None:
                    query = query.filter_by(Period_Reduction=value)
            if field == 'Period_Reduction_Count':
                if value is not None:
                    query = query.filter_by(Period_Reduction_Count=value)
            if field == 'Period_Final_Q':
                if value is not None:
                    query = query.filter_by(Period_Final_Q=value)
            if field == 'CI_Id':
                if value is not None:
                    query = query.filter_by(CI_Id=value)
            if field == 'CC_Id':
                if value is not None:
                    query = query.filter_by(CC_Id=value)
            if field == 'Cus_Id':
                if value is not None:
                    query = query.filter_by(Cus_Id=value)
            if field == 'Rat_Id':
                if value is not None:
                    query = query.filter_by(Rat_Id=value)
            if field == 'Typ_Code':
                if value is not None:
                    query = query.filter_by(Typ_Code=value)
            if field == 'Pla_Id':
                if value is not None:
                    query = query.filter_by(Pla_Id=value)
            if field == 'Mean':
                if value is not None:
                    query = query.filter_by(Mean=value)
            if field == 'Variance':
                if value is not None:
                    query = query.filter_by(Variance=value)
            if field == 'StdDev':
                if value is not None:
                    query = query.filter_by(StdDev=value)
            if field == 'Min':
                if value is not None:
                    query = query.filter_by(Min=value)
            if field == 'Max':
                if value is not None:
                    query = query.filter_by(Max=value)
            
    # Actual request from DB follows
    tracebox_log(query,logger,length=50)
    rows = query.paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
    # Setting pagination variables ...
    if field is not None:
       next_url = url_for('.select_ST_Use_Per_CU_query', field=field, value=value, page=rows.next_num) if rows.has_next else None
       prev_url = url_for('.select_ST_Use_Per_CU_query', field=field, value=value, page=rows.prev_num) if rows.has_prev else None
    else:
       next_url = url_for('.select_ST_Use_Per_CU_query', page=rows.next_num) if rows.has_next else None
       prev_url = url_for('.select_ST_Use_Per_CU_query', page=rows.prev_num) if rows.has_prev else None
    # Actual rendering ...
    if request.headers.get('Content-Type') is not None or request.args.get('JSON',None,type=str) is not None:
        if "JSON" in request.headers.get('Content-Type') or request.args.get('JSON',None,type=str) is not None:
            logger.debug('select_ST_Use_Per_CU_query(): will render: JSON rows')
            logger.debug('select_ST_Use_Per_CU_query(): Exit')
            return json.dumps(serialize_object(rows.__dict__))
    logger.debug('select_ST_Use_Per_CU_query(): will render: st_use_per_cu_All.html')
    logger.debug('select_ST_Use_Per_CU_query(): Exit')
    return render_template('st_use_per_cu_select_All.html',rows=rows,options=options)
#===============================================================================
   # NOTE: HARDCODE. TO REMOVE --------------------------------------------
def chk_c000001(*args,**kwargs):
    pass
    
from emtec.common.interface import *
from emtec.collector.db.orm_model          import Interface
from emtec.collector.db.flask_models       import interface
#-----------------------------------------------------------------------
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2020-02-20 16:44:35
# =============================================================================

# ======================================================================
#  Auto-Generated code. Do not modify 
#  (C) Sertechno/Emtec Group (2018,2019)
#  GLVH @ 2020-02-20 16:44:45.858673
# ======================================================================
        
# gen_views_form.html:AG 2020-02-20 16:44:45.858697
@main.route('/forms/ST_Use_Per_Type', methods=['GET', 'POST'])
@login_required

def forms_ST_Use_Per_Type():
    """ Form handling function for table ST_Use_Per_Type """
    logger.debug('forms_ST_Use_Per_Type(): Enter')
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
    session['data'] =  {  'Typ_Code':row.Typ_Code, 'Cus_Id':row.Cus_Id, 'Pla_Id':row.Pla_Id, 'CC_Id':row.CC_Id, 'CI_Id':row.CI_Id, 'Year':row.Year, 'Month':row.Month, 'Count':row.Count, 'Mean':row.Mean, 'Variance':row.Variance, 'StdDev':row.StdDev, 'Min':row.Min, 'Max':row.Max }
    
    form = frm_st_use_per_type()
    
    # Actual Form activation here
    if form.validate_on_submit():
    # Code for SAVE option
        if form.submit_Save.data and current_user.role_id > 1:
    
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
                   flash('New ST Use Per Type created OK')
               else:
                   logger.audit ( '%s:OLD:%s' % (current_user.username,session['prev_row']) )
                   logger.audit ( '%s:UPD:%s' % (current_user.username,session['new_row'] ) )    
                   message=Markup('<b>ST Use Per Type Typ_Code,Cus_Id,Pla_Id,CC_Id,CI_Id,Year,Month saved OK</b>')
                   flash(message)
               db.session.close()
            except Exception as e:
               db.session.rollback()
               db.session.close()
               message=Markup('ERROR saving ST Use Per Type record : %s'%(e))
               flash(message)
            return redirect(url_for('.select_ST_Use_Per_Type_query'))    
    # Code for NEW option
    # GV 20190109 f.write(        "        elif   form.submit_New.data:\n")
        elif   form.submit_New.data and current_user.role_id>1:
            #print('New Data Here ...')
            session['is_new_row']=True
            db.session.close()
            row=st_use_per_type()
    
            return redirect(url_for('.forms_ST_Use_Per_Type'))    
    
    # Code for CANCEL option 
        elif   form.submit_Cancel.data:
            #print('Cancel Data Here ... does nothing')
            message=Markup('ST Use Per Type Record modifications discarded ...')
            flash(message)
    # Code for ANY OTHER option should never get here
        else:
            #print('form validated but not submited ???')
            message=Markup("<b>ST Use Per Type data modifications not allowed for user '%s'. Please contact EG Suite's Administrator ...</b>"%(current_user.username))    
            flash(message)
    
            return redirect(url_for('.forms_'))    
    
    
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
    session['prev_row'] = str(row)
    session['is_new_row'] = False
    logger.debug('forms_ST_Use_Per_Type(): Exit')
    # Generates pagination data here
    P=[]
    # Tab Relations = []
    
    # Generation of pagination data completed       
    return render_template('st_use_per_type.html', form=form, row=row, P=P)    
# ======================================================================



# ======================================================================
#  Auto-Generated code. Do not modify 
#  (C) Sertechno/Emtec Group (2018,2019)
#  GLVH @ 2020-02-20 16:44:45.883732
# ======================================================================
        
# gen_views_delete.html:AG 2020-02-20 16:44:45.883756
@main.route('/forms/ST_Use_Per_Type_delete', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)

def forms_ST_Use_Per_Type_delete():
    """ Delete record handling function for table ST_Use_Per_Type """
    logger.debug('forms_ST_Use_Per_Type_delete(): Enter')
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
    session['data'] =  {  'Typ_Code':row.Typ_Code, 'Cus_Id':row.Cus_Id, 'Pla_Id':row.Pla_Id, 'CC_Id':row.CC_Id, 'CI_Id':row.CI_Id, 'Year':row.Year, 'Month':row.Month, 'Count':row.Count, 'Mean':row.Mean, 'Variance':row.Variance, 'StdDev':row.StdDev, 'Min':row.Min, 'Max':row.Max }
                       
    form = frm_st_use_per_type_delete()

    # Tab['has_fks'] False
    
            
    # Actual Form activation here
    if form.validate_on_submit():
    
    # Code for SAVE option
        if  form.submit_Delete.data:
            print('Delete Data Here...')

    
    #f.write(        "            print('Delete Data Here...')
            try:
                session['deleted_row']=str(row)
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                logger.audit ( '%s:DEL:%s' % (current_user.username,session['deleted_row']) )
                flash('ST Use Per Type Typ_Code,Cus_Id,Pla_Id,CC_Id,CI_Id,Year,Month deleted OK')
            except exc.IntegrityError as e:
                db.session.rollback()    
                flash('INTEGRITY ERROR: Are you sure there are no dependant records in other tables?')
                return redirect(url_for('.forms_ST_Use_Per_Type_delete',Typ_Code=session['data']['Typ_Code'],Cus_Id=session['data']['Cus_Id'],Pla_Id=session['data']['Pla_Id'],CC_Id=session['data']['CC_Id'],CI_Id=session['data']['CI_Id'],Year=session['data']['Year'],Month=session['data']['Month']))    
    
            return redirect(url_for('.select_ST_Use_Per_Type_query'))    
    # Code for CANCEL option 
        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
            return redirect(url_for('.select_ST_Use_Per_Type_query'))    
    # Code for ANY OTHER option should never get here
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.select_ST_Use_Per_Type_query'))    
    
    logger.debug('forms_ST_Use_Per_Type_delete(): Exit')
    return render_template('st_use_per_type_delete.html', form=form, data=session.get('data'),row=row)
#===============================================================================

# ======================================================================
#  Auto-Generated code. Do not modify 
#  (C) Sertechno/Emtec Group (2018,2019)
#  GLVH @ 2020-02-20 16:44:45.950858
# ======================================================================


from pprint import pprint, pformat

# gen_views_select_query.html:AG 2020-02-20 16:44:45.950884        
@main.route('/select/ST_Use_Per_Type_Query', methods=['GET','POST'])
@login_required

def select_ST_Use_Per_Type_query():
    """ Select rows handling function for table 'ST_Use_Per_Type' """
    logger.debug('select_ST_Use_Per_Type_query(): Enter')
    chk_c000001(filename=os.path.join(current_app.root_path, '.c000001'),request=request,db=db,logger=logger)
    # Get parameters from URL call
    ia       =  request.args.get('ia',     None,type=str)
    if ia is not None:
        ia=ia.split(',')
        if ia[0]=='ORDER':
            set_query_option(engine=db.engine,Interface=Interface,User_Id=current_user.id,Table_name='st_use_per_type',Option_Type=OPTION_ORDER_BY,Argument_1=ia[1],Argument_2=ia[2])
        elif ia[0]=='GROUP':
            set_query_option(engine=db.engine,Interface=Interface,User_Id=current_user.id,Table_name='st_use_per_type',Option_Type=OPTION_GROUP_BY,Argument_1=ia[1])
        elif ia[0]=='LIMIT':
            set_query_option(engine=db.engine,Interface=Interface,User_Id=current_user.id,Table_name='st_use_per_type',Option_Type=OPTION_LIMIT,Argument_1=ia[1])

    iad      =  request.args.get('iad',     None,type=int)
    if iad is not None: delete_query_option(engine=db.engine,Interface=Interface,Id=iad) 
    
    field    =  request.args.get('field',   None,type=str)
    value    =  request.args.get('value',   None,type=str)
    
    # Populates a list of foreign keys used for advanced filtering
    # ------------------------------------------------------------------
    foreign_keys={}
    
    # ------------------------------------------------------------------
    
    if field is not None:
        reset_query_options(    engine=db.engine,Interface=Interface,
                                User_Id=current_user.id,
                                Table_name='st_use_per_type'
                                )

        
        if field in foreign_keys.keys():
            Class,referenced_classname,referenced_Field,referenced_Value,column_Header=foreign_keys[field]
            foreign_field='%s.%s:%s'%(referenced_classname,referenced_Value,column_Header)
            foreign_record=Class.query.get(value)
            foreign_description="'%s'"%getattr(foreign_record,referenced_Value)
        set_query_option(   engine=db.engine,Interface=Interface,
                        User_Id=current_user.id,
                        Table_name='st_use_per_type',
                        Option_Type=OPTION_FILTER,
                        Argument_1=foreign_field,
                        Argument_2='==',
                        Argument_3=foreign_description
                        )
    page     =  request.args.get('page',    1   ,type=int)
    addx     =  request.args.get('add.x',   None,type=int)
    addy     =  request.args.get('add.y',   None,type=int)
    exportx  =  request.args.get('export.x',None,type=int)
    exporty  =  request.args.get('export.y',None,type=int)
    filterx  =  request.args.get('filter.x',None,type=int)
    filtery  =  request.args.get('filter.y',None,type=int)
    # Select excluyent view mode
    if   addx    is not None: mode = 'add'
    elif exportx is not None: mode = 'export'
    elif filterx is not None: mode = 'filter'
    else:                     mode = 'select'
    Typ_Code =  request.args.get('Typ_Code',None,type=str)
    Cus_Id =  request.args.get('Cus_Id',None,type=str)
    Pla_Id =  request.args.get('Pla_Id',None,type=str)
    CC_Id =  request.args.get('CC_Id',None,type=str)
    CI_Id =  request.args.get('CI_Id',None,type=str)
    Year =  request.args.get('Year',None,type=str)
    Month =  request.args.get('Month',None,type=str)
    Count =  request.args.get('Count',None,type=str)
    Mean =  request.args.get('Mean',None,type=str)
    Variance =  request.args.get('Variance',None,type=str)
    StdDev =  request.args.get('StdDev',None,type=str)
    Min =  request.args.get('Min',None,type=str)
    Max =  request.args.get('Max',None,type=str)
    
    
    # Build default query all fields from table
    
    if Typ_Code is not None and len(Typ_Code)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='st_use_per_type',
                Option_Type=OPTION_FILTER,
                Argument_1='Typ_Code:Typ_Code',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Typ_Code
                )
    
    
    if Cus_Id is not None and len(Cus_Id)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='st_use_per_type',
                Option_Type=OPTION_FILTER,
                Argument_1='Cus_Id:Cus_Id',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Cus_Id
                )
    
    
    if Pla_Id is not None and len(Pla_Id)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='st_use_per_type',
                Option_Type=OPTION_FILTER,
                Argument_1='Pla_Id:Pla_Id',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Pla_Id
                )
    
    
    if CC_Id is not None and len(CC_Id)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='st_use_per_type',
                Option_Type=OPTION_FILTER,
                Argument_1='CC_Id:CC_Id',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%CC_Id
                )
    
    
    if CI_Id is not None and len(CI_Id)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='st_use_per_type',
                Option_Type=OPTION_FILTER,
                Argument_1='CI_Id:CI_Id',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%CI_Id
                )
    
    
    if Year is not None and len(Year)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='st_use_per_type',
                Option_Type=OPTION_FILTER,
                Argument_1='Year:Year',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Year
                )
    
    
    if Month is not None and len(Month)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='st_use_per_type',
                Option_Type=OPTION_FILTER,
                Argument_1='Month:Month',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Month
                )
    
    
    if Count is not None and len(Count)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='st_use_per_type',
                Option_Type=OPTION_FILTER,
                Argument_1='Count:Count',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Count
                )
    
    
    if Mean is not None and len(Mean)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='st_use_per_type',
                Option_Type=OPTION_FILTER,
                Argument_1='Mean:Mean',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Mean
                )
    
    
    if Variance is not None and len(Variance)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='st_use_per_type',
                Option_Type=OPTION_FILTER,
                Argument_1='Variance:Variance',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Variance
                )
    
    
    if StdDev is not None and len(StdDev)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='st_use_per_type',
                Option_Type=OPTION_FILTER,
                Argument_1='StdDev:StdDev',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%StdDev
                )
    
    
    if Min is not None and len(Min)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='st_use_per_type',
                Option_Type=OPTION_FILTER,
                Argument_1='Min:Min',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Min
                )
    
    
    if Max is not None and len(Max)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='st_use_per_type',
                Option_Type=OPTION_FILTER,
                Argument_1='Max:Max',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Max
                )
    
    
    
    statement_query,options=get_query_options(engine=db.engine,Interface=Interface,Table_name='st_use_per_type',User_Id=current_user.id)
    query=eval(statement_query)
    filtered_query = query    
    if mode == 'filter':
        query=filtered_query
    elif mode == 'export':
        query=filtered_query
        fh,output_file = tempfile.mkstemp(suffix='', prefix='ST_Use_Per_Type_', dir=None, text=False)
        dict = {'header':{},'detail':[]}
        count = 0
        rows = query.all()
        for row in rows:
            dict['detail'].append({})
            for column in ['Typ_Code', 'Cus_Id', 'Pla_Id', 'CC_Id', 'CI_Id', 'Year', 'Month', 'Count', 'Mean', 'Variance', 'StdDev', 'Min', 'Max']:
                dict['detail'][count].update( { column:str(row.__getattribute__(column))})
                
            count += 1
        dict['header'].update({'count':count})
        jsonarray      = json.dumps(dict)
        data           = json.loads(jsonarray)  
        dataframe      = json_normalize(data, 'detail').assign(**data['header'])
        fh,output_file = tempfile.mkstemp(suffix='', prefix='ST_Use_Per_Type_', dir='/tmp', text=False)
        xlsx_file      = '%s/%s'%(current_app.root_path,url_for('static',filename='%s.xls'%(output_file)))
        dataframe.to_excel(xlsx_file,sheet_name='ST_Use_Per_Type',columns=['Typ_Code', 'Cus_Id', 'Pla_Id', 'CC_Id', 'CI_Id', 'Year', 'Month', 'Count', 'Mean', 'Variance', 'StdDev', 'Min', 'Max'])
        return send_file(xlsx_file,as_attachment=True,attachment_filename=output_file.replace('/','_')+'.xls')
    elif mode == 'add':
        return redirect(url_for('.forms_ST_Use_Per_Type'))
    elif mode == 'select':
        pass
        # if some filter is required
        if field is not None:
            if field == 'Typ_Code':
                if value is not None:
                    query = query.filter_by(Typ_Code=value)
            if field == 'Cus_Id':
                if value is not None:
                    query = query.filter_by(Cus_Id=value)
            if field == 'Pla_Id':
                if value is not None:
                    query = query.filter_by(Pla_Id=value)
            if field == 'CC_Id':
                if value is not None:
                    query = query.filter_by(CC_Id=value)
            if field == 'CI_Id':
                if value is not None:
                    query = query.filter_by(CI_Id=value)
            if field == 'Year':
                if value is not None:
                    query = query.filter_by(Year=value)
            if field == 'Month':
                if value is not None:
                    query = query.filter_by(Month=value)
            if field == 'Count':
                if value is not None:
                    query = query.filter_by(Count=value)
            if field == 'Mean':
                if value is not None:
                    query = query.filter_by(Mean=value)
            if field == 'Variance':
                if value is not None:
                    query = query.filter_by(Variance=value)
            if field == 'StdDev':
                if value is not None:
                    query = query.filter_by(StdDev=value)
            if field == 'Min':
                if value is not None:
                    query = query.filter_by(Min=value)
            if field == 'Max':
                if value is not None:
                    query = query.filter_by(Max=value)
            
    # Actual request from DB follows
    tracebox_log(query,logger,length=50)
    rows = query.paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
    # Setting pagination variables ...
    if field is not None:
       next_url = url_for('.select_ST_Use_Per_Type_query', field=field, value=value, page=rows.next_num) if rows.has_next else None
       prev_url = url_for('.select_ST_Use_Per_Type_query', field=field, value=value, page=rows.prev_num) if rows.has_prev else None
    else:
       next_url = url_for('.select_ST_Use_Per_Type_query', page=rows.next_num) if rows.has_next else None
       prev_url = url_for('.select_ST_Use_Per_Type_query', page=rows.prev_num) if rows.has_prev else None
    # Actual rendering ...
    if request.headers.get('Content-Type') is not None or request.args.get('JSON',None,type=str) is not None:
        if "JSON" in request.headers.get('Content-Type') or request.args.get('JSON',None,type=str) is not None:
            logger.debug('select_ST_Use_Per_Type_query(): will render: JSON rows')
            logger.debug('select_ST_Use_Per_Type_query(): Exit')
            return json.dumps(serialize_object(rows.__dict__))
    logger.debug('select_ST_Use_Per_Type_query(): will render: st_use_per_type_All.html')
    logger.debug('select_ST_Use_Per_Type_query(): Exit')
    return render_template('st_use_per_type_select_All.html',rows=rows,options=options)
#===============================================================================
   # NOTE: HARDCODE. TO REMOVE --------------------------------------------
def chk_c000001(*args,**kwargs):
    pass
    
from emtec.common.interface import *
from emtec.collector.db.orm_model          import Interface
from emtec.collector.db.flask_models       import interface
#-----------------------------------------------------------------------
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2020-02-20 16:44:35
# =============================================================================

# ======================================================================
#  Auto-Generated code. Do not modify 
#  (C) Sertechno/Emtec Group (2018,2019)
#  GLVH @ 2020-02-20 16:44:46.215358
# ======================================================================
        
# gen_views_form.html:AG 2020-02-20 16:44:46.215381
@main.route('/forms/Trace', methods=['GET', 'POST'])
@login_required

def forms_Trace():
    """ Form handling function for table Trace """
    logger.debug('forms_Trace(): Enter')
    ID  =  request.args.get('ID',0,type=int)
    
    row =  trace.query.filter(trace.ID == ID).first()
    if row is None:
        row=trace()
        session['is_new_row']=True
    session['data'] =  {  'ID':row.ID, 'LINE':row.LINE }
    
    form = frm_trace()
    
    # Actual Form activation here
    if form.validate_on_submit():
    # Code for SAVE option
        if form.submit_Save.data and current_user.role_id > 1:
    
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
                   message=Markup('<b>Trace line ID saved OK</b>')
                   flash(message)
               db.session.close()
            except Exception as e:
               db.session.rollback()
               db.session.close()
               message=Markup('ERROR saving Trace line record : %s'%(e))
               flash(message)
            return redirect(url_for('.select_Trace_query'))    
    # Code for NEW option
    # GV 20190109 f.write(        "        elif   form.submit_New.data:\n")
        elif   form.submit_New.data and current_user.role_id>1:
            #print('New Data Here ...')
            session['is_new_row']=True
            db.session.close()
            row=trace()
    
            return redirect(url_for('.forms_Trace',ID=row.ID))
    
    # Code for CANCEL option 
        elif   form.submit_Cancel.data:
            #print('Cancel Data Here ... does nothing')
            message=Markup('Trace line Record modifications discarded ...')
            flash(message)
    # Code for ANY OTHER option should never get here
        else:
            #print('form validated but not submited ???')
            message=Markup("<b>Trace line data modifications not allowed for user '%s'. Please contact EG Suite's Administrator ...</b>"%(current_user.username))    
            flash(message)
    
            return redirect(url_for('.forms_Trace',ID=row.ID))
    
    
    form.LINE.data = row.LINE
    session['prev_row'] = str(row)
    session['is_new_row'] = False
    logger.debug('forms_Trace(): Exit')
    # Generates pagination data here
    P=[]
    # Tab Relations = []
    
    # Generation of pagination data completed       
    return render_template('trace.html', form=form, row=row, P=P)    
# ======================================================================



# ======================================================================
#  Auto-Generated code. Do not modify 
#  (C) Sertechno/Emtec Group (2018,2019)
#  GLVH @ 2020-02-20 16:44:46.239203
# ======================================================================
        
# gen_views_delete.html:AG 2020-02-20 16:44:46.239226
@main.route('/forms/Trace_delete', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@admin_required
def forms_Trace_delete():
    """ Delete record handling function for table Trace """
    logger.debug('forms_Trace_delete(): Enter')
    ID  =  request.args.get('ID',0,type=int)
    row =  trace.query.filter(trace.ID == ID).first()

    if row is None:
        row=trace()
    session['data'] =  {  'ID':row.ID, 'LINE':row.LINE }
                       
    form = frm_trace_delete()

    # Tab['has_fks'] False
    
            
    # Actual Form activation here
    if form.validate_on_submit():
    
    # Code for SAVE option
        if  form.submit_Delete.data:
            print('Delete Data Here...')

    
    #f.write(        "            print('Delete Data Here...')
            try:
                session['deleted_row']=str(row)
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                logger.audit ( '%s:DEL:%s' % (current_user.username,session['deleted_row']) )
                flash('Trace line ID deleted OK')
            except exc.IntegrityError as e:
                db.session.rollback()    
                flash('INTEGRITY ERROR: Are you sure there are no dependant records in other tables?')
                return redirect(url_for('.forms_Trace_delete',ID=session['data']['ID']))    
    
            return redirect(url_for('.select_Trace_query'))    
    # Code for CANCEL option 
        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
            return redirect(url_for('.select_Trace_query'))    
    # Code for ANY OTHER option should never get here
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.select_Trace_query'))    
    
    logger.debug('forms_Trace_delete(): Exit')
    return render_template('trace_delete.html', form=form, data=session.get('data'),row=row)
#===============================================================================

# ======================================================================
#  Auto-Generated code. Do not modify 
#  (C) Sertechno/Emtec Group (2018,2019)
#  GLVH @ 2020-02-20 16:44:46.291236
# ======================================================================


from pprint import pprint, pformat

# gen_views_select_query.html:AG 2020-02-20 16:44:46.291260        
@main.route('/select/Trace_Query', methods=['GET','POST'])
@login_required
@admin_required
def select_Trace_query():
    """ Select rows handling function for table 'Trace' """
    logger.debug('select_Trace_query(): Enter')
    chk_c000001(filename=os.path.join(current_app.root_path, '.c000001'),request=request,db=db,logger=logger)
    # Get parameters from URL call
    ia       =  request.args.get('ia',     None,type=str)
    if ia is not None:
        ia=ia.split(',')
        if ia[0]=='ORDER':
            set_query_option(engine=db.engine,Interface=Interface,User_Id=current_user.id,Table_name='trace',Option_Type=OPTION_ORDER_BY,Argument_1=ia[1],Argument_2=ia[2])
        elif ia[0]=='GROUP':
            set_query_option(engine=db.engine,Interface=Interface,User_Id=current_user.id,Table_name='trace',Option_Type=OPTION_GROUP_BY,Argument_1=ia[1])
        elif ia[0]=='LIMIT':
            set_query_option(engine=db.engine,Interface=Interface,User_Id=current_user.id,Table_name='trace',Option_Type=OPTION_LIMIT,Argument_1=ia[1])

    iad      =  request.args.get('iad',     None,type=int)
    if iad is not None: delete_query_option(engine=db.engine,Interface=Interface,Id=iad) 
    
    field    =  request.args.get('field',   None,type=str)
    value    =  request.args.get('value',   None,type=str)
    
    # Populates a list of foreign keys used for advanced filtering
    # ------------------------------------------------------------------
    foreign_keys={}
    
    # ------------------------------------------------------------------
    
    if field is not None:
        reset_query_options(    engine=db.engine,Interface=Interface,
                                User_Id=current_user.id,
                                Table_name='trace'
                                )

        
        if field in foreign_keys.keys():
            Class,referenced_classname,referenced_Field,referenced_Value,column_Header=foreign_keys[field]
            foreign_field='%s.%s:%s'%(referenced_classname,referenced_Value,column_Header)
            foreign_record=Class.query.get(value)
            foreign_description="'%s'"%getattr(foreign_record,referenced_Value)
        set_query_option(   engine=db.engine,Interface=Interface,
                        User_Id=current_user.id,
                        Table_name='trace',
                        Option_Type=OPTION_FILTER,
                        Argument_1=foreign_field,
                        Argument_2='==',
                        Argument_3=foreign_description
                        )
    page     =  request.args.get('page',    1   ,type=int)
    addx     =  request.args.get('add.x',   None,type=int)
    addy     =  request.args.get('add.y',   None,type=int)
    exportx  =  request.args.get('export.x',None,type=int)
    exporty  =  request.args.get('export.y',None,type=int)
    filterx  =  request.args.get('filter.x',None,type=int)
    filtery  =  request.args.get('filter.y',None,type=int)
    # Select excluyent view mode
    if   addx    is not None: mode = 'add'
    elif exportx is not None: mode = 'export'
    elif filterx is not None: mode = 'filter'
    else:                     mode = 'select'
    ID =  request.args.get('ID',None,type=str)
    LINE =  request.args.get('LINE',None,type=str)
    
    
    # Build default query all fields from table
    
    if ID is not None and len(ID)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='trace',
                Option_Type=OPTION_FILTER,
                Argument_1='ID:ID',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%ID
                )
    
    
    if LINE is not None and len(LINE)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='trace',
                Option_Type=OPTION_FILTER,
                Argument_1='LINE:LINE',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%LINE
                )
    
    
    
    statement_query,options=get_query_options(engine=db.engine,Interface=Interface,Table_name='trace',User_Id=current_user.id)
    query=eval(statement_query)
    filtered_query = query    
    if mode == 'filter':
        query=filtered_query
    elif mode == 'export':
        query=filtered_query
        fh,output_file = tempfile.mkstemp(suffix='', prefix='Trace_', dir=None, text=False)
        dict = {'header':{},'detail':[]}
        count = 0
        rows = query.all()
        for row in rows:
            dict['detail'].append({})
            for column in ['ID', 'LINE']:
                dict['detail'][count].update( { column:str(row.__getattribute__(column))})
                
            count += 1
        dict['header'].update({'count':count})
        jsonarray      = json.dumps(dict)
        data           = json.loads(jsonarray)  
        dataframe      = json_normalize(data, 'detail').assign(**data['header'])
        fh,output_file = tempfile.mkstemp(suffix='', prefix='Trace_', dir='/tmp', text=False)
        xlsx_file      = '%s/%s'%(current_app.root_path,url_for('static',filename='%s.xls'%(output_file)))
        dataframe.to_excel(xlsx_file,sheet_name='Trace',columns=['ID', 'LINE'])
        return send_file(xlsx_file,as_attachment=True,attachment_filename=output_file.replace('/','_')+'.xls')
    elif mode == 'add':
        return redirect(url_for('.forms_Trace'))
    elif mode == 'select':
        pass
        # if some filter is required
        if field is not None:
            if field == 'ID':
                if value is not None:
                    query = query.filter_by(ID=value)
            if field == 'LINE':
                if value is not None:
                    query = query.filter_by(LINE=value)
            
    # Actual request from DB follows
    tracebox_log(query,logger,length=50)
    rows = query.paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
    # Setting pagination variables ...
    if field is not None:
       next_url = url_for('.select_Trace_query', field=field, value=value, page=rows.next_num) if rows.has_next else None
       prev_url = url_for('.select_Trace_query', field=field, value=value, page=rows.prev_num) if rows.has_prev else None
    else:
       next_url = url_for('.select_Trace_query', page=rows.next_num) if rows.has_next else None
       prev_url = url_for('.select_Trace_query', page=rows.prev_num) if rows.has_prev else None
    # Actual rendering ...
    if request.headers.get('Content-Type') is not None or request.args.get('JSON',None,type=str) is not None:
        if "JSON" in request.headers.get('Content-Type') or request.args.get('JSON',None,type=str) is not None:
            logger.debug('select_Trace_query(): will render: JSON rows')
            logger.debug('select_Trace_query(): Exit')
            return json.dumps(serialize_object(rows.__dict__))
    logger.debug('select_Trace_query(): will render: trace_All.html')
    logger.debug('select_Trace_query(): Exit')
    return render_template('trace_select_All.html',rows=rows,options=options)
#===============================================================================
   # NOTE: HARDCODE. TO REMOVE --------------------------------------------
def chk_c000001(*args,**kwargs):
    pass
    
from emtec.common.interface import *
from emtec.collector.db.orm_model          import Interface
from emtec.collector.db.flask_models       import interface
#-----------------------------------------------------------------------
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2020-02-20 16:44:35
# =============================================================================

# ======================================================================
#  Auto-Generated code. Do not modify 
#  (C) Sertechno/Emtec Group (2018,2019)
#  GLVH @ 2020-02-20 16:44:46.744096
# ======================================================================
        
# gen_views_form.html:AG 2020-02-20 16:44:46.744128
@main.route('/forms/User_Resumes', methods=['GET', 'POST'])
@login_required

def forms_User_Resumes():
    """ Form handling function for table User_Resumes """
    logger.debug('forms_User_Resumes(): Enter')
    CR_Date_From  =  request.args.get('CR_Date_From',0,type=int)
    CR_Date_To  =  request.args.get('CR_Date_To',0,type=int)
    CIT_Status  =  request.args.get('CIT_Status',0,type=int)
    Cur_Code  =  request.args.get('Cur_Code',0,type=int)
    CU_Id  =  request.args.get('CU_Id',0,type=int)
    CI_Id  =  request.args.get('CI_Id',0,type=int)
    
    row =  user_resumes.query.filter(user_resumes.CR_Date_From == CR_Date_From,user_resumes.CR_Date_To == CR_Date_To,user_resumes.CIT_Status == CIT_Status,user_resumes.Cur_Code == Cur_Code,user_resumes.CU_Id == CU_Id,user_resumes.CI_Id == CI_Id).first()
    if row is None:
        row=user_resumes()
        session['is_new_row']=True
    session['data'] =  {  'Cus_Id':row.Cus_Id, 'CR_Date_From':row.CR_Date_From, 'CR_Date_To':row.CR_Date_To, 'CIT_Status':row.CIT_Status, 'Cur_Code':row.Cur_Code, 'CIT_Count':row.CIT_Count, 'CIT_Quantity':row.CIT_Quantity, 'CIT_Generation':row.CIT_Generation, 'CU_Id':row.CU_Id, 'CI_CC_Id':row.CI_CC_Id, 'CU_Operation':row.CU_Operation, 'Typ_Code':row.Typ_Code, 'CC_Cur_Code':row.CC_Cur_Code, 'CI_Id':row.CI_Id, 'Rat_Id':row.Rat_Id, 'Rat_Price':row.Rat_Price, 'Rat_MU_Code':row.Rat_MU_Code, 'Rat_Cur_Code':row.Rat_Cur_Code, 'Rat_Period':row.Rat_Period, 'Rat_Hourly':row.Rat_Hourly, 'Rat_Daily':row.Rat_Daily, 'Rat_Monthly':row.Rat_Monthly, 'CR_Quantity':row.CR_Quantity, 'CR_Quantity_at_Rate':row.CR_Quantity_at_Rate, 'CC_XR':row.CC_XR, 'CR_Cur_XR':row.CR_Cur_XR, 'CR_ST_at_Rate_Cur':row.CR_ST_at_Rate_Cur, 'CR_ST_at_CC_Cur':row.CR_ST_at_CC_Cur, 'CR_ST_at_Cur':row.CR_ST_at_Cur, 'Cus_Name':row.Cus_Name, 'CI_Name':row.CI_Name, 'CU_Description':row.CU_Description, 'CC_Description':row.CC_Description, 'Rat_Period_Description':row.Rat_Period_Description, 'CC_Code':row.CC_Code, 'Pla_Id':row.Pla_Id, 'Pla_Name':row.Pla_Name }
    
    form = frm_user_resumes()
    
    # Actual Form activation here
    if form.validate_on_submit():
    # Code for SAVE option
        if form.submit_Save.data and current_user.role_id > 1:
    
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
            row.CC_Code = form.CC_Code.data
            row.Pla_Id = form.Pla_Id.data
            row.Pla_Name = form.Pla_Name.data  
            try:
               session['new_row']=str(row)
               db.session.close()
               db.session.add(row)
               db.session.commit()
               if session['is_new_row']==True:
                   logger.audit ( '%s:NEW:%s' % (current_user.username,session['new_row'] ) )
                   flash('New User Resume created OK')
               else:
                   logger.audit ( '%s:OLD:%s' % (current_user.username,session['prev_row']) )
                   logger.audit ( '%s:UPD:%s' % (current_user.username,session['new_row'] ) )    
                   message=Markup('<b>User Resume CR_Date_From,CR_Date_To,CIT_Status,Cur_Code,CU_Id,CI_Id saved OK</b>')
                   flash(message)
               db.session.close()
            except Exception as e:
               db.session.rollback()
               db.session.close()
               message=Markup('ERROR saving User Resume record : %s'%(e))
               flash(message)
            return redirect(url_for('.select_User_Resumes_query'))    
    # Code for NEW option
    # GV 20190109 f.write(        "        elif   form.submit_New.data:\n")
        elif   form.submit_New.data and current_user.role_id>1:
            #print('New Data Here ...')
            session['is_new_row']=True
            db.session.close()
            row=user_resumes()
    
            return redirect(url_for('.forms_User_Resumes'))    
    
    # Code for CANCEL option 
        elif   form.submit_Cancel.data:
            #print('Cancel Data Here ... does nothing')
            message=Markup('User Resume Record modifications discarded ...')
            flash(message)
    # Code for ANY OTHER option should never get here
        else:
            #print('form validated but not submited ???')
            message=Markup("<b>User Resume data modifications not allowed for user '%s'. Please contact EG Suite's Administrator ...</b>"%(current_user.username))    
            flash(message)
    
            return redirect(url_for('.forms_'))    
    
    
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
    form.CC_Code.data = row.CC_Code
    form.Pla_Id.data = row.Pla_Id
    form.Pla_Name.data = row.Pla_Name
    session['prev_row'] = str(row)
    session['is_new_row'] = False
    logger.debug('forms_User_Resumes(): Exit')
    # Generates pagination data here
    P=[]
    # Tab Relations = []
    
    # Generation of pagination data completed       
    return render_template('user_resumes.html', form=form, row=row, P=P)    
# ======================================================================



# ======================================================================
#  Auto-Generated code. Do not modify 
#  (C) Sertechno/Emtec Group (2018,2019)
#  GLVH @ 2020-02-20 16:44:46.780641
# ======================================================================
        
# gen_views_delete.html:AG 2020-02-20 16:44:46.780681
@main.route('/forms/User_Resumes_delete', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)

def forms_User_Resumes_delete():
    """ Delete record handling function for table User_Resumes """
    logger.debug('forms_User_Resumes_delete(): Enter')
    CR_Date_From  =  request.args.get('CR_Date_From',0,type=int)
    CR_Date_To  =  request.args.get('CR_Date_To',0,type=int)
    CIT_Status  =  request.args.get('CIT_Status',0,type=int)
    Cur_Code  =  request.args.get('Cur_Code',0,type=int)
    CU_Id  =  request.args.get('CU_Id',0,type=int)
    CI_Id  =  request.args.get('CI_Id',0,type=int)
    row =  user_resumes.query.filter(user_resumes.CR_Date_From == CR_Date_From,user_resumes.CR_Date_To == CR_Date_To,user_resumes.CIT_Status == CIT_Status,user_resumes.Cur_Code == Cur_Code,user_resumes.CU_Id == CU_Id,user_resumes.CI_Id == CI_Id).first()

    if row is None:
        row=user_resumes()
    session['data'] =  {  'Cus_Id':row.Cus_Id, 'CR_Date_From':row.CR_Date_From, 'CR_Date_To':row.CR_Date_To, 'CIT_Status':row.CIT_Status, 'Cur_Code':row.Cur_Code, 'CIT_Count':row.CIT_Count, 'CIT_Quantity':row.CIT_Quantity, 'CIT_Generation':row.CIT_Generation, 'CU_Id':row.CU_Id, 'CI_CC_Id':row.CI_CC_Id, 'CU_Operation':row.CU_Operation, 'Typ_Code':row.Typ_Code, 'CC_Cur_Code':row.CC_Cur_Code, 'CI_Id':row.CI_Id, 'Rat_Id':row.Rat_Id, 'Rat_Price':row.Rat_Price, 'Rat_MU_Code':row.Rat_MU_Code, 'Rat_Cur_Code':row.Rat_Cur_Code, 'Rat_Period':row.Rat_Period, 'Rat_Hourly':row.Rat_Hourly, 'Rat_Daily':row.Rat_Daily, 'Rat_Monthly':row.Rat_Monthly, 'CR_Quantity':row.CR_Quantity, 'CR_Quantity_at_Rate':row.CR_Quantity_at_Rate, 'CC_XR':row.CC_XR, 'CR_Cur_XR':row.CR_Cur_XR, 'CR_ST_at_Rate_Cur':row.CR_ST_at_Rate_Cur, 'CR_ST_at_CC_Cur':row.CR_ST_at_CC_Cur, 'CR_ST_at_Cur':row.CR_ST_at_Cur, 'Cus_Name':row.Cus_Name, 'CI_Name':row.CI_Name, 'CU_Description':row.CU_Description, 'CC_Description':row.CC_Description, 'Rat_Period_Description':row.Rat_Period_Description, 'CC_Code':row.CC_Code, 'Pla_Id':row.Pla_Id, 'Pla_Name':row.Pla_Name }
                       
    form = frm_user_resumes_delete()

    # Tab['has_fks'] False
    
            
    # Actual Form activation here
    if form.validate_on_submit():
    
    # Code for SAVE option
        if  form.submit_Delete.data:
            print('Delete Data Here...')

    
    #f.write(        "            print('Delete Data Here...')
            try:
                session['deleted_row']=str(row)
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                logger.audit ( '%s:DEL:%s' % (current_user.username,session['deleted_row']) )
                flash('User Resume CR_Date_From,CR_Date_To,CIT_Status,Cur_Code,CU_Id,CI_Id deleted OK')
            except exc.IntegrityError as e:
                db.session.rollback()    
                flash('INTEGRITY ERROR: Are you sure there are no dependant records in other tables?')
                return redirect(url_for('.forms_User_Resumes_delete',CR_Date_From=session['data']['CR_Date_From'],CR_Date_To=session['data']['CR_Date_To'],CIT_Status=session['data']['CIT_Status'],Cur_Code=session['data']['Cur_Code'],CU_Id=session['data']['CU_Id'],CI_Id=session['data']['CI_Id']))    
    
            return redirect(url_for('.select_User_Resumes_query'))    
    # Code for CANCEL option 
        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
            return redirect(url_for('.select_User_Resumes_query'))    
    # Code for ANY OTHER option should never get here
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.select_User_Resumes_query'))    
    
    logger.debug('forms_User_Resumes_delete(): Exit')
    return render_template('user_resumes_delete.html', form=form, data=session.get('data'),row=row)
#===============================================================================

# ======================================================================
#  Auto-Generated code. Do not modify 
#  (C) Sertechno/Emtec Group (2018,2019)
#  GLVH @ 2020-02-20 16:44:46.841565
# ======================================================================


from pprint import pprint, pformat

# gen_views_select_query.html:AG 2020-02-20 16:44:46.841597        
@main.route('/select/User_Resumes_Query', methods=['GET','POST'])
@login_required

def select_User_Resumes_query():
    """ Select rows handling function for table 'User_Resumes' """
    logger.debug('select_User_Resumes_query(): Enter')
    chk_c000001(filename=os.path.join(current_app.root_path, '.c000001'),request=request,db=db,logger=logger)
    # Get parameters from URL call
    ia       =  request.args.get('ia',     None,type=str)
    if ia is not None:
        ia=ia.split(',')
        if ia[0]=='ORDER':
            set_query_option(engine=db.engine,Interface=Interface,User_Id=current_user.id,Table_name='user_resumes',Option_Type=OPTION_ORDER_BY,Argument_1=ia[1],Argument_2=ia[2])
        elif ia[0]=='GROUP':
            set_query_option(engine=db.engine,Interface=Interface,User_Id=current_user.id,Table_name='user_resumes',Option_Type=OPTION_GROUP_BY,Argument_1=ia[1])
        elif ia[0]=='LIMIT':
            set_query_option(engine=db.engine,Interface=Interface,User_Id=current_user.id,Table_name='user_resumes',Option_Type=OPTION_LIMIT,Argument_1=ia[1])

    iad      =  request.args.get('iad',     None,type=int)
    if iad is not None: delete_query_option(engine=db.engine,Interface=Interface,Id=iad) 
    
    field    =  request.args.get('field',   None,type=str)
    value    =  request.args.get('value',   None,type=str)
    
    # Populates a list of foreign keys used for advanced filtering
    # ------------------------------------------------------------------
    foreign_keys={}
    
    # ------------------------------------------------------------------
    
    if field is not None:
        reset_query_options(    engine=db.engine,Interface=Interface,
                                User_Id=current_user.id,
                                Table_name='user_resumes'
                                )

        
        if field in foreign_keys.keys():
            Class,referenced_classname,referenced_Field,referenced_Value,column_Header=foreign_keys[field]
            foreign_field='%s.%s:%s'%(referenced_classname,referenced_Value,column_Header)
            foreign_record=Class.query.get(value)
            foreign_description="'%s'"%getattr(foreign_record,referenced_Value)
        set_query_option(   engine=db.engine,Interface=Interface,
                        User_Id=current_user.id,
                        Table_name='user_resumes',
                        Option_Type=OPTION_FILTER,
                        Argument_1=foreign_field,
                        Argument_2='==',
                        Argument_3=foreign_description
                        )
    page     =  request.args.get('page',    1   ,type=int)
    addx     =  request.args.get('add.x',   None,type=int)
    addy     =  request.args.get('add.y',   None,type=int)
    exportx  =  request.args.get('export.x',None,type=int)
    exporty  =  request.args.get('export.y',None,type=int)
    filterx  =  request.args.get('filter.x',None,type=int)
    filtery  =  request.args.get('filter.y',None,type=int)
    # Select excluyent view mode
    if   addx    is not None: mode = 'add'
    elif exportx is not None: mode = 'export'
    elif filterx is not None: mode = 'filter'
    else:                     mode = 'select'
    Cus_Id =  request.args.get('Cus_Id',None,type=str)
    CR_Date_From =  request.args.get('CR_Date_From',None,type=str)
    CR_Date_To =  request.args.get('CR_Date_To',None,type=str)
    CIT_Status =  request.args.get('CIT_Status',None,type=str)
    Cur_Code =  request.args.get('Cur_Code',None,type=str)
    CIT_Count =  request.args.get('CIT_Count',None,type=str)
    CIT_Quantity =  request.args.get('CIT_Quantity',None,type=str)
    CIT_Generation =  request.args.get('CIT_Generation',None,type=str)
    CU_Id =  request.args.get('CU_Id',None,type=str)
    CI_CC_Id =  request.args.get('CI_CC_Id',None,type=str)
    CU_Operation =  request.args.get('CU_Operation',None,type=str)
    Typ_Code =  request.args.get('Typ_Code',None,type=str)
    CC_Cur_Code =  request.args.get('CC_Cur_Code',None,type=str)
    CI_Id =  request.args.get('CI_Id',None,type=str)
    Rat_Id =  request.args.get('Rat_Id',None,type=str)
    Rat_Price =  request.args.get('Rat_Price',None,type=str)
    Rat_MU_Code =  request.args.get('Rat_MU_Code',None,type=str)
    Rat_Cur_Code =  request.args.get('Rat_Cur_Code',None,type=str)
    Rat_Period =  request.args.get('Rat_Period',None,type=str)
    Rat_Hourly =  request.args.get('Rat_Hourly',None,type=str)
    Rat_Daily =  request.args.get('Rat_Daily',None,type=str)
    Rat_Monthly =  request.args.get('Rat_Monthly',None,type=str)
    CR_Quantity =  request.args.get('CR_Quantity',None,type=str)
    CR_Quantity_at_Rate =  request.args.get('CR_Quantity_at_Rate',None,type=str)
    CC_XR =  request.args.get('CC_XR',None,type=str)
    CR_Cur_XR =  request.args.get('CR_Cur_XR',None,type=str)
    CR_ST_at_Rate_Cur =  request.args.get('CR_ST_at_Rate_Cur',None,type=str)
    CR_ST_at_CC_Cur =  request.args.get('CR_ST_at_CC_Cur',None,type=str)
    CR_ST_at_Cur =  request.args.get('CR_ST_at_Cur',None,type=str)
    Cus_Name =  request.args.get('Cus_Name',None,type=str)
    CI_Name =  request.args.get('CI_Name',None,type=str)
    CU_Description =  request.args.get('CU_Description',None,type=str)
    CC_Description =  request.args.get('CC_Description',None,type=str)
    Rat_Period_Description =  request.args.get('Rat_Period_Description',None,type=str)
    CC_Code =  request.args.get('CC_Code',None,type=str)
    Pla_Id =  request.args.get('Pla_Id',None,type=str)
    Pla_Name =  request.args.get('Pla_Name',None,type=str)
    
    
    # Build default query all fields from table
    
    if Cus_Id is not None and len(Cus_Id)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='user_resumes',
                Option_Type=OPTION_FILTER,
                Argument_1='Cus_Id:Cus_Id',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Cus_Id
                )
    
    
    if CR_Date_From is not None and len(CR_Date_From)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='user_resumes',
                Option_Type=OPTION_FILTER,
                Argument_1='CR_Date_From:CR_Date_From',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%CR_Date_From
                )
    
    
    if CR_Date_To is not None and len(CR_Date_To)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='user_resumes',
                Option_Type=OPTION_FILTER,
                Argument_1='CR_Date_To:CR_Date_To',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%CR_Date_To
                )
    
    
    if CIT_Status is not None and len(CIT_Status)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='user_resumes',
                Option_Type=OPTION_FILTER,
                Argument_1='CIT_Status:CIT_Status',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%CIT_Status
                )
    
    
    if Cur_Code is not None and len(Cur_Code)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='user_resumes',
                Option_Type=OPTION_FILTER,
                Argument_1='Cur_Code:Cur_Code',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Cur_Code
                )
    
    
    if CIT_Count is not None and len(CIT_Count)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='user_resumes',
                Option_Type=OPTION_FILTER,
                Argument_1='CIT_Count:CIT_Count',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%CIT_Count
                )
    
    
    if CIT_Quantity is not None and len(CIT_Quantity)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='user_resumes',
                Option_Type=OPTION_FILTER,
                Argument_1='CIT_Quantity:CIT_Quantity',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%CIT_Quantity
                )
    
    
    if CIT_Generation is not None and len(CIT_Generation)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='user_resumes',
                Option_Type=OPTION_FILTER,
                Argument_1='CIT_Generation:CIT_Generation',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%CIT_Generation
                )
    
    
    if CU_Id is not None and len(CU_Id)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='user_resumes',
                Option_Type=OPTION_FILTER,
                Argument_1='CU_Id:CU_Id',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%CU_Id
                )
    
    
    if CI_CC_Id is not None and len(CI_CC_Id)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='user_resumes',
                Option_Type=OPTION_FILTER,
                Argument_1='CI_CC_Id:CI_CC_Id',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%CI_CC_Id
                )
    
    
    if CU_Operation is not None and len(CU_Operation)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='user_resumes',
                Option_Type=OPTION_FILTER,
                Argument_1='CU_Operation:CU_Operation',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%CU_Operation
                )
    
    
    if Typ_Code is not None and len(Typ_Code)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='user_resumes',
                Option_Type=OPTION_FILTER,
                Argument_1='Typ_Code:Typ_Code',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Typ_Code
                )
    
    
    if CC_Cur_Code is not None and len(CC_Cur_Code)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='user_resumes',
                Option_Type=OPTION_FILTER,
                Argument_1='CC_Cur_Code:CC_Cur_Code',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%CC_Cur_Code
                )
    
    
    if CI_Id is not None and len(CI_Id)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='user_resumes',
                Option_Type=OPTION_FILTER,
                Argument_1='CI_Id:CI_Id',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%CI_Id
                )
    
    
    if Rat_Id is not None and len(Rat_Id)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='user_resumes',
                Option_Type=OPTION_FILTER,
                Argument_1='Rat_Id:Rat_Id',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Rat_Id
                )
    
    
    if Rat_Price is not None and len(Rat_Price)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='user_resumes',
                Option_Type=OPTION_FILTER,
                Argument_1='Rat_Price:Rat_Price',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Rat_Price
                )
    
    
    if Rat_MU_Code is not None and len(Rat_MU_Code)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='user_resumes',
                Option_Type=OPTION_FILTER,
                Argument_1='Rat_MU_Code:Rat_MU_Code',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Rat_MU_Code
                )
    
    
    if Rat_Cur_Code is not None and len(Rat_Cur_Code)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='user_resumes',
                Option_Type=OPTION_FILTER,
                Argument_1='Rat_Cur_Code:Rat_Cur_Code',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Rat_Cur_Code
                )
    
    
    if Rat_Period is not None and len(Rat_Period)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='user_resumes',
                Option_Type=OPTION_FILTER,
                Argument_1='Rat_Period:Rat_Period',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Rat_Period
                )
    
    
    if Rat_Hourly is not None and len(Rat_Hourly)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='user_resumes',
                Option_Type=OPTION_FILTER,
                Argument_1='Rat_Hourly:Rat_Hourly',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Rat_Hourly
                )
    
    
    if Rat_Daily is not None and len(Rat_Daily)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='user_resumes',
                Option_Type=OPTION_FILTER,
                Argument_1='Rat_Daily:Rat_Daily',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Rat_Daily
                )
    
    
    if Rat_Monthly is not None and len(Rat_Monthly)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='user_resumes',
                Option_Type=OPTION_FILTER,
                Argument_1='Rat_Monthly:Rat_Monthly',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Rat_Monthly
                )
    
    
    if CR_Quantity is not None and len(CR_Quantity)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='user_resumes',
                Option_Type=OPTION_FILTER,
                Argument_1='CR_Quantity:CR_Quantity',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%CR_Quantity
                )
    
    
    if CR_Quantity_at_Rate is not None and len(CR_Quantity_at_Rate)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='user_resumes',
                Option_Type=OPTION_FILTER,
                Argument_1='CR_Quantity_at_Rate:CR_Quantity_at_Rate',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%CR_Quantity_at_Rate
                )
    
    
    if CC_XR is not None and len(CC_XR)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='user_resumes',
                Option_Type=OPTION_FILTER,
                Argument_1='CC_XR:CC_XR',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%CC_XR
                )
    
    
    if CR_Cur_XR is not None and len(CR_Cur_XR)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='user_resumes',
                Option_Type=OPTION_FILTER,
                Argument_1='CR_Cur_XR:CR_Cur_XR',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%CR_Cur_XR
                )
    
    
    if CR_ST_at_Rate_Cur is not None and len(CR_ST_at_Rate_Cur)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='user_resumes',
                Option_Type=OPTION_FILTER,
                Argument_1='CR_ST_at_Rate_Cur:CR_ST_at_Rate_Cur',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%CR_ST_at_Rate_Cur
                )
    
    
    if CR_ST_at_CC_Cur is not None and len(CR_ST_at_CC_Cur)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='user_resumes',
                Option_Type=OPTION_FILTER,
                Argument_1='CR_ST_at_CC_Cur:CR_ST_at_CC_Cur',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%CR_ST_at_CC_Cur
                )
    
    
    if CR_ST_at_Cur is not None and len(CR_ST_at_Cur)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='user_resumes',
                Option_Type=OPTION_FILTER,
                Argument_1='CR_ST_at_Cur:CR_ST_at_Cur',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%CR_ST_at_Cur
                )
    
    
    if Cus_Name is not None and len(Cus_Name)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='user_resumes',
                Option_Type=OPTION_FILTER,
                Argument_1='Cus_Name:Cus_Name',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Cus_Name
                )
    
    
    if CI_Name is not None and len(CI_Name)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='user_resumes',
                Option_Type=OPTION_FILTER,
                Argument_1='CI_Name:CI_Name',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%CI_Name
                )
    
    
    if CU_Description is not None and len(CU_Description)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='user_resumes',
                Option_Type=OPTION_FILTER,
                Argument_1='CU_Description:CU_Description',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%CU_Description
                )
    
    
    if CC_Description is not None and len(CC_Description)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='user_resumes',
                Option_Type=OPTION_FILTER,
                Argument_1='CC_Description:CC_Description',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%CC_Description
                )
    
    
    if Rat_Period_Description is not None and len(Rat_Period_Description)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='user_resumes',
                Option_Type=OPTION_FILTER,
                Argument_1='Rat_Period_Description:Rat_Period_Description',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Rat_Period_Description
                )
    
    
    if CC_Code is not None and len(CC_Code)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='user_resumes',
                Option_Type=OPTION_FILTER,
                Argument_1='CC_Code:CC_Code',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%CC_Code
                )
    
    
    if Pla_Id is not None and len(Pla_Id)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='user_resumes',
                Option_Type=OPTION_FILTER,
                Argument_1='Pla_Id:Pla_Id',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Pla_Id
                )
    
    
    if Pla_Name is not None and len(Pla_Name)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='user_resumes',
                Option_Type=OPTION_FILTER,
                Argument_1='Pla_Name:Pla_Name',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Pla_Name
                )
    
    
    
    statement_query,options=get_query_options(engine=db.engine,Interface=Interface,Table_name='user_resumes',User_Id=current_user.id)
    query=eval(statement_query)
    filtered_query = query    
    if mode == 'filter':
        query=filtered_query
    elif mode == 'export':
        query=filtered_query
        fh,output_file = tempfile.mkstemp(suffix='', prefix='User_Resumes_', dir=None, text=False)
        dict = {'header':{},'detail':[]}
        count = 0
        rows = query.all()
        for row in rows:
            dict['detail'].append({})
            for column in ['Cus_Id', 'CR_Date_From', 'CR_Date_To', 'CIT_Status', 'Cur_Code', 'CIT_Count', 'CIT_Quantity', 'CIT_Generation', 'CU_Id', 'CI_CC_Id', 'CU_Operation', 'Typ_Code', 'CC_Cur_Code', 'CI_Id', 'Rat_Id', 'Rat_Price', 'Rat_MU_Code', 'Rat_Cur_Code', 'Rat_Period', 'Rat_Hourly', 'Rat_Daily', 'Rat_Monthly', 'CR_Quantity', 'CR_Quantity_at_Rate', 'CC_XR', 'CR_Cur_XR', 'CR_ST_at_Rate_Cur', 'CR_ST_at_CC_Cur', 'CR_ST_at_Cur', 'Cus_Name', 'CI_Name', 'CU_Description', 'CC_Description', 'Rat_Period_Description', 'CC_Code', 'Pla_Id', 'Pla_Name']:
                dict['detail'][count].update( { column:str(row.__getattribute__(column))})
                
            count += 1
        dict['header'].update({'count':count})
        jsonarray      = json.dumps(dict)
        data           = json.loads(jsonarray)  
        dataframe      = json_normalize(data, 'detail').assign(**data['header'])
        fh,output_file = tempfile.mkstemp(suffix='', prefix='User_Resumes_', dir='/tmp', text=False)
        xlsx_file      = '%s/%s'%(current_app.root_path,url_for('static',filename='%s.xls'%(output_file)))
        dataframe.to_excel(xlsx_file,sheet_name='User_Resumes',columns=['Cus_Id', 'CR_Date_From', 'CR_Date_To', 'CIT_Status', 'Cur_Code', 'CIT_Count', 'CIT_Quantity', 'CIT_Generation', 'CU_Id', 'CI_CC_Id', 'CU_Operation', 'Typ_Code', 'CC_Cur_Code', 'CI_Id', 'Rat_Id', 'Rat_Price', 'Rat_MU_Code', 'Rat_Cur_Code', 'Rat_Period', 'Rat_Hourly', 'Rat_Daily', 'Rat_Monthly', 'CR_Quantity', 'CR_Quantity_at_Rate', 'CC_XR', 'CR_Cur_XR', 'CR_ST_at_Rate_Cur', 'CR_ST_at_CC_Cur', 'CR_ST_at_Cur', 'Cus_Name', 'CI_Name', 'CU_Description', 'CC_Description', 'Rat_Period_Description', 'CC_Code', 'Pla_Id', 'Pla_Name'])
        return send_file(xlsx_file,as_attachment=True,attachment_filename=output_file.replace('/','_')+'.xls')
    elif mode == 'add':
        return redirect(url_for('.forms_User_Resumes'))
    elif mode == 'select':
        pass
        # if some filter is required
        if field is not None:
            if field == 'Cus_Id':
                if value is not None:
                    query = query.filter_by(Cus_Id=value)
            if field == 'CR_Date_From':
                if value is not None:
                    query = query.filter_by(CR_Date_From=value)
            if field == 'CR_Date_To':
                if value is not None:
                    query = query.filter_by(CR_Date_To=value)
            if field == 'CIT_Status':
                if value is not None:
                    query = query.filter_by(CIT_Status=value)
            if field == 'Cur_Code':
                if value is not None:
                    query = query.filter_by(Cur_Code=value)
            if field == 'CIT_Count':
                if value is not None:
                    query = query.filter_by(CIT_Count=value)
            if field == 'CIT_Quantity':
                if value is not None:
                    query = query.filter_by(CIT_Quantity=value)
            if field == 'CIT_Generation':
                if value is not None:
                    query = query.filter_by(CIT_Generation=value)
            if field == 'CU_Id':
                if value is not None:
                    query = query.filter_by(CU_Id=value)
            if field == 'CI_CC_Id':
                if value is not None:
                    query = query.filter_by(CI_CC_Id=value)
            if field == 'CU_Operation':
                if value is not None:
                    query = query.filter_by(CU_Operation=value)
            if field == 'Typ_Code':
                if value is not None:
                    query = query.filter_by(Typ_Code=value)
            if field == 'CC_Cur_Code':
                if value is not None:
                    query = query.filter_by(CC_Cur_Code=value)
            if field == 'CI_Id':
                if value is not None:
                    query = query.filter_by(CI_Id=value)
            if field == 'Rat_Id':
                if value is not None:
                    query = query.filter_by(Rat_Id=value)
            if field == 'Rat_Price':
                if value is not None:
                    query = query.filter_by(Rat_Price=value)
            if field == 'Rat_MU_Code':
                if value is not None:
                    query = query.filter_by(Rat_MU_Code=value)
            if field == 'Rat_Cur_Code':
                if value is not None:
                    query = query.filter_by(Rat_Cur_Code=value)
            if field == 'Rat_Period':
                if value is not None:
                    query = query.filter_by(Rat_Period=value)
            if field == 'Rat_Hourly':
                if value is not None:
                    query = query.filter_by(Rat_Hourly=value)
            if field == 'Rat_Daily':
                if value is not None:
                    query = query.filter_by(Rat_Daily=value)
            if field == 'Rat_Monthly':
                if value is not None:
                    query = query.filter_by(Rat_Monthly=value)
            if field == 'CR_Quantity':
                if value is not None:
                    query = query.filter_by(CR_Quantity=value)
            if field == 'CR_Quantity_at_Rate':
                if value is not None:
                    query = query.filter_by(CR_Quantity_at_Rate=value)
            if field == 'CC_XR':
                if value is not None:
                    query = query.filter_by(CC_XR=value)
            if field == 'CR_Cur_XR':
                if value is not None:
                    query = query.filter_by(CR_Cur_XR=value)
            if field == 'CR_ST_at_Rate_Cur':
                if value is not None:
                    query = query.filter_by(CR_ST_at_Rate_Cur=value)
            if field == 'CR_ST_at_CC_Cur':
                if value is not None:
                    query = query.filter_by(CR_ST_at_CC_Cur=value)
            if field == 'CR_ST_at_Cur':
                if value is not None:
                    query = query.filter_by(CR_ST_at_Cur=value)
            if field == 'Cus_Name':
                if value is not None:
                    query = query.filter_by(Cus_Name=value)
            if field == 'CI_Name':
                if value is not None:
                    query = query.filter_by(CI_Name=value)
            if field == 'CU_Description':
                if value is not None:
                    query = query.filter_by(CU_Description=value)
            if field == 'CC_Description':
                if value is not None:
                    query = query.filter_by(CC_Description=value)
            if field == 'Rat_Period_Description':
                if value is not None:
                    query = query.filter_by(Rat_Period_Description=value)
            if field == 'CC_Code':
                if value is not None:
                    query = query.filter_by(CC_Code=value)
            if field == 'Pla_Id':
                if value is not None:
                    query = query.filter_by(Pla_Id=value)
            if field == 'Pla_Name':
                if value is not None:
                    query = query.filter_by(Pla_Name=value)
            
    # Actual request from DB follows
    tracebox_log(query,logger,length=50)
    rows = query.paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
    # Setting pagination variables ...
    if field is not None:
       next_url = url_for('.select_User_Resumes_query', field=field, value=value, page=rows.next_num) if rows.has_next else None
       prev_url = url_for('.select_User_Resumes_query', field=field, value=value, page=rows.prev_num) if rows.has_prev else None
    else:
       next_url = url_for('.select_User_Resumes_query', page=rows.next_num) if rows.has_next else None
       prev_url = url_for('.select_User_Resumes_query', page=rows.prev_num) if rows.has_prev else None
    # Actual rendering ...
    if request.headers.get('Content-Type') is not None or request.args.get('JSON',None,type=str) is not None:
        if "JSON" in request.headers.get('Content-Type') or request.args.get('JSON',None,type=str) is not None:
            logger.debug('select_User_Resumes_query(): will render: JSON rows')
            logger.debug('select_User_Resumes_query(): Exit')
            return json.dumps(serialize_object(rows.__dict__))
    logger.debug('select_User_Resumes_query(): will render: user_resumes_All.html')
    logger.debug('select_User_Resumes_query(): Exit')
    return render_template('user_resumes_select_All.html',rows=rows,options=options)
#===============================================================================
   # NOTE: HARDCODE. TO REMOVE --------------------------------------------
def chk_c000001(*args,**kwargs):
    pass
    
from emtec.common.interface import *
from emtec.collector.db.orm_model          import Interface
from emtec.collector.db.flask_models       import interface
#-----------------------------------------------------------------------
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2020-02-20 16:44:35
# =============================================================================

# ======================================================================
#  Auto-Generated code. Do not modify 
#  (C) Sertechno/Emtec Group (2018,2019)
#  GLVH @ 2020-02-20 16:44:47.137521
# ======================================================================
        
# gen_views_form.html:AG 2020-02-20 16:44:47.137545
@main.route('/forms/Users', methods=['GET', 'POST'])
@login_required

def forms_Users():
    """ Form handling function for table Users """
    logger.debug('forms_Users(): Enter')
    id  =  request.args.get('id',0,type=int)
    
    row =  User.query.filter(User.id == id).first()
    if row is None:
        row=User()
        session['is_new_row']=True
    session['data'] =  {  'id':row.id, 'username':row.username, 'role_id':row.role_id, 'email':row.email, 'password_hash':row.password_hash, 'confirmed':row.confirmed, 'CC_Id':row.CC_Id }
    
    form = frm_User()
    
    if form.has_FKs:
        form.role_id.choices = db.session.query(Role.id,Role.name).order_by(Role.name).all()
        form.CC_Id.choices = db.session.query(cost_center.CC_Id,cost_center.CC_Description).order_by(cost_center.CC_Description).all()

    
    # Actual Form activation here
    if form.validate_on_submit():
    # Code for SAVE option
        if form.submit_Save.data and current_user.role_id > 1:
    
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
                   message=Markup('<b>User id saved OK</b>')
                   flash(message)
               db.session.close()
            except Exception as e:
               db.session.rollback()
               db.session.close()
               message=Markup('ERROR saving User record : %s'%(e))
               flash(message)
            return redirect(url_for('.select_Users_query'))    
    # Code for NEW option
    # GV 20190109 f.write(        "        elif   form.submit_New.data:\n")
        elif   form.submit_New.data and current_user.role_id>1:
            #print('New Data Here ...')
            session['is_new_row']=True
            db.session.close()
            row=User()
    
            return redirect(url_for('.forms_Users',Id=row.Id))
    
    # Code for CANCEL option 
        elif   form.submit_Cancel.data:
            #print('Cancel Data Here ... does nothing')
            message=Markup('User Record modifications discarded ...')
            flash(message)
    # Code for ANY OTHER option should never get here
        else:
            #print('form validated but not submited ???')
            message=Markup("<b>User data modifications not allowed for user '%s'. Please contact EG Suite's Administrator ...</b>"%(current_user.username))    
            flash(message)
    
            return redirect(url_for('.forms_Users',Id=row.Id))
    
    
    form.username.data = row.username
    form.role_id.data = row.role_id
    form.email.data = row.email
    form.password_hash.data = row.password_hash
    form.confirmed.data = row.confirmed
    form.CC_Id.data = row.CC_Id
    session['prev_row'] = str(row)
    session['is_new_row'] = False
    logger.debug('forms_Users(): Exit')
    # Generates pagination data here
    P=[]
    # Tab Relations = []
    
    # Generation of pagination data completed       
    return render_template('users.html', form=form, row=row, P=P)    
# ======================================================================



# ======================================================================
#  Auto-Generated code. Do not modify 
#  (C) Sertechno/Emtec Group (2018,2019)
#  GLVH @ 2020-02-20 16:44:47.165518
# ======================================================================
        
# gen_views_delete.html:AG 2020-02-20 16:44:47.165553
@main.route('/forms/Users_delete', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@admin_required
def forms_Users_delete():
    """ Delete record handling function for table Users """
    logger.debug('forms_Users_delete(): Enter')
    id  =  request.args.get('id',0,type=int)
    row =  User.query.filter(User.id == id).first()

    if row is None:
        row=User()
    session['data'] =  {  'id':row.id, 'username':row.username, 'role_id':row.role_id, 'email':row.email, 'password_hash':row.password_hash, 'confirmed':row.confirmed, 'CC_Id':row.CC_Id }
                       
    form = frm_User_delete()

    # Tab['has_fks'] True
    
    pass # Tab['has_fks'] True
    
            
    # Actual Form activation here
    if form.validate_on_submit():
    
    # Code for SAVE option
        if  form.submit_Delete.data:
            print('Delete Data Here...')

    
    #f.write(        "            print('Delete Data Here...')
            try:
                session['deleted_row']=str(row)
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                logger.audit ( '%s:DEL:%s' % (current_user.username,session['deleted_row']) )
                flash('User id deleted OK')
            except exc.IntegrityError as e:
                db.session.rollback()    
                flash('INTEGRITY ERROR: Are you sure there are no dependant records in other tables?')
                return redirect(url_for('.forms_Users_delete',id=session['data']['id']))    
    
            return redirect(url_for('.select_Users_query'))    
    # Code for CANCEL option 
        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
            return redirect(url_for('.select_Users_query'))    
    # Code for ANY OTHER option should never get here
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.select_Users_query'))    
    
    logger.debug('forms_Users_delete(): Exit')
    return render_template('users_delete.html', form=form, data=session.get('data'),row=row)
#===============================================================================

# ======================================================================
#  Auto-Generated code. Do not modify 
#  (C) Sertechno/Emtec Group (2018,2019)
#  GLVH @ 2020-02-20 16:44:47.235853
# ======================================================================


from pprint import pprint, pformat

# gen_views_select_query.html:AG 2020-02-20 16:44:47.235879        
@main.route('/select/Users_Query', methods=['GET','POST'])
@login_required
@admin_required
def select_Users_query():
    """ Select rows handling function for table 'Users' """
    logger.debug('select_Users_query(): Enter')
    chk_c000001(filename=os.path.join(current_app.root_path, '.c000001'),request=request,db=db,logger=logger)
    # Get parameters from URL call
    ia       =  request.args.get('ia',     None,type=str)
    if ia is not None:
        ia=ia.split(',')
        if ia[0]=='ORDER':
            set_query_option(engine=db.engine,Interface=Interface,User_Id=current_user.id,Table_name='User',Option_Type=OPTION_ORDER_BY,Argument_1=ia[1],Argument_2=ia[2])
        elif ia[0]=='GROUP':
            set_query_option(engine=db.engine,Interface=Interface,User_Id=current_user.id,Table_name='User',Option_Type=OPTION_GROUP_BY,Argument_1=ia[1])
        elif ia[0]=='LIMIT':
            set_query_option(engine=db.engine,Interface=Interface,User_Id=current_user.id,Table_name='User',Option_Type=OPTION_LIMIT,Argument_1=ia[1])

    iad      =  request.args.get('iad',     None,type=int)
    if iad is not None: delete_query_option(engine=db.engine,Interface=Interface,Id=iad) 
    
    field    =  request.args.get('field',   None,type=str)
    value    =  request.args.get('value',   None,type=str)
    
    # Populates a list of foreign keys used for advanced filtering
    # ------------------------------------------------------------------
    foreign_keys={}
    
    foreign_keys.update({'role_id':(Role,'Role','id','name','role_id')})
    foreign_keys.update({'CC_Id':(cost_center,'cost_center','CC_Id','CC_Description','CC_Id')})
    # ------------------------------------------------------------------
    
    if field is not None:
        reset_query_options(    engine=db.engine,Interface=Interface,
                                User_Id=current_user.id,
                                Table_name='User'
                                )

        
        if field in foreign_keys.keys():
            Class,referenced_classname,referenced_Field,referenced_Value,column_Header=foreign_keys[field]
            foreign_field='%s.%s:%s'%(referenced_classname,referenced_Value,column_Header)
            foreign_record=Class.query.get(value)
            foreign_description="'%s'"%getattr(foreign_record,referenced_Value)
        set_query_option(   engine=db.engine,Interface=Interface,
                        User_Id=current_user.id,
                        Table_name='User',
                        Option_Type=OPTION_FILTER,
                        Argument_1=foreign_field,
                        Argument_2='==',
                        Argument_3=foreign_description
                        )
    page     =  request.args.get('page',    1   ,type=int)
    addx     =  request.args.get('add.x',   None,type=int)
    addy     =  request.args.get('add.y',   None,type=int)
    exportx  =  request.args.get('export.x',None,type=int)
    exporty  =  request.args.get('export.y',None,type=int)
    filterx  =  request.args.get('filter.x',None,type=int)
    filtery  =  request.args.get('filter.y',None,type=int)
    # Select excluyent view mode
    if   addx    is not None: mode = 'add'
    elif exportx is not None: mode = 'export'
    elif filterx is not None: mode = 'filter'
    else:                     mode = 'select'
    id =  request.args.get('id',None,type=str)
    username =  request.args.get('username',None,type=str)
    role_id =  request.args.get('role_id',None,type=str)
    email =  request.args.get('email',None,type=str)
    password_hash =  request.args.get('password_hash',None,type=str)
    confirmed =  request.args.get('confirmed',None,type=str)
    CC_Id =  request.args.get('CC_Id',None,type=str)
    
    
    # Build default query all fields from table
    
    if id is not None and len(id)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='User',
                Option_Type=OPTION_FILTER,
                Argument_1='id:Id',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%id
                )
    
    
    if username is not None and len(username)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='User',
                Option_Type=OPTION_FILTER,
                Argument_1='username:username',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%username
                )
    
    
    if role_id is not None and len(role_id)>0:
            Class,referenced_classname,referenced_Field,referenced_Value,column_Header=foreign_keys['role_id']
            foreign_field='%s.%s:%s'%(referenced_classname,referenced_Value,column_Header)            
            set_query_option(   engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='User',
                Option_Type=OPTION_FILTER,
                Argument_1=foreign_field,
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%role_id
                )
                                
    
    
    if email is not None and len(email)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='User',
                Option_Type=OPTION_FILTER,
                Argument_1='email:email',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%email
                )
    
    
    if password_hash is not None and len(password_hash)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='User',
                Option_Type=OPTION_FILTER,
                Argument_1='password_hash:password_hash',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%password_hash
                )
    
    
    if confirmed is not None and len(confirmed)>0:
            set_query_option(engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='User',
                Option_Type=OPTION_FILTER,
                Argument_1='confirmed:confirmed',
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%confirmed
                )
    
    
    if CC_Id is not None and len(CC_Id)>0:
            Class,referenced_classname,referenced_Field,referenced_Value,column_Header=foreign_keys['CC_Id']
            foreign_field='%s.%s:%s'%(referenced_classname,referenced_Value,column_Header)            
            set_query_option(   engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='User',
                Option_Type=OPTION_FILTER,
                Argument_1=foreign_field,
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%CC_Id
                )
                                
    
    
    
    statement_query,options=get_query_options(engine=db.engine,Interface=Interface,Table_name='User',User_Id=current_user.id)
    query=eval(statement_query)
    filtered_query = query    
    if mode == 'filter':
        query=filtered_query
    elif mode == 'export':
        query=filtered_query
        fh,output_file = tempfile.mkstemp(suffix='', prefix='Users_', dir=None, text=False)
        dict = {'header':{},'detail':[]}
        count = 0
        rows = query.all()
        for row in rows:
            dict['detail'].append({})
            for column in ['id', 'username', 'role_id', 'email', 'password_hash', 'confirmed', 'CC_Id']:
                dict['detail'][count].update( { column:str(row.__getattribute__(column))})
                
            count += 1
        dict['header'].update({'count':count})
        jsonarray      = json.dumps(dict)
        data           = json.loads(jsonarray)  
        dataframe      = json_normalize(data, 'detail').assign(**data['header'])
        fh,output_file = tempfile.mkstemp(suffix='', prefix='Users_', dir='/tmp', text=False)
        xlsx_file      = '%s/%s'%(current_app.root_path,url_for('static',filename='%s.xls'%(output_file)))
        dataframe.to_excel(xlsx_file,sheet_name='Users',columns=['id', 'username', 'role_id', 'email', 'password_hash', 'confirmed', 'CC_Id'])
        return send_file(xlsx_file,as_attachment=True,attachment_filename=output_file.replace('/','_')+'.xls')
    elif mode == 'add':
        return redirect(url_for('.forms_Users'))
    elif mode == 'select':
        pass
        # if some filter is required
        if field is not None:
            if field == 'id':
                if value is not None:
                    query = query.filter_by(id=value)
            if field == 'username':
                if value is not None:
                    query = query.filter_by(username=value)
            if field == 'role_id':
                if value is not None:
                    query = query.filter_by(role_id=value)
            if field == 'email':
                if value is not None:
                    query = query.filter_by(email=value)
            if field == 'password_hash':
                if value is not None:
                    query = query.filter_by(password_hash=value)
            if field == 'confirmed':
                if value is not None:
                    query = query.filter_by(confirmed=value)
            if field == 'CC_Id':
                if value is not None:
                    query = query.filter_by(CC_Id=value)
            # JOIN other tables and generate foreign fields
    query = query.join(Role,User.role_id == Role.role_id).add_columns(Role.name).join(cost_center,User.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)
    
    # Actual request from DB follows
    tracebox_log(query,logger,length=50)
    rows = query.paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
    # Setting pagination variables ...
    if field is not None:
       next_url = url_for('.select_Users_query', field=field, value=value, page=rows.next_num) if rows.has_next else None
       prev_url = url_for('.select_Users_query', field=field, value=value, page=rows.prev_num) if rows.has_prev else None
    else:
       next_url = url_for('.select_Users_query', page=rows.next_num) if rows.has_next else None
       prev_url = url_for('.select_Users_query', page=rows.prev_num) if rows.has_prev else None
    # Actual rendering ...
    if request.headers.get('Content-Type') is not None or request.args.get('JSON',None,type=str) is not None:
        if "JSON" in request.headers.get('Content-Type') or request.args.get('JSON',None,type=str) is not None:
            logger.debug('select_Users_query(): will render: JSON rows')
            logger.debug('select_Users_query(): Exit')
            return json.dumps(serialize_object(rows.__dict__))
    logger.debug('select_Users_query(): will render: users_All.html')
    logger.debug('select_Users_query(): Exit')
    return render_template('users_select_All.html',rows=rows,options=options)
#===============================================================================
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
                                #Pla_Name        = form.Pla_Id.choices[pla_index][1],
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
                                #Pla_Name        = form.Pla_Id.choices[pla_index][1],
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

    return render_template('charging_resume_all.html',form=form, data=session.get('data'))

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
        CI = db.session.query(Configuration_Items.CI_Id).\
                distinct().\
                order_by(Configuration_Items.CC_Id,Configuration_Items.CI_Id).all()
        
        logger.debug ("report_Changing_Resume_All: %d CI's found "%(len(CI)))
        
        resume_records=0

        for ci in CI:
            records = db.Update_Charge_Resume_CI2(CIT_Date_From,CIT_Date_To,CIT_Status,Cur_Code,ci)
            if records is not None:
                resume_records += records # OJO AQUI ME QUEDE 

        logger.debug ("report_Changing_Resume_All: resume_records = %s"%resume_records)
        
    # Get Actual Remume Data from Database
    # NOTE: Here needs some Sand-Clock Message or something in case it takes so long ...
    rows = db.Get_Charge_Resume2(4,0,CIT_Date_From,CIT_Date_To,CIT_Status,Cur_Code)
    
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

from emtec.collector.forms  import frm_charging_resume_cc
from babel.numbers          import format_number, format_decimal, format_percent

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
    # ------------------------------------------------------------------------------

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
        # -------------------------------------------------------------------------------------------------------------- #
        LISTA = db.get_cost_centers(CC_Id)
        CI = db.session.query(Configuration_Items.CI_Id).\
                filter(Configuration_Items.CI_Id.in_(LISTA)).\
                order_by(Configuration_Items.CC_Id,Configuration_Items.CI_Id).all()
        
        logger.debug ("report_Changing_Resume: %d CI's found for cost center %d"%(len(CI),CC_Id))
        
        resume_records=0

        for ci in CI:
            records = db.Update_Charge_Resume_CI2(CIT_Date_From,CIT_Date_To,CIT_Status,Cur_Code,ci.CI_Id)
            if records is not None:
                resume_records += records
            
        logger.debug ("report_Changing_Resume: resume_records = %s"%resume_records)
        
    # Get Actual Remume Data from Database
    # NOTE: Here needs some Sand-Clock Message or something in case it takes so long ...
    rows = db.Get_Charge_Resume2(2,CC_Id,CIT_Date_From,CIT_Date_To,CIT_Status,Cur_Code)
    
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
        CI = db.session.query(Configuration_Items.CI_Id.distinct()).\
                filter(Configuration_Items.Cus_Id==Cus_Id).\
                order_by(Configuration_Items.CI_Id)
        print(CI)
        CI=CI.all()
        logger.debug ("report_Changing_Resume_Level: %d CI's found for customer %d"%(len(CI),Cus_Id))
        
        resume_records=0

        for ci in CI:
            records = db.Update_Charge_Resume_CI2(CIT_Date_From,CIT_Date_To,CIT_Status,Cur_Code,ci)
            if records is not None:
                resume_records += records
            
        logger.debug ("report_Changing_Resume_Level: resume_records = %s"%resume_records)
        
    # Get Actual Remume Data from Database
    # NOTE: Here needs some Sand-Clock Message or something in case it takes so long ...
    rows =  db.Get_Charge_Resume(Cus_Id,CIT_Date_From,CIT_Date_To,CIT_Status,Cur_Code)
    
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

    return render_template('charging_resume_platform.html',form=form, data=session.get('data'))

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
        # query="C*ALL Update_Charge_Resume(%d,'%s','%s',%d,'%s')"%(Pla_Id,CIT_Date_From,CIT_Date_To,CIT_Status,Cur_Code) #
        # resume_records = db.engine.execute(query).scalar()                                                             #
        # -------------------------------------------------------------------------------------------------------------- #
        # 20181228 GV query = "S*ELECT DISTINCT CI_Id FROM Configuration_Items WHERE Pla_Id=%d"%(Pla_Id)
        """
        query = "S*ELECT CI_Id FROM Configuration_Items WHERE Pla_Id=%d ORDER BY CC_Id,CI_Id"%(Pla_Id)
        
        logger.debug ("report_Changing_Resume_Platform: query: %s"%(query))

        CI = db.engine.execute(query)
        """
        
        CI = db.session.query(Configuration_Items.CI_Id).\
                filter(Configuration_Items.Pla_Id==Pla_Id).\
                order_by(Configuration_Items.CC_Id,Configuration_Items.CI_Id).all()
        
        logger.debug ("report_Changing_Resume_Platform: %d CI's found for platform %d"%(len(CI),Pla_Id))
        
        resume_records=0

        print("CI=",CI)
        for ci in CI:
            """
            query="C*ALL Update_Charge_Resume_CI2('%s','%s',%s,'%s',%s)"%\
                    (CIT_Date_From,CIT_Date_To,CIT_Status,Cur_Code,ci.CI_Id)
            logger.debug ("report_Changing_Resume_Platform: query: %s"%query)
            records=db.engine.execute(query)
            resume_records += records.scalar()
            """
            records = db.Update_Charge_Resume_CI2(CIT_Date_From,CIT_Date_To,CIT_Status,Cur_Code,ci)
            if records is not None:
                resume_records += records
        logger.debug ("report_Changing_Resume_Platform: resume_records = %s"%resume_records)
        
    # Get Actual Remume Data from Database
    # NOTE: Here needs some Sand-Clock Message or something in case it takes so long ...
    """
    query="C*ALL Get_Charge_Resume2(3,%d,'%s','%s',%d,'%s')"%(Pla_Id,CIT_Date_From,CIT_Date_To,CIT_Status,Cur_Code)
    
    logger.debug ("report_Changing_Resume: query: %s"%query)
    
    rows =  db.engine.execute(query).fetchall()
    """
    rows = db.Get_Charge_Resume2(3,Pla_Id,CIT_Date_From,CIT_Date_To,CIT_Status,Cur_Code)
    
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
# GLVH @ 2019-08-18 Refactoring to ORM DB Only
# =============================================================================

#from    sqlalchemy.orm             import sessionmaker

from emtec.collector.forms       import frm_charging_resume
from babel.numbers  import format_number, format_decimal, format_percent
from emtec.collector.db.orm_model      import Configuration_Items

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
            #flash('WILL USE FULL ORM DB VERSION ...')
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
        # query="C*ALL Update_Charge_Resume(%d,'%s','%s',%d,'%s')"%(Cus_Id,CIT_Date_From,CIT_Date_To,CIT_Status,Cur_Code) #
        # resume_records = db.engine.execute(query).scalar()                                                             #
        # -------------------------------------------------------------------------------------------------------------- #
        # 20181228 GV query = "S*ELECT DISTINCT CI_Id FROM Configuration_Items WHERE Cus_Id=%d"%(Cus_Id)
        """ 20190819 GV
        #query = "S*ELECT CI_Id FROM Configuration_Items WHERE Cus_Id=%d ORDER BY CC_Id,CI_Id"%(Cus_Id)
        
        logger.debug ("report_Changing_Resume: query: %s"%(query))

        CI = db.engine.execute(query)
        """
        CI = db.session.query(Configuration_Items.CI_Id).\
                filter(Configuration_Items.Cus_Id==Cus_Id).\
                order_by(Configuration_Items.CC_Id,Configuration_Items.CI_Id).all()
        #print("CI=",CI,type(CI),dir(CI))
        #logger.debug ("report_Changing_Resume: %d CI's found for customer %d"%(CI.count(),Cus_Id))
        logger.debug ("report_Changing_Resume: %d CI's found for customer %d"%(len(CI),Cus_Id))
        #flash        ("report_Changing_Resume: %d CI's found for customer %d"%(len(CI),Cus_Id))
        
        
        resume_records=0

        for ci in CI:
            """ 20190819 GV
            query="C*ALL Update_Charge_Resume_CI(%s,'%s','%s',%s,'%s',%s)"%\
                    (Cus_Id,CIT_Date_From,CIT_Date_To,CIT_Status,Cur_Code,ci.CI_Id)
            logger.debug ("report_Changing_Resume: query: %s"%query)
            records=db.engine.execute(query)
            """
            records = db.Update_Charge_Resume_CI(Cus_Id,CIT_Date_From,CIT_Date_To,CIT_Status,Cur_Code,ci.CI_Id)
            #resume_records += records.scalar()
            resume_records += records

        logger.debug ("report_Changing_Resume: resume_records = %s"%resume_records)
        #flash        ("report_Changing_Resume: resume_records = %s"%resume_records)
        
    # Get Actual Remume Data from Database
    # NOTE: Here needs some Sand-Clock Message or something in case it takes so long ...
    """ 20190819 GV
    query="C*ALL Get_Charge_Resume(%d,'%s','%s',%d,'%s')"%(Cus_Id,CIT_Date_From,CIT_Date_To,CIT_Status,Cur_Code)
    
    logger.debug ("report_Changing_Resume: query: %s"%query)
    
    rows =  db.engine.execute(query).fetchall()
    """
    rows = db.Get_Charge_Resume(Cus_Id,CIT_Date_From,CIT_Date_To,CIT_Status,Cur_Code)
    #flash("rows = db.Get_Charge_Resume(%s,%s,%s,%s,%s)"%(Cus_Id,CIT_Date_From,CIT_Date_To,CIT_Status,Cur_Code))
    #flash("type rows = %s)"%(type(rows)))
    #flash("dir rows = %s)"%(dir(rows)))
    #flash("len rows = %s)"%(len(rows)))

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
    """
    query = "SELECT * "\
                "FROM Rates "\
                    "JOIN Customers             USING   (Cus_Id) "\
                    "JOIN Platforms             USING   (Pla_Id) "\
                    "JOIN Configuration_Items   USING   (CI_Id) "\
                    "JOIN Cost_Centers          ON      Cost_Centers.CC_Id=Rates.CC_id "\
                "ORDER BY Typ_Code,Rates.Pla_Id,Rates.Cus_Id,Rates.CC_Id,Rates.CI_Id"
    """
    # GV 20190907
    """
    query = db.session.query(Rates,Customers,Platforms,Configuration_Items,Cost_Centes).\
                join(Customers          , Rates.Cus_Id == Customers.Cus_Id).\
                join(Platforms          , Rates.Pla_Id == Platforms.Pla_Id).\
                join(Configuration_Items, Rates.CI_Id  == Configuration_Items.CI_Id).\
                join(Cost_Centers       , Rates.CC_Id  == Cost_Centers.CC_Id).\
                order_by(   Rates.Typ_Code,
                            Rates.Pla_Id,
                            Rates.Cus_Id,
                            Rates.CC_Id,
                            Rates.CI_Id)
    """
    
    query = db.session.query(rate,customer,platform,configuration_item,cost_center).\
                join(customer          , rate.Cus_Id == customer.Cus_Id).\
                join(platform          , rate.Pla_Id == platform.Pla_Id).\
                join(configuration_item, rate.CI_Id  == configuration_item.CI_Id).\
                join(cost_center       , rate.CC_Id  == cost_center.CC_Id).\
                order_by(   rate.Typ_Code,
                            rate.Pla_Id,
                            rate.Cus_Id,
                            rate.CC_Id,
                            rate.CI_Id)
    
    rate_rows=[]

    try:
        rate_rows = db.session.execute(query).fetchall()
    except Exception as e:
        print("**************************************")
        print(e)
        print("**************************************")

    data.update({'rate_rows': rate_rows})

    """ GV 20190907 AQUI AUN HAY QUE CONSTRUIR UN ALGORITMO EQUIVALENTE
    query = "SELECT CU_Id,CU_Description,Typ_Code,Pla_Id,Cus_Id,CI.CC_Id AS CC_ID,Rat_Id,"\
                    "Get_Rate_Id (Typ_Code,Pla_Id,Cus_Id,CI.CC_Id,CU_Id) AS RATE, "\
                    "Pla_Name,Cus_Name,CC_Description,CI_Name "\
                "FROM Charge_Units AS CU "\
                    "JOIN Configuration_Items AS CI  USING (CI_Id) "\
                    "JOIN Platforms           AS PLA USING (Pla_Id) "\
                    "JOIN Customers           AS CUS USING (Cus_Id) "\
                    "JOIN Cost_Centers        AS CC  ON CC.CC_Id = CI.CC_Id "\
                "WHERE Rat_Id != Get_Rate_Id(Typ_Code,Pla_Id,Cus_Id,CI.CC_Id,CU_Id)"
    """

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

# NOTE: THOS IS FULL MYSQL CODE NEEDS TO BE VARIABLE ADAPTED FOR
# AGNOSTIC DB STATUS REPORT

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

    """
    query = "S*ELECT COUNT(*) AS RECORDS,Cus_Id,CR_Date_From,CR_Date_To,CIT_Status,Cur_Code,Cus_Name FROM Charge_Resumes "\
                "GROUP BY Cus_Id,CR_Date_From,CR_Date_To,CIT_Status,Cur_Code,Cus_Name "\
                "ORDER BY Cus_Name,CR_Date_From,CR_Date_To,CIT_Status,Cur_Code"
                
    rows=db.engine.execute(query).fetchall()
    """
    
    """
    row = db.session.query( func.count(Charge_Resumes.Cus_Id).label('RECORDS'),
                    Charge_Resumes.Cus_Id,
                    Charge_Resumes.CR_Date_From,
                    Charge_Resumes.CR_Date_To,
                    Charge_Resumes.CIT_Status,
                    Charge_Resumes.Cur_Code,
                    Charge_Resumes.Cus_Name
                    ).\
                group_by(   Charge_Resumes.Cus_Id,
                            Charge_Resumes.CR_Date_From,
                            Charge_Resumes.CR_Date_To,
                            Charge_Resumes.CIT_Status,
                            Charge_Resumes.Cur_Code,
                            Charge_Resumes.Cus_Name).\
                order_by(   Charge_Resumes.Cus_Name,
                            Charge_Resumes.CR_Date_From,
                            Charge_Resumes.CR_Date_To,
                            Charge_Resumes.CIT_Status,
                            Charge_Resumes.Cur_Code)
    """
    rows = db.session.query( func.count(charge_resume.Cus_Id).label('RECORDS'),
                    charge_resume.Cus_Id,
                    charge_resume.CR_Date_From,
                    charge_resume.CR_Date_To,
                    charge_resume.CIT_Status,
                    charge_resume.Cur_Code,
                    charge_resume.Cus_Name
                    ).\
                group_by(   charge_resume.Cus_Id,
                            charge_resume.CR_Date_From,
                            charge_resume.CR_Date_To,
                            charge_resume.CIT_Status,
                            charge_resume.Cur_Code,
                            charge_resume.Cus_Name).\
                order_by(   charge_resume.Cus_Name,
                            charge_resume.CR_Date_From,
                            charge_resume.CR_Date_To,
                            charge_resume.CIT_Status,
                            charge_resume.Cur_Code)
    
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
    """
    query="C*ALL Get_Charge_Resume(%d,'%s','%s',%d,'%s')"%(Cus_Id,CIT_Date_From,CIT_Date_To,CIT_Status,Cur_Code)
    
    rows =  db.engine.execute(query).fetchall()
    """
    rows = db.Get_Charge_Resume(Cus_Id,CIT_Date_From,CIT_Date_To,CIT_Status,Cur_Code)
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

    USERCAN = db.get_user_cost_centers(current_user.id) 
    rows = db.session.query(    func.count(user_resumes.CI_CC_Id).label('RECORDS'),
                        user_resumes.CI_CC_Id,
                        user_resumes.CR_Date_From,
                        user_resumes.CR_Date_To,
                        user_resumes.CIT_Status,
                        user_resumes.Cur_Code,
                        user_resumes.CC_Description).\
                    filter(     user_resumes.CI_CC_Id.in_(USERCAN)).\
                    group_by(   user_resumes.CI_CC_Id,
                                user_resumes.CR_Date_From,
                                user_resumes.CR_Date_To,
                                user_resumes.CIT_Status,
                                user_resumes.Cur_Code,
                                user_resumes.CC_Description).\
                    order_by(   user_resumes.CI_CC_Id,
                                user_resumes.CR_Date_From,
                                user_resumes.CR_Date_To,
                                user_resumes.CIT_Status,
                                user_resumes.Cur_Code)
    # Load Statuses
    statuses=cit_status.query.all()
    dstatuses={}
    for s in statuses:
        dstatuses[s.CIT_Status]=s.Value
        
    currencies=currency.query.all()
    dcurrencies={}
    for c in currencies:
        dcurrencies[c.Cur_Code]=c.Cur_Name
    
    # Load Currency Names

    export_choices = []
    for row in rows:
        option="%s_%s_%s_%s_%s_%s"%(row.CI_CC_Id,row.CR_Date_From,row.CR_Date_To,row.CIT_Status,row.Cur_Code,row.CC_Description)
        value ="%s from %s to %s status=%s currency=%s"%(row.CC_Description,row.CR_Date_From,row.CR_Date_To,dstatuses[row.CIT_Status],dcurrencies[row.Cur_Code])
        export_choices.append((option,value))
    
    form.Export.choices   = export_choices

    if form.validate_on_submit():

        data=form.Export.data.split("_")
        print("data=",data)
        
        CC_Code=db.session.query(cost_center.CC_Code).filter(cost_center.CC_Id==data[0]).one()
        
        if     form.submit_PDF.data:
            return redirect(url_for('.export_User_Resume',
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
    rows = db.Get_User_Resume(current_user.id,CIT_Date_From,CIT_Date_To,CIT_Status,Cur_Code)

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
# View for User Data in Tree structure
# (c) Sertechno 2018,2019
# GLVH @ 2019-01-11
# =============================================================================

# view required imports
import json
from pprint import pprint

# view required functions

img='xxx'

def load_children(DATA,children):
        cc_counter=0
        for child in children:
            #print("%s: child=%s"%(__name__,child))
            DATA.append({'cc_id':child.CC_Id,'cc_code':child.CC_Code,'cc_description':child.CC_Description,'children':[],'ci_list':[]})
            # Load CIs
            query=db.session.query(configuration_item.CI_Id,configuration_item.CI_Name).filter(configuration_item.CC_Id==child.CC_Id)
            CIS=query.all()
            ci_counter=0
            for ci in CIS:
                DATA[cc_counter]['ci_list'].append({'ci_id':ci.CI_Id,'ci_name':ci.CI_Name,'cu_list':[]})
                # Load CUs
                #query=db.session.query(charge_unit.CU_Id,charge_unit.CU_Description).filter(charge_unit.CI_Id==ci.CI_Id)
                query=db.session.query(charge_unit).filter(charge_unit.CI_Id==ci.CI_Id)
                CUS=query.all()
                for cu in CUS:
                    ref=''
                    if cu.CU_UUID is not None:
                        ref=    ( " / %s"%cu.CU_UUID.strip()        if (len( cu.CU_UUID.strip() ) > 0) else '')
                    if cu.CU_Reference_1 is not None:
                        ref=ref+( " / %s"%cu.CU_Reference_1.strip() if (len( cu.CU_Reference_1.strip() ) > 0) else '')
                    if cu.CU_Reference_2 is not None:
                        ref=ref+( " / %s"%cu.CU_Reference_2.strip() if (len( cu.CU_Reference_2.strip() ) > 0) else '')
                    if cu.CU_Reference_3 is not None:
                        ref=ref+( " / %s"%cu.CU_Reference_3.strip() if (len( cu.CU_Reference_3.strip() ) > 0) else '')
                    DATA[cc_counter]['ci_list'][ci_counter]['cu_list'].append({'cu_id':cu.CU_Id,'cu_description':cu.CU_Description,'cu_reference':ref})
                ci_counter+=1
            
            # Look for more children
            query=db.session.query(cost_center).filter(cost_center.CC_Parent_Code==child.CC_Code,cost_center.CC_Code!=cost_center.CC_Parent_Code)
            list_children_cc=query.all()
            #print("%s: list_children_cc=%s"%(__name__,list_children_cc))
            if len(list_children_cc)>0:
                load_children(DATA[cc_counter]['children'],list_children_cc)
            cc_counter+=1

def render_ci(ci,f,level):
    img='<img src="/static/img/edit.png" width="32" height="32" title="" alt="Details">'
    indent="  "*level
    M='<font color="white">%s</font>'%("MM"*level)
    cu_list_name="cul_%s"%ci['ci_id']
    # If there is CUs
    if len(ci['cu_list']):
        href="/forms/Configuration_Items?CI_Id=%s"%ci['ci_id']
        if ci['ci_id'] == 1:
            href='#'
            img=''
        f.write('%s%s<button type="button" class="btn btn-link" data-toggle="collapse" data-target="#%s">Configuration Item: %s (%s Charge Units)</button><a href="%s"  target="_blank">%s</a><br>\n'%\
                            (indent*3,M*2, cu_list_name, ci['ci_name'], len(ci['cu_list']),href,img))
                            
        f.write('%s<div id="%s" class="collapse">\n'%(indent*4,cu_list_name))
        for cu in ci['cu_list']:
            href="/forms/Charge_Units?CU_Id=%s"%cu['cu_id']
            if cu['cu_id'] == 1:
                f.write('%s%sCharge Unit: %s %s<br>\n'%(indent*5,M*3,cu['cu_description'],cu['cu_reference']))
            else:
                f.write('%s%s<a href="%s" target="_blank">Charge Unit: %s %s</a><br>\n'%(indent*5,M*3,href,cu['cu_description'],cu['cu_reference']))
                            
        f.write("%s</div>"%(indent*4))
    else:
        href="/forms/Configuration_Items?CI_Id=%s"%ci['ci_id']
        f.write('%s%s<a href="%s" target="_blank">Configuration Item: %s %s</a><br>\n'% (indent*3,M*2, href, ci['ci_name'],img) )                     

def render_children(DATA,f,level=1):
    img='<img src="/static/img/edit.png" width="32" height="32" title="" alt="Details">'
    child_counter=0
    indent="  "*level
    M='<font color="white">%s</font>'%("MM"*level)
    cc_list_name="ccl_%s"%id(DATA['children'])
    for child in DATA['children']:
        # If there's CIs
        if len(child['ci_list'])>0:
            href="/forms/Cost_Centers?CC_Id=%s"%child['cc_id']
            ci_list_name="cil_%s"%child['cc_id']
            if child['cc_id'] == 1:
                f.write('%s%s'
                    '<button type="button" class="btn btn-link" data-toggle="collapse" data-target="#%s">Cost Center: %s %s (%s Configuration Items)</button>'
                    '<a href="%s" target="_blank">%s</a><br>\n'%\
                     (indent,M, 
                      ci_list_name, child['cc_code'], child['cc_description'], len(child['ci_list']),
                      "#",""))
            else:
                f.write('%s%s'
                    '<button type="button" class="btn btn-link" data-toggle="collapse" data-target="#%s">Cost Center: %s %s (%s Configuration Items)</button>'
                    '<a href="%s" target="_blank">%s</a><br>\n'%\
                     (indent,M, 
                      ci_list_name, child['cc_code'], child['cc_description'], len(child['ci_list']),
                      href,img))
            f.write('%s<div id="%s" class="collapse">\n'%(indent*2,ci_list_name))
                
            for ci in child['ci_list']:
                render_ci(ci,f,level)
            f.write("%s</div>"%(indent*2))
        else:
            href="/forms/Cost_Centers?CC_Id=%s"%child['cc_id']
            f.write('<font color="white">%s%s__</font><a href="%s" target="_blank">Cost Center: %s %s</a><br>\n'%(indent,M, href, child['cc_code'], child['cc_description'])  )      
        if len(child['children'])>0:
            render_children(child,f,level+1)
        child_counter+=1        

    
@main.route('/forms/User_Data_View', methods=['GET'])
@login_required
@permission_required(Permission.CUSTOMER)
def forms_User_Data_View():
    logger.debug('Enter: forms_User_Data_View()'%())

    USER=current_user.id

    user_cc=db.session.query(User.CC_Id).filter(User.id==USER).scalar() 
    list_cc=db.session.query(cost_center).filter(cost_center.CC_Id==user_cc).all() 

    DATA={}
    DATA.update({'user':{'user_id':USER},'cc_id':list_cc[0].CC_Id,'cc_code':list_cc[0].CC_Code,'cc_description':list_cc[0].CC_Description,'children':[]})

    #print("Children=",DATA['children'])
    #print("list_cc=",list_cc)

    load_children(DATA['children'],list_cc)
    #print("DATA=",DATA)

    #filename="tmp/%s_%s_user_data_tree.html"%(current_user.id,id(current_user.id))
    filename="tmp/%s_user_data_tree.html"%(current_user.id)
    try:
        f=open("/%s"%filename,'w')
    except Exception as e:
        message=("Couldn't open file: '%s'. Please inform administrator. EXCEPTION: %s"%(filename,e))
        flash(message)
        logger.error(message)
        return render_template("exception.html",filename=filename,data=DATA)

    
#  generate HTML

    render_children(DATA,f)
   
    f.close()
    
    return render_template("user_data_view.html",filename=filename,data=DATA)

# =============================================================================

# =============================================================================
# View for Get Charging Resume from DB
# (c) Sertechno 2018
# GLVH @ 2018-11-26
# =============================================================================

from emtec.collector.forms       import frm_user_resume
from babel.numbers  import format_number, format_decimal, format_percent

"""
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
        #query = db.session.execute("S*ELECT CC_Id FROM Cost_Centers WHERE CC_Parent_Code='DEFAULT-CC-CODE' AND CC_Id>1")
        query = db.query(Cost_Centers.CC_Id).\
                    filter(Cost_Centers.CC_Parent_Code=='DEFAULT-CC-CODE').\
                    filter(Cost_Centers.CC_Id > 1).all()
    else:
        #query = db.session.execute("S*ELECT CC_Id FROM Cost_Centers WHERE usercancc(%s,CC_Id)"%current_user.id)
        USERCAN = db.get_user_cost_centers(current_user.id,CC_Id)
        query = db.query(Cost_Centers.CC_Id).\
                    filter(Cost_Centers.CC_Id.in_(USERCAN)).all
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
"""

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
        #query = db.session.execute("S*ELECT CC_Id FROM cost_center WHERE CC_Parent_Code='DEFAULT-CC-CODE' AND CC_Id>1")
        query = db.session.query(cost_center.CC_Id
                        ).filter(cost_center.CC_Parent_Code=='DEFAULT-CC-CODE'
                        ).filter(cost_center.CC_Id > 1
                        ).all()
    else:
        #20200210 GV USERCAN = db.get_user_cost_centers(current_user.id,current_user.CC_Id)
        USERCAN = db.get_user_cost_centers(current_user.id)
        query = db.session.query(cost_center.CC_Id).\
                    filter(cost_center.CC_Id.in_(USERCAN)).all()
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

"""
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
        # query="C*ALL Update_Charge_Resume(%d,'%s','%s',%d,'%s')"%(Cus_Id,CIT_Date_From,CIT_Date_To,CIT_Status,Cur_Code) #
        # resume_records = db.engine.execute(query).scalar()                                                             #
        # -------------------------------------------------------------------------------------------------------------- #
        # 20181228 GV query = "S*ELECT DISTINCT CI_Id FROM Configuration_Items WHERE Cus_Id=%d"%(Cus_Id)
        CCISBELOW=get_cost_centers(CC_Id)
        if current_user.CC_Id == 1:        
            " ""
            query = "S*ELECT CI_Id FROM Configuration_Items WHERE CC_Id IN (S*ELECT CC_Id FROM Cost_Centers WHERE ccisbelow(CC_Id,%d)) ORDER BY CC_Id,CI_Id"%(CC_Id)
            print("query=",query)
            " ""
            query = db.query(Configuration_Items.CI).\
                        filter(Configuration_Items.CC_Id.in_(CCISBELOW)).\
                        order_by(Configuration_Items.CC_Id,Configuration_Items.CI_Id)
        else:
            " ""
            query = "S*ELECT CI_Id FROM Configuration_Items WHERE CC_Id IN (S*ELECT CC_Id FROM Cost_Centers WHERE usercancc(%d,CC_Id) AND ccisbelow(CC_Id,%d)) ORDER BY CC_Id,CI_Id"%(current_user.id,CC_Id)
            " ""
            USERCAN=get_user_cost_centers(CC_Id)
            query = db.query(Configuration_Items.CI).\
                        filter(Configuration_Items.CC_Id.in_(USERCAN)).\
                        filter(Configuration_Items.CC_Id.in_(CCISBELOW)).\
                        order_by(Configuration_Items.CC_Id,Configuration_Items.CI_Id)
            
        " ""
        logger.debug ("report_User_Resume: query: %s"%(query))

        CI = db.engine.execute(query)
        " ""
        CI = query.all()
        
        print ("report_User_Resume: %d CI's found for user %d"%(CI.rowcount,current_user.id))
        logger.debug ("report_User_Resume: %d CI's found for user %d"%(CI.rowcount,current_user.id))
        
        resume_records=0

        for ci in CI:
            " ""
            query="C*ALL Update_User_Resume_CI('%s','%s',%s,'%s',%s)"%\
                    (CIT_Date_From,CIT_Date_To,CIT_Status,Cur_Code,ci.CI_Id)
            logger.debug ("report_User_Resume: query: %s"%query)
            records=db.engine.execute(query)
            resume_records += records.scalar()
            " ""
            records = db.Update_User_Resume_CI(CIT_Date_From,CIT_Date_To,CIT_Status,Cur_Code,ci.CI_Id)
            resume_records += records
            
        logger.debug ("report_User_Resume: resume_records = %s"%resume_records)
        
    # Get Actual Resume Data from Database
    # NOTE: Here needs some Sand-Clock Message or something in case it takes so long ...
    if current_user.CC_Id == 1:
        user_id=db.session.query(User.id).filter(User.CC_Id==CC_Id).one()      
        #query="C*ALL Get_User_Resume(%d,'%s','%s',%d,'%s',%d)"%(current_user.id,CIT_Date_From,CIT_Date_To,CIT_Status,Cur_Code,CC_Id)
        #query="C*ALL Get_User_Resume(%d,'%s','%s',%d,'%s',%d)"%(user_id.id,CIT_Date_From,CIT_Date_To,CIT_Status,Cur_Code,CC_Id)
        rows = db.Get_User_Resume(user_id.id,CIT_Date_From,CIT_Date_To,CIT_Status,Cur_Code,CC_Id)
    else:
        #query="C*ALL Get_User_Resume(%d,'%s','%s',%d,'%s',%d)"%(current_user.id,CIT_Date_From,CIT_Date_To,CIT_Status,Cur_Code,CC_Id)
        rows = db.Get_User_Resume(current_user.id,CIT_Date_From,CIT_Date_To,CIT_Status,Cur_Code,CC_Id)
    "" "
    logger.debug ("report_User_Resume: query: %s"%query)
    print ("report_User_Resume: query: %s"%query)
    
    rows =  db.engine.execute(query).fetchall()
    "" "
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
"""


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
        # query="C*ALL Update_Charge_Resume(%d,'%s','%s',%d,'%s')"%(Cus_Id,CIT_Date_From,CIT_Date_To,CIT_Status,Cur_Code) #
        # resume_records = db.engine.execute(query).scalar()                                                             #
        # -------------------------------------------------------------------------------------------------------------- #
        # 20181228 GV query = "S*ELECT DISTINCT CI_Id FROM configuration_item WHERE Cus_Id=%d"%(Cus_Id)
        print("***********************")
        print("Update Mode")
        print("current user=",current_user)
        print("current user id=",current_user.id)
        print("current user CC_Id=",current_user.CC_Id)
        
        CCISBELOW=db.get_cost_centers(CC_Id)
        print("CCISBELOW=",CCISBELOW)
        if current_user.CC_Id == 1:        
        #if current_user.id == 1:        
            query = db.session.query(configuration_item.CI_Id).\
                        filter(configuration_item.CC_Id.in_(CCISBELOW)).\
                        order_by(configuration_item.CC_Id,configuration_item.CI_Id)
        else:
            #USERCAN=db.get_user_cost_centers(CC_Id)
            USERCAN=db.get_user_cost_centers(current_user.id)
            print("USERCAN=",USERCAN)
            query = db.session.query(configuration_item.CI_Id).\
                        filter(configuration_item.CC_Id.in_(USERCAN)).\
                        filter(configuration_item.CC_Id.in_(CCISBELOW)).\
                        order_by(configuration_item.CC_Id,configuration_item.CI_Id)
            
        CI = query.all()
        print("CI=",CI)

        
        #print ("report_User_Resume: %d CI's found for user %d"%(CI.rowcount,current_user.id))
        #logger.debug ("report_User_Resume: %d CI's found for user %d"%(CI.rowcount,current_user.id))
        print ("report_User_Resume: %d CI's found for user %d"%(len(CI),current_user.id))
        logger.debug ("report_User_Resume: %d CI's found for user %d"%(len(CI),current_user.id))
        
        resume_records=0

        for ci in CI:
            """print("records = db.Update_User_Resume_CI(%s,%s,%s,%s,%s)"%(
                CIT_Date_From,
                CIT_Date_To,
                CIT_Status,
                Cur_Code,
                ci.CI_Id))"""
            #records = db.Update_User_Resume_CI(CIT_Date_From,CIT_Date_To,CIT_Status,Cur_Code,ci.CI_Id)
            print("records = db.Update_User_Resume_CI(%s,%s,%s,%s,%s,%s)"%(
                current_user.id,
                CIT_Date_From,
                CIT_Date_To,
                CIT_Status,
                Cur_Code,
                ci.CI_Id))
            records = db.Update_User_Resume_CI(current_user.id,CIT_Date_From,CIT_Date_To,CIT_Status,Cur_Code,ci.CI_Id)
            print("ci=",ci,"records=",records)
            if records is not None:
                resume_records += records
            
        logger.debug ("report_User_Resume: resume_records = %s"%resume_records)
        
    # Get Actual Resume Data from Database
    # NOTE: Here needs some Sand-Clock Message or something in case it takes so long ...
    try:
        print("rows = db.Get_User_Resume(%s,%s,%s,%s,%s)"%(
            current_user.id,
            CIT_Date_From,
            CIT_Date_To,
            CIT_Status,
            Cur_Code))
        if current_user.CC_Id == 1:
            user_id=db.session.query(User.id).filter(User.CC_Id==CC_Id).one()      
            # 20200207 GV rows = db.Get_User_Resume(user_id.id,CIT_Date_From,CIT_Date_To,CIT_Status,Cur_Code,CC_Id)
            #rows = db.Get_Charge_Resume(user_id.id,CIT_Date_From,CIT_Date_To,CIT_Status,Cur_Code)
            rows = db.Get_User_Resume(current_user.id,CIT_Date_From,CIT_Date_To,CIT_Status,Cur_Code)
        else:
            # rows = db.Get_User_Resume(current_user.id,CIT_Date_From,CIT_Date_To,CIT_Status,Cur_Code,CC_Id)
            rows = db.Get_User_Resume(current_user.id,CIT_Date_From,CIT_Date_To,CIT_Status,Cur_Code)
        return render_template('report_user_resume.html',rows=rows,
                    CC_Description=CC_Description,
                    CIT_Date_From=CIT_Date_From,
                    CIT_Date_To=CIT_Date_To,
                    CIT_Status=CIT_Status,
                    CIT_Status_Value=CIT_Status_Value,                
                    Cur_Code=Cur_Code,
                    Cur_Name=Cur_Name
                    )
    except Exception as e:
        print("EXCEPCION",str(e))
        message=str(e)
        return render_template("404.html",message=message), 404
