# ======================================================================
# View for Get Charging Resume from DB
# (c) Sertechno 2018
# GLVH @ 2019-08-16
# GLVH @ 2019-08-18 Refactoring to ORM DB Only
# GLVH @ 2020-10-25 Proper sharding and initialization handling
# ======================================================================

from pprint                         import pformat
from emtec.collector.forms          import frm_charging_resume
from emtec.collector.forms          import frm_charging_resume_customer
from emtec.collector.forms          import frm_charging_resume_costcenter
from emtec.collector.forms          import frm_charging_resume_level_new
from emtec.collector.forms          import frm_charging_resume_platform_new
from emtec.collector.forms          import frm_charging_resume_all_new
from babel.numbers                  import format_number
from babel.numbers                  import format_decimal
from babel.numbers                  import format_percent
from emtec.collector.db.orm_model   import Configuration_Items
from emtec.feedback                 import *
import tempfile
import threading
import queue
import configparser
import uuid

# A map to hold queues or othr items ammong threads
FEEDBACK={}

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
    try:
        logger.debug(f'{this()}: Enter')
        Filter =  request.args.get('filter','customer',type=str)
        print(f"{this}: current_app = {current_app}")
        print(f"{this}: current_user = {current_user}")
        collectordata=get_collectordata()
        print(f"{this}: collectordata = {collectordata}")
        logger.debug(f"{this()}: getting configuration information")
        config_parser = configparser.ConfigParser()
        logger.debug(f"{this()}: current_app.config.get('COLLECTOR_CONFIG_FILE') = {current_app.config.get('COLLECTOR_CONFIG_FILE')}")
        config_file   = current_app.config.get('COLLECTOR_CONFIG_FILE')
        logger.debug(f"{this()}: config_file = {config_file}")
        try:
            config_parser.read(config_file)
            logger.debug(f"{this()}: config_parser loaded with '{config_file}'")
        except Exception as e:
            emtec_handle_general_exception(e,logger=logger)
            return emtec_handle_general_exception(e)
            
        logger.debug(f"{this()}: setting session data.")
        session['data'] =  {    
            'Filter'        : Filter,
            'User_Id'       : 0,
            'Cus_Id'        : None,
            'CC_Id'         : None,
            'Pla_Id'         : None,
            'CIT_Date_From' : collectordata['COLLECTOR_PERIOD']['start'], 
            'CIT_Date_To'   : collectordata['COLLECTOR_PERIOD']['end'], 
            'CIT_Status'    : 1,
            'Cur_Code'      : None,
            'Level'         : 0
            }
            
        logger.debug(f"{this()} setting variables ...")
        Cus_Id = Cus_Name       = None
        CC_Id  = CC_Description = None
        Pla_Id = Pla_Name       = None
        Level  = Level_Name     = None

        template = 'report_charging_resume.html'
        if   Filter == 'customer':
            form = frm_charging_resume_customer()
        elif Filter == 'costcenter':
            form = frm_charging_resume_costcenter()
        elif Filter == 'resume':
            form = frm_charging_resume_level_new()
            template = 'report_charging_resume_level.html'
        elif Filter == 'platform':
            form = frm_charging_resume_platform_new()
        elif Filter == 'all':
            form = frm_charging_resume_all_new()
        else:
            form = frm_charging_resume()
            
        logger.debug(f"{this()}: Filter={Filter} form={form} template={template}")

        # ------------------------------------------------------------------------------
        # Will setup filter to consider only Currencies with actual Exchange Rates in DB
        # Commit all pending DB states in order to refresh data
        logger.debug(f"{this()} commit session and flushing DB ...")
        db.session.commit()
        db.session.flush()
        # Prepare query
        # Execute query and convert in list for further use in choices selection

        logger.debug(f"{this()} Initializing form choices ...")
        if hasattr(form,'CC_Id'):
            form.CC_Id.choices      = db.session.query(cost_center.CC_Id,cost_center.CC_Description).all()
        if hasattr(form,'Cus_Id'):
            form.Cus_Id.choices     = db.session.query(customer.Cus_Id,customer.Cus_Name).all()
        if hasattr(form,'Pla_Id'):
            form.Pla_Id.choices     = db.session.query(platform.Pla_Id,platform.Pla_Name).all()
        if hasattr(form,'CIT_Status'):
            form.CIT_Status.choices = db.session.query(cit_status.CIT_Status,cit_status.Value).all()
        if hasattr(form,'Cur_Code'):
            query = db.session.query(exchange_rate.Cur_Code.distinct().label('Cur_Code'))
            cur_choices = [row.Cur_Code for row in query.all()]
            form.Cur_Code.choices   = db.session.query(currency.Cur_Code,currency.Cur_Name).filter(currency.Cur_Code.in_(cur_choices)).all()
        if hasattr(form,'Level'):
            form.Level.choices      = [(1,"Cost Center"),(2,"Device"),(3,"Component")]

        logger.debug(f"{this()} checking if form validated ...")
        if form.validate_on_submit():
            logger.debug(f"{this()} form.validate_on_submit() = True")
            session['data']['Filter'        ] = Filter 
            if hasattr(form,'User_Id')      : session['data']['User_Id'       ] = form.User_Id 
            if hasattr(form,'Cus_Id')       : session['data']['Cus_Id'        ] = form.Cus_Id.data
            if hasattr(form,'CC_Id')        : session['data']['CC_Id'         ] = form.CC_Id.data
            if hasattr(form,'Pla_Id')       : session['data']['Pla_Id'        ] = form.Pla_Id.data
            if hasattr(form,'CIT_Date_From'): session['data']['CIT_Date_From' ] = form.CIT_Date_From.data
            if hasattr(form,'CIT_Date_To')  : session['data']['CIT_Date_To'   ] = form.CIT_Date_To.data
            if hasattr(form,'CIT_Status')   : session['data']['CIT-Status'    ] = form.CIT_Status.data
            if hasattr(form,'Cur_Code')     : session['data']['Cur_Code'      ] = form.Cur_Code.data
            if hasattr(form,'Level')        : session['data']['Level'         ] = form.Level.data

            logger.debug(f"{this()}: session[data]={session.get('data')}")
            logger.debug(f"{this()}: current_user={current_user}")
            
            Cus_Id   = None
            Cus_Name = None
            CC_Id    = None
            CC_Description = None
            Cur_Code = None
            Cur_Name = None
            Pla_Id   = None
            Pla_Name = None
            # Get the Selected options index for string lists
            if hasattr(form,'Cus_Id'):
                for i in range(len(form.Cus_Id.choices)):
                    if form.Cus_Id.choices[i][0]==form.Cus_Id.data:
                        Cus_Id   = form.Cus_Id.data
                        Cus_Name = form.Cus_Id.choices[i][1]
            if hasattr(form,'Pla_Id'):
                for i in range(len(form.Pla_Id.choices)):
                    if form.Pla_Id.choices[i][0]==form.Pla_Id.data:
                        Pla_Id   = form.Pla_Id.data
                        Pla_Name = form.Pla_Id.choices[i][1]
            if hasattr(form,'CC_Id'):
                for i in range(len(form.CC_Id.choices)):
                    if form.CC_Id.choices[i][0]==form.CC_Id.data:
                        CC_Id          = form.CC_Id.data
                        CC_Description = form.CC_Id.choices[i][1]
            if hasattr(form,'Cur_Code'):
                for i in range(len(form.Cur_Code.choices)):
                    if form.Cur_Code.choices[i][0]==form.Cur_Code.data:
                        Cur_Code = form.Cur_Code.data
                        Cur_Name = form.Cur_Code.choices[i][1]
            if hasattr(form,'CIT_Status'):
                for i in range(len(form.CIT_Status.choices)):
                    if form.CIT_Status.choices[i][0]==form.CIT_Status.data:
                        CIT_Status       = form.CIT_Status.data
                        CIT_Status_Value = form.CIT_Status.choices[i][1]
            if hasattr(form,'Level'):
                for i in range(len(form.Level.choices)):
                    if form.Level.choices[i][0]==form.Level.data:
                        Level       = form.Level.data
                        Level_Name = form.Level.choices[i][1]

        
            if     form.submit_Report.data:
                logger.debug(f"{this()} form.submit_Report.data")
                logger.warning(f"{this()}: 277 Filter = {Filter}")
                return redirect(url_for('.report_Charging_Resume_Progress',
                                    Filter          = Filter,
                                    User_Id         = current_user.id,
                                    Cus_Id          = Cus_Id,
                                    Cus_Name        = Cus_Name,
                                    Pla_Id          = Pla_Id,
                                    Pla_Name        = Pla_Name,
                                    CC_Id           = CC_Id,
                                    CC_Description  = CC_Description,
                                    CIT_Date_From   = form.CIT_Date_From.data,
                                    CIT_Date_To     = form.CIT_Date_To.data,
                                    CIT_Status      = CIT_Status,
                                    CIT_Status_Value= CIT_Status_Value,
                                    Cur_Code        = Cur_Code,
                                    Cur_Name        = Cur_Name,
                                    Update          = 0,
                                    Level           = Level,
                                    Level_Name      = Level_Name,
                                    template        = template
                                    ))
            if     form.submit_Update.data:
                logger.debug(f"{this()} form.submit_Update.data")
                return redirect(url_for('.report_Charging_Resume_Progress',
                                    Filter          = Filter,
                                    User_Id         = current_user.id,
                                    Cus_Id          = Cus_Id,
                                    Cus_Name        = Cus_Name,
                                    Pla_Id          = Pla_Id,
                                    Pla_Name        = Pla_Name,
                                    CC_Id           = CC_Id,
                                    CC_Description  = CC_Description,
                                    CIT_Date_From   = form.CIT_Date_From.data,
                                    CIT_Date_To     = form.CIT_Date_To.data,
                                    CIT_Status      = CIT_Status,
                                    CIT_Status_Value= CIT_Status_Value,
                                    Cur_Code        = Cur_Code,
                                    Cur_Name        = Cur_Name,
                                    Update          = 1,
                                    Level           = Level,
                                    Level_Name      = Level_Name,
                                    template        = template
                                    ))
            elif   form.submit_Cancel.data:
                logger.debug(f"{this()} form.submit_Cancel.data")
                flash('{this()}: Report discarded ...')
            else:
                logger.debug(f"{this()} form validated but not submited. Report to Support")
                flash('{this()}: form validated but not submited. Report to Support ...','error')
            return redirect(url_for('.forms_Get_Charging_Resume_Progress'))
        
        # Setting defaults from config/DB/environment
        logger.debug(f"{this()} loading session data defaults ...")
        if session['data']['CC_Id']   is None:
            session['data']['CC_Id']     = current_user.cost_center.CC_Id    
        if session['data']['Cus_Id']   is None:
            session['data']['Cus_Id']   = current_user.cost_center.Cus_Id    
        if session['data']['Cur_Code'] is None:
            session['data']['Cur_Code'] = current_user.cost_center.Cur_Code
        if session['data']['Pla_Id']   is None:
            session['data']['Pla_Id']   = config_parser.getint('Defaults','platform',fallback=1)

        logger.debug(f"{this()} loading form fields from session data ...")
        if hasattr(form,'User_Id')      :
            form.User_Id            = session['data']['User_Id']
        if hasattr(form,'Cus_Id')       :
            form.Cus_Id.data        = session['data']['Cus_Id']
        if hasattr(form,'CC_Id')       :
            form.CC_Id.data        = session['data']['CC_Id']
        if hasattr(form,'Pla_Id')       :
            form.Pla_Id.data        = session['data']['Pla_Id']
        if hasattr(form,'CIT_Date_From'):
            form.CIT_Date_From.data = session['data']['CIT_Date_From']
        if hasattr(form,'CIT_Date_To')  :
            form.CIT_Date_To.data   = session['data']['CIT_Date_To']
        if hasattr(form,'CIT_Status')   :
            form.CIT_Status.data    = session['data']['CIT_Status']
        if hasattr(form,'Cur_Code')     :
            form.Cur_Code.data      = session['data']['Cur_Code']
        if hasattr(form,'Level')     :
            form.Level.data         = session['data']['Level']

        logger.debug(f"{this()}: ---------------------------------------")
        logger.debug(f"{this()}: template      = {template}")
        logger.debug(f"{this()}: data          = {session.get('data')}")
        logger.debug(f"{this()}: form          = {form}")
        logger.debug(f"{this()}: ---------------------------------------")
        for field in form._fields:
            logger.debug(f"{this()}: field  = {field} {type(field)}")
            logger.debug(f"{this()}: {field}  = {getattr(form,field)}")
        logger.debug(f"{this()}: ---------------------------------------")
        
        logger.debug(f"{this()} render_template('charging_resume.html'")
        return render_template(
                    'charging_resume.html',
                    form          = form, 
                    data          = session.get('data'), 
                    collectordata = collectordata
                    #collectordata = get_collectordata()
                    )
    except Exception as e:
        emtec_handle_general_exception(e,logger=logger)
        # idea es: return render_template(50x,exception=emtec_handle_general_exception(e))
        return emtec_handle_general_exception(e)

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
            logger.warning(f"{this()}: Updated Name CUs = {updated_cus}")
        # BE SURE all CU records has proper rate id
        updated_cus = db.Update_CU_Rates()
        if updated_cus:
            logger.warning(f"{this()}: Updated Rate CUs = {updated_cus}")
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

