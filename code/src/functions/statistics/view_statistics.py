# =============================================================================
# Statistics basic reporter
# (c) Sertechno 2022
# GLVH @ 2022-04-12
# =============================================================================

# view required imports
import os
import json
import datetime
from pprint import pprint
from xml.dom.expatbuilder import FragmentBuilderNS
from flask import request
from pprint import pprint,pformat
from emtec.collector.statistics import *
# view required functions

def Gen_Resume_Graphics(
        x,y,resume,agregation,
        include_history    = False,
        max_history_months = 13,
        rotation           = 0,
        precision          = 0,
        logger             = logging.getLogger()
    ):
    filename = None
    history_filename = None

    xfield,xtitle = x.split(':')
    ytokens = y.split(',')
    yfields = []
    ytitles = []
    for i in range(len(ytokens)):
        field,title=ytokens[i].split(':')
        yfields.append(field)
        ytitles.append(title)

    x=[]
    y=[]
    xh=[] 
    yh=[]
    series={}
    series_to_plot=[]
    units = resume.get('currency')

    name = '+'.join(resume.get('periods',[]))

    graphic1     = None
    graphic1     = Graphic(name)
    graphic2     = None
    graphic2     = Graphic(f"{name}_history")
    for i in range(len(yfields)):
        y.append([])
        series_to_plot.append(i)
    for row in resume.get('rows'):
        x.append(getattr(row,xfield))
        for i in range(len(y)):
            y[i].append(getattr(row,yfields[i]))
    graphic1.add_x_serie(xtitle,values=x,labels=x,rotation=rotation,precision=precision)
    for i in range(len(y)):
        graphic1.add_y_serie(ytitles[i],values=y[i],units=units,rotation=rotation,precision=precision)
    filename=Plot_Graphic(graphic1,resume.get('user'),name,agregation,series_to_plot=series_to_plot)
    
    if include_history:
        logger.debug(f"{this()}: Check for history availability")

        history = Get_Resume_History(
                    db,
                    resume.get('user'),
                    resume.get('customer'),
                    resume.get('platform'),
                    resume.get('currency'),
                    resume.get('status'),
                    start=None,
                    end=None,

                    periods=['previous_month','current_month'],
                    agregation=agregation,
                    include_rows=True,
                    logger=logger
                    )

        for resume in history:
            key = resume['start'].strftime("%b %y")
            xh.append(key) 
            for r in resume['rows']:
                serie = getattr(r,xfield)
                value = getattr(r,yfields[0])
                #print(f"serie={serie} value={value}")
                if serie not in series.keys():
                    index = int(len(series)/2)
                    series.update({serie:index,index:serie})
                    yh.append([])
                yh[series[serie]].append(value)   

        width = 1/len(xh)/len(yh)
        left = width*len(yh)/2
        
        graphic2     = None
        graphic2     = Graphic(name)
        graphic2.add_x_serie('Month',values=xh,labels=xh,precision=0)
        logger.debug(f"len y series ={len(yh)} {series}")
        series_to_plot=[]
        for i in range(len(yh)):
            logger.debug(f"adding serie '{series.get(i)}' values {len(yh[i])} ={yh[i]}")
            graphic2.add_y_serie(series.get(i),values=yh[i],units=units)
            series_to_plot.append(i)
        history_filename=Plot_Graphic(graphic2,resume.get('user'),f"{name}_history",agregation,series_to_plot=series_to_plot)
    
    return filename,history_filename

