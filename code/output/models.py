# GV =============================================================================
# GV Models File
# GV Static Header File. 
# GV source: models_py_header.py
# GV GLVH 2019-08-16
# GV GLVH 2020-01-30 JSON Serializing code added
# GV =============================================================================
from app                    import db
from app                    import login_manager

from datetime               import datetime

from sqlalchemy             import Column, String, Integer, Numeric, Date, Time, Boolean, DateTime
from sqlalchemy             import ForeignKey

from flask_sqlalchemy       import SQLAlchemy
from copy                   import copy, deepcopy

# GV Required form Authorization subsystem
from werkzeug.security      import generate_password_hash, check_password_hash
from itsdangerous           import TimedJSONWebSignatureSerializer as Serializer
from flask                  import current_app
from flask_login            import UserMixin, AnonymousUserMixin

# GV JSON Serializing enabling code
from sqlalchemy.inspection import inspect


class Serializer(object):

    def serialize(self):
        return {c: getattr(self, c) for c in inspect(self).attrs.keys()}

    @staticmethod
    def serialize_list(l):
        return [m.serialize() for m in l]

# GV 20200224 GV force import of the whole emtec db library ---------------
from emtec.collector.db.orm_model       import *
from emtec.collector.db.flask_models    import *
# GV ----------------------------------------------------------------------
# GV =============================================================================
# GV Models File
# GV Authorization subsystem. 
# GV Static File. 
# GV GLVH 2018-12-17
# GV =============================================================================

class Permission:
    CUSTOMER            = 0x001
    VIEW                = 0x002
    DELETE              = 0x004
    MODIFY              = 0x008
    REPORT              = 0x010
    EXPORT              = 0x020
    RESERVED040         = 0x040
    ADMINISTER          = 0x080
    AUDIT               = 0x100
    RESERVED200         = 0x200
    RESERVED400         = 0x400
    GOD                 = 0x8

class AnonymousUser(AnonymousUserMixin):
    def can(self, permissions):
        return False

    def is_administrator(self):
        return False

login_manager.anonymous_user = AnonymousUser


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2022-03-07 18:58:14
# =============================================================================

# gen_model_flask.py:117 => /home/gvalera/GIT/EG-Suite-Tools/Collector/code/auto/models/flask_charge_items.py
class charge_item(db.Model,Serializer):
    __tablename__ = 'Charge_Items'

    def check_shard(suffix=None,engine=None):
       if engine is not None:
           try:
               if not engine.dialect.has_table(engine, __class__.__tablename__):
                   print(f'131 Table {__class__.__tablename__} does not exist')
                   metadata=MetaData()
                   metadata.bind=engine
                   __class__.__table__.metadata=metadata
                   __class__.__table__.create(checkfirst=True)
                   if not engine.dialect.has_table(engine, __class__.__tablename__):
                       print('137 Table %s does not exist. creation error?'% __class__.__tablename__)
                   else:
                       print('139 Table %s exist !!!'% __class__.__tablename__)
               else:
                   pass # GV print('141 Table %s exist !!!'% __class__.__tablename__)
           except Exception as e:
              print(f'143 exception: {str(e)}')
           return
    def set_shard(suffix=None,engine=None):
       if suffix is not None:
           name='Charge_Items_{suffix}'.format(suffix=suffix)
           __class__.__tablename__  = name
           __class__.__table__.name = name
       __class__.check_shard(suffix,engine)
       return __class__.__tablename__

    CU_Id         = db.Column( db.Integer, db.ForeignKey('Charge_Units.CU_Id'), primary_key=True, default=0 )
    CIT_Date      = db.Column( db.Date )
    CIT_Time      = db.Column( db.Time )
    CIT_Quantity  = db.Column( db.Numeric(20,12), default=0.000000000000 )
    CIT_Status    = db.Column( db.Integer, db.ForeignKey('CIT_Statuses.CIT_Status'), default=0 )
    CIT_Is_Active = db.Column( db.Boolean, default=0 )
    CIT_DateTime  = db.Column( db.DateTime, primary_key=True )


    # looking for include file: /home/gvalera/GIT/EG-Suite-Tools/Collector/code/src/include/models/flask_charge_items_properties.py
    # file: /home/gvalera/GIT/EG-Suite-Tools/Collector/code/src/include/models/flask_charge_items_properties.py not found
    def __init__(self, CU_Id=0, CIT_Date=None, CIT_Time=None, CIT_Quantity=0.000000000000, CIT_Status=0, CIT_Is_Active=0, CIT_DateTime=None):
        self.CU_Id         = CU_Id
        self.CIT_Date      = CIT_Date
        self.CIT_Time      = CIT_Time
        self.CIT_Quantity  = CIT_Quantity
        self.CIT_Status    = CIT_Status
        self.CIT_Is_Active = CIT_Is_Active
        self.CIT_DateTime  = CIT_DateTime

    def __repr__(self):
        return "<Charge_Items( CU_Id='%s', CIT_Date='%s', CIT_Time='%s', CIT_Quantity='%s', CIT_Status='%s', CIT_Is_Active='%s', CIT_DateTime='%s')>" % \
                ( self.CU_Id, self.CIT_Date, self.CIT_Time, self.CIT_Quantity, self.CIT_Status, self.CIT_Is_Active, self.CIT_DateTime)

# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2022-03-07 18:58:14
# =============================================================================

# gen_model_flask.py:717 => /home/gvalera/GIT/EG-Suite-Tools/Collector/code/auto/models/flask_charge_items.py
def get_charge_item(table_name_suffix):
  # gen_model_flask.py:725 =>/home/gvalera/GIT/EG-Suite-Tools/Collector/code/auto/models/flask_charge_items.py
  class charge_item_Class(db.Model,Serializer):
    __tablename__ = 'Charge_Items_%s'%(table_name_suffix)

    def set_shard(suffix=None,engine=None):
        if suffix is not None:
           name='Charge_Items_{suffix}'.format(suffix=suffix)
           __class__.__tablename__  = name
           __class__.__table__.name = name
           __class__.check_shard(suffix,engine)
        return __class__.__tablename__

    CU_Id         = db.Column( db.Integer, db.ForeignKey('Charge_Units.CU_Id'), primary_key=True, default=0 )
    CIT_Date      = db.Column( db.Date )
    CIT_Time      = db.Column( db.Time )
    CIT_Quantity  = db.Column( db.Numeric(20,12), default=0.000000000000 )
    CIT_Status    = db.Column( db.Integer, db.ForeignKey('CIT_Statuses.CIT_Status'), default=0 )
    CIT_Is_Active = db.Column( db.Boolean, default=0 )
    CIT_DateTime  = db.Column( db.DateTime, primary_key=True )


    def __init__(self, CU_Id=0, CIT_Date=None, CIT_Time=None, CIT_Quantity=0.000000000000, CIT_Status=0, CIT_Is_Active=0, CIT_DateTime=None):
        self.CU_Id         = CU_Id
        self.CIT_Date      = CIT_Date
        self.CIT_Time      = CIT_Time
        self.CIT_Quantity  = CIT_Quantity
        self.CIT_Status    = CIT_Status
        self.CIT_Is_Active = CIT_Is_Active
        self.CIT_DateTime  = CIT_DateTime

    def __repr__(self):
        return "<Charge_Items( CU_Id='%s', CIT_Date='%s', CIT_Time='%s', CIT_Quantity='%s', CIT_Status='%s', CIT_Is_Active='%s', CIT_DateTime='%s')>" % \
                ( self.CU_Id, self.CIT_Date, self.CIT_Time, self.CIT_Quantity, self.CIT_Status, self.CIT_Is_Active, self.CIT_DateTime)

  charge_item_Class.__name__ = 'charge_item_%s'%(table_name_suffix)
  return charge_item_Class
  # gen_model_flask.py 849 => /home/gvalera/GIT/EG-Suite-Tools/Collector/code/auto/models/flask_charge_items.py
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2020-02-24 15:33:48
# =============================================================================

def get_charge_item(table_name_sufix):
  class charge_item_Class(db.Model,Serializer):
    __tablename__ = 'Charge_Items_%s'%(table_name_sufix)
    CU_Id         = db.Column( db.Integer, db.ForeignKey('Charge_Units.CU_Id'), primary_key=True, default=0 )
    CIT_Date      = db.Column( db.Date )
    CIT_Time      = db.Column( db.Time )
    CIT_Quantity  = db.Column( db.Numeric(20,6), default=0.000000 )
    CIT_Status    = db.Column( db.Integer, db.ForeignKey('CIT_Statuses.CIT_Status'), default=0 )
    CIT_Is_Active = db.Column( db.Boolean, default=0 )
    CIT_DateTime  = db.Column( db.DateTime, primary_key=True )


    def __init__(self, CU_Id=0, CIT_Date=None, CIT_Time=None, CIT_Quantity=0.000000, CIT_Status=0, CIT_Is_Active=0, CIT_DateTime=None):
        self.CU_Id         = CU_Id
        self.CIT_Date      = CIT_Date
        self.CIT_Time      = CIT_Time
        self.CIT_Quantity  = CIT_Quantity
        self.CIT_Status    = CIT_Status
        self.CIT_Is_Active = CIT_Is_Active
        self.CIT_DateTime  = CIT_DateTime

    def __repr__(self):
        return "<Charge_Items( CU_Id='%s', CIT_Date='%s', CIT_Time='%s', CIT_Quantity='%s', CIT_Status='%s', CIT_Is_Active='%s', CIT_DateTime='%s')>" % \
                ( self.CU_Id, self.CIT_Date, self.CIT_Time, self.CIT_Quantity, self.CIT_Status, self.CIT_Is_Active, self.CIT_DateTime)

  charge_item_Class.__name__ = 'charge_item_%s'%(table_name_sufix)
  return charge_item_Class
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2022-03-07 18:58:14
# =============================================================================