@main.route('/read-progress',methods=['GET'])
def read_progress():
    ''' Reads progress data from cache file in file system 
        and returns it as a JSON string
    '''
    global FEEDBACK
    ipc_mode          = request.args.get('ipc_mode'    , None)
    ipc_id            = request.args.get('ipc_id'      , None)
    logger.debug(f"{this()}: IPC mode:{ipc_mode} id:{ipc_id} FEEDBACK = {FEEDBACK}")  

    temp_dir = tempfile.gettempdir()   
    error = False 
    if   ipc_mode == 'filesystem':
        progress_filename = f"{temp_dir}/{ipc_id}"  
    elif ipc_mode == 'fifo':
        progress_fifo     = f"{temp_dir}/{ipc_id}"  
    elif ipc_mode == 'queue':
        progress_queue    = FEEDBACK.get(ipc_id,None)
        if progress_queue is not None:
            logger.debug(f"{this()}: IPC mode:{ipc_mode} id:{ipc_id} queue:{progress_queue} size={progress_queue.qsize()} FEEDBACK = {FEEDBACK}")  
        else:
            logger.error(f"{this()}: IPC mode:{ipc_mode} id:{ipc_id} queue:{progress_queue} size=None FEEDBACK = {FEEDBACK} url={request.url}")              
            error = True
    else:
        logger.error(f"{this()}: IPC invalid mode:{ipc_mode} id:{ipc_id} FEEDBACK = {FEEDBACK}")  
        error = True
    data={}
    if not error:
        if   ipc_mode == 'filesystem':
            try:
                logger.debug(f"will read file: '{progress_filename}' ...")
                with open(progress_filename,'r') as fp:
                    read_bytes = fp.read(1024*1024)
                    logger.debug(f"{this()}: read bytes = {len(read_bytes)} bytes")
                    data = json.loads(read_bytes.encode())
            except FileNotFoundError:
                logger.debug(f"{this()}: File '{progress_filename}' does not exist.")
            except Exception as e:
                emtec_handle_general_exception(e,logger=logger)
                data={}
            finally:
                # anyway remove temporary file
                if os.path.exists(progress_filename):
                    os.remove(progress_filename)
        elif ipc_mode == 'fifo':
            try:
                logger.warning(f"{this()}: will read fifo: '{progress_fifo}' ...")
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
            except Exception as e:
                emtec_handle_general_exception(e,logger=logger)
                data={}        
        elif ipc_mode == 'queue':
            if progress_queue:
                logger.debug(f"{this()}: will read queue: '{ipc_id}' ... {progress_queue} qsize={progress_queue.qsize()}")
                try:
                    #data = progress_queue.get(block=False,timeout=1)
                    data = progress_queue.get(block=False)
                    progress_queue.task_done()
                except Empty:
                    logger.debug(f"{this()}: empty queue {ipc_id}.")
                    data={}
                except Exception as e:
                    emtec_handle_general_exception(e,logger=logger)
                    data={}
            else:
                logger.warning(f"{this()}: Invalid queue {progress_queue} FEEDBACK = {FEEDBACK}")
                data={}
    if len(data):
        logger.debug(f"{this()}: read from: {ipc_mode}:{ipc_id} => {type(data)} data:{data}")  
    return json.dumps(data)
        
