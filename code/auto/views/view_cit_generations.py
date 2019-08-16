# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-16 15:51:37
# =============================================================================

@main.route('/forms/CIT_Generations', methods=['GET', 'POST'])
@login_required
@admin_required
def forms_CIT_Generations():
    """ Form handling function for table CIT_Generations """

    logger.debug('Enter: forms_CIT_Generations()')
    CIT_Generation  =  request.args.get('CIT_Generation',0,type=int)
    row =  cit_generation.query.filter(cit_generation.CIT_Generation == CIT_Generation).first()
    if row is None:
        row=cit_generation()
        session['is_new_row']=True

    session['data'] =  { 'CIT_Generation':row.CIT_Generation, 'Value':row.Value}
    form = frm_cit_generation()

    if form.validate_on_submit():
        if     form.submit_Save.data and current_user.role_id>1:
            row.CIT_Generation = form.CIT_Generation.data
            row.Value = form.Value.data
            try:
               session['new_row']=str(row)
               db.session.close()
               db.session.add(row)
               db.session.commit()
               if session['is_new_row']==True:
                   logger.audit ( '%s:NEW:%s' % (current_user.username,session['new_row'] ) )
                   flash('New Configuration Item Generation Type created OK')
               else:
                   logger.audit ( '%s:OLD:%s' % (current_user.username,session['prev_row']) )
                   logger.audit ( '%s:UPD:%s' % (current_user.username,session['new_row'] ) )
                   message=Markup('<b>Configuration Item Generation Type %s saved OK</b>'%(CIT_Generation))
                   flash(message)
               db.session.close()
            except Exception as e:
               db.session.rollback()
               db.session.close()
               message=Markup('ERROR saving Configuration Item Generation Type record : %s'%(e))
               flash(message)
            return redirect(url_for('.select_CIT_Generations_query'))
        elif   form.submit_New.data and current_user.role_id>1:
            #print('New Data Here ...')
            session['is_new_row']=True
            db.session.close()
            row=cit_generation()
            return redirect(url_for('.forms_CIT_Generations'))

        elif   form.submit_Cancel.data:
            #print('Cancel Data Here ... does nothing')
            message=Markup('Configuration Item Generation Type Record modifications discarded ...')
            flash(message)
        else:
            #print('form validated but not submited ???')
            message=Markup('<b>Configuration Item Generation Type data modifications not allowed for user \'%s\'. Please contact Collector\'s Administrator ...</b>'%(current_user.username))
            flash(message)
            return redirect(url_for('.forms_CIT_Generations'))

    form.CIT_Generation.data = row.CIT_Generation
    form.Value.data = row.Value
    session['prev_row']=str(row)
    session['is_new_row']=False
    return render_template('cit_generations.html', form=form, row=row)

# =============================================================================
@main.route('/forms/CIT_Generations_delete', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@admin_required
def forms_CIT_Generations_delete():
    """ Delete record handling function for table CIT_Generations """

    logger.debug('Enter: forms_CIT_Generations_delete()')
    CIT_Generation  =  request.args.get('CIT_Generation',0,type=int)
    row =  cit_generation.query.filter(cit_generation.CIT_Generation == CIT_Generation).first()
    if row is None:
        row=cit_generation()
    session['data'] =  { 'CIT_Generation':row.CIT_Generation, 'Value':row.Value}
    form = frm_cit_generation_delete()

    if form.validate_on_submit():
        if  form.submit_Delete.data:
            print('Delete Data Here...')
            try:
                session['deleted_row']=str(row)
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                logger.audit ( '%s:DEL:%s' % (current_user.username,session['deleted_row']) )
                flash('Configuration Item Generation Type %s deleted OK'%(CIT_Generation))
            except exc.IntegrityError as e:
                db.session.rollback()
                flash('INTEGRITY ERROR: Are you sure there are no dependant records in other tables?')
                return redirect(url_for('.forms_CIT_Generations_delete',CIT_Generation=session['data']['CIT_Generation']))

            return redirect(url_for('.select_CIT_Generations_query'))
        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
            return redirect(url_for('.select_CIT_Generations_query'))
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.select_CIT_Generations_query'))


    return render_template('cit_generations_delete.html', form=form, data=session.get('data'),row=row)

# =============================================================================
@main.route('/select/CIT_Generations_Query', methods=['GET','POST'])
@login_required
@admin_required
def select_CIT_Generations_query():
    """ Select rows handling function for table CIT_Generations """

    logger.debug('Enter: select_CIT_Generations_query()')
    field =  request.args.get('field',None,type=str)
    value =  request.args.get('value',0,type=str)
    page  =  request.args.get('page',1,type=int)

    if field is not None:
        if   field == 'CIT_Generation':
            rows =  cit_generation.query.filter_by(CIT_Generation=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Value':
            rows =  cit_generation.query.filter_by(Value=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
    else:
       rows =  cit_generation.query\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)

    if field is not None:
       next_url = url_for('.select_CIT_Generations_query', field=field, value=value, page=rows.next_num) \
           if rows.has_next else None
       prev_url = url_for('.select_CIT_Generations_query', field=field, value=value, page=rows.prev_num) \
           if rows.has_prev else None

    else:
       next_url = url_for('.select_CIT_Generations_query', page=rows.next_num) \
           if rows.has_next else None
       prev_url = url_for('.select_CIT_Generations_query', page=rows.prev_num) \
           if rows.has_prev else None

    return render_template('cit_generations_All.html',rows=rows)
# =============================================================================
