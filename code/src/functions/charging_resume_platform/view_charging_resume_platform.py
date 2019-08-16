# =============================================================================
# View for Get Charging Resume from DB
# (c) Sertechno 2018
# GLVH @ 2019-08-16
# =============================================================================

from emtec.collector.forms       import frm_charging_resume_platform
from babel.numbers  import format_number, format_decimal, format_percent

@main.route('/forms/Get_Charging_Resume_Platform', methods=['GET', 'POST'])
@login_required
def forms_Get_Charging_Resume_Platform():
    logger.debug('Enter: forms_Get_Charging_Resume_Platform()')

    session['data'] =  { 'Pla_Id': None, 'CIT_Date_From':None, 'CIT_Date_To':None, 'CIT_Status':1,'Cur_Code':'USD'}

    form = frm_charging_resume_platform()

    # ------------------------------------------------------------------------------
    # Will setup filter to consider only Currencies with actual Exchange Rates in DB
    # Prepare query
    query = db.session.query(exchange_rate.Cur_Code.distinct().label('Cur_Code'))
    # Execute query and convert in list for further use in choices selection
    cur_choices = [row.Cur_Code for row in query.all()]

    form.Pla_Id.choices     = db.session.query(platform.Pla_Id,platform.Pla_Name).all()
    form.CIT_Status.choices = db.session.query(cit_status.CIT_Status,cit_status.Value).all()
    form.Cur_Code.choices   = db.session.query(currency.Cur_Code,currency.Cur_Name).filter(currency.Cur_Code.in_(cur_choices)).all()

    if form.validate_on_submit():
        session['data']['Pla_Id'        ] = form.Pla_Id.data
        session['data']['CIT_Date_From' ] = form.CIT_Date_From.data
        session['data']['CIT_Date_To'   ] = form.CIT_Date_To.data
        session['data']['CIT-Status'    ] = form.CIT_Status.data
        session['data']['Cur_Code'      ] = form.Cur_Code.data
        if     form.submit_Report.data:
            # Get the Selected options index for string lists
            for i in range(len(form.Pla_Id.choices)):
                if form.Pla_Id.choices[i][0]==form.Pla_Id.data:
                    pla_index=i
            for i in range(len(form.Cur_Code.choices)):
                if form.Cur_Code.choices[i][0]==form.Cur_Code.data:
                    cur_index=i
            return redirect(url_for('.report_Charging_Resume_Platform',
                                Pla_Id          = form.Pla_Id.data,
                                Pla_Name        = form.Pla_Id.choices[pla_index][1],
                                CIT_Date_From   = form.CIT_Date_From.data,
                                CIT_Date_To     = form.CIT_Date_To.data,
                                CIT_Status      = form.CIT_Status.data,
                                CIT_Status_Value= form.CIT_Status.choices[form.CIT_Status.data-1][1],
                                Cur_Code        = form.Cur_Code.data,
                                Cur_Name        = form.Cur_Code.choices[cur_index][1],
                                Update          = 0
                                ))
        if     form.submit_Update.data:
            # Get the Selected options index for string lists
            for i in range(len(form.Pla_Id.choices)):
                if form.Pla_Id.choices[i][0]==form.Pla_Id.data:
                    pla_index=i
            for i in range(len(form.Cur_Code.choices)):
                if form.Cur_Code.choices[i][0]==form.Cur_Code.data:
                    cur_index=i
            return redirect(url_for('.report_Charging_Resume_Platform',
                                Pla_Id          = form.Pla_Id.data,
                                Pla_Name        = form.Pla_Id.choices[pla_index][1],
                                CIT_Date_From   = form.CIT_Date_From.data,
                                CIT_Date_To     = form.CIT_Date_To.data,
                                CIT_Status      = form.CIT_Status.data,
                                CIT_Status_Value= form.CIT_Status.choices[form.CIT_Status.data-1][1],
                                Cur_Code        = form.Cur_Code.data,
                                Cur_Name        = form.Cur_Code.choices[cur_index][1],
                                Update          = 1
                                ))

        elif   form.submit_Cancel.data:
            #print('Cancel Data Here ... does nothing')
            flash('Report discarded ...')
        else:
            flash('form validated but not submited. Report to Support ...')
            #print('form validated but not submited ???')
        return redirect(url_for('.forms_Get_Charging_Resume_Platform'))

    form.Pla_Id.data        = session['data']['Pla_Id']
    form.CIT_Date_From.data = session['data']['CIT_Date_From']
    form.CIT_Date_To.data   = session['data']['CIT_Date_To']
    form.CIT_Status.data    = session['data']['CIT_Status']
    form.Cur_Code.data      = session['data']['Cur_Code']

    return render_template('get_charging_resume.html',form=form, data=session.get('data'))

