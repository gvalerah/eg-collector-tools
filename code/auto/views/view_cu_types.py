# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-16 15:51:37
# =============================================================================

@main.route('/forms/CU_Types', methods=['GET', 'POST'])
@login_required
@admin_required
def forms_CU_Types():
    """ Form handling function for table CU_Types """

    logger.debug('Enter: forms_CU_Types()')
    Typ_Code  =  request.args.get('Typ_Code',0,type=int)
    row =  cu_type.query.filter(cu_type.Typ_Code == Typ_Code).first()
    if row is None:
        row=cu_type()
        session['is_new_row']=True

    session['data'] =  { 'Typ_Code':row.Typ_Code, 'Typ_Description':row.Typ_Description}
    form = frm_cu_type()

    if form.validate_on_submit():
        if     form.submit_Save.data and current_user.role_id>1:
            row.Typ_Code = form.Typ_Code.data
            row.Typ_Description = form.Typ_Description.data
            try:
               session['new_row']=str(row)
               db.session.close()
               db.session.add(row)
               db.session.commit()
               if session['is_new_row']==True:
                   logger.audit ( '%s:NEW:%s' % (current_user.username,session['new_row'] ) )
                   flash('New Configuration Unit Type created OK')
               else:
                   logger.audit ( '%s:OLD:%s' % (current_user.username,session['prev_row']) )
                   logger.audit ( '%s:UPD:%s' % (current_user.username,session['new_row'] ) )
                   message=Markup('<b>Configuration Unit Type %s saved OK</b>'%(Typ_Code))
                   flash(message)
               db.session.close()
            except Exception as e:
               db.session.rollback()
               db.session.close()
               message=Markup('ERROR saving Configuration Unit Type record : %s'%(e))
               flash(message)
            return redirect(url_for('.select_CU_Types_query'))
        elif   form.submit_New.data and current_user.role_id>1:
            #print('New Data Here ...')
            session['is_new_row']=True
            db.session.close()
            row=cu_type()
            return redirect(url_for('.forms_CU_Types'))

        elif   form.submit_Cancel.data:
            #print('Cancel Data Here ... does nothing')
            message=Markup('Configuration Unit Type Record modifications discarded ...')
            flash(message)
        else:
            #print('form validated but not submited ???')
            message=Markup('<b>Configuration Unit Type data modifications not allowed for user \'%s\'. Please contact Collector\'s Administrator ...</b>'%(current_user.username))
            flash(message)
            return redirect(url_for('.forms_CU_Types'))

    form.Typ_Code.data = row.Typ_Code
    form.Typ_Description.data = row.Typ_Description
    session['prev_row']=str(row)
    session['is_new_row']=False
    return render_template('cu_types.html', form=form, row=row)

# =============================================================================
@main.route('/forms/CU_Types_delete', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@admin_required
def forms_CU_Types_delete():
    """ Delete record handling function for table CU_Types """

    logger.debug('Enter: forms_CU_Types_delete()')
    Typ_Code  =  request.args.get('Typ_Code',0,type=int)
    row =  cu_type.query.filter(cu_type.Typ_Code == Typ_Code).first()
    if row is None:
        row=cu_type()
    session['data'] =  { 'Typ_Code':row.Typ_Code, 'Typ_Description':row.Typ_Description}
    form = frm_cu_type_delete()

    if form.validate_on_submit():
        if  form.submit_Delete.data:
            print('Delete Data Here...')
            try:
                session['deleted_row']=str(row)
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                logger.audit ( '%s:DEL:%s' % (current_user.username,session['deleted_row']) )
                flash('Configuration Unit Type %s deleted OK'%(Typ_Code))
            except exc.IntegrityError as e:
                db.session.rollback()
                flash('INTEGRITY ERROR: Are you sure there are no dependant records in other tables?')
                return redirect(url_for('.forms_CU_Types_delete',Typ_Code=session['data']['Typ_Code']))

            return redirect(url_for('.select_CU_Types_query'))
        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
            return redirect(url_for('.select_CU_Types_query'))
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.select_CU_Types_query'))


    return render_template('cu_types_delete.html', form=form, data=session.get('data'),row=row)

# =============================================================================
@main.route('/select/CU_Types_Query', methods=['GET','POST'])
@login_required
@admin_required
def select_CU_Types_query():
    """ Select rows handling function for table CU_Types """

    logger.debug('Enter: select_CU_Types_query()')
    field =  request.args.get('field',None,type=str)
    value =  request.args.get('value',0,type=str)
    page  =  request.args.get('page',1,type=int)

    if field is not None:
        if   field == 'Typ_Code':
            rows =  cu_type.query.filter_by(Typ_Code=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Typ_Description':
            rows =  cu_type.query.filter_by(Typ_Description=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
    else:
       rows =  cu_type.query\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)

    if field is not None:
       next_url = url_for('.select_CU_Types_query', field=field, value=value, page=rows.next_num) \
           if rows.has_next else None
       prev_url = url_for('.select_CU_Types_query', field=field, value=value, page=rows.prev_num) \
           if rows.has_prev else None

    else:
       next_url = url_for('.select_CU_Types_query', page=rows.next_num) \
           if rows.has_next else None
       prev_url = url_for('.select_CU_Types_query', page=rows.prev_num) \
           if rows.has_prev else None

    return render_template('cu_types_All.html',rows=rows)
# =============================================================================
