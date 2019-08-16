# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-11-01 18:15:21
# =============================================================================
from db.charge_items import Charge_Items,frm_Charge_Items

@app.route('/forms/Charge_Items/<CU_Id>&<CIT_Date>&<CIT_Time>', methods=['GET', 'POST'])
def forms_Charge_Items(CU_Id,CIT_Date,CIT_Time):
    logger.debug('Enter: forms_Charge_Items(%s,%s,%s,)'%(CU_Id,CIT_Date,CIT_Time))
    charge_items =  Charge_Items()
    row =  charge_items.queryone(CU_Id,CIT_Date,CIT_Time)
    if row is not None:
        session['data'] =  { 'CU_Id':row.CU_Id, 'CIT_Date':row.CIT_Date, 'CIT_Time':str(row.CIT_Time), 'CIT_Quantity':row.CIT_Quantity, 'CIT_Status':row.CIT_Status, 'CIT_Is_Active':row.CIT_Is_Active}
    else:
        session['data'] =  { 'CU_Id':None, 'CIT_Date':None, 'CIT_Time':None, 'CIT_Quantity':None, 'CIT_Status':None, 'CIT_Is_Active':None}
    form = frm_Charge_Items()

    if form.has_FKs:
        form.set_FK_list()

        Session=sessionmaker(bind=C.db)
        sess=Session()
        form.FK_List['CU_Id']['Value'] = sess.query(Charge_Units.CU_Description).filter(Charge_Units.CU_Id == session['data']['CU_Id']).first()

    form.CIT_Status.choices    = [(1,"Pending Approval"),(2,"Claimed"),(3,"Rejected"),(4,"Approved")]
    if form.validate_on_submit():
        session['data']['CU_Id'] = form.CU_Id.data
        session['data']['CIT_Date'] = form.CIT_Date.data
        session['data']['CIT_Time'] = form.CIT_Time.data
        session['data']['CIT_Quantity'] = form.CIT_Quantity.data
        session['data']['CIT_Status'] = form.CIT_Status.data
        session['data']['CIT_Is_Active'] = form.CIT_Is_Active.data
        return redirect(url_for('forms_Charge_Items',CU_Id=session['data']['CU_Id'],CIT_Date=session['data']['CIT_Date'],CIT_Time=session['data']['CIT_Time']))

    form.CU_Id.data = session['data']['CU_Id']
    form.CIT_Date.data = session['data']['CIT_Date']
    form.CIT_Time.data = session['data']['CIT_Time']
    form.CIT_Quantity.data = session['data']['CIT_Quantity']
    form.CIT_Status.data = session['data']['CIT_Status']
    form.CIT_Is_Active.data = session['data']['CIT_Is_Active']

    return render_template('Charge_Items.html',C=C, form=form, data=session.get('data'),row=row)

@app.route('/select/Charge_Items', methods=['GET'])
def select_Charge_Items():
    logger.debug('Enter: select_Charge_Items()')
    charge_items =  Charge_Items()
    result =  charge_items.queryall()
    rows = []
    for r in result:
	    row = object_as_dict(r)
	    rows.append(row)
    return render_template('Charge_Items_All.html',C=C,rows=rows)
# =============================================================================
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-11-01 18:15:21
# =============================================================================
from db.charge_units import Charge_Units,frm_Charge_Units

