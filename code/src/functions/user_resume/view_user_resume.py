# ======================================================================
# View for Get Charging Resume from DB
# (c) Sertechno 2018
# GLVH @ 2018-11-26
# 2021-05-1 GLVH Ajustes a sessiones dinamicas 
# ======================================================================

from babel.numbers  import format_number, format_decimal, format_percent
from pprint import pprint,pformat
import simplejson as json
from emtec.collector.forms       import frm_user_resume

@main.route('/forms/Get_User_Resume', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.CUSTOMER)
def forms_Get_User_Resume():
    logger.debug('Enter: forms_Get_User_Resume()'%())
    collectordata=get_collectordata()
    logger.debug("collectordata=")
    logger.debug(pformat(collectordata))
    db.logger=logger
    view_session = db.Session(db.engine)

    session['data'] =  { 
        'CIT_Date_From':collectordata['COLLECTOR_PERIOD']['start'], 
        'CIT_Date_To'  :collectordata['COLLECTOR_PERIOD']['end'], 
        'CIT_Status'   :1,
        'Cur_Code'     :current_user.cost_center.Cur_Code,
        'CC_Id'        :current_user.CC_Id
        }

    form = frm_user_resume()
    
    # ------------------------------------------------------------------------------
    # Will setup filter to consider only Currencies with actual Exchange Rates in DB
    # Prepare query
    logger.debug(f"db.session = {db.session}")
    #b.New_Session()
    logger.debug(f"db.session = {db.session}")
    query = view_session.query(exchange_rate.Cur_Code.distinct().label('Cur_Code'))
    # Execute query and convert in list for further use in choices selection
    cur_choices = [row.Cur_Code for row in query.all()]
    # Get default value from current_user.CC_Id -> Cost_Centers.Cur_Code
    # ------------------------------------------------------------------------------
    # Will setup filter to consider only User's visible Cost Centers
    # Prepare query
    if current_user.CC_Id == 1:
        query = view_session.query(cost_center.CC_Id
                        ).filter(cost_center.CC_Parent_Code=='DEFAULT-CC-CODE'
                        ).filter(cost_center.CC_Id > 1
                        ).all()
    else:
        #20200210 GV USERCAN = db.get_user_cost_centers(current_user.id,current_user.CC_Id)
        USERCAN = db.get_user_cost_centers(current_user.id)
        query   = view_session.query(cost_center.CC_Id).\
                    filter(cost_center.CC_Id.in_(USERCAN)).all()
    # Execute query and convert in list for further use in choices selection
    cc_choices = [row.CC_Id for row in query]

    CC_Description          = view_session.query(cost_center.CC_Description).filter(cost_center.CC_Id==current_user.CC_Id).one()
    form.CIT_Status.choices = view_session.query(cit_status.CIT_Status,cit_status.Value).all()
    form.Cur_Code.choices   = view_session.query(currency.Cur_Code,currency.Cur_Name).filter(currency.Cur_Code.in_(cur_choices)).all()
    form.CC_Id.choices      = view_session.query(cost_center.CC_Id,cost_center.CC_Description).filter(cost_center.CC_Id.in_(cc_choices)).all()    
        
    if form.validate_on_submit():
        session['data']['CIT_Date_From' ] = form.CIT_Date_From.data
        session['data']['CIT_Date_To'   ] = form.CIT_Date_To.data
        session['data']['CIT-Status'    ] = form.CIT_Status.data
        session['data']['Cur_Code'      ] = form.Cur_Code.data
        session['data']['CC_Id   '      ] = form.CC_Id.data
        if     form.submit_Report.data:
            # Get the Selected options index for string lists
            for i in range(len(form.Cur_Code.choices)):
                if form.Cur_Code.choices[i][0]==form.Cur_Code.data:
                    cur_index=i
            for i in range(len(form.CC_Id.choices)):
                if form.CC_Id.choices[i][0]==form.CC_Id.data:
                    cc_index=i
            return redirect(url_for('.report_User_Resume',
                                CIT_Date_From   = form.CIT_Date_From.data,
                                CIT_Date_To     = form.CIT_Date_To.data,
                                CIT_Status      = form.CIT_Status.data,
                                CIT_Status_Value= form.CIT_Status.choices[form.CIT_Status.data-1][1],
                                Cur_Code        = form.Cur_Code.data,
                                Cur_Name        = form.Cur_Code.choices[cur_index][1],
                                CC_Id           = form.CC_Id.data,
                                CC_Description  = form.CC_Id.choices[cc_index][1],
                                Update          = 0
                                ))
        if     form.submit_Update.data:
            # Get the Selected options index for string lists
            for i in range(len(form.Cur_Code.choices)):
                if form.Cur_Code.choices[i][0]==form.Cur_Code.data:
                    cur_index=i
            for i in range(len(form.CC_Id.choices)):
                if form.CC_Id.choices[i][0]==form.CC_Id.data:
                    cc_index=i
            return redirect(url_for('.report_User_Resume',
                                CIT_Date_From   = form.CIT_Date_From.data,
                                CIT_Date_To     = form.CIT_Date_To.data,
                                CIT_Status      = form.CIT_Status.data,
                                CIT_Status_Value= form.CIT_Status.choices[form.CIT_Status.data-1][1],
                                Cur_Code        = form.Cur_Code.data,
                                Cur_Name        = form.Cur_Code.choices[cur_index][1],
                                CC_Id           = form.CC_Id.data,
                                CC_Description  = form.CC_Id.choices[cc_index][1],
                                Update          = 1
                                ))

        elif   form.submit_Cancel.data:
            #print('Cancel Data Here ... does nothing')
            flash('Report discarded ...')
        else:
            flash('form validated but not submited. Report to Support ...')
            #print('form validated but not submited ???')
        return redirect(url_for('.forms_Get_User_Resume'))

    form.CIT_Date_From.data = session['data']['CIT_Date_From']
    form.CIT_Date_To.data   = session['data']['CIT_Date_To']
    form.CIT_Status.data    = session['data']['CIT_Status']
    form.Cur_Code.data      = session['data']['Cur_Code']
    
    return render_template('get_user_resume.html',
            form=form, 
            data=session.get('data'),
            collectordata=collectordata
            )

