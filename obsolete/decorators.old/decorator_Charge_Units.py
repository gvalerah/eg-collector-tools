# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-10-31 18:36:07
# =============================================================================
from db.Charge_Units import Charge_Units,frm_Charge_Units

@app.route('/forms/Charge_Units/<CU_Id>', methods=['GET', 'POST'])
def forms_Charge_Units(CU_Id):
    logger.debug('Enter: forms_Charge_Units(%s,)'%(CU_Id))
    charge_units =  Charge_Units( None, None, None, None, None, None, None, None, None, None)
    charge_units.engine =  C.db
    row =  charge_units.queryone(CU_Id)
    if row is not None:
        session['data'] =  { 'CU_Id':row.CU_Id, 'CI_Id':row.CI_Id, 'CU_Description':row.CU_Description, 'CU_UUID':row.CU_UUID, 'CU_Is_Billeable':row.CU_Is_Billeable, 'CU_Is_Always_Billeable':row.CU_Is_Always_Billeable, 'CU_Quantity':row.CU_Quantity, 'CU_Operation':row.CU_Operation, 'Typ_Code':row.Typ_Code, 'CC_Id':row.CC_Id}
    else:
        session['data'] =  { 'CU_Id':None, 'CI_Id':None, 'CU_Description':None, 'CU_UUID':None, 'CU_Is_Billeable':None, 'CU_Is_Always_Billeable':None, 'CU_Quantity':None, 'CU_Operation':None, 'Typ_Code':None, 'CC_Id':None}
    form = frm_Charge_Units()

    form.engine = C.db

    if form.has_FKs:
        form.set_FK_list()

        Session=sessionmaker(bind=C.db)
        sess=Session()
        form.FK_List['CI_Id']['Value'] = sess.query(Configuration_Items.CI_Name).filter(Configuration_Items.CI_Id == session['data']['CI_Id']).first()
        form.FK_List['Typ_Code']['Value'] = sess.query(CU_Types.Typ_Description).filter(CU_Types.Typ_Code == session['data']['Typ_Code']).first()
        form.FK_List['CC_Id']['Value'] = sess.query(Cost_Centers.CC_Description).filter(Cost_Centers.CC_Id == session['data']['CC_Id']).first()

    form.CU_Operation.choices           = [("None","No Conversion"),("BTOKB","Bytes to KB"),("BTOMB","Bytes to MB"),("BTOGB","Bytes to GB"),("KBTOB","KB to Bytes"),("KBTOMB","KB to MB"),("KBTOGB","KB to GB"),("MBTOB","MB to Bytes"),("MBTOKB","MB to KB"),("MBTOGB","MB to GB"),("GBTOB","GB to Bytes"),("GBTOKB","GB to KB"),("GBTOMB","GB to MB"),("HTOD","Hours to Days"),("HTOM","Hours to Months"),("DTOH","Days to Hours"),("DTOM","Days to Months"),("MTOH","Months to Hours"),("MTOD","Months to Days"),]
    if form.validate_on_submit():
        session['data']['CU_Id'] = form.CU_Id.data
        session['data']['CI_Id'] = form.CI_Id.data
        session['data']['CU_Description'] = form.CU_Description.data
        session['data']['CU_UUID'] = form.CU_UUID.data
        session['data']['CU_Is_Billeable'] = form.CU_Is_Billeable.data
        session['data']['CU_Is_Always_Billeable'] = form.CU_Is_Always_Billeable.data
        session['data']['CU_Quantity'] = form.CU_Quantity.data
        session['data']['CU_Operation'] = form.CU_Operation.data
        session['data']['Typ_Code'] = form.Typ_Code.data
        session['data']['CC_Id'] = form.CC_Id.data
        return redirect(url_for('forms_Charge_Units',CU_Id=session['data']['CU_Id']))

    form.CU_Id.data = session['data']['CU_Id']
    form.CI_Id.data = session['data']['CI_Id']
    form.CU_Description.data = session['data']['CU_Description']
    form.CU_UUID.data = session['data']['CU_UUID']
    form.CU_Is_Billeable.data = session['data']['CU_Is_Billeable']
    form.CU_Is_Always_Billeable.data = session['data']['CU_Is_Always_Billeable']
    form.CU_Quantity.data = session['data']['CU_Quantity']
    form.CU_Operation.data = session['data']['CU_Operation']
    form.Typ_Code.data = session['data']['Typ_Code']
    form.CC_Id.data = session['data']['CC_Id']

    return render_template('Charge_Units.html',C=C, form=form, data=session.get('data'),row=row)

@app.route('/select/Charge_Units', methods=['GET'])
def select_Charge_Units():
    logger.debug('Enter: select_Charge_Units()')
    charge_units =  Charge_Units( None, None, None, None, None, None, None, None, None, None)
    charge_units.engine =  C.db
    result =  charge_units.queryall()
    rows = []
    for r in result:
	    row = object_as_dict(r)
	    rows.append(row)
    return render_template('Charge_Units_All.html',C=C,rows=rows)
# =============================================================================
