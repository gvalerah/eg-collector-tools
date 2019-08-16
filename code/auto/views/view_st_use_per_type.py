# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-16 15:51:37
# =============================================================================

@main.route('/forms/ST_Use_Per_Type', methods=['GET', 'POST'])
@login_required
@admin_required
def forms_ST_Use_Per_Type():
    """ Form handling function for table ST_Use_Per_Type """

    logger.debug('Enter: forms_ST_Use_Per_Type()')
    Typ_Code  =  request.args.get('Typ_Code',0,type=int)
    Cus_Id  =  request.args.get('Cus_Id',0,type=int)
    Pla_Id  =  request.args.get('Pla_Id',0,type=int)
    CC_Id  =  request.args.get('CC_Id',0,type=int)
    CI_Id  =  request.args.get('CI_Id',0,type=int)
    Year  =  request.args.get('Year',0,type=int)
    Month  =  request.args.get('Month',0,type=int)
    row =  st_use_per_type.query.filter(st_use_per_type.Typ_Code == Typ_Code,st_use_per_type.Cus_Id == Cus_Id,st_use_per_type.Pla_Id == Pla_Id,st_use_per_type.CC_Id == CC_Id,st_use_per_type.CI_Id == CI_Id,st_use_per_type.Year == Year,st_use_per_type.Month == Month).first()
    if row is None:
        row=st_use_per_type()
        session['is_new_row']=True

    session['data'] =  { 'Typ_Code':row.Typ_Code, 'Cus_Id':row.Cus_Id, 'Pla_Id':row.Pla_Id, 'CC_Id':row.CC_Id, 'CI_Id':row.CI_Id, 'Year':row.Year, 'Month':row.Month, 'Count':row.Count, 'Mean':row.Mean, 'Variance':row.Variance, 'StdDev':row.StdDev, 'Min':row.Min, 'Max':row.Max}
    form = frm_st_use_per_type()

    if form.validate_on_submit():
        if     form.submit_Save.data and current_user.role_id>1:
            row.Typ_Code = form.Typ_Code.data
            row.Cus_Id = form.Cus_Id.data
            row.Pla_Id = form.Pla_Id.data
            row.CC_Id = form.CC_Id.data
            row.CI_Id = form.CI_Id.data
            row.Year = form.Year.data
            row.Month = form.Month.data
            row.Count = form.Count.data
            row.Mean = form.Mean.data
            row.Variance = form.Variance.data
            row.StdDev = form.StdDev.data
            row.Min = form.Min.data
            row.Max = form.Max.data
            try:
               session['new_row']=str(row)
               db.session.close()
               db.session.add(row)
               db.session.commit()
               if session['is_new_row']==True:
                   logger.audit ( '%s:NEW:%s' % (current_user.username,session['new_row'] ) )
                   flash('New ST_Use_Per_Type created OK')
               else:
                   logger.audit ( '%s:OLD:%s' % (current_user.username,session['prev_row']) )
                   logger.audit ( '%s:UPD:%s' % (current_user.username,session['new_row'] ) )
                   message=Markup('<b>ST_Use_Per_Type %s saved OK</b>'%(Typ_Code,Cus_Id,Pla_Id,CC_Id,CI_Id,Year,Month))
                   flash(message)
               db.session.close()
            except Exception as e:
               db.session.rollback()
               db.session.close()
               message=Markup('ERROR saving ST_Use_Per_Type record : %s'%(e))
               flash(message)
            return redirect(url_for('.select_ST_Use_Per_Type_query'))
        elif   form.submit_New.data and current_user.role_id>1:
            #print('New Data Here ...')
            session['is_new_row']=True
            db.session.close()
            row=st_use_per_type()
            return redirect(url_for('.forms_ST_Use_Per_Type'))

        elif   form.submit_Cancel.data:
            #print('Cancel Data Here ... does nothing')
            message=Markup('ST_Use_Per_Type Record modifications discarded ...')
            flash(message)
        else:
            #print('form validated but not submited ???')
            message=Markup('<b>ST_Use_Per_Type data modifications not allowed for user \'%s\'. Please contact Collector\'s Administrator ...</b>'%(current_user.username))
            flash(message)
            return redirect(url_for('.forms_ST_Use_Per_Type'))

    form.Typ_Code.data = row.Typ_Code
    form.Cus_Id.data = row.Cus_Id
    form.Pla_Id.data = row.Pla_Id
    form.CC_Id.data = row.CC_Id
    form.CI_Id.data = row.CI_Id
    form.Year.data = row.Year
    form.Month.data = row.Month
    form.Count.data = row.Count
    form.Mean.data = row.Mean
    form.Variance.data = row.Variance
    form.StdDev.data = row.StdDev
    form.Min.data = row.Min
    form.Max.data = row.Max
    session['prev_row']=str(row)
    session['is_new_row']=False
    return render_template('st_use_per_type.html', form=form, row=row)

