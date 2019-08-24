# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-11-13 10:26:02
# =============================================================================
from db.Forms import Forms,frm_Forms

@app.route('/forms/Forms/<Id>', methods=['GET', 'POST'])
def forms_Forms(Id):
    logger.debug('Enter: forms_Forms(%s,)'%(Id))
    forms =  Forms( None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None)
    forms.engine =  C.db
    row =  forms.queryone(Id)
    if row is not None:
        session['data'] =  { 'Id':row.Id, 'Table':row.Table, 'Field':row.Field, 'Type':row.Type, 'Null':row.Null, 'Key':row.Key, 'Default':row.Default, 'Extra':row.Extra, 'Foreign_Key':row.Foreign_Key, 'Referenced_Table':row.Referenced_Table, 'Foreign_Field':row.Foreign_Field, 'Length':row.Length, 'Validation':row.Validation, 'Validation_Type':row.Validation_Type, 'Validation_String':row.Validation_String, 'Caption_String':row.Caption_String}
    else:
        session['data'] =  { 'Id':None, 'Table':None, 'Field':None, 'Type':None, 'Null':None, 'Key':None, 'Default':None, 'Extra':None, 'Foreign_Key':None, 'Referenced_Table':None, 'Foreign_Field':None, 'Length':None, 'Validation':None, 'Validation_Type':None, 'Validation_String':None, 'Caption_String':None}
    form = frm_Forms()

    form.engine = C.db

    if form.has_FKs:
        form.set_FK_list()

        Session=sessionmaker(bind=C.db)
        sess=Session()

    if form.validate_on_submit():
        session['data']['Id'] = form.Id.data
        session['data']['Table'] = form.Table.data
        session['data']['Field'] = form.Field.data
        session['data']['Type'] = form.Type.data
        session['data']['Null'] = form.Null.data
        session['data']['Key'] = form.Key.data
        session['data']['Default'] = form.Default.data
        session['data']['Extra'] = form.Extra.data
        session['data']['Foreign_Key'] = form.Foreign_Key.data
        session['data']['Referenced_Table'] = form.Referenced_Table.data
        session['data']['Foreign_Field'] = form.Foreign_Field.data
        session['data']['Length'] = form.Length.data
        session['data']['Validation'] = form.Validation.data
        session['data']['Validation_Type'] = form.Validation_Type.data
        session['data']['Validation_String'] = form.Validation_String.data
        session['data']['Caption_String'] = form.Caption_String.data
        return redirect(url_for('forms_Forms',Id=session['data']['Id']))

    form.Id.data = session['data']['Id']
    form.Table.data = session['data']['Table']
    form.Field.data = session['data']['Field']
    form.Type.data = session['data']['Type']
    form.Null.data = session['data']['Null']
    form.Key.data = session['data']['Key']
    form.Default.data = session['data']['Default']
    form.Extra.data = session['data']['Extra']
    form.Foreign_Key.data = session['data']['Foreign_Key']
    form.Referenced_Table.data = session['data']['Referenced_Table']
    form.Foreign_Field.data = session['data']['Foreign_Field']
    form.Length.data = session['data']['Length']
    form.Validation.data = session['data']['Validation']
    form.Validation_Type.data = session['data']['Validation_Type']
    form.Validation_String.data = session['data']['Validation_String']
    form.Caption_String.data = session['data']['Caption_String']

    return render_template('Forms.html',C=C, form=form, data=session.get('data'),row=row)

@app.route('/select/Forms', methods=['GET'])
def select_Forms():
    logger.debug('Enter: select_Forms()')
    forms =  Forms( None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None)
    forms.engine =  C.db
    result =  forms.queryall()
    rows = []
    for r in result:
	    row = object_as_dict(r)
	    rows.append(row)
    return render_template('Forms_All.html',C=C,rows=rows)
# =============================================================================
