# =============================================================================

# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-11-30 16:47:18
# =============================================================================


@main.route('/forms/Currencies', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@permission_required(Permission.MODIFY)
@admin_required
def forms_Currencies():
    """ Form handling function for table Currencies """

    logger.debug('Enter: forms_Currencies()')
    Cur_Code  =  request.args.get('Cur_Code',0,type=int)
    row =  currency.query.filter(currency.Cur_Code == Cur_Code).first()
    if row is None:
        row=currency()

    session['data'] =  { 'Cur_Code':row.Cur_Code, 'Cur_Name':row.Cur_Name, 'Cur_Id':row.Cur_Id, 'Cur_Comment':row.Cur_Comment}
    form = frm_currency()

    if form.validate_on_submit():
        if     form.submit_Save.data:
            row.Cur_Code = form.Cur_Code.data
            row.Cur_Name = form.Cur_Name.data
            row.Cur_Id = form.Cur_Id.data
            row.Cur_Comment = form.Cur_Comment.data
            try:
               db.session.close()
               db.session.add(row)
               db.session.commit()
               db.session.close()
               flash('Record %s saved OK'%(Cur_Code))
            except Exception as e:
               db.session.rollback()
               db.session.close()
               flash('ERROR saving record : %s'%(e))
            return redirect(url_for('.select_Currencies_query'))
        elif   form.submit_New.data:
            print('New Data Here...')
            db.session.close()
            row=currency()
            return redirect(url_for('.forms_Currencies'))

        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.forms_Currencies'))

    form.Cur_Code.data = row.Cur_Code
    form.Cur_Name.data = row.Cur_Name
    form.Cur_Id.data = row.Cur_Id
    form.Cur_Comment.data = row.Cur_Comment
    return render_template('currencies.html', form=form, row=row)

# =============================================================================

@main.route('/forms/Currencies_delete', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@admin_required
def forms_Currencies_delete():
    """ Delete record handling function for table Currencies """

    logger.debug('Enter: forms_Currencies_delete()')
    Cur_Code  =  request.args.get('Cur_Code',0,type=int)
    row =  currency.query.filter(currency.Cur_Code == Cur_Code).first()
    if row is None:
        row=currency()
    session['data'] =  { 'Cur_Code':row.Cur_Code, 'Cur_Name':row.Cur_Name, 'Cur_Id':row.Cur_Id, 'Cur_Comment':row.Cur_Comment}
    form = frm_currency_delete()

    if form.validate_on_submit():
        if  form.submit_Delete.data:
            print('Delete Data Here...')
            print('Delete Data Here...')
            try:
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                flash('Record %s deleted OK'%(Cur_Code))
            except exc.IntegrityError as e:
                db.session.rollback()
                flash('INTEGRITY ERROR: Are you sure there are no dependant records in other tables?')
                return redirect(url_for('.forms_Currencies_delete',Cur_Code=session['data']['Cur_Code']))

            return redirect(url_for('.select_Currencies_query'))
        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
            return redirect(url_for('.select_Currencies_query'))
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.select_Currencies_query'))


    return render_template('currencies_delete.html',C=C, form=form, data=session.get('data'),row=row)

# =============================================================================

@main.route('/select/Currencies_Query', methods=['GET','POST'])
@login_required
@admin_required
def select_Currencies_query():
    """ Select rows handling function for table Currencies """

    logger.debug('Enter: select_Currencies_query()')
    field =  request.args.get('field',None,type=str)
    value =  request.args.get('value',0,type=str)
    page  =  request.args.get('page',1,type=int)

    if field is not None:
        if   field == 'Cur_Code':
            rows =  currency.query.filter_by(Cur_Code=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Cur_Name':
            rows =  currency.query.filter_by(Cur_Name=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Cur_Id':
            rows =  currency.query.filter_by(Cur_Id=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Cur_Comment':
            rows =  currency.query.filter_by(Cur_Comment=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
    else:
       rows =  currency.query\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)

    next_url = url_for('.select_Currencies_query', page=rows.next_num) \
        if rows.has_next else None
    prev_url = url_for('.select_Currencies_query', page=rows.prev_num) \
        if rows.has_prev else None

    return render_template('currencies_All.html',C=C,rows=rows.items,next_url=next_url,prev_url=prev_url)
# =============================================================================

