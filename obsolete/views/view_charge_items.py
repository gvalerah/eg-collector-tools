# =============================================================================

# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-11-30 16:47:18
# =============================================================================


@main.route('/forms/Charge_Items', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@permission_required(Permission.MODIFY)
@admin_required
def forms_Charge_Items():
    """ Form handling function for table Charge_Items """

    logger.debug('Enter: forms_Charge_Items()')
    CU_Id  =  request.args.get('CU_Id',0,type=int)
    CIT_Date  =  request.args.get('CIT_Date',0,type=int)
    CIT_Time  =  request.args.get('CIT_Time',0,type=int)
    parent_key  =  request.args.get('parent_key',None,type=str)
    parent_value=  request.args.get('parent_value',0,type=int)

    row =  charge_item.query.filter(charge_item.CU_Id == CU_Id,charge_item.CIT_Date == CIT_Date,charge_item.CIT_Time == CIT_Time).first()
    if row is None:
        row=charge_item()

    session['data'] =  { 'CU_Id':row.CU_Id, 'CIT_Date':row.CIT_Date, 'CIT_Time':str(row.CIT_Time), 'CIT_Quantity':row.CIT_Quantity, 'CIT_Status':row.CIT_Status, 'CIT_Is_Active':row.CIT_Is_Active}
    if parent_key is not None:
       session['data'][parent_key] = parent_value

       print('parent_key  = ',parent_key)
       print('parent_value= ',parent_value)
       print('session["data"][parent_key] = %s'%(parent_key,session['data'][parent_key]))

    form = frm_charge_item()

    if form.has_FKs:
        form.CU_Id.choices = db.session.query(charge_unit.CU_Id,charge_unit.CU_Description).order_by(charge_unit.CU_Description).all()
        form.CIT_Status.choices = db.session.query(cit_status.CIT_Status,cit_status.Value).order_by(cit_status.Value).all()

    if form.validate_on_submit():
        if     form.submit_Save.data:
            row.CU_Id = form.CU_Id.data
            row.CIT_Date = form.CIT_Date.data
            row.CIT_Time = form.CIT_Time.data
            row.CIT_Quantity = form.CIT_Quantity.data
            row.CIT_Status = form.CIT_Status.data
            row.CIT_Is_Active = form.CIT_Is_Active.data
            try:
               db.session.close()
               db.session.add(row)
               db.session.commit()
               db.session.close()
               flash('Record %s saved OK'%(CU_Id,CIT_Date,CIT_Time))
            except Exception as e:
               db.session.rollback()
               db.session.close()
               flash('ERROR saving record : %s'%(e))
            return redirect(url_for('.select_Charge_Items_query'))
        elif   form.submit_New.data:
            print('New Data Here...')
            db.session.close()
            row=charge_item()
            return redirect(url_for('.forms_Charge_Items'))

        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.forms_Charge_Items'))

    form.CU_Id.data = row.CU_Id
    form.CIT_Date.data = row.CIT_Date
    form.CIT_Time.data = row.CIT_Time
    form.CIT_Quantity.data = row.CIT_Quantity
    form.CIT_Status.data = row.CIT_Status
    form.CIT_Is_Active.data = row.CIT_Is_Active
    return render_template('charge_items.html', form=form, row=row)

# =============================================================================

@main.route('/forms/Charge_Items_delete', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@admin_required
def forms_Charge_Items_delete():
    """ Delete record handling function for table Charge_Items """

    logger.debug('Enter: forms_Charge_Items_delete()')
    CU_Id  =  request.args.get('CU_Id',0,type=int)
    CIT_Date  =  request.args.get('CIT_Date',0,type=int)
    CIT_Time  =  request.args.get('CIT_Time',0,type=int)
    row =  charge_item.query.filter(charge_item.CU_Id == CU_Id,charge_item.CIT_Date == CIT_Date,charge_item.CIT_Time == CIT_Time).first()
    if row is None:
        row=charge_item()
    session['data'] =  { 'CU_Id':row.CU_Id, 'CIT_Date':row.CIT_Date, 'CIT_Time':str(row.CIT_Time), 'CIT_Quantity':row.CIT_Quantity, 'CIT_Status':row.CIT_Status, 'CIT_Is_Active':row.CIT_Is_Active}
    form = frm_charge_item_delete()

    if form.validate_on_submit():
        if  form.submit_Delete.data:
            print('Delete Data Here...')
            print('Delete Data Here...')
            try:
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                flash('Record %s deleted OK'%(CU_Id,CIT_Date,CIT_Time))
            except exc.IntegrityError as e:
                db.session.rollback()
                flash('INTEGRITY ERROR: Are you sure there are no dependant records in other tables?')
                return redirect(url_for('.forms_Charge_Items_delete',CU_Id=session['data']['CU_Id'],CIT_Date=session['data']['CIT_Date'],CIT_Time=session['data']['CIT_Time']))

            return redirect(url_for('.select_Charge_Items_query'))
        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
            return redirect(url_for('.select_Charge_Items_query'))
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.select_Charge_Items_query'))


    return render_template('charge_items_delete.html',C=C, form=form, data=session.get('data'),row=row)

# =============================================================================

@main.route('/select/Charge_Items_Query', methods=['GET','POST'])
@login_required
@admin_required
def select_Charge_Items_query():
    """ Select rows handling function for table Charge_Items """

    logger.debug('Enter: select_Charge_Items_query()')
    field =  request.args.get('field',None,type=str)
    value =  request.args.get('value',0,type=str)
    page  =  request.args.get('page',1,type=int)

    if field is not None:
        if   field == 'CU_Id':
            rows =  charge_item.query.filter_by(CU_Id=value)\
               .join(charge_unit,charge_item.CU_Id == charge_unit.CU_Id).add_columns(charge_unit.CU_Description)\
               .join(cit_status,charge_item.CIT_Status == cit_status.CIT_Status).add_columns(cit_status.Value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CIT_Date':
            rows =  charge_item.query.filter_by(CIT_Date=value)\
               .join(charge_unit,charge_item.CU_Id == charge_unit.CU_Id).add_columns(charge_unit.CU_Description)\
               .join(cit_status,charge_item.CIT_Status == cit_status.CIT_Status).add_columns(cit_status.Value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CIT_Time':
            rows =  charge_item.query.filter_by(CIT_Time=value)\
               .join(charge_unit,charge_item.CU_Id == charge_unit.CU_Id).add_columns(charge_unit.CU_Description)\
               .join(cit_status,charge_item.CIT_Status == cit_status.CIT_Status).add_columns(cit_status.Value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CIT_Quantity':
            rows =  charge_item.query.filter_by(CIT_Quantity=value)\
               .join(charge_unit,charge_item.CU_Id == charge_unit.CU_Id).add_columns(charge_unit.CU_Description)\
               .join(cit_status,charge_item.CIT_Status == cit_status.CIT_Status).add_columns(cit_status.Value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CIT_Status':
            rows =  charge_item.query.filter_by(CIT_Status=value)\
               .join(charge_unit,charge_item.CU_Id == charge_unit.CU_Id).add_columns(charge_unit.CU_Description)\
               .join(cit_status,charge_item.CIT_Status == cit_status.CIT_Status).add_columns(cit_status.Value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CIT_Is_Active':
            rows =  charge_item.query.filter_by(CIT_Is_Active=value)\
               .join(charge_unit,charge_item.CU_Id == charge_unit.CU_Id).add_columns(charge_unit.CU_Description)\
               .join(cit_status,charge_item.CIT_Status == cit_status.CIT_Status).add_columns(cit_status.Value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
    else:
       rows =  charge_item.query\
               .join(charge_unit,charge_item.CU_Id == charge_unit.CU_Id).add_columns(charge_unit.CU_Description)\
               .join(cit_status,charge_item.CIT_Status == cit_status.CIT_Status).add_columns(cit_status.Value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)

    next_url = url_for('.select_Charge_Items_query', page=rows.next_num) \
        if rows.has_next else None
    prev_url = url_for('.select_Charge_Items_query', page=rows.prev_num) \
        if rows.has_prev else None

    return render_template('charge_items_All.html',C=C,rows=rows.items,next_url=next_url,prev_url=prev_url)
# =============================================================================

