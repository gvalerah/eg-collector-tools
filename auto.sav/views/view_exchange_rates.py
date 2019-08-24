# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-20 18:43:44
# =============================================================================

@main.route('/forms/Exchange_Rates', methods=['GET', 'POST'])
@login_required
@admin_required
def forms_Exchange_Rates():
    """ Form handling function for table Exchange_Rates """

    logger.debug('Enter: forms_Exchange_Rates()')
    ER_Id  =  request.args.get('ER_Id',0,type=int)
    row =  exchange_rate.query.filter(exchange_rate.ER_Id == ER_Id).first()
    if row is None:
        row=exchange_rate()
        session['is_new_row']=True

    session['data'] =  { 'ER_Id':row.ER_Id, 'Cur_Code':row.Cur_Code, 'ER_Factor':row.ER_Factor, 'ER_Date':row.ER_Date}
    form = frm_exchange_rate()

    if form.has_FKs:
        form.Cur_Code.choices = db.session.query(currency.Cur_Code,currency.Cur_Name).order_by(currency.Cur_Name).all()

    if form.validate_on_submit():
        if     form.submit_Save.data and current_user.role_id>1:
            row.Cur_Code = form.Cur_Code.data
            row.ER_Factor = form.ER_Factor.data
            row.ER_Date = form.ER_Date.data
            try:
               session['new_row']=str(row)
               db.session.close()
               db.session.add(row)
               db.session.commit()
               if session['is_new_row']==True:
                   logger.audit ( '%s:NEW:%s' % (current_user.username,session['new_row'] ) )
                   flash('New Exchange Rate created OK')
               else:
                   logger.audit ( '%s:OLD:%s' % (current_user.username,session['prev_row']) )
                   logger.audit ( '%s:UPD:%s' % (current_user.username,session['new_row'] ) )
                   message=Markup('<b>Exchange Rate %s saved OK</b>'%(ER_Id))
                   flash(message)
               db.session.close()
            except Exception as e:
               db.session.rollback()
               db.session.close()
               message=Markup('ERROR saving Exchange Rate record : %s'%(e))
               flash(message)
            return redirect(url_for('.select_Exchange_Rates_query'))
        elif   form.submit_New.data and current_user.role_id>1:
            #print('New Data Here ...')
            session['is_new_row']=True
            db.session.close()
            row=exchange_rate()
            return redirect(url_for('.forms_Exchange_Rates',ER_Id=row.ER_Id))

        elif   form.submit_Cancel.data:
            #print('Cancel Data Here ... does nothing')
            message=Markup('Exchange Rate Record modifications discarded ...')
            flash(message)
        else:
            #print('form validated but not submited ???')
            message=Markup('<b>Exchange Rate data modifications not allowed for user \'%s\'. Please contact Collector\'s Administrator ...</b>'%(current_user.username))
            flash(message)
            return redirect(url_for('.forms_Exchange_Rates',ER_Id=row.ER_Id))

    form.Cur_Code.data = row.Cur_Code
    form.ER_Factor.data = row.ER_Factor
    form.ER_Date.data = row.ER_Date
    session['prev_row']=str(row)
    session['is_new_row']=False
    return render_template('exchange_rates.html', form=form, row=row)

# =============================================================================
@main.route('/forms/Exchange_Rates_delete', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@admin_required
def forms_Exchange_Rates_delete():
    """ Delete record handling function for table Exchange_Rates """

    logger.debug('Enter: forms_Exchange_Rates_delete()')
    ER_Id  =  request.args.get('ER_Id',0,type=int)
    row =  exchange_rate.query.filter(exchange_rate.ER_Id == ER_Id).first()
    if row is None:
        row=exchange_rate()
    session['data'] =  { 'ER_Id':row.ER_Id, 'Cur_Code':row.Cur_Code, 'ER_Factor':row.ER_Factor, 'ER_Date':row.ER_Date}
    form = frm_exchange_rate_delete()

    if form.validate_on_submit():
        if  form.submit_Delete.data:
            print('Delete Data Here...')
            try:
                session['deleted_row']=str(row)
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                logger.audit ( '%s:DEL:%s' % (current_user.username,session['deleted_row']) )
                flash('Exchange Rate %s deleted OK'%(ER_Id))
            except exc.IntegrityError as e:
                db.session.rollback()
                flash('INTEGRITY ERROR: Are you sure there are no dependant records in other tables?')
                return redirect(url_for('.forms_Exchange_Rates_delete',ER_Id=session['data']['ER_Id']))

            return redirect(url_for('.select_Exchange_Rates_query'))
        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
            return redirect(url_for('.select_Exchange_Rates_query'))
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.select_Exchange_Rates_query'))


    return render_template('exchange_rates_delete.html', form=form, data=session.get('data'),row=row)

# =============================================================================
@main.route('/select/Exchange_Rates_Query', methods=['GET','POST'])
@login_required
@admin_required
def select_Exchange_Rates_query():
    """ Select rows handling function for table Exchange_Rates """

    logger.debug('Enter: select_Exchange_Rates_query()')
    field =  request.args.get('field',None,type=str)
    value =  request.args.get('value',0,type=str)
    page  =  request.args.get('page',1,type=int)

    if field is not None:
        if   field == 'ER_Id':
            rows =  exchange_rate.query.filter_by(ER_Id=value)\
               .join(currency,exchange_rate.Cur_Code == currency.Cur_Code).add_columns(currency.Cur_Name)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Cur_Code':
            rows =  exchange_rate.query.filter_by(Cur_Code=value)\
               .join(currency,exchange_rate.Cur_Code == currency.Cur_Code).add_columns(currency.Cur_Name)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'ER_Factor':
            rows =  exchange_rate.query.filter_by(ER_Factor=value)\
               .join(currency,exchange_rate.Cur_Code == currency.Cur_Code).add_columns(currency.Cur_Name)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'ER_Date':
            rows =  exchange_rate.query.filter_by(ER_Date=value)\
               .join(currency,exchange_rate.Cur_Code == currency.Cur_Code).add_columns(currency.Cur_Name)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
    else:
       rows =  exchange_rate.query\
               .join(currency,exchange_rate.Cur_Code == currency.Cur_Code).add_columns(currency.Cur_Name)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)

    if field is not None:
       next_url = url_for('.select_Exchange_Rates_query', field=field, value=value, page=rows.next_num) \
           if rows.has_next else None
       prev_url = url_for('.select_Exchange_Rates_query', field=field, value=value, page=rows.prev_num) \
           if rows.has_prev else None

    else:
       next_url = url_for('.select_Exchange_Rates_query', page=rows.next_num) \
           if rows.has_next else None
       prev_url = url_for('.select_Exchange_Rates_query', page=rows.prev_num) \
           if rows.has_prev else None

    return render_template('exchange_rates_All.html',rows=rows)
# =============================================================================
