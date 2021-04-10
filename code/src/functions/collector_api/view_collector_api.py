# ======================================================================
# COLLECTOR API routes
# (c) Sertechno 2020
# GLVH @ 2020-10-09
# ======================================================================
# Version | Programmer | Description
# ------- | ---------- | -----------------------------------------------
# 1.0.0   | GLVH       | Initial version. Minimal implementation required
#         |            | Butler integration requirement.
# ======================================================================
import json
import inspect
import datetime

COLLECTOR_API_VERSION = '1.0.0'
COLLECTOR_API_OK      = 0
COLLECTOR_API_WARNING = 1
COLLECTOR_API_ERROR   = 2
COLLECTOR_API_UNKNOWN = 3
COLLECTOR_API_STATES  = ['OK','WARNING','ERROR','UNKNOWN']

@main.route('/api/heartbeat', methods=['GET'])
def api_heartbeat():
    logger.debug(f'{this()}: IN')
    kind='heartbeat'
    entities=[]
    name=current_app.config['NAME']
    authorized = api_check_authorization(request,current_app)
    if authorized:
        code    = API_OK
        message = 'Authorized request'
    else:
        code    = API_ERROR
        message = 'Unauthorized request'
    return get_api_response(
            code=code,
            message=message,
            kind=kind,
            entities=entities,
            name=name)

