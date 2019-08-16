# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-10-31 18:36:07
# =============================================================================
from db.Cost_Centers import Cost_Centers,frm_Cost_Centers

@app.route('/forms/Cost_Centers/<CC_Id>', methods=['GET', 'POST'])
def forms_Cost_Centers(CC_Id):
    logger.debug('Enter: forms_Cost_Centers(%s,)'%(CC_Id))
    cost_centers =  Cost_Centers( None, None, None, None)
    cost_centers.engine =  C.db
    row =  cost_centers.queryone(CC_Id)
    if row is not None:
        session['data'] =  { 'CC_Id':row.CC_Id, 'CC_Code':row.CC_Code, 'CC_Description':row.CC_Description, 'Cur_Code':row.Cur_Code}
    else:
        session['data'] =  { 'CC_Id':None, 'CC_Code':None, 'CC_Description':None, 'Cur_Code':None}
    form = frm_Cost_Centers()

    form.engine = C.db

    if form.has_FKs:
        form.set_FK_list()

        Session=sessionmaker(bind=C.db)
        sess=Session()
        form.FK_List['Cur_Code']['Value'] = sess.query(Currencies.Cur_Name).filter(Currencies.Cur_Code == session['data']['Cur_Code']).first()

    if form.validate_on_submit():
        session['data']['CC_Id'] = form.CC_Id.data
        session['data']['CC_Code'] = form.CC_Code.data
        session['data']['CC_Description'] = form.CC_Description.data
        session['data']['Cur_Code'] = form.Cur_Code.data
        return redirect(url_for('forms_Cost_Centers',CC_Id=session['data']['CC_Id']))

    form.CC_Id.data = session['data']['CC_Id']
    form.CC_Code.data = session['data']['CC_Code']
    form.CC_Description.data = session['data']['CC_Description']
    form.Cur_Code.data = session['data']['Cur_Code']

    return render_template('Cost_Centers.html',C=C, form=form, data=session.get('data'),row=row)

@app.route('/select/Cost_Centers', methods=['GET'])
def select_Cost_Centers():
    logger.debug('Enter: select_Cost_Centers()')
    cost_centers =  Cost_Centers( None, None, None, None)
    cost_centers.engine =  C.db
    result =  cost_centers.queryall()
    rows = []
    for r in result:
	    row = object_as_dict(r)
	    rows.append(row)
    return render_template('Cost_Centers_All.html',C=C,rows=rows)
# =============================================================================
