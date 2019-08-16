# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-10-31 18:36:07
# =============================================================================
from db.Rates import Rates,frm_Rates

@app.route('/forms/Rates/<Rat_Id>', methods=['GET', 'POST'])
def forms_Rates(Rat_Id):
    logger.debug('Enter: forms_Rates(%s,)'%(Rat_Id))
    rates =  Rates( None, None, None, None, None, None, None, None, None, None)
    rates.engine =  C.db
    row =  rates.queryone(Rat_Id)
    if row is not None:
        session['data'] =  { 'Rat_Id':row.Rat_Id, 'Cus_Id':row.Cus_Id, 'Pla_Id':row.Pla_Id, 'CC_Id':row.CC_Id, 'CU_Id':row.CU_Id, 'Rat_Price':row.Rat_Price, 'Rat_Period':row.Rat_Period, 'MU_Code':row.MU_Code, 'Typ_Code':row.Typ_Code, 'Cur_Code':row.Cur_Code}
    else:
        session['data'] =  { 'Rat_Id':None, 'Cus_Id':None, 'Pla_Id':None, 'CC_Id':None, 'CU_Id':None, 'Rat_Price':None, 'Rat_Period':None, 'MU_Code':None, 'Typ_Code':None, 'Cur_Code':None}
    form = frm_Rates()

    form.engine = C.db

    if form.has_FKs:
        form.set_FK_list()

        Session=sessionmaker(bind=C.db)
        sess=Session()
        form.FK_List['Cus_Id']['Value'] = sess.query(Customers.Cus_Name).filter(Customers.Cus_Id == session['data']['Cus_Id']).first()
        form.FK_List['Pla_Id']['Value'] = sess.query(Platforms.Pla_Name).filter(Platforms.Pla_Id == session['data']['Pla_Id']).first()
        form.FK_List['CC_Id']['Value'] = sess.query(Cost_Centers.CC_Description).filter(Cost_Centers.CC_Id == session['data']['CC_Id']).first()
        form.FK_List['CU_Id']['Value'] = sess.query(Charge_Units.CU_Description).filter(Charge_Units.CU_Id == session['data']['CU_Id']).first()
        form.FK_List['MU_Code']['Value'] = sess.query(Measure_Units.MU_Description).filter(Measure_Units.MU_Code == session['data']['MU_Code']).first()
        form.FK_List['Typ_Code']['Value'] = sess.query(CU_Types.Typ_Description).filter(CU_Types.Typ_Code == session['data']['Typ_Code']).first()
        form.FK_List['Cur_Code']['Value'] = sess.query(Currencies.Cur_Name).filter(Currencies.Cur_Code == session['data']['Cur_Code']).first()

    if form.validate_on_submit():
        session['data']['Rat_Id'] = form.Rat_Id.data
        session['data']['Cus_Id'] = form.Cus_Id.data
        session['data']['Pla_Id'] = form.Pla_Id.data
        session['data']['CC_Id'] = form.CC_Id.data
        session['data']['CU_Id'] = form.CU_Id.data
        session['data']['Rat_Price'] = form.Rat_Price.data
        session['data']['Rat_Period'] = form.Rat_Period.data
        session['data']['MU_Code'] = form.MU_Code.data
        session['data']['Typ_Code'] = form.Typ_Code.data
        session['data']['Cur_Code'] = form.Cur_Code.data
        return redirect(url_for('forms_Rates',Rat_Id=session['data']['Rat_Id']))

    form.Rat_Id.data = session['data']['Rat_Id']
    form.Cus_Id.data = session['data']['Cus_Id']
    form.Pla_Id.data = session['data']['Pla_Id']
    form.CC_Id.data = session['data']['CC_Id']
    form.CU_Id.data = session['data']['CU_Id']
    form.Rat_Price.data = session['data']['Rat_Price']
    form.Rat_Period.data = session['data']['Rat_Period']
    form.MU_Code.data = session['data']['MU_Code']
    form.Typ_Code.data = session['data']['Typ_Code']
    form.Cur_Code.data = session['data']['Cur_Code']

    return render_template('Rates.html',C=C, form=form, data=session.get('data'),row=row)

@app.route('/select/Rates', methods=['GET'])
def select_Rates():
    logger.debug('Enter: select_Rates()')
    rates =  Rates( None, None, None, None, None, None, None, None, None, None)
    rates.engine =  C.db
    result =  rates.queryall()
    rows = []
    for r in result:
	    row = object_as_dict(r)
	    rows.append(row)
    return render_template('Rates_All.html',C=C,rows=rows)
# =============================================================================