# gen_model_flask.py:117 => /home/gvalera/GIT/EG-Suite-Tools/Collector/code/auto/models/flask_charge_resumes.py
class charge_resume(db.Model,Serializer):
    __tablename__ = 'Charge_Resumes'

    def check_shard(suffix=None,engine=None):
       if engine is not None:
           try:
               if not engine.dialect.has_table(engine, __class__.__tablename__):
                   print(f'131 Table {__class__.__tablename__} does not exist')
                   metadata=MetaData()
                   metadata.bind=engine
                   __class__.__table__.metadata=metadata
                   __class__.__table__.create(checkfirst=True)
                   if not engine.dialect.has_table(engine, __class__.__tablename__):
                       print('137 Table %s does not exist. creation error?'% __class__.__tablename__)
                   else:
                       print('139 Table %s exist !!!'% __class__.__tablename__)
               else:
                   pass # GV print('141 Table %s exist !!!'% __class__.__tablename__)
           except Exception as e:
              print(f'143 exception: {str(e)}')
           return
    def set_shard(suffix=None,engine=None):
       if suffix is not None:
           name='Charge_Resumes_{suffix}'.format(suffix=suffix)
           __class__.__tablename__  = name
           __class__.__table__.name = name
       __class__.check_shard(suffix,engine)
       return __class__.__tablename__

    User_Id                = db.Column( db.Integer, primary_key=True )
    Cus_Id                 = db.Column( db.Integer, primary_key=True )
    CR_Date_From           = db.Column( db.Date, primary_key=True )
    CR_Date_To             = db.Column( db.Date, primary_key=True )
    CIT_Status             = db.Column( db.Integer, primary_key=True )
    Cur_Code               = db.Column( db.String(3), primary_key=True )
    CU_Id                  = db.Column( db.Integer, primary_key=True )
    CIT_Count              = db.Column( db.Integer, default=0 )
    CIT_Quantity           = db.Column( db.Numeric(20,12), default=0.000000000000 )
    CIT_Generation         = db.Column( db.Integer, default=1 )
    CI_CC_Id               = db.Column( db.Integer, default=0 )
    CU_Operation           = db.Column( db.String(10), default='NONE' )
    Typ_Code               = db.Column( db.String(10), default='NUL' )
    CC_Cur_Code            = db.Column( db.String(3), default='UF' )
    CI_Id                  = db.Column( db.Integer, default=1 )
    Rat_Id                 = db.Column( db.Integer, default=0 )
    Rat_Price              = db.Column( db.Numeric(20,12), default=0.000000000000 )
    Rat_MU_Code            = db.Column( db.String(3), default='UNT' )
    Rat_Cur_Code           = db.Column( db.String(3), default='UF' )
    Rat_Period             = db.Column( db.Integer, default=1 )
    Rat_Hourly             = db.Column( db.Numeric(20,12), default=0.000000000000 )
    Rat_Daily              = db.Column( db.Numeric(20,12), default=0.000000000000 )
    Rat_Monthly            = db.Column( db.Numeric(20,12), default=0.000000000000 )
    CR_Quantity            = db.Column( db.Numeric(20,12), default=0.000000000000 )
    CR_Quantity_at_Rate    = db.Column( db.Numeric(20,12), default=0.000000000000 )
    CC_XR                  = db.Column( db.Numeric(20,12), default=0.000000000000 )
    CR_Cur_XR              = db.Column( db.Numeric(20,12), default=0.000000000000 )
    CR_ST_at_Rate_Cur      = db.Column( db.Numeric(20,12), default=0.000000000000 )
    CR_ST_at_CC_Cur        = db.Column( db.Numeric(20,12), default=0.000000000000 )
    CR_ST_at_Cur           = db.Column( db.Numeric(20,12), default=0.000000000000 )
    Cus_Name               = db.Column( db.String(255) )
    CI_Name                = db.Column( db.String(255) )
    CU_Description         = db.Column( db.String(255) )
    CC_Description         = db.Column( db.String(255) )
    Rat_Period_Description = db.Column( db.String(10) )
    CC_Code                = db.Column( db.String(45) )
    Pla_Id                 = db.Column( db.Integer, default=0 )
    Pla_Name               = db.Column( db.String(255) )


    # looking for include file: /home/gvalera/GIT/EG-Suite-Tools/Collector/code/src/include/models/flask_charge_resumes_properties.py
    # file: /home/gvalera/GIT/EG-Suite-Tools/Collector/code/src/include/models/flask_charge_resumes_properties.py not found
    def __init__(self, User_Id=None, Cus_Id=None, CR_Date_From=None, CR_Date_To=None, CIT_Status=None, Cur_Code='None', CU_Id=None, CIT_Count=0, CIT_Quantity=0.000000000000, CIT_Generation=1, CI_CC_Id=0, CU_Operation='NONE', Typ_Code='NUL', CC_Cur_Code='UF', CI_Id=1, Rat_Id=0, Rat_Price=0.000000000000, Rat_MU_Code='UNT', Rat_Cur_Code='UF', Rat_Period=1, Rat_Hourly=0.000000000000, Rat_Daily=0.000000000000, Rat_Monthly=0.000000000000, CR_Quantity=0.000000000000, CR_Quantity_at_Rate=0.000000000000, CC_XR=0.000000000000, CR_Cur_XR=0.000000000000, CR_ST_at_Rate_Cur=0.000000000000, CR_ST_at_CC_Cur=0.000000000000, CR_ST_at_Cur=0.000000000000, Cus_Name='None', CI_Name='None', CU_Description='None', CC_Description='None', Rat_Period_Description='None', CC_Code='None', Pla_Id=0, Pla_Name='None'):
        self.User_Id                = User_Id
        self.Cus_Id                 = Cus_Id
        self.CR_Date_From           = CR_Date_From
        self.CR_Date_To             = CR_Date_To
        self.CIT_Status             = CIT_Status
        self.Cur_Code               = Cur_Code
        self.CU_Id                  = CU_Id
        self.CIT_Count              = CIT_Count
        self.CIT_Quantity           = CIT_Quantity
        self.CIT_Generation         = CIT_Generation
        self.CI_CC_Id               = CI_CC_Id
        self.CU_Operation           = CU_Operation
        self.Typ_Code               = Typ_Code
        self.CC_Cur_Code            = CC_Cur_Code
        self.CI_Id                  = CI_Id
        self.Rat_Id                 = Rat_Id
        self.Rat_Price              = Rat_Price
        self.Rat_MU_Code            = Rat_MU_Code
        self.Rat_Cur_Code           = Rat_Cur_Code
        self.Rat_Period             = Rat_Period
        self.Rat_Hourly             = Rat_Hourly
        self.Rat_Daily              = Rat_Daily
        self.Rat_Monthly            = Rat_Monthly
        self.CR_Quantity            = CR_Quantity
        self.CR_Quantity_at_Rate    = CR_Quantity_at_Rate
        self.CC_XR                  = CC_XR
        self.CR_Cur_XR              = CR_Cur_XR
        self.CR_ST_at_Rate_Cur      = CR_ST_at_Rate_Cur
        self.CR_ST_at_CC_Cur        = CR_ST_at_CC_Cur
        self.CR_ST_at_Cur           = CR_ST_at_Cur
        self.Cus_Name               = Cus_Name
        self.CI_Name                = CI_Name
        self.CU_Description         = CU_Description
        self.CC_Description         = CC_Description
        self.Rat_Period_Description = Rat_Period_Description
        self.CC_Code                = CC_Code
        self.Pla_Id                 = Pla_Id
        self.Pla_Name               = Pla_Name

    def __repr__(self):
        return "<Charge_Resumes( User_Id='%s', Cus_Id='%s', CR_Date_From='%s', CR_Date_To='%s', CIT_Status='%s', Cur_Code='%s', CU_Id='%s', CIT_Count='%s', CIT_Quantity='%s', CIT_Generation='%s', CI_CC_Id='%s', CU_Operation='%s', Typ_Code='%s', CC_Cur_Code='%s', CI_Id='%s', Rat_Id='%s', Rat_Price='%s', Rat_MU_Code='%s', Rat_Cur_Code='%s', Rat_Period='%s', Rat_Hourly='%s', Rat_Daily='%s', Rat_Monthly='%s', CR_Quantity='%s', CR_Quantity_at_Rate='%s', CC_XR='%s', CR_Cur_XR='%s', CR_ST_at_Rate_Cur='%s', CR_ST_at_CC_Cur='%s', CR_ST_at_Cur='%s', Cus_Name='%s', CI_Name='%s', CU_Description='%s', CC_Description='%s', Rat_Period_Description='%s', CC_Code='%s', Pla_Id='%s', Pla_Name='%s')>" % \
                ( self.User_Id, self.Cus_Id, self.CR_Date_From, self.CR_Date_To, self.CIT_Status, self.Cur_Code, self.CU_Id, self.CIT_Count, self.CIT_Quantity, self.CIT_Generation, self.CI_CC_Id, self.CU_Operation, self.Typ_Code, self.CC_Cur_Code, self.CI_Id, self.Rat_Id, self.Rat_Price, self.Rat_MU_Code, self.Rat_Cur_Code, self.Rat_Period, self.Rat_Hourly, self.Rat_Daily, self.Rat_Monthly, self.CR_Quantity, self.CR_Quantity_at_Rate, self.CC_XR, self.CR_Cur_XR, self.CR_ST_at_Rate_Cur, self.CR_ST_at_CC_Cur, self.CR_ST_at_Cur, self.Cus_Name, self.CI_Name, self.CU_Description, self.CC_Description, self.Rat_Period_Description, self.CC_Code, self.Pla_Id, self.Pla_Name)

# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2022-03-07 18:58:14
# =============================================================================

# gen_model_flask.py:117 => /home/gvalera/GIT/EG-Suite-Tools/Collector/code/auto/models/flask_charge_unit_egm.py
class charge_unit_egm(db.Model,Serializer):
    __tablename__ = 'Charge_Unit_EGM'

    def check_shard(suffix=None,engine=None):
       if engine is not None:
           try:
               if not engine.dialect.has_table(engine, __class__.__tablename__):
                   print(f'131 Table {__class__.__tablename__} does not exist')
                   metadata=MetaData()
                   metadata.bind=engine
                   __class__.__table__.metadata=metadata
                   __class__.__table__.create(checkfirst=True)
                   if not engine.dialect.has_table(engine, __class__.__tablename__):
                       print('137 Table %s does not exist. creation error?'% __class__.__tablename__)
                   else:
                       print('139 Table %s exist !!!'% __class__.__tablename__)
               else:
                   pass # GV print('141 Table %s exist !!!'% __class__.__tablename__)
           except Exception as e:
              print(f'143 exception: {str(e)}')
           return
    def set_shard(suffix=None,engine=None):
       if suffix is not None:
           name='Charge_Unit_EGM_{suffix}'.format(suffix=suffix)
           __class__.__tablename__  = name
           __class__.__table__.name = name
       __class__.check_shard(suffix,engine)
       return __class__.__tablename__

    CU_Id           = db.Column( db.Integer, db.ForeignKey('Charge_Units.CU_Id'), primary_key=True )
    Archive         = db.Column( db.Integer )
    Path            = db.Column( db.String(256) )
    Metric          = db.Column( db.String(256) )
    Host            = db.Column( db.String(45), default='localhost' )
    Port            = db.Column( db.Integer, default=22 )
    User            = db.Column( db.String(45) )
    Password        = db.Column( db.String(45) )
    Public_Key_File = db.Column( db.String(256) )
    Passphrase      = db.Column( db.String(256) )


    # looking for include file: /home/gvalera/GIT/EG-Suite-Tools/Collector/code/src/include/models/flask_charge_unit_egm_properties.py
    # file: /home/gvalera/GIT/EG-Suite-Tools/Collector/code/src/include/models/flask_charge_unit_egm_properties.py not found
    def __init__(self, CU_Id=None, Archive=None, Path='None', Metric='None', Host='localhost', Port=22, User='None', Password='None', Public_Key_File='None', Passphrase='None'):
        self.CU_Id           = CU_Id
        self.Archive         = Archive
        self.Path            = Path
        self.Metric          = Metric
        self.Host            = Host
        self.Port            = Port
        self.User            = User
        self.Password        = Password
        self.Public_Key_File = Public_Key_File
        self.Passphrase      = Passphrase

    def __repr__(self):
        return "<Charge_Unit_EGM( CU_Id='%s', Archive='%s', Path='%s', Metric='%s', Host='%s', Port='%s', User='%s', Password='%s', Public_Key_File='%s', Passphrase='%s')>" % \
                ( self.CU_Id, self.Archive, self.Path, self.Metric, self.Host, self.Port, self.User, self.Password, self.Public_Key_File, self.Passphrase)

# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2022-03-07 18:58:14
# =============================================================================

# gen_model_flask.py:117 => /home/gvalera/GIT/EG-Suite-Tools/Collector/code/auto/models/flask_charge_units.py
class charge_unit(db.Model,Serializer):
    __tablename__ = 'Charge_Units'

    def check_shard(suffix=None,engine=None):
       if engine is not None:
           try:
               if not engine.dialect.has_table(engine, __class__.__tablename__):
                   print(f'131 Table {__class__.__tablename__} does not exist')
                   metadata=MetaData()
                   metadata.bind=engine
                   __class__.__table__.metadata=metadata
                   __class__.__table__.create(checkfirst=True)
                   if not engine.dialect.has_table(engine, __class__.__tablename__):
                       print('137 Table %s does not exist. creation error?'% __class__.__tablename__)
                   else:
                       print('139 Table %s exist !!!'% __class__.__tablename__)
               else:
                   pass # GV print('141 Table %s exist !!!'% __class__.__tablename__)
           except Exception as e:
              print(f'143 exception: {str(e)}')
           return
    def set_shard(suffix=None,engine=None):
       if suffix is not None:
           name='Charge_Units_{suffix}'.format(suffix=suffix)
           __class__.__tablename__  = name
           __class__.__table__.name = name
       __class__.check_shard(suffix,engine)
       return __class__.__tablename__

    CU_Id                  = db.Column( db.Integer, primary_key=True, autoincrement=True )
    CI_Id                  = db.Column( db.Integer, db.ForeignKey('Configuration_Items.CI_Id') )
    CU_Description         = db.Column( db.String(255) )
    CU_UUID                = db.Column( db.String(45) )
    CU_Is_Billeable        = db.Column( db.Boolean, default=0 )
    CU_Is_Always_Billeable = db.Column( db.Boolean, default=0 )
    CU_Quantity            = db.Column( db.Numeric(20,12) )
    CU_Operation           = db.Column( db.String(10), db.ForeignKey('CU_Operations.CU_Operation') )
    Typ_Code               = db.Column( db.String(10), db.ForeignKey('CU_Types.Typ_Code') )
    CIT_Generation         = db.Column( db.Integer, db.ForeignKey('CIT_Generations.CIT_Generation') )
    Rat_Id                 = db.Column( db.Integer )
    CU_Reference_1         = db.Column( db.String(45) )
    CU_Reference_2         = db.Column( db.String(45) )
    CU_Reference_3         = db.Column( db.String(45) )

    # child_table=None gen_children=False
    # child_table=None gen_children=False

    # looking for include file: /home/gvalera/GIT/EG-Suite-Tools/Collector/code/src/include/models/flask_charge_units_properties.py
    # file: /home/gvalera/GIT/EG-Suite-Tools/Collector/code/src/include/models/flask_charge_units_properties.py not found
    def __init__(self, CU_Id=0, CI_Id=None, CU_Description='None', CU_UUID='None', CU_Is_Billeable=0, CU_Is_Always_Billeable=0, CU_Quantity=None, CU_Operation='None', Typ_Code='None', CIT_Generation=None, Rat_Id=None, CU_Reference_1='None', CU_Reference_2='None', CU_Reference_3='None'):
        self.CU_Id                  = CU_Id
        self.CI_Id                  = CI_Id
        self.CU_Description         = CU_Description
        self.CU_UUID                = CU_UUID
        self.CU_Is_Billeable        = CU_Is_Billeable
        self.CU_Is_Always_Billeable = CU_Is_Always_Billeable
        self.CU_Quantity            = CU_Quantity
        self.CU_Operation           = CU_Operation
        self.Typ_Code               = Typ_Code
        self.CIT_Generation         = CIT_Generation
        self.Rat_Id                 = Rat_Id
        self.CU_Reference_1         = CU_Reference_1
        self.CU_Reference_2         = CU_Reference_2
        self.CU_Reference_3         = CU_Reference_3

    def __repr__(self):
        return "<Charge_Units( CU_Id='%s', CI_Id='%s', CU_Description='%s', CU_UUID='%s', CU_Is_Billeable='%s', CU_Is_Always_Billeable='%s', CU_Quantity='%s', CU_Operation='%s', Typ_Code='%s', CIT_Generation='%s', Rat_Id='%s', CU_Reference_1='%s', CU_Reference_2='%s', CU_Reference_3='%s')>" % \
                ( self.CU_Id, self.CI_Id, self.CU_Description, self.CU_UUID, self.CU_Is_Billeable, self.CU_Is_Always_Billeable, self.CU_Quantity, self.CU_Operation, self.Typ_Code, self.CIT_Generation, self.Rat_Id, self.CU_Reference_1, self.CU_Reference_2, self.CU_Reference_3)

# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2020-02-24 14:48:48
# =============================================================================

def get_charge_unit(table_name_sufix):
  class charge_unit_Class(db.Model,Serializer):
    __tablename__ = 'Charge_Units_%s'%(table_name_sufix)
    CU_Id                  = db.Column( db.Integer, primary_key=True, autoincrement=True )
    CI_Id                  = db.Column( db.Integer, db.ForeignKey('Configuration_Items.CI_Id') )
    CU_Description         = db.Column( db.String(45) )
    CU_UUID                = db.Column( db.String(45) )
    CU_Is_Billeable        = db.Column( db.Boolean, default=0 )
    CU_Is_Always_Billeable = db.Column( db.Boolean, default=0 )
    CU_Quantity            = db.Column( db.Numeric(20,6) )
    CU_Operation           = db.Column( db.String(10), db.ForeignKey('CU_Operations.CU_Operation') )
    Typ_Code               = db.Column( db.String(10), db.ForeignKey('CU_Types.Typ_Code') )
    CIT_Generation         = db.Column( db.Integer, db.ForeignKey('CIT_Generations.CIT_Generation') )
    Rat_Id                 = db.Column( db.Integer )
    CU_Reference_1         = db.Column( db.String(45) )
    CU_Reference_2         = db.Column( db.String(45) )
    CU_Reference_3         = db.Column( db.String(45) )

    charge_items           = db.relationship('charge_item',backref='charge_unit',lazy='dynamic')
    charge_unit_egm        = db.relationship('charge_unit_egm',backref='charge_unit',lazy='dynamic')

    def __init__(self, CU_Id=0, CI_Id=None, CU_Description='None', CU_UUID='None', CU_Is_Billeable=0, CU_Is_Always_Billeable=0, CU_Quantity=None, CU_Operation='None', Typ_Code='None', CIT_Generation=None, Rat_Id=None, CU_Reference_1='None', CU_Reference_2='None', CU_Reference_3='None'):
        self.CU_Id                  = CU_Id
        self.CI_Id                  = CI_Id
        self.CU_Description         = CU_Description
        self.CU_UUID                = CU_UUID
        self.CU_Is_Billeable        = CU_Is_Billeable
        self.CU_Is_Always_Billeable = CU_Is_Always_Billeable
        self.CU_Quantity            = CU_Quantity
        self.CU_Operation           = CU_Operation
        self.Typ_Code               = Typ_Code
        self.CIT_Generation         = CIT_Generation
        self.Rat_Id                 = Rat_Id
        self.CU_Reference_1         = CU_Reference_1
        self.CU_Reference_2         = CU_Reference_2
        self.CU_Reference_3         = CU_Reference_3

    def __repr__(self):
        return "<Charge_Units( CU_Id='%s', CI_Id='%s', CU_Description='%s', CU_UUID='%s', CU_Is_Billeable='%s', CU_Is_Always_Billeable='%s', CU_Quantity='%s', CU_Operation='%s', Typ_Code='%s', CIT_Generation='%s', Rat_Id='%s', CU_Reference_1='%s', CU_Reference_2='%s', CU_Reference_3='%s')>" % \
                ( self.CU_Id, self.CI_Id, self.CU_Description, self.CU_UUID, self.CU_Is_Billeable, self.CU_Is_Always_Billeable, self.CU_Quantity, self.CU_Operation, self.Typ_Code, self.CIT_Generation, self.Rat_Id, self.CU_Reference_1, self.CU_Reference_2, self.CU_Reference_3)

  charge_unit_Class.__name__ = 'charge_unit_%s'%(table_name_sufix)
  return charge_unit_Class
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2022-03-07 18:58:14
# =============================================================================

# gen_model_flask.py:117 => /home/gvalera/GIT/EG-Suite-Tools/Collector/code/auto/models/flask_cit_generations.py
class cit_generation(db.Model,Serializer):
    __tablename__ = 'CIT_Generations'

    def check_shard(suffix=None,engine=None):
       if engine is not None:
           try:
               if not engine.dialect.has_table(engine, __class__.__tablename__):
                   print(f'131 Table {__class__.__tablename__} does not exist')
                   metadata=MetaData()
                   metadata.bind=engine
                   __class__.__table__.metadata=metadata
                   __class__.__table__.create(checkfirst=True)
                   if not engine.dialect.has_table(engine, __class__.__tablename__):
                       print('137 Table %s does not exist. creation error?'% __class__.__tablename__)
                   else:
                       print('139 Table %s exist !!!'% __class__.__tablename__)
               else:
                   pass # GV print('141 Table %s exist !!!'% __class__.__tablename__)
           except Exception as e:
              print(f'143 exception: {str(e)}')
           return
    def set_shard(suffix=None,engine=None):
       if suffix is not None:
           name='CIT_Generations_{suffix}'.format(suffix=suffix)
           __class__.__tablename__  = name
           __class__.__table__.name = name
       __class__.check_shard(suffix,engine)
       return __class__.__tablename__

    CIT_Generation = db.Column( db.Integer, primary_key=True )
    Value          = db.Column( db.String(45) )

    # child_table=None gen_children=True
    charge_units   = db.relationship('charge_unit',backref='cit_generation',lazy='dynamic')

    # looking for include file: /home/gvalera/GIT/EG-Suite-Tools/Collector/code/src/include/models/flask_cit_generations_properties.py
    # file: /home/gvalera/GIT/EG-Suite-Tools/Collector/code/src/include/models/flask_cit_generations_properties.py not found
    def __init__(self, CIT_Generation=None, Value='None'):
        self.CIT_Generation = CIT_Generation
        self.Value          = Value

    def __repr__(self):
        return "<CIT_Generations( CIT_Generation='%s', Value='%s')>" % \
                ( self.CIT_Generation, self.Value)

# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2022-03-07 18:58:14
# =============================================================================

# gen_model_flask.py:117 => /home/gvalera/GIT/EG-Suite-Tools/Collector/code/auto/models/flask_cit_statuses.py
class cit_status(db.Model,Serializer):
    __tablename__ = 'CIT_Statuses'

    def check_shard(suffix=None,engine=None):
       if engine is not None:
           try:
               if not engine.dialect.has_table(engine, __class__.__tablename__):
                   print(f'131 Table {__class__.__tablename__} does not exist')
                   metadata=MetaData()
                   metadata.bind=engine
                   __class__.__table__.metadata=metadata
                   __class__.__table__.create(checkfirst=True)
                   if not engine.dialect.has_table(engine, __class__.__tablename__):
                       print('137 Table %s does not exist. creation error?'% __class__.__tablename__)
                   else:
                       print('139 Table %s exist !!!'% __class__.__tablename__)
               else:
                   pass # GV print('141 Table %s exist !!!'% __class__.__tablename__)
           except Exception as e:
              print(f'143 exception: {str(e)}')
           return
    def set_shard(suffix=None,engine=None):
       if suffix is not None:
           name='CIT_Statuses_{suffix}'.format(suffix=suffix)
           __class__.__tablename__  = name
           __class__.__table__.name = name
       __class__.check_shard(suffix,engine)
       return __class__.__tablename__

    CIT_Status = db.Column( db.Integer, primary_key=True )
    Value      = db.Column( db.String(45) )

    # child_table=None gen_children=True
    charge_items = db.relationship('charge_item',backref='cit_status',lazy='dynamic')

    # looking for include file: /home/gvalera/GIT/EG-Suite-Tools/Collector/code/src/include/models/flask_cit_statuses_properties.py
    # file: /home/gvalera/GIT/EG-Suite-Tools/Collector/code/src/include/models/flask_cit_statuses_properties.py not found
    def __init__(self, CIT_Status=None, Value='None'):
        self.CIT_Status = CIT_Status
        self.Value      = Value

    def __repr__(self):
        return "<CIT_Statuses( CIT_Status='%s', Value='%s')>" % \
                ( self.CIT_Status, self.Value)

# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2022-03-07 18:58:14
# =============================================================================

# gen_model_flask.py:117 => /home/gvalera/GIT/EG-Suite-Tools/Collector/code/auto/models/flask_configuration_items.py
class configuration_item(db.Model,Serializer):
    __tablename__ = 'Configuration_Items'

    def check_shard(suffix=None,engine=None):
       if engine is not None:
           try:
               if not engine.dialect.has_table(engine, __class__.__tablename__):
                   print(f'131 Table {__class__.__tablename__} does not exist')
                   metadata=MetaData()
                   metadata.bind=engine
                   __class__.__table__.metadata=metadata
                   __class__.__table__.create(checkfirst=True)
                   if not engine.dialect.has_table(engine, __class__.__tablename__):
                       print('137 Table %s does not exist. creation error?'% __class__.__tablename__)
                   else:
                       print('139 Table %s exist !!!'% __class__.__tablename__)
               else:
                   pass # GV print('141 Table %s exist !!!'% __class__.__tablename__)
           except Exception as e:
              print(f'143 exception: {str(e)}')
           return
    def set_shard(suffix=None,engine=None):
       if suffix is not None:
           name='Configuration_Items_{suffix}'.format(suffix=suffix)
           __class__.__tablename__  = name
           __class__.__table__.name = name
       __class__.check_shard(suffix,engine)
       return __class__.__tablename__

    CI_Id                       = db.Column( db.Integer, primary_key=True, autoincrement=True )
    CI_Name                     = db.Column( db.String(255) )
    CI_UUID                     = db.Column( db.String(45) )
    Pla_Id                      = db.Column( db.Integer, db.ForeignKey('Platforms.Pla_Id') )
    CC_Id                       = db.Column( db.Integer, db.ForeignKey('Cost_Centers.CC_Id') )
    Cus_Id                      = db.Column( db.Integer, db.ForeignKey('Customers.Cus_Id'), default=1 )
    CI_Commissioning_DateTime   = db.Column( db.DateTime )
    CI_Decommissioning_DateTime = db.Column( db.DateTime )

    # child_table=Charge_Units gen_children=True
    charge_units                = db.relationship('charge_unit',backref='configuration_item',lazy='dynamic')
    # child_table=Charge_Units gen_children=True
    rates                       = db.relationship('rate',backref='configuration_item',lazy='dynamic')

    # looking for include file: /home/gvalera/GIT/EG-Suite-Tools/Collector/code/src/include/models/flask_configuration_items_properties.py
    # file: /home/gvalera/GIT/EG-Suite-Tools/Collector/code/src/include/models/flask_configuration_items_properties.py not found
    def __init__(self, CI_Id=0, CI_Name='None', CI_UUID='None', Pla_Id=None, CC_Id=None, Cus_Id=1, CI_Commissioning_DateTime=None, CI_Decommissioning_DateTime=None):
        self.CI_Id                       = CI_Id
        self.CI_Name                     = CI_Name
        self.CI_UUID                     = CI_UUID
        self.Pla_Id                      = Pla_Id
        self.CC_Id                       = CC_Id
        self.Cus_Id                      = Cus_Id
        self.CI_Commissioning_DateTime   = CI_Commissioning_DateTime
        self.CI_Decommissioning_DateTime = CI_Decommissioning_DateTime

    def __repr__(self):
        return "<Configuration_Items( CI_Id='%s', CI_Name='%s', CI_UUID='%s', Pla_Id='%s', CC_Id='%s', Cus_Id='%s', CI_Commissioning_DateTime='%s', CI_Decommissioning_DateTime='%s')>" % \
                ( self.CI_Id, self.CI_Name, self.CI_UUID, self.Pla_Id, self.CC_Id, self.Cus_Id, self.CI_Commissioning_DateTime, self.CI_Decommissioning_DateTime)

# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2022-03-07 18:58:14
# =============================================================================

