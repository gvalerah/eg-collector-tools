#!/usr/bin/python
# coding: utf-8
# EG Collector - Grafana Datasource
#
# 0.0.1 2022-03-20 GLVH Initial version
#
# GLVH Gerardo L Valera gvalera@emtecgroup.net

# Application imports
import  os
import  sys
import  argparse
import  logging
import  pandas as pd         # NOT USED
import  datetime
from    configparser    import ConfigParser,ExtendedInterpolation
from    sre_constants   import CATEGORY_UNI_DIGIT
from    flask           import Flask, request, jsonify, json, abort
from    flask_cors      import CORS, cross_origin

from    emtec                           import *
from    emtec.collector.db.orm          import *
from    emtec.collector.db.orm_model    import *

# Main Global definitions
app = Flask(__name__)
# Required for Grafana cross_origin
cors = CORS(app)
app.config['CORS_HEADERS'] = "Content-Type"
methods = ('GET','POST')

# Datasource constants/defaults
NAME    = "EG Collector - Grafana Datasource"
MAYOR   = 0
MINOR   = 0
PATCH   = 1
BUILD   = 1
HOST    = '0.0.0.0'
PORT    = 8050
DETAIL  = False
DEBUG   = False
logger  = None

# Application Global Context Setup here

# Operational data buffers
metric_finders= {}
metric_readers = {}
annotation_readers = {}
panel_readers = {}
nodes_mapping = {'customer': [],
                 'cost_center': [],
                 'cu_type':[],
                 'state':[],
                 'currency':[]
                 }

# support functions
def get_args():
    parser = argparse.ArgumentParser(description=f'{NAME} v {MAYOR}.{MINOR}.{PATCH} build {BUILD}')
    parser.add_argument('-V', '--version', action='version', version='%(prog)s v' + f'{MAYOR}.{MINOR}.{PATCH}')
    parser.add_argument('-v', '--verbose', action='count', required=False, default=0,
                        help="Increase verbosity.")
    parser.add_argument('-H', '--host', required=False, default='0.0.0.0',help='Listener host defaults to 0.0.0.0')
    parser.add_argument('-P', '--port', required=False,default=8050,help='Listener port defaults to 8050')
    parser.add_argument('-c', '--config', required=False,default='collector.ini',help='Configuration file name (collector.ini)')

    parser.add_argument('--rdbms',      required=False,default='mysql', help='RDBMS')
    parser.add_argument('--dialect',    required=False,default='pymysql', help='RDBMS dialect')
    parser.add_argument('--dbhost',     required=False,default='localhost', help='DB Host')
    parser.add_argument('--dbport',     required=False,default=3306, help='DB Listener port')
    parser.add_argument('--user',       required=False,default=None, help='DB username')
    parser.add_argument('--password',   required=False,default=None, help='DB password')
    parser.add_argument('--schema',     required=False,default=None, help='DB schema')

    return parser.parse_args()

def add_reader(name, reader):
    metric_readers[name] = reader

def add_finder(name, finder):
    metric_finders[name] = finder

def add_annotation_reader(name, reader):
    annotation_readers[name] = reader

def add_panel_reader(name, reader):
    panel_readers[name] = reader

def dataframe_to_response(target, df, freq=None):
    response = []

    if df.empty:
        return response

    if freq is not None:
        orig_tz = df.index.tz
        df = df.tz_convert('UTC').resample(rule=freq, label='right', closed='right', how='mean').tz_convert(orig_tz)

    if isinstance(df, pd.Series):
        response.append(_series_to_response(df, target))
    elif isinstance(df, pd.DataFrame):
        for col in df:
            response.append(_series_to_response(df[col], target))
    else:
        abort(404, Exception('Received object is not a dataframe or series.'))

    return response

def dataframe_to_json_table(target, df):
    response = []

    if df.empty:
        return response

    if isinstance(df, pd.DataFrame):
        response.append({'type': 'table',
                         'columns': df.columns.map(lambda col: {"text": col}).tolist(),
                         'rows': df.where(pd.notnull(df), None).values.tolist()})
    else:
        abort(404, Exception('Received object is not a dataframe.'))

    return response

