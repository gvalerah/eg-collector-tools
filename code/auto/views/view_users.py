# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-16 15:51:37
# =============================================================================

@main.route('/forms/Users', methods=['GET', 'POST'])
@login_required
@admin_required
def forms_Users():
    """ Form handling function for table Users """

    logger.debug('Enter: forms_Users()')
    id  =  request.args.get('id',0,type=int)
    row =  User.query.filter(User.id == id).first()
    if row is None:
        row=User()
        session['is_new_row']=True

    session['data'] =  { 'id':row.id, 'username':row.username, 'role_id':row.role_id, 'email':row.email, 'password_hash':row.password_hash, 'confirmed':row.confirmed, 'CC_Id':row.CC_Id}
    form = frm_User()

    if form.has_FKs:
        form.role_id.choices = db.session.query(Role.id,Role.name).order_by(Role.name).all()
        form.CC_Id.choices = db.session.query(cost_center.CC_Id,cost_center.CC_Description).order_by(cost_center.CC_Description).all()

    if form.validate_on_submit():
        if     form.submit_Save.data and current_user.role_id>1:
            row.username = form.username.data
            row.role_id = form.role_id.data
            row.email = form.email.data
            row.password_hash = form.password_hash.data
            row.confirmed = form.confirmed.data
            row.CC_Id = form.CC_Id.data
            try:
               session['new_row']=str(row)
               db.session.close()
               db.session.add(row)
               db.session.commit()
               if session['is_new_row']==True:
                   logger.audit ( '%s:NEW:%s' % (current_user.username,session['new_row'] ) )
                   flash('New User created OK')
               else:
                   logger.audit ( '%s:OLD:%s' % (current_user.username,session['prev_row']) )
                   logger.audit ( '%s:UPD:%s' % (current_user.username,session['new_row'] ) )
                   message=Markup('<b>User %s saved OK</b>'%(id))
                   flash(message)
               db.session.close()
            except Exception as e:
               db.session.rollback()
               db.session.close()
               message=Markup('ERROR saving User record : %s'%(e))
               flash(message)
            return redirect(url_for('.select_Users_query'))
        elif   form.submit_New.data and current_user.role_id>1:
            #print('New Data Here ...')
            session['is_new_row']=True
            db.session.close()
            row=User()
            return redirect(url_for('.forms_Users',Id=row.Id))

        elif   form.submit_Cancel.data:
            #print('Cancel Data Here ... does nothing')
            message=Markup('User Record modifications discarded ...')
            flash(message)
        else:
            #print('form validated but not submited ???')
            message=Markup('<b>User data modifications not allowed for user \'%s\'. Please contact Collector\'s Administrator ...</b>'%(current_user.username))
            flash(message)
            return redirect(url_for('.forms_Users',Id=row.Id))

    form.username.data = row.username
    form.role_id.data = row.role_id
    form.email.data = row.email
    form.password_hash.data = row.password_hash
    form.confirmed.data = row.confirmed
    form.CC_Id.data = row.CC_Id
    session['prev_row']=str(row)
    session['is_new_row']=False
    return render_template('users.html', form=form, row=row)

# =============================================================================
@main.route('/forms/Users_delete', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@admin_required
def forms_Users_delete():
    """ Delete record handling function for table Users """

    logger.debug('Enter: forms_Users_delete()')
    id  =  request.args.get('id',0,type=int)
    row =  User.query.filter(User.id == id).first()
    if row is None:
        row=User()
    session['data'] =  { 'id':row.id, 'username':row.username, 'role_id':row.role_id, 'email':row.email, 'password_hash':row.password_hash, 'confirmed':row.confirmed, 'CC_Id':row.CC_Id}
    form = frm_User_delete()

    if form.validate_on_submit():
        if  form.submit_Delete.data:
            print('Delete Data Here...')
            try:
                session['deleted_row']=str(row)
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                logger.audit ( '%s:DEL:%s' % (current_user.username,session['deleted_row']) )
                flash('User %s deleted OK'%(id))
            except exc.IntegrityError as e:
                db.session.rollback()
                flash('INTEGRITY ERROR: Are you sure there are no dependant records in other tables?')
                return redirect(url_for('.forms_Users_delete',id=session['data']['id']))

            return redirect(url_for('.select_Users_query'))
        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
            return redirect(url_for('.select_Users_query'))
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.select_Users_query'))


    return render_template('users_delete.html', form=form, data=session.get('data'),row=row)

# =============================================================================
@main.route('/select/Users_Query', methods=['GET','POST'])
@login_required
@admin_required
def select_Users_query():
    """ Select rows handling function for table Users """

    logger.debug('Enter: select_Users_query()')
    field =  request.args.get('field',None,type=str)
    value =  request.args.get('value',0,type=str)
    page  =  request.args.get('page',1,type=int)

    if field is not None:
        if   field == 'id':
            rows =  User.query.filter_by(id=value)\
               .join(Role,User.role_id == Role.role_id).add_columns(Role.name)\
               .join(cost_center,User.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'username':
            rows =  User.query.filter_by(username=value)\
               .join(Role,User.role_id == Role.role_id).add_columns(Role.name)\
               .join(cost_center,User.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'role_id':
            rows =  User.query.filter_by(role_id=value)\
               .join(Role,User.role_id == Role.role_id).add_columns(Role.name)\
               .join(cost_center,User.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'email':
            rows =  User.query.filter_by(email=value)\
               .join(Role,User.role_id == Role.role_id).add_columns(Role.name)\
               .join(cost_center,User.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'password_hash':
            rows =  User.query.filter_by(password_hash=value)\
               .join(Role,User.role_id == Role.role_id).add_columns(Role.name)\
               .join(cost_center,User.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'confirmed':
            rows =  User.query.filter_by(confirmed=value)\
               .join(Role,User.role_id == Role.role_id).add_columns(Role.name)\
               .join(cost_center,User.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CC_Id':
            rows =  User.query.filter_by(CC_Id=value)\
               .join(Role,User.role_id == Role.role_id).add_columns(Role.name)\
               .join(cost_center,User.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
    else:
       rows =  User.query\
               .join(Role,User.role_id == Role.role_id).add_columns(Role.name)\
               .join(cost_center,User.CC_Id == cost_center.CC_Id).add_columns(cost_center.CC_Description)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)

    if field is not None:
       next_url = url_for('.select_Users_query', field=field, value=value, page=rows.next_num) \
           if rows.has_next else None
       prev_url = url_for('.select_Users_query', field=field, value=value, page=rows.prev_num) \
           if rows.has_prev else None

    else:
       next_url = url_for('.select_Users_query', page=rows.next_num) \
           if rows.has_next else None
       prev_url = url_for('.select_Users_query', page=rows.prev_num) \
           if rows.has_prev else None

    return render_template('users_All.html',rows=rows)
# =============================================================================
