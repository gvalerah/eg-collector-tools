#!/usr/bin/python
# coding: utf-8
# EG Collector - Grafana Datasource
#
# 0.0.1 2022-03-20 GLVH Initial version
#
# GLVH Gerardo L Valera gvalera@emtecgroup.net

# Application imports
from sre_constants import CATEGORY_UNI_DIGIT
from flask import Flask, request, jsonify, json, abort
from flask_cors import CORS, cross_origin

import pandas as pd
import datetime

from emtec import *
from emtec.collector.db.orm import *
from emtec.collector.db.orm_model import *


app = Flask(__name__)
cors=CORS(app)
app.config['CORS_HEADERS'] = "Content-Type"
methods = ('GET','POST')

# Datasource constants
NAME="EG Colector - Datasource"
MAYOR=0
MINOR=0
PATCH=1
BUILD=1
HOST='0.0.0.0'
PORT=8050
DEBUG=True

# Operational data buffers
metric_finders= {}
metric_readers = {}
annotation_readers = {}
panel_readers = {}
nodes_mapping = {'customer': ['EMTEC', 'LUMEN'],
                 'cost_center': ['30000000', '30000001', ''],
                 'cu_type':['CPU','RAM','DSK'],
                 'currency':['UF','CLP','USD']
                 }

# support functions
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
        sorted by datetime ascending
    '''
    if rows is None or len(rows) == 0:
        return {'type': 'table',
                'columns': [],
                'rows': []}
    else:
        column_names=[]
        print(f"type of rows   = {type(rows)}")
        print(f"dir rows       = {dir(rows)}")
        print(f"type of rows 0 = {type(rows[0])}")
        print(f"dir rows 0 = {dir(rows[0])}")
        print(f"dir rows 0 = {rows[0]._asdict()}")
        print(f"rows 0 _fields= {rows[0]._fields}")
        print(f"rows 0 keys  = {rows[0].keys()}")
        for field in rows[0].keys():
            column_names.append(field)
        datarows = []
        for row in rows:
            datarows.append   (row)

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
    print (f"log_request: ---------------------------------")
    print (f"request         : {request}")
    #rint (f"request: {dir(request)}")
    print (f"request.method  : {request.method}")
    print (f"request.args    : {request.args}")
    print (f"request.form    : {request.args}")
    print (f"request.data    : {request.data}")
    print (f"request.headers :\n{request.headers}\n")
    print (f"request.get_json: {request.get_json()}\n")
    print (f"log_request: ---------------------------------")
    

# reader functions
def get_usage(target,ts_range,**kwargs):
    # suffix need to be defined upon end-start pair
    print(f"{this()}: target = {target} ts_range = {ts_range}")
    finder,metric_query = target['target'].split(':',1)
    customer,cost_center,cu_type,state,currency = metric_query.split(',',4)
    start = ts_range['$gt']
    end   = ts_range['$lte']
    suffix=f"{customer}_{start.strftime('%Y%m')}"
    print(f"{this()}: start = {start} end   = {end} suffix={suffix}")
    Charge_Items.set_shard(suffix)
    print(f"{this()}: CIT table = {Charge_Items.__tablename__}")

    # Typ code need to be argument in target !!!!!
    query=session.query(
            func.sum(Charge_Items.CIT_Quantity
            ),Charge_Items.CIT_DateTime
            ).join(Charge_Units,Charge_Units.CU_Id==Charge_Items.CU_Id
            ).join(Configuration_Items,Configuration_Items.CI_Id==Charge_Units.CI_Id
            )
    if len(customer):
        query = query.filter(Configuration_Items.Cus_Id==int(customer))
    if len(cost_center):
        # esta logica puede cambiarse usando funcion "is_below"
        cost_centers = cost_center.split(';')
        for i in range(len(cost_centers)):
            cost_centers[i] = int(cost_centers[i])
        print(f"{this()}: cost_centers={cost_centers}")
        query = query.filter(Configuration_Items.CC_Id.in_(cost_centers))
    if len(cu_type):
        query = query.filter(Charge_Units.Typ_Code==cu_type)
    query = query.group_by(Charge_Units.Typ_Code,Charge_Items.CIT_DateTime)
    query = query.order_by(Charge_Units.Typ_Code,Charge_Items.CIT_DateTime)
    #print(f"query={query}")
    rows = query.all()
    if rows:
        print(f"{this()}: rows = {len(rows)}")
    else:
        print(f"{this()}: No rows found. rows = {rows}")
    if target['type']=='timeserie':
        response = _rows_to_response(rows,target['target'])
    else:
        response = _rows_to_table(rows,target['target'])

    print(f"{this()}: response.target = {response.get('target')}")
    #print(f"{this()}: response.datapoints = {len(response.get('datapoints'))}")
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
            print(f"EXCEPTION: {str(e)}")
            abort(404,f"EXCEPTION: {str(e)}")
    print(f"ERROR: arguments error.req={req} type={str(type(req))}")
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

    print(f"{this()}: ts_range={ts_range}")
    if 'intervalMs' in req:
        freq = str(req.get('intervalMs')) + 'ms'
    else:
        freq = None

    print(f"{this()}: targets={req['targets']} {type(req['targets'])}")
    for target in req['targets']:
        print(f"target={target} {type(target)}")
        if ':' not in target.get('target', ''):
            abort(404, Exception('Target must be of type: <finder>:<metric_query>, got instead: ' + target['target']))

        req_type = target.get('type', 'timeserie')

        finder, metric_query = target['target'].split(':', 1)
        print(f"{this()}: will use reader '{finder}' with target={target} and ts_range={ts_range}")
        query_results = metric_readers[finder](target, ts_range)
        # Check if valid pandas dataframe (legacy)
        if hasattr(query_results,'empty'):
            if req_type == 'table':
                results.extend(dataframe_to_json_table(target, query_results))
            else:
                results.extend(dataframe_to_response(target, query_results, freq=freq))
        else:
            print(f"{this()}: query_results = {type(query_results)}")
            if type(query_results) == dict:
                print(f"query_results.target = {query_results.get('target')}")
                print(f"query_results.datapoints = {len(query_results.get('datapoints',[]))}")
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
        if key == 'customer':
            array = [{'text':'EMTEC'},{'text':'LUMEN'}]
        elif key == 'cost_center':
            array = [{'text':'30000000'}]
        elif key == 'cu_type':
            array = [{'text':'CPU'},{'text':'RAM'},{'text':'DSK'}]
        elif key == 'state':
            array = [{'text':'Created'},{'text':'Rejected'},{'text':'Paid'}]
        elif key == 'currency':
            array = [{'text':'UF'},{'text':'USD'},{'text':'CLP'}]
        else:
            array = []
    else:
        array=[]
    return jsonify(array)

@app.route('/panels',methods=methods)
@cross_origin()
def panels():
    return f'{NAME} v {MAYOR}.{MINOR}.{PATCH} build {BUILD} panels\n'


# Application Global Context Setup here
rdbms='mysql'
dialect='pymysql'
host='localhost'
port=3306
user='root'
password='36MMySQLr00t1.,'
schema='collector'

connection_string=f"{rdbms}+{dialect}://{user}:{password}@{host}:{port}/{schema}"
print("connection_string=",connection_string)
db=create_engine(connection_string)
print("db               =",db)
Session=sessionmaker(bind=db)
print("Session          =",Session)
session=Session()
print("session          =",session)
print("just loaded class:",Charge_Items)    
#print_class(CU_Types,session=session)


if __name__ == '__main__':
    # load datasource readers
    add_reader('monthly_usage',get_usage)
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