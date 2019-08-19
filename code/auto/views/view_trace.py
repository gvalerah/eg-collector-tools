# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-18 18:05:34
# =============================================================================

@main.route('/forms/Trace', methods=['GET', 'POST'])
@login_required
@admin_required
def forms_Trace():
    """ Form handling function for table Trace """

    logger.debug('Enter: forms_Trace()')
    ID  =  request.args.get('ID',0,type=int)
    row =  trace.query.filter(trace.ID == ID).first()
    if row is None:
        row=trace()
        session['is_new_row']=True

    session['data'] =  { 'ID':row.ID, 'LINE':row.LINE}
    form = frm_trace()

    if form.validate_on_submit():
        if     form.submit_Save.data and current_user.role_id>1:
            row.LINE = form.LINE.data
            try:
               session['new_row']=str(row)
               db.session.close()
               db.session.add(row)
               db.session.commit()
               if session['is_new_row']==True:
                   logger.audit ( '%s:NEW:%s' % (current_user.username,session['new_row'] ) )
                   flash('New Trace line created OK')
               else:
                   logger.audit ( '%s:OLD:%s' % (current_user.username,session['prev_row']) )
                   logger.audit ( '%s:UPD:%s' % (current_user.username,session['new_row'] ) )
                   message=Markup('<b>Trace line %s saved OK</b>'%(ID))
                   flash(message)
               db.session.close()
            except Exception as e:
               db.session.rollback()
               db.session.close()
               message=Markup('ERROR saving Trace line record : %s'%(e))
               flash(message)
            return redirect(url_for('.select_Trace_query'))
        elif   form.submit_New.data and current_user.role_id>1:
            #print('New Data Here ...')
            session['is_new_row']=True
            db.session.close()
            row=trace()
            return redirect(url_for('.forms_Trace',ID=row.ID))

        elif   form.submit_Cancel.data:
            #print('Cancel Data Here ... does nothing')
            message=Markup('Trace line Record modifications discarded ...')
            flash(message)
        else:
            #print('form validated but not submited ???')
            message=Markup('<b>Trace line data modifications not allowed for user \'%s\'. Please contact Collector\'s Administrator ...</b>'%(current_user.username))
            flash(message)
            return redirect(url_for('.forms_Trace',ID=row.ID))

    form.LINE.data = row.LINE
    session['prev_row']=str(row)
    session['is_new_row']=False
    return render_template('trace.html', form=form, row=row)

# =============================================================================
@main.route('/forms/Trace_delete', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@admin_required
def forms_Trace_delete():
    """ Delete record handling function for table Trace """

    logger.debug('Enter: forms_Trace_delete()')
    ID  =  request.args.get('ID',0,type=int)
    row =  trace.query.filter(trace.ID == ID).first()
    if row is None:
        row=trace()
    session['data'] =  { 'ID':row.ID, 'LINE':row.LINE}
    form = frm_trace_delete()

    if form.validate_on_submit():
        if  form.submit_Delete.data:
            print('Delete Data Here...')
            try:
                session['deleted_row']=str(row)
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                logger.audit ( '%s:DEL:%s' % (current_user.username,session['deleted_row']) )
                flash('Trace line %s deleted OK'%(ID))
            except exc.IntegrityError as e:
                db.session.rollback()
                flash('INTEGRITY ERROR: Are you sure there are no dependant records in other tables?')
                return redirect(url_for('.forms_Trace_delete',ID=session['data']['ID']))

            return redirect(url_for('.select_Trace_query'))
        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
            return redirect(url_for('.select_Trace_query'))
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.select_Trace_query'))


    return render_template('trace_delete.html', form=form, data=session.get('data'),row=row)

# =============================================================================
@main.route('/select/Trace_Query', methods=['GET','POST'])
@login_required
@admin_required
def select_Trace_query():
    """ Select rows handling function for table Trace """

    logger.debug('Enter: select_Trace_query()')
    field =  request.args.get('field',None,type=str)
    value =  request.args.get('value',0,type=str)
    page  =  request.args.get('page',1,type=int)

    if field is not None:
        if   field == 'ID':
            rows =  trace.query.filter_by(ID=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'LINE':
            rows =  trace.query.filter_by(LINE=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
    else:
       rows =  trace.query\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)

    if field is not None:
       next_url = url_for('.select_Trace_query', field=field, value=value, page=rows.next_num) \
           if rows.has_next else None
       prev_url = url_for('.select_Trace_query', field=field, value=value, page=rows.prev_num) \
           if rows.has_prev else None

    else:
       next_url = url_for('.select_Trace_query', page=rows.next_num) \
           if rows.has_next else None
       prev_url = url_for('.select_Trace_query', page=rows.prev_num) \
           if rows.has_prev else None

    return render_template('trace_All.html',rows=rows)
# =============================================================================
