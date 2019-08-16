# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-10-31 18:36:07
# =============================================================================
from db.Countries_Currencies import Countries_Currencies,frm_Countries_Currencies

@app.route('/forms/Countries_Currencies/<Cou_Code>&<Cur_Code>', methods=['GET', 'POST'])
def forms_Countries_Currencies(Cou_Code,Cur_Code):
    logger.debug('Enter: forms_Countries_Currencies(%s,%s,)'%(Cou_Code,Cur_Code))
    countries_currencies =  Countries_Currencies( None, None, None)
    countries_currencies.engine =  C.db
    row =  countries_currencies.queryone(Cou_Code,Cur_Code)
    if row is not None:
        session['data'] =  { 'Cou_Code':row.Cou_Code, 'Cur_Code':row.Cur_Code, 'Cou_Cur_Comment':row.Cou_Cur_Comment}
    else:
        session['data'] =  { 'Cou_Code':None, 'Cur_Code':None, 'Cou_Cur_Comment':None}
    form = frm_Countries_Currencies()

    form.engine = C.db

    if form.has_FKs:
        form.set_FK_list()

        Session=sessionmaker(bind=C.db)
        sess=Session()
        form.FK_List['Cou_Code']['Value'] = sess.query(Countries.Cou_Name).filter(Countries.Cou_Code == session['data']['Cou_Code']).first()
        form.FK_List['Cur_Code']['Value'] = sess.query(Currencies.Cur_Name).filter(Currencies.Cur_Code == session['data']['Cur_Code']).first()

    if form.validate_on_submit():
        session['data']['Cou_Code'] = form.Cou_Code.data
        session['data']['Cur_Code'] = form.Cur_Code.data
        session['data']['Cou_Cur_Comment'] = form.Cou_Cur_Comment.data
        return redirect(url_for('forms_Countries_Currencies',Cou_Code=session['data']['Cou_Code'],Cur_Code=session['data']['Cur_Code']))

    form.Cou_Code.data = session['data']['Cou_Code']
    form.Cur_Code.data = session['data']['Cur_Code']
    form.Cou_Cur_Comment.data = session['data']['Cou_Cur_Comment']

    return render_template('Countries_Currencies.html',C=C, form=form, data=session.get('data'),row=row)

@app.route('/select/Countries_Currencies', methods=['GET'])
def select_Countries_Currencies():
    logger.debug('Enter: select_Countries_Currencies()')
    countries_currencies =  Countries_Currencies( None, None, None)
    countries_currencies.engine =  C.db
    result =  countries_currencies.queryall()
    rows = []
    for r in result:
	    row = object_as_dict(r)
	    rows.append(row)
    return render_template('Countries_Currencies_All.html',C=C,rows=rows)
# =============================================================================
