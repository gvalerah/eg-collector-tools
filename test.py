from datetime import datetime
import simplejson as json
from emtec import *
from emtec.collector.db.flask_models import *
from pprint import pprint

i=1
f=3.1415
s='Hello word'
d=datetime.now()
l=[i,f,s]
x=charge_unit()
dd={'k1':'value1','k2':'value2'}

di={'ki':i,'kf':f,'ks':s,'kd':d,'kl':l,'kdd':dd}

l2=[l,dd,x,x,x]

d2={'kdd':dd,'kdi':di}

pprint(             json.dumps(serialize_object(i)))
pprint(json.loads(  json.dumps(serialize_object(i))))
print()
pprint(             json.dumps(serialize_object(f)))
pprint(json.loads(  json.dumps(serialize_object(f))))
print()
pprint(             json.dumps(serialize_object(s)))
pprint(json.loads(  json.dumps(serialize_object(s))))
print()
pprint(             json.dumps(serialize_object(d)))
pprint(json.loads(  json.dumps(serialize_object(d))))
print()
pprint(             json.dumps(serialize_object(l)))
pprint(json.loads(  json.dumps(serialize_object(l))))
print()
pprint(             json.dumps(serialize_object(dd)))
pprint(json.loads(  json.dumps(serialize_object(dd))))
print()
pprint(             json.dumps(serialize_object(di)))
pprint(json.loads(  json.dumps(serialize_object(di))))
print()
pprint(             json.dumps(serialize_object(x)))
pprint(json.loads(  json.dumps(serialize_object(x))))
print()
pprint(             json.dumps(serialize_object(l2)))
pprint(json.loads(  json.dumps(serialize_object(l2))))
print()
pprint(             json.dumps(serialize_object(d2)))
pprint(json.loads(  json.dumps(serialize_object(d2))))
print()
