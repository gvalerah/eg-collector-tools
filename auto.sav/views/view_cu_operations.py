# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-20 18:43:44
# =============================================================================

@main.route('/forms/CU_Operations', methods=['GET', 'POST'])
@login_required
@admin_required
def forms_CU_Operations():
    """ Form handling function for table CU_Operations """

    logger.debug('Enter: forms_CU_Operations()')
    CU_Operation  =  request.args.get('CU_Operation',0,type=int)
    row =  cu_operation.query.filter(cu_operation.CU_Operation == CU_Operation).first()
    if row is None:
        row=cu_operation()
        session['is_new_row']=True

    session['data'] =  { 'CU_Operation':row.CU_Operation, 'Value':row.Value, 'Is_Multiply':row.Is_Multiply, 'Factor':row.Factor}
    form = frm_cu_operation()

    if form.validate_on_submit():
        if     form.submit_Save.data and current_user.role_id>1:
            row.CU_Operation = form.CU_Operation.data
            row.Value = form.Value.data
            row.Is_Multiply = form.Is_Multiply.data
            row.Factor = form.Factor.data
            try:
               session['new_row']=str(row)
               db.session.close()
               db.session.add(row)
               db.session.commit()
               if session['is_new_row']==True:
                   logger.audit ( '%s:NEW:%s' % (current_user.username,session['new_row'] ) )
                   flash('New Charge Unit Conversion Operation created OK')
               else:
                   logger.audit ( '%s:OLD:%s' % (current_user.username,session['prev_row']) )
                   logger.audit ( '%s:UPD:%s' % (current_user.username,session['new_row'] ) )
                   message=Markup('<b>Charge Unit Conversion Operation %s saved OK</b>'%(CU_Operation))
                   flash(message)
               db.session.close()
            except Exception as e:
               db.session.rollback()
               db.session.close()
               message=Markup('ERROR saving Charge Unit Conversion Operation record : %s'%(e))
               flash(message)
            return redirect(url_for('.select_CU_Operations_query'))
        elif   form.submit_New.data and current_user.role_id>1:
            #print('New Data Here ...')
            session['is_new_row']=True
            db.session.close()
            row=cu_operation()
            return redirect(url_for('.forms_CU_Operations'))

        elif   form.submit_Cancel.data:
            #print('Cancel Data Here ... does nothing')
            message=Markup('Charge Unit Conversion Operation Record modifications discarded ...')
            flash(message)
        else:
            #print('form validated but not submited ???')
            message=Markup('<b>Charge Unit Conversion Operation data modifications not allowed for user \'%s\'. Please contact Collector\'s Administrator ...</b>'%(current_user.username))
            flash(message)
            return redirect(url_for('.forms_CU_Operations'))

    form.CU_Operation.data = row.CU_Operation
    form.Value.data = row.Value
    form.Is_Multiply.data = row.Is_Multiply
    form.Factor.data = row.Factor
    session['prev_row']=str(row)
    session['is_new_row']=False
    return render_template('cu_operations.html', form=form, row=row)

# =============================================================================
@main.route('/forms/CU_Operations_delete', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@admin_required
def forms_CU_Operations_delete():
    """ Delete record handling function for table CU_Operations """

    logger.debug('Enter: forms_CU_Operations_delete()')
    CU_Operation  =  request.args.get('CU_Operation',0,type=int)
    row =  cu_operation.query.filter(cu_operation.CU_Operation == CU_Operation).first()
    if row is None:
        row=cu_operation()
    session['data'] =  { 'CU_Operation':row.CU_Operation, 'Value':row.Value, 'Is_Multiply':row.Is_Multiply, 'Factor':row.Factor}
    form = frm_cu_operation_delete()

    if form.validate_on_submit():
        if  form.submit_Delete.data:
            print('Delete Data Here...')
            try:
                session['deleted_row']=str(row)
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                logger.audit ( '%s:DEL:%s' % (current_user.username,session['deleted_row']) )
                flash('Charge Unit Conversion Operation %s deleted OK'%(CU_Operation))
            except exc.IntegrityError as e:
                db.session.rollback()
                flash('INTEGRITY ERROR: Are you sure there are no dependant records in other tables?')
                return redirect(url_for('.forms_CU_Operations_delete',CU_Operation=session['data']['CU_Operation']))

            return redirect(url_for('.select_CU_Operations_query'))
        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
            return redirect(url_for('.select_CU_Operations_query'))
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.select_CU_Operations_query'))


    return render_template('cu_operations_delete.html', form=form, data=session.get('data'),row=row)

# =============================================================================
@main.route('/select/CU_Operations_Query', methods=['GET','POST'])
@login_required
@admin_required
def select_CU_Operations_query():
    """ Select rows handling function for table CU_Operations """

    logger.debug('Enter: select_CU_Operations_query()')
    field =  request.args.get('field',None,type=str)
    value =  request.args.get('value',0,type=str)
    page  =  request.args.get('page',1,type=int)

    if field is not None:
        if   field == 'CU_Operation':
            rows =  cu_operation.query.filter_by(CU_Operation=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Value':
            rows =  cu_operation.query.filter_by(Value=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Is_Multiply':
            rows =  cu_operation.query.filter_by(Is_Multiply=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Factor':
            rows =  cu_operation.query.filter_by(Factor=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
    else:
       rows =  cu_operation.query\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)

    if field is not None:
       next_url = url_for('.select_CU_Operations_query', field=field, value=value, page=rows.next_num) \
           if rows.has_next else None
       prev_url = url_for('.select_CU_Operations_query', field=field, value=value, page=rows.prev_num) \
           if rows.has_prev else None

    else:
       next_url = url_for('.select_CU_Operations_query', page=rows.next_num) \
           if rows.has_next else None
       prev_url = url_for('.select_CU_Operations_query', page=rows.prev_num) \
           if rows.has_prev else None

    return render_template('cu_operations_All.html',rows=rows)
# =============================================================================