# =============================================================================
@main.route('/forms/ST_Use_Per_Type_delete', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@admin_required
def forms_ST_Use_Per_Type_delete():
    """ Delete record handling function for table ST_Use_Per_Type """

    logger.debug('Enter: forms_ST_Use_Per_Type_delete()')
    Typ_Code  =  request.args.get('Typ_Code',0,type=int)
    Cus_Id  =  request.args.get('Cus_Id',0,type=int)
    Pla_Id  =  request.args.get('Pla_Id',0,type=int)
    CC_Id  =  request.args.get('CC_Id',0,type=int)
    CI_Id  =  request.args.get('CI_Id',0,type=int)
    Year  =  request.args.get('Year',0,type=int)
    Month  =  request.args.get('Month',0,type=int)
    row =  st_use_per_type.query.filter(st_use_per_type.Typ_Code == Typ_Code,st_use_per_type.Cus_Id == Cus_Id,st_use_per_type.Pla_Id == Pla_Id,st_use_per_type.CC_Id == CC_Id,st_use_per_type.CI_Id == CI_Id,st_use_per_type.Year == Year,st_use_per_type.Month == Month).first()
    if row is None:
        row=st_use_per_type()
    session['data'] =  { 'Typ_Code':row.Typ_Code, 'Cus_Id':row.Cus_Id, 'Pla_Id':row.Pla_Id, 'CC_Id':row.CC_Id, 'CI_Id':row.CI_Id, 'Year':row.Year, 'Month':row.Month, 'Count':row.Count, 'Mean':row.Mean, 'Variance':row.Variance, 'StdDev':row.StdDev, 'Min':row.Min, 'Max':row.Max}
    form = frm_st_use_per_type_delete()

    if form.validate_on_submit():
        if  form.submit_Delete.data:
            print('Delete Data Here...')
            try:
                session['deleted_row']=str(row)
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                logger.audit ( '%s:DEL:%s' % (current_user.username,session['deleted_row']) )
                flash('ST_Use_Per_Type %s deleted OK'%(Typ_Code,Cus_Id,Pla_Id,CC_Id,CI_Id,Year,Month))
            except exc.IntegrityError as e:
                db.session.rollback()
                flash('INTEGRITY ERROR: Are you sure there are no dependant records in other tables?')
                return redirect(url_for('.forms_ST_Use_Per_Type_delete',Typ_Code=session['data']['Typ_Code'],Cus_Id=session['data']['Cus_Id'],Pla_Id=session['data']['Pla_Id'],CC_Id=session['data']['CC_Id'],CI_Id=session['data']['CI_Id'],Year=session['data']['Year'],Month=session['data']['Month']))

            return redirect(url_for('.select_ST_Use_Per_Type_query'))
        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
            return redirect(url_for('.select_ST_Use_Per_Type_query'))
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.select_ST_Use_Per_Type_query'))


    return render_template('st_use_per_type_delete.html', form=form, data=session.get('data'),row=row)

# =============================================================================
@main.route('/select/ST_Use_Per_Type_Query', methods=['GET','POST'])
@login_required
@admin_required
def select_ST_Use_Per_Type_query():
    """ Select rows handling function for table ST_Use_Per_Type """

    logger.debug('Enter: select_ST_Use_Per_Type_query()')
    field =  request.args.get('field',None,type=str)
    value =  request.args.get('value',0,type=str)
    page  =  request.args.get('page',1,type=int)

    if field is not None:
        if   field == 'Typ_Code':
            rows =  st_use_per_type.query.filter_by(Typ_Code=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Cus_Id':
            rows =  st_use_per_type.query.filter_by(Cus_Id=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Pla_Id':
            rows =  st_use_per_type.query.filter_by(Pla_Id=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CC_Id':
            rows =  st_use_per_type.query.filter_by(CC_Id=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CI_Id':
            rows =  st_use_per_type.query.filter_by(CI_Id=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Year':
            rows =  st_use_per_type.query.filter_by(Year=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Month':
            rows =  st_use_per_type.query.filter_by(Month=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Count':
            rows =  st_use_per_type.query.filter_by(Count=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Mean':
            rows =  st_use_per_type.query.filter_by(Mean=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Variance':
            rows =  st_use_per_type.query.filter_by(Variance=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'StdDev':
            rows =  st_use_per_type.query.filter_by(StdDev=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Min':
            rows =  st_use_per_type.query.filter_by(Min=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Max':
            rows =  st_use_per_type.query.filter_by(Max=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
    else:
       rows =  st_use_per_type.query\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)

    if field is not None:
       next_url = url_for('.select_ST_Use_Per_Type_query', field=field, value=value, page=rows.next_num) \
           if rows.has_next else None
       prev_url = url_for('.select_ST_Use_Per_Type_query', field=field, value=value, page=rows.prev_num) \
           if rows.has_prev else None

    else:
       next_url = url_for('.select_ST_Use_Per_Type_query', page=rows.next_num) \
           if rows.has_next else None
       prev_url = url_for('.select_ST_Use_Per_Type_query', page=rows.prev_num) \
           if rows.has_prev else None

    return render_template('st_use_per_type_All.html',rows=rows)
# =============================================================================