@main.route('/clean-progress',methods=['GET'])
def clean_progress():
    ''' Deletes/cleans up progress data from server
    '''
    global FEEDBACK
    status = f"{this()}: UNKNOWN"
    
    ipc_mode          = request.args.get('ipc_mode'    , None)
    ipc_id            = request.args.get('ipc_id'      , None)

    temp_dir = tempfile.gettempdir()
    
    if   ipc_mode == 'filesystem':
        progress_filename = f"{temp_dir}/{ipc_id}"  
    elif ipc_mode == 'fifo':
        progress_fifo     = f"{temp_dir}/{ipc_id}"  
    elif ipc_mode == 'queue':
        progress_queue    = FEEDBACK.get(ipc_id)
    else:
        logger.error(f"{this()}: IPC invalid mode:{ipc_mode} id:{ipc_id} FEEDBACK = {FEEDBACK}")  

    logger.debug(f"{this()}: IPC mode:{ipc_mode} id:{ipc_id} FEEDBACK = {FEEDBACK}")  

    if ipc_mode == 'filesystem':
        if os.path.exists(progress_filename):
            try:
                os.remove(progress_filename)
                status = f"{this()}: file: '{progress_filename}' removed OK"
            except Exception as e:
                status = f"{this()}: exception: {str(e)}"
        else:
            status = f"{this()}: file: '{progress_filename}' did not exist."
    if ipc_mode == 'fifo':
        try:
            os.remove(progress_fifo)
            status = f"{this()}: named pipe fifo'{progress_fifo}' removed OK"
        except Exception as e:
            status = f"{this()}: exception: {str(e)}"
    if ipc_mode == 'queue':
        try:
            while not progress_queue.empty():
                item = progress_queue.get(block=False)
            FEEDBACK.pop(ipc_id,None)
            status = f"{this()}: OK queue '{ipc_id}' is empty and deleted now"
        except queue.exc.Empty:
            status = f"{this()}: OK queue is empty"
        except Exception as e:
            status = f"{this()}: ERROR exception: {str(e)}"
            emtec_handle_general_exception(e,logger=logger)
    logger.info(f"{this()}: status = {status}")
    data = { 'status' : status }
    return json.dumps(data)