# =============================================================================

import simplejson as json

@main.route('/report/Charging_Resume_Platform', methods=['GET','POST'])
@login_required
def report_Charging_Resume_Platform():
    logger.debug('Enter: report_Charging_Resume_Platform()')
    Pla_Id          =  request.args.get('Pla_Id',None,type=int)
    Pla_Name        =  request.args.get('Pla_Name',None,type=str)
    CIT_Date_From   =  request.args.get('CIT_Date_From',None,type=str)
    CIT_Date_To     =  request.args.get('CIT_Date_To',None,type=str)
    CIT_Status      =  request.args.get('CIT_Status',None,type=int)
    CIT_Status_Value=  request.args.get('CIT_Status_Value',None,type=str)
    Cur_Code        =  request.args.get('Cur_Code',None,type=str)
    Cur_Name        =  request.args.get('Cur_Name',None,type=str)
    Update          =  request.args.get('Update',0,type=int)
    
    
    # Updated cached data for this specific query if requested 
    if Update == 1:
        # -------------------------------------------------------------------------------------------------------------- #
        # Previous Code faster but requires more memory will be replaced by an by CI loop                                #
        # query="CALL Update_Charge_Resume(%d,'%s','%s',%d,'%s')"%(Pla_Id,CIT_Date_From,CIT_Date_To,CIT_Status,Cur_Code) #
        # resume_records = db.engine.execute(query).scalar()                                                             #
        # -------------------------------------------------------------------------------------------------------------- #
        # 20181228 GV query = "SELECT DISTINCT CI_Id FROM Configuration_Items WHERE Pla_Id=%d"%(Pla_Id)
        query = "SELECT CI_Id FROM Configuration_Items WHERE Pla_Id=%d ORDER BY CC_Id,CI_Id"%(Pla_Id)
        
        logger.debug ("report_Changing_Resume_Platform: query: %s"%(query))

        CI = db.engine.execute(query)

        logger.debug ("report_Changing_Resume_Platform: %d CI's found for platform %d"%(CI.rowcount,Pla_Id))
        
        resume_records=0

        for ci in CI:
            query="CALL Update_Charge_Resume_CI2('%s','%s',%s,'%s',%s)"%\
                    (CIT_Date_From,CIT_Date_To,CIT_Status,Cur_Code,ci.CI_Id)
            logger.debug ("report_Changing_Resume_Platform: query: %s"%query)
            records=db.engine.execute(query)
            resume_records += records.scalar()

        logger.debug ("report_Changing_Resume_Platform: resume_records = %s"%resume_records)
        
    # Get Actual Remume Data from Database
    # NOTE: Here needs some Sand-Clock Message or something in case it takes so long ...
    query="CALL Get_Charge_Resume2(3,%d,'%s','%s',%d,'%s')"%(Pla_Id,CIT_Date_From,CIT_Date_To,CIT_Status,Cur_Code)
    
    logger.debug ("report_Changing_Resume: query: %s"%query)
    
    rows =  db.engine.execute(query).fetchall()
    
    return render_template('report_charging_resume_platform.html',rows=rows,
                Pla_Id=Pla_Id,
                Pla_Name=Pla_Name,
                CIT_Date_From=CIT_Date_From,
                CIT_Date_To=CIT_Date_To,
                CIT_Status=CIT_Status,
                CIT_Status_Value=CIT_Status_Value,                
                Cur_Code=Cur_Code,
                Cur_Name=Cur_Name
                )

