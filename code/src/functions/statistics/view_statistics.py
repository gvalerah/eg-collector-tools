# =============================================================================
# Statistics basic reporter
# (c) Sertechno 2022
# GLVH @ 2022-04-12
# =============================================================================

# view required imports
import os
import json
import datetime
from flask import request
from pprint import pprint,pformat
from emtec.collector.statistics import *
# view required functions

@main.route('/statistics/resumes', methods=['GET'])
@login_required
#@permission_required(Permission.CUSTOMER)
def statistics_Resumes():
    logger.warning('Enter: statistics_Resumes()'%())
    print         ('Enter: statistics_Resumes()'%())
    """
    collectordata=get_collectordata()
        
    config_ini = configparser.ConfigParser(interpolation=ExtendedInterpolation())
    if current_app.config.get('COLLECTOR_CONFIG_FILE'):
        config_ini.read( current_app.config.get('COLLECTOR_CONFIG_FILE') )        
        limit_user_cost_centers = config_ini.getboolean('Interface','limit_user_cost_centers',fallback=False)
    else:
        limit_user_cost_centers = False
    """ 
    # Will get all meaningfull periods
    periods_data = Get_Periods(logger=logger)

    periods = request.args.get('periods','today').split(',')

    print(f"periods_data = {periods_data}")
    print(f"periods      = {periods}")

    user        = 1 # Forced Global system Adm Statistical User
    customer    = 3
    status      = 1
    currency    = 'UF'
    platform    = 1
    agregations = request.args.get('agregations',AGREGATION_CU_TYPE)
    print(f"agregations={agregations}")
    agregations = str(agregations).split(',')
    print(f"agregations={agregations}")
    for i in range(len(agregations)):
        agregations[i]=int(agregations[i])
    print(f"agregations={agregations}")

    resumes=[]
    for name in periods:
        start       = periods_data[name][0]
        end         = periods_data[name][1]
        resumes.append({'name':name,'resume':Get_Resume(db,user,customer,start,end,status,currency,platform,agregations,logger)})


    #return render_template("report_statistics.html",resume=resume,collectordata=collectordata)
    return render_template("report_statistics.html",resumes=resumes)

# =============================================================================

