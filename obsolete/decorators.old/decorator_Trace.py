# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-10-31 18:36:07
# =============================================================================
from db.Trace import Trace,frm_Trace

@app.route('/forms/Trace/<ID>', methods=['GET', 'POST'])
def forms_Trace(ID):
    logger.debug('Enter: forms_Trace(%s,)'%(ID))
    trace =  Trace( None, None)
    trace.engine =  C.db
    row =  trace.queryone(ID)
    if row is not None:
        session['data'] =  { 'ID':row.ID, 'LINE':row.LINE}
    else:
        session['data'] =  { 'ID':None, 'LINE':None}
    form = frm_Trace()

    form.engine = C.db

    if form.has_FKs:
        form.set_FK_list()

        Session=sessionmaker(bind=C.db)
        sess=Session()

    if form.validate_on_submit():
        session['data']['ID'] = form.ID.data
        session['data']['LINE'] = form.LINE.data
        return redirect(url_for('forms_Trace',ID=session['data']['ID']))

    form.ID.data = session['data']['ID']
    form.LINE.data = session['data']['LINE']

    return render_template('Trace.html',C=C, form=form, data=session.get('data'),row=row)

@app.route('/select/Trace', methods=['GET'])
def select_Trace():
    logger.debug('Enter: select_Trace()')
    trace =  Trace( None, None)
    trace.engine =  C.db
    result =  trace.queryall()
    rows = []
    for r in result:
	    row = object_as_dict(r)
	    rows.append(row)
    return render_template('Trace_All.html',C=C,rows=rows)
# =============================================================================
