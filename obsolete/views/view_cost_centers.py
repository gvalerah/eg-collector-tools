# =============================================================================

# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-11-30 16:47:18
# =============================================================================


@main.route('/forms/Cost_Centers', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@permission_required(Permission.MODIFY)
@admin_required
def forms_Cost_Centers():
    """ Form handling function for table Cost_Centers """

    logger.debug('Enter: forms_Cost_Centers()')
    CC_Id  =  request.args.get('CC_Id',0,type=int)
    row =  cost_center.query.filter(cost_center.CC_Id == CC_Id).first()
    if row is None:
        row=cost_center()

    session['data'] =  { 'CC_Id':row.CC_Id, 'CC_Code':row.CC_Code, 'CC_Description':row.CC_Description, 'Cur_Code':row.Cur_Code}
    form = frm_cost_center()

    if form.has_FKs:
        form.Cur_Code.choices = db.session.query(currency.Cur_Code,currency.Cur_Name).order_by(currency.Cur_Name).all()

    if form.validate_on_submit():
        if     form.submit_Save.data:
            row.CC_Code = form.CC_Code.data
            row.CC_Description = form.CC_Description.data
            row.Cur_Code = form.Cur_Code.data
            try:
               db.session.close()
               db.session.add(row)
               db.session.commit()
               db.session.close()
               flash('Record %s saved OK'%(CC_Id))
            except Exception as e:
               db.session.rollback()
               db.session.close()
               flash('ERROR saving record : %s'%(e))
            return redirect(url_for('.select_Cost_Centers_query'))
        elif   form.submit_New.data:
            print('New Data Here...')
            db.session.close()
            row=cost_center()
            pass
            pass
            pass
            return redirect(url_for('.forms_Cost_Centers',CC_Id=row.CC_Id))

        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.forms_Cost_Centers',CC_Id=row.CC_Id))

    form.CC_Code.data = row.CC_Code
    form.CC_Description.data = row.CC_Description
    form.Cur_Code.data = row.Cur_Code
    return render_template('cost_centers.html', form=form, row=row)

# =============================================================================

@main.route('/forms/Cost_Centers_delete', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@admin_required
def forms_Cost_Centers_delete():
    """ Delete record handling function for table Cost_Centers """

    logger.debug('Enter: forms_Cost_Centers_delete()')
    CC_Id  =  request.args.get('CC_Id',0,type=int)
    row =  cost_center.query.filter(cost_center.CC_Id == CC_Id).first()
    if row is None:
        row=cost_center()
    session['data'] =  { 'CC_Id':row.CC_Id, 'CC_Code':row.CC_Code, 'CC_Description':row.CC_Description, 'Cur_Code':row.Cur_Code}
    form = frm_cost_center_delete()

    if form.validate_on_submit():
        if  form.submit_Delete.data:
            print('Delete Data Here...')
            print('Delete Data Here...')
            try:
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                flash('Record %s deleted OK'%(CC_Id))
            except exc.IntegrityError as e:
                db.session.rollback()
                flash('INTEGRITY ERROR: Are you sure there are no dependant records in other tables?')
                return redirect(url_for('.forms_Cost_Centers_delete',CC_Id=session['data']['CC_Id']))

            return redirect(url_for('.select_Cost_Centers_query'))
        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
            return redirect(url_for('.select_Cost_Centers_query'))
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.select_Cost_Centers_query'))


    return render_template('cost_centers_delete.html',C=C, form=form, data=session.get('data'),row=row)

# =============================================================================

@main.route('/select/Cost_Centers_Query', methods=['GET','POST'])
@login_required
@admin_required
def select_Cost_Centers_query():
    """ Select rows handling function for table Cost_Centers """

    logger.debug('Enter: select_Cost_Centers_query()')
    field =  request.args.get('field',None,type=str)
    value =  request.args.get('value',0,type=str)
    page  =  request.args.get('page',1,type=int)

    if field is not None:
        if   field == 'CC_Id':
            rows =  cost_center.query.filter_by(CC_Id=value)\
               .join(currency,cost_center.Cur_Code == currency.Cur_Code).add_columns(currency.Cur_Name)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CC_Code':
            rows =  cost_center.query.filter_by(CC_Code=value)\
               .join(currency,cost_center.Cur_Code == currency.Cur_Code).add_columns(currency.Cur_Name)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CC_Description':
            rows =  cost_center.query.filter_by(CC_Description=value)\
               .join(currency,cost_center.Cur_Code == currency.Cur_Code).add_columns(currency.Cur_Name)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Cur_Code':
            rows =  cost_center.query.filter_by(Cur_Code=value)\
               .join(currency,cost_center.Cur_Code == currency.Cur_Code).add_columns(currency.Cur_Name)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
    else:
       rows =  cost_center.query\
               .join(currency,cost_center.Cur_Code == currency.Cur_Code).add_columns(currency.Cur_Name)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)

    next_url = url_for('.select_Cost_Centers_query', page=rows.next_num) \
        if rows.has_next else None
    prev_url = url_for('.select_Cost_Centers_query', page=rows.prev_num) \
        if rows.has_prev else None

    return render_template('cost_centers_All.html',C=C,rows=rows.items,next_url=next_url,prev_url=prev_url)
# =============================================================================

