# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-11-13 10:26:02
# =============================================================================
from db.Tables import Tables,frm_Tables

@app.route('/forms/Tables/<Id>', methods=['GET', 'POST'])
def forms_Tables(Id):
    logger.debug('Enter: forms_Tables(%s,)'%(Id))
    tables =  Tables( None, None, None, None, None, None, None, None, None, None, None, None)
    tables.engine =  C.db
    row =  tables.queryone(Id)
    if row is not None:
        session['data'] =  { 'Id':row.Id, 'Name':row.Name, 'Caption':row.Caption, 'Entity':row.Entity, 'Class_Name':row.Class_Name, 'Child_Table':row.Child_Table, 'Use_Pagination':row.Use_Pagination, 'Use_Children_Pagination':row.Use_Children_Pagination, 'Generate_Form_One':row.Generate_Form_One, 'Generate_Form_All':row.Generate_Form_All, 'Generate_Form_Filter':row.Generate_Form_Filter, 'Generate_Children':row.Generate_Children}
    else:
        session['data'] =  { 'Id':None, 'Name':None, 'Caption':None, 'Entity':None, 'Class_Name':None, 'Child_Table':None, 'Use_Pagination':None, 'Use_Children_Pagination':None, 'Generate_Form_One':None, 'Generate_Form_All':None, 'Generate_Form_Filter':None, 'Generate_Children':None}
    form = frm_Tables()

    form.engine = C.db

    if form.has_FKs:
        form.set_FK_list()

        Session=sessionmaker(bind=C.db)
        sess=Session()

    if form.validate_on_submit():
        session['data']['Id'] = form.Id.data
        session['data']['Name'] = form.Name.data
        session['data']['Caption'] = form.Caption.data
        session['data']['Entity'] = form.Entity.data
        session['data']['Class_Name'] = form.Class_Name.data
        session['data']['Child_Table'] = form.Child_Table.data
        session['data']['Use_Pagination'] = form.Use_Pagination.data
        session['data']['Use_Children_Pagination'] = form.Use_Children_Pagination.data
        session['data']['Generate_Form_One'] = form.Generate_Form_One.data
        session['data']['Generate_Form_All'] = form.Generate_Form_All.data
        session['data']['Generate_Form_Filter'] = form.Generate_Form_Filter.data
        session['data']['Generate_Children'] = form.Generate_Children.data
        return redirect(url_for('forms_Tables',Id=session['data']['Id']))

    form.Id.data = session['data']['Id']
    form.Name.data = session['data']['Name']
    form.Caption.data = session['data']['Caption']
    form.Entity.data = session['data']['Entity']
    form.Class_Name.data = session['data']['Class_Name']
    form.Child_Table.data = session['data']['Child_Table']
    form.Use_Pagination.data = session['data']['Use_Pagination']
    form.Use_Children_Pagination.data = session['data']['Use_Children_Pagination']
    form.Generate_Form_One.data = session['data']['Generate_Form_One']
    form.Generate_Form_All.data = session['data']['Generate_Form_All']
    form.Generate_Form_Filter.data = session['data']['Generate_Form_Filter']
    form.Generate_Children.data = session['data']['Generate_Children']

    return render_template('Tables.html',C=C, form=form, data=session.get('data'),row=row)

@app.route('/select/Tables', methods=['GET'])
def select_Tables():
    logger.debug('Enter: select_Tables()')
    tables =  Tables( None, None, None, None, None, None, None, None, None, None, None, None)
    tables.engine =  C.db
    result =  tables.queryall()
    rows = []
    for r in result:
	    row = object_as_dict(r)
	    rows.append(row)
    return render_template('Tables_All.html',C=C,rows=rows)
# =============================================================================