@app.route('/forms/Charge_Units/<CU_Id>', methods=['GET', 'POST'])
def forms_Charge_Units(CU_Id):
    logger.debug('Enter: forms_Charge_Units(%s,)'%(CU_Id))
    charge_units =  Charge_Units()
    row =  charge_units.queryone(CU_Id)
    if row is not None:
        session['data'] =  { 'CU_Id':row.CU_Id, 'CI_Id':row.CI_Id, 'CU_Description':row.CU_Description, 'CU_UUID':row.CU_UUID, 'CU_Is_Billeable':row.CU_Is_Billeable, 'CU_Is_Always_Billeable':row.CU_Is_Always_Billeable, 'CU_Quantity':row.CU_Quantity, 'CU_Operation':row.CU_Operation, 'Typ_Code':row.Typ_Code, 'CC_Id':row.CC_Id}
    else:
        session['data'] =  { 'CU_Id':None, 'CI_Id':None, 'CU_Description':None, 'CU_UUID':None, 'CU_Is_Billeable':None, 'CU_Is_Always_Billeable':None, 'CU_Quantity':None, 'CU_Operation':None, 'Typ_Code':None, 'CC_Id':None}
    form = frm_Charge_Units()

    if form.has_FKs:
        form.set_FK_list()

        Session=sessionmaker(bind=C.db)
        sess=Session()
        form.FK_List['CI_Id']['Value'] = sess.query(Configuration_Items.CI_Name).filter(Configuration_Items.CI_Id == session['data']['CI_Id']).first()
        form.FK_List['Typ_Code']['Value'] = sess.query(CU_Types.Typ_Description).filter(CU_Types.Typ_Code == session['data']['Typ_Code']).first()
        form.FK_List['CC_Id']['Value'] = sess.query(Cost_Centers.CC_Description).filter(Cost_Centers.CC_Id == session['data']['CC_Id']).first()

    form.CU_Operation.choices           = [("None","No Conversion"),("BTOKB","Bytes to KB"),("BTOMB","Bytes to MB"),("BTOGB","Bytes to GB"),("KBTOB","KB to Bytes"),("KBTOMB","KB to MB"),("KBTOGB","KB to GB"),("MBTOB","MB to Bytes"),("MBTOKB","MB to KB"),("MBTOGB","MB to GB"),("GBTOB","GB to Bytes"),("GBTOKB","GB to KB"),("GBTOMB","GB to MB"),("HTOD","Hours to Days"),("HTOM","Hours to Months"),("DTOH","Days to Hours"),("DTOM","Days to Months"),("MTOH","Months to Hours"),("MTOD","Months to Days"),]
    if form.validate_on_submit():
        session['data']['CU_Id'] = form.CU_Id.data
        session['data']['CI_Id'] = form.CI_Id.data
        session['data']['CU_Description'] = form.CU_Description.data
        session['data']['CU_UUID'] = form.CU_UUID.data
        session['data']['CU_Is_Billeable'] = form.CU_Is_Billeable.data
        session['data']['CU_Is_Always_Billeable'] = form.CU_Is_Always_Billeable.data
        session['data']['CU_Quantity'] = form.CU_Quantity.data
        session['data']['CU_Operation'] = form.CU_Operation.data
        session['data']['Typ_Code'] = form.Typ_Code.data
        session['data']['CC_Id'] = form.CC_Id.data
        return redirect(url_for('forms_Charge_Units',CU_Id=session['data']['CU_Id']))

    form.CU_Id.data = session['data']['CU_Id']
    form.CI_Id.data = session['data']['CI_Id']
    form.CU_Description.data = session['data']['CU_Description']
    form.CU_UUID.data = session['data']['CU_UUID']
    form.CU_Is_Billeable.data = session['data']['CU_Is_Billeable']
    form.CU_Is_Always_Billeable.data = session['data']['CU_Is_Always_Billeable']
    form.CU_Quantity.data = session['data']['CU_Quantity']
    form.CU_Operation.data = session['data']['CU_Operation']
    form.Typ_Code.data = session['data']['Typ_Code']
    form.CC_Id.data = session['data']['CC_Id']

    return render_template('Charge_Units.html',C=C, form=form, data=session.get('data'),row=row)

@app.route('/select/Charge_Units', methods=['GET'])
def select_Charge_Units():
    logger.debug('Enter: select_Charge_Units()')
    charge_units =  Charge_Units()
    result =  charge_units.queryall()
    rows = []
    for r in result:
	    row = object_as_dict(r)
	    rows.append(row)
    return render_template('Charge_Units_All.html',C=C,rows=rows)
# =============================================================================
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-11-01 18:15:21
# =============================================================================
from db.configuration_items import Configuration_Items,frm_Configuration_Items

