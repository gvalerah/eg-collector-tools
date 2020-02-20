


#-----------------------------------------------------------------------
def chk_c000001(*args,**kwargs):
    pass
    
from emtec.common.interface import *
from emtec.collector.db.orm_model          import Interface
from emtec.collector.db.flask_models       import interface
from emtec.collector.db.flask_models       import *
#-----------------------------------------------------------------------
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2020-01-31 18:07:30
# =============================================================================

# ======================================================================
#  Auto-Generated code. Do not modify 
#  (C) Sertechno/Emtec Group (2018,2019)
#  GLVH @ 2020-01-31 18:07:34.508113
# ======================================================================
        

from pprint import pprint, pformat

# gen_views_select_query.html:AG 2020-01-31 18:07:34.586184        
#@main.route('/select/Configuration_Items_Query', methods=['GET','POST'])
#@login_required
#@admin_required
def select_Configuration_Items_query():
    """ Select rows handling function for table 'Configuration_Items' """
    #logger.debug('select_Configuration_Items_query(): Enter')
    #chk_c000001(filename=os.path.join(current_app.root_path, '.c000001'),request=request,db=db,logger=logger)
    # Get parameters from URL call
    """
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
    """
    # Populates a list of foreign keys used for advanced filtering
    # ------------------------------------------------------------------
    foreign_keys={}
    
    foreign_keys.update({'Pla_Id':(platform,'platform','Pla_Id','Pla_Name','Platform Id')})
    foreign_keys.update({'CC_Id':(cost_center,'cost_center','CC_Id','CC_Description','Cost Center Id')})
    foreign_keys.update({'Cus_Id':(customer,'customer','Cus_Id','Cus_Name','Customer Id')})
    # ------------------------------------------------------------------
    field=None
    if field is not None:
        reset_query_options(    engine=db.engine,Interface=Interface,
                                User_Id=current_user.id,
                                Table_name='configuration_item'
                                )

        
        if field in foreign_keys.keys():
            Class,klass,Field,Value,Header=foreign_keys[field]
            print('Class=',Class,'klass=',klass,'Field=',Field,'Value=',Value)
            field='%s.%s:%s'%(klass,Value,Header)
            print('Class=',Class,'klass=',klass,'Field=',Field,'Value=',Value)
            record=Class.query.get(value)
            print("record=",record,type(record))
            value="'%s'"%getattr(record,Value)
            print("value=",value)
        print("Setting filter to:",field,"==",value)
        set_query_option(   engine=db.engine,Interface=Interface,
                        User_Id=current_user.id,
                        Table_name='configuration_item',
                        Option_Type=OPTION_FILTER,
                        Argument_1=field,
                        Argument_2='==',
                        Argument_3=value
                        )
    """
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
    """
    
    # Build default query all fields from table
    """
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
            Class,klass,Field,Value,Header=foreign_keys['Pla_Id']
            field='%s.%s:%s'%(klass,Value,Header)            
            set_query_option(   engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='configuration_item',
                Option_Type=OPTION_FILTER,
                Argument_1=field,
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%Pla_Id
                )
    
    
    if CC_Id is not None and len(CC_Id)>0:
            Class,klass,Field,Value,Header=foreign_keys['CC_Id']
            field='%s.%s:%s'%(klass,Value,Header)            
            set_query_option(   engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='configuration_item',
                Option_Type=OPTION_FILTER,
                Argument_1=field,
                Argument_2='LIKE',
                Argument_3='\"%%%s%%\"'%CC_Id
                )
    
    
    if Cus_Id is not None and len(Cus_Id)>0:
            Class,klass,Field,Value,Header=foreign_keys['Cus_Id']
            field='%s.%s:%s'%(klass,Value,Header)            
            set_query_option(   engine=db.engine,Interface=Interface,
                User_Id=current_user.id,
                Table_name='configuration_item',
                Option_Type=OPTION_FILTER,
                Argument_1=field,
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
    """
    query=session.query(configuration_item)
    query = query.join(platform,configuration_item.Pla_Id == platform.Pla_Id).add_columns(platform.Pla_Name).join(cost_center,configuration_item.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description).join(customer,configuration_item.Cus_Id == customer.Cus_Id).add_columns(customer.Cus_Name)
    
    # Actual request from DB follows
    rows = query.paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
    print("rows type =",type(rows))
    print("rows dir  =",dor(rows))
    return
    # Setting pagination variables ...
    if field is not None:
       next_url = url_for('.select_Configuration_Items_query', field=field, value=value, page=rows.next_num) if rows.has_next else None
       prev_url = url_for('.select_Configuration_Items_query', field=field, value=value, page=rows.prev_num) if rows.has_prev else None
    else:
       next_url = url_for('.select_Configuration_Items_query', page=rows.next_num) if rows.has_next else None
       prev_url = url_for('.select_Configuration_Items_query', page=rows.prev_num) if rows.has_prev else None
    # Actual rendering ...
    if "JSON" in request.headers.get('Content-Type') or request.args.get('JSON',None,type=str) is not None:
        rows = query.all()
        print("typ rows=",type(rows))
        print("len rows=",len(rows))
        logger.debug('select_Configuration_Items_query(): will JSONnify rows ...')
        logger.debug('select_Configuration_Items_query(): Exit')
        Rows=[]
        for row in rows:
            print("type row=",type(row))
            print("     row=",row)
            Columns=[]
            for column in row:
                Columns.append(serialize_object(column))
            Rows.append(Columns)
        pprint(Rows)
        return json.dumps(Rows)
    else:
        logger.debug('select_Configuration_Items_query(): will render: configuration_items_All.html')
        logger.debug('select_Configuration_Items_query(): Exit')
        return render_template('configuration_items_select_All.html',rows=rows,options=options)
#===============================================================================
   
if __name__ == '__main__':
    #from flask import Flask, request
    #app = Flask(__name__)
    #request = Request() 
    select_Configuration_Items_query()
