# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-18 18:05:34
# =============================================================================

@main.route('/forms/Configuration_Items', methods=['GET', 'POST'])
@login_required
def forms_Configuration_Items():
    """ Form handling function for table Configuration_Items """

    logger.debug('Enter: forms_Configuration_Items()')
    CI_Id  =  request.args.get('CI_Id',0,type=int)
    row =  configuration_item.query.filter(configuration_item.CI_Id == CI_Id).first()
    if row is None:
        row=configuration_item()
        session['is_new_row']=True

    session['data'] =  { 'CI_Id':row.CI_Id, 'CI_Name':row.CI_Name, 'CI_UUID':row.CI_UUID, 'Pla_Id':row.Pla_Id, 'CC_Id':row.CC_Id, 'Cus_Id':row.Cus_Id, 'CI_Commissioning_DateTime':row.CI_Commissioning_DateTime, 'CI_Decommissioning_DateTime':row.CI_Decommissioning_DateTime}
    form = frm_configuration_item()

    if form.has_FKs:
        form.Pla_Id.choices = db.session.query(platform.Pla_Id,platform.Pla_Name).order_by(platform.Pla_Name).all()
        form.CC_Id.choices = db.session.query(cost_center.CC_Id,cost_center.CC_Description).order_by(cost_center.CC_Description).all()
        form.Cus_Id.choices = db.session.query(customer.Cus_Id,customer.Cus_Name).order_by(customer.Cus_Name).all()

    if form.validate_on_submit():
        if     form.submit_Save.data and current_user.role_id>1:
            row.CI_Name = form.CI_Name.data
            row.CI_UUID = form.CI_UUID.data
            row.Pla_Id = form.Pla_Id.data
            row.CC_Id = form.CC_Id.data
            row.Cus_Id = form.Cus_Id.data
            row.CI_Commissioning_DateTime = form.CI_Commissioning_DateTime.data
            row.CI_Decommissioning_DateTime = form.CI_Decommissioning_DateTime.data
            try:
               session['new_row']=str(row)
               db.session.close()
               db.session.add(row)
               db.session.commit()
               if session['is_new_row']==True:
                   logger.audit ( '%s:NEW:%s' % (current_user.username,session['new_row'] ) )
                   flash('New Configuration Item created OK')
               else:
                   logger.audit ( '%s:OLD:%s' % (current_user.username,session['prev_row']) )
                   logger.audit ( '%s:UPD:%s' % (current_user.username,session['new_row'] ) )
                   message=Markup('<b>Configuration Item %s saved OK</b>'%(CI_Id))
                   flash(message)
               db.session.close()
            except Exception as e:
               db.session.rollback()
               db.session.close()
               message=Markup('ERROR saving Configuration Item record : %s'%(e))
               flash(message)
            return redirect(url_for('.select_Configuration_Items_query'))
        elif   form.submit_New.data and current_user.role_id>1:
            #print('New Data Here ...')
            session['is_new_row']=True
            db.session.close()
            row=configuration_item()
            return redirect(url_for('.forms_Configuration_Items',CI_Id=row.CI_Id))

        elif   form.submit_Cancel.data:
            #print('Cancel Data Here ... does nothing')
            message=Markup('Configuration Item Record modifications discarded ...')
            flash(message)
        else:
            #print('form validated but not submited ???')
            message=Markup('<b>Configuration Item data modifications not allowed for user \'%s\'. Please contact Collector\'s Administrator ...</b>'%(current_user.username))
            flash(message)
            return redirect(url_for('.forms_Configuration_Items',CI_Id=row.CI_Id))

    form.CI_Name.data = row.CI_Name
    form.CI_UUID.data = row.CI_UUID
    form.Pla_Id.data = row.Pla_Id
    form.CC_Id.data = row.CC_Id
    form.Cus_Id.data = row.Cus_Id
    form.CI_Commissioning_DateTime.data = row.CI_Commissioning_DateTime
    form.CI_Decommissioning_DateTime.data = row.CI_Decommissioning_DateTime
    session['prev_row']=str(row)
    session['is_new_row']=False
    return render_template('configuration_items.html', form=form, row=row)

