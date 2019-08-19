# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-18 18:05:34
# =============================================================================

@main.route('/forms/CIT_Statuses', methods=['GET', 'POST'])
@login_required
@admin_required
def forms_CIT_Statuses():
    """ Form handling function for table CIT_Statuses """

    logger.debug('Enter: forms_CIT_Statuses()')
    CIT_Status  =  request.args.get('CIT_Status',0,type=int)
    row =  cit_status.query.filter(cit_status.CIT_Status == CIT_Status).first()
    if row is None:
        row=cit_status()
        session['is_new_row']=True

    session['data'] =  { 'CIT_Status':row.CIT_Status, 'Value':row.Value}
    form = frm_cit_status()

    if form.validate_on_submit():
        if     form.submit_Save.data and current_user.role_id>1:
            row.CIT_Status = form.CIT_Status.data
            row.Value = form.Value.data
            try:
               session['new_row']=str(row)
               db.session.close()
               db.session.add(row)
               db.session.commit()
               if session['is_new_row']==True:
                   logger.audit ( '%s:NEW:%s' % (current_user.username,session['new_row'] ) )
                   flash('New Configuration Item Status Type created OK')
               else:
                   logger.audit ( '%s:OLD:%s' % (current_user.username,session['prev_row']) )
                   logger.audit ( '%s:UPD:%s' % (current_user.username,session['new_row'] ) )
                   message=Markup('<b>Configuration Item Status Type %s saved OK</b>'%(CIT_Status))
                   flash(message)
               db.session.close()
            except Exception as e:
               db.session.rollback()
               db.session.close()
               message=Markup('ERROR saving Configuration Item Status Type record : %s'%(e))
               flash(message)
            return redirect(url_for('.select_CIT_Statuses_query'))
        elif   form.submit_New.data and current_user.role_id>1:
            #print('New Data Here ...')
            session['is_new_row']=True
            db.session.close()
            row=cit_status()
            return redirect(url_for('.forms_CIT_Statuses'))

        elif   form.submit_Cancel.data:
            #print('Cancel Data Here ... does nothing')
            message=Markup('Configuration Item Status Type Record modifications discarded ...')
            flash(message)
        else:
            #print('form validated but not submited ???')
            message=Markup('<b>Configuration Item Status Type data modifications not allowed for user \'%s\'. Please contact Collector\'s Administrator ...</b>'%(current_user.username))
            flash(message)
            return redirect(url_for('.forms_CIT_Statuses'))

    form.CIT_Status.data = row.CIT_Status
    form.Value.data = row.Value
    session['prev_row']=str(row)
    session['is_new_row']=False
    return render_template('cit_statuses.html', form=form, row=row)

# =============================================================================
@main.route('/forms/CIT_Statuses_delete', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@admin_required
def forms_CIT_Statuses_delete():
    """ Delete record handling function for table CIT_Statuses """

    logger.debug('Enter: forms_CIT_Statuses_delete()')
    CIT_Status  =  request.args.get('CIT_Status',0,type=int)
    row =  cit_status.query.filter(cit_status.CIT_Status == CIT_Status).first()
    if row is None:
        row=cit_status()
    session['data'] =  { 'CIT_Status':row.CIT_Status, 'Value':row.Value}
    form = frm_cit_status_delete()

    if form.validate_on_submit():
        if  form.submit_Delete.data:
            print('Delete Data Here...')
            try:
                session['deleted_row']=str(row)
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                logger.audit ( '%s:DEL:%s' % (current_user.username,session['deleted_row']) )
                flash('Configuration Item Status Type %s deleted OK'%(CIT_Status))
            except exc.IntegrityError as e:
                db.session.rollback()
                flash('INTEGRITY ERROR: Are you sure there are no dependant records in other tables?')
                return redirect(url_for('.forms_CIT_Statuses_delete',CIT_Status=session['data']['CIT_Status']))

            return redirect(url_for('.select_CIT_Statuses_query'))
        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
            return redirect(url_for('.select_CIT_Statuses_query'))
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.select_CIT_Statuses_query'))


    return render_template('cit_statuses_delete.html', form=form, data=session.get('data'),row=row)

# =============================================================================
@main.route('/select/CIT_Statuses_Query', methods=['GET','POST'])
@login_required
@admin_required
def select_CIT_Statuses_query():
    """ Select rows handling function for table CIT_Statuses """

    logger.debug('Enter: select_CIT_Statuses_query()')
    field =  request.args.get('field',None,type=str)
    value =  request.args.get('value',0,type=str)
    page  =  request.args.get('page',1,type=int)

    if field is not None:
        if   field == 'CIT_Status':
            rows =  cit_status.query.filter_by(CIT_Status=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Value':
            rows =  cit_status.query.filter_by(Value=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
    else:
       rows =  cit_status.query\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)

    if field is not None:
       next_url = url_for('.select_CIT_Statuses_query', field=field, value=value, page=rows.next_num) \
           if rows.has_next else None
       prev_url = url_for('.select_CIT_Statuses_query', field=field, value=value, page=rows.prev_num) \
           if rows.has_prev else None

    else:
       next_url = url_for('.select_CIT_Statuses_query', page=rows.next_num) \
           if rows.has_next else None
       prev_url = url_for('.select_CIT_Statuses_query', page=rows.prev_num) \
           if rows.has_prev else None

    return render_template('cit_statuses_All.html',rows=rows)
# =============================================================================
