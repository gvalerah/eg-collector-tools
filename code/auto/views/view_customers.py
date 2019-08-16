# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-16 15:51:37
# =============================================================================

@main.route('/forms/Customers', methods=['GET', 'POST'])
@login_required
@admin_required
def forms_Customers():
    """ Form handling function for table Customers """

    logger.debug('Enter: forms_Customers()')
    Cus_Id  =  request.args.get('Cus_Id',0,type=int)
    row =  customer.query.filter(customer.Cus_Id == Cus_Id).first()
    if row is None:
        row=customer()
        session['is_new_row']=True

    session['data'] =  { 'Cus_Id':row.Cus_Id, 'Cus_Name':row.Cus_Name, 'CC_Id':row.CC_Id}
    form = frm_customer()

    if form.has_FKs:
        form.CC_Id.choices = db.session.query(cost_center.CC_Id,cost_center.CC_Description).order_by(cost_center.CC_Description).all()

    if form.validate_on_submit():
        if     form.submit_Save.data and current_user.role_id>1:
            row.Cus_Name = form.Cus_Name.data
            row.CC_Id = form.CC_Id.data
            try:
               session['new_row']=str(row)
               db.session.close()
               db.session.add(row)
               db.session.commit()
               if session['is_new_row']==True:
                   logger.audit ( '%s:NEW:%s' % (current_user.username,session['new_row'] ) )
                   flash('New Customer created OK')
               else:
                   logger.audit ( '%s:OLD:%s' % (current_user.username,session['prev_row']) )
                   logger.audit ( '%s:UPD:%s' % (current_user.username,session['new_row'] ) )
                   message=Markup('<b>Customer %s saved OK</b>'%(Cus_Id))
                   flash(message)
               db.session.close()
            except Exception as e:
               db.session.rollback()
               db.session.close()
               message=Markup('ERROR saving Customer record : %s'%(e))
               flash(message)
            return redirect(url_for('.select_Customers_query'))
        elif   form.submit_New.data and current_user.role_id>1:
            #print('New Data Here ...')
            session['is_new_row']=True
            db.session.close()
            row=customer()
            return redirect(url_for('.forms_Customers',Cus_Id=row.Cus_Id))

        elif   form.submit_Cancel.data:
            #print('Cancel Data Here ... does nothing')
            message=Markup('Customer Record modifications discarded ...')
            flash(message)
        else:
            #print('form validated but not submited ???')
            message=Markup('<b>Customer data modifications not allowed for user \'%s\'. Please contact Collector\'s Administrator ...</b>'%(current_user.username))
            flash(message)
            return redirect(url_for('.forms_Customers',Cus_Id=row.Cus_Id))

    form.Cus_Name.data = row.Cus_Name
    form.CC_Id.data = row.CC_Id
    session['prev_row']=str(row)
    session['is_new_row']=False
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
            try:
                session['deleted_row']=str(row)
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                logger.audit ( '%s:DEL:%s' % (current_user.username,session['deleted_row']) )
                flash('Customer %s deleted OK'%(Cus_Id))
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


    return render_template('customers_delete.html', form=form, data=session.get('data'),row=row)

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

    if field is not None:
       next_url = url_for('.select_Customers_query', field=field, value=value, page=rows.next_num) \
           if rows.has_next else None
       prev_url = url_for('.select_Customers_query', field=field, value=value, page=rows.prev_num) \
           if rows.has_prev else None

    else:
       next_url = url_for('.select_Customers_query', page=rows.next_num) \
           if rows.has_next else None
       prev_url = url_for('.select_Customers_query', page=rows.prev_num) \
           if rows.has_prev else None

    return render_template('customers_All.html',rows=rows)
# =============================================================================
