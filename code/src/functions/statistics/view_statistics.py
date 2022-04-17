# =============================================================================
# Statistics basic reporter
# (c) Sertechno 2022
# GLVH @ 2022-04-12
# =============================================================================

# view required imports
import os
import json
import datetime
from xml.dom.expatbuilder import FragmentBuilderNS
from flask import request
from pprint import pprint,pformat
from emtec.collector.statistics import *
# view required functions

@main.route('/statistics/resumes', methods=['GET'])
@login_required
#@permission_required(Permission.CUSTOMER)
def statistics_Resumes():
    logger.info(f'{this()}: IN')
    
    collectordata=get_collectordata()
        
    config = configparser.ConfigParser(interpolation=ExtendedInterpolation())
    if current_app.config.get('COLLECTOR_CONFIG_FILE'):
        config.read( current_app.config.get('COLLECTOR_CONFIG_FILE') )        
 
    date        = request.args.get('date',       'today')
    user        = request.args.get('user',       config.getint('Statistics','user',fallback=1))
    customer    = request.args.get('customer',   config.getint('Statistics','customer',fallback=3))
    status      = request.args.get('status',     config.getint('Statistics','status',fallback=1))
    currency    = request.args.get('currency',   config.getint('Statistics','currency',fallback='UF'))
    platform    = request.args.get('platform',   config.getint('Statistics','platform',fallback=2))
    periods     = request.args.get('periods',    PERIOD_RANGES[PERIOD_TODAY]).split(',')
    agregations = request.args.get('agregations',AGREGATION_TYPE)

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
    for name in periods:
        start       = periods_data[name][0]
        end         = periods_data[name][1]
        resume      = Get_Resume(db,user,customer,start,end,status,currency,platform,name,agregations,logger)
        graphic     = None
        graphic     = Graphic(name)
        for agregation in agregations:
            filename = None
            if agregation == AGREGATION_TYPE:
                x=[]
                y1=[]
                y2=[]
                for row in resume.get('rows'):
                    x.append(row.Typ_Code)
                    y1.append(row.CR_Quantity_at_Rate)
                    y2.append(row.CR_ST_at_Cur)
                graphic.add_x_serie('Type',values=x,labels=x,precision=0)
                graphic.add_y_serie('Quantity',values=y1)
                graphic.add_y_serie('Bill',values=y2,units=currency)
                print(f"graphic={graphic}")
                filename=Plot_Graphic(graphic,user,name,agregation,series_to_plot=[1])
            elif agregation == AGREGATION_CC:
                x=[]
                y1=[]
                y2=[]
                for row in resume.get('rows'):
                    x.append(row.CC_Id)
                    y1.append(row.CR_Quantity_at_Rate)
                    y2.append(row.CR_ST_at_Cur)
                graphic.add_x_serie('CC',values=x,labels=x,rotation=15,precision=0)
                graphic.add_y_serie('Quantity',values=y1)
                graphic.add_y_serie('Bill',values=y2,units=currency)
                print(f"graphic={graphic}")
                filename=Plot_Graphic(graphic,user,name,agregation,series_to_plot=[1])

        resumes.append({'name':name,'resume':resume,'graphic':graphic,'figure':filename})


    #return render_template("report_statistics.html",resume=resume,collectordata=collectordata)
    return render_template("report_statistics.html",resumes=resumes)


PLOT_COLORS=['SkyBlue','IndianRed']
def Plot_Graphic(graphic,user,name,agregation,series_to_plot=[0],logger=logging.getLogger()):
    import numpy as np
    import matplotlib.pyplot as plt
    # matplot fill
    filename=None
    try:
        ind = np.arange(len(graphic.X[0].values)) # The x locations for groups X axe
        width = 0.35 # bar width

        fig,ax = plt.subplots() # figura maestra y subplots por eje
        #rects1 = ax.bar(ind - width/2, Quantity, width,
        #                color='SkyBlue', label='Quantity')
        rects=[]

        for yaxe in series_to_plot:
            rects.append(   ax.bar(
                                    ind , 
                                    graphic.Y[yaxe].values, 
                                    width,
                                    color=PLOT_COLORS[len(rects)], 
                                    label=graphic.Y[yaxe].name
                            )
                        )
            ax.set_ylabel(graphic.Y[yaxe].units)

        # Add some text for labels, title and custom x-axis tick labels, etc.
        ax.set_title(f'Values for {name} and {AGREGATIONS[agregation]}')
        ax.set_xticks(ind)
        ax.set_xticklabels(graphic.X[0].labels,rotation=graphic.X[0].rotation)
        ax.legend()
        for i in range(len(rects)):
            autolabel(ax,rects[i], "center")
        filename = url_for('static',filename=f'tmp/{user}-{name}-{agregation}.png')
        plt.savefig(f"{current_app.root_path}{filename}")
    except Exception as e:
        emtec_handle_general_exception(e,logger=logger)
    return filename



# graphic support functions
def autolabel(ax,rects, xpos='center'):
    """
    Attach a text label above each bar in *rects*, displaying its height.

    *xpos* indicates which side to place the text w.r.t. the center of
    the bar. It can be one of the following {'center', 'right', 'left'}.
    """

    xpos = xpos.lower()  # normalize the case of the parameter
    ha = {'center': 'center', 'right': 'left', 'left': 'right'}
    offset = {'center': 0.5, 'right': 0.57, 'left': 0.43}  # x_txt = x + w*off

    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()*offset[xpos], 1.01*height,
                '{}'.format(height), ha=ha[xpos], va='bottom')



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
    currency    = request.args.get('currency',   config.getint('Statistics','currency',fallback='UF'))
    platform    = request.args.get('platform',   config.getint('Statistics','platform',fallback=2))
    periods     = request.args.get('periods',    PERIOD_RANGES[PERIOD_TODAY]).split(',')
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
        resumes.append({'name':name,'agregations':Get_Resume(db,user,customer,start,end,status,currency,platform,name,agregations,logger)})
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

