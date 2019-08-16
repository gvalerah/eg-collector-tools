# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-16 15:51:37
# =============================================================================

@main.route('/forms/Countries', methods=['GET', 'POST'])
@login_required
@admin_required
def forms_Countries():
    """ Form handling function for table Countries """

    logger.debug('Enter: forms_Countries()')
    Cou_Code  =  request.args.get('Cou_Code',0,type=int)
    row =  country.query.filter(country.Cou_Code == Cou_Code).first()
    if row is None:
        row=country()
        session['is_new_row']=True

    session['data'] =  { 'Cou_Code':row.Cou_Code, 'Cou_Name':row.Cou_Name, 'Cou_A3':row.Cou_A3, 'Cou_N':row.Cou_N}
    form = frm_country()

    if form.validate_on_submit():
        if     form.submit_Save.data and current_user.role_id>1:
            row.Cou_Code = form.Cou_Code.data
            row.Cou_Name = form.Cou_Name.data
            row.Cou_A3 = form.Cou_A3.data
            row.Cou_N = form.Cou_N.data
            try:
               session['new_row']=str(row)
               db.session.close()
               db.session.add(row)
               db.session.commit()
               if session['is_new_row']==True:
                   logger.audit ( '%s:NEW:%s' % (current_user.username,session['new_row'] ) )
                   flash('New Country created OK')
               else:
                   logger.audit ( '%s:OLD:%s' % (current_user.username,session['prev_row']) )
                   logger.audit ( '%s:UPD:%s' % (current_user.username,session['new_row'] ) )
                   message=Markup('<b>Country %s saved OK</b>'%(Cou_Code))
                   flash(message)
               db.session.close()
            except Exception as e:
               db.session.rollback()
               db.session.close()
               message=Markup('ERROR saving Country record : %s'%(e))
               flash(message)
            return redirect(url_for('.select_Countries_query'))
        elif   form.submit_New.data and current_user.role_id>1:
            #print('New Data Here ...')
            session['is_new_row']=True
            db.session.close()
            row=country()
            return redirect(url_for('.forms_Countries'))

        elif   form.submit_Cancel.data:
            #print('Cancel Data Here ... does nothing')
            message=Markup('Country Record modifications discarded ...')
            flash(message)
        else:
            #print('form validated but not submited ???')
            message=Markup('<b>Country data modifications not allowed for user \'%s\'. Please contact Collector\'s Administrator ...</b>'%(current_user.username))
            flash(message)
            return redirect(url_for('.forms_Countries'))

    form.Cou_Code.data = row.Cou_Code
    form.Cou_Name.data = row.Cou_Name
    form.Cou_A3.data = row.Cou_A3
    form.Cou_N.data = row.Cou_N
    session['prev_row']=str(row)
    session['is_new_row']=False
    return render_template('countries.html', form=form, row=row)

# =============================================================================
@main.route('/forms/Countries_delete', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@admin_required
def forms_Countries_delete():
    """ Delete record handling function for table Countries """

    logger.debug('Enter: forms_Countries_delete()')
    Cou_Code  =  request.args.get('Cou_Code',0,type=int)
    row =  country.query.filter(country.Cou_Code == Cou_Code).first()
    if row is None:
        row=country()
    session['data'] =  { 'Cou_Code':row.Cou_Code, 'Cou_Name':row.Cou_Name, 'Cou_A3':row.Cou_A3, 'Cou_N':row.Cou_N}
    form = frm_country_delete()

    if form.validate_on_submit():
        if  form.submit_Delete.data:
            print('Delete Data Here...')
            try:
                session['deleted_row']=str(row)
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                logger.audit ( '%s:DEL:%s' % (current_user.username,session['deleted_row']) )
                flash('Country %s deleted OK'%(Cou_Code))
            except exc.IntegrityError as e:
                db.session.rollback()
                flash('INTEGRITY ERROR: Are you sure there are no dependant records in other tables?')
                return redirect(url_for('.forms_Countries_delete',Cou_Code=session['data']['Cou_Code']))

            return redirect(url_for('.select_Countries_query'))
        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
            return redirect(url_for('.select_Countries_query'))
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.select_Countries_query'))


    return render_template('countries_delete.html', form=form, data=session.get('data'),row=row)

# =============================================================================
@main.route('/select/Countries_Query', methods=['GET','POST'])
@login_required
@admin_required
def select_Countries_query():
    """ Select rows handling function for table Countries """

    logger.debug('Enter: select_Countries_query()')
    field =  request.args.get('field',None,type=str)
    value =  request.args.get('value',0,type=str)
    page  =  request.args.get('page',1,type=int)

    if field is not None:
        if   field == 'Cou_Code':
            rows =  country.query.filter_by(Cou_Code=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Cou_Name':
            rows =  country.query.filter_by(Cou_Name=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Cou_A3':
            rows =  country.query.filter_by(Cou_A3=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Cou_N':
            rows =  country.query.filter_by(Cou_N=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
    else:
       rows =  country.query\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)

    if field is not None:
       next_url = url_for('.select_Countries_query', field=field, value=value, page=rows.next_num) \
           if rows.has_next else None
       prev_url = url_for('.select_Countries_query', field=field, value=value, page=rows.prev_num) \
           if rows.has_prev else None

    else:
       next_url = url_for('.select_Countries_query', page=rows.next_num) \
           if rows.has_next else None
       prev_url = url_for('.select_Countries_query', page=rows.prev_num) \
           if rows.has_prev else None

    return render_template('countries_All.html',rows=rows)
# =============================================================================
