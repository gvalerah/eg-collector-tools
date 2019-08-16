# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-10-31 18:36:07
# =============================================================================
from db.Charge_Items import Charge_Items,frm_Charge_Items

@app.route('/forms/Charge_Items/<CU_Id>&<CIT_Date>&<CIT_Time>', methods=['GET', 'POST'])
def forms_Charge_Items(CU_Id,CIT_Date,CIT_Time):
    logger.debug('Enter: forms_Charge_Items(%s,%s,%s,)'%(CU_Id,CIT_Date,CIT_Time))
    charge_items =  Charge_Items( None, None, None, None, None, None)
    charge_items.engine =  C.db
    row =  charge_items.queryone(CU_Id,CIT_Date,CIT_Time)
    if row is not None:
        session['data'] =  { 'CU_Id':row.CU_Id, 'CIT_Date':row.CIT_Date, 'CIT_Time':str(row.CIT_Time), 'CIT_Quantity':row.CIT_Quantity, 'CIT_Status':row.CIT_Status, 'CIT_Is_Active':row.CIT_Is_Active}
    else:
        session['data'] =  { 'CU_Id':None, 'CIT_Date':None, 'CIT_Time':None, 'CIT_Quantity':None, 'CIT_Status':None, 'CIT_Is_Active':None}
    form = frm_Charge_Items()

    form.engine = C.db

    if form.has_FKs:
        form.set_FK_list()

        Session=sessionmaker(bind=C.db)
        sess=Session()
        form.FK_List['CU_Id']['Value'] = sess.query(Charge_Units.CU_Description).filter(Charge_Units.CU_Id == session['data']['CU_Id']).first()

    form.CIT_Status.choices    = [(1,"Pending Approval"),(2,"Claimed"),(3,"Rejected"),(4,"Approved")]
    if form.validate_on_submit():
        session['data']['CU_Id'] = form.CU_Id.data
        session['data']['CIT_Date'] = form.CIT_Date.data
        session['data']['CIT_Time'] = form.CIT_Time.data
        session['data']['CIT_Quantity'] = form.CIT_Quantity.data
        session['data']['CIT_Status'] = form.CIT_Status.data
        session['data']['CIT_Is_Active'] = form.CIT_Is_Active.data
        return redirect(url_for('forms_Charge_Items',CU_Id=session['data']['CU_Id'],CIT_Date=session['data']['CIT_Date'],CIT_Time=session['data']['CIT_Time']))

    form.CU_Id.data = session['data']['CU_Id']
    form.CIT_Date.data = session['data']['CIT_Date']
    form.CIT_Time.data = session['data']['CIT_Time']
    form.CIT_Quantity.data = session['data']['CIT_Quantity']
    form.CIT_Status.data = session['data']['CIT_Status']
    form.CIT_Is_Active.data = session['data']['CIT_Is_Active']

    return render_template('Charge_Items.html',C=C, form=form, data=session.get('data'),row=row)

@app.route('/select/Charge_Items', methods=['GET'])
def select_Charge_Items():
    logger.debug('Enter: select_Charge_Items()')
    charge_items =  Charge_Items( None, None, None, None, None, None)
    charge_items.engine =  C.db
    result =  charge_items.queryall()
    rows = []
    for r in result:
	    row = object_as_dict(r)
	    rows.append(row)
    return render_template('Charge_Items_All.html',C=C,rows=rows)
# =============================================================================
