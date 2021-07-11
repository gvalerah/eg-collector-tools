# ======================================================================
# View for Get Charging Resume from DB per CC
# (c) Sertechno 2019
# GLVH @ 2019-08-16
# ======================================================================

from emtec.collector.db.orm import *
from emtec.collector.forms  import frm_charging_resume_cc
from babel.numbers          import format_number
from babel.numbers          import format_decimal
from babel.numbers          import format_percent

@main.route('/forms/Get_Charging_Resume_CC', methods=['GET', 'POST'])
@login_required
def forms_Get_Charging_Resume_CC():
    logger.debug(f'{this()}: Enter')
    collectordata=get_collectordata()

    session['data'] =  {    'CC_Id': None, 
                            'CIT_Date_From':collectordata['COLLECTOR_PERIOD']['start'], 
                            'CIT_Date_To':collectordata['COLLECTOR_PERIOD']['end'], 
                            'CIT_Status':1,
                            'Cur_Code':'USD'
                        }

    form = frm_charging_resume_cc()
    # ------------------------------------------------------------------
    # Will setup filter to consider only Currencies with actual Exchange
    # Rates in DB
    # Commit all pending DB states in order to refresh data
    db.session.commit()
    # Prepare query
    query = db.session.query(exchange_rate.Cur_Code.distinct().label('Cur_Code'))
    # Execute query and convert in list for further use in choices selection
    cur_choices = [row.Cur_Code for row in query.all()]
    # ------------------------------------------------------------------

    form.CC_Id.choices      = db.session.query(cost_center.CC_Id,cost_center.CC_Description).all()
    form.CIT_Status.choices = db.session.query(cit_status.CIT_Status,cit_status.Value).all()
    form.Cur_Code.choices   = db.session.query(currency.Cur_Code,currency.Cur_Name).filter(currency.Cur_Code.in_(cur_choices)).all()

    if form.validate_on_submit():
        session['data']['CC_Id'         ] = form.CC_Id.data
        session['data']['CIT_Date_From' ] = form.CIT_Date_From.data
        session['data']['CIT_Date_To'   ] = form.CIT_Date_To.data
        session['data']['CIT-Status'    ] = form.CIT_Status.data
        session['data']['Cur_Code'      ] = form.Cur_Code.data
        if     form.submit_Report.data:
            # Get the Selected options index for string lists
            for i in range(len(form.CC_Id.choices)):
                if form.CC_Id.choices[i][0]==form.CC_Id.data:
                    cc_index=i
            for i in range(len(form.Cur_Code.choices)):
                if form.Cur_Code.choices[i][0]==form.Cur_Code.data:
                    cur_index=i
            return redirect(url_for('.report_Charging_Resume_CC',
                                CC_Id           = form.CC_Id.data,
                                CC_Description  = form.CC_Id.choices[cc_index][1],
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
            for i in range(len(form.CC_Id.choices)):
                if form.CC_Id.choices[i][0]==form.CC_Id.data:
                    cc_index=i
            for i in range(len(form.Cur_Code.choices)):
                if form.Cur_Code.choices[i][0]==form.Cur_Code.data:
                    cur_index=i
            return redirect(url_for('.report_Charging_Resume_CC',
                                CC_Id           = form.CC_Id.data,
                                CC_Description  = form.CC_Id.choices[cc_index][1],
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
        return redirect(url_for('.forms_Get_Charging_Resume'))

    form.CC_Id.data         = session['data']['CC_Id']
    form.CIT_Date_From.data = session['data']['CIT_Date_From']
    form.CIT_Date_To.data   = session['data']['CIT_Date_To']
    form.CIT_Status.data    = session['data']['CIT_Status']
    form.Cur_Code.data      = session['data']['Cur_Code']

    return render_template( 'charging_resume_cc.html',
                            form=form, 
                            data=session.get('data'),
                            collectordata=collectordata
                            )

# ======================================================================

import simplejson as json

@main.route('/report/Charging_Resume_CC', methods=['GET','POST'])
@login_required
def report_Charging_Resume_CC():
    logger.debug(f'{this()}: Enter')
    
    collectordata=get_collectordata()
    
    db.session.flush()
    db.session.commit()

    CC_Id           =  request.args.get('CC_Id',None,type=int)
    CC_Description  =  request.args.get('CC_Description',None,type=str)
    CIT_Date_From   =  request.args.get('CIT_Date_From',None,type=str)
    CIT_Date_To     =  request.args.get('CIT_Date_To',None,type=str)
    CIT_Status      =  request.args.get('CIT_Status',None,type=int)
    CIT_Status_Value=  request.args.get('CIT_Status_Value',None,type=str)
    Cur_Code        =  request.args.get('Cur_Code',None,type=str)
    Cur_Name        =  request.args.get('Cur_Name',None,type=str)
    Update          =  request.args.get('Update',0,type=int)
    
    # Updated cached data for this specific query if requested 
    if Update == 1:
        logger.debug (f"{this()}: Update is requested")
        # -------------------------------------------------------------------------------------------------------------- #
        # Previous Code faster but requires more memory will be replaced by an by CI loop                                #
        # -------------------------------------------------------------------------------------------------------------- #
        Cus_Id=db.session.query(Cost_Centers.Cus_Id
            ).filter(Cost_Centers.CC_Id==CC_Id
            ).first(
            )[0]
            
        LISTA = db.get_cost_centers(CC_Id)
        logger.debug(f"{this()}: LISTA de CCs= {LISTA}")
        CI = db.session.query(Configuration_Items.CI_Id,Configuration_Items.Cus_Id).\
                filter(Configuration_Items.CC_Id.in_(LISTA)).\
                order_by(Configuration_Items.CC_Id,Configuration_Items.CI_Id).all()
        
        logger.debug (f"{this()}: {len(CI)} CI's found for cost center {CC_Id}")
        
        resume_records=0
        
        logger.info(f"{this()}: Updating Charge Resume Update ...")
        ci_list = []
        
        for ci in CI:
            ci_list.append(ci.CI_Id)
        records = db.Update_Charge_Resume_CIS(
            Cus_Id,
            CIT_Date_From,
            CIT_Date_To,
            CIT_Status,
            Cur_Code,
            ci_list,             # <-- Lista de CIs Requeridos          
            charge_item,
            current_user.id
            )
    
        logger.debug (f"{this()}: Resume_records updated= {resume_records}")
    else:
        logger.debug (f"{this()}: Update is NOT requested")
    
    # Get Actual Remume Data from Database
    # NOTE: Here needs some Sand-Clock Message or something in case it takes so long ...
    rows = db.Get_Charge_Resume_Filter(
                FILTER_COST_CENTER,
                CC_Id,
                CIT_Date_From,
                CIT_Date_To,
                CIT_Status,
                Cur_Code,
                User_Id=current_user.id
            )
    return render_template(
                'report_charging_resume.html',
                rows=rows,
                CC_Id=CC_Id,
                CC_Description=CC_Description,
                CIT_Date_From=CIT_Date_From,
                CIT_Date_To=CIT_Date_To,
                CIT_Status=CIT_Status,
                CIT_Status_Value=CIT_Status_Value,                
                Cur_Code=Cur_Code,
                Cur_Name=Cur_Name,
                collectordata=collectordata
                )
