# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-20 18:43:44
# =============================================================================

@main.route('/forms/Rat_Periods', methods=['GET', 'POST'])
@login_required
@admin_required
def forms_Rat_Periods():
    """ Form handling function for table Rat_Periods """

    logger.debug('Enter: forms_Rat_Periods()')
    Rat_Period  =  request.args.get('Rat_Period',0,type=int)
    row =  rat_period.query.filter(rat_period.Rat_Period == Rat_Period).first()
    if row is None:
        row=rat_period()
        session['is_new_row']=True

    session['data'] =  { 'Rat_Period':row.Rat_Period, 'Value':row.Value}
    form = frm_rat_period()

    if form.validate_on_submit():
        if     form.submit_Save.data and current_user.role_id>1:
            row.Rat_Period = form.Rat_Period.data
            row.Value = form.Value.data
            try:
               session['new_row']=str(row)
               db.session.close()
               db.session.add(row)
               db.session.commit()
               if session['is_new_row']==True:
                   logger.audit ( '%s:NEW:%s' % (current_user.username,session['new_row'] ) )
                   flash('New Rate Period created OK')
               else:
                   logger.audit ( '%s:OLD:%s' % (current_user.username,session['prev_row']) )
                   logger.audit ( '%s:UPD:%s' % (current_user.username,session['new_row'] ) )
                   message=Markup('<b>Rate Period %s saved OK</b>'%(Rat_Period))
                   flash(message)
               db.session.close()
            except Exception as e:
               db.session.rollback()
               db.session.close()
               message=Markup('ERROR saving Rate Period record : %s'%(e))
               flash(message)
            return redirect(url_for('.select_Rat_Periods_query'))
        elif   form.submit_New.data and current_user.role_id>1:
            #print('New Data Here ...')
            session['is_new_row']=True
            db.session.close()
            row=rat_period()
            return redirect(url_for('.forms_Rat_Periods'))

        elif   form.submit_Cancel.data:
            #print('Cancel Data Here ... does nothing')
            message=Markup('Rate Period Record modifications discarded ...')
            flash(message)
        else:
            #print('form validated but not submited ???')
            message=Markup('<b>Rate Period data modifications not allowed for user \'%s\'. Please contact Collector\'s Administrator ...</b>'%(current_user.username))
            flash(message)
            return redirect(url_for('.forms_Rat_Periods'))

    form.Rat_Period.data = row.Rat_Period
    form.Value.data = row.Value
    session['prev_row']=str(row)
    session['is_new_row']=False
    return render_template('rat_periods.html', form=form, row=row)

# =============================================================================
@main.route('/forms/Rat_Periods_delete', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@admin_required
def forms_Rat_Periods_delete():
    """ Delete record handling function for table Rat_Periods """

    logger.debug('Enter: forms_Rat_Periods_delete()')
    Rat_Period  =  request.args.get('Rat_Period',0,type=int)
    row =  rat_period.query.filter(rat_period.Rat_Period == Rat_Period).first()
    if row is None:
        row=rat_period()
    session['data'] =  { 'Rat_Period':row.Rat_Period, 'Value':row.Value}
    form = frm_rat_period_delete()

    if form.validate_on_submit():
        if  form.submit_Delete.data:
            print('Delete Data Here...')
            try:
                session['deleted_row']=str(row)
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                logger.audit ( '%s:DEL:%s' % (current_user.username,session['deleted_row']) )
                flash('Rate Period %s deleted OK'%(Rat_Period))
            except exc.IntegrityError as e:
                db.session.rollback()
                flash('INTEGRITY ERROR: Are you sure there are no dependant records in other tables?')
                return redirect(url_for('.forms_Rat_Periods_delete',Rat_Period=session['data']['Rat_Period']))

            return redirect(url_for('.select_Rat_Periods_query'))
        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
            return redirect(url_for('.select_Rat_Periods_query'))
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.select_Rat_Periods_query'))


    return render_template('rat_periods_delete.html', form=form, data=session.get('data'),row=row)

# =============================================================================
@main.route('/select/Rat_Periods_Query', methods=['GET','POST'])
@login_required
@admin_required
def select_Rat_Periods_query():
    """ Select rows handling function for table Rat_Periods """

    logger.debug('Enter: select_Rat_Periods_query()')
    field =  request.args.get('field',None,type=str)
    value =  request.args.get('value',0,type=str)
    page  =  request.args.get('page',1,type=int)

    if field is not None:
        if   field == 'Rat_Period':
            rows =  rat_period.query.filter_by(Rat_Period=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Value':
            rows =  rat_period.query.filter_by(Value=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
    else:
       rows =  rat_period.query\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)

    if field is not None:
       next_url = url_for('.select_Rat_Periods_query', field=field, value=value, page=rows.next_num) \
           if rows.has_next else None
       prev_url = url_for('.select_Rat_Periods_query', field=field, value=value, page=rows.prev_num) \
           if rows.has_prev else None

    else:
       next_url = url_for('.select_Rat_Periods_query', page=rows.next_num) \
           if rows.has_next else None
       prev_url = url_for('.select_Rat_Periods_query', page=rows.prev_num) \
           if rows.has_prev else None

    return render_template('rat_periods_All.html',rows=rows)
# =============================================================================
