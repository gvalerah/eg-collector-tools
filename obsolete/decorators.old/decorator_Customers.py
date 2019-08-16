# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-10-31 18:36:07
# =============================================================================
from db.Customers import Customers,frm_Customers

@app.route('/forms/Customers/<Cus_Id>', methods=['GET', 'POST'])
def forms_Customers(Cus_Id):
    logger.debug('Enter: forms_Customers(%s,)'%(Cus_Id))
    customers =  Customers( None, None, None)
    customers.engine =  C.db
    row =  customers.queryone(Cus_Id)
    if row is not None:
        session['data'] =  { 'Cus_Id':row.Cus_Id, 'Cus_Name':row.Cus_Name, 'CC_Id':row.CC_Id}
    else:
        session['data'] =  { 'Cus_Id':None, 'Cus_Name':None, 'CC_Id':None}
    form = frm_Customers()

    form.engine = C.db

    if form.has_FKs:
        form.set_FK_list()

        Session=sessionmaker(bind=C.db)
        sess=Session()
        form.FK_List['CC_Id']['Value'] = sess.query(Cost_Centers.CC_Description).filter(Cost_Centers.CC_Id == session['data']['CC_Id']).first()

    if form.validate_on_submit():
        session['data']['Cus_Id'] = form.Cus_Id.data
        session['data']['Cus_Name'] = form.Cus_Name.data
        session['data']['CC_Id'] = form.CC_Id.data
        return redirect(url_for('forms_Customers',Cus_Id=session['data']['Cus_Id']))

    form.Cus_Id.data = session['data']['Cus_Id']
    form.Cus_Name.data = session['data']['Cus_Name']
    form.CC_Id.data = session['data']['CC_Id']

    return render_template('Customers.html',C=C, form=form, data=session.get('data'),row=row)

@app.route('/select/Customers', methods=['GET'])
def select_Customers():
    logger.debug('Enter: select_Customers()')
    customers =  Customers( None, None, None)
    customers.engine =  C.db
    result =  customers.queryall()
    rows = []
    for r in result:
	    row = object_as_dict(r)
	    rows.append(row)
    return render_template('Customers_All.html',C=C,rows=rows)
# =============================================================================
