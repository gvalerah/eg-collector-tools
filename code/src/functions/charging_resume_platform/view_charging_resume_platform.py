# =============================================================================
# View for Get Charging Resume from DB
# (c) Sertechno 2018
# GLVH @ 2019-08-16
# =============================================================================

from emtec.collector.forms  import frm_charging_resume_platform
from babel.numbers          import format_number
from babel.numbers          import format_decimal
from babel.numbers          import format_percent

@main.route('/forms/Get_Charging_Resume_Platform', methods=['GET', 'POST'])
@login_required
def forms_Get_Charging_Resume_Platform():
    logger.debug(f'{this()}: Enter')
    collectordata=get_collectordata()
    session['data'] =  {    'Pla_Id': None, 
                            'CIT_Date_From':collectordata['COLLECTOR_PERIOD']['start'], 
                            'CIT_Date_To':collectordata['COLLECTOR_PERIOD']['end'], 
                            'CIT_Status':1,
                            'Cur_Code':'USD'}

    form = frm_charging_resume_platform()

    # ------------------------------------------------------------------------------
    # Will setup filter to consider only Currencies with actual Exchange Rates in DB
    # Commit all pending DB states in order to refresh data
    db.session.commit()
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
            flash('Report discarded ...')
        else:
            flash('Form validated but not submited. Report to Support ...')
        return redirect(url_for('.forms_Get_Charging_Resume_Platform'))

    form.Pla_Id.data        = session['data']['Pla_Id']
    form.CIT_Date_From.data = session['data']['CIT_Date_From']
    form.CIT_Date_To.data   = session['data']['CIT_Date_To']
    form.CIT_Status.data    = session['data']['CIT_Status']
    form.Cur_Code.data      = session['data']['Cur_Code']

    return render_template('charging_resume_platform.html',form=form, data=session.get('data'),collectordata=collectordata)

# =============================================================================

import simplejson as json

@main.route('/report/Charging_Resume_Platform', methods=['GET','POST'])
@login_required
def report_Charging_Resume_Platform():
    logger.debug(f'{this()}: Enter')
    
    collectordata=get_collectordata()

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
        
        CI = db.session.query(
                Configuration_Items.CI_Id,
                Configuration_Items.Cus_Id,
                ).filter(Configuration_Items.Pla_Id==Pla_Id
                ).order_by( Configuration_Items.CC_Id,
                            Configuration_Items.CI_Id
                ).all()
        
        logger.debug (f"{this()}: {len(CI)} CI's found for platform {Pla_Id}")
        
        resume_records=0

        if CI is not None:
            cis=len(CI)
            cis_count=0
            
        for ci in CI:
            cis_count+=1
            logger.debug ("%s: %.2f%% calling db.Update_Charge_Resume_CI(%s,%s,%s,%s,%s,%s,%s)"%(
                this(),
                cis_count*100/cis,
                ci.Cus_Id,
                CIT_Date_From,
                CIT_Date_To,
                CIT_Status,
                Cur_Code,
                ci.CI_Id,
                charge_item
                )
            )

            records = db.Update_Charge_Resume_CI(
                ci.Cus_Id,
                CIT_Date_From,
                CIT_Date_To,
                CIT_Status,
                Cur_Code,
                ci.CI_Id,
                charge_item,
                current_user.id
                )
            if records is not None:
                resume_records += records
        logger.debug (f"{this()}: resume_records = {resume_records}")
        
    # Get Actual Remume Data from Database
    # NOTE: Here needs some Sand-Clock Message or something in case it takes so long ...
    '''
    rows = db.Get_Charge_Resume2(
                3,
                Pla_Id,
                CIT_Date_From,
                CIT_Date_To,
                CIT_Status,Cur_Code
            )
    '''
    rows =  db.Get_Charge_Resume_Filter(
            FILTER_PLATFORM,
            Pla_Id,
            CIT_Date_From,
            CIT_Date_To,
            CIT_Status,
            Cur_Code
        )

    return render_template('report_charging_resume_platform.html',
                rows=rows,
                Pla_Id=Pla_Id,
                Pla_Name=Pla_Name,
                CIT_Date_From=CIT_Date_From,
                CIT_Date_To=CIT_Date_To,
                CIT_Status=CIT_Status,
                CIT_Status_Value=CIT_Status_Value,                
                Cur_Code=Cur_Code,
                Cur_Name=Cur_Name,
                collectordata=collectordata
                )