@app.route('/forms/Configuration_Items/<CI_Id>', methods=['GET', 'POST'])
def forms_Configuration_Items(CI_Id):
    logger.debug('Enter: forms_Configuration_Items(%s,)'%(CI_Id))
    configuration_items =  Configuration_Items()
    row =  configuration_items.queryone(CI_Id)
    if row is not None:
        session['data'] =  { 'CI_Id':row.CI_Id, 'CI_Name':row.CI_Name, 'CI_UUID':row.CI_UUID, 'Pla_Id':row.Pla_Id, 'CC_Id':row.CC_Id, 'CI_CIT_Generation':row.CI_CIT_Generation, 'Cus_Id':row.Cus_Id}
    else:
        session['data'] =  { 'CI_Id':None, 'CI_Name':None, 'CI_UUID':None, 'Pla_Id':None, 'CC_Id':None, 'CI_CIT_Generation':None, 'Cus_Id':None}
    form = frm_Configuration_Items()

    if form.has_FKs:
        form.set_FK_list()

        Session=sessionmaker(bind=C.db)
        sess=Session()
        form.FK_List['Pla_Id']['Value'] = sess.query(Platforms.Pla_Name).filter(Platforms.Pla_Id == session['data']['Pla_Id']).first()
        form.FK_List['CC_Id']['Value'] = sess.query(Cost_Centers.CC_Description).filter(Cost_Centers.CC_Id == session['data']['CC_Id']).first()
        form.FK_List['Cus_Id']['Value'] = sess.query(Customers.Cus_Name).filter(Customers.Cus_Id == session['data']['Cus_Id']).first()

    form.CI_CIT_Generation.choices = [(0,"Undefined"),(1,"Daemon"),(2,"Manual"),(3,"Monthly")]
    if form.validate_on_submit():
        session['data']['CI_Id'] = form.CI_Id.data
        session['data']['CI_Name'] = form.CI_Name.data
        session['data']['CI_UUID'] = form.CI_UUID.data
        session['data']['Pla_Id'] = form.Pla_Id.data
        session['data']['CC_Id'] = form.CC_Id.data
        session['data']['CI_CIT_Generation'] = form.CI_CIT_Generation.data
        session['data']['Cus_Id'] = form.Cus_Id.data
        return redirect(url_for('forms_Configuration_Items',CI_Id=session['data']['CI_Id']))

    form.CI_Id.data = session['data']['CI_Id']
    form.CI_Name.data = session['data']['CI_Name']
    form.CI_UUID.data = session['data']['CI_UUID']
    form.Pla_Id.data = session['data']['Pla_Id']
    form.CC_Id.data = session['data']['CC_Id']
    form.CI_CIT_Generation.data = session['data']['CI_CIT_Generation']
    form.Cus_Id.data = session['data']['Cus_Id']

    return render_template('Configuration_Items.html',C=C, form=form, data=session.get('data'),row=row)

@app.route('/select/Configuration_Items', methods=['GET'])
def select_Configuration_Items():
    logger.debug('Enter: select_Configuration_Items()')
    configuration_items =  Configuration_Items()
    result =  configuration_items.queryall()
    rows = []
    for r in result:
	    row = object_as_dict(r)
	    rows.append(row)
    return render_template('Configuration_Items_All.html',C=C,rows=rows)
# =============================================================================
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-11-01 18:15:21
# =============================================================================
from db.cost_centers import Cost_Centers,frm_Cost_Centers

