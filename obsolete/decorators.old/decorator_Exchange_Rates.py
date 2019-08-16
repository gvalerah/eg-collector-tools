# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-10-31 18:36:07
# =============================================================================
from db.Exchange_Rates import Exchange_Rates,frm_Exchange_Rates

@app.route('/forms/Exchange_Rates/<ER_Id>', methods=['GET', 'POST'])
def forms_Exchange_Rates(ER_Id):
    logger.debug('Enter: forms_Exchange_Rates(%s,)'%(ER_Id))
    exchange_rates =  Exchange_Rates( None, None, None, None)
    exchange_rates.engine =  C.db
    row =  exchange_rates.queryone(ER_Id)
    if row is not None:
        session['data'] =  { 'ER_Id':row.ER_Id, 'Cur_Code':row.Cur_Code, 'ER_Factor':row.ER_Factor, 'ER_Date':row.ER_Date}
    else:
        session['data'] =  { 'ER_Id':None, 'Cur_Code':None, 'ER_Factor':None, 'ER_Date':None}
    form = frm_Exchange_Rates()

    form.engine = C.db

    if form.has_FKs:
        form.set_FK_list()

        Session=sessionmaker(bind=C.db)
        sess=Session()
        form.FK_List['Cur_Code']['Value'] = sess.query(Currencies.Cur_Name).filter(Currencies.Cur_Code == session['data']['Cur_Code']).first()

    if form.validate_on_submit():
        session['data']['ER_Id'] = form.ER_Id.data
        session['data']['Cur_Code'] = form.Cur_Code.data
        session['data']['ER_Factor'] = form.ER_Factor.data
        session['data']['ER_Date'] = form.ER_Date.data
        return redirect(url_for('forms_Exchange_Rates',ER_Id=session['data']['ER_Id']))

    form.ER_Id.data = session['data']['ER_Id']
    form.Cur_Code.data = session['data']['Cur_Code']
    form.ER_Factor.data = session['data']['ER_Factor']
    form.ER_Date.data = session['data']['ER_Date']

    return render_template('Exchange_Rates.html',C=C, form=form, data=session.get('data'),row=row)

@app.route('/select/Exchange_Rates', methods=['GET'])
def select_Exchange_Rates():
    logger.debug('Enter: select_Exchange_Rates()')
    exchange_rates =  Exchange_Rates( None, None, None, None)
    exchange_rates.engine =  C.db
    result =  exchange_rates.queryall()
    rows = []
    for r in result:
	    row = object_as_dict(r)
	    rows.append(row)
    return render_template('Exchange_Rates_All.html',C=C,rows=rows)
# =============================================================================
