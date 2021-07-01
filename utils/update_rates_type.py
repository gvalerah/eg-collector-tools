
# Import system modules
import sys
# Import logging functions
import logging

# Import time formatter fuctions
from time           import strftime

# Import create_engine function
from sqlalchemy         import create_engine
from sqlalchemy         import text
from sqlalchemy.orm     import sessionmaker
#import sqlalchemy.orm.exc 
from sqlalchemy.exc     import IntegrityError

# Import App Modules

from common.log import Log
#from models.rates   import Rates


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

from sqlalchemy             import Column, String, Integer, Numeric, Date, Time, Boolean
from sqlalchemy             import ForeignKey

class Rates(Base):
    __tablename__ = 'Rates'
    engine        = None

    Rat_Id     = Column( Integer, primary_key=True, autoincrement=True )
    Typ_Code   = Column( String(10), ForeignKey('CU_Types.Typ_Code') )
    Cus_Id     = Column( Integer, ForeignKey('Customers.Cus_Id') )
    Pla_Id     = Column( Integer, ForeignKey('Platforms.Pla_Id') )
    CC_Id      = Column( Integer, ForeignKey('Cost_Centers.CC_Id') )
    CU_Id      = Column( Integer, ForeignKey('Charge_Units.CU_Id') )
    Rat_Price  = Column( Numeric(20,12) )
    Cur_Code   = Column( String(3), ForeignKey('Currencies.Cur_Code') )
    MU_Code    = Column( String(3), ForeignKey('Measure_Units.MU_Code') )
    Rat_Period = Column( Integer, ForeignKey('Rat_Periods.Rat_Period') )
    Rat_Type   = Column( Integer )

    def __init__(self, Rat_Id, Typ_Code, Cus_Id, Pla_Id, CC_Id, CU_Id, Rat_Price, Cur_Code, MU_Code, Rat_Period, Rat_Type):
        self.set( Rat_Id, Typ_Code, Cus_Id, Pla_Id, CC_Id, CU_Id, Rat_Price, Cur_Code, MU_Code, Rat_Period, Rat_Type)

    def __repr__(self):
        return "<Rates( Rat_Id='%s', Typ_Code='%s', Cus_Id='%s', Pla_Id='%s', CC_Id='%s', CU_Id='%s', Rat_Price='%s', Cur_Code='%s', MU_Code='%s', Rat_Period='%s', Rat_Type='%s')>" % \
                ( self.Rat_Id, self.Typ_Code, self.Cus_Id, self.Pla_Id, self.CC_Id, self.CU_Id, self.Rat_Price, self.Cur_Code, self.MU_Code, self.Rat_Period, self.Rat_Type)


RAT_TYPE        =0x01
RAT_PLATFORM    =0x02
RAT_CUSTOMER    =0x04
RAT_CC          =0x08
RAT_CU          =0x10

Rat_Types = [   RAT_TYPE,
                RAT_TYPE|RAT_PLATFORM,
                RAT_TYPE|RAT_PLATFORM|RAT_CUSTOMER,
                RAT_TYPE|RAT_PLATFORM|RAT_CUSTOMER|RAT_CC,
                RAT_TYPE|RAT_PLATFORM|RAT_CUSTOMER|RAT_CC|RAT_CU
                ]


# Setup DB connection parameters
driver = "mysql+pymysql"
user =  "root"
password = "Zj1245//$$"
host = "127.0.0.1"
port = 3306
schema = "collector"
app_folder = "/home/gvalera/CODE/Python/collector"
log_folder = "/home/gvalera/CODE/Python/collector/log"
log_format = "col_%Y-%m-%d.log"
log_format_debug = "col_%Y-%m-%d-%H.log"
charset="utf8mb4"
    
logger = Log('update_rates_type',log_folder,log_format,log_format_debug,logging.DEBUG).logger

# 'application' code

logger.info("Start Execution")

# Connect to DB
engine_string=str("%s://%s:%s@%s:%s/%s?charset=%s"%(driver,user,password,host,port,schema,charset))

#engine_string=str("mysql+pymysql://root:Zj1245//$$@localhost:3306/collector")

engine = create_engine(engine_string)

# Get Schema relationships
logger.info("Getting Schema Relationships ...")


def Get_Rat_Type(Rate):
    rate_type = 0
    if Rate.Typ_Code != 'NUL'   :   rate_type |= RAT_TYPE    
    if Rate.Pla_Id != 1         :   rate_type |= RAT_PLATFORM
    if Rate.Cus_Id != 1         :   rate_type |= RAT_CUSTOMER
    if Rate.CC_Id  != 1         :   rate_type |= RAT_CC
    if Rate.CU_Id  != 1         :   rate_type |= CU
    return rate_type