@app.route('/forms/Cost_Centers/<CC_Id>', methods=['GET', 'POST'])
def forms_Cost_Centers(CC_Id):
    logger.debug('Enter: forms_Cost_Centers(%s,)'%(CC_Id))
    cost_centers =  Cost_Centers()
    row =  cost_centers.queryone(CC_Id)
    if row is not None:
        session['data'] =  { 'CC_Id':row.CC_Id, 'CC_Code':row.CC_Code, 'CC_Description':row.CC_Description, 'Cur_Code':row.Cur_Code}
    else:
        session['data'] =  { 'CC_Id':None, 'CC_Code':None, 'CC_Description':None, 'Cur_Code':None}
    form = frm_Cost_Centers()

    if form.has_FKs:
        form.set_FK_list()

        Session=sessionmaker(bind=C.db)
        sess=Session()
        form.FK_List['Cur_Code']['Value'] = sess.query(Currencies.Cur_Name).filter(Currencies.Cur_Code == session['data']['Cur_Code']).first()

    if form.validate_on_submit():
        session['data']['CC_Id'] = form.CC_Id.data
        session['data']['CC_Code'] = form.CC_Code.data
        session['data']['CC_Description'] = form.CC_Description.data
        session['data']['Cur_Code'] = form.Cur_Code.data
        return redirect(url_for('forms_Cost_Centers',CC_Id=session['data']['CC_Id']))

    form.CC_Id.data = session['data']['CC_Id']
    form.CC_Code.data = session['data']['CC_Code']
    form.CC_Description.data = session['data']['CC_Description']
    form.Cur_Code.data = session['data']['Cur_Code']

    return render_template('Cost_Centers.html',C=C, form=form, data=session.get('data'),row=row)

@app.route('/select/Cost_Centers', methods=['GET'])
def select_Cost_Centers():
    logger.debug('Enter: select_Cost_Centers()')
    cost_centers =  Cost_Centers()
    result =  cost_centers.queryall()
    rows = []
    for r in result:
	    row = object_as_dict(r)
	    rows.append(row)
    return render_template('Cost_Centers_All.html',C=C,rows=rows)
# =============================================================================
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-11-01 18:15:21
# =============================================================================
from db.countries_currencies import Countries_Currencies,frm_Countries_Currencies

@app.route('/forms/Countries_Currencies/<Cou_Code>&<Cur_Code>', methods=['GET', 'POST'])
def forms_Countries_Currencies(Cou_Code,Cur_Code):
    logger.debug('Enter: forms_Countries_Currencies(%s,%s,)'%(Cou_Code,Cur_Code))
    countries_currencies =  Countries_Currencies()
    row =  countries_currencies.queryone(Cou_Code,Cur_Code)
    if row is not None:
        session['data'] =  { 'Cou_Code':row.Cou_Code, 'Cur_Code':row.Cur_Code, 'Cou_Cur_Comment':row.Cou_Cur_Comment}
    else:
        session['data'] =  { 'Cou_Code':None, 'Cur_Code':None, 'Cou_Cur_Comment':None}
    form = frm_Countries_Currencies()

    if form.has_FKs:
        form.set_FK_list()

        Session=sessionmaker(bind=C.db)
        sess=Session()
        form.FK_List['Cou_Code']['Value'] = sess.query(Countries.Cou_Name).filter(Countries.Cou_Code == session['data']['Cou_Code']).first()
        form.FK_List['Cur_Code']['Value'] = sess.query(Currencies.Cur_Name).filter(Currencies.Cur_Code == session['data']['Cur_Code']).first()

    if form.validate_on_submit():
        session['data']['Cou_Code'] = form.Cou_Code.data
        session['data']['Cur_Code'] = form.Cur_Code.data
        session['data']['Cou_Cur_Comment'] = form.Cou_Cur_Comment.data
        return redirect(url_for('forms_Countries_Currencies',Cou_Code=session['data']['Cou_Code'],Cur_Code=session['data']['Cur_Code']))

    form.Cou_Code.data = session['data']['Cou_Code']
    form.Cur_Code.data = session['data']['Cur_Code']
    form.Cou_Cur_Comment.data = session['data']['Cou_Cur_Comment']

    return render_template('Countries_Currencies.html',C=C, form=form, data=session.get('data'),row=row)

@app.route('/select/Countries_Currencies', methods=['GET'])
def select_Countries_Currencies():
    logger.debug('Enter: select_Countries_Currencies()')
    countries_currencies =  Countries_Currencies()
    result =  countries_currencies.queryall()
    rows = []
    for r in result:
	    row = object_as_dict(r)
	    rows.append(row)
    return render_template('Countries_Currencies_All.html',C=C,rows=rows)
# =============================================================================
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-11-01 18:15:21
# =============================================================================
from db.countries import Countries,frm_Countries