@main.route('/statistics/resumes', methods=['GET'])
@login_required
#@permission_required(Permission.CUSTOMER)
def statistics_Resumes():
    logger.info(f'{this()}: IN')
    
    collectordata = get_collectordata()
        
    config = configparser.ConfigParser(interpolation=ExtendedInterpolation())
    if current_app.config.get('COLLECTOR_CONFIG_FILE'):
        config.read( current_app.config.get('COLLECTOR_CONFIG_FILE') )        
 
    date        = request.args.get('date',       'today')
    user        = request.args.get('user',       config.getint('Statistics','user',fallback=1))
    customer    = request.args.get('customer',   config.getint('Statistics','customer',fallback=3))
    status      = request.args.get('status',     config.getint('Statistics','status',fallback=1))
    currency    = request.args.get('currency',   config.get   ('Statistics','currency',fallback='UF'))
    platform    = request.args.get('platform',   config.getint('Statistics','platform',fallback=2))
    periods     = request.args.get('periods',    PERIOD_RANGES[STAT_PERIOD_TODAY]).split(',')
    agregations = request.args.get('agregations',AGREGATION_TYPE)

    if date.lower() == 'today':
        date=datetime.datetime.now()
    else:
        date=datetime.datetime.strptime(date,"%Y-%m-%d")

    # Will get all meaningfull periods upon request argument or default
    periods_data = Get_Periods(today=date,logger=logger)

    # periods array will include requested periods only
    for name in periods:
        if name not in periods_data.keys():
            try:
                periods.append(PERIOD_RANGES[int(name)])
            except:
                continue
    # will remove any invalid period name
    removals = True
    while removals:
        removals = False
        for name in periods:
            if name not in periods_data.keys():
                periods.remove(name)
                removals=True

    # will create appropiate Agregations array upon request
    agregations = str(agregations).split(',')
    for i in range(len(agregations)):
        agregations[i]=int(agregations[i])

    resumes=[]
    # For each required period will prepare data and graphics
    filename = None
    history_filename = None
    for name in periods:
        start       = periods_data[name][0]
        end         = periods_data[name][1]
        # Get Resume (it may include mix of period names Ex. 'current_month_so_far'+'today')
        resume      = Get_Resume(db,user,customer,platform,None,currency,status,start,end,name,agregations,logger=logger)

        for row in resume.get('rows'):
            # Will process all resume's rows upon agregation Type
            # Sets Up graphic objects for actual resume and historic comparison
            for agregation in agregations:
                
                filename = None
                history_filename = None

                if   agregation == AGREGATION_TYPE:
                    x='Typ_Code:Type'
                    y='CR_ST_at_Cur:Bill'
                    
                    filename,history_filename=Gen_Resume_Graphics(
                            x,y,resume,agregation,
                            include_history=True,
                            logger=logger
                            )
                elif agregation == AGREGATION_CC:
                    x='CC_Id:CC'
                    y='CR_ST_at_Cur:Bill'
                    
                    filename,history_filename=Gen_Resume_Graphics(
                            x,y,resume,agregation,
                            include_history=True,
                            rotation=15,
                            precision=0,
                            logger=logger
                            )
                elif agregation == AGREGATION_CUSTOMER:
                    x='Cus_Id:Customer'
                    y='CR_ST_at_Cur:Bill'
                    filename,history_filename=Gen_Resume_Graphics(
                            x,y,resume,agregation,
                            include_history=True,
                            precision=0,
                            logger=logger
                            )

        resumes.append({'name':name,'resume':resume,'figure':filename,'history':history_filename})

    #return render_template("report_statistics.html",resume=resume,collectordata=collectordata)
    return render_template("report_statistics.html",resumes=resumes)

