# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-18 18:05:34
# =============================================================================

@main.route('/forms/Charge_Resumes', methods=['GET', 'POST'])
@login_required
def forms_Charge_Resumes():
    """ Form handling function for table Charge_Resumes """

    logger.debug('Enter: forms_Charge_Resumes()')
    Cus_Id  =  request.args.get('Cus_Id',0,type=int)
    CR_Date_From  =  request.args.get('CR_Date_From',0,type=int)
    CR_Date_To  =  request.args.get('CR_Date_To',0,type=int)
    CIT_Status  =  request.args.get('CIT_Status',0,type=int)
    Cur_Code  =  request.args.get('Cur_Code',0,type=int)
    CU_Id  =  request.args.get('CU_Id',0,type=int)
    row =  charge_resume.query.filter(charge_resume.Cus_Id == Cus_Id,charge_resume.CR_Date_From == CR_Date_From,charge_resume.CR_Date_To == CR_Date_To,charge_resume.CIT_Status == CIT_Status,charge_resume.Cur_Code == Cur_Code,charge_resume.CU_Id == CU_Id).first()
    if row is None:
        row=charge_resume()
        session['is_new_row']=True

    session['data'] =  { 'Cus_Id':row.Cus_Id, 'CR_Date_From':row.CR_Date_From, 'CR_Date_To':row.CR_Date_To, 'CIT_Status':row.CIT_Status, 'Cur_Code':row.Cur_Code, 'CIT_Count':row.CIT_Count, 'CIT_Quantity':row.CIT_Quantity, 'CIT_Generation':row.CIT_Generation, 'CU_Id':row.CU_Id, 'CI_CC_Id':row.CI_CC_Id, 'CU_Operation':row.CU_Operation, 'Typ_Code':row.Typ_Code, 'CC_Cur_Code':row.CC_Cur_Code, 'CI_Id':row.CI_Id, 'Rat_Id':row.Rat_Id, 'Rat_Price':row.Rat_Price, 'Rat_MU_Code':row.Rat_MU_Code, 'Rat_Cur_Code':row.Rat_Cur_Code, 'Rat_Period':row.Rat_Period, 'Rat_Hourly':row.Rat_Hourly, 'Rat_Daily':row.Rat_Daily, 'Rat_Monthly':row.Rat_Monthly, 'CR_Quantity':row.CR_Quantity, 'CR_Quantity_at_Rate':row.CR_Quantity_at_Rate, 'CC_XR':row.CC_XR, 'CR_Cur_XR':row.CR_Cur_XR, 'CR_ST_at_Rate_Cur':row.CR_ST_at_Rate_Cur, 'CR_ST_at_CC_Cur':row.CR_ST_at_CC_Cur, 'CR_ST_at_Cur':row.CR_ST_at_Cur, 'Cus_Name':row.Cus_Name, 'CI_Name':row.CI_Name, 'CU_Description':row.CU_Description, 'CC_Description':row.CC_Description, 'Rat_Period_Description':row.Rat_Period_Description, 'Pla_Id':row.Pla_Id}
    form = frm_charge_resume()

    if form.validate_on_submit():
        if     form.submit_Save.data and current_user.role_id>1:
            row.Cus_Id = form.Cus_Id.data
            row.CR_Date_From = form.CR_Date_From.data
            row.CR_Date_To = form.CR_Date_To.data
            row.CIT_Status = form.CIT_Status.data
            row.Cur_Code = form.Cur_Code.data
            row.CIT_Count = form.CIT_Count.data
            row.CIT_Quantity = form.CIT_Quantity.data
            row.CIT_Generation = form.CIT_Generation.data
            row.CU_Id = form.CU_Id.data
            row.CI_CC_Id = form.CI_CC_Id.data
            row.CU_Operation = form.CU_Operation.data
            row.Typ_Code = form.Typ_Code.data
            row.CC_Cur_Code = form.CC_Cur_Code.data
            row.CI_Id = form.CI_Id.data
            row.Rat_Id = form.Rat_Id.data
            row.Rat_Price = form.Rat_Price.data
            row.Rat_MU_Code = form.Rat_MU_Code.data
            row.Rat_Cur_Code = form.Rat_Cur_Code.data
            row.Rat_Period = form.Rat_Period.data
            row.Rat_Hourly = form.Rat_Hourly.data
            row.Rat_Daily = form.Rat_Daily.data
            row.Rat_Monthly = form.Rat_Monthly.data
            row.CR_Quantity = form.CR_Quantity.data
            row.CR_Quantity_at_Rate = form.CR_Quantity_at_Rate.data
            row.CC_XR = form.CC_XR.data
            row.CR_Cur_XR = form.CR_Cur_XR.data
            row.CR_ST_at_Rate_Cur = form.CR_ST_at_Rate_Cur.data
            row.CR_ST_at_CC_Cur = form.CR_ST_at_CC_Cur.data
            row.CR_ST_at_Cur = form.CR_ST_at_Cur.data
            row.Cus_Name = form.Cus_Name.data
            row.CI_Name = form.CI_Name.data
            row.CU_Description = form.CU_Description.data
            row.CC_Description = form.CC_Description.data
            row.Rat_Period_Description = form.Rat_Period_Description.data
            row.Pla_Id = form.Pla_Id.data
            try:
               session['new_row']=str(row)
               db.session.close()
               db.session.add(row)
               db.session.commit()
               if session['is_new_row']==True:
                   logger.audit ( '%s:NEW:%s' % (current_user.username,session['new_row'] ) )
                   flash('New Charge Resume created OK')
               else:
                   logger.audit ( '%s:OLD:%s' % (current_user.username,session['prev_row']) )
                   logger.audit ( '%s:UPD:%s' % (current_user.username,session['new_row'] ) )
                   message=Markup('<b>Charge Resume %s saved OK</b>'%(Cus_Id,CR_Date_From,CR_Date_To,CIT_Status,Cur_Code,CU_Id))
                   flash(message)
               db.session.close()
            except Exception as e:
               db.session.rollback()
               db.session.close()
               message=Markup('ERROR saving Charge Resume record : %s'%(e))
               flash(message)
            return redirect(url_for('.select_Charge_Resumes_query'))
        elif   form.submit_New.data and current_user.role_id>1:
            #print('New Data Here ...')
            session['is_new_row']=True
            db.session.close()
            row=charge_resume()
            return redirect(url_for('.forms_Charge_Resumes'))

        elif   form.submit_Cancel.data:
            #print('Cancel Data Here ... does nothing')
            message=Markup('Charge Resume Record modifications discarded ...')
            flash(message)
        else:
            #print('form validated but not submited ???')
            message=Markup('<b>Charge Resume data modifications not allowed for user \'%s\'. Please contact Collector\'s Administrator ...</b>'%(current_user.username))
            flash(message)
            return redirect(url_for('.forms_Charge_Resumes'))

    form.Cus_Id.data = row.Cus_Id
    form.CR_Date_From.data = row.CR_Date_From
    form.CR_Date_To.data = row.CR_Date_To
    form.CIT_Status.data = row.CIT_Status
    form.Cur_Code.data = row.Cur_Code
    form.CIT_Count.data = row.CIT_Count
    form.CIT_Quantity.data = row.CIT_Quantity
    form.CIT_Generation.data = row.CIT_Generation
    form.CU_Id.data = row.CU_Id
    form.CI_CC_Id.data = row.CI_CC_Id
    form.CU_Operation.data = row.CU_Operation
    form.Typ_Code.data = row.Typ_Code
    form.CC_Cur_Code.data = row.CC_Cur_Code
    form.CI_Id.data = row.CI_Id
    form.Rat_Id.data = row.Rat_Id
    form.Rat_Price.data = row.Rat_Price
    form.Rat_MU_Code.data = row.Rat_MU_Code
    form.Rat_Cur_Code.data = row.Rat_Cur_Code
    form.Rat_Period.data = row.Rat_Period
    form.Rat_Hourly.data = row.Rat_Hourly
    form.Rat_Daily.data = row.Rat_Daily
    form.Rat_Monthly.data = row.Rat_Monthly
    form.CR_Quantity.data = row.CR_Quantity
    form.CR_Quantity_at_Rate.data = row.CR_Quantity_at_Rate
    form.CC_XR.data = row.CC_XR
    form.CR_Cur_XR.data = row.CR_Cur_XR
    form.CR_ST_at_Rate_Cur.data = row.CR_ST_at_Rate_Cur
    form.CR_ST_at_CC_Cur.data = row.CR_ST_at_CC_Cur
    form.CR_ST_at_Cur.data = row.CR_ST_at_Cur
    form.Cus_Name.data = row.Cus_Name
    form.CI_Name.data = row.CI_Name
    form.CU_Description.data = row.CU_Description
    form.CC_Description.data = row.CC_Description
    form.Rat_Period_Description.data = row.Rat_Period_Description
    form.Pla_Id.data = row.Pla_Id
    session['prev_row']=str(row)
    session['is_new_row']=False
    return render_template('charge_resumes.html', form=form, row=row)