@app.route('/forms/Countries/<Cou_Code>', methods=['GET', 'POST'])
def forms_Countries(Cou_Code):
    logger.debug('Enter: forms_Countries(%s,)'%(Cou_Code))
    countries =  Countries()
    row =  countries.queryone(Cou_Code)
    if row is not None:
        session['data'] =  { 'Cou_Code':row.Cou_Code, 'Cou_Name':row.Cou_Name, 'Cou_A3':row.Cou_A3, 'Cou_N':row.Cou_N}
    else:
        session['data'] =  { 'Cou_Code':None, 'Cou_Name':None, 'Cou_A3':None, 'Cou_N':None}
    form = frm_Countries()

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
    countries =  Countries()
    result =  countries.queryall()
    rows = []
    for r in result:
	    row = object_as_dict(r)
	    rows.append(row)
    return render_template('Countries_All.html',C=C,rows=rows)
# =============================================================================
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-11-01 18:15:21
# =============================================================================
from db.currencies import Currencies,frm_Currencies

@app.route('/forms/Currencies/<Cur_Code>', methods=['GET', 'POST'])
def forms_Currencies(Cur_Code):
    logger.debug('Enter: forms_Currencies(%s,)'%(Cur_Code))
    currencies =  Currencies()
    row =  currencies.queryone(Cur_Code)
    if row is not None:
        session['data'] =  { 'Cur_Code':row.Cur_Code, 'Cur_Name':row.Cur_Name, 'Cur_Id':row.Cur_Id, 'Cur_Comment':row.Cur_Comment}
    else:
        session['data'] =  { 'Cur_Code':None, 'Cur_Name':None, 'Cur_Id':None, 'Cur_Comment':None}
    form = frm_Currencies()

    if form.has_FKs:
        form.set_FK_list()

        Session=sessionmaker(bind=C.db)
        sess=Session()

    if form.validate_on_submit():
        session['data']['Cur_Code'] = form.Cur_Code.data
        session['data']['Cur_Name'] = form.Cur_Name.data
        session['data']['Cur_Id'] = form.Cur_Id.data
        session['data']['Cur_Comment'] = form.Cur_Comment.data
        return redirect(url_for('forms_Currencies',Cur_Code=session['data']['Cur_Code']))

    form.Cur_Code.data = session['data']['Cur_Code']
    form.Cur_Name.data = session['data']['Cur_Name']
    form.Cur_Id.data = session['data']['Cur_Id']
    form.Cur_Comment.data = session['data']['Cur_Comment']

    return render_template('Currencies.html',C=C, form=form, data=session.get('data'),row=row)

@app.route('/select/Currencies', methods=['GET'])
def select_Currencies():
    logger.debug('Enter: select_Currencies()')
    currencies =  Currencies()
    result =  currencies.queryall()
    rows = []
    for r in result:
	    row = object_as_dict(r)
	    rows.append(row)
    return render_template('Currencies_All.html',C=C,rows=rows)
# =============================================================================
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-11-01 18:15:21
# =============================================================================
from db.customers import Customers,frm_Customers

@app.route('/forms/Customers/<Cus_Id>', methods=['GET', 'POST'])
def forms_Customers(Cus_Id):
    logger.debug('Enter: forms_Customers(%s,)'%(Cus_Id))
    customers =  Customers()
    row =  customers.queryone(Cus_Id)
    if row is not None:
        session['data'] =  { 'Cus_Id':row.Cus_Id, 'Cus_Name':row.Cus_Name, 'CC_Id':row.CC_Id}
    else:
        session['data'] =  { 'Cus_Id':None, 'Cus_Name':None, 'CC_Id':None}
    form = frm_Customers()

    if form.has_FKs:
        form.set_FK_list()

        Session=sessionmaker(bind=C.db)
        sess=Session()
        form.FK_List['CC_Id']['Value'] = sess.query(Cost_Centers.CC_Description).filter(Cost_Centers.CC_Id == session['data']['CC_Id']).first()

    if form.validate_on_submit():
        session['data']['Cus_Id'] = form.Cus_Id.data
        session['data']['Cus_Name'] = form.Cus_Name.data
        session['data']['CC_Id'] = form.CC_Id.data
        return redirect(url_for('forms_Customers',Cus_Id=session['data']['Cus_Id']))

    form.Cus_Id.data = session['data']['Cus_Id']
    form.Cus_Name.data = session['data']['Cus_Name']
    form.CC_Id.data = session['data']['CC_Id']

    return render_template('Customers.html',C=C, form=form, data=session.get('data'),row=row)

