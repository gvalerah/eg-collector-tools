# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-10-31 18:36:07
# =============================================================================
from db.Lists import Lists,frm_Lists

@app.route('/forms/Lists/<Type>&<Value>&<Caption>', methods=['GET', 'POST'])
def forms_Lists(Type,Value,Caption):
    logger.debug('Enter: forms_Lists(%s,%s,%s,)'%(Type,Value,Caption))
    lists =  Lists( None, None, None)
    lists.engine =  C.db
    row =  lists.queryone(Type,Value,Caption)
    if row is not None:
        session['data'] =  { 'Type':row.Type, 'Value':row.Value, 'Caption':row.Caption}
    else:
        session['data'] =  { 'Type':None, 'Value':None, 'Caption':None}
    form = frm_Lists()

    form.engine = C.db

    if form.has_FKs:
        form.set_FK_list()

        Session=sessionmaker(bind=C.db)
        sess=Session()

    if form.validate_on_submit():
        session['data']['Type'] = form.Type.data
        session['data']['Value'] = form.Value.data
        session['data']['Caption'] = form.Caption.data
        return redirect(url_for('forms_Lists',Type=session['data']['Type'],Value=session['data']['Value'],Caption=session['data']['Caption']))

    form.Type.data = session['data']['Type']
    form.Value.data = session['data']['Value']
    form.Caption.data = session['data']['Caption']

    return render_template('Lists.html',C=C, form=form, data=session.get('data'),row=row)

@app.route('/select/Lists', methods=['GET'])
def select_Lists():
    logger.debug('Enter: select_Lists()')
    lists =  Lists( None, None, None)
    lists.engine =  C.db
    result =  lists.queryall()
    rows = []
    for r in result:
	    row = object_as_dict(r)
	    rows.append(row)
    return render_template('Lists_All.html',C=C,rows=rows)
# =============================================================================