# =============================================================================
@main.route('/forms/Charge_Resumes_delete', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.DELETE)
def forms_Charge_Resumes_delete():
    """ Delete record handling function for table Charge_Resumes """

    logger.debug('Enter: forms_Charge_Resumes_delete()')
    Cus_Id  =  request.args.get('Cus_Id',0,type=int)
    CR_Date_From  =  request.args.get('CR_Date_From',0,type=int)
    CR_Date_To  =  request.args.get('CR_Date_To',0,type=int)
    CIT_Status  =  request.args.get('CIT_Status',0,type=int)
    Cur_Code  =  request.args.get('Cur_Code',0,type=int)
    CU_Id  =  request.args.get('CU_Id',0,type=int)
    row =  charge_resume.query.filter(charge_resume.Cus_Id == Cus_Id,charge_resume.CR_Date_From == CR_Date_From,charge_resume.CR_Date_To == CR_Date_To,charge_resume.CIT_Status == CIT_Status,charge_resume.Cur_Code == Cur_Code,charge_resume.CU_Id == CU_Id).first()
    if row is None:
        row=charge_resume()
    session['data'] =  { 'Cus_Id':row.Cus_Id, 'CR_Date_From':row.CR_Date_From, 'CR_Date_To':row.CR_Date_To, 'CIT_Status':row.CIT_Status, 'Cur_Code':row.Cur_Code, 'CIT_Count':row.CIT_Count, 'CIT_Quantity':row.CIT_Quantity, 'CIT_Generation':row.CIT_Generation, 'CU_Id':row.CU_Id, 'CI_CC_Id':row.CI_CC_Id, 'CU_Operation':row.CU_Operation, 'Typ_Code':row.Typ_Code, 'CC_Cur_Code':row.CC_Cur_Code, 'CI_Id':row.CI_Id, 'Rat_Id':row.Rat_Id, 'Rat_Price':row.Rat_Price, 'Rat_MU_Code':row.Rat_MU_Code, 'Rat_Cur_Code':row.Rat_Cur_Code, 'Rat_Period':row.Rat_Period, 'Rat_Hourly':row.Rat_Hourly, 'Rat_Daily':row.Rat_Daily, 'Rat_Monthly':row.Rat_Monthly, 'CR_Quantity':row.CR_Quantity, 'CR_Quantity_at_Rate':row.CR_Quantity_at_Rate, 'CC_XR':row.CC_XR, 'CR_Cur_XR':row.CR_Cur_XR, 'CR_ST_at_Rate_Cur':row.CR_ST_at_Rate_Cur, 'CR_ST_at_CC_Cur':row.CR_ST_at_CC_Cur, 'CR_ST_at_Cur':row.CR_ST_at_Cur, 'Cus_Name':row.Cus_Name, 'CI_Name':row.CI_Name, 'CU_Description':row.CU_Description, 'CC_Description':row.CC_Description, 'Rat_Period_Description':row.Rat_Period_Description, 'Pla_Id':row.Pla_Id}
    form = frm_charge_resume_delete()

    if form.validate_on_submit():
        if  form.submit_Delete.data:
            print('Delete Data Here...')
            try:
                session['deleted_row']=str(row)
                db.session.close()
                db.session.delete(row)
                db.session.commit()
                logger.audit ( '%s:DEL:%s' % (current_user.username,session['deleted_row']) )
                flash('Charge Resume %s deleted OK'%(Cus_Id,CR_Date_From,CR_Date_To,CIT_Status,Cur_Code,CU_Id))
            except exc.IntegrityError as e:
                db.session.rollback()
                flash('INTEGRITY ERROR: Are you sure there are no dependant records in other tables?')
                return redirect(url_for('.forms_Charge_Resumes_delete',Cus_Id=session['data']['Cus_Id'],CR_Date_From=session['data']['CR_Date_From'],CR_Date_To=session['data']['CR_Date_To'],CIT_Status=session['data']['CIT_Status'],Cur_Code=session['data']['Cur_Code'],CU_Id=session['data']['CU_Id']))

            return redirect(url_for('.select_Charge_Resumes_query'))
        elif   form.submit_Cancel.data:
            print('Cancel Data Here ... does nothing')
            flash('Record modifications discarded ...')
            return redirect(url_for('.select_Charge_Resumes_query'))
        else:
            print('form validated but not submited ???')
            return redirect(url_for('.select_Charge_Resumes_query'))


    return render_template('charge_resumes_delete.html', form=form, data=session.get('data'),row=row)

