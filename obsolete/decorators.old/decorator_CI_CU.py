# GV 20181030 --- in
#from db.CI_CU import frm_CI_CU
from db.Charge_Units import Charge_Units,frm_Charge_Units
# GV 20181030 --- out


# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-10-30 17:07:27
# =============================================================================
from db.Configuration_Items import Configuration_Items,frm_Configuration_Items

#@app.route('/forms/Configuration_Items/<CI_Id>', methods=['GET', 'POST'])
#def forms_Configuration_Items(CI_Id):
@app.route('/forms/CI_CU/<CI_Id>', methods=['GET', 'POST'])
def forms_CI_CU(CI_Id):
    logger.debug('Enter: forms_Configuration_Items(%s,)'%(CI_Id))
    configuration_items =  Configuration_Items( None, None, None, None, None, None, None)
    configuration_items.engine =  C.db
    row =  configuration_items.queryone(CI_Id)
    if row is not None:
        session['data'] =  { 'CI_Id':row.CI_Id, 'CI_Name':row.CI_Name, 'CI_UUID':row.CI_UUID, 'Pla_Id':row.Pla_Id, 'CC_Id':row.CC_Id, 'CI_CIT_Generation':row.CI_CIT_Generation, 'Cus_Id':row.Cus_Id}
    else:
        session['data'] =  { 'CI_Id':None, 'CI_Name':None, 'CI_UUID':None, 'Pla_Id':None, 'CC_Id':None, 'CI_CIT_Generation':None, 'Cus_Id':None}
    form = frm_Configuration_Items()

    form.engine = C.db

    if form.has_FKs:
        form.set_FK_list()
        Session=sessionmaker(bind=C.db)
        sess=Session()
        form.FK_List['Pla_Id']['Value'] = sess.query(Platforms.Pla_Name).filter(Platforms.Pla_Id == session['data']['Pla_Id']).first()
        form.FK_List['CC_Id']['Value'] = sess.query(Cost_Centers.CC_Description).filter(Cost_Centers.CC_Id == session['data']['CC_Id']).first()
        form.FK_List['Cus_Id']['Value'] = sess.query(Customers.Cus_Name).filter(Customers.Cus_Id == session['data']['Cus_Id']).first()
        
    print("form.CI_CIT_Generation >>>>",form.CI_CIT_Generation,"<<<")
    if form.validate_on_submit():
        session['data']['CI_Id'] = form.CI_Id.data
        session['data']['CI_Name'] = form.CI_Name.data
        session['data']['CI_UUID'] = form.CI_UUID.data
        session['data']['Pla_Id'] = form.Pla_Id.data
        session['data']['CC_Id'] = form.CC_Id.data
        session['data']['CI_CIT_Generation'] = form.CI_CIT_Generation.data
        session['data']['Cus_Id'] = form.Cus_Id.data
        # GV 20181030
        #session['data']['CU'] = form.CU
        return redirect(url_for('forms_CI_CU',CI_Id=session['data']['CI_Id']))

    # GV 20181030 ---- from
    charge_units =  Charge_Units( None, None, None, None, None, None, None, None, None, None)
    charge_units.engine =  C.db
    result = sess.query(Charge_Units).filter(Charge_Units.CI_Id == session['data']['CI_Id']).all()
    rows = []
    for r in result:
        cu_row = object_as_dict(r)
        rows.append(cu_row)
    session['data']['CU'] =  rows
    # GV 20181030 ---- to

    form.CI_Id.data = session['data']['CI_Id']
    form.CI_Name.data = session['data']['CI_Name']
    form.CI_UUID.data = session['data']['CI_UUID']
    form.Pla_Id.data = session['data']['Pla_Id']
    form.CC_Id.data = session['data']['CC_Id']
    form.CI_CIT_Generation.data = session['data']['CI_CIT_Generation']
    form.Cus_Id.data = session['data']['Cus_Id']
    # GV 20181020
    #form.CU = session['data']['CU']

    return render_template('CI_CU.html',C=C, form=form, data=session.get('data'),row=row,rows=rows)