def report_Charging_Resume_Update(kwargs):
    logger.debug(f".................................................")
    logger.debug(f"{this()}: kwargs = {kwargs}")
    logger.debug(f".................................................")
    global FEEDBACK
    try:
        app_ctx          = kwargs.get('app_ctx')
        db               = kwargs.get('db')
        current_user     = kwargs.get('current_user')
        Filter           = kwargs.get('Filter')
        User_Id          = kwargs.get('User_Id')
        Cus_Id           = kwargs.get('Cus_Id')
        Cus_Name         = kwargs.get('Cus_Name')
        CC_Id            = kwargs.get('CC_Id')
        CC_Description   = kwargs.get('CC_Description')
        Level            = kwargs.get('Level')
        Level_Name       = kwargs.get('Level_Name')
        CIT_Date_From    = kwargs.get('CIT_Date_From')
        CIT_Date_To      = kwargs.get('CIT_Date_To')
        CIT_Status       = kwargs.get('CIT_Status')
        CIT_Status_Value = kwargs.get('CIT_Status_Value')
        Cur_Code         = kwargs.get('Cur_Code')
        Cur_Name         = kwargs.get('Cur_Name')
        Update           = kwargs.get('Update')
        callback         = kwargs.get('callback')
        ipc_mode         = kwargs.get('ipc_mode')
        ipc_id           = kwargs.get('ipc_id')
        ipc_fmt          = kwargs.get('ipc_fmt')
        verbose          = kwargs.get('verbose')
        fast             = kwargs.get('fast',1)
        step             = kwargs.get('step',0.1) # Callback step default = 10%

        fast = True if str(fast).upper() in ['1','TRUE','T','VERDADERO','V','YES','Y'] else False
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
            logger.debug(f"{this()}: Updated Name CUs = {updated_cus:,.0f}")
        # BE SURE all CU records has proper rate id
        updated_cus = db.Update_CU_Rates()
        if updated_cus:
            logger.debug(f"{this()}: Updated Rate CUs = {updated_cus:,.0f}")
        # --------------------------------------------------------------
        
        query = db.session.query(
                Configuration_Items.CI_Id
                ).filter(Configuration_Items.Cus_Id==Cus_Id)
        logger.debug (f"{this()}: Cus_Id= {Cus_Id} query: {query}")
        if Filter == 'costcenter':
            ccs = db.get_cost_centers(CC_Id)
            logger.debug(f"Fileter by CC_Id in {ccs}")
            query = query.filter(Configuration_Items.CC_Id.in_(ccs))
        CI = query.order_by( 
                    Configuration_Items.CC_Id,
                    Configuration_Items.CI_Id
                ).all()
        logger.debug (f"{this()}: {len(CI)} CI's found for customer {Cus_Id}")
        logger.debug (f"{this()}: {pformat(CI)}")
        resume_records=0

        logger.info(f"{this()}: Updating Charge Resume Update ...")
        ci_list = []
        if filter == 'costcenter' and CC_Id is not None:
            ci_list = None
        else:
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
            XCC_ID=CC_Id,
            fast=fast,
            callback=display_advance,
            step=step,
            ipc_mode=ipc_mode,
            ipc_id=ipc_id,
            fmt=ipc_fmt,
            verbose=verbose,
            FEEDBACK=FEEDBACK
            )
        logger.info(f"{this()}: Updated {records:,.0f} records")
        if records == 0:
            display_advance(
                value=100,maximum=100,last_shown=100,
                logger=logger,
                message='Proces completed. No data found.'
            )
    except Exception as e:
        emtec_handle_general_exception(e,logger=logger)
        records = 0
    logger.info(f"{this()}: return number of updated records = {records:,.0f}. Update process completed.")
    return records

