# =============================================================================

# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-11-30 16:47:18
# =============================================================================


@main.route('/forms/Measure_Units', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@permission_required(Permission.MODIFY)
@admin_required
def forms_Measure_Units():
    """ Form handling function for table Measure_Units """

    logger.debug('Enter: forms_Measure_Units()')
    MU_Code  =  request.args.get('MU_Code',0,type=int)
    row =  measure_unit.query.filter(measure_unit.MU_Code == MU_Code).first()
    if row is None:
        row=measure_unit()

    session['data'] =  { 'MU_Code':row.MU_Code, 'MU_Description':row.MU_Description}
    form = frm_measure_unit()

    if form.validate_on_submit():
        if     form.submit_Save.data:
            row.MU_Code = form.MU_Code.data
            row.MU_Description = form.MU_Description.data
            try:
               db.session.close()
               db.session.add(row)
               db.session.commit()
               db.session.close()
               flash('Record %s saved OK'%(MU_Code))
            except Exception as e:
               db.session.rollback()
               db.session.close()
               flash('ERROR saving record : %s'%(e))
            return redirect(url_for('.select_Measure_Units_query'))
        elif   form.submit_New.data:
            print('New Data Here...')
            db.session.close()
            row=measure_unit()
            return redirect(url_for('.forms_Measure_Units'))

        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.forms_Measure_Units'))

    form.MU_Code.data = row.MU_Code
    form.MU_Description.data = row.MU_Description
    return render_template('measure_units.html', form=form, row=row)

# =============================================================================

@main.route('/forms/Measure_Units_delete', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@admin_required
def forms_Measure_Units_delete():
    """ Delete record handling function for table Measure_Units """

    logger.debug('Enter: forms_Measure_Units_delete()')
    MU_Code  =  request.args.get('MU_Code',0,type=int)
    row =  measure_unit.query.filter(measure_unit.MU_Code == MU_Code).first()
    if row is None:
        row=measure_unit()
    session['data'] =  { 'MU_Code':row.MU_Code, 'MU_Description':row.MU_Description}
    form = frm_measure_unit_delete()

    if form.validate_on_submit():
        if  form.submit_Delete.data:
            print('Delete Data Here...')
            print('Delete Data Here...')
            try:
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                flash('Record %s deleted OK'%(MU_Code))
            except exc.IntegrityError as e:
                db.session.rollback()
                flash('INTEGRITY ERROR: Are you sure there are no dependant records in other tables?')
                return redirect(url_for('.forms_Measure_Units_delete',MU_Code=session['data']['MU_Code']))

            return redirect(url_for('.select_Measure_Units_query'))
        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
            return redirect(url_for('.select_Measure_Units_query'))
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.select_Measure_Units_query'))


    return render_template('measure_units_delete.html',C=C, form=form, data=session.get('data'),row=row)

# =============================================================================

@main.route('/select/Measure_Units_Query', methods=['GET','POST'])
@login_required
@admin_required
def select_Measure_Units_query():
    """ Select rows handling function for table Measure_Units """

    logger.debug('Enter: select_Measure_Units_query()')
    field =  request.args.get('field',None,type=str)
    value =  request.args.get('value',0,type=str)
    page  =  request.args.get('page',1,type=int)

    if field is not None:
        if   field == 'MU_Code':
            rows =  measure_unit.query.filter_by(MU_Code=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'MU_Description':
            rows =  measure_unit.query.filter_by(MU_Description=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
    else:
       rows =  measure_unit.query\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)

    next_url = url_for('.select_Measure_Units_query', page=rows.next_num) \
        if rows.has_next else None
    prev_url = url_for('.select_Measure_Units_query', page=rows.prev_num) \
        if rows.has_prev else None

    return render_template('measure_units_All.html',C=C,rows=rows.items,next_url=next_url,prev_url=prev_url)
# =============================================================================

