# =============================================================================

# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-11-30 16:47:18
# =============================================================================


@main.route('/forms/Charge_Units', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@permission_required(Permission.MODIFY)
@admin_required
def forms_Charge_Units():
    """ Form handling function for table Charge_Units """

    logger.debug('Enter: forms_Charge_Units()')
    CU_Id  =  request.args.get('CU_Id',0,type=int)
    parent_key  =  request.args.get('parent_key',None,type=str)
    parent_value=  request.args.get('parent_value',0,type=int)

    row =  charge_unit.query.filter(charge_unit.CU_Id == CU_Id).first()
    if row is None:
        row=charge_unit()

    session['data'] =  { 'CU_Id':row.CU_Id, 'CI_Id':row.CI_Id, 'CU_Description':row.CU_Description, 'CU_UUID':row.CU_UUID, 'CU_Is_Billeable':row.CU_Is_Billeable, 'CU_Is_Always_Billeable':row.CU_Is_Always_Billeable, 'CU_Quantity':row.CU_Quantity, 'CU_Operation':row.CU_Operation, 'Typ_Code':row.Typ_Code, 'CC_Id':row.CC_Id, 'CIT_Generation':row.CIT_Generation, 'Rat_Id':row.Rat_Id, 'CU_Reference_1':row.CU_Reference_1, 'CU_Reference_2':row.CU_Reference_2, 'CU_Reference_3':row.CU_Reference_3}
    if parent_key is not None:
       session['data'][parent_key] = parent_value

       print('parent_key  = ',parent_key)
       print('parent_value= ',parent_value)
       print('session["data"][parent_key] = %s'%(parent_key,session['data'][parent_key]))

    form = frm_charge_unit()

    if form.has_FKs:
        form.CI_Id.choices = db.session.query(configuration_item.CI_Id,configuration_item.CI_Name).order_by(configuration_item.CI_Name).all()
        form.CU_Operation.choices = db.session.query(cu_operation.CU_Operation,cu_operation.Value).order_by(cu_operation.Value).all()
        form.Typ_Code.choices = db.session.query(cu_type.Typ_Code,cu_type.Typ_Description).order_by(cu_type.Typ_Description).all()
        form.CC_Id.choices = db.session.query(cost_center.CC_Id,cost_center.CC_Description).order_by(cost_center.CC_Description).all()
        form.CIT_Generation.choices = db.session.query(cit_generation.CIT_Generation,cit_generation.Value).order_by(cit_generation.Value).all()

    if form.validate_on_submit():
        if     form.submit_Save.data:
            row.CI_Id = form.CI_Id.data
            row.CU_Description = form.CU_Description.data
            row.CU_UUID = form.CU_UUID.data
            row.CU_Is_Billeable = form.CU_Is_Billeable.data
            row.CU_Is_Always_Billeable = form.CU_Is_Always_Billeable.data
            row.CU_Quantity = form.CU_Quantity.data
            row.CU_Operation = form.CU_Operation.data
            row.Typ_Code = form.Typ_Code.data
            row.CC_Id = form.CC_Id.data
            row.CIT_Generation = form.CIT_Generation.data
            row.CU_Reference_1 = form.CU_Reference_1.data
            row.CU_Reference_2 = form.CU_Reference_2.data
            row.CU_Reference_3 = form.CU_Reference_3.data
            try:
               db.session.close()
               db.session.add(row)
               db.session.commit()
               db.session.close()
               flash('Record %s saved OK'%(CU_Id))
            except Exception as e:
               db.session.rollback()
               db.session.close()
               flash('ERROR saving record : %s'%(e))
            return redirect(url_for('.select_Charge_Units_query'))
        elif   form.submit_New.data:
            print('New Data Here...')
            db.session.close()
            row=charge_unit()
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
            pass
            pass
            pass
            pass
            return redirect(url_for('.forms_Charge_Units',CU_Id=row.CU_Id))

        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.forms_Charge_Units',CU_Id=row.CU_Id))

    form.CI_Id.data = row.CI_Id
    form.CU_Description.data = row.CU_Description
    form.CU_UUID.data = row.CU_UUID
    form.CU_Is_Billeable.data = row.CU_Is_Billeable
    form.CU_Is_Always_Billeable.data = row.CU_Is_Always_Billeable
    form.CU_Quantity.data = row.CU_Quantity
    form.CU_Operation.data = row.CU_Operation
    form.Typ_Code.data = row.Typ_Code
    form.CC_Id.data = row.CC_Id
    form.CIT_Generation.data = row.CIT_Generation
    form.CU_Reference_1.data = row.CU_Reference_1
    form.CU_Reference_2.data = row.CU_Reference_2
    form.CU_Reference_3.data = row.CU_Reference_3
    return render_template('charge_units.html', form=form, row=row)

# =============================================================================

@main.route('/forms/Charge_Units_delete', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@admin_required
def forms_Charge_Units_delete():
    """ Delete record handling function for table Charge_Units """

    logger.debug('Enter: forms_Charge_Units_delete()')
    CU_Id  =  request.args.get('CU_Id',0,type=int)
    row =  charge_unit.query.filter(charge_unit.CU_Id == CU_Id).first()
    if row is None:
        row=charge_unit()
    session['data'] =  { 'CU_Id':row.CU_Id, 'CI_Id':row.CI_Id, 'CU_Description':row.CU_Description, 'CU_UUID':row.CU_UUID, 'CU_Is_Billeable':row.CU_Is_Billeable, 'CU_Is_Always_Billeable':row.CU_Is_Always_Billeable, 'CU_Quantity':row.CU_Quantity, 'CU_Operation':row.CU_Operation, 'Typ_Code':row.Typ_Code, 'CC_Id':row.CC_Id, 'CIT_Generation':row.CIT_Generation, 'Rat_Id':row.Rat_Id, 'CU_Reference_1':row.CU_Reference_1, 'CU_Reference_2':row.CU_Reference_2, 'CU_Reference_3':row.CU_Reference_3}
    form = frm_charge_unit_delete()

    if form.validate_on_submit():
        if  form.submit_Delete.data:
            print('Delete Data Here...')
            print('Delete Data Here...')
            try:
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                flash('Record %s deleted OK'%(CU_Id))
            except exc.IntegrityError as e:
                db.session.rollback()
                flash('INTEGRITY ERROR: Are you sure there are no dependant records in other tables?')
                return redirect(url_for('.forms_Charge_Units_delete',CU_Id=session['data']['CU_Id']))

            return redirect(url_for('.select_Charge_Units_query'))
        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
            return redirect(url_for('.select_Charge_Units_query'))
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.select_Charge_Units_query'))


    return render_template('charge_units_delete.html',C=C, form=form, data=session.get('data'),row=row)

# =============================================================================

@main.route('/select/Charge_Units_Query', methods=['GET','POST'])
@login_required
@admin_required
def select_Charge_Units_query():
    """ Select rows handling function for table Charge_Units """

    logger.debug('Enter: select_Charge_Units_query()')
    field =  request.args.get('field',None,type=str)
    value =  request.args.get('value',0,type=str)
    page  =  request.args.get('page',1,type=int)

    if field is not None:
        if   field == 'CU_Id':
            rows =  charge_unit.query.filter_by(CU_Id=value)\
               .join(configuration_item,charge_unit.CI_Id == configuration_item.CI_Id).add_columns(configuration_item.CI_Name)\
               .join(cu_operation,charge_unit.CU_Operation == cu_operation.CU_Operation).add_columns(cu_operation.Value)\
               .join(cu_type,charge_unit.Typ_Code == cu_type.Typ_Code).add_columns(cu_type.Typ_Description)\
               .join(cost_center,charge_unit.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .join(cit_generation,charge_unit.CIT_Generation == cit_generation.CIT_Generation).add_columns(cit_generation.Value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CI_Id':
            rows =  charge_unit.query.filter_by(CI_Id=value)\
               .join(configuration_item,charge_unit.CI_Id == configuration_item.CI_Id).add_columns(configuration_item.CI_Name)\
               .join(cu_operation,charge_unit.CU_Operation == cu_operation.CU_Operation).add_columns(cu_operation.Value)\
               .join(cu_type,charge_unit.Typ_Code == cu_type.Typ_Code).add_columns(cu_type.Typ_Description)\
               .join(cost_center,charge_unit.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .join(cit_generation,charge_unit.CIT_Generation == cit_generation.CIT_Generation).add_columns(cit_generation.Value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CU_Description':
            rows =  charge_unit.query.filter_by(CU_Description=value)\
               .join(configuration_item,charge_unit.CI_Id == configuration_item.CI_Id).add_columns(configuration_item.CI_Name)\
               .join(cu_operation,charge_unit.CU_Operation == cu_operation.CU_Operation).add_columns(cu_operation.Value)\
               .join(cu_type,charge_unit.Typ_Code == cu_type.Typ_Code).add_columns(cu_type.Typ_Description)\
               .join(cost_center,charge_unit.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .join(cit_generation,charge_unit.CIT_Generation == cit_generation.CIT_Generation).add_columns(cit_generation.Value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CU_UUID':
            rows =  charge_unit.query.filter_by(CU_UUID=value)\
               .join(configuration_item,charge_unit.CI_Id == configuration_item.CI_Id).add_columns(configuration_item.CI_Name)\
               .join(cu_operation,charge_unit.CU_Operation == cu_operation.CU_Operation).add_columns(cu_operation.Value)\
               .join(cu_type,charge_unit.Typ_Code == cu_type.Typ_Code).add_columns(cu_type.Typ_Description)\
               .join(cost_center,charge_unit.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .join(cit_generation,charge_unit.CIT_Generation == cit_generation.CIT_Generation).add_columns(cit_generation.Value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CU_Is_Billeable':
            rows =  charge_unit.query.filter_by(CU_Is_Billeable=value)\
               .join(configuration_item,charge_unit.CI_Id == configuration_item.CI_Id).add_columns(configuration_item.CI_Name)\
               .join(cu_operation,charge_unit.CU_Operation == cu_operation.CU_Operation).add_columns(cu_operation.Value)\
               .join(cu_type,charge_unit.Typ_Code == cu_type.Typ_Code).add_columns(cu_type.Typ_Description)\
               .join(cost_center,charge_unit.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .join(cit_generation,charge_unit.CIT_Generation == cit_generation.CIT_Generation).add_columns(cit_generation.Value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CU_Is_Always_Billeable':
            rows =  charge_unit.query.filter_by(CU_Is_Always_Billeable=value)\
               .join(configuration_item,charge_unit.CI_Id == configuration_item.CI_Id).add_columns(configuration_item.CI_Name)\
               .join(cu_operation,charge_unit.CU_Operation == cu_operation.CU_Operation).add_columns(cu_operation.Value)\
               .join(cu_type,charge_unit.Typ_Code == cu_type.Typ_Code).add_columns(cu_type.Typ_Description)\
               .join(cost_center,charge_unit.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .join(cit_generation,charge_unit.CIT_Generation == cit_generation.CIT_Generation).add_columns(cit_generation.Value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CU_Quantity':
            rows =  charge_unit.query.filter_by(CU_Quantity=value)\
               .join(configuration_item,charge_unit.CI_Id == configuration_item.CI_Id).add_columns(configuration_item.CI_Name)\
               .join(cu_operation,charge_unit.CU_Operation == cu_operation.CU_Operation).add_columns(cu_operation.Value)\
               .join(cu_type,charge_unit.Typ_Code == cu_type.Typ_Code).add_columns(cu_type.Typ_Description)\
               .join(cost_center,charge_unit.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .join(cit_generation,charge_unit.CIT_Generation == cit_generation.CIT_Generation).add_columns(cit_generation.Value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CU_Operation':
            rows =  charge_unit.query.filter_by(CU_Operation=value)\
               .join(configuration_item,charge_unit.CI_Id == configuration_item.CI_Id).add_columns(configuration_item.CI_Name)\
               .join(cu_operation,charge_unit.CU_Operation == cu_operation.CU_Operation).add_columns(cu_operation.Value)\
               .join(cu_type,charge_unit.Typ_Code == cu_type.Typ_Code).add_columns(cu_type.Typ_Description)\
               .join(cost_center,charge_unit.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .join(cit_generation,charge_unit.CIT_Generation == cit_generation.CIT_Generation).add_columns(cit_generation.Value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Typ_Code':
            rows =  charge_unit.query.filter_by(Typ_Code=value)\
               .join(configuration_item,charge_unit.CI_Id == configuration_item.CI_Id).add_columns(configuration_item.CI_Name)\
               .join(cu_operation,charge_unit.CU_Operation == cu_operation.CU_Operation).add_columns(cu_operation.Value)\
               .join(cu_type,charge_unit.Typ_Code == cu_type.Typ_Code).add_columns(cu_type.Typ_Description)\
               .join(cost_center,charge_unit.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .join(cit_generation,charge_unit.CIT_Generation == cit_generation.CIT_Generation).add_columns(cit_generation.Value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CC_Id':
            rows =  charge_unit.query.filter_by(CC_Id=value)\
               .join(configuration_item,charge_unit.CI_Id == configuration_item.CI_Id).add_columns(configuration_item.CI_Name)\
               .join(cu_operation,charge_unit.CU_Operation == cu_operation.CU_Operation).add_columns(cu_operation.Value)\
               .join(cu_type,charge_unit.Typ_Code == cu_type.Typ_Code).add_columns(cu_type.Typ_Description)\
               .join(cost_center,charge_unit.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .join(cit_generation,charge_unit.CIT_Generation == cit_generation.CIT_Generation).add_columns(cit_generation.Value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CIT_Generation':
            rows =  charge_unit.query.filter_by(CIT_Generation=value)\
               .join(configuration_item,charge_unit.CI_Id == configuration_item.CI_Id).add_columns(configuration_item.CI_Name)\
               .join(cu_operation,charge_unit.CU_Operation == cu_operation.CU_Operation).add_columns(cu_operation.Value)\
               .join(cu_type,charge_unit.Typ_Code == cu_type.Typ_Code).add_columns(cu_type.Typ_Description)\
               .join(cost_center,charge_unit.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .join(cit_generation,charge_unit.CIT_Generation == cit_generation.CIT_Generation).add_columns(cit_generation.Value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Rat_Id':
            rows =  charge_unit.query.filter_by(Rat_Id=value)\
               .join(configuration_item,charge_unit.CI_Id == configuration_item.CI_Id).add_columns(configuration_item.CI_Name)\
               .join(cu_operation,charge_unit.CU_Operation == cu_operation.CU_Operation).add_columns(cu_operation.Value)\
               .join(cu_type,charge_unit.Typ_Code == cu_type.Typ_Code).add_columns(cu_type.Typ_Description)\
               .join(cost_center,charge_unit.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .join(cit_generation,charge_unit.CIT_Generation == cit_generation.CIT_Generation).add_columns(cit_generation.Value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CU_Reference_1':
            rows =  charge_unit.query.filter_by(CU_Reference_1=value)\
               .join(configuration_item,charge_unit.CI_Id == configuration_item.CI_Id).add_columns(configuration_item.CI_Name)\
               .join(cu_operation,charge_unit.CU_Operation == cu_operation.CU_Operation).add_columns(cu_operation.Value)\
               .join(cu_type,charge_unit.Typ_Code == cu_type.Typ_Code).add_columns(cu_type.Typ_Description)\
               .join(cost_center,charge_unit.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .join(cit_generation,charge_unit.CIT_Generation == cit_generation.CIT_Generation).add_columns(cit_generation.Value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CU_Reference_2':
            rows =  charge_unit.query.filter_by(CU_Reference_2=value)\
               .join(configuration_item,charge_unit.CI_Id == configuration_item.CI_Id).add_columns(configuration_item.CI_Name)\
               .join(cu_operation,charge_unit.CU_Operation == cu_operation.CU_Operation).add_columns(cu_operation.Value)\
               .join(cu_type,charge_unit.Typ_Code == cu_type.Typ_Code).add_columns(cu_type.Typ_Description)\
               .join(cost_center,charge_unit.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .join(cit_generation,charge_unit.CIT_Generation == cit_generation.CIT_Generation).add_columns(cit_generation.Value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CU_Reference_3':
            rows =  charge_unit.query.filter_by(CU_Reference_3=value)\
               .join(configuration_item,charge_unit.CI_Id == configuration_item.CI_Id).add_columns(configuration_item.CI_Name)\
               .join(cu_operation,charge_unit.CU_Operation == cu_operation.CU_Operation).add_columns(cu_operation.Value)\
               .join(cu_type,charge_unit.Typ_Code == cu_type.Typ_Code).add_columns(cu_type.Typ_Description)\
               .join(cost_center,charge_unit.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .join(cit_generation,charge_unit.CIT_Generation == cit_generation.CIT_Generation).add_columns(cit_generation.Value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
    else:
       rows =  charge_unit.query\
               .join(configuration_item,charge_unit.CI_Id == configuration_item.CI_Id).add_columns(configuration_item.CI_Name)\
               .join(cu_operation,charge_unit.CU_Operation == cu_operation.CU_Operation).add_columns(cu_operation.Value)\
               .join(cu_type,charge_unit.Typ_Code == cu_type.Typ_Code).add_columns(cu_type.Typ_Description)\
               .join(cost_center,charge_unit.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .join(cit_generation,charge_unit.CIT_Generation == cit_generation.CIT_Generation).add_columns(cit_generation.Value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)

    next_url = url_for('.select_Charge_Units_query', page=rows.next_num) \
        if rows.has_next else None
    prev_url = url_for('.select_Charge_Units_query', page=rows.prev_num) \
        if rows.has_prev else None

    return render_template('charge_units_All.html',C=C,rows=rows.items,next_url=next_url,prev_url=prev_url)
# =============================================================================