# =============================================================================
@main.route('/forms/Configuration_Items_delete', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
def forms_Configuration_Items_delete():
    """ Delete record handling function for table Configuration_Items """

    logger.debug('Enter: forms_Configuration_Items_delete()')
    CI_Id  =  request.args.get('CI_Id',0,type=int)
    row =  configuration_item.query.filter(configuration_item.CI_Id == CI_Id).first()
    if row is None:
        row=configuration_item()
    session['data'] =  { 'CI_Id':row.CI_Id, 'CI_Name':row.CI_Name, 'CI_UUID':row.CI_UUID, 'Pla_Id':row.Pla_Id, 'CC_Id':row.CC_Id, 'Cus_Id':row.Cus_Id, 'CI_Commissioning_DateTime':row.CI_Commissioning_DateTime, 'CI_Decommissioning_DateTime':row.CI_Decommissioning_DateTime}
    form = frm_configuration_item_delete()

    if form.validate_on_submit():
        if  form.submit_Delete.data:
            print('Delete Data Here...')
            try:
                session['deleted_row']=str(row)
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                logger.audit ( '%s:DEL:%s' % (current_user.username,session['deleted_row']) )
                flash('Configuration Item %s deleted OK'%(CI_Id))
            except exc.IntegrityError as e:
                db.session.rollback()
                flash('INTEGRITY ERROR: Are you sure there are no dependant records in other tables?')
                return redirect(url_for('.forms_Configuration_Items_delete',CI_Id=session['data']['CI_Id']))

            return redirect(url_for('.select_Configuration_Items_query'))
        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
            return redirect(url_for('.select_Configuration_Items_query'))
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.select_Configuration_Items_query'))


    return render_template('configuration_items_delete.html', form=form, data=session.get('data'),row=row)

# =============================================================================
@main.route('/select/Configuration_Items_Query', methods=['GET','POST'])
@login_required
def select_Configuration_Items_query():
    """ Select rows handling function for table Configuration_Items """

    logger.debug('Enter: select_Configuration_Items_query()')
    field =  request.args.get('field',None,type=str)
    value =  request.args.get('value',0,type=str)
    page  =  request.args.get('page',1,type=int)

    if field is not None:
        if   field == 'CI_Id':
            rows =  configuration_item.query.filter_by(CI_Id=value)\
               .join(platform,configuration_item.Pla_Id == platform.Pla_Id).add_columns(platform.Pla_Name)\
               .join(cost_center,configuration_item.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .join(customer,configuration_item.Cus_Id == customer.Cus_Id).add_columns(customer.Cus_Name)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CI_Name':
            rows =  configuration_item.query.filter_by(CI_Name=value)\
               .join(platform,configuration_item.Pla_Id == platform.Pla_Id).add_columns(platform.Pla_Name)\
               .join(cost_center,configuration_item.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .join(customer,configuration_item.Cus_Id == customer.Cus_Id).add_columns(customer.Cus_Name)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CI_UUID':
            rows =  configuration_item.query.filter_by(CI_UUID=value)\
               .join(platform,configuration_item.Pla_Id == platform.Pla_Id).add_columns(platform.Pla_Name)\
               .join(cost_center,configuration_item.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .join(customer,configuration_item.Cus_Id == customer.Cus_Id).add_columns(customer.Cus_Name)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Pla_Id':
            rows =  configuration_item.query.filter_by(Pla_Id=value)\
               .join(platform,configuration_item.Pla_Id == platform.Pla_Id).add_columns(platform.Pla_Name)\
               .join(cost_center,configuration_item.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .join(customer,configuration_item.Cus_Id == customer.Cus_Id).add_columns(customer.Cus_Name)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CC_Id':
            rows =  configuration_item.query.filter_by(CC_Id=value)\
               .join(platform,configuration_item.Pla_Id == platform.Pla_Id).add_columns(platform.Pla_Name)\
               .join(cost_center,configuration_item.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .join(customer,configuration_item.Cus_Id == customer.Cus_Id).add_columns(customer.Cus_Name)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Cus_Id':
            rows =  configuration_item.query.filter_by(Cus_Id=value)\
               .join(platform,configuration_item.Pla_Id == platform.Pla_Id).add_columns(platform.Pla_Name)\
               .join(cost_center,configuration_item.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .join(customer,configuration_item.Cus_Id == customer.Cus_Id).add_columns(customer.Cus_Name)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CI_Commissioning_DateTime':
            rows =  configuration_item.query.filter_by(CI_Commissioning_DateTime=value)\
               .join(platform,configuration_item.Pla_Id == platform.Pla_Id).add_columns(platform.Pla_Name)\
               .join(cost_center,configuration_item.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .join(customer,configuration_item.Cus_Id == customer.Cus_Id).add_columns(customer.Cus_Name)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CI_Decommissioning_DateTime':
            rows =  configuration_item.query.filter_by(CI_Decommissioning_DateTime=value)\
               .join(platform,configuration_item.Pla_Id == platform.Pla_Id).add_columns(platform.Pla_Name)\
               .join(cost_center,configuration_item.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .join(customer,configuration_item.Cus_Id == customer.Cus_Id).add_columns(customer.Cus_Name)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
    else:
       rows =  configuration_item.query\
               .join(platform,configuration_item.Pla_Id == platform.Pla_Id).add_columns(platform.Pla_Name)\
               .join(cost_center,configuration_item.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .join(customer,configuration_item.Cus_Id == customer.Cus_Id).add_columns(customer.Cus_Name)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)

    if field is not None:
       next_url = url_for('.select_Configuration_Items_query', field=field, value=value, page=rows.next_num) \
           if rows.has_next else None
       prev_url = url_for('.select_Configuration_Items_query', field=field, value=value, page=rows.prev_num) \
           if rows.has_prev else None

    else:
       next_url = url_for('.select_Configuration_Items_query', page=rows.next_num) \
           if rows.has_next else None
       prev_url = url_for('.select_Configuration_Items_query', page=rows.prev_num) \
           if rows.has_prev else None

    return render_template('configuration_items_All.html',rows=rows)
# =============================================================================