@main.route('/api/statistics/resumes', methods=['GET'])
@login_required
#@permission_required(Permission.CUSTOMER)
def API_statistics_Resumes():
    logger.info(f'{this()}: IN')
   
    config = configparser.ConfigParser(interpolation=ExtendedInterpolation())
    if current_app.config.get('COLLECTOR_CONFIG_FILE'):
        config.read( current_app.config.get('COLLECTOR_CONFIG_FILE') )        
 
    date        = request.args.get('date',       'today')
    user        = request.args.get('user',       config.getint('Statistics','user',fallback=1))
    customer    = request.args.get('customer',   config.getint('Statistics','customer',fallback=3))
    status      = request.args.get('status',     config.getint('Statistics','status',fallback=1))
    currency    = request.args.get('currency',   config.get   ('Statistics','currency',fallback='UF'))
    platform    = request.args.get('platform',   config.getint('Statistics','platform',fallback=2))
    periods     = request.args.get('periods',    PERIOD_RANGES[STAT_PERIOD_TODAY]).split(',')
    agregations = request.args.get('agregations',AGREGATION_TYPE)
    table       = request.args.get('table',      False)

    table = True if str(table).upper() in ['1','TRUE'] else False

    if date.lower() == 'today':
        date=datetime.datetime.now()
    else:
        date=datetime.datetime.strptime(date,"%Y-%m-%d")

    # Will get all meaningfull periods upon request argument or default
    periods_data = Get_Periods(today=date,logger=logger)

    for name in periods:
        if name not in periods_data.keys():
            try:
                periods.append(PERIOD_RANGES[int(name)])
            except:
                continue
    removals = True
    while removals:
        removals = False
        for name in periods:
            if name not in periods_data.keys():
                periods.remove(name)
                removals=True

    agregations = str(agregations).split(',')
    for i in range(len(agregations)):
        agregations[i]=int(agregations[i])

    resumes=[]
    
    d={
        'user':user,
        'customer':customer,
        'status':status,
        'currency':currency,
        'platform':platform,
        'date':date.strftime("%Y-%m-%d"),
        'available_periods':[key for key in periods_data.keys()],
        'requested':periods,
        'agregations':agregations,
        'periods':[],
        'table':table
    }
    i=0
    for name in periods:
        start       = periods_data[name][0]
        end         = periods_data[name][1]
        resumes.append({'name':name,'agregations':Get_Resume(db,user,customer,platform,None,currency,status,start,end,name,agregations,logger=logger)})
        for key in resumes[i]['agregations'].keys():
            if key == 'rows':
                for j in range(len(resumes[i]['agregations']['rows'])):
                    resumes[i]['agregations']['rows'][j]=resumes[i]['agregations']['rows'][j].get_json_dict()
            else:
                if type(resumes[i]['agregations'][key]) == datetime.datetime:
                    resumes[i]['agregations'][key] = resumes[i]['agregations'][key].strftime("%Y-%m-%d")
        if table:
            resumes[i]['agregations'].update(rows_to_table(resumes[i]['agregations']['rows']))
        d['periods'].append({'name':name,'resumes':resumes})
        i+=1
    return json.dumps(d)

