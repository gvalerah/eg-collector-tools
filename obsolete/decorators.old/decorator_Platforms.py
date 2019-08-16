# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-10-31 18:36:07
# =============================================================================
from db.Platforms import Platforms,frm_Platforms

@app.route('/forms/Platforms/<Pla_Id>', methods=['GET', 'POST'])
def forms_Platforms(Pla_Id):
    logger.debug('Enter: forms_Platforms(%s,)'%(Pla_Id))
    platforms =  Platforms( None, None, None, None, None, None)
    platforms.engine =  C.db
    row =  platforms.queryone(Pla_Id)
    if row is not None:
        session['data'] =  { 'Pla_Id':row.Pla_Id, 'Pla_Name':row.Pla_Name, 'Pla_Host':row.Pla_Host, 'Pla_Port':row.Pla_Port, 'Pla_User':row.Pla_User, 'Pla_Password':row.Pla_Password}
    else:
        session['data'] =  { 'Pla_Id':None, 'Pla_Name':None, 'Pla_Host':None, 'Pla_Port':None, 'Pla_User':None, 'Pla_Password':None}
    form = frm_Platforms()

    form.engine = C.db

    if form.has_FKs:
        form.set_FK_list()

        Session=sessionmaker(bind=C.db)
        sess=Session()

    if form.validate_on_submit():
        session['data']['Pla_Id'] = form.Pla_Id.data
        session['data']['Pla_Name'] = form.Pla_Name.data
        session['data']['Pla_Host'] = form.Pla_Host.data
        session['data']['Pla_Port'] = form.Pla_Port.data
        session['data']['Pla_User'] = form.Pla_User.data
        session['data']['Pla_Password'] = form.Pla_Password.data
        return redirect(url_for('forms_Platforms',Pla_Id=session['data']['Pla_Id']))

    form.Pla_Id.data = session['data']['Pla_Id']
    form.Pla_Name.data = session['data']['Pla_Name']
    form.Pla_Host.data = session['data']['Pla_Host']
    form.Pla_Port.data = session['data']['Pla_Port']
    form.Pla_User.data = session['data']['Pla_User']
    form.Pla_Password.data = session['data']['Pla_Password']

    return render_template('Platforms.html',C=C, form=form, data=session.get('data'),row=row)

@app.route('/select/Platforms', methods=['GET'])
def select_Platforms():
    logger.debug('Enter: select_Platforms()')
    platforms =  Platforms( None, None, None, None, None, None)
    platforms.engine =  C.db
    result =  platforms.queryall()
    rows = []
    for r in result:
	    row = object_as_dict(r)
	    rows.append(row)
    return render_template('Platforms_All.html',C=C,rows=rows)
# =============================================================================
