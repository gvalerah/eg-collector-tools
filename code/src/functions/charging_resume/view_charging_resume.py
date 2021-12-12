# ======================================================================
# View for Get Charging Resume from DB
# (c) Sertechno 2018
# GLVH @ 2019-08-16
# GLVH @ 2019-08-18 Refactoring to ORM DB Only
# GLVH @ 2020-10-25 Proper sharding and initialization handling
# ======================================================================

from pprint                         import pformat
from emtec.collector.forms          import frm_charging_resume
from babel.numbers                  import format_number
from babel.numbers                  import format_decimal
from babel.numbers                  import format_percent
from emtec.collector.db.orm_model   import Configuration_Items
from emtec.feedback                 import *
import tempfile
import threading
import queue

# ======================================================================

@main.route('/forms/Get_Charging_Resume', methods=['GET', 'POST'])
@login_required
def forms_Get_Charging_Resume():
    logger.debug(f'{this()}: Enter')
    collectordata=get_collectordata()

    session['data'] =  {    
        'User_Id': 0,
        'Cus_Id': None,
        'CIT_Date_From':collectordata['COLLECTOR_PERIOD']['start'], 
        'CIT_Date_To':collectordata['COLLECTOR_PERIOD']['end'], 
        'CIT_Status':1,
        'Cur_Code':'USD'
        }

    form = frm_charging_resume()

    # ------------------------------------------------------------------------------
    # Will setup filter to consider only Currencies with actual Exchange Rates in DB
    # Commit all pending DB states in order to refresh data
    db.session.commit()
    db.session.flush()
    # Prepare query
    query = db.session.query(exchange_rate.Cur_Code.distinct().label('Cur_Code'))
    # Execute query and convert in list for further use in choices selection
    cur_choices = [row.Cur_Code for row in query.all()]

    form.Cus_Id.choices     = db.session.query(customer.Cus_Id,customer.Cus_Name).all()
    form.CIT_Status.choices = db.session.query(cit_status.CIT_Status,cit_status.Value).all()
    form.Cur_Code.choices   = db.session.query(currency.Cur_Code,currency.Cur_Name).filter(currency.Cur_Code.in_(cur_choices)).all()

    if form.validate_on_submit():
        session['data']['User_Id'       ] = form.User_Id 
        session['data']['Cus_Id'        ] = form.Cus_Id.data
        session['data']['CIT_Date_From' ] = form.CIT_Date_From.data
        session['data']['CIT_Date_To'   ] = form.CIT_Date_To.data
        session['data']['CIT-Status'    ] = form.CIT_Status.data
        session['data']['Cur_Code'      ] = form.Cur_Code.data
        print(f"session[data]={session.get('data')}")
        print(f"current_user={current_user}")
        if     form.submit_Report.data:
            # Get the Selected options index for string lists
            for i in range(len(form.Cus_Id.choices)):
                if form.Cus_Id.choices[i][0]==form.Cus_Id.data:
                    cus_index=i
            for i in range(len(form.Cur_Code.choices)):
                if form.Cur_Code.choices[i][0]==form.Cur_Code.data:
                    cur_index=i
            return redirect(url_for('.report_Charging_Resume',
                                User_Id         = current_user.id,
                                Cus_Id          = form.Cus_Id.data,
                                Cus_Name        = form.Cus_Id.choices[cus_index][1],
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
            for i in range(len(form.Cus_Id.choices)):
                if form.Cus_Id.choices[i][0]==form.Cus_Id.data:
                    cus_index=i
            for i in range(len(form.Cur_Code.choices)):
                if form.Cur_Code.choices[i][0]==form.Cur_Code.data:
                    cur_index=i
            return redirect(url_for('.report_Charging_Resume',
                                User_Id         = current_user.id,
                                Cus_Id          = form.Cus_Id.data,
                                Cus_Name        = form.Cus_Id.choices[cus_index][1],
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
            flash('form validated but not submited. Report to Support ...')
        return redirect(url_for('.forms_Get_Charging_Resume'))
    
    form.User_Id            = session['data']['User_Id']
    form.Cus_Id.data        = session['data']['Cus_Id']
    form.CIT_Date_From.data = session['data']['CIT_Date_From']
    form.CIT_Date_To.data   = session['data']['CIT_Date_To']
    form.CIT_Status.data    = session['data']['CIT_Status']
    form.Cur_Code.data      = session['data']['Cur_Code']

    return render_template('charging_resume.html',
                form=form, 
                data=session.get('data'), 
                collectordata=get_collectordata()
                )

@main.route('/forms/Get_Charging_Resume_Progress', methods=['GET', 'POST'])
@login_required
def forms_Get_Charging_Resume_Progress():
    logger.debug(f'{this()}: Enter')
    collectordata=get_collectordata()

    session['data'] =  {    
        'User_Id': 0,
        'Cus_Id': None,
        'CIT_Date_From':collectordata['COLLECTOR_PERIOD']['start'], 
        'CIT_Date_To':collectordata['COLLECTOR_PERIOD']['end'], 
        'CIT_Status':1,
        'Cur_Code':'USD'
        }

    form = frm_charging_resume()

    # ------------------------------------------------------------------------------
    # Will setup filter to consider only Currencies with actual Exchange Rates in DB
    # Commit all pending DB states in order to refresh data
    db.session.commit()
    db.session.flush()
    # Prepare query
    query = db.session.query(exchange_rate.Cur_Code.distinct().label('Cur_Code'))
    # Execute query and convert in list for further use in choices selection
    cur_choices = [row.Cur_Code for row in query.all()]

    form.Cus_Id.choices     = db.session.query(customer.Cus_Id,customer.Cus_Name).all()
    form.CIT_Status.choices = db.session.query(cit_status.CIT_Status,cit_status.Value).all()
    form.Cur_Code.choices   = db.session.query(currency.Cur_Code,currency.Cur_Name).filter(currency.Cur_Code.in_(cur_choices)).all()

    if form.validate_on_submit():
        session['data']['User_Id'       ] = form.User_Id 
        session['data']['Cus_Id'        ] = form.Cus_Id.data
        session['data']['CIT_Date_From' ] = form.CIT_Date_From.data
        session['data']['CIT_Date_To'   ] = form.CIT_Date_To.data
        session['data']['CIT-Status'    ] = form.CIT_Status.data
        session['data']['Cur_Code'      ] = form.Cur_Code.data
        print(f"session[data]={session.get('data')}")
        print(f"current_user={current_user}")
        if     form.submit_Report.data:
            # Get the Selected options index for string lists
            for i in range(len(form.Cus_Id.choices)):
                if form.Cus_Id.choices[i][0]==form.Cus_Id.data:
                    cus_index=i
            for i in range(len(form.Cur_Code.choices)):
                if form.Cur_Code.choices[i][0]==form.Cur_Code.data:
                    cur_index=i
            return redirect(url_for('.report_Charging_Resume_Progress',
                                User_Id         = current_user.id,
                                Cus_Id          = form.Cus_Id.data,
                                Cus_Name        = form.Cus_Id.choices[cus_index][1],
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
            for i in range(len(form.Cus_Id.choices)):
                if form.Cus_Id.choices[i][0]==form.Cus_Id.data:
                    cus_index=i
            for i in range(len(form.Cur_Code.choices)):
                if form.Cur_Code.choices[i][0]==form.Cur_Code.data:
                    cur_index=i
            return redirect(url_for('.report_Charging_Resume_Progress',
                                User_Id         = current_user.id,
                                Cus_Id          = form.Cus_Id.data,
                                Cus_Name        = form.Cus_Id.choices[cus_index][1],
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
            flash('form validated but not submited. Report to Support ...')
        return redirect(url_for('.forms_Get_Charging_Resume_Progress'))
    
    form.User_Id            = session['data']['User_Id']
    form.Cus_Id.data        = session['data']['Cus_Id']
    form.CIT_Date_From.data = session['data']['CIT_Date_From']
    form.CIT_Date_To.data   = session['data']['CIT_Date_To']
    form.CIT_Status.data    = session['data']['CIT_Status']
    form.Cur_Code.data      = session['data']['Cur_Code']

    return render_template('charging_resume.html',
                form=form, 
                data=session.get('data'), 
                collectordata=get_collectordata()
                )


# ======================================================================

import simplejson as json

@main.route('/report/Charging_Resume', methods=['GET','POST'])
@login_required
def report_Charging_Resume():
    logger.debug(f'{this()}: Enter')    
    collectordata=get_collectordata()
    
    db.session.flush()
    db.session.commit()
    
    User_Id         =  request.args.get('User_Id',None,type=int)
    Cus_Id          =  request.args.get('Cus_Id',None,type=int)
    Cus_Name        =  request.args.get('Cus_Name',None,type=str)
    CIT_Date_From   =  request.args.get('CIT_Date_From',None,type=str)
    CIT_Date_To     =  request.args.get('CIT_Date_To',None,type=str)
    CIT_Status      =  request.args.get('CIT_Status',None,type=int)
    CIT_Status_Value=  request.args.get('CIT_Status_Value',None,type=str)
    Cur_Code        =  request.args.get('Cur_Code',None,type=str)
    Cur_Name        =  request.args.get('Cur_Name',None,type=str)
    Update          =  request.args.get('Update',0,type=int)
        
    # Updated cached data for this specific query if requested 
    if Update == 1:
        # BE SURE all CU records has proper description ----------------
        updated_cus = db.Update_CU_Names()
        if updated_cus:
            logger.warning(f"Updated Name CUs = {updated_cus}")
        # BE SURE all CU records has proper rate id
        updated_cus = db.Update_CU_Rates()
        if updated_cus:
            logger.warning(f"Updated Rate CUs = {updated_cus}")
        # --------------------------------------------------------------
        
        query = db.session.query(
                Configuration_Items.CI_Id
                ).filter(Configuration_Items.Cus_Id==Cus_Id
                ).order_by( Configuration_Items.CC_Id,
                            Configuration_Items.CI_Id
                )
        logger.debug (f"{this()}: Cus_Id= {Cus_Id} query: {query}")
        CI = query.all()
        logger.debug (f"{this()}: {len(CI)} CI's found for customer {Cus_Id}")
        logger.debug (f"{this()}: {pformat(CI)}")
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
    
    # Get Actual Remume Data from Database
    rows = db.Get_Charge_Resume_Filter(
                FILTER_CUSTOMER,
                Cus_Id,
                CIT_Date_From,
                CIT_Date_To,
                CIT_Status,
                Cur_Code,
                User_Id=current_user.id
                )
    logger.debug(f"{this()}: PRE RENDER")
    logger.debug(f"{this()}: len rows         = {len(rows)}")
    logger.debug(f"{this()}: Cus_Id           = {Cus_Id}")
    logger.debug(f"{this()}: Cus_Name         = {Cus_Name}")
    logger.debug(f"{this()}: CIT_Date_From    = {CIT_Date_From}")
    logger.debug(f"{this()}: CIT_Date_To      = {CIT_Date_To}")
    logger.debug(f"{this()}: CIT_Status       = {CIT_Status}")
    logger.debug(f"{this()}: CIT_Status_Value = {CIT_Status_Value}")                
    logger.debug(f"{this()}: Cur_Code         = {Cur_Code}")
    logger.debug(f"{this()}: Cur_Name         = {Cur_Name}")
    logger.debug(f"{this()}: template         : report_charging_resume.html")
    try:
        return render_template('report_charging_resume.html',
                    rows=rows,
                    Cus_Id=Cus_Id,
                    Cus_Name=Cus_Name,
                    CIT_Date_From=CIT_Date_From,
                    CIT_Date_To=CIT_Date_To,
                    CIT_Status=CIT_Status,
                    CIT_Status_Value=CIT_Status_Value,                
                    Cur_Code=Cur_Code,
                    Cur_Name=Cur_Name,
                    collectordata=get_collectordata(),
                    filter_type=FILTER_CUSTOMER,
                    filter_code=Cus_Id
                    )
    except Exception as e:
        return f"{this()}: Exception:  {str(e)}"


#main.route('/internal/Charging_Resume_Update', methods=['GET','POST'])
def report_Charging_Resume_Update(kwargs):
    logger.warning(f".................................................")
    logger.warning(f"{this()}: kwargs = {kwargs}")
    logger.warning(f".................................................")
    try:
        app_ctx          = kwargs.get('app_ctx')
        db               = kwargs.get('db')
        current_user     = kwargs.get('current_user')
        User_Id          = kwargs.get('User_Id')
        Cus_Id           = kwargs.get('Cus_Id')
        Cus_Name         = kwargs.get('Cus_Name')
        CIT_Date_From    = kwargs.get('CIT_Date_From')
        CIT_Date_To      = kwargs.get('CIT_Date_To')
        CIT_Status       = kwargs.get('CIT_Status')
        CIT_Status_Value = kwargs.get('CIT_Status_Value')
        Cur_Code         = kwargs.get('Cur_Code')
        Cur_Name         = kwargs.get('Cur_Name')
        Update           = kwargs.get('Update')
        callback         = kwargs.get('callback')
        filename         = kwargs.get('filename')
        mode             = kwargs.get('mode')
        progress         = kwargs.get('progress')
        verbose          = kwargs.get('verbose')
        logger.debug(f"{this()}: current_user = {current_user}")
        logger.debug(f"{this()}: db           = {db}")
        logger.debug(f"{this()}: pushing context ...")
        app_ctx.push()
        logger.debug(f"{this()}: current_app  = {current_app}")
        logger.debug(f"{this()}: current_user = {current_user}")
        logger.debug(f"{this()}: db           = {db}")

        # BE SURE all CU records has proper description ----------------
        updated_cus = db.Update_CU_Names()
        if updated_cus:
            logger.warning(f"Updated Name CUs = {updated_cus:,.0f}")
        # BE SURE all CU records has proper rate id
        updated_cus = db.Update_CU_Rates()
        if updated_cus:
            logger.warning(f"Updated Rate CUs = {updated_cus:,.0f}")
        # --------------------------------------------------------------
        
        query = db.session.query(
                Configuration_Items.CI_Id
                ).filter(Configuration_Items.Cus_Id==Cus_Id
                ).order_by( Configuration_Items.CC_Id,
                            Configuration_Items.CI_Id
                )
        logger.debug (f"{this()}: Cus_Id= {Cus_Id} query: {query}")
        CI = query.all()
        logger.debug (f"{this()}: {len(CI)} CI's found for customer {Cus_Id}")
        logger.debug (f"{this()}: {pformat(CI)}")
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
            User_Id,              # 20211212 GV was current_user.id
            fast=False,
            callback=display_advance,
            filename=filename,
            progress=progress,
            verbose=verbose
            )
        logger.info(f"{this()}: Updated {records:,.0f} records")
    except Exception as e:
        emtec_handle_general_exception(e,logger=logger)
        records = 0
    logger.info(f"{this()}: return number of updated records = {records:,.0f}. Update process completed.")
    return records

#@main.route('/internal/Charging_Resume_Report', methods=['GET','POST'])
def report_Charging_Resume_Report(**kwargs):
    logger.warning(f"{this()}: kwargs = {kwargs}")
    User_Id          = kwargs.get('User_Id')
    Cus_Id           = kwargs.get('Cus_Id')
    Cus_Name         = kwargs.get('Cus_Name')
    CIT_Date_From    = kwargs.get('CIT_Date_From')
    CIT_Date_To      = kwargs.get('CIT_Date_To')
    CIT_Status       = kwargs.get('CIT_Status')
    CIT_Status_Value = kwargs.get('CIT_Status_Value')
    Cur_Code         = kwargs.get('Cur_Code')
    Cur_Name         = kwargs.get('Cur_Name')
    Update           = kwargs.get('Update')
    rows = db.Get_Charge_Resume_Filter(
                FILTER_CUSTOMER,
                Cus_Id,
                CIT_Date_From,
                CIT_Date_To,
                CIT_Status,
                Cur_Code,
                User_Id=current_user.id
                )
    logger.debug(f"{this()}: PRE RENDER")
    logger.debug(f"{this()}: len rows         = {len(rows)}")
    logger.debug(f"{this()}: Cus_Id           = {Cus_Id}")
    logger.debug(f"{this()}: Cus_Name         = {Cus_Name}")
    logger.debug(f"{this()}: CIT_Date_From    = {CIT_Date_From}")
    logger.debug(f"{this()}: CIT_Date_To      = {CIT_Date_To}")
    logger.debug(f"{this()}: CIT_Status       = {CIT_Status}")
    logger.debug(f"{this()}: CIT_Status_Value = {CIT_Status_Value}")                
    logger.debug(f"{this()}: Cur_Code         = {Cur_Code}")
    logger.debug(f"{this()}: Cur_Name         = {Cur_Name}")
    logger.debug(f"{this()}: template         : report_charging_resume.html")
    try:
        return render_template('report_charging_resume.html',
                    rows             = rows,
                    Cus_Id           = Cus_Id,
                    Cus_Name         = Cus_Name,
                    CIT_Date_From    = CIT_Date_From,
                    CIT_Date_To      = CIT_Date_To,
                    CIT_Status       = CIT_Status,
                    CIT_Status_Value = CIT_Status_Value,                
                    Cur_Code         = Cur_Code,
                    Cur_Name         = Cur_Name,
                    collectordata    = get_collectordata(),
                    filter_type      = FILTER_CUSTOMER,
                    filter_code      = Cus_Id
                    )
    except Exception as e:
        return f"{this()}: Exception:  {str(e)}"

@main.route('/report/Charging_Resume_Progress', methods=['GET','POST'])
@login_required
def report_Charging_Resume_Progress():
    logger.debug(f'{this()}: Enter')    
    collectordata=get_collectordata()
    
    db.session.flush()
    db.session.commit()
    
    User_Id          =  request.args.get('User_Id',None,type=int)
    Cus_Id           =  request.args.get('Cus_Id',None,type=int)
    Cus_Name         =  request.args.get('Cus_Name',None,type=str)
    CIT_Date_From    =  request.args.get('CIT_Date_From',None,type=str)
    CIT_Date_To      =  request.args.get('CIT_Date_To',None,type=str)
    CIT_Status       =  request.args.get('CIT_Status',None,type=int)
    CIT_Status_Value =  request.args.get('CIT_Status_Value',None,type=str)
    Cur_Code         =  request.args.get('Cur_Code',None,type=str)
    Cur_Name         =  request.args.get('Cur_Name',None,type=str)
    Update           =  request.args.get('Update',0,type=int)
    
    temp_dir         =  tempfile.mkdtemp()
    filename         =  os.path.join(temp_dir,f'{this()}.out')
    mode             =  'a'
    progress         =  os.path.join(temp_dir,f'{this()}.advance')
    verbose          =  1
    multimode        =  'fork'   # or thread
    multimode        =  'thread' # or fork

    logger.debug(f"{this()}: current_app     = {current_app}")
    logger.debug(f"{this()}: current_user    = {current_user}")
    logger.debug(f"{this()} db              = {db}")
    app_ctx = current_app.app_context()
    
    kwargs = {
        'current_app'      :  current_app,
        'current_user'     :  current_user,
        'app_ctx'          :  app_ctx,
        'db'               :  db,
        'User_Id'          :  User_Id,
        'Cus_Id'           :  Cus_Id,
        'Cus_Name'         :  Cus_Name,
        'CIT_Date_From'    :  CIT_Date_From,
        'CIT_Date_To'      :  CIT_Date_To,
        'CIT_Status'       :  CIT_Status,
        'CIT_Status_Value' :  CIT_Status_Value,
        'Cur_Code'         :  Cur_Code,
        'Cur_Name'         :  Cur_Name,
        'Update'           :  Update,
        'callback'         :  display_advance,
        'filename'         :  filename, # callback arguments
        'mode'             :  mode, # callback arguments
        'progress'         :  progress, # callback arguments
        'verbose'          :  verbose,  # callback arguments
    }
    logger.warning(f"{this()}: kwargs={kwargs}")
    # Updated cached data for this specific query if requested 
    if Update == 1:
        try:
            db.session.flush()
        except Exception as e:
            msg = f"{this()}: DB Flush exception: {str(e)}"
            logger.warning(msg)
        if multimode == 'fork':
            # Aqui el fork no esta funcionando muy bien probar threads ....
            pid = os.fork()
            if pid == 0: # Child Process need to update in background while parent showa bar ....
                try:
                    logger.warning(f"{this()}: Forked child process {os.getppid()}:{os.getpid()} initiates update")
                    logger.warning(f"{this()}: Update={Update} filename={filename} progress={progress}")
                    records = report_Charging_Resume_Update(**kwargs)
                    logger.warning(f"{this()}: updated = {records} records")
                    logger.warning(f"{this()}: Updated={Update} filename={filename} progress={progress}")
                    logger.warning(f"{this()}: Child: {os.getppid()}:{os.getpid()} is completed now. will return inmediately.")
                    return "update completed"
                except Exception as e:
                    emtec_handle_general_exception(e,logger=logger)
                    msg = f"{this()}: Update failure. exception: {str(e)}"
                    flash(msg,'error')
                    return msg
                #eturn report_Charging_Resume_Report(**kwargs)
            else:
                logger.info(f"{this()}: parent process {os.getpid()}::{pid} continues ...")
                try:
                    flash(f"{this()}: parent {os.getpid()}::{pid} Update={Update} filename={filename} progress={progress} will render report_charging_resume_update.html")
                    return render_template('report_charging_resume_update.html',
                                Cus_Id           = Cus_Id,
                                Cus_Name         = Cus_Name,
                                CIT_Date_From    = CIT_Date_From,
                                CIT_Date_To      = CIT_Date_To,
                                CIT_Status       = CIT_Status,
                                CIT_Status_Value = CIT_Status_Value,                
                                Cur_Code         = Cur_Code,
                                Cur_Name         = Cur_Name,
                                collectordata    = get_collectordata(),
                                filter_type      = FILTER_CUSTOMER,
                                filter_code      = Cus_Id,
                                filename         = filename,
                                progress         = progress,
                                )
                except Exception as e:
                    msg = f"{this()}: Exception:  {str(e)}"
                    flash(msg,'error')
                    return msg
        elif multimode == 'thread':            
                try:
                    logger.warning(f"{this()}: Initiating Thread Update={Update} filename={filename} progress={progress}")
                    threading.Thread(
                        target=report_Charging_Resume_Update,
                        args=(kwargs,)
                        ).start()
                    logger.warning(f"{this()}: Inmediatelly rendering bar html")
                    return render_template('report_charging_resume_update.html',
                                Cus_Id           = Cus_Id,
                                Cus_Name         = Cus_Name,
                                CIT_Date_From    = CIT_Date_From,
                                CIT_Date_To      = CIT_Date_To,
                                CIT_Status       = CIT_Status,
                                CIT_Status_Value = CIT_Status_Value,                
                                Cur_Code         = Cur_Code,
                                Cur_Name         = Cur_Name,
                                collectordata    = get_collectordata(),
                                filter_type      = FILTER_CUSTOMER,
                                filter_code      = Cus_Id,
                                filename         = filename,
                                progress         = progress,
                                )
                except Exception as e:
                    emtec_handle_general_exception(e,logger=logger)
                    msg = f"{this()}: Update failure. exception: {str(e)}"
                    flash(msg,'error')
                    return msg
                #eturn report_Charging_Resume_Report(**kwargs)
        else:
            msg = f"{this()}: Invalid multiprocess mode: {multimode}"
            flash(msg,'error')
            logger.error(msg)
            return msg
    else:
        flash(f"{this()}: Update={Update} filename={filename} progress={progress}")
        return report_Charging_Resume_Report(**kwargs)
        
        
@main.route('/download/Charging_Resume', methods=['GET','POST'])
@login_required
def download_Charging_Resume():
    logger.debug(f'{this()}: Enter')    
    collectordata=get_collectordata()
    
    db.session.flush()
    db.session.commit()
    
    Cus_Id          =  request.args.get('Cus_Id',None,type=int)
    Cus_Name        =  request.args.get('Cus_Name',None,type=str)
    CIT_Date_From   =  request.args.get('CIT_Date_From',None,type=str)
    CIT_Date_To     =  request.args.get('CIT_Date_To',None,type=str)
    CIT_Status      =  request.args.get('CIT_Status',None,type=int)
    CIT_Status_Value=  request.args.get('CIT_Status_Value',None,type=str)
    Cur_Code        =  request.args.get('Cur_Code',None,type=str)
    Cur_Name        =  request.args.get('Cur_Name',None,type=str)
    Update          =  request.args.get('Update',0,type=int)
    FILTER          =  request.args.get('filter_type',0,type=int)
    CODE            =  request.args.get('filter_code',None)
        
    print(f"**********************************************************")
    print(f"{this()}: FILTER={FILTER} CODE={CODE} {type(CODE)}")
    print(f"**********************************************************")
    CODE=int(CODE)
    # Get Actual Remume Data from Database
    # NOTE: Here needs some Sand-Clock Message or something in case it takes so long ...
    # Gets Charge Resume from DB
    logger.debug(f"**********************************************************")
    logger.debug(f"{this()}: FILTER={FILTER} CODE={CODE} {type(CODE)}")
    logger.debug(f"{this()}: FROM={CIT_Date_From} TO={CIT_Date_To} ST:{CIT_Status} CUR:{Cur_Code}")
    logger.debug(f"{this()}: User={current_user}")
    logger.debug(f"**********************************************************")
    
    rows = db.Get_Charge_Resume_Filter(
                FILTER,
                CODE,
                CIT_Date_From,
                CIT_Date_To,
                CIT_Status,
                Cur_Code,
                User_Id=current_user.id
                )
    if rows is not None:
        logger.debug(f"{this()}: {len(rows)} rows found to export ...")
    else:
        logger.error(f"{this()}: None rows found to export ...")
        
    temp_name   = next(tempfile._get_candidate_names())
    output_file = f"CR_{FILTER}_{CODE}_{CIT_Date_From}_{CIT_Date_To}_{CIT_Status}_{current_user.id}_{temp_name}.xlsx"
    
    d = {
        'detail':[],
        'Cus-Id':Cus_Id,
        'CIT_Date_From':CIT_Date_From,
        'CIT_Date_To':CIT_Date_To,
        'CIT_Status':CIT_Status,
        'Cur_Code':Cur_Code,
        'file':output_file,
        'rows':len(rows)
    }
    # Build list of records to export from query
    for row in rows:
        d['detail'].append({
                'ccCode':row.CC_Code,
                'ccDescription':row.CC_Description,
                'ciName':row.CI_Name,
                'cuDescription':row.CU_Description,
                'hours':row.CIT_Count,
                'mu':row.Rat_MU_Code,
                'price':float(row.Rat_Price),
                'rateCurrency':row.Cur_Code,
                'ratePeriodDescription':row.Rat_Period_Description,
                'resumeQuantityAtRate':float(row.CR_Quantity_at_Rate),
                'totalAtCurrency':float(row.CR_ST_at_Rate_Cur),
                'from':row.CR_Date_From,
                'to':row.CR_Date_To,
        })
    # List of fields in desired order 
    headers=[
                'ccCode',
                'ccDescription',
                'ciName',
                'cuDescription',
                'hours',
                'mu',
                'price',
                'rateCurrency',
                'ratePeriodDescription',
                'resumeQuantityAtRate',
                'totalAtCurrency',
                'from',
                'to',
    ]
    # Normalize data into a Pandas Dataframe
    df1 = json_normalize(d, 'detail')
    # Reorder columns
    df1 = df1.reindex(columns=headers)
    # create temporary filename       
    xlsx_file="%s/%s"%(current_app.root_path,url_for('static',filename='tmp/%s'%(output_file)))
    df1.to_excel(xlsx_file,'Sheet 1')
    return send_file(xlsx_file,as_attachment=True,attachment_filename=output_file)
