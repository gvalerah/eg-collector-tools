# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-10-31 18:36:07
# =============================================================================
from db.Countries import Countries,frm_Countries

@app.route('/forms/Countries/<Cou_Code>', methods=['GET', 'POST'])
def forms_Countries(Cou_Code):
    logger.debug('Enter: forms_Countries(%s,)'%(Cou_Code))
    countries =  Countries( None, None, None, None)
    countries.engine =  C.db
    row =  countries.queryone(Cou_Code)
    if row is not None:
        session['data'] =  { 'Cou_Code':row.Cou_Code, 'Cou_Name':row.Cou_Name, 'Cou_A3':row.Cou_A3, 'Cou_N':row.Cou_N}
    else:
        session['data'] =  { 'Cou_Code':None, 'Cou_Name':None, 'Cou_A3':None, 'Cou_N':None}
    form = frm_Countries()

    form.engine = C.db

    if form.has_FKs:
        form.set_FK_list()

        Session=sessionmaker(bind=C.db)
        sess=Session()

    if form.validate_on_submit():
        session['data']['Cou_Code'] = form.Cou_Code.data
        session['data']['Cou_Name'] = form.Cou_Name.data
        session['data']['Cou_A3'] = form.Cou_A3.data
        session['data']['Cou_N'] = form.Cou_N.data
        return redirect(url_for('forms_Countries',Cou_Code=session['data']['Cou_Code']))

    form.Cou_Code.data = session['data']['Cou_Code']
    form.Cou_Name.data = session['data']['Cou_Name']
    form.Cou_A3.data = session['data']['Cou_A3']
    form.Cou_N.data = session['data']['Cou_N']

    return render_template('Countries.html',C=C, form=form, data=session.get('data'),row=row)

@app.route('/select/Countries', methods=['GET'])
def select_Countries():
    logger.debug('Enter: select_Countries()')
    countries =  Countries( None, None, None, None)
    countries.engine =  C.db
    result =  countries.queryall()
    rows = []
    for r in result:
	    row = object_as_dict(r)
	    rows.append(row)
    return render_template('Countries_All.html',C=C,rows=rows)
# =============================================================================
