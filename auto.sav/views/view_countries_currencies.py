# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-20 18:43:44
# =============================================================================

@main.route('/forms/Countries_Currencies', methods=['GET', 'POST'])
@login_required
@admin_required
def forms_Countries_Currencies():
    """ Form handling function for table Countries_Currencies """

    logger.debug('Enter: forms_Countries_Currencies()')
    Cou_Code  =  request.args.get('Cou_Code',0,type=int)
    Cur_Code  =  request.args.get('Cur_Code',0,type=int)
    row =  country_currency.query.filter(country_currency.Cou_Code == Cou_Code,country_currency.Cur_Code == Cur_Code).first()
    if row is None:
        row=country_currency()
        session['is_new_row']=True

    session['data'] =  { 'Cou_Code':row.Cou_Code, 'Cur_Code':row.Cur_Code, 'Cou_Cur_Comment':row.Cou_Cur_Comment}
    form = frm_country_currency()

    if form.has_FKs:
        form.Cou_Code.choices = db.session.query(country.Cou_Code,country.Cou_Name).order_by(country.Cou_Name).all()
        form.Cur_Code.choices = db.session.query(currency.Cur_Code,currency.Cur_Name).order_by(currency.Cur_Name).all()

    if form.validate_on_submit():
        if     form.submit_Save.data and current_user.role_id>1:
            row.Cou_Code = form.Cou_Code.data
            row.Cur_Code = form.Cur_Code.data
            row.Cou_Cur_Comment = form.Cou_Cur_Comment.data
            try:
               session['new_row']=str(row)
               db.session.close()
               db.session.add(row)
               db.session.commit()
               if session['is_new_row']==True:
                   logger.audit ( '%s:NEW:%s' % (current_user.username,session['new_row'] ) )
                   flash('New Country vs Currency created OK')
               else:
                   logger.audit ( '%s:OLD:%s' % (current_user.username,session['prev_row']) )
                   logger.audit ( '%s:UPD:%s' % (current_user.username,session['new_row'] ) )
                   message=Markup('<b>Country vs Currency %s saved OK</b>'%(Cou_Code,Cur_Code))
                   flash(message)
               db.session.close()
            except Exception as e:
               db.session.rollback()
               db.session.close()
               message=Markup('ERROR saving Country vs Currency record : %s'%(e))
               flash(message)
            return redirect(url_for('.select_Countries_Currencies_query'))
        elif   form.submit_New.data and current_user.role_id>1:
            #print('New Data Here ...')
            session['is_new_row']=True
            db.session.close()
            row=country_currency()
            return redirect(url_for('.forms_Countries_Currencies'))

        elif   form.submit_Cancel.data:
            #print('Cancel Data Here ... does nothing')
            message=Markup('Country vs Currency Record modifications discarded ...')
            flash(message)
        else:
            #print('form validated but not submited ???')
            message=Markup('<b>Country vs Currency data modifications not allowed for user \'%s\'. Please contact Collector\'s Administrator ...</b>'%(current_user.username))
            flash(message)
            return redirect(url_for('.forms_Countries_Currencies'))

    form.Cou_Code.data = row.Cou_Code
    form.Cur_Code.data = row.Cur_Code
    form.Cou_Cur_Comment.data = row.Cou_Cur_Comment
    session['prev_row']=str(row)
    session['is_new_row']=False
    return render_template('countries_currencies.html', form=form, row=row)

# =============================================================================
@main.route('/forms/Countries_Currencies_delete', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@admin_required
def forms_Countries_Currencies_delete():
    """ Delete record handling function for table Countries_Currencies """

    logger.debug('Enter: forms_Countries_Currencies_delete()')
    Cou_Code  =  request.args.get('Cou_Code',0,type=int)
    Cur_Code  =  request.args.get('Cur_Code',0,type=int)
    row =  country_currency.query.filter(country_currency.Cou_Code == Cou_Code,country_currency.Cur_Code == Cur_Code).first()
    if row is None:
        row=country_currency()
    session['data'] =  { 'Cou_Code':row.Cou_Code, 'Cur_Code':row.Cur_Code, 'Cou_Cur_Comment':row.Cou_Cur_Comment}
    form = frm_country_currency_delete()

    if form.validate_on_submit():
        if  form.submit_Delete.data:
            print('Delete Data Here...')
            try:
                session['deleted_row']=str(row)
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                logger.audit ( '%s:DEL:%s' % (current_user.username,session['deleted_row']) )
                flash('Country vs Currency %s deleted OK'%(Cou_Code,Cur_Code))
            except exc.IntegrityError as e:
                db.session.rollback()
                flash('INTEGRITY ERROR: Are you sure there are no dependant records in other tables?')
                return redirect(url_for('.forms_Countries_Currencies_delete',Cou_Code=session['data']['Cou_Code'],Cur_Code=session['data']['Cur_Code']))

            return redirect(url_for('.select_Countries_Currencies_query'))
        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
            return redirect(url_for('.select_Countries_Currencies_query'))
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.select_Countries_Currencies_query'))


    return render_template('countries_currencies_delete.html', form=form, data=session.get('data'),row=row)

# =============================================================================
@main.route('/select/Countries_Currencies_Query', methods=['GET','POST'])
@login_required
@admin_required
def select_Countries_Currencies_query():
    """ Select rows handling function for table Countries_Currencies """

    logger.debug('Enter: select_Countries_Currencies_query()')
    field =  request.args.get('field',None,type=str)
    value =  request.args.get('value',0,type=str)
    page  =  request.args.get('page',1,type=int)

    if field is not None:
        if   field == 'Cou_Code':
            rows =  country_currency.query.filter_by(Cou_Code=value)\
               .join(country,country_currency.Cou_Code == country.Cou_Code).add_columns(country.Cou_Name)\
               .join(currency,country_currency.Cur_Code == currency.Cur_Code).add_columns(currency.Cur_Name)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Cur_Code':
            rows =  country_currency.query.filter_by(Cur_Code=value)\
               .join(country,country_currency.Cou_Code == country.Cou_Code).add_columns(country.Cou_Name)\
               .join(currency,country_currency.Cur_Code == currency.Cur_Code).add_columns(currency.Cur_Name)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Cou_Cur_Comment':
            rows =  country_currency.query.filter_by(Cou_Cur_Comment=value)\
               .join(country,country_currency.Cou_Code == country.Cou_Code).add_columns(country.Cou_Name)\
               .join(currency,country_currency.Cur_Code == currency.Cur_Code).add_columns(currency.Cur_Name)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
    else:
       rows =  country_currency.query\
               .join(country,country_currency.Cou_Code == country.Cou_Code).add_columns(country.Cou_Name)\
               .join(currency,country_currency.Cur_Code == currency.Cur_Code).add_columns(currency.Cur_Name)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)

    if field is not None:
       next_url = url_for('.select_Countries_Currencies_query', field=field, value=value, page=rows.next_num) \
           if rows.has_next else None
       prev_url = url_for('.select_Countries_Currencies_query', field=field, value=value, page=rows.prev_num) \
           if rows.has_prev else None

    else:
       next_url = url_for('.select_Countries_Currencies_query', page=rows.next_num) \
           if rows.has_next else None
       prev_url = url_for('.select_Countries_Currencies_query', page=rows.prev_num) \
           if rows.has_prev else None

    return render_template('countries_currencies_All.html',rows=rows)
# =============================================================================