# gen_model_flask.py:117 => /home/gvalera/GIT/EG-Suite-Tools/Collector/code/auto/models/flask_cost_centers.py
class cost_center(db.Model,Serializer):
    __tablename__ = 'Cost_Centers'

    def check_shard(suffix=None,engine=None):
       if engine is not None:
           try:
               if not engine.dialect.has_table(engine, __class__.__tablename__):
                   print(f'131 Table {__class__.__tablename__} does not exist')
                   metadata=MetaData()
                   metadata.bind=engine
                   __class__.__table__.metadata=metadata
                   __class__.__table__.create(checkfirst=True)
                   if not engine.dialect.has_table(engine, __class__.__tablename__):
                       print('137 Table %s does not exist. creation error?'% __class__.__tablename__)
                   else:
                       print('139 Table %s exist !!!'% __class__.__tablename__)
               else:
                   pass # GV print('141 Table %s exist !!!'% __class__.__tablename__)
           except Exception as e:
              print(f'143 exception: {str(e)}')
           return
    def set_shard(suffix=None,engine=None):
       if suffix is not None:
           name='Cost_Centers_{suffix}'.format(suffix=suffix)
           __class__.__tablename__  = name
           __class__.__table__.name = name
       __class__.check_shard(suffix,engine)
       return __class__.__tablename__

    CC_Id          = db.Column( db.Integer, primary_key=True, autoincrement=True )
    CC_Code        = db.Column( db.String(45) )
    CC_Description = db.Column( db.String(255) )
    Cur_Code       = db.Column( db.String(3), db.ForeignKey('Currencies.Cur_Code') )
    CC_Parent_Code = db.Column( db.String(45), default='1' )
    CC_Reg_Exp     = db.Column( db.String(45) )
    CC_Reference   = db.Column( db.String(245) )
    Cus_Id         = db.Column( db.Integer )

    # child_table=None gen_children=True
    configuration_items = db.relationship('configuration_item',backref='cost_center',lazy='dynamic')
    # child_table=None gen_children=True
    customers      = db.relationship('customer',backref='cost_center',lazy='dynamic')
    # child_table=None gen_children=True
    rates          = db.relationship('rate',backref='cost_center',lazy='dynamic')
    # child_table=None gen_children=True
    users          = db.relationship('User',backref='cost_center',lazy='dynamic')

    # looking for include file: /home/gvalera/GIT/EG-Suite-Tools/Collector/code/src/include/models/flask_cost_centers_properties.py
    # file: /home/gvalera/GIT/EG-Suite-Tools/Collector/code/src/include/models/flask_cost_centers_properties.py not found
    def __init__(self, CC_Id=0, CC_Code='None', CC_Description='None', Cur_Code='None', CC_Parent_Code='1', CC_Reg_Exp='None', CC_Reference='None', Cus_Id=None):
        self.CC_Id          = CC_Id
        self.CC_Code        = CC_Code
        self.CC_Description = CC_Description
        self.Cur_Code       = Cur_Code
        self.CC_Parent_Code = CC_Parent_Code
        self.CC_Reg_Exp     = CC_Reg_Exp
        self.CC_Reference   = CC_Reference
        self.Cus_Id         = Cus_Id

    def __repr__(self):
        return "<Cost_Centers( CC_Id='%s', CC_Code='%s', CC_Description='%s', Cur_Code='%s', CC_Parent_Code='%s', CC_Reg_Exp='%s', CC_Reference='%s', Cus_Id='%s')>" % \
                ( self.CC_Id, self.CC_Code, self.CC_Description, self.Cur_Code, self.CC_Parent_Code, self.CC_Reg_Exp, self.CC_Reference, self.Cus_Id)

# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2022-03-07 18:58:14
# =============================================================================

# gen_model_flask.py:117 => /home/gvalera/GIT/EG-Suite-Tools/Collector/code/auto/models/flask_countries_currencies.py
class country_currency(db.Model,Serializer):
    __tablename__ = 'Countries_Currencies'

    def check_shard(suffix=None,engine=None):
       if engine is not None:
           try:
               if not engine.dialect.has_table(engine, __class__.__tablename__):
                   print(f'131 Table {__class__.__tablename__} does not exist')
                   metadata=MetaData()
                   metadata.bind=engine
                   __class__.__table__.metadata=metadata
                   __class__.__table__.create(checkfirst=True)
                   if not engine.dialect.has_table(engine, __class__.__tablename__):
                       print('137 Table %s does not exist. creation error?'% __class__.__tablename__)
                   else:
                       print('139 Table %s exist !!!'% __class__.__tablename__)
               else:
                   pass # GV print('141 Table %s exist !!!'% __class__.__tablename__)
           except Exception as e:
              print(f'143 exception: {str(e)}')
           return
    def set_shard(suffix=None,engine=None):
       if suffix is not None:
           name='Countries_Currencies_{suffix}'.format(suffix=suffix)
           __class__.__tablename__  = name
           __class__.__table__.name = name
       __class__.check_shard(suffix,engine)
       return __class__.__tablename__

    Cou_Code        = db.Column( db.String(2), db.ForeignKey('Countries.Cou_Code'), primary_key=True )
    Cur_Code        = db.Column( db.String(3), db.ForeignKey('Currencies.Cur_Code'), primary_key=True )
    Cou_Cur_Comment = db.Column( db.String(45) )


    # looking for include file: /home/gvalera/GIT/EG-Suite-Tools/Collector/code/src/include/models/flask_countries_currencies_properties.py
    # file: /home/gvalera/GIT/EG-Suite-Tools/Collector/code/src/include/models/flask_countries_currencies_properties.py not found
    def __init__(self, Cou_Code='None', Cur_Code='None', Cou_Cur_Comment='None'):
        self.Cou_Code        = Cou_Code
        self.Cur_Code        = Cur_Code
        self.Cou_Cur_Comment = Cou_Cur_Comment

    def __repr__(self):
        return "<Countries_Currencies( Cou_Code='%s', Cur_Code='%s', Cou_Cur_Comment='%s')>" % \
                ( self.Cou_Code, self.Cur_Code, self.Cou_Cur_Comment)

# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2022-03-07 18:58:14
# =============================================================================

# gen_model_flask.py:117 => /home/gvalera/GIT/EG-Suite-Tools/Collector/code/auto/models/flask_countries.py
class country(db.Model,Serializer):
    __tablename__ = 'Countries'

    def check_shard(suffix=None,engine=None):
       if engine is not None:
           try:
               if not engine.dialect.has_table(engine, __class__.__tablename__):
                   print(f'131 Table {__class__.__tablename__} does not exist')
                   metadata=MetaData()
                   metadata.bind=engine
                   __class__.__table__.metadata=metadata
                   __class__.__table__.create(checkfirst=True)
                   if not engine.dialect.has_table(engine, __class__.__tablename__):
                       print('137 Table %s does not exist. creation error?'% __class__.__tablename__)
                   else:
                       print('139 Table %s exist !!!'% __class__.__tablename__)
               else:
                   pass # GV print('141 Table %s exist !!!'% __class__.__tablename__)
           except Exception as e:
              print(f'143 exception: {str(e)}')
           return
    def set_shard(suffix=None,engine=None):
       if suffix is not None:
           name='Countries_{suffix}'.format(suffix=suffix)
           __class__.__tablename__  = name
           __class__.__table__.name = name
       __class__.check_shard(suffix,engine)
       return __class__.__tablename__

    Cou_Code = db.Column( db.String(2), primary_key=True )
    Cou_Name = db.Column( db.String(45) )
    Cou_A3   = db.Column( db.String(3) )
    Cou_N    = db.Column( db.Integer )

    # child_table=None gen_children=True
    countries_currencies = db.relationship('country_currency',backref='country',lazy='dynamic')

    # looking for include file: /home/gvalera/GIT/EG-Suite-Tools/Collector/code/src/include/models/flask_countries_properties.py
    # file: /home/gvalera/GIT/EG-Suite-Tools/Collector/code/src/include/models/flask_countries_properties.py not found
    def __init__(self, Cou_Code='None', Cou_Name='None', Cou_A3='None', Cou_N=None):
        self.Cou_Code = Cou_Code
        self.Cou_Name = Cou_Name
        self.Cou_A3   = Cou_A3
        self.Cou_N    = Cou_N

    def __repr__(self):
        return "<Countries( Cou_Code='%s', Cou_Name='%s', Cou_A3='%s', Cou_N='%s')>" % \
                ( self.Cou_Code, self.Cou_Name, self.Cou_A3, self.Cou_N)

# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2022-03-07 18:58:14
# =============================================================================

# gen_model_flask.py:117 => /home/gvalera/GIT/EG-Suite-Tools/Collector/code/auto/models/flask_cu_operations.py
class cu_operation(db.Model,Serializer):
    __tablename__ = 'CU_Operations'

    def check_shard(suffix=None,engine=None):
       if engine is not None:
           try:
               if not engine.dialect.has_table(engine, __class__.__tablename__):
                   print(f'131 Table {__class__.__tablename__} does not exist')
                   metadata=MetaData()
                   metadata.bind=engine
                   __class__.__table__.metadata=metadata
                   __class__.__table__.create(checkfirst=True)
                   if not engine.dialect.has_table(engine, __class__.__tablename__):
                       print('137 Table %s does not exist. creation error?'% __class__.__tablename__)
                   else:
                       print('139 Table %s exist !!!'% __class__.__tablename__)
               else:
                   pass # GV print('141 Table %s exist !!!'% __class__.__tablename__)
           except Exception as e:
              print(f'143 exception: {str(e)}')
           return
    def set_shard(suffix=None,engine=None):
       if suffix is not None:
           name='CU_Operations_{suffix}'.format(suffix=suffix)
           __class__.__tablename__  = name
           __class__.__table__.name = name
       __class__.check_shard(suffix,engine)
       return __class__.__tablename__

    CU_Operation = db.Column( db.String(10), primary_key=True )
    Value        = db.Column( db.String(45) )
    Is_Multiply  = db.Column( db.Boolean )
    Factor       = db.Column( db.Integer )

    # child_table=None gen_children=True
    charge_units = db.relationship('charge_unit',backref='cu_operation',lazy='dynamic')

    # looking for include file: /home/gvalera/GIT/EG-Suite-Tools/Collector/code/src/include/models/flask_cu_operations_properties.py
    # file: /home/gvalera/GIT/EG-Suite-Tools/Collector/code/src/include/models/flask_cu_operations_properties.py not found
    def __init__(self, CU_Operation='None', Value='None', Is_Multiply=None, Factor=None):
        self.CU_Operation = CU_Operation
        self.Value        = Value
        self.Is_Multiply  = Is_Multiply
        self.Factor       = Factor

    def __repr__(self):
        return "<CU_Operations( CU_Operation='%s', Value='%s', Is_Multiply='%s', Factor='%s')>" % \
                ( self.CU_Operation, self.Value, self.Is_Multiply, self.Factor)

# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2022-03-07 18:58:14
# =============================================================================

# gen_model_flask.py:117 => /home/gvalera/GIT/EG-Suite-Tools/Collector/code/auto/models/flask_currencies.py
class currency(db.Model,Serializer):
    __tablename__ = 'Currencies'

    def check_shard(suffix=None,engine=None):
       if engine is not None:
           try:
               if not engine.dialect.has_table(engine, __class__.__tablename__):
                   print(f'131 Table {__class__.__tablename__} does not exist')
                   metadata=MetaData()
                   metadata.bind=engine
                   __class__.__table__.metadata=metadata
                   __class__.__table__.create(checkfirst=True)
                   if not engine.dialect.has_table(engine, __class__.__tablename__):
                       print('137 Table %s does not exist. creation error?'% __class__.__tablename__)
                   else:
                       print('139 Table %s exist !!!'% __class__.__tablename__)
               else:
                   pass # GV print('141 Table %s exist !!!'% __class__.__tablename__)
           except Exception as e:
              print(f'143 exception: {str(e)}')
           return
    def set_shard(suffix=None,engine=None):
       if suffix is not None:
           name='Currencies_{suffix}'.format(suffix=suffix)
           __class__.__tablename__  = name
           __class__.__table__.name = name
       __class__.check_shard(suffix,engine)
       return __class__.__tablename__

    Cur_Code    = db.Column( db.String(3), primary_key=True )
    Cur_Name    = db.Column( db.String(45) )
    Cur_Id      = db.Column( db.Integer )
    Cur_Comment = db.Column( db.String(128) )

    # child_table=None gen_children=True
    cost_centers = db.relationship('cost_center',backref='currency',lazy='dynamic')
    # child_table=None gen_children=True
    countries_currencies = db.relationship('country_currency',backref='currency',lazy='dynamic')
    # child_table=None gen_children=True
    exchange_rates = db.relationship('exchange_rate',backref='currency',lazy='dynamic')
    # child_table=None gen_children=True
    rates       = db.relationship('rate',backref='currency',lazy='dynamic')

    # looking for include file: /home/gvalera/GIT/EG-Suite-Tools/Collector/code/src/include/models/flask_currencies_properties.py
    # file: /home/gvalera/GIT/EG-Suite-Tools/Collector/code/src/include/models/flask_currencies_properties.py not found
    def __init__(self, Cur_Code='None', Cur_Name='None', Cur_Id=None, Cur_Comment='None'):
        self.Cur_Code    = Cur_Code
        self.Cur_Name    = Cur_Name
        self.Cur_Id      = Cur_Id
        self.Cur_Comment = Cur_Comment

    def __repr__(self):
        return "<Currencies( Cur_Code='%s', Cur_Name='%s', Cur_Id='%s', Cur_Comment='%s')>" % \
                ( self.Cur_Code, self.Cur_Name, self.Cur_Id, self.Cur_Comment)

# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2022-03-07 18:58:14
# =============================================================================

# gen_model_flask.py:117 => /home/gvalera/GIT/EG-Suite-Tools/Collector/code/auto/models/flask_customers.py
class customer(db.Model,Serializer):
    __tablename__ = 'Customers'

    def check_shard(suffix=None,engine=None):
       if engine is not None:
           try:
               if not engine.dialect.has_table(engine, __class__.__tablename__):
                   print(f'131 Table {__class__.__tablename__} does not exist')
                   metadata=MetaData()
                   metadata.bind=engine
                   __class__.__table__.metadata=metadata
                   __class__.__table__.create(checkfirst=True)
                   if not engine.dialect.has_table(engine, __class__.__tablename__):
                       print('137 Table %s does not exist. creation error?'% __class__.__tablename__)
                   else:
                       print('139 Table %s exist !!!'% __class__.__tablename__)
               else:
                   pass # GV print('141 Table %s exist !!!'% __class__.__tablename__)
           except Exception as e:
              print(f'143 exception: {str(e)}')
           return
    def set_shard(suffix=None,engine=None):
       if suffix is not None:
           name='Customers_{suffix}'.format(suffix=suffix)
           __class__.__tablename__  = name
           __class__.__table__.name = name
       __class__.check_shard(suffix,engine)
       return __class__.__tablename__

    Cus_Id   = db.Column( db.Integer, primary_key=True, autoincrement=True )
    Cus_Name = db.Column( db.String(255) )
    CC_Id    = db.Column( db.Integer, db.ForeignKey('Cost_Centers.CC_Id') )

    # child_table=None gen_children=True
    configuration_items = db.relationship('configuration_item',backref='customer',lazy='dynamic')
    # child_table=None gen_children=True
    rates    = db.relationship('rate',backref='customer',lazy='dynamic')

    # looking for include file: /home/gvalera/GIT/EG-Suite-Tools/Collector/code/src/include/models/flask_customers_properties.py
    # file: /home/gvalera/GIT/EG-Suite-Tools/Collector/code/src/include/models/flask_customers_properties.py not found
    def __init__(self, Cus_Id=0, Cus_Name='None', CC_Id=None):
        self.Cus_Id   = Cus_Id
        self.Cus_Name = Cus_Name
        self.CC_Id    = CC_Id

    def __repr__(self):
        return "<Customers( Cus_Id='%s', Cus_Name='%s', CC_Id='%s')>" % \
                ( self.Cus_Id, self.Cus_Name, self.CC_Id)

# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2022-03-07 18:58:14
# =============================================================================

# gen_model_flask.py:117 => /home/gvalera/GIT/EG-Suite-Tools/Collector/code/auto/models/flask_cu_types.py
class cu_type(db.Model,Serializer):
    __tablename__ = 'CU_Types'

    def check_shard(suffix=None,engine=None):
       if engine is not None:
           try:
               if not engine.dialect.has_table(engine, __class__.__tablename__):
                   print(f'131 Table {__class__.__tablename__} does not exist')
                   metadata=MetaData()
                   metadata.bind=engine
                   __class__.__table__.metadata=metadata
                   __class__.__table__.create(checkfirst=True)
                   if not engine.dialect.has_table(engine, __class__.__tablename__):
                       print('137 Table %s does not exist. creation error?'% __class__.__tablename__)
                   else:
                       print('139 Table %s exist !!!'% __class__.__tablename__)
               else:
                   pass # GV print('141 Table %s exist !!!'% __class__.__tablename__)
           except Exception as e:
              print(f'143 exception: {str(e)}')
           return
    def set_shard(suffix=None,engine=None):
       if suffix is not None:
           name='CU_Types_{suffix}'.format(suffix=suffix)
           __class__.__tablename__  = name
           __class__.__table__.name = name
       __class__.check_shard(suffix,engine)
       return __class__.__tablename__

    Typ_Code        = db.Column( db.String(10), primary_key=True )
    Typ_Description = db.Column( db.String(45) )

    # child_table=None gen_children=True
    charge_units    = db.relationship('charge_unit',backref='cu_type',lazy='dynamic')
    # child_table=None gen_children=True
    rates           = db.relationship('rate',backref='cu_type',lazy='dynamic')

    # looking for include file: /home/gvalera/GIT/EG-Suite-Tools/Collector/code/src/include/models/flask_cu_types_properties.py
    # file: /home/gvalera/GIT/EG-Suite-Tools/Collector/code/src/include/models/flask_cu_types_properties.py not found
    def __init__(self, Typ_Code='None', Typ_Description='None'):
        self.Typ_Code        = Typ_Code
        self.Typ_Description = Typ_Description

    def __repr__(self):
        return "<CU_Types( Typ_Code='%s', Typ_Description='%s')>" % \
                ( self.Typ_Code, self.Typ_Description)

# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2022-03-07 18:58:14
# =============================================================================

# gen_model_flask.py:117 => /home/gvalera/GIT/EG-Suite-Tools/Collector/code/auto/models/flask_exchange_rates.py
class exchange_rate(db.Model,Serializer):
    __tablename__ = 'Exchange_Rates'

    def check_shard(suffix=None,engine=None):
       if engine is not None:
           try:
               if not engine.dialect.has_table(engine, __class__.__tablename__):
                   print(f'131 Table {__class__.__tablename__} does not exist')
                   metadata=MetaData()
                   metadata.bind=engine
                   __class__.__table__.metadata=metadata
                   __class__.__table__.create(checkfirst=True)
                   if not engine.dialect.has_table(engine, __class__.__tablename__):
                       print('137 Table %s does not exist. creation error?'% __class__.__tablename__)
                   else:
                       print('139 Table %s exist !!!'% __class__.__tablename__)
               else:
                   pass # GV print('141 Table %s exist !!!'% __class__.__tablename__)
           except Exception as e:
              print(f'143 exception: {str(e)}')
           return
    def set_shard(suffix=None,engine=None):
       if suffix is not None:
           name='Exchange_Rates_{suffix}'.format(suffix=suffix)
           __class__.__tablename__  = name
           __class__.__table__.name = name
       __class__.check_shard(suffix,engine)
       return __class__.__tablename__

    ER_Id     = db.Column( db.Integer, primary_key=True, autoincrement=True )
    Cur_Code  = db.Column( db.String(3), db.ForeignKey('Currencies.Cur_Code') )
    ER_Factor = db.Column( db.Numeric(20,12) )
    ER_Date   = db.Column( db.Date )


    # looking for include file: /home/gvalera/GIT/EG-Suite-Tools/Collector/code/src/include/models/flask_exchange_rates_properties.py
    # file: /home/gvalera/GIT/EG-Suite-Tools/Collector/code/src/include/models/flask_exchange_rates_properties.py not found
    def __init__(self, ER_Id=0, Cur_Code='None', ER_Factor=None, ER_Date=None):
        self.ER_Id     = ER_Id
        self.Cur_Code  = Cur_Code
        self.ER_Factor = ER_Factor
        self.ER_Date   = ER_Date

    def __repr__(self):
        return "<Exchange_Rates( ER_Id='%s', Cur_Code='%s', ER_Factor='%s', ER_Date='%s')>" % \
                ( self.ER_Id, self.Cur_Code, self.ER_Factor, self.ER_Date)

# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2022-03-07 18:58:14
# =============================================================================

# gen_model_flask.py:117 => /home/gvalera/GIT/EG-Suite-Tools/Collector/code/auto/models/flask_interface.py
class interface(db.Model,Serializer):
    __tablename__ = 'Interface'

    def check_shard(suffix=None,engine=None):
       if engine is not None:
           try:
               if not engine.dialect.has_table(engine, __class__.__tablename__):
                   print(f'131 Table {__class__.__tablename__} does not exist')
                   metadata=MetaData()
                   metadata.bind=engine
                   __class__.__table__.metadata=metadata
                   __class__.__table__.create(checkfirst=True)
                   if not engine.dialect.has_table(engine, __class__.__tablename__):
                       print('137 Table %s does not exist. creation error?'% __class__.__tablename__)
                   else:
                       print('139 Table %s exist !!!'% __class__.__tablename__)
               else:
                   pass # GV print('141 Table %s exist !!!'% __class__.__tablename__)
           except Exception as e:
              print(f'143 exception: {str(e)}')
           return
    def set_shard(suffix=None,engine=None):
       if suffix is not None:
           name='Interface_{suffix}'.format(suffix=suffix)
           __class__.__tablename__  = name
           __class__.__table__.name = name
       __class__.check_shard(suffix,engine)
       return __class__.__tablename__

    Id          = db.Column( db.Integer, primary_key=True, autoincrement=True )
    User_Id     = db.Column( db.Integer )
    Table_name  = db.Column( db.String(45) )
    Option_Type = db.Column( db.Integer )
    Argument_1  = db.Column( db.String(256) )
    Argument_2  = db.Column( db.String(256) )
    Argument_3  = db.Column( db.String(256) )
    Is_Active   = db.Column( db.Boolean )


    # looking for include file: /home/gvalera/GIT/EG-Suite-Tools/Collector/code/src/include/models/flask_interface_properties.py
    # file: /home/gvalera/GIT/EG-Suite-Tools/Collector/code/src/include/models/flask_interface_properties.py not found
    def __init__(self, Id=0, User_Id=None, Table_name='None', Option_Type=None, Argument_1='None', Argument_2='None', Argument_3='None', Is_Active=None):
        self.Id          = Id
        self.User_Id     = User_Id
        self.Table_name  = Table_name
        self.Option_Type = Option_Type
        self.Argument_1  = Argument_1
        self.Argument_2  = Argument_2
        self.Argument_3  = Argument_3
        self.Is_Active   = Is_Active

    def __repr__(self):
        return "<Interface( Id='%s', User_Id='%s', Table_name='%s', Option_Type='%s', Argument_1='%s', Argument_2='%s', Argument_3='%s', Is_Active='%s')>" % \
                ( self.Id, self.User_Id, self.Table_name, self.Option_Type, self.Argument_1, self.Argument_2, self.Argument_3, self.Is_Active)

# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2022-03-07 18:58:14
# =============================================================================

# gen_model_flask.py:117 => /home/gvalera/GIT/EG-Suite-Tools/Collector/code/auto/models/flask_measure_units.py
class measure_unit(db.Model,Serializer):
    __tablename__ = 'Measure_Units'

    def check_shard(suffix=None,engine=None):
       if engine is not None:
           try:
               if not engine.dialect.has_table(engine, __class__.__tablename__):
                   print(f'131 Table {__class__.__tablename__} does not exist')
                   metadata=MetaData()
                   metadata.bind=engine
                   __class__.__table__.metadata=metadata
                   __class__.__table__.create(checkfirst=True)
                   if not engine.dialect.has_table(engine, __class__.__tablename__):
                       print('137 Table %s does not exist. creation error?'% __class__.__tablename__)
                   else:
                       print('139 Table %s exist !!!'% __class__.__tablename__)
               else:
                   pass # GV print('141 Table %s exist !!!'% __class__.__tablename__)
           except Exception as e:
              print(f'143 exception: {str(e)}')
           return
    def set_shard(suffix=None,engine=None):
       if suffix is not None:
           name='Measure_Units_{suffix}'.format(suffix=suffix)
           __class__.__tablename__  = name
           __class__.__table__.name = name
       __class__.check_shard(suffix,engine)
       return __class__.__tablename__

    MU_Code        = db.Column( db.String(3), primary_key=True )
    MU_Description = db.Column( db.String(45) )

    # child_table=None gen_children=True
    rates          = db.relationship('rate',backref='measure_unit',lazy='dynamic')

    # looking for include file: /home/gvalera/GIT/EG-Suite-Tools/Collector/code/src/include/models/flask_measure_units_properties.py
    # file: /home/gvalera/GIT/EG-Suite-Tools/Collector/code/src/include/models/flask_measure_units_properties.py not found
    def __init__(self, MU_Code='None', MU_Description='None'):
        self.MU_Code        = MU_Code
        self.MU_Description = MU_Description

    def __repr__(self):
        return "<Measure_Units( MU_Code='%s', MU_Description='%s')>" % \
                ( self.MU_Code, self.MU_Description)

# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2022-03-07 18:58:14
# =============================================================================

# gen_model_flask.py:117 => /home/gvalera/GIT/EG-Suite-Tools/Collector/code/auto/models/flask_platforms.py
class platform(db.Model,Serializer):
    __tablename__ = 'Platforms'

    def check_shard(suffix=None,engine=None):
       if engine is not None:
           try:
               if not engine.dialect.has_table(engine, __class__.__tablename__):
                   print(f'131 Table {__class__.__tablename__} does not exist')
                   metadata=MetaData()
                   metadata.bind=engine
                   __class__.__table__.metadata=metadata
                   __class__.__table__.create(checkfirst=True)
                   if not engine.dialect.has_table(engine, __class__.__tablename__):
                       print('137 Table %s does not exist. creation error?'% __class__.__tablename__)
                   else:
                       print('139 Table %s exist !!!'% __class__.__tablename__)
               else:
                   pass # GV print('141 Table %s exist !!!'% __class__.__tablename__)
           except Exception as e:
              print(f'143 exception: {str(e)}')
           return
    def set_shard(suffix=None,engine=None):
       if suffix is not None:
           name='Platforms_{suffix}'.format(suffix=suffix)
           __class__.__tablename__  = name
           __class__.__table__.name = name
       __class__.check_shard(suffix,engine)
       return __class__.__tablename__

    Pla_Id       = db.Column( db.Integer, primary_key=True, autoincrement=True )
    Pla_Name     = db.Column( db.String(255) )
    Pla_Host     = db.Column( db.String(45) )
    Pla_Port     = db.Column( db.String(45) )
    Pla_User     = db.Column( db.String(45) )
    Pla_Password = db.Column( db.String(45) )

    # child_table=None gen_children=True
    configuration_items = db.relationship('configuration_item',backref='platform',lazy='dynamic')
    # child_table=None gen_children=True
    rates        = db.relationship('rate',backref='platform',lazy='dynamic')

    # looking for include file: /home/gvalera/GIT/EG-Suite-Tools/Collector/code/src/include/models/flask_platforms_properties.py
    # file: /home/gvalera/GIT/EG-Suite-Tools/Collector/code/src/include/models/flask_platforms_properties.py not found
    def __init__(self, Pla_Id=0, Pla_Name='None', Pla_Host='None', Pla_Port='None', Pla_User='None', Pla_Password='None'):
        self.Pla_Id       = Pla_Id
        self.Pla_Name     = Pla_Name
        self.Pla_Host     = Pla_Host
        self.Pla_Port     = Pla_Port
        self.Pla_User     = Pla_User
        self.Pla_Password = Pla_Password

    def __repr__(self):
        return "<Platforms( Pla_Id='%s', Pla_Name='%s', Pla_Host='%s', Pla_Port='%s', Pla_User='%s', Pla_Password='%s')>" % \
                ( self.Pla_Id, self.Pla_Name, self.Pla_Host, self.Pla_Port, self.Pla_User, self.Pla_Password)

# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2022-03-07 18:58:14
# =============================================================================

# gen_model_flask.py:117 => /home/gvalera/GIT/EG-Suite-Tools/Collector/code/auto/models/flask_rates.py
class rate(db.Model,Serializer):
    __tablename__ = 'Rates'

    def check_shard(suffix=None,engine=None):
       if engine is not None:
           try:
               if not engine.dialect.has_table(engine, __class__.__tablename__):
                   print(f'131 Table {__class__.__tablename__} does not exist')
                   metadata=MetaData()
                   metadata.bind=engine
                   __class__.__table__.metadata=metadata
                   __class__.__table__.create(checkfirst=True)
                   if not engine.dialect.has_table(engine, __class__.__tablename__):
                       print('137 Table %s does not exist. creation error?'% __class__.__tablename__)
                   else:
                       print('139 Table %s exist !!!'% __class__.__tablename__)
               else:
                   pass # GV print('141 Table %s exist !!!'% __class__.__tablename__)
           except Exception as e:
              print(f'143 exception: {str(e)}')
           return
    def set_shard(suffix=None,engine=None):
       if suffix is not None:
           name='Rates_{suffix}'.format(suffix=suffix)
           __class__.__tablename__  = name
           __class__.__table__.name = name
       __class__.check_shard(suffix,engine)
       return __class__.__tablename__

    Rat_Id     = db.Column( db.Integer, primary_key=True, autoincrement=True )
    Typ_Code   = db.Column( db.String(10), db.ForeignKey('CU_Types.Typ_Code') )
    Cus_Id     = db.Column( db.Integer, db.ForeignKey('Customers.Cus_Id') )
    Pla_Id     = db.Column( db.Integer, db.ForeignKey('Platforms.Pla_Id') )
    CC_Id      = db.Column( db.Integer, db.ForeignKey('Cost_Centers.CC_Id') )
    CI_Id      = db.Column( db.Integer, db.ForeignKey('Configuration_Items.CI_Id') )
    Rat_Price  = db.Column( db.Numeric(20,12) )
    Cur_Code   = db.Column( db.String(3), db.ForeignKey('Currencies.Cur_Code') )
    MU_Code    = db.Column( db.String(3), db.ForeignKey('Measure_Units.MU_Code') )
    Rat_Period = db.Column( db.Integer, db.ForeignKey('Rat_Periods.Rat_Period') )
    Rat_Type   = db.Column( db.Integer )


    # looking for include file: /home/gvalera/GIT/EG-Suite-Tools/Collector/code/src/include/models/flask_rates_properties.py
    # including file: /home/gvalera/GIT/EG-Suite-Tools/Collector/code/src/include/models/flask_rates_properties.py
    # @property
    #
    
    def __init__(self, Rat_Id=0, Typ_Code='None', Cus_Id=None, Pla_Id=None, CC_Id=None, CI_Id=None, Rat_Price=None, Cur_Code='None', MU_Code='None', Rat_Period=None, Rat_Type=None):
        self.Rat_Id     = Rat_Id
        self.Typ_Code   = Typ_Code
        self.Cus_Id     = Cus_Id
        self.Pla_Id     = Pla_Id
        self.CC_Id      = CC_Id
        self.CI_Id      = CI_Id
        self.Rat_Price  = Rat_Price
        self.Cur_Code   = Cur_Code
        self.MU_Code    = MU_Code
        self.Rat_Period = Rat_Period
        self.Rat_Type   = Rat_Type

    def __repr__(self):
        return "<Rates( Rat_Id='%s', Typ_Code='%s', Cus_Id='%s', Pla_Id='%s', CC_Id='%s', CI_Id='%s', Rat_Price='%s', Cur_Code='%s', MU_Code='%s', Rat_Period='%s', Rat_Type='%s')>" % \
                ( self.Rat_Id, self.Typ_Code, self.Cus_Id, self.Pla_Id, self.CC_Id, self.CI_Id, self.Rat_Price, self.Cur_Code, self.MU_Code, self.Rat_Period, self.Rat_Type)

    # method
    def method(self):
        pass
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2022-03-07 18:58:14
# =============================================================================

# gen_model_flask.py:117 => /home/gvalera/GIT/EG-Suite-Tools/Collector/code/auto/models/flask_rat_periods.py
class rat_period(db.Model,Serializer):
    __tablename__ = 'Rat_Periods'

    def check_shard(suffix=None,engine=None):
       if engine is not None:
           try:
               if not engine.dialect.has_table(engine, __class__.__tablename__):
                   print(f'131 Table {__class__.__tablename__} does not exist')
                   metadata=MetaData()
                   metadata.bind=engine
                   __class__.__table__.metadata=metadata
                   __class__.__table__.create(checkfirst=True)
                   if not engine.dialect.has_table(engine, __class__.__tablename__):
                       print('137 Table %s does not exist. creation error?'% __class__.__tablename__)
                   else:
                       print('139 Table %s exist !!!'% __class__.__tablename__)
               else:
                   pass # GV print('141 Table %s exist !!!'% __class__.__tablename__)
           except Exception as e:
              print(f'143 exception: {str(e)}')
           return
    def set_shard(suffix=None,engine=None):
       if suffix is not None:
           name='Rat_Periods_{suffix}'.format(suffix=suffix)
           __class__.__tablename__  = name
           __class__.__table__.name = name
       __class__.check_shard(suffix,engine)
       return __class__.__tablename__

    Rat_Period = db.Column( db.Integer, primary_key=True )
    Value      = db.Column( db.String(45) )

    # child_table=None gen_children=True
    rates      = db.relationship('rate',backref='rat_period',lazy='dynamic')

    # looking for include file: /home/gvalera/GIT/EG-Suite-Tools/Collector/code/src/include/models/flask_rat_periods_properties.py
    # file: /home/gvalera/GIT/EG-Suite-Tools/Collector/code/src/include/models/flask_rat_periods_properties.py not found
    def __init__(self, Rat_Period=None, Value='None'):
        self.Rat_Period = Rat_Period
        self.Value      = Value

    def __repr__(self):
        return "<Rat_Periods( Rat_Period='%s', Value='%s')>" % \
                ( self.Rat_Period, self.Value)

# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2022-03-07 18:58:14
# =============================================================================

# gen_model_flask.py:117 => /home/gvalera/GIT/EG-Suite-Tools/Collector/code/auto/models/flask_roles.py
class Role(db.Model,Serializer):
    __tablename__ = 'Roles'

    def check_shard(suffix=None,engine=None):
       if engine is not None:
           try:
               if not engine.dialect.has_table(engine, __class__.__tablename__):
                   print(f'131 Table {__class__.__tablename__} does not exist')
                   metadata=MetaData()
                   metadata.bind=engine
                   __class__.__table__.metadata=metadata
                   __class__.__table__.create(checkfirst=True)
                   if not engine.dialect.has_table(engine, __class__.__tablename__):
                       print('137 Table %s does not exist. creation error?'% __class__.__tablename__)
                   else:
                       print('139 Table %s exist !!!'% __class__.__tablename__)
               else:
                   pass # GV print('141 Table %s exist !!!'% __class__.__tablename__)
           except Exception as e:
              print(f'143 exception: {str(e)}')
           return
    def set_shard(suffix=None,engine=None):
       if suffix is not None:
           name='Roles_{suffix}'.format(suffix=suffix)
           __class__.__tablename__  = name
           __class__.__table__.name = name
       __class__.check_shard(suffix,engine)
       return __class__.__tablename__

    id          = db.Column( db.Integer, primary_key=True )
    name        = db.Column( db.String(64) )
    default     = db.Column( db.Boolean )
    permissions = db.Column( db.Integer )

    # child_table=None gen_children=True
    users       = db.relationship('User',backref='role',lazy='dynamic')

    # looking for include file: /home/gvalera/GIT/EG-Suite-Tools/Collector/code/src/include/models/flask_roles_properties.py
    # file: /home/gvalera/GIT/EG-Suite-Tools/Collector/code/src/include/models/flask_roles_properties.py not found
    @staticmethod
    def insert_roles():
        roles = {
            'Customer': (   Permission.CUSTOMER, False),
            'Reporter': (   Permission.VIEW |
                            Permission.REPORT |
                            Permission.EXPORT, True),
            'Charger': (    Permission.VIEW |
                            Permission.DELETE |
                            Permission.MODIFY |
                            Permission.REPORT, False),
            'Administrator':    (0xfe, False),                      # Administrator does not have 'Customer' permisions
            'Auditor':          (0x1fe, False),                      # Auditor does not have 'Customer' permissions
            'God':              (0xfff, False)
        }
        for r in roles:
            role = Role.query.filter_by(name=r).first()
            if role is None:
                role = Role(name=r)
            role.permissions = roles[r][0]
            role.default = roles[r][1]
            db.session.add(role)
        db.session.commit()
    """
    def __repr__(self):
        return '<Role %r>' % self.name
    """
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2022-03-07 18:58:14
# =============================================================================

# gen_model_flask.py:117 => /home/gvalera/GIT/EG-Suite-Tools/Collector/code/auto/models/flask_st_use_per_cu.py
class st_use_per_cu(db.Model,Serializer):
    __tablename__ = 'ST_Use_Per_CU'

    def check_shard(suffix=None,engine=None):
       if engine is not None:
           try:
               if not engine.dialect.has_table(engine, __class__.__tablename__):
                   print(f'131 Table {__class__.__tablename__} does not exist')
                   metadata=MetaData()
                   metadata.bind=engine
                   __class__.__table__.metadata=metadata
                   __class__.__table__.create(checkfirst=True)
                   if not engine.dialect.has_table(engine, __class__.__tablename__):
                       print('137 Table %s does not exist. creation error?'% __class__.__tablename__)
                   else:
                       print('139 Table %s exist !!!'% __class__.__tablename__)
               else:
                   pass # GV print('141 Table %s exist !!!'% __class__.__tablename__)
           except Exception as e:
              print(f'143 exception: {str(e)}')
           return
    def set_shard(suffix=None,engine=None):
       if suffix is not None:
           name='ST_Use_Per_CU_{suffix}'.format(suffix=suffix)
           __class__.__tablename__  = name
           __class__.__table__.name = name
       __class__.check_shard(suffix,engine)
       return __class__.__tablename__

    CU_Id                  = db.Column( db.Integer, primary_key=True )
    From                   = db.Column( db.DateTime, primary_key=True )
    To                     = db.Column( db.DateTime, primary_key=True )
    Total_Slices           = db.Column( db.Integer, default=0 )
    Found_Slices           = db.Column( db.Integer, default=0 )
    Not_Found_Slices       = db.Column( db.Integer, default=0 )
    Period_Initial_Q       = db.Column( db.Numeric(20,12), default=0.000000000000 )
    Period_Increase        = db.Column( db.Numeric(20,12), default=0.000000000000 )
    Period_Increase_Count  = db.Column( db.Integer, default=0 )
    Period_Reduction       = db.Column( db.Numeric(20,12), default=0.000000000000 )
    Period_Reduction_Count = db.Column( db.Integer, default=0 )
    Period_Final_Q         = db.Column( db.Numeric(20,12), default=0.000000000000 )
    CI_Id                  = db.Column( db.Integer, default=1 )
    CC_Id                  = db.Column( db.Integer, default=1 )
    Cus_Id                 = db.Column( db.Integer, default=1 )
    Rat_Id                 = db.Column( db.Integer, default=1 )
    Typ_Code               = db.Column( db.String(10), default='NUL' )
    Pla_Id                 = db.Column( db.Integer, default=1 )
    Mean                   = db.Column( db.Numeric(20,12), default=0.000000000000 )
    Variance               = db.Column( db.Numeric(20,12), default=0.000000000000 )
    StdDev                 = db.Column( db.Numeric(20,12), default=0.000000000000 )
    Min                    = db.Column( db.Numeric(20,12), default=0.000000000000 )
    Max                    = db.Column( db.Numeric(20,12), default=0.000000000000 )


    # looking for include file: /home/gvalera/GIT/EG-Suite-Tools/Collector/code/src/include/models/flask_st_use_per_cu_properties.py
    # file: /home/gvalera/GIT/EG-Suite-Tools/Collector/code/src/include/models/flask_st_use_per_cu_properties.py not found
    def __init__(self, CU_Id=None, From=None, To=None, Total_Slices=0, Found_Slices=0, Not_Found_Slices=0, Period_Initial_Q=0.000000000000, Period_Increase=0.000000000000, Period_Increase_Count=0, Period_Reduction=0.000000000000, Period_Reduction_Count=0, Period_Final_Q=0.000000000000, CI_Id=1, CC_Id=1, Cus_Id=1, Rat_Id=1, Typ_Code='NUL', Pla_Id=1, Mean=0.000000000000, Variance=0.000000000000, StdDev=0.000000000000, Min=0.000000000000, Max=0.000000000000):
        self.CU_Id                  = CU_Id
        self.From                   = From
        self.To                     = To
        self.Total_Slices           = Total_Slices
        self.Found_Slices           = Found_Slices
        self.Not_Found_Slices       = Not_Found_Slices
        self.Period_Initial_Q       = Period_Initial_Q
        self.Period_Increase        = Period_Increase
        self.Period_Increase_Count  = Period_Increase_Count
        self.Period_Reduction       = Period_Reduction
        self.Period_Reduction_Count = Period_Reduction_Count
        self.Period_Final_Q         = Period_Final_Q
        self.CI_Id                  = CI_Id
        self.CC_Id                  = CC_Id
        self.Cus_Id                 = Cus_Id
        self.Rat_Id                 = Rat_Id
        self.Typ_Code               = Typ_Code
        self.Pla_Id                 = Pla_Id
        self.Mean                   = Mean
        self.Variance               = Variance
        self.StdDev                 = StdDev
        self.Min                    = Min
        self.Max                    = Max

    def __repr__(self):
        return "<ST_Use_Per_CU( CU_Id='%s', From='%s', To='%s', Total_Slices='%s', Found_Slices='%s', Not_Found_Slices='%s', Period_Initial_Q='%s', Period_Increase='%s', Period_Increase_Count='%s', Period_Reduction='%s', Period_Reduction_Count='%s', Period_Final_Q='%s', CI_Id='%s', CC_Id='%s', Cus_Id='%s', Rat_Id='%s', Typ_Code='%s', Pla_Id='%s', Mean='%s', Variance='%s', StdDev='%s', Min='%s', Max='%s')>" % \
                ( self.CU_Id, self.From, self.To, self.Total_Slices, self.Found_Slices, self.Not_Found_Slices, self.Period_Initial_Q, self.Period_Increase, self.Period_Increase_Count, self.Period_Reduction, self.Period_Reduction_Count, self.Period_Final_Q, self.CI_Id, self.CC_Id, self.Cus_Id, self.Rat_Id, self.Typ_Code, self.Pla_Id, self.Mean, self.Variance, self.StdDev, self.Min, self.Max)

# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2022-03-07 18:58:14
# =============================================================================

# gen_model_flask.py:117 => /home/gvalera/GIT/EG-Suite-Tools/Collector/code/auto/models/flask_st_use_per_type.py
class st_use_per_type(db.Model,Serializer):
    __tablename__ = 'ST_Use_Per_Type'

    def check_shard(suffix=None,engine=None):
       if engine is not None:
           try:
               if not engine.dialect.has_table(engine, __class__.__tablename__):
                   print(f'131 Table {__class__.__tablename__} does not exist')
                   metadata=MetaData()
                   metadata.bind=engine
                   __class__.__table__.metadata=metadata
                   __class__.__table__.create(checkfirst=True)
                   if not engine.dialect.has_table(engine, __class__.__tablename__):
                       print('137 Table %s does not exist. creation error?'% __class__.__tablename__)
                   else:
                       print('139 Table %s exist !!!'% __class__.__tablename__)
               else:
                   pass # GV print('141 Table %s exist !!!'% __class__.__tablename__)
           except Exception as e:
              print(f'143 exception: {str(e)}')
           return
    def set_shard(suffix=None,engine=None):
       if suffix is not None:
           name='ST_Use_Per_Type_{suffix}'.format(suffix=suffix)
           __class__.__tablename__  = name
           __class__.__table__.name = name
       __class__.check_shard(suffix,engine)
       return __class__.__tablename__

    Typ_Code = db.Column( db.String(10), primary_key=True )
    Cus_Id   = db.Column( db.Integer, primary_key=True, default=1 )
    Pla_Id   = db.Column( db.Integer, primary_key=True, default=1 )
    CC_Id    = db.Column( db.Integer, primary_key=True, default=1 )
    CI_Id    = db.Column( db.Integer, primary_key=True, default=1 )
    Year     = db.Column( db.Integer, primary_key=True )
    Month    = db.Column( db.Integer, primary_key=True )
    Count    = db.Column( db.Integer, default=0 )
    Mean     = db.Column( db.Numeric(20,12), default=0.000000000000 )
    Variance = db.Column( db.Numeric(20,12), default=0.000000000000 )
    StdDev   = db.Column( db.Numeric(20,12), default=0.000000000000 )
    Min      = db.Column( db.Numeric(20,12), default=0.000000000000 )
    Max      = db.Column( db.Numeric(20,12), default=0.000000000000 )


    # looking for include file: /home/gvalera/GIT/EG-Suite-Tools/Collector/code/src/include/models/flask_st_use_per_type_properties.py
    # file: /home/gvalera/GIT/EG-Suite-Tools/Collector/code/src/include/models/flask_st_use_per_type_properties.py not found
    def __init__(self, Typ_Code='None', Cus_Id=1, Pla_Id=1, CC_Id=1, CI_Id=1, Year=None, Month=None, Count=0, Mean=0.000000000000, Variance=0.000000000000, StdDev=0.000000000000, Min=0.000000000000, Max=0.000000000000):
        self.Typ_Code = Typ_Code
        self.Cus_Id   = Cus_Id
        self.Pla_Id   = Pla_Id
        self.CC_Id    = CC_Id
        self.CI_Id    = CI_Id
        self.Year     = Year
        self.Month    = Month
        self.Count    = Count
        self.Mean     = Mean
        self.Variance = Variance
        self.StdDev   = StdDev
        self.Min      = Min
        self.Max      = Max

    def __repr__(self):
        return "<ST_Use_Per_Type( Typ_Code='%s', Cus_Id='%s', Pla_Id='%s', CC_Id='%s', CI_Id='%s', Year='%s', Month='%s', Count='%s', Mean='%s', Variance='%s', StdDev='%s', Min='%s', Max='%s')>" % \
                ( self.Typ_Code, self.Cus_Id, self.Pla_Id, self.CC_Id, self.CI_Id, self.Year, self.Month, self.Count, self.Mean, self.Variance, self.StdDev, self.Min, self.Max)

# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2020-10-18 20:12:04
# =============================================================================

# gen_model_flask.py:115 => /home/gvalera/GIT/EG-Suite-Tools/Collector/code/auto/models/flask_trace_202003.py
class trace_202003(db.Model,Serializer):
    __tablename__ = 'Trace_202003'

    def set_shard(suffix=None):
       if suffix is not None:
           name='Trace_202003_{suffix}'.format(suffix=suffix)
           __class__.__tablename__  = name
           __class__.__table__.name = name
       return __class__.__tablename__

    ID   = db.Column( db.Integer, primary_key=True, autoincrement=True )
    LINE = db.Column( db.String(128) )


    # looking for include file: /home/gvalera/GIT/EG-Suite-Tools/Collector/code/src/include/models/flask_trace_202003_properties.py
    # file: /home/gvalera/GIT/EG-Suite-Tools/Collector/code/src/include/models/flask_trace_202003_properties.py not found
    def __init__(self, ID=0, LINE='None'):
        self.ID   = ID
        self.LINE = LINE

    def __repr__(self):
        return "<Trace_202003( ID='%s', LINE='%s')>" % \
                ( self.ID, self.LINE)

# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2020-10-18 20:12:04
# =============================================================================

# gen_model_flask.py:670 => /home/gvalera/GIT/EG-Suite-Tools/Collector/code/auto/models/flask_trace_202003.py
def get_trace_202003(table_name_suffix):
  # gen_model_flask.py:678 =>/home/gvalera/GIT/EG-Suite-Tools/Collector/code/auto/models/flask_trace_202003.py
  class trace_202003_Class(db.Model,Serializer):
    __tablename__ = 'Trace_202003_%s'%(table_name_suffix)

    def set_shard(suffix=None):
        if suffix is not None:
           name='Trace_202003_{suffix}'.format(suffix=suffix)
           __class__.__tablename__  = name
           __class__.__table__.name = name
        return __class__.__tablename__

    ID   = db.Column( db.Integer, primary_key=True, autoincrement=True )
    LINE = db.Column( db.String(128) )


    def __init__(self, ID=0, LINE='None'):
        self.ID   = ID
        self.LINE = LINE

    def __repr__(self):
        return "<Trace_202003( ID='%s', LINE='%s')>" % \
                ( self.ID, self.LINE)

  trace_202003_Class.__name__ = 'trace_202003_%s'%(table_name_suffix)
  return trace_202003_Class
  # gen_model_flask.py 801 => /home/gvalera/GIT/EG-Suite-Tools/Collector/code/auto/models/flask_trace_202003.py
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2020-10-18 20:12:04
# =============================================================================

# gen_model_flask.py:115 => /home/gvalera/GIT/EG-Suite-Tools/Collector/code/auto/models/flask_trace_202101.py
class trace_202101(db.Model,Serializer):
    __tablename__ = 'Trace_202101'

    def set_shard(suffix=None):
       if suffix is not None:
           name='Trace_202101_{suffix}'.format(suffix=suffix)
           __class__.__tablename__  = name
           __class__.__table__.name = name
       return __class__.__tablename__

    ID   = db.Column( db.Integer, primary_key=True, autoincrement=True )
    LINE = db.Column( db.String(128) )


    # looking for include file: /home/gvalera/GIT/EG-Suite-Tools/Collector/code/src/include/models/flask_trace_202101_properties.py
    # file: /home/gvalera/GIT/EG-Suite-Tools/Collector/code/src/include/models/flask_trace_202101_properties.py not found
    def __init__(self, ID=0, LINE='None'):
        self.ID   = ID
        self.LINE = LINE

    def __repr__(self):
        return "<Trace_202101( ID='%s', LINE='%s')>" % \
                ( self.ID, self.LINE)

# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2020-10-18 20:12:04
# =============================================================================

# gen_model_flask.py:670 => /home/gvalera/GIT/EG-Suite-Tools/Collector/code/auto/models/flask_trace_202101.py
def get_trace_202101(table_name_suffix):
  # gen_model_flask.py:678 =>/home/gvalera/GIT/EG-Suite-Tools/Collector/code/auto/models/flask_trace_202101.py
  class trace_202101_Class(db.Model,Serializer):
    __tablename__ = 'Trace_202101_%s'%(table_name_suffix)

    def set_shard(suffix=None):
        if suffix is not None:
           name='Trace_202101_{suffix}'.format(suffix=suffix)
           __class__.__tablename__  = name
           __class__.__table__.name = name
        return __class__.__tablename__

    ID   = db.Column( db.Integer, primary_key=True, autoincrement=True )
    LINE = db.Column( db.String(128) )


    def __init__(self, ID=0, LINE='None'):
        self.ID   = ID
        self.LINE = LINE

    def __repr__(self):
        return "<Trace_202101( ID='%s', LINE='%s')>" % \
                ( self.ID, self.LINE)

  trace_202101_Class.__name__ = 'trace_202101_%s'%(table_name_suffix)
  return trace_202101_Class
  # gen_model_flask.py 801 => /home/gvalera/GIT/EG-Suite-Tools/Collector/code/auto/models/flask_trace_202101.py
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2022-03-07 18:58:14
# =============================================================================

# gen_model_flask.py:117 => /home/gvalera/GIT/EG-Suite-Tools/Collector/code/auto/models/flask_trace.py
class trace(db.Model,Serializer):
    __tablename__ = 'Trace'

    def check_shard(suffix=None,engine=None):
       if engine is not None:
           try:
               if not engine.dialect.has_table(engine, __class__.__tablename__):
                   print(f'131 Table {__class__.__tablename__} does not exist')
                   metadata=MetaData()
                   metadata.bind=engine
                   __class__.__table__.metadata=metadata
                   __class__.__table__.create(checkfirst=True)
                   if not engine.dialect.has_table(engine, __class__.__tablename__):
                       print('137 Table %s does not exist. creation error?'% __class__.__tablename__)
                   else:
                       print('139 Table %s exist !!!'% __class__.__tablename__)
               else:
                   pass # GV print('141 Table %s exist !!!'% __class__.__tablename__)
           except Exception as e:
              print(f'143 exception: {str(e)}')
           return
    def set_shard(suffix=None,engine=None):
       if suffix is not None:
           name='Trace_{suffix}'.format(suffix=suffix)
           __class__.__tablename__  = name
           __class__.__table__.name = name
       __class__.check_shard(suffix,engine)
       return __class__.__tablename__

    ID   = db.Column( db.Integer, primary_key=True, autoincrement=True )
    LINE = db.Column( db.String(128) )


    # looking for include file: /home/gvalera/GIT/EG-Suite-Tools/Collector/code/src/include/models/flask_trace_properties.py
    # file: /home/gvalera/GIT/EG-Suite-Tools/Collector/code/src/include/models/flask_trace_properties.py not found
    def __init__(self, ID=0, LINE='None'):
        self.ID   = ID
        self.LINE = LINE

    def __repr__(self):
        return "<Trace( ID='%s', LINE='%s')>" % \
                ( self.ID, self.LINE)

# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2022-03-07 18:58:14
# =============================================================================