def annotations_to_response(target, df):
    response = []

    # Single series with DatetimeIndex and values as text
    if isinstance(df, pd.Series):
        for timestamp, value in df.iteritems():
            response.append({
                "annotation": target, # The original annotation sent from Grafana.
                "time": timestamp.value // 10 ** 6, # Time since UNIX Epoch in milliseconds. (required)
                "title": value, # The title for the annotation tooltip. (required)
                #"tags": tags, # Tags for the annotation. (optional)
                #"text": text # Text for the annotation. (optional)
            })
    # Dataframe with annotation text/tags for each entry
    elif isinstance(df, pd.DataFrame):
        for timestamp, row in df.iterrows():
            annotation = {
                "annotation": target,  # The original annotation sent from Grafana.
                "time": timestamp.value // 10 ** 6,  # Time since UNIX Epoch in milliseconds. (required)
                "title": row.get('title', ''),  # The title for the annotation tooltip. (required)
            }

            if 'text' in row:
                annotation['text'] = str(row.get('text'))
            if 'tags' in row:
                annotation['tags'] = str(row.get('tags'))

            response.append(annotation)
    else:
        abort(404, Exception('Received object is not a dataframe or series.'))

    return response

def _series_to_annotations(df, target):
    if df.empty:
        return {'target': '%s' % (target),
                'datapoints': []}

    sorted_df = df.dropna().sort_index()
    timestamps = (sorted_df.index.astype(pd.np.int64) // 10 ** 6).values.tolist()
    values = sorted_df.values.tolist()

    return {'target': '%s' % (df.name),
            'datapoints': zip(values, timestamps)}

def _series_to_response(df, target):
    if df.empty:
        return {'target': '%s' % (target),
                'datapoints': []}

    sorted_df = df.dropna().sort_index()

    try:
        timestamps = (sorted_df.index.astype(pd.np.int64) // 10 ** 6).values.tolist() # New pandas version
    except:
        timestamps = (sorted_df.index.astype(pd.np.int64) // 10 ** 6).tolist()

    values = sorted_df.values.tolist()

    return {'target': '%s' % (df.name),
            'datapoints': zip(values, timestamps)}

def _rows_to_table(rows, target):
    ''' Expects a list of rows containing value,datetime pairs 
        and/or other fields (sorted by datetime ascending)
    '''
    if rows is None or len(rows) == 0:
        return {'type': 'table',
                'columns': [],
                'rows': []}
    else:
        column_names=[]
        for field in rows[0].keys():
            column_names.append(field)
        datarows = []
        for row in rows:
            data=[]
            for i in range(len(column_names)):
                value=row[i]
                if type(value) == datetime.datetime:
                    value = int(value.timestamp()*1000)
                data.append(value)
            datarows.append   (data)

    return {'type': 'table',
            'columns': column_names,
            'rows': datarows}

def _rows_to_response(rows, target):
    ''' Expects a list of rows containing value,datetime pairs
        sorted by datetime ascending
    '''
    if rows is None or len(rows) == 0:
        return {'target': '%s' % (target),
                'datapoints': []}

    datapoints = []
    for row in rows:
        datapoints.append   ((float(row[0]),int(row[1].timestamp()*1000)))

    return {'target': '%s' % (target),
            'datapoints': datapoints}

def log_request(request):
    logger.debug (f"log_request: ---------------------------------")
    logger.debug (f"request         : {request}")
    logger.debug (f"request.method  : {request.method}")
    logger.debug (f"request.args    : {request.args}")
    logger.debug (f"request.form    : {request.args}")
    logger.debug (f"request.data    : {request.data}")
    logger.debug (f"request.headers :\n{request.headers}\n")
    logger.debug (f"request.get_json: {request.get_json()}\n")
    logger.debug (f"log_request: ---------------------------------")
    
# reader functions
def get_usage(target,ts_range,**kwargs):
    # suffix need to be defined upon end-start pair
    logger.debug(f"{this()}: target = {target} ts_range = {ts_range}")
    finder,metric_query = target['target'].split(':',1)
    customer,cost_center,cu_type,state,currency = metric_query.split(',',4)
    start = ts_range['$gt']
    end   = ts_range['$lte']
    suffix=f"{customer}_{start.strftime('%Y%m')}"
    logger.debug(f"{this()}: start = {start} end   = {end} suffix={suffix}")
    Charge_Items.set_shard(suffix)
    logger.debug(f"{this()}: CIT table = {Charge_Items.__tablename__}")

    # Typ code need to be argument in target !!!!!
    query=session.query(
            func.sum(Charge_Items.CIT_Quantity).label('QUANTITY'
            ),Charge_Items.CIT_DateTime.label('TIME')
        )
    if target['type'] == 'table':
        query=query.add_columns(func.count().label('COUNT'))
        query=query.add_columns(func.avg(Charge_Items.CIT_Quantity).label('AVERAGE'))

    query = query.join(Charge_Units,Charge_Units.CU_Id==Charge_Items.CU_Id
                ).join(Configuration_Items,Configuration_Items.CI_Id==Charge_Units.CI_Id
                )
    if len(customer):
        query = query.filter(Configuration_Items.Cus_Id==int(customer))
    if len(cost_center):
        # esta logica puede cambiarse usando funcion "is_below"
        cost_centers = cost_center.split(';')
        for i in range(len(cost_centers)):
            cost_centers[i] = int(cost_centers[i])
        logger.debug(f"{this()}: cost_centers={cost_centers}")
        query = query.filter(Configuration_Items.CC_Id.in_(cost_centers))
    if len(cu_type):
        query = query.filter(Charge_Units.Typ_Code==cu_type)
    query = query.group_by(Charge_Units.Typ_Code,Charge_Items.CIT_DateTime)
    query = query.order_by(Charge_Units.Typ_Code,Charge_Items.CIT_DateTime)
    rows = query.all()
    if rows:
        logger.debug(f"{this()}: rows        = {len(rows)}")
        logger.debug(f"{this()}: rows[0]     = {rows[0]} {type(rows[0])} {rows[0].keys()}")
    else:
        logger.debug(f"{this()}: No rows found. rows = {rows}")
    if target['type']=='timeserie':
        response = _rows_to_response(rows,target['target'])
    else:
        response = _rows_to_table(rows,target['target'])

    logger.debug(f"{this()}: response.target = {response.get('target')}")
    return response

# Datasource views

@app.route('/')
@cross_origin()
def entry_point():
    return f'{NAME} v {MAYOR}.{MINOR}.{PATCH} build {BUILD}\n'

@app.route('/search',methods=methods)
@cross_origin()
def search():
    # POST method required
    # Content-Type: application/json required
    # Gets request arguments as dictionary
    log_request(request)
    req = request.get_json()

    if req is not None:
        try:
            # Gets 'target' attribute or defaults to '*'
            target = req.get('target', '*')
            # gets finder if any or defaults to target
            if ':' in target:
                finder, target = target.split(':', 1)
            else:
                finder = target

            if not target or finder not in metric_finders:
                metrics = []
                if target == '*':
                    metrics += list(metric_finders.keys()) + list(metric_readers.keys())
                else:
                    metrics.append(target)

                return jsonify(metrics)
            else:
                return jsonify(list(metric_finders[finder](target)))
        except Exception as e:
            emtec_handle_general_exception(e,logger=logger)
            abort(404,f"EXCEPTION: {str(e)}")
    logger.error(f"ERROR: arguments error.req={req} type={str(type(req))}")
    abort(404,Exception(f"ERROR: arguments error.req={req} type={str(type(req))}"))

@app.route('/query',methods=methods)
@cross_origin(max_age=600)
def query():    
    log_request(request)
    # gets request data, method POST required
    # data required:
    # { range:{from:timestamp, to:timestamp}
    #   intervalMs:<int>                        optional miliseconds
    #   targets:[]                              targets as target:type pairs
    #                                               type = timeserie (default) or table)
    # }
    req = request.get_json()

    results = []

    ts_range = {'$gt':  datetime.datetime.strptime(req['range']['from'],'%Y-%m-%dT%H:%M:%S.%fZ'),
                '$lte': datetime.datetime.strptime(req['range']['to']  ,'%Y-%m-%dT%H:%M:%S.%fZ')}

    logger.debug(f"{this()}: ts_range={ts_range}")
    if 'intervalMs' in req:
        freq = str(req.get('intervalMs')) + 'ms'
    else:
        freq = None

    logger.debug(f"{this()}: targets={req['targets']} {type(req['targets'])}")
    for target in req['targets']:
        logger.debug(f"target={target} {type(target)}")
        if ':' not in target.get('target', ''):
            abort(404, Exception('Target must be of type: <finder>:<metric_query>, got instead: ' + target['target']))

        req_type = target.get('type', 'timeserie')

        finder, metric_query = target['target'].split(':', 1)
        logger.debug(f"{this()}: will use reader '{finder}' with target={target} and ts_range={ts_range}")
        query_results = metric_readers[finder](target, ts_range)
        # Check if valid pandas dataframe (legacy)
        if hasattr(query_results,'empty'):
            if req_type == 'table':
                results.extend(dataframe_to_json_table(target, query_results))
            else:
                results.extend(dataframe_to_response(target, query_results, freq=freq))
        else:
            logger.debug(f"{this()}: query_results = {type(query_results)}")
            if type(query_results) == dict:
                logger.debug(f"query_results.target = {query_results.get('target')}")
                logger.debug(f"query_results.datapoints = {len(query_results.get('datapoints',[]))}")
            results.append(query_results)
    return jsonify(results)

@app.route('/annotations',methods=methods)
@cross_origin(max_age=600)
def annotations():
    return f'{NAME} v {MAYOR}.{MINOR}.{PATCH} build {BUILD} annotations\n'

@app.route('/tag-keys',methods=methods)
@cross_origin()
def tag_keys():
    array = [
        {"type":"string","text":"customer"},
        {"type":"string","text":"cost_center"},
        {"type":"string","text":"cu_type"},
        {"type":"string","text":"state"},
        {"type":"string","text":"currency"},
    ]
    return jsonify(array)

@app.route('/tag-values',methods=methods)
@cross_origin()
def tag_values():
    log_request(request)
    data = request.get_json()
    if data:
        key = data.get('key')
        array = []
        if key == 'customer':
            rows = session.query(Customers).filter(Customers.Cus_Id>1).all()
            for row in rows:
                array.append({'text':row.Cus_Name})
        elif key == 'cost_center':
            rows = session.query(Cost_Centers).filter(Cost_Centers.CC_Id>1).all()
            for row in rows:
                array.append({'text':f"{row.CC_Code}:{row.CC_Description}"})
        elif key == 'cu_type':
            rows = session.query(CU_Types).all()
            for row in rows:
                array.append({'text':f"{row.Typ_Code}:{row.Typ_Description}"})
        elif key == 'state':
            rows = session.query(CIT_Statuses).all()
            for row in rows:
                array.append({'text':f"{row.CIT_Status}:{row.Value}"})
        elif key == 'currency':
            rows = session.query(Currencies).all()
            for row in rows:
                array.append({'text':f"{row.Cur_Code}:{row.Cur_Name}"})
        else:
            array = []
    else:
        array=[]
    return jsonify(array)

@app.route('/panels',methods=methods)
@cross_origin()
def panels():
    return f'{NAME} v {MAYOR}.{MINOR}.{PATCH} build {BUILD} panels\n'

def update_nodes_mapping():
    nodes_mapping = {'customer': [],
                    'cost_center': [],
                    'cu_type':[],
                    'state':[],
                    'currency':[],
                    }
    rows = session.query(Customers).filter(Customers.Cus_Id>1).all()
    for row in rows:
        nodes_mapping['customer'].append(row.Cus_Name)
    rows = session.query(Cost_Centers).filter(Cost_Centers.CC_Id>1).all()
    for row in rows:
        nodes_mapping['customer'].append(f"{row.CC_Code}:{row.CC_Description}")
    rows = session.query(CU_Types).all()
    for row in rows:
        nodes_mapping['cu_type'].append(f"{row.Typ_Code}:{row.Typ_Description}")
    rows = session.query(CIT_Statuses).all()
    for row in rows:
        nodes_mapping['state'].append(f"{row.CIT_Status}:{row.Value}")
    rows = session.query(Currencies).all()
    for row in rows:
        nodes_mapping['currency'].append(f"{row.Cur_Code}:{row.Cur_Name}")

args = get_args()

# Setup application logging system

logger = logging.getLogger(__name__)
logger.setLevel(logging.WARNING)
#formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
formatter = logging.Formatter('%(levelname)8s - %(message)s')
ch = logging.StreamHandler()
ch.setFormatter(formatter)
if args.verbose > 0: 
    DETAIL=True
    logger.setLevel(logging.INFO)
    ch.setLevel(logging.INFO)
if args.verbose > 1: 
    DEBUG=True
    logger.setLevel(logging.DEBUG)
    ch.setLevel(logging.DEBUG)
logger.addHandler(ch)

# Load needed data from configuration file is reqired
# overrides defaults and command line arguments
if os.path.exists(args.config):
    config = ConfigParser(interpolation=ExtendedInterpolation())
    logger.info(f"reading configuration from '{args.config}'")
    config.read(args.config)
    if config.get('DB','rdbms'):    args.rdbms   =config.get('DB','rdbms')
    if config.get('DB','dialect'):  args.dialect =config.get('DB','dialect')
    if config.get('DB','host'):     args.dbhost  =config.get('DB','host')
    if config.get('DB','port'):     args.dbport  =config.get('DB','port')
    if config.get('DB','user'):     args.user    =config.get('DB','user')
    if config.get('DB','password'): args.password=config.get('DB','password')
    if config.get('DB','schema'):   args.schema  =config.get('DB','schema')

logger.debug(f"{this()}: args = {args}")

# Global DB Connection

try:
    connection_string=f"{args.rdbms}+{args.dialect}://{args.user}:{args.password}@{args.dbhost}:{args.dbport}/{args.schema}"
    logger.debug(f"connection_string= {connection_string}")
    db=create_engine(connection_string)
    if db is None:
        logger.error(f"ERROR: NO DB connection")
        sys.exit(1)
    logger.debug(f"db               = {db}")
    db.connect()
    Session=sessionmaker(bind=db)
    if Session is None:
        logger.debug(f"ERROR: NO DB Session binded to engine: {db}")
        sys.exit(1)

    logger.debug(f"Session          = {Session}")
    session=Session()
    if session is None:
        logger.error(f"ERROR: NO DB session conection to engine: {db}")
        sys.exit(1)
    logger.debug(f"session          = {session}")
except Exception as e:
    emtec_handle_general_exception(e,logger=logger)
    sys.exit(1)

if __name__ == '__main__':
    # load datasource readers
    add_reader('monthly_usage',get_usage)
    
    # load nodes mappings
    update_nodes_mapping()
    add_finder('get_nodes', lambda q: nodes_mapping.get(q, nodes_mapping.keys()) if q != '*' else sum(nodes_mapping.values(), []))

    app.run(host=HOST,port=PORT,debug=DEBUG)

"""
Reference links:

https://github.com/grafana/grafana/tree/main/docs/sources/datasources
https://grafana.com/grafana/plugins/grafana-simple-json-datasource/
https://community.grafana.com/t/grafana-simplejson-dashboard/5627/3?u=mefraimsson

Example backend implementations

https://github.com/bergquist/fake-simple-json-datasource
https://github.com/smcquay/jsonds
https://github.com/ContextLogic/eventmaster
https://gist.github.com/linar-jether/95ff412f9d19fdf5e51293eb0c09b850 (Python/pandas backend) ****************
"""

"""
Call formats

Search:

curl -X POST http://localhost:8050/search -H "Content-Type: application/json" -d '{"target":"aaa"}'
[
  "aaa"
]

curl -X POST http://localhost:8050/search -H "Content-Type: application/json" -d '{"target":"*"}'
[
  "monthly_usage"
]

Query:


 curl -X POST http://localhost:8050/query -H "Content-Type: application/json" -d '
 {
    "targets":
        [
            {
                "target":"monthly_usage:10",
                "type":"timeserie"
            }
        ],
    "range":
        {
            "from":1647804466072000,
            "to":164784466073000
        }
}
'



"""

"""
Queries

Agrupamiento por tipo de CIT en un mes, sin filtro por Tipo

mysql> select Typ_Code,CIT_DateTime,sum(CIT_Quantity),count(*) from Charge_Items_202201 join Charge_Units using (CU_Id) group by Typ_Code,CIT_DateTime;

Agrupamiento por tipo de CIT en un mes, con filtro por Tipo

mysql> select Typ_Code,CIT_DateTime,sum(CIT_Quantity),count(*) from Charge_Items_202201 join Charge_Units using (CU_Id) where Typ_Code="DSK" group by Typ_Code,CIT_DateTime;

select Typ_Code,CIT_DateTime,sum(CIT_Quantity),count(*) 
from Charge_Items_202202 
join Charge_Units using (CU_Id) 
where Typ_Code="DSK" 
group by Typ_Code,CIT_DateTime 
order by Typ_Code,CIT_DateTime;

"""

"""
query request data:
request.data    : b'
{
    "app":"dashboard",
    "requestId":"Q101",
    "timezone":"browser",
    "panelId":2,
    "dashboardId":null,
    "range":{
        "from":"2022-03-21T12:01:33.482Z",
        "to":"2022-03-21T18:01:33.482Z",
        "raw":{
            "from":"now-6h",
            "to":"now"
            }
        },
    "timeInfo":"",
    "interval":"15s",
    "intervalMs":15000,
    "targets":[
        {"target":"","refId":"A","type":"timeserie"}
        ],
    "maxDataPoints":1377,
    "scopedVars":{
        "__interval":{
            "text":"15s",
            "value":"15s"
            },
        "__interval_ms":{
            "text":"15000",
            "value":15000
            }
        },
    "startTime":1647885693484,
    "rangeRaw":{
        "from":"now-6h",
        "to":"now"
        },
    "adhocFilters":[]
}'
"""