@main.route('/api/statistics/resumes/update', methods=['GET'])
@login_required
#@permission_required(Permission.CUSTOMER)
def API_statistics_Resumes_Update():
    logger.info(f'{this()}: IN')
   
    config = configparser.ConfigParser(interpolation=ExtendedInterpolation())
    if current_app.config.get('COLLECTOR_CONFIG_FILE'):
        config.read( current_app.config.get('COLLECTOR_CONFIG_FILE') )        
 
    period       = request.args.get('period',       None)
    user         = request.args.get('user',         config.getint('Statistics','user'       ,fallback=1))
    customer     = request.args.get('customer',     config.getint('Statistics','customer'   ,fallback=3))
    platform     = request.args.get('platform',     config.getint('Statistics','platform'   ,fallback=2))
    cost_center  = request.args.get('cost_center',  config.get   ('Statistics','cost_center',fallback=None))
    status       = request.args.get('status',       config.getint('Statistics','status'     ,fallback=1))
    currency     = request.args.get('currency',     config.get   ('Statistics','currency'   ,fallback='UF'))
    periods      = request.args.get('periods',      PERIOD_RANGES[STAT_PERIOD_CURRENT_MONTH]).split(',')
    agregations  = request.args.get('agregations',  AGREGATION_TYPE)
    table        = request.args.get('table',        False)
    include_rows = request.args.get('include_rows', False)
    force_update = request.args.get('force_update', False)
    callback     = config.get('Statistics','callback',fallback=None)   

    if str(include_rows).upper() in ['1','T','TRUE','V','VERDADERO']:
        include_rows = True     
    if str(force_update).upper() in ['1','T','TRUE','V','VERDADERO']:
        force_update = True     

    logger.debug(f"{this()}: callback = {callback}")

    if callback is not None:
        if  callback == 'default':
            callback=display_advance
        else:
            callback=globals().get(callback)
    logger.debug(f"{this()}: callback = {callback}")

    logger.debug(f"{this()}: period = {period}")
    if period is None:
        date = datetime.datetime.now()
    else:
        try:
            date = datetime.datetime.strptime(period,"%Y%m")
        except:
            date = None
    logger.debug(f"{this()}: date = {date}")

    resume={}
    if type(date) == datetime.datetime:
        start,end = Get_Period(date,PERIOD_MONTH)
        logger.info(f"{this()}: will Get Resume {user}-{customer}-{platform}-{status}-{currency}-{start}-{end}")
        name = 'previous_month'
        ci_id=None
        cc_id=None
        resume = Get_Resume(db,user,customer,platform,cost_center,currency,status,start,end,name,agregations,include_rows=include_rows,logger=logger)            
        logger.debug(f"{this()}: resume = {resume}")
        rows =  resume.get('rows',0)
        if (type(rows) == int and rows==0) or (type(rows)==list and len(rows)==0):
            logger.warning(f"{this()}: NO rows found in resume. Will update resume ... callback={callback}")

            count = Generate_Resume(
                        db,
                        customer,
                        start,
                        end,
                        status,
                        currency,
                        ci_id,
                        user,
                        cc_id,
                        fast=True,
                        force_update=force_update,
                        logger=logger,
                        callback=callback,
                        #step=0.01,
                        #**kwargs
                    )
            logger.debug(f"{this()}: count={count}")
            if count > 0:
                logger.info(f"{this()}: Generating consolidations ...")
                Consolidate_Resume(db,user,customer,platform,cost_center,currency,status,start,end,name,logger)
                logger.info(f"{this()}: Results follows ...")
                for agregation in AGREGATIONS:
                    resume = Get_Resume(db,user,customer,platform,cost_center,currency,status,start,end,name,agregation,include_rows=include_rows,logger=logger)
                    if resume:
                        rows=resume.get('rows',0)
                        if type(rows)==list:
                            rows=len(rows)
                        logger.info(
                            f"{this()}: resume: "
                            f"Q@R = {resume.get('Quantity_at_Rate'):,.0f} "
                            f"Q = {resume.get('Quantity'):,.0f} "
                            f"P = {resume.get('ST_at_Cur'):,.2f} {resume.get('currency')} "
                            f"rows = {rows:7,.0f} "
                            f"{resume.get('description','Unknown')}"
                        )            
        else:
            pass            
    else:
        logger.error(f"{this()}: Invalid period={period} ==> date={date}")
    logger.info(f"{this()}: will return resume now ...")
    for key in resume.keys():
        if key == 'rows'  and type(resume['rows'])==list:
            for j in range(len(resume['rows'])):
                resume['rows'][j]=resume['rows'][j].get_json_dict()
        else:
            if type(resume[key]) == datetime.datetime:
                resume[key] = resume[key].strftime("%Y-%m-%d")

    return json.dumps(resume)








    table = True if str(table).upper() in ['1','TRUE'] else False

    if date.lower() == 'today':
        date=datetime.datetime.now()
    else:
        date=datetime.datetime.strptime(date,"%Y-%m-%d")

    # Will get all meaningfull periods upon request argument or default
    periods_data = Get_Periods(today=date,logger=logger)

    for name in periods:
        if name not in periods_data.keys():
            try:
                periods.append(PERIOD_RANGES[int(name)])
            except:
                continue
    removals = True
    while removals:
        removals = False
        for name in periods:
            if name not in periods_data.keys():
                periods.remove(name)
                removals=True

    agregations = str(agregations).split(',')
    for i in range(len(agregations)):
        agregations[i]=int(agregations[i])

    resumes=[]
    
    d={
        'user':user,
        'customer':customer,
        'status':status,
        'currency':currency,
        'platform':platform,
        'date':date.strftime("%Y-%m-%d"),
        'available_periods':[key for key in periods_data.keys()],
        'requested':periods,
        'agregations':agregations,
        'periods':[],
        'table':table
    }
    i=0
    for name in periods:
        start       = periods_data[name][0]
        end         = periods_data[name][1]
        resumes.append({'name':name,'agregations':Get_Resume(db,user,customer,platform,None,currency,status,start,end,name,agregations,logger=logger)})
        for key in resumes[i]['agregations'].keys():
            if key == 'rows':
                for j in range(len(resumes[i]['agregations']['rows'])):
                    resumes[i]['agregations']['rows'][j]=resumes[i]['agregations']['rows'][j].get_json_dict()
            else:
                if type(resumes[i]['agregations'][key]) == datetime.datetime:
                    resumes[i]['agregations'][key] = resumes[i]['agregations'][key].strftime("%Y-%m-%d")
        if table:
            resumes[i]['agregations'].update(rows_to_table(resumes[i]['agregations']['rows']))
        d['periods'].append({'name':name,'resumes':resumes})
        i+=1
    return json.dumps(d)


def rows_to_table(rows):
    table = {'columns':[],'rows':[]}
    if len(rows):
        table['columns'] = [column for column in rows[0].keys()]
        for row in rows:
            table['rows'].append([value for value in row.values()])
    return table

# =============================================================================

