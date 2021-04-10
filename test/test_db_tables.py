from pprint import pprint,pformat
from emtec.collector.db.orm import *
import warnings
warnings.filterwarnings("ignore")

db=Collector_ORM_DB('mysql','pymysql','localhost',3306,'root','Zj1245//$$','collector')
print("db=",db)
print("db.connection_string=",db.connection_string)

# Actual DB session connection setup need to be forced
# due to test code is out of flask app context

engine=create_engine(db.connection_string)
Session=sessionmaker(bind=engine)
db.session=Session()

print("db.session=",db.session)

tablas=db.Get_Table_Names()
pprint(tablas)
print()
if tablas is not None:
    print("%s tablas detectadas en DB."%len(tablas))
print()

for mes in range(12):
    print(db.Create_Sharding_Table('Charge_Items','2020%02d'%(mes+1)))


tablasfragmentadas=db.Get_Sharding_Tables('Charge_Items')
if tablasfragmentadas is not None:
    print("%s tablas fragmentadas detectadas en DB."%len(tablasfragmentadas))
print()
