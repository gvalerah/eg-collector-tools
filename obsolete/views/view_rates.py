# =============================================================================

# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-11-30 16:47:18
# =============================================================================


@main.route('/forms/Rates', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@permission_required(Permission.MODIFY)
@admin_required
def forms_Rates():
    """ Form handling function for table Rates """

    logger.debug('Enter: forms_Rates()')
    Rat_Id  =  request.args.get('Rat_Id',0,type=int)
    row =  rate.query.filter(rate.Rat_Id == Rat_Id).first()
    if row is None:
        row=rate()

    session['data'] =  { 'Rat_Id':row.Rat_Id, 'Typ_Code':row.Typ_Code, 'Cus_Id':row.Cus_Id, 'Pla_Id':row.Pla_Id, 'CC_Id':row.CC_Id, 'CU_Id':row.CU_Id, 'Rat_Price':row.Rat_Price, 'Cur_Code':row.Cur_Code, 'MU_Code':row.MU_Code, 'Rat_Period':row.Rat_Period, 'Rat_Type':row.Rat_Type}
    form = frm_rate()

    if form.has_FKs:
        form.Typ_Code.choices = db.session.query(cu_type.Typ_Code,cu_type.Typ_Description).order_by(cu_type.Typ_Description).all()
        form.Cus_Id.choices = db.session.query(customer.Cus_Id,customer.Cus_Name).order_by(customer.Cus_Name).all()
        form.Pla_Id.choices = db.session.query(platform.Pla_Id,platform.Pla_Name).order_by(platform.Pla_Name).all()
        form.CC_Id.choices = db.session.query(cost_center.CC_Id,cost_center.CC_Description).order_by(cost_center.CC_Description).all()
        form.CU_Id.choices = db.session.query(charge_unit.CU_Id,charge_unit.CU_Description).order_by(charge_unit.CU_Description).all()
        form.Cur_Code.choices = db.session.query(currency.Cur_Code,currency.Cur_Name).order_by(currency.Cur_Name).all()
        form.MU_Code.choices = db.session.query(measure_unit.MU_Code,measure_unit.MU_Description).order_by(measure_unit.MU_Description).all()
        form.Rat_Period.choices = db.session.query(rat_period.Rat_Period,rat_period.Value).order_by(rat_period.Value).all()

    if form.validate_on_submit():
        if     form.submit_Save.data:
            row.Typ_Code = form.Typ_Code.data
            row.Cus_Id = form.Cus_Id.data
            row.Pla_Id = form.Pla_Id.data
            row.CC_Id = form.CC_Id.data
            row.CU_Id = form.CU_Id.data
            row.Rat_Price = form.Rat_Price.data
            row.Cur_Code = form.Cur_Code.data
            row.MU_Code = form.MU_Code.data
            row.Rat_Period = form.Rat_Period.data
            try:
               db.session.close()
               db.session.add(row)
               db.session.commit()
               db.session.close()
               flash('Record %s saved OK'%(Rat_Id))
            except Exception as e:
               db.session.rollback()
               db.session.close()
               flash('ERROR saving record : %s'%(e))
            return redirect(url_for('.select_Rates_query'))
        elif   form.submit_New.data:
            print('New Data Here...')
            db.session.close()
            row=rate()
            pass
            pass
            pass
            pass
            pass
            pass
            pass
            pass
            pass
            pass
            return redirect(url_for('.forms_Rates',Rat_Id=row.Rat_Id))

        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.forms_Rates',Rat_Id=row.Rat_Id))

    form.Typ_Code.data = row.Typ_Code
    form.Cus_Id.data = row.Cus_Id
    form.Pla_Id.data = row.Pla_Id
    form.CC_Id.data = row.CC_Id
    form.CU_Id.data = row.CU_Id
    form.Rat_Price.data = row.Rat_Price
    form.Cur_Code.data = row.Cur_Code
    form.MU_Code.data = row.MU_Code
    form.Rat_Period.data = row.Rat_Period
    return render_template('rates.html', form=form, row=row)

# =============================================================================

@main.route('/forms/Rates_delete', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@admin_required
def forms_Rates_delete():
    """ Delete record handling function for table Rates """

    logger.debug('Enter: forms_Rates_delete()')
    Rat_Id  =  request.args.get('Rat_Id',0,type=int)
    row =  rate.query.filter(rate.Rat_Id == Rat_Id).first()
    if row is None:
        row=rate()
    session['data'] =  { 'Rat_Id':row.Rat_Id, 'Typ_Code':row.Typ_Code, 'Cus_Id':row.Cus_Id, 'Pla_Id':row.Pla_Id, 'CC_Id':row.CC_Id, 'CU_Id':row.CU_Id, 'Rat_Price':row.Rat_Price, 'Cur_Code':row.Cur_Code, 'MU_Code':row.MU_Code, 'Rat_Period':row.Rat_Period, 'Rat_Type':row.Rat_Type}
    form = frm_rate_delete()

    if form.validate_on_submit():
        if  form.submit_Delete.data:
            print('Delete Data Here...')
            print('Delete Data Here...')
            try:
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                flash('Record %s deleted OK'%(Rat_Id))
            except exc.IntegrityError as e:
                db.session.rollback()
                flash('INTEGRITY ERROR: Are you sure there are no dependant records in other tables?')
                return redirect(url_for('.forms_Rates_delete',Rat_Id=session['data']['Rat_Id']))

            return redirect(url_for('.select_Rates_query'))
        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
            return redirect(url_for('.select_Rates_query'))
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.select_Rates_query'))


    return render_template('rates_delete.html',C=C, form=form, data=session.get('data'),row=row)

# =============================================================================

@main.route('/select/Rates_Query', methods=['GET','POST'])
@login_required
@admin_required
def select_Rates_query():
    """ Select rows handling function for table Rates """

    logger.debug('Enter: select_Rates_query()')
    field =  request.args.get('field',None,type=str)
    value =  request.args.get('value',0,type=str)
    page  =  request.args.get('page',1,type=int)

    if field is not None:
        if   field == 'Rat_Id':
            rows =  rate.query.filter_by(Rat_Id=value)\
               .join(cu_type,rate.Typ_Code == cu_type.Typ_Code).add_columns(cu_type.Typ_Description)\
               .join(customer,rate.Cus_Id == customer.Cus_Id).add_columns(customer.Cus_Name)\
               .join(platform,rate.Pla_Id == platform.Pla_Id).add_columns(platform.Pla_Name)\
               .join(cost_center,rate.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .join(charge_unit,rate.CU_Id == charge_unit.CU_Id).add_columns(charge_unit.CU_Description)\
               .join(currency,rate.Cur_Code == currency.Cur_Code).add_columns(currency.Cur_Name)\
               .join(measure_unit,rate.MU_Code == measure_unit.MU_Code).add_columns(measure_unit.MU_Description)\
               .join(rat_period,rate.Rat_Period == rat_period.Rat_Period).add_columns(rat_period.Value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Typ_Code':
            rows =  rate.query.filter_by(Typ_Code=value)\
               .join(cu_type,rate.Typ_Code == cu_type.Typ_Code).add_columns(cu_type.Typ_Description)\
               .join(customer,rate.Cus_Id == customer.Cus_Id).add_columns(customer.Cus_Name)\
               .join(platform,rate.Pla_Id == platform.Pla_Id).add_columns(platform.Pla_Name)\
               .join(cost_center,rate.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .join(charge_unit,rate.CU_Id == charge_unit.CU_Id).add_columns(charge_unit.CU_Description)\
               .join(currency,rate.Cur_Code == currency.Cur_Code).add_columns(currency.Cur_Name)\
               .join(measure_unit,rate.MU_Code == measure_unit.MU_Code).add_columns(measure_unit.MU_Description)\
               .join(rat_period,rate.Rat_Period == rat_period.Rat_Period).add_columns(rat_period.Value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Cus_Id':
            rows =  rate.query.filter_by(Cus_Id=value)\
               .join(cu_type,rate.Typ_Code == cu_type.Typ_Code).add_columns(cu_type.Typ_Description)\
               .join(customer,rate.Cus_Id == customer.Cus_Id).add_columns(customer.Cus_Name)\
               .join(platform,rate.Pla_Id == platform.Pla_Id).add_columns(platform.Pla_Name)\
               .join(cost_center,rate.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .join(charge_unit,rate.CU_Id == charge_unit.CU_Id).add_columns(charge_unit.CU_Description)\
               .join(currency,rate.Cur_Code == currency.Cur_Code).add_columns(currency.Cur_Name)\
               .join(measure_unit,rate.MU_Code == measure_unit.MU_Code).add_columns(measure_unit.MU_Description)\
               .join(rat_period,rate.Rat_Period == rat_period.Rat_Period).add_columns(rat_period.Value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Pla_Id':
            rows =  rate.query.filter_by(Pla_Id=value)\
               .join(cu_type,rate.Typ_Code == cu_type.Typ_Code).add_columns(cu_type.Typ_Description)\
               .join(customer,rate.Cus_Id == customer.Cus_Id).add_columns(customer.Cus_Name)\
               .join(platform,rate.Pla_Id == platform.Pla_Id).add_columns(platform.Pla_Name)\
               .join(cost_center,rate.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .join(charge_unit,rate.CU_Id == charge_unit.CU_Id).add_columns(charge_unit.CU_Description)\
               .join(currency,rate.Cur_Code == currency.Cur_Code).add_columns(currency.Cur_Name)\
               .join(measure_unit,rate.MU_Code == measure_unit.MU_Code).add_columns(measure_unit.MU_Description)\
               .join(rat_period,rate.Rat_Period == rat_period.Rat_Period).add_columns(rat_period.Value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CC_Id':
            rows =  rate.query.filter_by(CC_Id=value)\
               .join(cu_type,rate.Typ_Code == cu_type.Typ_Code).add_columns(cu_type.Typ_Description)\
               .join(customer,rate.Cus_Id == customer.Cus_Id).add_columns(customer.Cus_Name)\
               .join(platform,rate.Pla_Id == platform.Pla_Id).add_columns(platform.Pla_Name)\
               .join(cost_center,rate.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .join(charge_unit,rate.CU_Id == charge_unit.CU_Id).add_columns(charge_unit.CU_Description)\
               .join(currency,rate.Cur_Code == currency.Cur_Code).add_columns(currency.Cur_Name)\
               .join(measure_unit,rate.MU_Code == measure_unit.MU_Code).add_columns(measure_unit.MU_Description)\
               .join(rat_period,rate.Rat_Period == rat_period.Rat_Period).add_columns(rat_period.Value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CU_Id':
            rows =  rate.query.filter_by(CU_Id=value)\
               .join(cu_type,rate.Typ_Code == cu_type.Typ_Code).add_columns(cu_type.Typ_Description)\
               .join(customer,rate.Cus_Id == customer.Cus_Id).add_columns(customer.Cus_Name)\
               .join(platform,rate.Pla_Id == platform.Pla_Id).add_columns(platform.Pla_Name)\
               .join(cost_center,rate.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .join(charge_unit,rate.CU_Id == charge_unit.CU_Id).add_columns(charge_unit.CU_Description)\
               .join(currency,rate.Cur_Code == currency.Cur_Code).add_columns(currency.Cur_Name)\
               .join(measure_unit,rate.MU_Code == measure_unit.MU_Code).add_columns(measure_unit.MU_Description)\
               .join(rat_period,rate.Rat_Period == rat_period.Rat_Period).add_columns(rat_period.Value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Rat_Price':
            rows =  rate.query.filter_by(Rat_Price=value)\
               .join(cu_type,rate.Typ_Code == cu_type.Typ_Code).add_columns(cu_type.Typ_Description)\
               .join(customer,rate.Cus_Id == customer.Cus_Id).add_columns(customer.Cus_Name)\
               .join(platform,rate.Pla_Id == platform.Pla_Id).add_columns(platform.Pla_Name)\
               .join(cost_center,rate.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .join(charge_unit,rate.CU_Id == charge_unit.CU_Id).add_columns(charge_unit.CU_Description)\
               .join(currency,rate.Cur_Code == currency.Cur_Code).add_columns(currency.Cur_Name)\
               .join(measure_unit,rate.MU_Code == measure_unit.MU_Code).add_columns(measure_unit.MU_Description)\
               .join(rat_period,rate.Rat_Period == rat_period.Rat_Period).add_columns(rat_period.Value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Cur_Code':
            rows =  rate.query.filter_by(Cur_Code=value)\
               .join(cu_type,rate.Typ_Code == cu_type.Typ_Code).add_columns(cu_type.Typ_Description)\
               .join(customer,rate.Cus_Id == customer.Cus_Id).add_columns(customer.Cus_Name)\
               .join(platform,rate.Pla_Id == platform.Pla_Id).add_columns(platform.Pla_Name)\
               .join(cost_center,rate.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .join(charge_unit,rate.CU_Id == charge_unit.CU_Id).add_columns(charge_unit.CU_Description)\
               .join(currency,rate.Cur_Code == currency.Cur_Code).add_columns(currency.Cur_Name)\
               .join(measure_unit,rate.MU_Code == measure_unit.MU_Code).add_columns(measure_unit.MU_Description)\
               .join(rat_period,rate.Rat_Period == rat_period.Rat_Period).add_columns(rat_period.Value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'MU_Code':
            rows =  rate.query.filter_by(MU_Code=value)\
               .join(cu_type,rate.Typ_Code == cu_type.Typ_Code).add_columns(cu_type.Typ_Description)\
               .join(customer,rate.Cus_Id == customer.Cus_Id).add_columns(customer.Cus_Name)\
               .join(platform,rate.Pla_Id == platform.Pla_Id).add_columns(platform.Pla_Name)\
               .join(cost_center,rate.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .join(charge_unit,rate.CU_Id == charge_unit.CU_Id).add_columns(charge_unit.CU_Description)\
               .join(currency,rate.Cur_Code == currency.Cur_Code).add_columns(currency.Cur_Name)\
               .join(measure_unit,rate.MU_Code == measure_unit.MU_Code).add_columns(measure_unit.MU_Description)\
               .join(rat_period,rate.Rat_Period == rat_period.Rat_Period).add_columns(rat_period.Value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Rat_Period':
            rows =  rate.query.filter_by(Rat_Period=value)\
               .join(cu_type,rate.Typ_Code == cu_type.Typ_Code).add_columns(cu_type.Typ_Description)\
               .join(customer,rate.Cus_Id == customer.Cus_Id).add_columns(customer.Cus_Name)\
               .join(platform,rate.Pla_Id == platform.Pla_Id).add_columns(platform.Pla_Name)\
               .join(cost_center,rate.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .join(charge_unit,rate.CU_Id == charge_unit.CU_Id).add_columns(charge_unit.CU_Description)\
               .join(currency,rate.Cur_Code == currency.Cur_Code).add_columns(currency.Cur_Name)\
               .join(measure_unit,rate.MU_Code == measure_unit.MU_Code).add_columns(measure_unit.MU_Description)\
               .join(rat_period,rate.Rat_Period == rat_period.Rat_Period).add_columns(rat_period.Value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Rat_Type':
            rows =  rate.query.filter_by(Rat_Type=value)\
               .join(cu_type,rate.Typ_Code == cu_type.Typ_Code).add_columns(cu_type.Typ_Description)\
               .join(customer,rate.Cus_Id == customer.Cus_Id).add_columns(customer.Cus_Name)\
               .join(platform,rate.Pla_Id == platform.Pla_Id).add_columns(platform.Pla_Name)\
               .join(cost_center,rate.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .join(charge_unit,rate.CU_Id == charge_unit.CU_Id).add_columns(charge_unit.CU_Description)\
               .join(currency,rate.Cur_Code == currency.Cur_Code).add_columns(currency.Cur_Name)\
               .join(measure_unit,rate.MU_Code == measure_unit.MU_Code).add_columns(measure_unit.MU_Description)\
               .join(rat_period,rate.Rat_Period == rat_period.Rat_Period).add_columns(rat_period.Value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
    else:
       rows =  rate.query\
               .join(cu_type,rate.Typ_Code == cu_type.Typ_Code).add_columns(cu_type.Typ_Description)\
               .join(customer,rate.Cus_Id == customer.Cus_Id).add_columns(customer.Cus_Name)\
               .join(platform,rate.Pla_Id == platform.Pla_Id).add_columns(platform.Pla_Name)\
               .join(cost_center,rate.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .join(charge_unit,rate.CU_Id == charge_unit.CU_Id).add_columns(charge_unit.CU_Description)\
               .join(currency,rate.Cur_Code == currency.Cur_Code).add_columns(currency.Cur_Name)\
               .join(measure_unit,rate.MU_Code == measure_unit.MU_Code).add_columns(measure_unit.MU_Description)\
               .join(rat_period,rate.Rat_Period == rat_period.Rat_Period).add_columns(rat_period.Value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)

    next_url = url_for('.select_Rates_query', page=rows.next_num) \
        if rows.has_next else None
    prev_url = url_for('.select_Rates_query', page=rows.prev_num) \
        if rows.has_prev else None

    return render_template('rates_All.html',C=C,rows=rows.items,next_url=next_url,prev_url=prev_url)
# =============================================================================