def report_Charging_Resume_Report(**kwargs):
    logger.debug(f"{this()}: IN kwargs = {kwargs}")
    Filter           = kwargs.get('Filter')
    User_Id          = kwargs.get('User_Id')
    Cus_Id           = kwargs.get('Cus_Id')
    Cus_Name         = kwargs.get('Cus_Name')
    CC_Id            = kwargs.get('CC_Id')
    CC_Description   = kwargs.get('CC_Description')
    CIT_Date_From    = kwargs.get('CIT_Date_From')
    CIT_Date_To      = kwargs.get('CIT_Date_To')
    CIT_Status       = kwargs.get('CIT_Status')
    CIT_Status_Value = kwargs.get('CIT_Status_Value')
    Cur_Code         = kwargs.get('Cur_Code')
    Cur_Name         = kwargs.get('Cur_Name')
    Pla_Id           = kwargs.get('Pla_Id')
    Pla_Name         = kwargs.get('Pla_Name')
    Update           = kwargs.get('Update')
    Level            = kwargs.get('Level')
    Level_Name       = kwargs.get('Level_Name')
    template         = kwargs.get('template')
    if   Filter == 'customer'  : 
        FILTER = FILTER_CUSTOMER
        CODE   = Cus_Id
    elif Filter == 'costcenter': 
        FILTER = FILTER_COST_CENTER
        CODE   = CC_Id
    elif Filter == 'period'    : 
        FILTER = FILTER_PERIOD
        CODE   = None
    elif Filter == 'platform'  : 
        FILTER = FILTER_PLATFORM
        CODE = Pla_Id
    else: 
        FILTER = FILTER_ALL
        CODE = None
    rows = db.Get_Charge_Resume_Filter(
                FILTER,
                CODE,
                CIT_Date_From,
                CIT_Date_To,
                CIT_Status,
                Cur_Code,
                CC_Id   = CC_Id,
                Pla_Id  = Pla_Id,
                User_Id = User_Id
                )
    logger.debug(f"{this()}: PRE RENDER")
    logger.debug(f"{this()}: len rows         = {len(rows)}")
    logger.debug(f"{this()}: Filter           = {Filter}")
    logger.debug(f"{this()}: Level            = {Level}")
    logger.debug(f"{this()}: Level_Name       = {Level_Name}")
    logger.debug(f"{this()}: Cus_Id           = {Cus_Id}")
    logger.debug(f"{this()}: Cus_Name         = {Cus_Name}")
    logger.debug(f"{this()}: CC_Id            = {CC_Id}")
    logger.debug(f"{this()}: CC_Description   = {CC_Description}")
    logger.debug(f"{this()}: Pla_Id           = {Pla_Id}")
    logger.debug(f"{this()}: Pla_Name         = {Pla_Name}")
    logger.debug(f"{this()}: CIT_Date_From    = {CIT_Date_From}")
    logger.debug(f"{this()}: CIT_Date_To      = {CIT_Date_To}")
    logger.debug(f"{this()}: CIT_Status       = {CIT_Status}")
    logger.debug(f"{this()}: CIT_Status_Value = {CIT_Status_Value}")                
    logger.debug(f"{this()}: Cur_Code         = {Cur_Code}")
    logger.debug(f"{this()}: Cur_Name         = {Cur_Name}")
    logger.debug(f"{this()}: template         = {template}")
    try:
        logger.info(f"{this()}: will render template '{template}'. function completed.")
        return render_template(
                    template,
                    rows             = rows,
                    Cus_Id           = Cus_Id,
                    Cus_Name         = Cus_Name,
                    CC_Id            = Cus_Id,
                    CC_Description   = CC_Description,
                    Pla_Id           = Pla_Id,
                    Pla_Name         = Pla_Name,
                    CIT_Date_From    = CIT_Date_From,
                    CIT_Date_To      = CIT_Date_To,
                    CIT_Status       = CIT_Status,
                    CIT_Status_Value = CIT_Status_Value,                
                    Cur_Code         = Cur_Code,
                    Cur_Name         = Cur_Name,
                    collectordata    = get_collectordata(),
                    filter_type      = FILTER,
                    filter_code      = CODE,
                    Level            = Level,
                    Level_Name       = Level_Name,
                    )
    except Exception as e:
        emtec_handle_general_exception(e,logger=logger)
        return f"{this()}: Exception:  {str(e)}"

