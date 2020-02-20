# =============================================================================
# View for Get Charging Resume from DB
# (c) Sertechno 2018
# GLVH @ 2019-08-16
# =============================================================================

from emtec.collector.forms       import frm_charging_resume_level
from babel.numbers  import format_number, format_decimal, format_percent

@main.route('/forms/Get_Charging_Resume_Level', methods=['GET', 'POST'])
@login_required
def forms_Get_Charging_Resume_Level():
    logger.debug('Enter: forms_Get_Charging_Resume()'%())

    session['data'] =  { 'Cus_Id': None, 'CIT_Date_From':None, 'CIT_Date_To':None, 'CIT_Status':1,'Cur_Code':'USD','Level':1}

    form = frm_charging_resume_level()

    # ------------------------------------------------------------------------------
    # Will setup filter to consider only Currencies with actual Exchange Rates in DB
    # Prepare query
    query = db.session.query(exchange_rate.Cur_Code.distinct().label('Cur_Code'))
    # Execute query and convert in list for further use in choices selection
    cur_choices = [row.Cur_Code for row in query.all()]

    form.Cus_Id.choices     = db.session.query(customer.Cus_Id,customer.Cus_Name).all()
    form.CIT_Status.choices = db.session.query(cit_status.CIT_Status,cit_status.Value).all()
    form.Cur_Code.choices   = db.session.query(currency.Cur_Code,currency.Cur_Name).filter(currency.Cur_Code.in_(cur_choices)).all()
    form.Level.choices      = [(1,"Cost Center"),(2,"Device"),(3,"Component")]

    if form.validate_on_submit():
        session['data']['Cus_Id'        ] = form.Cus_Id.data
        session['data']['CIT_Date_From' ] = form.CIT_Date_From.data
        session['data']['CIT_Date_To'   ] = form.CIT_Date_To.data
        session['data']['CIT-Status'    ] = form.CIT_Status.data
        session['data']['Cur_Code'      ] = form.Cur_Code.data
        session['data']['Level'         ] = form.Level.data
        
        if     form.submit_Report.data:
            # Get the Selected options index for string lists
            for i in range(len(form.Cus_Id.choices)):
                if form.Cus_Id.choices[i][0]==form.Cus_Id.data:
                    cus_index=i
            for i in range(len(form.Cur_Code.choices)):
                if form.Cur_Code.choices[i][0]==form.Cur_Code.data:
                    cur_index=i
            for i in range(len(form.Level.choices)):
                if form.Level.choices[i][0]==form.Level.data:
                    level_index=i
            return redirect(url_for('.report_Charging_Resume_Level',
                                Cus_Id          = form.Cus_Id.data,
                                Cus_Name        = form.Cus_Id.choices[cus_index][1],
                                CIT_Date_From   = form.CIT_Date_From.data,
                                CIT_Date_To     = form.CIT_Date_To.data,
                                CIT_Status      = form.CIT_Status.data,
                                CIT_Status_Value= form.CIT_Status.choices[form.CIT_Status.data-1][1],
                                Cur_Code        = form.Cur_Code.data,
                                Cur_Name        = form.Cur_Code.choices[cur_index][1],
                                Level           = form.Level.choices[level_index][1],
                                Update          = 0
                                ))
        if     form.submit_Update.data:
            # Get the Selected options index for string lists
            for i in range(len(form.Cus_Id.choices)):
                if form.Cus_Id.choices[i][0]==form.Cus_Id.data:
                    cus_index=i
            for i in range(len(form.Cur_Code.choices)):
                if form.Cur_Code.choices[i][0]==form.Cur_Code.data:
                    cur_index=i
            for i in range(len(form.Level.choices)):
                if form.Level.choices[i][0]==form.Level.data:
                    level_index=i
            return redirect(url_for('.report_Charging_Resume_Level',
                                Cus_Id          = form.Cus_Id.data,
                                Cus_Name        = form.Cus_Id.choices[cus_index][1],
                                CIT_Date_From   = form.CIT_Date_From.data,
                                CIT_Date_To     = form.CIT_Date_To.data,
                                CIT_Status      = form.CIT_Status.data,
                                CIT_Status_Value= form.CIT_Status.choices[form.CIT_Status.data-1][1],
                                Cur_Code        = form.Cur_Code.data,
                                Cur_Name        = form.Cur_Code.choices[cur_index][1],
                                Level           = form.Level.choices[level_index][1],
                                Update          = 1
                                ))

        elif   form.submit_Cancel.data:
            #print('Cancel Data Here ... does nothing')
            flash('Report discarded ...')
        else:
            flash('form validated but not submited. Report to Support ...')
            #print('form validated but not submited ???')
        return redirect(url_for('.forms_Get_Charging_Resume_Level'))

    form.Cus_Id.data        = session['data']['Cus_Id']
    form.CIT_Date_From.data = session['data']['CIT_Date_From']
    form.CIT_Date_To.data   = session['data']['CIT_Date_To']
    form.CIT_Status.data    = session['data']['CIT_Status']
    form.Cur_Code.data      = session['data']['Cur_Code']
    form.Level.data         = session['data']['Level']

    return render_template('charging_resume_level.html',form=form, data=session.get('data'))

# =============================================================================

import simplejson as json

@main.route('/report/Charging_Resume_Level', methods=['GET','POST'])
@login_required
def report_Charging_Resume_Level():
    logger.debug('Enter: report_Charging_Resume_Level()')
    Cus_Id          =  request.args.get('Cus_Id',None,type=int)
    Cus_Name        =  request.args.get('Cus_Name',None,type=str)
    CIT_Date_From   =  request.args.get('CIT_Date_From',None,type=str)
    CIT_Date_To     =  request.args.get('CIT_Date_To',None,type=str)
    CIT_Status      =  request.args.get('CIT_Status',None,type=int)
    CIT_Status_Value=  request.args.get('CIT_Status_Value',None,type=str)
    Cur_Code        =  request.args.get('Cur_Code',None,type=str)
    Cur_Name        =  request.args.get('Cur_Name',None,type=str)
    Level           =  request.args.get('Level',None,type=str)
    Update          =  request.args.get('Update',0,type=int)
    
    # Updated cached data for this specific query if requested 
    if Update == 1:
        CI = db.session.query(Configuration_Items.CI_Id.distinct()).\
                filter(Configuration_Items.Cus_Id==Cus_Id).\
                order_by(Configuration_Items.CI_Id)
        print(CI)
        CI=CI.all()
        logger.debug ("report_Changing_Resume_Level: %d CI's found for customer %d"%(len(CI),Cus_Id))
        
        resume_records=0

        for ci in CI:
            records = db.Update_Charge_Resume_CI2(CIT_Date_From,CIT_Date_To,CIT_Status,Cur_Code,ci)
            if records is not None:
                resume_records += records
            
        logger.debug ("report_Changing_Resume_Level: resume_records = %s"%resume_records)
        
    # Get Actual Remume Data from Database
    # NOTE: Here needs some Sand-Clock Message or something in case it takes so long ...
    rows =  db.Get_Charge_Resume(Cus_Id,CIT_Date_From,CIT_Date_To,CIT_Status,Cur_Code)
    
    return render_template('report_charging_resume_level.html',rows=rows,
                Cus_Id=Cus_Id,
                Cus_Name=Cus_Name,
                CIT_Date_From=CIT_Date_From,
                CIT_Date_To=CIT_Date_To,
                CIT_Status=CIT_Status,
                CIT_Status_Value=CIT_Status_Value,                
                Cur_Code=Cur_Code,
                Cur_Name=Cur_Name,
                Level=Level
                )