Session = sessionmaker(bind=engine)
session = Session()

for t in Rat_Types:
    print("Rat Type ",t)

rates=session.query(Rates).all()
for rat in rates:
    print(rat,Get_Rat_Type(rat))
    rat.Rat_Type=Get_Rat_Type(rat)
    session.add(rat)
    session.commit()

rates=session.query(Rates).all()
for rat in rates:
    print(rat,Get_Rat_Type(rat))



"""


new_fields=0
for t in range(len(TABLES)):
    table_name = TABLES[t][0]
    
    if table_name in (["Users","Roles","Charge_Resumes"]):
        print("OMITING TABLE '%s'"%table_name)
        continue
    
    logger.debug("Creating inserts for '%s'..."%(table_name))
    print("")
    print("Creating inserts for '%s'..."%(table_name))
    print("*******************************************")
    
    # Here needs to be replaced by parameter use, next test
    query = text("SHOW COLUMNS FROM collector."+table_name)
    COLUMNS = engine.execute(query).fetchall()
    
    order=1
    for c in range(len(COLUMNS)):
        field_name=COLUMNS[c][0]
        try:
            print("looking for '%s'.'%s'"%(table_name,field_name))
            Forms=session.query(Dev_Forms).filter(Dev_Forms.Table==table_name).filter(Dev_Forms.Field==field_name).all()
            if len(Forms)==1:
                F=Forms[0]
                #print("\t%s.%s FOUND !!!"%(table_name,field_name))
            else:
                print("\t**********************************************")
                print("\t%s.%s NOT FOUND in Dev_Forms!!!"%(table_name,field_name))
                print("\t**********************************************")
                F=Dev_Forms()
                F.Table   = table_name        
                F.Field   = field_name        
                F.Foreign_Key = None
                F.Referenced_Table = None
                F.Foreign_Field = None
                F.Length = None
                F.Validation = None
                F.Validation_Type= None
                F.Validation_String = None        
                F.Caption_String = field_name        
                F.Field_Order = order
                F.Field_Format = None
                F.Form_Editable = 1
                print("\t\tsession add %s.%s"%(table_name,field_name))
                session.add(F)
                new_fields+=1            
            # If Found Update data from actual DB Metadata
        except Exception as e:
            print("EXCEPTION:",e)
            # If not Found initalizes record Data
            F=Dev_Forms()
            F.Table   = table_name        
            F.Field   = field_name        
            F.Foreign_Key = None
            F.Referenced_Table = None
            F.Foreign_Field = None
            F.Length = None
            F.Validation = None
            F.Validation_Type= None
            F.Validation_String = None        
            F.Caption_String = field_name        
            F.Field_Order = order
            F.Field_Format = None
            F.Form_Editable = 1
            print("\t\ŧsession add %s.%s"%(table_name,field_name))
            session.add(F)
            new_fields+=1            
            
        # Allways updates main Metadata from DB
        F.Type          = COLUMNS[c][1]
        F.Null          = COLUMNS[c][2]
        F.Key           = COLUMNS[c][3]
        F.Default       = COLUMNS[c][4]
        F.Extra         = COLUMNS[c][5]
        F.Field_Order   = order
        order=order+1
        
        # Adjust PK Data
        if (F.Key == "PRI"):
                print ("\t\tPrimary Key: collector.%s.%s"%(table_name,F.Field))
                F.Validation = True 
                F.Validation_Type = 'PK' 
                F.Validation_String = 'Required()' 
                
        # Allways resets FK Data in order to re-create if needed
        F.Foreign_Key = None
        F.Referenced_Table = None
        F.Foreign_Field = None
        # Updates Relations Data        
        for r in range(len(RELATIONS)):
            rel=RELATIONS[r]
            if ((rel[1] == table_name) and (rel[2] == F.Field)):
                F.Foreign_Key = rel[2]
                F.Referenced_Table = rel[4]
                F.Foreign_Field = rel[2]
                print ("\tRelationship Found(%02d %s:%s): collector.%s.%s -> collector.%s.%s" % \
                        (r,table_name,F.Field,rel[1],rel[2],F.Referenced_Table,F.Foreign_Field)) 
                break
        
        try:        
            #print("\t\t\tsession add (UPDATE) %s.%s"%(table_name,field_name))
            session.add(F)
            session.commit()
        except IntegrityError as e:
            logger.warning("\tDuplicate Key Ignored : (%s/%s)"%(Table,F.Field))


session. close()

print("*********************************************")
print("%d new fields found"%new_fields)
print("*********************************************")

logger.info("End Execution")
"""
