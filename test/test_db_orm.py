from emtec.collector.db.orm import *

db=Collector_ORM_DB('mysql','pymysql','localhost',3306,'root','Zj1245//$$','collector')
print("db=",db)
print("db.connection_string=",db.connection_string)

# Actual DB session connection setup need to be forced
# due to test code is out of flask app context

engine=create_engine(db.connection_string)
Session=sessionmaker(bind=engine)
db.session=Session()

print("db.session=",db.session)
CIs=db.session.query(Configuration_Items).all()
total=len(CIs)
undefined=0
recomended=0
for CI in CIs:
	if CI.CC_Id == 1:
		undefined = undefined + 1
		result=db.Set_CI_CC_From_Name(CI.CI_Id,True)
		if result is not None:
			CC=db.session.query(Cost_Centers).filter(Cost_Centers.CC_Id==result).one_or_none()
			print("CI=",CI,"recomended CC=",CC)
			recomended = recomended + 1
print()
print("total",total)
print("undefined",undefined)
print("recomended",recomended)

