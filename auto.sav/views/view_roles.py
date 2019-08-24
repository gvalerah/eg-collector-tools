# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-20 18:43:44
# =============================================================================

@main.route('/forms/Roles', methods=['GET', 'POST'])
@login_required
@admin_required
def forms_Roles():
    """ Form handling function for table Roles """

    logger.debug('Enter: forms_Roles()')
    id  =  request.args.get('id',0,type=int)
    row =  Role.query.filter(Role.id == id).first()
    if row is None:
        row=Role()
        session['is_new_row']=True

    session['data'] =  { 'id':row.id, 'name':row.name, 'default':row.default, 'permissions':row.permissions}
    form = frm_Role()

    if form.validate_on_submit():
        if     form.submit_Save.data and current_user.role_id>1:
            row.id = form.id.data
            row.name = form.name.data
            row.default = form.default.data
            row.permissions = form.permissions.data
            try:
               session['new_row']=str(row)
               db.session.close()
               db.session.add(row)
               db.session.commit()
               if session['is_new_row']==True:
                   logger.audit ( '%s:NEW:%s' % (current_user.username,session['new_row'] ) )
                   flash('New Role created OK')
               else:
                   logger.audit ( '%s:OLD:%s' % (current_user.username,session['prev_row']) )
                   logger.audit ( '%s:UPD:%s' % (current_user.username,session['new_row'] ) )
                   message=Markup('<b>Role %s saved OK</b>'%(id))
                   flash(message)
               db.session.close()
            except Exception as e:
               db.session.rollback()
               db.session.close()
               message=Markup('ERROR saving Role record : %s'%(e))
               flash(message)
            return redirect(url_for('.select_Roles_query'))
        elif   form.submit_New.data and current_user.role_id>1:
            #print('New Data Here ...')
            session['is_new_row']=True
            db.session.close()
            row=Role()
            return redirect(url_for('.forms_Roles'))

        elif   form.submit_Cancel.data:
            #print('Cancel Data Here ... does nothing')
            message=Markup('Role Record modifications discarded ...')
            flash(message)
        else:
            #print('form validated but not submited ???')
            message=Markup('<b>Role data modifications not allowed for user \'%s\'. Please contact Collector\'s Administrator ...</b>'%(current_user.username))
            flash(message)
            return redirect(url_for('.forms_Roles'))

    form.id.data = row.id
    form.name.data = row.name
    form.default.data = row.default
    form.permissions.data = row.permissions
    session['prev_row']=str(row)
    session['is_new_row']=False
    return render_template('roles.html', form=form, row=row)

# =============================================================================
@main.route('/forms/Roles_delete', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@admin_required
def forms_Roles_delete():
    """ Delete record handling function for table Roles """

    logger.debug('Enter: forms_Roles_delete()')
    id  =  request.args.get('id',0,type=int)
    row =  Role.query.filter(Role.id == id).first()
    if row is None:
        row=Role()
    session['data'] =  { 'id':row.id, 'name':row.name, 'default':row.default, 'permissions':row.permissions}
    form = frm_Role_delete()

    if form.validate_on_submit():
        if  form.submit_Delete.data:
            print('Delete Data Here...')
            try:
                session['deleted_row']=str(row)
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                logger.audit ( '%s:DEL:%s' % (current_user.username,session['deleted_row']) )
                flash('Role %s deleted OK'%(id))
            except exc.IntegrityError as e:
                db.session.rollback()
                flash('INTEGRITY ERROR: Are you sure there are no dependant records in other tables?')
                return redirect(url_for('.forms_Roles_delete',id=session['data']['id']))

            return redirect(url_for('.select_Roles_query'))
        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
            return redirect(url_for('.select_Roles_query'))
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.select_Roles_query'))


    return render_template('roles_delete.html', form=form, data=session.get('data'),row=row)

# =============================================================================
@main.route('/select/Roles_Query', methods=['GET','POST'])
@login_required
@admin_required
def select_Roles_query():
    """ Select rows handling function for table Roles """

    logger.debug('Enter: select_Roles_query()')
    field =  request.args.get('field',None,type=str)
    value =  request.args.get('value',0,type=str)
    page  =  request.args.get('page',1,type=int)

    if field is not None:
        if   field == 'id':
            rows =  Role.query.filter_by(id=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'name':
            rows =  Role.query.filter_by(name=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'default':
            rows =  Role.query.filter_by(default=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'permissions':
            rows =  Role.query.filter_by(permissions=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
    else:
       rows =  Role.query\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)

    if field is not None:
       next_url = url_for('.select_Roles_query', field=field, value=value, page=rows.next_num) \
           if rows.has_next else None
       prev_url = url_for('.select_Roles_query', field=field, value=value, page=rows.prev_num) \
           if rows.has_prev else None

    else:
       next_url = url_for('.select_Roles_query', page=rows.next_num) \
           if rows.has_next else None
       prev_url = url_for('.select_Roles_query', page=rows.prev_num) \
           if rows.has_prev else None

    return render_template('roles_All.html',rows=rows)
# =============================================================================
