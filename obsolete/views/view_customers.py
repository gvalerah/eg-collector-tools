# =============================================================================

# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-11-30 16:47:18
# =============================================================================


@main.route('/forms/Customers', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@permission_required(Permission.MODIFY)
@admin_required
def forms_Customers():
    """ Form handling function for table Customers """

    logger.debug('Enter: forms_Customers()')
    Cus_Id  =  request.args.get('Cus_Id',0,type=int)
    row =  customer.query.filter(customer.Cus_Id == Cus_Id).first()
    if row is None:
        row=customer()

    session['data'] =  { 'Cus_Id':row.Cus_Id, 'Cus_Name':row.Cus_Name, 'CC_Id':row.CC_Id}
    form = frm_customer()

    if form.has_FKs:
        form.CC_Id.choices = db.session.query(cost_center.CC_Id,cost_center.CC_Description).order_by(cost_center.CC_Description).all()

    if form.validate_on_submit():
        if     form.submit_Save.data:
            row.Cus_Name = form.Cus_Name.data
            row.CC_Id = form.CC_Id.data
            try:
               db.session.close()
               db.session.add(row)
               db.session.commit()
               db.session.close()
               flash('Record %s saved OK'%(Cus_Id))
            except Exception as e:
               db.session.rollback()
               db.session.close()
               flash('ERROR saving record : %s'%(e))
            return redirect(url_for('.select_Customers_query'))
        elif   form.submit_New.data:
            print('New Data Here...')
            db.session.close()
            row=customer()
            pass
            pass
            return redirect(url_for('.forms_Customers',Cus_Id=row.Cus_Id))

        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.forms_Customers',Cus_Id=row.Cus_Id))

    form.Cus_Name.data = row.Cus_Name
    form.CC_Id.data = row.CC_Id
    return render_template('customers.html', form=form, row=row)

# =============================================================================

@main.route('/forms/Customers_delete', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@admin_required
def forms_Customers_delete():
    """ Delete record handling function for table Customers """

    logger.debug('Enter: forms_Customers_delete()')
    Cus_Id  =  request.args.get('Cus_Id',0,type=int)
    row =  customer.query.filter(customer.Cus_Id == Cus_Id).first()
    if row is None:
        row=customer()
    session['data'] =  { 'Cus_Id':row.Cus_Id, 'Cus_Name':row.Cus_Name, 'CC_Id':row.CC_Id}
    form = frm_customer_delete()

    if form.validate_on_submit():
        if  form.submit_Delete.data:
            print('Delete Data Here...')
            print('Delete Data Here...')
            try:
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                flash('Record %s deleted OK'%(Cus_Id))
            except exc.IntegrityError as e:
                db.session.rollback()
                flash('INTEGRITY ERROR: Are you sure there are no dependant records in other tables?')
                return redirect(url_for('.forms_Customers_delete',Cus_Id=session['data']['Cus_Id']))

            return redirect(url_for('.select_Customers_query'))
        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
            return redirect(url_for('.select_Customers_query'))
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.select_Customers_query'))


    return render_template('customers_delete.html',C=C, form=form, data=session.get('data'),row=row)

# =============================================================================

@main.route('/select/Customers_Query', methods=['GET','POST'])
@login_required
@admin_required
def select_Customers_query():
    """ Select rows handling function for table Customers """

    logger.debug('Enter: select_Customers_query()')
    field =  request.args.get('field',None,type=str)
    value =  request.args.get('value',0,type=str)
    page  =  request.args.get('page',1,type=int)

    if field is not None:
        if   field == 'Cus_Id':
            rows =  customer.query.filter_by(Cus_Id=value)\
               .join(cost_center,customer.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Cus_Name':
            rows =  customer.query.filter_by(Cus_Name=value)\
               .join(cost_center,customer.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CC_Id':
            rows =  customer.query.filter_by(CC_Id=value)\
               .join(cost_center,customer.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
    else:
       rows =  customer.query\
               .join(cost_center,customer.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)

    next_url = url_for('.select_Customers_query', page=rows.next_num) \
        if rows.has_next else None
    prev_url = url_for('.select_Customers_query', page=rows.prev_num) \
        if rows.has_prev else None

    return render_template('customers_All.html',C=C,rows=rows.items,next_url=next_url,prev_url=prev_url)
# =============================================================================

