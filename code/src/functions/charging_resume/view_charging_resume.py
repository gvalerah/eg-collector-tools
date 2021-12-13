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


# ======================================================================
# Progress bar Beta implementation
# Support routines
# Calculates progress data 
# and returns progress data as a JSON formated string
@main.route('/get-progress')
def get_progress(value,maximum,start=None,message=None,precision=3,expected_format=None,filename=None,previous=0,step=1,logger=None,level=logging.WARNING):
    try:
        if logger is None:
            logger = logging('get_process')
        logger_level = logger.getEffectiveLevel()
        logger.setLevel(level)
        #print(f"pget-progress: logger={logger} {id(logger)} pre={logger_level}")
        logger.debug(f"get progress IN value:{value} maximum:{maximum} start:{start} message:{message} precision:{precision} expected_format:{expected_format} filename:{filename} previous:{previous} step:{step}")
        nowts      = datetime.datetime.now().timestamp()                      # actual time timestamp
        progress   = value/maximum if maximum != 0 else 0                     # % of progress
        elapsed    = nowts - start                                            # seconds elapsed since start
        remaining  = (elapsed * (1-progress))/progress if progress !=0 else 0 # seconds remining for completion
        remaining  = remaining
        eta        = nowts + remaining
        if expected_format is None:
            expected = datetime.datetime.fromtimestamp(
                            eta).strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        else:
            expected = datetime.datetime.fromtimestamp(
                            eta).strftime(expected_format)
        data={
            'value'    : value,                                             # Actual progress discrete value
            'max'      : maximum,                                           # Actual maximum discrete value (100%)
            'start'    : start,                                             # Process init time (loop time)
            'elapsed'  : round(elapsed,precision),                          # Seconds elapsed since loop init
            'remaining': round(remaining,precision),                        # Remaining seconds to loop complete (estimate)
            'message'  : message,                                           # Actual message to be returned
            'progress' : progress,                                          # Progress in % (0.0-1.0)
            'percent'  : round(progress*100,2),                             # Progress in % (0.00%-100.00%)
            'eta'      : eta,                                               # ETA for loop completion (estimate)
            'expected' : expected,                                          # ETA human readable
            'previous' : previous,                                          # Previous displayed value
            'step'     : step,                                              # Display % step
        }
        if message is None:
            message = f"progress={progress*100:.3f}%"
        else:
            message = message.format(**data)
        data.update({'message':message})
        output = json.dumps(data)
        delta = data.get('percent') - previous
        logger.debug(f"percent={data.get('percent')} previous={previous} delta={delta} step={step} {delta>step}")
        
        if previous == 0 or delta > step or data.get('percent')==100:
            if filename is not None:
                data['previous'] = data.get("percent")       # Reported % will become previous 
                output = json.dumps(data)
                with open(filename,"w") as fp:
                    logger.info(f"{os.getppid()}->{os.getpid()} writing: {data.get('message')}")
                    #print         (f"   pwriting: {data.get('message')}")
                    fp.write(output)
    except Exception as e:
        if logger:            
            logger.error(f"get_progress: {str(e)}")
        else:
            sys.stderr.write(f"get_progress: {str(e)}\n")
        output="{}"
    if logger:
        logger.setLevel(logger_level)
    return output
    