@app.route('/select/Customers', methods=['GET'])
def select_Customers():
    logger.debug('Enter: select_Customers()')
    customers =  Customers()
    result =  customers.queryall()
    rows = []
    for r in result:
	    row = object_as_dict(r)
	    rows.append(row)
    return render_template('Customers_All.html',C=C,rows=rows)
# =============================================================================
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-11-01 18:15:21
# =============================================================================
from db.cu_types import CU_Types,frm_CU_Types

@app.route('/forms/CU_Types/<Typ_Code>', methods=['GET', 'POST'])
def forms_CU_Types(Typ_Code):
    logger.debug('Enter: forms_CU_Types(%s,)'%(Typ_Code))
    cu_types =  CU_Types()
    row =  cu_types.queryone(Typ_Code)
    if row is not None:
        session['data'] =  { 'Typ_Code':row.Typ_Code, 'Typ_Description':row.Typ_Description}
    else:
        session['data'] =  { 'Typ_Code':None, 'Typ_Description':None}
    form = frm_CU_Types()

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
    cu_types =  CU_Types()
    result =  cu_types.queryall()
    rows = []
    for r in result:
	    row = object_as_dict(r)
	    rows.append(row)
    return render_template('CU_Types_All.html',C=C,rows=rows)
# =============================================================================
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-11-01 18:15:21
# =============================================================================
from db.exchange_rates import Exchange_Rates,frm_Exchange_Rates

@app.route('/forms/Exchange_Rates/<ER_Id>', methods=['GET', 'POST'])
def forms_Exchange_Rates(ER_Id):
    logger.debug('Enter: forms_Exchange_Rates(%s,)'%(ER_Id))
    exchange_rates =  Exchange_Rates()
    row =  exchange_rates.queryone(ER_Id)
    if row is not None:
        session['data'] =  { 'ER_Id':row.ER_Id, 'Cur_Code':row.Cur_Code, 'ER_Factor':row.ER_Factor, 'ER_Date':row.ER_Date}
    else:
        session['data'] =  { 'ER_Id':None, 'Cur_Code':None, 'ER_Factor':None, 'ER_Date':None}
    form = frm_Exchange_Rates()

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
    exchange_rates =  Exchange_Rates()
    result =  exchange_rates.queryall()
    rows = []
    for r in result:
	    row = object_as_dict(r)
	    rows.append(row)
    return render_template('Exchange_Rates_All.html',C=C,rows=rows)
# =============================================================================
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-11-01 18:15:21
# =============================================================================
from db.lists import Lists,frm_Lists

@app.route('/forms/Lists/<Type>&<Value>&<Caption>', methods=['GET', 'POST'])
def forms_Lists(Type,Value,Caption):
    logger.debug('Enter: forms_Lists(%s,%s,%s,)'%(Type,Value,Caption))
    lists =  Lists()
    row =  lists.queryone(Type,Value,Caption)
    if row is not None:
        session['data'] =  { 'Type':row.Type, 'Value':row.Value, 'Caption':row.Caption}
    else:
        session['data'] =  { 'Type':None, 'Value':None, 'Caption':None}
    form = frm_Lists()

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
    lists =  Lists()
    result =  lists.queryall()
    rows = []
    for r in result:
	    row = object_as_dict(r)
	    rows.append(row)
    return render_template('Lists_All.html',C=C,rows=rows)
# =============================================================================
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-11-01 18:15:21
# =============================================================================
from db.measure_units import Measure_Units,frm_Measure_Units

