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
        resumes.append({'name':name,'resume':Get_Resume(db,user,customer,start,end,status,currency,platform,agregations,logger)})

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
        resumes.append({'name':name,'agregations':Get_Resume(db,user,customer,start,end,status,currency,platform,agregations,logger)})
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

