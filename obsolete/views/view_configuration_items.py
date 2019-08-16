# =============================================================================

# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-11-30 16:47:18
# =============================================================================


@main.route('/forms/Configuration_Items', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@permission_required(Permission.MODIFY)
@admin_required
def forms_Configuration_Items():
    """ Form handling function for table Configuration_Items """

    logger.debug('Enter: forms_Configuration_Items()')
    CI_Id  =  request.args.get('CI_Id',0,type=int)
    row =  configuration_item.query.filter(configuration_item.CI_Id == CI_Id).first()
    if row is None:
        row=configuration_item()

    session['data'] =  { 'CI_Id':row.CI_Id, 'CI_Name':row.CI_Name, 'CI_UUID':row.CI_UUID, 'Pla_Id':row.Pla_Id, 'CC_Id':row.CC_Id, 'CIT_Generation':row.CIT_Generation, 'Cus_Id':row.Cus_Id}
    form = frm_configuration_item()

    if form.has_FKs:
        form.Pla_Id.choices = db.session.query(platform.Pla_Id,platform.Pla_Name).order_by(platform.Pla_Name).all()
        form.CC_Id.choices = db.session.query(cost_center.CC_Id,cost_center.CC_Description).order_by(cost_center.CC_Description).all()
        form.CIT_Generation.choices = db.session.query(cit_generation.CIT_Generation,cit_generation.Value).order_by(cit_generation.Value).all()
        form.Cus_Id.choices = db.session.query(customer.Cus_Id,customer.Cus_Name).order_by(customer.Cus_Name).all()

    if form.validate_on_submit():
        if     form.submit_Save.data:
            row.CI_Name = form.CI_Name.data
            row.CI_UUID = form.CI_UUID.data
            row.Pla_Id = form.Pla_Id.data
            row.CC_Id = form.CC_Id.data
            row.CIT_Generation = form.CIT_Generation.data
            row.Cus_Id = form.Cus_Id.data
            try:
               db.session.close()
               db.session.add(row)
               db.session.commit()
               db.session.close()
               flash('Record %s saved OK'%(CI_Id))
            except Exception as e:
               db.session.rollback()
               db.session.close()
               flash('ERROR saving record : %s'%(e))
            return redirect(url_for('.select_Configuration_Items_query'))
        elif   form.submit_New.data:
            print('New Data Here...')
            db.session.close()
            row=configuration_item()
            pass
            pass
            pass
            pass
            pass
            pass
            return redirect(url_for('.forms_Configuration_Items',CI_Id=row.CI_Id))

        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.forms_Configuration_Items',CI_Id=row.CI_Id))

    form.CI_Name.data = row.CI_Name
    form.CI_UUID.data = row.CI_UUID
    form.Pla_Id.data = row.Pla_Id
    form.CC_Id.data = row.CC_Id
    form.CIT_Generation.data = row.CIT_Generation
    form.Cus_Id.data = row.Cus_Id
    return render_template('configuration_items.html', form=form, row=row)

# =============================================================================

@main.route('/forms/Configuration_Items_delete', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@admin_required
def forms_Configuration_Items_delete():
    """ Delete record handling function for table Configuration_Items """

    logger.debug('Enter: forms_Configuration_Items_delete()')
    CI_Id  =  request.args.get('CI_Id',0,type=int)
    row =  configuration_item.query.filter(configuration_item.CI_Id == CI_Id).first()
    if row is None:
        row=configuration_item()
    session['data'] =  { 'CI_Id':row.CI_Id, 'CI_Name':row.CI_Name, 'CI_UUID':row.CI_UUID, 'Pla_Id':row.Pla_Id, 'CC_Id':row.CC_Id, 'CIT_Generation':row.CIT_Generation, 'Cus_Id':row.Cus_Id}
    form = frm_configuration_item_delete()

    if form.validate_on_submit():
        if  form.submit_Delete.data:
            print('Delete Data Here...')
            print('Delete Data Here...')
            try:
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                flash('Record %s deleted OK'%(CI_Id))
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


    return render_template('configuration_items_delete.html',C=C, form=form, data=session.get('data'),row=row)

# =============================================================================

@main.route('/select/Configuration_Items_Query', methods=['GET','POST'])
@login_required
@admin_required
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
               .join(cit_generation,configuration_item.CIT_Generation == cit_generation.CIT_Generation).add_columns(cit_generation.Value)\
               .join(customer,configuration_item.Cus_Id == customer.Cus_Id).add_columns(customer.Cus_Name)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CI_Name':
            rows =  configuration_item.query.filter_by(CI_Name=value)\
               .join(platform,configuration_item.Pla_Id == platform.Pla_Id).add_columns(platform.Pla_Name)\
               .join(cost_center,configuration_item.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .join(cit_generation,configuration_item.CIT_Generation == cit_generation.CIT_Generation).add_columns(cit_generation.Value)\
               .join(customer,configuration_item.Cus_Id == customer.Cus_Id).add_columns(customer.Cus_Name)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CI_UUID':
            rows =  configuration_item.query.filter_by(CI_UUID=value)\
               .join(platform,configuration_item.Pla_Id == platform.Pla_Id).add_columns(platform.Pla_Name)\
               .join(cost_center,configuration_item.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .join(cit_generation,configuration_item.CIT_Generation == cit_generation.CIT_Generation).add_columns(cit_generation.Value)\
               .join(customer,configuration_item.Cus_Id == customer.Cus_Id).add_columns(customer.Cus_Name)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Pla_Id':
            rows =  configuration_item.query.filter_by(Pla_Id=value)\
               .join(platform,configuration_item.Pla_Id == platform.Pla_Id).add_columns(platform.Pla_Name)\
               .join(cost_center,configuration_item.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .join(cit_generation,configuration_item.CIT_Generation == cit_generation.CIT_Generation).add_columns(cit_generation.Value)\
               .join(customer,configuration_item.Cus_Id == customer.Cus_Id).add_columns(customer.Cus_Name)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CC_Id':
            rows =  configuration_item.query.filter_by(CC_Id=value)\
               .join(platform,configuration_item.Pla_Id == platform.Pla_Id).add_columns(platform.Pla_Name)\
               .join(cost_center,configuration_item.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .join(cit_generation,configuration_item.CIT_Generation == cit_generation.CIT_Generation).add_columns(cit_generation.Value)\
               .join(customer,configuration_item.Cus_Id == customer.Cus_Id).add_columns(customer.Cus_Name)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CIT_Generation':
            rows =  configuration_item.query.filter_by(CIT_Generation=value)\
               .join(platform,configuration_item.Pla_Id == platform.Pla_Id).add_columns(platform.Pla_Name)\
               .join(cost_center,configuration_item.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .join(cit_generation,configuration_item.CIT_Generation == cit_generation.CIT_Generation).add_columns(cit_generation.Value)\
               .join(customer,configuration_item.Cus_Id == customer.Cus_Id).add_columns(customer.Cus_Name)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Cus_Id':
            rows =  configuration_item.query.filter_by(Cus_Id=value)\
               .join(platform,configuration_item.Pla_Id == platform.Pla_Id).add_columns(platform.Pla_Name)\
               .join(cost_center,configuration_item.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .join(cit_generation,configuration_item.CIT_Generation == cit_generation.CIT_Generation).add_columns(cit_generation.Value)\
               .join(customer,configuration_item.Cus_Id == customer.Cus_Id).add_columns(customer.Cus_Name)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
    else:
       rows =  configuration_item.query\
               .join(platform,configuration_item.Pla_Id == platform.Pla_Id).add_columns(platform.Pla_Name)\
               .join(cost_center,configuration_item.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .join(cit_generation,configuration_item.CIT_Generation == cit_generation.CIT_Generation).add_columns(cit_generation.Value)\
               .join(customer,configuration_item.Cus_Id == customer.Cus_Id).add_columns(customer.Cus_Name)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)

    next_url = url_for('.select_Configuration_Items_query', page=rows.next_num) \
        if rows.has_next else None
    prev_url = url_for('.select_Configuration_Items_query', page=rows.prev_num) \
        if rows.has_prev else None

    return render_template('configuration_items_All.html',C=C,rows=rows.items,next_url=next_url,prev_url=prev_url)
# =============================================================================

