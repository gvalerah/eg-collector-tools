# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-10-31 18:36:07
# =============================================================================
from db.Currencies import Currencies,frm_Currencies

@app.route('/forms/Currencies/<Cur_Code>', methods=['GET', 'POST'])
def forms_Currencies(Cur_Code):
    logger.debug('Enter: forms_Currencies(%s,)'%(Cur_Code))
    currencies =  Currencies( None, None, None, None)
    currencies.engine =  C.db
    row =  currencies.queryone(Cur_Code)
    if row is not None:
        session['data'] =  { 'Cur_Code':row.Cur_Code, 'Cur_Name':row.Cur_Name, 'Cur_Id':row.Cur_Id, 'Cur_Comment':row.Cur_Comment}
    else:
        session['data'] =  { 'Cur_Code':None, 'Cur_Name':None, 'Cur_Id':None, 'Cur_Comment':None}
    form = frm_Currencies()

    form.engine = C.db

    if form.has_FKs:
        form.set_FK_list()

        Session=sessionmaker(bind=C.db)
        sess=Session()

    if form.validate_on_submit():
        session['data']['Cur_Code'] = form.Cur_Code.data
        session['data']['Cur_Name'] = form.Cur_Name.data
        session['data']['Cur_Id'] = form.Cur_Id.data
        session['data']['Cur_Comment'] = form.Cur_Comment.data
        return redirect(url_for('forms_Currencies',Cur_Code=session['data']['Cur_Code']))

    form.Cur_Code.data = session['data']['Cur_Code']
    form.Cur_Name.data = session['data']['Cur_Name']
    form.Cur_Id.data = session['data']['Cur_Id']
    form.Cur_Comment.data = session['data']['Cur_Comment']

    return render_template('Currencies.html',C=C, form=form, data=session.get('data'),row=row)

@app.route('/select/Currencies', methods=['GET'])
def select_Currencies():
    logger.debug('Enter: select_Currencies()')
    currencies =  Currencies( None, None, None, None)
    currencies.engine =  C.db
    result =  currencies.queryall()
    rows = []
    for r in result:
	    row = object_as_dict(r)
	    rows.append(row)
    return render_template('Currencies_All.html',C=C,rows=rows)
# =============================================================================