# gen_model_flask.py:117 => /home/gvalera/GIT/EG-Suite-Tools/Collector/code/auto/models/flask_user_resumes.py
class user_resumes(db.Model,Serializer):
    __tablename__ = 'User_Resumes'

    def check_shard(suffix=None,engine=None):
       if engine is not None:
           try:
               if not engine.dialect.has_table(engine, __class__.__tablename__):
                   print(f'131 Table {__class__.__tablename__} does not exist')
                   metadata=MetaData()
                   metadata.bind=engine
                   __class__.__table__.metadata=metadata
                   __class__.__table__.create(checkfirst=True)
                   if not engine.dialect.has_table(engine, __class__.__tablename__):
                       print('137 Table %s does not exist. creation error?'% __class__.__tablename__)
                   else:
                       print('139 Table %s exist !!!'% __class__.__tablename__)
               else:
                   pass # GV print('141 Table %s exist !!!'% __class__.__tablename__)
           except Exception as e:
              print(f'143 exception: {str(e)}')
           return
    def set_shard(suffix=None,engine=None):
       if suffix is not None:
           name='User_Resumes_{suffix}'.format(suffix=suffix)
           __class__.__tablename__  = name
           __class__.__table__.name = name
       __class__.check_shard(suffix,engine)
       return __class__.__tablename__

    User_Id                = db.Column( db.Integer, primary_key=True )
    Cus_Id                 = db.Column( db.Integer )
    CR_Date_From           = db.Column( db.Date, primary_key=True )
    CR_Date_To             = db.Column( db.Date, primary_key=True )
    CIT_Status             = db.Column( db.Integer, primary_key=True )
    Cur_Code               = db.Column( db.String(3), primary_key=True )
    CU_Id                  = db.Column( db.Integer, primary_key=True )
    CIT_Count              = db.Column( db.Integer )
    CIT_Quantity           = db.Column( db.Numeric(20,12) )
    CIT_Generation         = db.Column( db.Integer, default=1 )
    CI_CC_Id               = db.Column( db.Integer )
    CU_Operation           = db.Column( db.String(10) )
    Typ_Code               = db.Column( db.String(10) )
    CC_Cur_Code            = db.Column( db.String(3) )
    CI_Id                  = db.Column( db.Integer, primary_key=True )
    Rat_Id                 = db.Column( db.Integer )
    Rat_Price              = db.Column( db.Numeric(20,12) )
    Rat_MU_Code            = db.Column( db.String(3) )
    Rat_Cur_Code           = db.Column( db.String(3) )
    Rat_Period             = db.Column( db.Integer )
    Rat_Hourly             = db.Column( db.Numeric(20,12) )
    Rat_Daily              = db.Column( db.Numeric(20,12) )
    Rat_Monthly            = db.Column( db.Numeric(20,12) )
    CR_Quantity            = db.Column( db.Numeric(20,12) )
    CR_Quantity_at_Rate    = db.Column( db.Numeric(20,12) )
    CC_XR                  = db.Column( db.Numeric(20,12) )
    CR_Cur_XR              = db.Column( db.Numeric(20,12) )
    CR_ST_at_Rate_Cur      = db.Column( db.Numeric(20,12) )
    CR_ST_at_CC_Cur        = db.Column( db.Numeric(20,12) )
    CR_ST_at_Cur           = db.Column( db.Numeric(20,12) )
    Cus_Name               = db.Column( db.String(255) )
    CI_Name                = db.Column( db.String(255) )
    CU_Description         = db.Column( db.String(255) )
    CC_Description         = db.Column( db.String(255) )
    Rat_Period_Description = db.Column( db.String(10) )
    CC_Code                = db.Column( db.String(45) )
    Pla_Id                 = db.Column( db.Integer )
    Pla_Name               = db.Column( db.String(255) )


    # looking for include file: /home/gvalera/GIT/EG-Suite-Tools/Collector/code/src/include/models/flask_user_resumes_properties.py
    # file: /home/gvalera/GIT/EG-Suite-Tools/Collector/code/src/include/models/flask_user_resumes_properties.py not found
    def __init__(self, User_Id=None, Cus_Id=None, CR_Date_From=None, CR_Date_To=None, CIT_Status=None, Cur_Code='None', CU_Id=None, CIT_Count=None, CIT_Quantity=None, CIT_Generation=1, CI_CC_Id=None, CU_Operation='None', Typ_Code='None', CC_Cur_Code='None', CI_Id=None, Rat_Id=None, Rat_Price=None, Rat_MU_Code='None', Rat_Cur_Code='None', Rat_Period=None, Rat_Hourly=None, Rat_Daily=None, Rat_Monthly=None, CR_Quantity=None, CR_Quantity_at_Rate=None, CC_XR=None, CR_Cur_XR=None, CR_ST_at_Rate_Cur=None, CR_ST_at_CC_Cur=None, CR_ST_at_Cur=None, Cus_Name='None', CI_Name='None', CU_Description='None', CC_Description='None', Rat_Period_Description='None', CC_Code='None', Pla_Id=None, Pla_Name='None'):
        self.User_Id                = User_Id
        self.Cus_Id                 = Cus_Id
        self.CR_Date_From           = CR_Date_From
        self.CR_Date_To             = CR_Date_To
        self.CIT_Status             = CIT_Status
        self.Cur_Code               = Cur_Code
        self.CU_Id                  = CU_Id
        self.CIT_Count              = CIT_Count
        self.CIT_Quantity           = CIT_Quantity
        self.CIT_Generation         = CIT_Generation
        self.CI_CC_Id               = CI_CC_Id
        self.CU_Operation           = CU_Operation
        self.Typ_Code               = Typ_Code
        self.CC_Cur_Code            = CC_Cur_Code
        self.CI_Id                  = CI_Id
        self.Rat_Id                 = Rat_Id
        self.Rat_Price              = Rat_Price
        self.Rat_MU_Code            = Rat_MU_Code
        self.Rat_Cur_Code           = Rat_Cur_Code
        self.Rat_Period             = Rat_Period
        self.Rat_Hourly             = Rat_Hourly
        self.Rat_Daily              = Rat_Daily
        self.Rat_Monthly            = Rat_Monthly
        self.CR_Quantity            = CR_Quantity
        self.CR_Quantity_at_Rate    = CR_Quantity_at_Rate
        self.CC_XR                  = CC_XR
        self.CR_Cur_XR              = CR_Cur_XR
        self.CR_ST_at_Rate_Cur      = CR_ST_at_Rate_Cur
        self.CR_ST_at_CC_Cur        = CR_ST_at_CC_Cur
        self.CR_ST_at_Cur           = CR_ST_at_Cur
        self.Cus_Name               = Cus_Name
        self.CI_Name                = CI_Name
        self.CU_Description         = CU_Description
        self.CC_Description         = CC_Description
        self.Rat_Period_Description = Rat_Period_Description
        self.CC_Code                = CC_Code
        self.Pla_Id                 = Pla_Id
        self.Pla_Name               = Pla_Name

    def __repr__(self):
        return "<User_Resumes( User_Id='%s', Cus_Id='%s', CR_Date_From='%s', CR_Date_To='%s', CIT_Status='%s', Cur_Code='%s', CU_Id='%s', CIT_Count='%s', CIT_Quantity='%s', CIT_Generation='%s', CI_CC_Id='%s', CU_Operation='%s', Typ_Code='%s', CC_Cur_Code='%s', CI_Id='%s', Rat_Id='%s', Rat_Price='%s', Rat_MU_Code='%s', Rat_Cur_Code='%s', Rat_Period='%s', Rat_Hourly='%s', Rat_Daily='%s', Rat_Monthly='%s', CR_Quantity='%s', CR_Quantity_at_Rate='%s', CC_XR='%s', CR_Cur_XR='%s', CR_ST_at_Rate_Cur='%s', CR_ST_at_CC_Cur='%s', CR_ST_at_Cur='%s', Cus_Name='%s', CI_Name='%s', CU_Description='%s', CC_Description='%s', Rat_Period_Description='%s', CC_Code='%s', Pla_Id='%s', Pla_Name='%s')>" % \
                ( self.User_Id, self.Cus_Id, self.CR_Date_From, self.CR_Date_To, self.CIT_Status, self.Cur_Code, self.CU_Id, self.CIT_Count, self.CIT_Quantity, self.CIT_Generation, self.CI_CC_Id, self.CU_Operation, self.Typ_Code, self.CC_Cur_Code, self.CI_Id, self.Rat_Id, self.Rat_Price, self.Rat_MU_Code, self.Rat_Cur_Code, self.Rat_Period, self.Rat_Hourly, self.Rat_Daily, self.Rat_Monthly, self.CR_Quantity, self.CR_Quantity_at_Rate, self.CC_XR, self.CR_Cur_XR, self.CR_ST_at_Rate_Cur, self.CR_ST_at_CC_Cur, self.CR_ST_at_Cur, self.Cus_Name, self.CI_Name, self.CU_Description, self.CC_Description, self.Rat_Period_Description, self.CC_Code, self.Pla_Id, self.Pla_Name)

# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2022-03-07 18:58:14
# =============================================================================

# gen_model_flask.py:117 => /home/gvalera/GIT/EG-Suite-Tools/Collector/code/auto/models/flask_users.py
class User(UserMixin, db.Model,Serializer):
    __tablename__ = 'Users'

    def check_shard(suffix=None,engine=None):
       if engine is not None:
           try:
               if not engine.dialect.has_table(engine, __class__.__tablename__):
                   print(f'131 Table {__class__.__tablename__} does not exist')
                   metadata=MetaData()
                   metadata.bind=engine
                   __class__.__table__.metadata=metadata
                   __class__.__table__.create(checkfirst=True)
                   if not engine.dialect.has_table(engine, __class__.__tablename__):
                       print('137 Table %s does not exist. creation error?'% __class__.__tablename__)
                   else:
                       print('139 Table %s exist !!!'% __class__.__tablename__)
               else:
                   pass # GV print('141 Table %s exist !!!'% __class__.__tablename__)
           except Exception as e:
              print(f'143 exception: {str(e)}')
           return
    def set_shard(suffix=None,engine=None):
       if suffix is not None:
           name='Users_{suffix}'.format(suffix=suffix)
           __class__.__tablename__  = name
           __class__.__table__.name = name
       __class__.check_shard(suffix,engine)
       return __class__.__tablename__

    id            = db.Column( db.Integer, primary_key=True, autoincrement=True )
    username      = db.Column( db.String(64) )
    role_id       = db.Column( db.Integer, db.ForeignKey('Roles.id') )
    email         = db.Column( db.String(64) )
    password_hash = db.Column( db.String(128) )
    confirmed     = db.Column( db.Boolean, default=0 )
    CC_Id         = db.Column( db.Integer, db.ForeignKey('Cost_Centers.CC_Id'), default=1 )


    # looking for include file: /home/gvalera/GIT/EG-Suite-Tools/Collector/code/src/include/models/flask_users_properties.py
    # file: /home/gvalera/GIT/EG-Suite-Tools/Collector/code/src/include/models/flask_users_properties.py not found
    # source: code/src/include/models/flask_users_methods.py
    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        ''' 20210614 GV Chance to define role at once
        if self.role is None:
            if self.username == current_app.config['COLLECTOR_ADMIN']:
                self.role = Role.query.filter_by(permissions=0xfe).first()
            if self.role is None:
                self.role = Role.query.filter_by(default=True).first()
        ''' 
        if self.role_id is None:
            if self.role is None:
                if self.username == current_app.config['COLLECTOR_ADMIN']:
                    self.role = Role.query.filter_by(permissions=0xfe).first()
                if self.role is None:
                    self.role = Role.query.filter_by(default=True).first()
        else:
            self.role = Role.query.filter_by(id=self.role_id).first()
    
    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def generate_confirmation_token(self, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'confirm': self.id})

    def confirm(self, token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        if data.get('confirm') != self.id:
            return False
        self.confirmed = True
        db.session.add(self)
        return True

    def generate_reset_token(self, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'reset': self.id})

    def reset_password(self, token, new_password):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        if data.get('reset') != self.id:
            return False
        self.password = new_password
        db.session.add(self)
        return True

    def generate_email_change_token(self, new_email, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'change_email': self.id, 'new_email': new_email})

    def change_email(self, token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        if data.get('change_email') != self.id:
            return False
        new_email = data.get('new_email')
        if new_email is None:
            return False
        if self.query.filter_by(email=new_email).first() is not None:
            return False
        self.email = new_email
        db.session.add(self)
        return True

    def can(self, permissions):
        return self.role is not None and \
            (self.role.permissions & permissions) == permissions

    def is_administrator(self):
        return self.can(Permission.ADMINISTER)

    def is_god(self):
        return self.can(Permission.GOD)

    def is_customer(self):
        return self.can(Permission.CUSTOMER)

    def __repr__(self):
        return '<User %r role=%r>' % (self.username,self.role)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
        print(f"password: password                    = {password}")
        print(f"password: self.password_hash          = {self.password_hash}")
        print(f"password: verify_password({password}) = {self.verify_password(password)}")

    def verify_password(self, password):
        #print(f"verify_password: verify_password({password}) = {self.verify_password(password)}")
        return check_password_hash(self.password_hash, password)

    def generate_confirmation_token(self, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'confirm': self.id})

    def confirm(self, token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        if data.get('confirm') != self.id:
            return False
        self.confirmed = True
        db.session.add(self)
        return True

    def generate_reset_token(self, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'reset': self.id})

    def reset_password(self, token, new_password):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        if data.get('reset') != self.id:
            return False
        self.password = new_password
        db.session.add(self)
        return True

    def generate_email_change_token(self, new_email, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'change_email': self.id, 'new_email': new_email})

    def change_email(self, token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        if data.get('change_email') != self.id:
            return False
        new_email = data.get('new_email')
        if new_email is None:
            return False
        if self.query.filter_by(email=new_email).first() is not None:
            return False
        self.email = new_email
        db.session.add(self)
        return True

    def can(self, permissions):
        return self.role is not None and \
            (self.role.permissions & permissions) == permissions

    def is_administrator(self):
        return self.can(Permission.ADMINISTER)

    def is_god(self):
        return self.can(Permission.GOD)

    def is_customer(self):
        return self.can(Permission.CUSTOMER)

    def __repr__(self):
        return '<User %r role=%r>' % (self.username,self.role)

