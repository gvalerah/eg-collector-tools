# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-18 18:05:34
# =============================================================================

@main.route('/forms/ST_Use_Per_CU', methods=['GET', 'POST'])
@login_required
@admin_required
def forms_ST_Use_Per_CU():
    """ Form handling function for table ST_Use_Per_CU """

    logger.debug('Enter: forms_ST_Use_Per_CU()')
    CU_Id  =  request.args.get('CU_Id',0,type=int)
    From  =  request.args.get('From',0,type=int)
    To  =  request.args.get('To',0,type=int)
    row =  st_use_per_cu.query.filter(st_use_per_cu.CU_Id == CU_Id,st_use_per_cu.From == From,st_use_per_cu.To == To).first()
    if row is None:
        row=st_use_per_cu()
        session['is_new_row']=True

    session['data'] =  { 'CU_Id':row.CU_Id, 'From':row.From, 'To':row.To, 'Total_Slices':row.Total_Slices, 'Found_Slices':row.Found_Slices, 'Not_Found_Slices':row.Not_Found_Slices, 'Period_Initial_Q':row.Period_Initial_Q, 'Period_Increase':row.Period_Increase, 'Period_Increase_Count':row.Period_Increase_Count, 'Period_Reduction':row.Period_Reduction, 'Period_Reduction_Count':row.Period_Reduction_Count, 'Period_Final_Q':row.Period_Final_Q, 'CI_Id':row.CI_Id, 'CC_Id':row.CC_Id, 'Cus_Id':row.Cus_Id, 'Rat_Id':row.Rat_Id, 'Typ_Code':row.Typ_Code, 'Pla_Id':row.Pla_Id, 'Mean':row.Mean, 'Variance':row.Variance, 'StdDev':row.StdDev, 'Min':row.Min, 'Max':row.Max}
    form = frm_st_use_per_cu()

    if form.validate_on_submit():
        if     form.submit_Save.data and current_user.role_id>1:
            row.CU_Id = form.CU_Id.data
            row.From = form.From.data
            row.To = form.To.data
            row.Total_Slices = form.Total_Slices.data
            row.Found_Slices = form.Found_Slices.data
            row.Not_Found_Slices = form.Not_Found_Slices.data
            row.Period_Initial_Q = form.Period_Initial_Q.data
            row.Period_Increase = form.Period_Increase.data
            row.Period_Increase_Count = form.Period_Increase_Count.data
            row.Period_Reduction = form.Period_Reduction.data
            row.Period_Reduction_Count = form.Period_Reduction_Count.data
            row.Period_Final_Q = form.Period_Final_Q.data
            row.CI_Id = form.CI_Id.data
            row.CC_Id = form.CC_Id.data
            row.Cus_Id = form.Cus_Id.data
            row.Rat_Id = form.Rat_Id.data
            row.Typ_Code = form.Typ_Code.data
            row.Pla_Id = form.Pla_Id.data
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
                   flash('New ST_Use_Per_CU created OK')
               else:
                   logger.audit ( '%s:OLD:%s' % (current_user.username,session['prev_row']) )
                   logger.audit ( '%s:UPD:%s' % (current_user.username,session['new_row'] ) )
                   message=Markup('<b>ST_Use_Per_CU %s saved OK</b>'%(CU_Id,From,To))
                   flash(message)
               db.session.close()
            except Exception as e:
               db.session.rollback()
               db.session.close()
               message=Markup('ERROR saving ST_Use_Per_CU record : %s'%(e))
               flash(message)
            return redirect(url_for('.select_ST_Use_Per_CU_query'))
        elif   form.submit_New.data and current_user.role_id>1:
            #print('New Data Here ...')
            session['is_new_row']=True
            db.session.close()
            row=st_use_per_cu()
            return redirect(url_for('.forms_ST_Use_Per_CU'))

        elif   form.submit_Cancel.data:
            #print('Cancel Data Here ... does nothing')
            message=Markup('ST_Use_Per_CU Record modifications discarded ...')
            flash(message)
        else:
            #print('form validated but not submited ???')
            message=Markup('<b>ST_Use_Per_CU data modifications not allowed for user \'%s\'. Please contact Collector\'s Administrator ...</b>'%(current_user.username))
            flash(message)
            return redirect(url_for('.forms_ST_Use_Per_CU'))

    form.CU_Id.data = row.CU_Id
    form.From.data = row.From
    form.To.data = row.To
    form.Total_Slices.data = row.Total_Slices
    form.Found_Slices.data = row.Found_Slices
    form.Not_Found_Slices.data = row.Not_Found_Slices
    form.Period_Initial_Q.data = row.Period_Initial_Q
    form.Period_Increase.data = row.Period_Increase
    form.Period_Increase_Count.data = row.Period_Increase_Count
    form.Period_Reduction.data = row.Period_Reduction
    form.Period_Reduction_Count.data = row.Period_Reduction_Count
    form.Period_Final_Q.data = row.Period_Final_Q
    form.CI_Id.data = row.CI_Id
    form.CC_Id.data = row.CC_Id
    form.Cus_Id.data = row.Cus_Id
    form.Rat_Id.data = row.Rat_Id
    form.Typ_Code.data = row.Typ_Code
    form.Pla_Id.data = row.Pla_Id
    form.Mean.data = row.Mean
    form.Variance.data = row.Variance
    form.StdDev.data = row.StdDev
    form.Min.data = row.Min
    form.Max.data = row.Max
    session['prev_row']=str(row)
    session['is_new_row']=False
    return render_template('st_use_per_cu.html', form=form, row=row)