# =============================================================================
@main.route('/select/Charge_Resumes_Query', methods=['GET','POST'])
@login_required
def select_Charge_Resumes_query():
    """ Select rows handling function for table Charge_Resumes """

    logger.debug('Enter: select_Charge_Resumes_query()')
    field =  request.args.get('field',None,type=str)
    value =  request.args.get('value',0,type=str)
    page  =  request.args.get('page',1,type=int)

    if field is not None:
        if   field == 'Cus_Id':
            rows =  charge_resume.query.filter_by(Cus_Id=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CR_Date_From':
            rows =  charge_resume.query.filter_by(CR_Date_From=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CR_Date_To':
            rows =  charge_resume.query.filter_by(CR_Date_To=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CIT_Status':
            rows =  charge_resume.query.filter_by(CIT_Status=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Cur_Code':
            rows =  charge_resume.query.filter_by(Cur_Code=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CIT_Count':
            rows =  charge_resume.query.filter_by(CIT_Count=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CIT_Quantity':
            rows =  charge_resume.query.filter_by(CIT_Quantity=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CIT_Generation':
            rows =  charge_resume.query.filter_by(CIT_Generation=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CU_Id':
            rows =  charge_resume.query.filter_by(CU_Id=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CI_CC_Id':
            rows =  charge_resume.query.filter_by(CI_CC_Id=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CU_Operation':
            rows =  charge_resume.query.filter_by(CU_Operation=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Typ_Code':
            rows =  charge_resume.query.filter_by(Typ_Code=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CC_Cur_Code':
            rows =  charge_resume.query.filter_by(CC_Cur_Code=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CI_Id':
            rows =  charge_resume.query.filter_by(CI_Id=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Rat_Id':
            rows =  charge_resume.query.filter_by(Rat_Id=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Rat_Price':
            rows =  charge_resume.query.filter_by(Rat_Price=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Rat_MU_Code':
            rows =  charge_resume.query.filter_by(Rat_MU_Code=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Rat_Cur_Code':
            rows =  charge_resume.query.filter_by(Rat_Cur_Code=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Rat_Period':
            rows =  charge_resume.query.filter_by(Rat_Period=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Rat_Hourly':
            rows =  charge_resume.query.filter_by(Rat_Hourly=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Rat_Daily':
            rows =  charge_resume.query.filter_by(Rat_Daily=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Rat_Monthly':
            rows =  charge_resume.query.filter_by(Rat_Monthly=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CR_Quantity':
            rows =  charge_resume.query.filter_by(CR_Quantity=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CR_Quantity_at_Rate':
            rows =  charge_resume.query.filter_by(CR_Quantity_at_Rate=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CC_XR':
            rows =  charge_resume.query.filter_by(CC_XR=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CR_Cur_XR':
            rows =  charge_resume.query.filter_by(CR_Cur_XR=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CR_ST_at_Rate_Cur':
            rows =  charge_resume.query.filter_by(CR_ST_at_Rate_Cur=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CR_ST_at_CC_Cur':
            rows =  charge_resume.query.filter_by(CR_ST_at_CC_Cur=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CR_ST_at_Cur':
            rows =  charge_resume.query.filter_by(CR_ST_at_Cur=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Cus_Name':
            rows =  charge_resume.query.filter_by(Cus_Name=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CI_Name':
            rows =  charge_resume.query.filter_by(CI_Name=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CU_Description':
            rows =  charge_resume.query.filter_by(CU_Description=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'CC_Description':
            rows =  charge_resume.query.filter_by(CC_Description=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Rat_Period_Description':
            rows =  charge_resume.query.filter_by(Rat_Period_Description=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
        elif field == 'Pla_Id':
            rows =  charge_resume.query.filter_by(Pla_Id=value)\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)
    else:
       rows =  charge_resume.query\
               .paginate(page, per_page=current_app.config['LINES_PER_PAGE'], error_out=False)

    if field is not None:
       next_url = url_for('.select_Charge_Resumes_query', field=field, value=value, page=rows.next_num) \
           if rows.has_next else None
       prev_url = url_for('.select_Charge_Resumes_query', field=field, value=value, page=rows.prev_num) \
           if rows.has_prev else None

    else:
       next_url = url_for('.select_Charge_Resumes_query', page=rows.next_num) \
           if rows.has_next else None
       prev_url = url_for('.select_Charge_Resumes_query', page=rows.prev_num) \
           if rows.has_prev else None

    return render_template('charge_resumes_All.html',rows=rows)
# =============================================================================
