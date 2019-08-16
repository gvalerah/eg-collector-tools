# =============================================================================

# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-11-30 16:47:18
# =============================================================================


@main.route('/forms/CU_Types', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@permission_required(Permission.MODIFY)
@admin_required
def forms_CU_Types():
    """ Form handling function for table CU_Types """

    logger.debug('Enter: forms_CU_Types()')
    Typ_Code  =  request.args.get('Typ_Code',0,type=int)
    row =  cu_type.query.filter(cu_type.Typ_Code == Typ_Code).first()
    if row is None:
        row=cu_type()

    session['data'] =  { 'Typ_Code':row.Typ_Code, 'Typ_Description':row.Typ_Description}
    form = frm_cu_type()

    if form.validate_on_submit():
        if     form.submit_Save.data:
            row.Typ_Code = form.Typ_Code.data
            row.Typ_Description = form.Typ_Description.data
            try:
               db.session.close()
               db.session.add(row)
               db.session.commit()
               db.session.close()
               flash('Record %s saved OK'%(Typ_Code))
            except Exception as e:
               db.session.rollback()
               db.session.close()
               flash('ERROR saving record : %s'%(e))
            return redirect(url_for('.select_CU_Types_query'))
        elif   form.submit_New.data:
            print('New Data Here...')
            db.session.close()
            row=cu_type()
            return redirect(url_for('.forms_CU_Types'))

        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.forms_CU_Types'))

    form.Typ_Code.data = row.Typ_Code
    form.Typ_Description.data = row.Typ_Description
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
            print('Delete Data Here...')
            try:
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                flash('Record %s deleted OK'%(Typ_Code))
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


    return render_template('cu_types_delete.html',C=C, form=form, data=session.get('data'),row=row)

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

    next_url = url_for('.select_CU_Types_query', page=rows.next_num) \
        if rows.has_next else None
    prev_url = url_for('.select_CU_Types_query', page=rows.prev_num) \
        if rows.has_prev else None

    return render_template('cu_types_All.html',C=C,rows=rows.items,next_url=next_url,prev_url=prev_url)
# =============================================================================

