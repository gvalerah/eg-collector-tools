# =============================================================================

# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-11-30 16:47:18
# =============================================================================


@main.route('/forms/Trace', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@permission_required(Permission.MODIFY)
@admin_required
def forms_Trace():
    """ Form handling function for table Trace """

    logger.debug('Enter: forms_Trace()')
    ID  =  request.args.get('ID',0,type=int)
    row =  trace.query.filter(trace.ID == ID).first()
    if row is None:
        row=trace()

    session['data'] =  { 'ID':row.ID, 'LINE':row.LINE}
    form = frm_trace()

    if form.validate_on_submit():
        if     form.submit_Save.data:
            row.LINE = form.LINE.data
            try:
               db.session.close()
               db.session.add(row)
               db.session.commit()
               db.session.close()
               flash('Record %s saved OK'%(ID))
            except Exception as e:
               db.session.rollback()
               db.session.close()
               flash('ERROR saving record : %s'%(e))
            return redirect(url_for('.select_Trace_query'))
        elif   form.submit_New.data:
            print('New Data Here...')
            db.session.close()
            row=trace()
            pass
            return redirect(url_for('.forms_Trace',ID=row.ID))

        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.forms_Trace',ID=row.ID))

    form.LINE.data = row.LINE
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
            print('Delete Data Here...')
            try:
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                flash('Record %s deleted OK'%(ID))
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


    return render_template('trace_delete.html',C=C, form=form, data=session.get('data'),row=row)

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

    next_url = url_for('.select_Trace_query', page=rows.next_num) \
        if rows.has_next else None
    prev_url = url_for('.select_Trace_query', page=rows.prev_num) \
        if rows.has_prev else None

    return render_template('trace_All.html',C=C,rows=rows.items,next_url=next_url,prev_url=prev_url)
# =============================================================================