# ======================================================================

@main.route('/report/User_Resume', methods=['GET','POST'])
@login_required
@permission_required(Permission.CUSTOMER)
def report_User_Resume():
    function_name=sys._getframe().f_code.co_name
    logger.debug('%s: Enter'%(function_name))
    
    db.logger        = logger
    view_session     = db.Session(db.engine)
    table_name       = 'Charge_Items'
    class_name       = 'charge_item'
    template_name    = 'Charge_Items'

    CC_Id            =  request.args.get('CC_Id',current_user.cost_center.CC_Id,type=int)
    CC_Description   =  request.args.get('CC_Description',None,type=str)
    CIT_Date_From    =  request.args.get('CIT_Date_From',None,type=str)
    CIT_Date_To      =  request.args.get('CIT_Date_To',None,type=str)
    CIT_Status       =  request.args.get('CIT_Status',None,type=int)
    CIT_Status_Value =  request.args.get('CIT_Status_Value',None,type=str)
    Cur_Code         =  request.args.get('Cur_Code',None,type=str)
    Cur_Name         =  request.args.get('Cur_Name',None,type=str)
    Update           =  request.args.get('Update',0,type=int)
    
    # Updated cached data for this specific query if requested 
    if Update == 1:
        # -------------------------------------------------------------------------------------------------------------- #
        # Previous Code faster but requires more memory will be replaced by an by CI loop                                #
        # query="C*ALL Update_Charge_Resume(%d,'%s','%s',%d,'%s')"%(Cus_Id,CIT_Date_From,CIT_Date_To,CIT_Status,Cur_Code) #
        # resume_records = db.engine.execute(query).scalar()                                                             #
        # -------------------------------------------------------------------------------------------------------------- #
        # 20181228 GV query = "S*ELECT DISTINCT CI_Id FROM configuration_item WHERE Cus_Id=%d"%(Cus_Id)
        logger.debug("%s: ***********************"%(function_name))
        logger.debug("%s: Update Mode"%(function_name))
        logger.debug("%s: current user= %s"%(function_name,current_user))
        logger.debug("%s: current user id= %s"%(function_name,current_user.id))
        logger.debug("%s: current user CC_Id=%s"%(function_name,current_user.CC_Id))
        
        CCISBELOW=db.get_cost_centers(CC_Id)
        logger.debug("%s: CCISBELOW= %s"%(function_name,CCISBELOW))
        if current_user.CC_Id == 1:        
            query = view_session.query(configuration_item.CI_Id
                        ).filter(configuration_item.CC_Id.in_(CCISBELOW)
                        ).order_by(
                            configuration_item.CC_Id,
                            configuration_item.CI_Id
                        )
        else:
            USERCAN=db.get_user_cost_centers(current_user.id)
            logger.debug("%s: USERCAN= %s"%(function_name,USERCAN))
            query = view_session.query(configuration_item.CI_Id
                        ).filter(configuration_item.CC_Id.in_(CCISBELOW)
                        ).order_by(configuration_item.CC_Id,configuration_item.CI_Id)
        CI = query.all()
        logger.debug("%s: CI=%s"%(function_name,CI))

        
        logger.debug("%s: user %s"%(function_name,current_user))
        logger.debug("%s: report_User_Resume: %d CI's found for user %d"%(function_name,len(CI),current_user.id))
        
        resume_records=0

        for ci in CI:
            logger.debug("%s: records = db.Update_User_Resume_CI(%s,%s,%s,%s,%s,%s,%s)"%(
                function_name,
                current_user.id,
                CIT_Date_From,
                CIT_Date_To,
                CIT_Status,
                Cur_Code,
                ci.CI_Id,
                charge_item.__table__.name
                )
            )
            records = db.Update_User_Resume_CI(
                current_user.id,
                CIT_Date_From,
                CIT_Date_To,
                CIT_Status,
                Cur_Code,
                ci.CI_Id,
                charge_item
                )
            logger.debug("%s: ci= %s records= %s"%(function_name,ci,records))
            if records is not None:
                resume_records += records
            
        logger.debug("%s: resume_records = %s"%(function_name,resume_records))
        
    # Get Actual Resume Data from Database
    # NOTE: Here needs some Sand-Clock Message or something in case it takes so long ...
    try:
        logger.debug("%s: rows = db.Get_User_Resume(%s,%s,%s,%s,%s,%s)"%(
            function_name,
            current_user.id,
            CIT_Date_From,
            CIT_Date_To,
            CIT_Status,
            Cur_Code,
            CC_Id)
            )
        if current_user.CC_Id == 1:
            # user has a super top level CC_Id
            user_id=view_session.query(User.id).filter(User.CC_Id==CC_Id).one()      
            logger.debug(f"User with super top level CC_Id will look for CC_Id={CC_Id}")
            # 20210423 force CC_Id in the call to filter report
            rows = db.Get_User_Resume(
                        user_id,
                        CIT_Date_From,
                        CIT_Date_To,
                        CIT_Status,
                        Cur_Code,
                        CC_Id=CC_Id
                        )
        else:
            # 20210423 force CC_Id in the call to filter report
            rows = db.Get_User_Resume(
                        current_user.id,
                        CIT_Date_From,
                        CIT_Date_To,
                        CIT_Status,
                        Cur_Code,
                        CC_Id=CC_Id
                        )
        logger.debug(f"{function_name}: user {current_user}")
        logger.debug("%s: %s rows in resume for user %s %s as role %s"%(
            function_name,
            len(rows),
            current_user.id,
            current_user.username,
            current_user.role_id
            )
        )
        return render_template( 'report_user_resume.html',
                    rows=rows,
                    CC_Description   = CC_Description,
                    CIT_Date_From    = CIT_Date_From,
                    CIT_Date_To      = CIT_Date_To,
                    CIT_Status       = CIT_Status,
                    CIT_Status_Value = CIT_Status_Value,                
                    Cur_Code         = Cur_Code,
                    Cur_Name         = Cur_Name
                    )
    except Exception as e:
        logger.error(f"{function_name}: EXCEPTION : {str(e)}")
        logger.error(f"{function_name}: user {current_user}")
        message=str(e)
        return render_template("404.html",message=message), 404