@main.route('/report/Charging_Resume_Progress', methods=['GET','POST'])
@login_required
def report_Charging_Resume_Progress():
    global FEEDBACK
    try:
        logger.debug(f'{this()}: Enter')    
        collectordata=get_collectordata()
        logger.debug(f"{this()}: flushing and commiting session")
        db.session.flush()
        db.session.commit()
        
        logger.debug(f"{this()}: getting request arguments")
        Filter           =  request.args.get('Filter','customer',type=str)
        User_Id          =  request.args.get('User_Id',None,type=int)
        Cus_Id           =  request.args.get('Cus_Id',None,type=int)
        Cus_Name         =  request.args.get('Cus_Name',None,type=str)
        CC_Id            =  request.args.get('CC_Id',None,type=int)
        CC_Description   =  request.args.get('CC_Description',None,type=str)
        Pla_Id           =  request.args.get('Pla_Id',None,type=int)
        Pla_Name         =  request.args.get('Pla_Name',None,type=str)
        CIT_Date_From    =  request.args.get('CIT_Date_From',None,type=str)
        CIT_Date_To      =  request.args.get('CIT_Date_To',None,type=str)
        CIT_Status       =  request.args.get('CIT_Status',None,type=int)
        CIT_Status_Value =  request.args.get('CIT_Status_Value',None,type=str)
        Cur_Code         =  request.args.get('Cur_Code',None,type=str)
        Cur_Name         =  request.args.get('Cur_Name',None,type=str)
        Update           =  request.args.get('Update',0,type=int)
        Level            =  request.args.get('Level',0,type=int)
        Level_Name       =  request.args.get('Level_Name',None,type=str)
        template         =  request.args.get('template',None,type=str)
        step             =  request.args.get('step',None)
        logger.debug(f"{this()}: getting variable defaults")

        if Cus_Id is None: 
            Cus_Id = current_user.cost_center.Cus_Id
            Cus_Name = db.session.query(Customers.Cus_Name
                        ).filter(Customers.Cus_Id==Cus_Id).first()
            if Cus_Name: Cus_Name=Cus_Name[0]
        if CC_Id is None: 
            CC_Id = current_user.cost_center.CC_Id
            CC_Description = db.session.query(Cost_Centers.CC_Description
                        ).filter(Cost_Centers.CC_Id==CC_Id).first()
            if CC_Description: CC_Description=CC_Description[0]
        if Pla_Id is not None: 
            Pla_Name = db.session.query(Platforms.Pla_Name
                        ).filter(Platforms.Pla_Id==Pla_Id).first()
            if Pla_Name: Pla_Name=Pla_Name[0]
        if Level:
            Level_Name = [None,'Cost Center','Device','Component'][Level]
            
        # IPC details
        logger.debug(f"{this()}: getting IPC details from configuration file {current_app.config.get('COLLECTOR_CONFIG_FILE')}...")
        parser = configparser.ConfigParser()
        parser.read(current_app.config.get("COLLECTOR_CONFIG_FILE"))
        if step is None:
            step = parser.getfloat('IPC','step',fallback=0.1)
        ipc_mode = parser.get('IPC','mode')
        ipc_fmt  = parser.get('IPC','format')
        try:
            ipc_id   = str(uuid.uuid4())
            logger.debug(f"{this()}: IPC id from uuid4 is {ipc_id}")
        except Exception as e:
            logger.warning(f"{this()}: IPC id from uuid4 exception: {str(e)}")
            ipc_id   = next(tempfile._get_candidate_names())
            logger.debug(f"{this()}: IPC id from tempfile is {ipc_id}")
        logger.info(f"{this()}: IPC: mode={ipc_mode} id={ipc_id}")
        temp_dir         =  tempfile.gettempdir()
        logger.info(f"{this()}: initializing IPC variables ...")
        if   ipc_mode == 'filesystem':
            progress_filename = f"{temp_dir}/{ipc_id}"  
            logger.info(f"{this()}: progress_filename = {progress_filename}")  
        elif ipc_mode == 'fifo':
            progress_fifo     = f"{temp_dir}/{ipc_id}"  
            try:
                os.mkfifo(progress_fifo)
                logger.info(f"{this()}: named pipe '{progress_fifo}' created ...")
            except FileExistsError:
                # the file already exists
                logger.warning(f"{this()}: named pipe '{progress_fifo}' already exists while starting ...")
            except Exception as e:
                emtec_handle_general_exception(e,logger=logger)
        elif ipc_mode == 'queue':
            FEEDBACK.update({ipc_id:queue.Queue()})
            progress_queue    = FEEDBACK.get(ipc_id,None)
            logger.info(f"{this()}: progress_queue = {progress_queue}")  
            if progress_queue is None:
                logger.error(f"No valid queue available for id={ipc_id} FEEDBACK={FEEDBACK}")

        verbose          =  1

        logger.debug(f"{this()}: current_app     = {current_app}")
        logger.debug(f"{this()}: current_user    = {current_user}")
        logger.debug(f"{this()} db              = {db}")
        logger.info(f"{this()}: pushing app context ...")
        app_ctx = current_app.app_context()
        logger.info(f"{this()}: populating kwargs ...")
        
        kwargs = {
            'current_app'      :  current_app,
            'current_user'     :  current_user,
            'app_ctx'          :  app_ctx,
            'db'               :  db,
            'Filter'           :  Filter,
            'Level'            :  Level,
            'Level_Name'       :  Level_Name,
            'template'         :  template,
            'User_Id'          :  User_Id,
            'Cus_Id'           :  Cus_Id,
            'Cus_Name'         :  Cus_Name,
            'CC_Id'            :  CC_Id,
            'CC_Description'   :  CC_Description,
            'Pla_Id'           :  Pla_Id,
            'Pla_Name'         :  Pla_Name,
            'CIT_Date_From'    :  CIT_Date_From,
            'CIT_Date_To'      :  CIT_Date_To,
            'CIT_Status'       :  CIT_Status,
            'CIT_Status_Value' :  CIT_Status_Value,
            'Cur_Code'         :  Cur_Code,
            'Cur_Name'         :  Cur_Name,
            'Update'           :  Update,
            'Level'            :  Level,
            'callback'         :  display_advance,
            'step'             :  step,
            'ipc_mode'         :  ipc_mode,
            'ipc_id'           :  ipc_id,
            'ipc_fmt'          :  ipc_fmt,
            'verbose'          :  verbose,  # callback arguments
            'FEEDBACK'         :  FEEDBACK,  # callback arguments
        }
        logger.debug(f"{this()}: kwargs={kwargs}")
        # Updated cached data for this specific query if requested 
        logger.info(f"{this()}: Update = {Update}")
        if Update == 1:
            logger.info(f"{this()}: Enter Update ...")
            try:
                db.session.flush()
            except Exception as e:
                logger.warning(f"{this()}: DB Flush exception: {str(e)}")

            data = {
                'host'    : 'localhost',
                'maximum' : 100,
                'percent' : 0,
                'value'   : 0,
                'mode'    : ipc_mode,
                'id'      : ipc_id,
            }
            try:
                logger.info(f"{this()}: Initiating Thread Update={Update} IPC mode={ipc_mode} id={ipc_id} filter={Filter}/{kwargs.get('Filter')}")
                threading.Thread(
                    target=report_Charging_Resume_Update,
                    args=(kwargs,)
                    ).start()
                logger.info(f"{this()}: Inmediatelly rendering bar html")

                if   Filter == 'customer'  : FILTER = FILTER_CUSTOMER
                elif Filter == 'costcenter': FILTER = FILTER_COST_CENTER
                elif Filter == 'period'    : FILTER = FILTER_PERIOD
                elif Filter == 'platform'  : FILTER = FILTER_PLATFORM
                elif Filter == 'all'       : FILTER = FILTER_ALL
                else:                        FILTER = FILTER_CUSTOMER
                
                return render_template('report_charging_resume_update.html',
                            Filter           = Filter,
                            Cus_Id           = Cus_Id,
                            Cus_Name         = Cus_Name,
                            CC_Id            = CC_Id,
                            CC_Description   = CC_Description,
                            Pla_Id           = Pla_Id,
                            Pla_Name         = Pla_Name,
                            Level            = Level,
                            Level_Name       = Level_Name,
                            CIT_Date_From    = CIT_Date_From,
                            CIT_Date_To      = CIT_Date_To,
                            CIT_Status       = CIT_Status,
                            CIT_Status_Value = CIT_Status_Value,                
                            Cur_Code         = Cur_Code,
                            Cur_Name         = Cur_Name,
                            collectordata    = get_collectordata(),
                            filter_type      = FILTER,
                            filter_code      = Cus_Id,
                            ipc_mode         = ipc_mode,
                            ipc_id           = ipc_id,
                            data             = data # 821
                            )
            except Exception as e:
                emtec_handle_general_exception(e,logger=logger)
                msg = f"{this()}: Update failure. exception: {str(e)}"
                flash(msg,'error')
                return msg
        else:
            logger.debug(f"{this()}: kwargs = {kwargs}")
            return report_Charging_Resume_Report(**kwargs)
    except Exception as e:
        # idea es: return render_template(50x,exception=emtec_handle_general_exception(e))
        return emtec_handle_general_exception(e,logger=logger)
        
        
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

'''
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
'''

