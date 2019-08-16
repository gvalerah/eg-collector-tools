# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-10-31 18:36:07
# =============================================================================
from db.Measure_Units import Measure_Units,frm_Measure_Units

@app.route('/forms/Measure_Units/<MU_Code>', methods=['GET', 'POST'])
def forms_Measure_Units(MU_Code):
    logger.debug('Enter: forms_Measure_Units(%s,)'%(MU_Code))
    measure_units =  Measure_Units( None, None)
    measure_units.engine =  C.db
    row =  measure_units.queryone(MU_Code)
    if row is not None:
        session['data'] =  { 'MU_Code':row.MU_Code, 'MU_Description':row.MU_Description}
    else:
        session['data'] =  { 'MU_Code':None, 'MU_Description':None}
    form = frm_Measure_Units()

    form.engine = C.db

    if form.has_FKs:
        form.set_FK_list()

        Session=sessionmaker(bind=C.db)
        sess=Session()

    if form.validate_on_submit():
        session['data']['MU_Code'] = form.MU_Code.data
        session['data']['MU_Description'] = form.MU_Description.data
        return redirect(url_for('forms_Measure_Units',MU_Code=session['data']['MU_Code']))

    form.MU_Code.data = session['data']['MU_Code']
    form.MU_Description.data = session['data']['MU_Description']

    return render_template('Measure_Units.html',C=C, form=form, data=session.get('data'),row=row)

@app.route('/select/Measure_Units', methods=['GET'])
def select_Measure_Units():
    logger.debug('Enter: select_Measure_Units()')
    measure_units =  Measure_Units( None, None)
    measure_units.engine =  C.db
    result =  measure_units.queryall()
    rows = []
    for r in result:
	    row = object_as_dict(r)
	    rows.append(row)
    return render_template('Measure_Units_All.html',C=C,rows=rows)
# =============================================================================
