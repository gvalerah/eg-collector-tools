# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-16 15:51:37
# =============================================================================

@main.route('/forms/Platforms', methods=['GET', 'POST'])
@login_required
@admin_required
def forms_Platforms():
    """ Form handling function for table Platforms """

    logger.debug('Enter: forms_Platforms()')
    Pla_Id  =  request.args.get('Pla_Id',0,type=int)
    row =  platform.query.filter(platform.Pla_Id == Pla_Id).first()
    if row is None:
        row=platform()
        session['is_new_row']=True

    session['data'] =  { 'Pla_Id':row.Pla_Id, 'Pla_Name':row.Pla_Name, 'Pla_Host':row.Pla_Host, 'Pla_Port':row.Pla_Port, 'Pla_User':row.Pla_User, 'Pla_Password':row.Pla_Password}
    form = frm_platform()

    if form.validate_on_submit():
        if     form.submit_Save.data and current_user.role_id>1:
            row.Pla_Name = form.Pla_Name.data
            row.Pla_Host = form.Pla_Host.data
            row.Pla_Port = form.Pla_Port.data
            row.Pla_User = form.Pla_User.data
            row.Pla_Password = form.Pla_Password.data
            try:
               session['new_row']=str(row)
               db.session.close()
               db.session.add(row)
               db.session.commit()
               if session['is_new_row']==True:
                   logger.audit ( '%s:NEW:%s' % (current_user.username,session['new_row'] ) )
                   flash('New Platform created OK')
               else:
                   logger.audit ( '%s:OLD:%s' % (current_user.username,session['prev_row']) )
                   logger.audit ( '%s:UPD:%s' % (current_user.username,session['new_row'] ) )
                   message=Markup('<b>Platform %s saved OK</b>'%(Pla_Id))
                   flash(message)
               db.session.close()
            except Exception as e:
               db.session.rollback()
               db.session.close()
               message=Markup('ERROR saving Platform record : %s'%(e))
               flash(message)
            return redirect(url_for('.select_Platforms_query'))
        elif   form.submit_New.data and current_user.role_id>1:
            #print('New Data Here ...')
            session['is_new_row']=True
            db.session.close()
            row=platform()
            return redirect(url_for('.forms_Platforms',Pla_Id=row.Pla_Id))

        elif   form.submit_Cancel.data:
            #print('Cancel Data Here ... does nothing')
            message=Markup('Platform Record modifications discarded ...')
            flash(message)
        else:
            #print('form validated but not submited ???')
            message=Markup('<b>Platform data modifications not allowed for user \'%s\'. Please contact Collector\'s Administrator ...</b>'%(current_user.username))
            flash(message)
            return redirect(url_for('.forms_Platforms',Pla_Id=row.Pla_Id))

    form.Pla_Name.data = row.Pla_Name
    form.Pla_Host.data = row.Pla_Host
    form.Pla_Port.data = row.Pla_Port
    form.Pla_User.data = row.Pla_User
    form.Pla_Password.data = row.Pla_Password
    session['prev_row']=str(row)
    session['is_new_row']=False
    return render_template('platforms.html', form=form, row=row)

# =============================================================================
@main.route('/forms/Platforms_delete', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@admin_required
def forms_Platforms_delete():
    """ Delete record handling function for table Platforms """

    logger.debug('Enter: forms_Platforms_delete()')
    Pla_Id  =  request.args.get('Pla_Id',0,type=int)
    row =  platform.query.filter(platform.Pla_Id == Pla_Id).first()
    if row is None:
        row=platform()
    session['data'] =  { 'Pla_Id':row.Pla_Id, 'Pla_Name':row.Pla_Name, 'Pla_Host':row.Pla_Host, 'Pla_Port':row.Pla_Port, 'Pla_User':row.Pla_User, 'Pla_Password':row.Pla_Password}
    form = frm_platform_delete()

    if form.validate_on_submit():
        if  form.submit_Delete.data:
            print('Delete Data Here...')
            try:
                session['deleted_row']=str(row)
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                logger.audit ( '%s:DEL:%s' % (current_user.username,session['deleted_row']) )
                flash('Platform %s deleted OK'%(Pla_Id))
            except exc.IntegrityError as e:
                db.session.rollback()
                flash('INTEGRITY ERROR: Are you sure there are no dependant records in other tables?')
                return redirect(url_for('.forms_Platforms_delete',Pla_Id=session['data']['Pla_Id']))

            return redirect(url_for('.select_Platforms_query'))
        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
            return redirect(url_for('.select_Platforms_query'))
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.select_Platforms_query'))


    return render_template('platforms_delete.html', form=form, data=session.get('data'),row=row)

# =============================================================================
@main.route('/select/Platforms_Query', methods=['GET','POST'])
@login_required
@admin_required
def select_Platforms_query():
    """ Select rows handling function for table Platforms """

    logger.debug('Enter: select_Platforms_query()')
    field =  request.args.get('field',None,type=str)
    value =  request.args.get('value',0,type=str)
    page  =  request.args.get('page',1,type=int)

    if field is not None:
        if   field == 'Pla_Id':
            rows =  platform.query.filter_by(Pla_Id=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Pla_Name':
            rows =  platform.query.filter_by(Pla_Name=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Pla_Host':
            rows =  platform.query.filter_by(Pla_Host=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Pla_Port':
            rows =  platform.query.filter_by(Pla_Port=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Pla_User':
            rows =  platform.query.filter_by(Pla_User=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Pla_Password':
            rows =  platform.query.filter_by(Pla_Password=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
    else:
       rows =  platform.query\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)

    if field is not None:
       next_url = url_for('.select_Platforms_query', field=field, value=value, page=rows.next_num) \
           if rows.has_next else None
       prev_url = url_for('.select_Platforms_query', field=field, value=value, page=rows.prev_num) \
           if rows.has_prev else None

    else:
       next_url = url_for('.select_Platforms_query', page=rows.next_num) \
           if rows.has_next else None
       prev_url = url_for('.select_Platforms_query', page=rows.prev_num) \
           if rows.has_prev else None

    return render_template('platforms_All.html',rows=rows)
# =============================================================================