@app.route('/forms/Measure_Units/<MU_Code>', methods=['GET', 'POST'])
def forms_Measure_Units(MU_Code):
    logger.debug('Enter: forms_Measure_Units(%s,)'%(MU_Code))
    measure_units =  Measure_Units()
    row =  measure_units.queryone(MU_Code)
    if row is not None:
        session['data'] =  { 'MU_Code':row.MU_Code, 'MU_Description':row.MU_Description}
    else:
        session['data'] =  { 'MU_Code':None, 'MU_Description':None}
    form = frm_Measure_Units()

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
    measure_units =  Measure_Units()
    result =  measure_units.queryall()
    rows = []
    for r in result:
	    row = object_as_dict(r)
	    rows.append(row)
    return render_template('Measure_Units_All.html',C=C,rows=rows)
# =============================================================================
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-11-01 18:15:21
# =============================================================================
from db.platforms import Platforms,frm_Platforms

@app.route('/forms/Platforms/<Pla_Id>', methods=['GET', 'POST'])
def forms_Platforms(Pla_Id):
    logger.debug('Enter: forms_Platforms(%s,)'%(Pla_Id))
    platforms =  Platforms()
    row =  platforms.queryone(Pla_Id)
    if row is not None:
        session['data'] =  { 'Pla_Id':row.Pla_Id, 'Pla_Name':row.Pla_Name, 'Pla_Host':row.Pla_Host, 'Pla_Port':row.Pla_Port, 'Pla_User':row.Pla_User, 'Pla_Password':row.Pla_Password}
    else:
        session['data'] =  { 'Pla_Id':None, 'Pla_Name':None, 'Pla_Host':None, 'Pla_Port':None, 'Pla_User':None, 'Pla_Password':None}
    form = frm_Platforms()

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
    platforms =  Platforms()
    result =  platforms.queryall()
    rows = []
    for r in result:
	    row = object_as_dict(r)
	    rows.append(row)
    return render_template('Platforms_All.html',C=C,rows=rows)
# =============================================================================
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-11-01 18:15:21
# =============================================================================
from db.rates import Rates,frm_Rates

@app.route('/forms/Rates/<Rat_Id>', methods=['GET', 'POST'])
def forms_Rates(Rat_Id):
    logger.debug('Enter: forms_Rates(%s,)'%(Rat_Id))
    rates =  Rates()
    row =  rates.queryone(Rat_Id)
    if row is not None:
        session['data'] =  { 'Rat_Id':row.Rat_Id, 'Cus_Id':row.Cus_Id, 'Pla_Id':row.Pla_Id, 'CC_Id':row.CC_Id, 'CU_Id':row.CU_Id, 'Rat_Price':row.Rat_Price, 'Rat_Period':row.Rat_Period, 'MU_Code':row.MU_Code, 'Typ_Code':row.Typ_Code, 'Cur_Code':row.Cur_Code}
    else:
        session['data'] =  { 'Rat_Id':None, 'Cus_Id':None, 'Pla_Id':None, 'CC_Id':None, 'CU_Id':None, 'Rat_Price':None, 'Rat_Period':None, 'MU_Code':None, 'Typ_Code':None, 'Cur_Code':None}
    form = frm_Rates()

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
    rates =  Rates()
    result =  rates.queryall()
    rows = []
    for r in result:
	    row = object_as_dict(r)
	    rows.append(row)
    return render_template('Rates_All.html',C=C,rows=rows)
# =============================================================================
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-11-01 18:15:21
# =============================================================================
from db.trace import Trace,frm_Trace

@app.route('/forms/Trace/<ID>', methods=['GET', 'POST'])
def forms_Trace(ID):
    logger.debug('Enter: forms_Trace(%s,)'%(ID))
    trace =  Trace()
    row =  trace.queryone(ID)
    if row is not None:
        session['data'] =  { 'ID':row.ID, 'LINE':row.LINE}
    else:
        session['data'] =  { 'ID':None, 'LINE':None}
    form = frm_Trace()

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
    trace =  Trace()
    result =  trace.queryall()
    rows = []
    for r in result:
	    row = object_as_dict(r)
	    rows.append(row)
    return render_template('Trace_All.html',C=C,rows=rows)
# =============================================================================