@main.route('/read-progress',methods=['GET'])
def read_progress():
    ''' Reads progress data from cache file in file system 
        and returns it as a JSON string
    '''
    progress_filename = request.args.get('filename',None)
    progress_fifo     = request.args.get('fifo',None)
    progress_queue    = request.args.get('queue',0,type=int)
    data={}
    if progress_filename:
        try:
            logger.debug(f"will read file: '{progress_filename}' ...")
            with open(progress_filename,'r') as fp:
                read_bytes = fp.read(1024*1024)
                logger.debug(f"{this()}: read bytes = {len(read_bytes)} bytes")
                data = json.loads(read_bytes.encode())
        except Exception as e:
            emtec_handle_general_exception(e,logger=logger)
            data={}
    elif progress_fifo:
        try:
            logger.warning(f"will read fifo: '{progress_fifo}' ...")
            ffh = os.open(progress_fifo,os.O_RDONLY|os.O_NONBLOCK)
            if ffh:
                read_bytes = os.read(ffh,1024*1024)
                logger.warning(f"{this()}: read bytes = {len(read_bytes)} bytes")
                if len(read_bytes) == 0:
                    data={} # data will be empty 
                else:
                    lines=read_bytes.encode().split('\n')
                    logger.warning(f"{this()}: lines = {len(lines)}")
                    for line in lines:
                        data = json.loads(line) # data will have last line read only
                os.close(ffh)
                logger.warning(f"{this()}: fifo fh {ffh} closed.")
            '''
            with open(progress_filename,'r') as fifo:
                lines = fifo.read()
                if len(lines) == 0:
                    data={} # data will be empty 
                else:
                    lines=lines.split('\n')
                    for line in lines:
                        data = json.loads(line) # data will have last line read only
            '''
        except Exception as e:
            emtec_handle_general_exception(e,logger=logger)
            data={}        
    elif progress_queue:
        logger.warning(f"{this()}: Queue code not implemented queue={queue}... skipping ...")
        if False:
            try:
                item = q.get(block=False)
                status = f"{this()}: OK queue is empty"
            #except queue.exc.Empty:
            #    status = f"{this()}: OK queue is empty"
            except Exception as e:
                status = f"{this()}: ERROR exception: {str(e)}"
                emtec_handle_general_exception(e,logger=logger)
                data={}
    return json.dumps(data)
        
@main.route('/clean-progress',methods=['GET'])
def clean_progress():
    ''' Deletes/cleans up progress data from server
    '''
    status = f"{this()}: UNKNOWN"
    progress_filename = request.args.get('filename',None)
    progress_queue_id = request.args.get('queue',0,type=int)
    if progress_filename:
        try:
            os.remove(filename)
            status = f"{this()}: OK"
        except Exception as e:
            status = f"{this()}: exception: {str(e)}"
    if progress_queue:
        try:
            progress_queue = object(progress_queue_id)
            while not progress_queue.empty():
                item = q.get(block=False)
            status = f"{this()}: OK queue is empty"
        except queue.exc.Empty:
            status = f"{this()}: OK queue is empty"
        except Exception as e:
            status = f"{this()}: ERROR exception: {str(e)}"
            emtec_handle_general_exception(e,logger=logger)
    return status


#main.route('/internal/Charging_Resume_Update', methods=['GET','POST'])
def report_Charging_Resume_Update(kwargs):
    logger.debug(f".................................................")
    logger.debug(f"{this()}: kwargs = {kwargs}")
    logger.debug(f".................................................")
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
        fifo             = kwargs.get('fifo')
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
            fast=True,
            callback=display_advance,
            filename=filename,
            progress=progress,
            fifo=fifo,
            fmt='json',
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
    fifo             =  os.path.join(temp_dir,f'{this()}.fifo')
    try:
        os.mkfifo(fifo)
        logger.info(f"named pipe '{fifo}' created ...")
    except FileExistsError:
        # the file already exists
        logger.info(f"named pipe '{fifo}' already exists while starting ...")
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
        'fifo'             :  fifo, # callback arguments
        'queue'            :  None, # callback arguments should be Queue id if any
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

        data = {
            'host'    : 'localhost',
            'maximum' : 100,
            'filename': progress,
            'fifo'    : fifo,
            'percent' : 0,
            'value'   : 0,
        }
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
                                data             = data         # Temporary for progress bar functions/views
                                )
                except Exception as e:
                    msg = f"{this()}: Exception:  {str(e)}"
                    flash(msg,'error')
                    return msg
        elif multimode == 'thread':            
                try:
                    logger.warning(f"{this()}: Initiating Thread Update={Update} filename={filename} progress={progress} fifo={fifo}")
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
                                data             = data
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
