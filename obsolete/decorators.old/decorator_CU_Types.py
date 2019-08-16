# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-10-31 18:36:07
# =============================================================================
from db.CU_Types import CU_Types,frm_CU_Types

@app.route('/forms/CU_Types/<Typ_Code>', methods=['GET', 'POST'])
def forms_CU_Types(Typ_Code):
    logger.debug('Enter: forms_CU_Types(%s,)'%(Typ_Code))
    cu_types =  CU_Types( None, None)
    cu_types.engine =  C.db
    row =  cu_types.queryone(Typ_Code)
    if row is not None:
        session['data'] =  { 'Typ_Code':row.Typ_Code, 'Typ_Description':row.Typ_Description}
    else:
        session['data'] =  { 'Typ_Code':None, 'Typ_Description':None}
    form = frm_CU_Types()

    form.engine = C.db

    if form.has_FKs:
        form.set_FK_list()

        Session=sessionmaker(bind=C.db)
        sess=Session()

    if form.validate_on_submit():
        session['data']['Typ_Code'] = form.Typ_Code.data
        session['data']['Typ_Description'] = form.Typ_Description.data
        return redirect(url_for('forms_CU_Types',Typ_Code=session['data']['Typ_Code']))

    form.Typ_Code.data = session['data']['Typ_Code']
    form.Typ_Description.data = session['data']['Typ_Description']

    return render_template('CU_Types.html',C=C, form=form, data=session.get('data'),row=row)

@app.route('/select/CU_Types', methods=['GET'])
def select_CU_Types():
    logger.debug('Enter: select_CU_Types()')
    cu_types =  CU_Types( None, None)
    cu_types.engine =  C.db
    result =  cu_types.queryall()
    rows = []
    for r in result:
	    row = object_as_dict(r)
	    rows.append(row)
    return render_template('CU_Types_All.html',C=C,rows=rows)
# =============================================================================