# =============================================================================
@main.route('/forms/ST_Use_Per_CU_delete', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
@admin_required
def forms_ST_Use_Per_CU_delete():
    """ Delete record handling function for table ST_Use_Per_CU """

    logger.debug('Enter: forms_ST_Use_Per_CU_delete()')
    CU_Id  =  request.args.get('CU_Id',0,type=int)
    From  =  request.args.get('From',0,type=int)
    To  =  request.args.get('To',0,type=int)
    row =  st_use_per_cu.query.filter(st_use_per_cu.CU_Id == CU_Id,st_use_per_cu.From == From,st_use_per_cu.To == To).first()
    if row is None:
        row=st_use_per_cu()
    session['data'] =  { 'CU_Id':row.CU_Id, 'From':row.From, 'To':row.To, 'Total_Slices':row.Total_Slices, 'Found_Slices':row.Found_Slices, 'Not_Found_Slices':row.Not_Found_Slices, 'Period_Initial_Q':row.Period_Initial_Q, 'Period_Increase':row.Period_Increase, 'Period_Increase_Count':row.Period_Increase_Count, 'Period_Reduction':row.Period_Reduction, 'Period_Reduction_Count':row.Period_Reduction_Count, 'Period_Final_Q':row.Period_Final_Q, 'CI_Id':row.CI_Id, 'CC_Id':row.CC_Id, 'Cus_Id':row.Cus_Id, 'Rat_Id':row.Rat_Id, 'Typ_Code':row.Typ_Code, 'Pla_Id':row.Pla_Id, 'Mean':row.Mean, 'Variance':row.Variance, 'StdDev':row.StdDev, 'Min':row.Min, 'Max':row.Max}
    form = frm_st_use_per_cu_delete()

    if form.validate_on_submit():
        if  form.submit_Delete.data:
            print('Delete Data Here...')
            try:
                session['deleted_row']=str(row)
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                logger.audit ( '%s:DEL:%s' % (current_user.username,session['deleted_row']) )
                flash('ST_Use_Per_CU %s deleted OK'%(CU_Id,From,To))
            except exc.IntegrityError as e:
                db.session.rollback()
                flash('INTEGRITY ERROR: Are you sure there are no dependant records in other tables?')
                return redirect(url_for('.forms_ST_Use_Per_CU_delete',CU_Id=session['data']['CU_Id'],From=session['data']['From'],To=session['data']['To']))

            return redirect(url_for('.select_ST_Use_Per_CU_query'))
        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
            return redirect(url_for('.select_ST_Use_Per_CU_query'))
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.select_ST_Use_Per_CU_query'))


    return render_template('st_use_per_cu_delete.html', form=form, data=session.get('data'),row=row)

# =============================================================================
@main.route('/select/ST_Use_Per_CU_Query', methods=['GET','POST'])
@login_required
@admin_required
def select_ST_Use_Per_CU_query():
    """ Select rows handling function for table ST_Use_Per_CU """

    logger.debug('Enter: select_ST_Use_Per_CU_query()')
    field =  request.args.get('field',None,type=str)
    value =  request.args.get('value',0,type=str)
    page  =  request.args.get('page',1,type=int)

    if field is not None:
        if   field == 'CU_Id':
            rows =  st_use_per_cu.query.filter_by(CU_Id=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'From':
            rows =  st_use_per_cu.query.filter_by(From=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'To':
            rows =  st_use_per_cu.query.filter_by(To=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Total_Slices':
            rows =  st_use_per_cu.query.filter_by(Total_Slices=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Found_Slices':
            rows =  st_use_per_cu.query.filter_by(Found_Slices=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Not_Found_Slices':
            rows =  st_use_per_cu.query.filter_by(Not_Found_Slices=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Period_Initial_Q':
            rows =  st_use_per_cu.query.filter_by(Period_Initial_Q=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Period_Increase':
            rows =  st_use_per_cu.query.filter_by(Period_Increase=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Period_Increase_Count':
            rows =  st_use_per_cu.query.filter_by(Period_Increase_Count=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Period_Reduction':
            rows =  st_use_per_cu.query.filter_by(Period_Reduction=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Period_Reduction_Count':
            rows =  st_use_per_cu.query.filter_by(Period_Reduction_Count=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Period_Final_Q':
            rows =  st_use_per_cu.query.filter_by(Period_Final_Q=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CI_Id':
            rows =  st_use_per_cu.query.filter_by(CI_Id=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CC_Id':
            rows =  st_use_per_cu.query.filter_by(CC_Id=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Cus_Id':
            rows =  st_use_per_cu.query.filter_by(Cus_Id=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Rat_Id':
            rows =  st_use_per_cu.query.filter_by(Rat_Id=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Typ_Code':
            rows =  st_use_per_cu.query.filter_by(Typ_Code=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Pla_Id':
            rows =  st_use_per_cu.query.filter_by(Pla_Id=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Mean':
            rows =  st_use_per_cu.query.filter_by(Mean=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Variance':
            rows =  st_use_per_cu.query.filter_by(Variance=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'StdDev':
            rows =  st_use_per_cu.query.filter_by(StdDev=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Min':
            rows =  st_use_per_cu.query.filter_by(Min=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Max':
            rows =  st_use_per_cu.query.filter_by(Max=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
    else:
       rows =  st_use_per_cu.query\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)

    if field is not None:
       next_url = url_for('.select_ST_Use_Per_CU_query', field=field, value=value, page=rows.next_num) \
           if rows.has_next else None
       prev_url = url_for('.select_ST_Use_Per_CU_query', field=field, value=value, page=rows.prev_num) \
           if rows.has_prev else None

    else:
       next_url = url_for('.select_ST_Use_Per_CU_query', page=rows.next_num) \
           if rows.has_next else None
       prev_url = url_for('.select_ST_Use_Per_CU_query', page=rows.prev_num) \
           if rows.has_prev else None

    return render_template('st_use_per_cu_All.html',rows=rows)
# =============================================================================
