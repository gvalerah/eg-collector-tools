# =============================================================================
# Models File
# Static Header File. 
# GLVH 2019-08-16
# =============================================================================
from app                    import db
from app                    import login_manager

from datetime               import datetime

from sqlalchemy             import Column, String, Integer, Numeric, Date, Time, Boolean, DateTime
from sqlalchemy             import ForeignKey

from flask_sqlalchemy       import SQLAlchemy
from copy                   import copy, deepcopy

# Required form Authorization subsystem
from werkzeug.security      import generate_password_hash, check_password_hash
from itsdangerous           import TimedJSONWebSignatureSerializer as Serializer
from flask                  import current_app
from flask_login            import UserMixin, AnonymousUserMixin



# =============================================================================
# Models File
# Authorization subsystem. 
# Static File. 
# GLVH 2018-12-17
# =============================================================================

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
# GLVH @ 2019-08-18 18:05:34
# =============================================================================

class charge_item(db.Model):
    __tablename__ = 'Charge_Items'
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

# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-18 18:05:34
# =============================================================================

class charge_resume(db.Model):
    __tablename__ = 'Charge_Resumes'
    Cus_Id                 = db.Column( db.Integer, primary_key=True )
    CR_Date_From           = db.Column( db.Date, primary_key=True )
    CR_Date_To             = db.Column( db.Date, primary_key=True )
    CIT_Status             = db.Column( db.Integer, primary_key=True )
    Cur_Code               = db.Column( db.String(3), primary_key=True )
    CIT_Count              = db.Column( db.Integer )
    CIT_Quantity           = db.Column( db.Numeric(20,6) )
    CIT_Generation         = db.Column( db.Integer, default=1 )
    CU_Id                  = db.Column( db.Integer, primary_key=True )
    CI_CC_Id               = db.Column( db.Integer )
    CU_Operation           = db.Column( db.String(10) )
    Typ_Code               = db.Column( db.String(10) )
    CC_Cur_Code            = db.Column( db.String(3) )
    CI_Id                  = db.Column( db.Integer )
    Rat_Id                 = db.Column( db.Integer )
    Rat_Price              = db.Column( db.Numeric(20,6) )
    Rat_MU_Code            = db.Column( db.String(3) )
    Rat_Cur_Code           = db.Column( db.String(3) )
    Rat_Period             = db.Column( db.Integer )
    Rat_Hourly             = db.Column( db.Numeric(20,6) )
    Rat_Daily              = db.Column( db.Numeric(20,6) )
    Rat_Monthly            = db.Column( db.Numeric(20,6) )
    CR_Quantity            = db.Column( db.Numeric(20,6) )
    CR_Quantity_at_Rate    = db.Column( db.Numeric(20,6) )
    CC_XR                  = db.Column( db.Numeric(20,10) )
    CR_Cur_XR              = db.Column( db.Numeric(20,10) )
    CR_ST_at_Rate_Cur      = db.Column( db.Numeric(20,6) )
    CR_ST_at_CC_Cur        = db.Column( db.Numeric(20,6) )
    CR_ST_at_Cur           = db.Column( db.Numeric(20,6) )
    Cus_Name               = db.Column( db.String(45) )
    CI_Name                = db.Column( db.String(45) )
    CU_Description         = db.Column( db.String(45) )
    CC_Description         = db.Column( db.String(45) )
    Rat_Period_Description = db.Column( db.String(10) )
    Pla_Id                 = db.Column( db.Integer )


    def __init__(self, Cus_Id=None, CR_Date_From=None, CR_Date_To=None, CIT_Status=None, Cur_Code='None', CIT_Count=None, CIT_Quantity=None, CIT_Generation=1, CU_Id=None, CI_CC_Id=None, CU_Operation='None', Typ_Code='None', CC_Cur_Code='None', CI_Id=None, Rat_Id=None, Rat_Price=None, Rat_MU_Code='None', Rat_Cur_Code='None', Rat_Period=None, Rat_Hourly=None, Rat_Daily=None, Rat_Monthly=None, CR_Quantity=None, CR_Quantity_at_Rate=None, CC_XR=None, CR_Cur_XR=None, CR_ST_at_Rate_Cur=None, CR_ST_at_CC_Cur=None, CR_ST_at_Cur=None, Cus_Name='None', CI_Name='None', CU_Description='None', CC_Description='None', Rat_Period_Description='None', Pla_Id=None):
        self.Cus_Id                 = Cus_Id
        self.CR_Date_From           = CR_Date_From
        self.CR_Date_To             = CR_Date_To
        self.CIT_Status             = CIT_Status
        self.Cur_Code               = Cur_Code
        self.CIT_Count              = CIT_Count
        self.CIT_Quantity           = CIT_Quantity
        self.CIT_Generation         = CIT_Generation
        self.CU_Id                  = CU_Id
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
        self.Pla_Id                 = Pla_Id

    def __repr__(self):
        return "<Charge_Resumes( Cus_Id='%s', CR_Date_From='%s', CR_Date_To='%s', CIT_Status='%s', Cur_Code='%s', CIT_Count='%s', CIT_Quantity='%s', CIT_Generation='%s', CU_Id='%s', CI_CC_Id='%s', CU_Operation='%s', Typ_Code='%s', CC_Cur_Code='%s', CI_Id='%s', Rat_Id='%s', Rat_Price='%s', Rat_MU_Code='%s', Rat_Cur_Code='%s', Rat_Period='%s', Rat_Hourly='%s', Rat_Daily='%s', Rat_Monthly='%s', CR_Quantity='%s', CR_Quantity_at_Rate='%s', CC_XR='%s', CR_Cur_XR='%s', CR_ST_at_Rate_Cur='%s', CR_ST_at_CC_Cur='%s', CR_ST_at_Cur='%s', Cus_Name='%s', CI_Name='%s', CU_Description='%s', CC_Description='%s', Rat_Period_Description='%s', Pla_Id='%s')>" % \
                ( self.Cus_Id, self.CR_Date_From, self.CR_Date_To, self.CIT_Status, self.Cur_Code, self.CIT_Count, self.CIT_Quantity, self.CIT_Generation, self.CU_Id, self.CI_CC_Id, self.CU_Operation, self.Typ_Code, self.CC_Cur_Code, self.CI_Id, self.Rat_Id, self.Rat_Price, self.Rat_MU_Code, self.Rat_Cur_Code, self.Rat_Period, self.Rat_Hourly, self.Rat_Daily, self.Rat_Monthly, self.CR_Quantity, self.CR_Quantity_at_Rate, self.CC_XR, self.CR_Cur_XR, self.CR_ST_at_Rate_Cur, self.CR_ST_at_CC_Cur, self.CR_ST_at_Cur, self.Cus_Name, self.CI_Name, self.CU_Description, self.CC_Description, self.Rat_Period_Description, self.Pla_Id)

# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-18 18:05:34
# =============================================================================

class charge_unit(db.Model):
    __tablename__ = 'Charge_Units'
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

    charge_items           = db.relationship('charge_item',backref='charge_unit')

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
# GLVH @ 2019-08-18 18:05:34
# =============================================================================

class cit_generation(db.Model):
    __tablename__ = 'CIT_Generations'
    CIT_Generation = db.Column( db.Integer, primary_key=True )
    Value          = db.Column( db.String(45) )

    charge_units   = db.relationship('charge_unit',backref='cit_generation')

    def __init__(self, CIT_Generation=None, Value='None'):
        self.CIT_Generation = CIT_Generation
        self.Value          = Value

    def __repr__(self):
        return "<CIT_Generations( CIT_Generation='%s', Value='%s')>" % \
                ( self.CIT_Generation, self.Value)

# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-18 18:05:34
# =============================================================================

class cit_status(db.Model):
    __tablename__ = 'CIT_Statuses'
    CIT_Status = db.Column( db.Integer, primary_key=True )
    Value      = db.Column( db.String(45) )

    charge_items = db.relationship('charge_item',backref='cit_status')

    def __init__(self, CIT_Status=None, Value='None'):
        self.CIT_Status = CIT_Status
        self.Value      = Value

    def __repr__(self):
        return "<CIT_Statuses( CIT_Status='%s', Value='%s')>" % \
                ( self.CIT_Status, self.Value)

# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-18 18:05:34
# =============================================================================

class configuration_item(db.Model):
    __tablename__ = 'Configuration_Items'
    CI_Id                       = db.Column( db.Integer, primary_key=True, autoincrement=True )
    CI_Name                     = db.Column( db.String(45) )
    CI_UUID                     = db.Column( db.String(45) )
    Pla_Id                      = db.Column( db.Integer, db.ForeignKey('Platforms.Pla_Id') )
    CC_Id                       = db.Column( db.Integer, db.ForeignKey('Cost_Centers.CC_Id') )
    Cus_Id                      = db.Column( db.Integer, db.ForeignKey('Customers.Cus_Id'), default=1 )
    CI_Commissioning_DateTime   = db.Column( db.DateTime )
    CI_Decommissioning_DateTime = db.Column( db.DateTime )

    charge_units                = db.relationship('charge_unit',backref='configuration_item')
    rates                       = db.relationship('rate',backref='configuration_item')

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
# GLVH @ 2019-08-18 18:05:34
# =============================================================================

class cost_center(db.Model):
    __tablename__ = 'Cost_Centers'
    CC_Id          = db.Column( db.Integer, primary_key=True, autoincrement=True )
    CC_Code        = db.Column( db.String(45) )
    CC_Description = db.Column( db.String(45) )
    Cur_Code       = db.Column( db.String(3), db.ForeignKey('Currencies.Cur_Code') )
    CC_Parent_Code = db.Column( db.String(45), default='1' )

    configuration_items = db.relationship('configuration_item',backref='cost_center')
    customers      = db.relationship('customer',backref='cost_center')
    rates          = db.relationship('rate',backref='cost_center')
    users          = db.relationship('User',backref='cost_center')

    def __init__(self, CC_Id=0, CC_Code='None', CC_Description='None', Cur_Code='None', CC_Parent_Code='1'):
        self.CC_Id          = CC_Id
        self.CC_Code        = CC_Code
        self.CC_Description = CC_Description
        self.Cur_Code       = Cur_Code
        self.CC_Parent_Code = CC_Parent_Code

    def __repr__(self):
        return "<Cost_Centers( CC_Id='%s', CC_Code='%s', CC_Description='%s', Cur_Code='%s', CC_Parent_Code='%s')>" % \
                ( self.CC_Id, self.CC_Code, self.CC_Description, self.Cur_Code, self.CC_Parent_Code)

# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-18 18:05:34
# =============================================================================

class country_currency(db.Model):
    __tablename__ = 'Countries_Currencies'
    Cou_Code        = db.Column( db.String(2), db.ForeignKey('Countries.Cou_Code'), primary_key=True )
    Cur_Code        = db.Column( db.String(3), db.ForeignKey('Currencies.Cur_Code'), primary_key=True )
    Cou_Cur_Comment = db.Column( db.String(45) )


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
# GLVH @ 2019-08-18 18:05:34
# =============================================================================

class country(db.Model):
    __tablename__ = 'Countries'
    Cou_Code = db.Column( db.String(2), primary_key=True )
    Cou_Name = db.Column( db.String(45) )
    Cou_A3   = db.Column( db.String(3) )
    Cou_N    = db.Column( db.Integer )

    countries_currencies = db.relationship('country_currency',backref='country')

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
# GLVH @ 2019-08-18 18:05:34
# =============================================================================

class cu_operation(db.Model):
    __tablename__ = 'CU_Operations'
    CU_Operation = db.Column( db.String(10), primary_key=True )
    Value        = db.Column( db.String(45) )
    Is_Multiply  = db.Column( db.Boolean )
    Factor       = db.Column( db.Integer )

    charge_units = db.relationship('charge_unit',backref='cu_operation')

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
# GLVH @ 2019-08-18 18:05:34
# =============================================================================

class currency(db.Model):
    __tablename__ = 'Currencies'
    Cur_Code    = db.Column( db.String(3), primary_key=True )
    Cur_Name    = db.Column( db.String(45) )
    Cur_Id      = db.Column( db.Integer )
    Cur_Comment = db.Column( db.String(128) )

    cost_centers = db.relationship('cost_center',backref='currency')
    countries_currencies = db.relationship('country_currency',backref='currency')
    exchange_rates = db.relationship('exchange_rate',backref='currency')
    rates       = db.relationship('rate',backref='currency')

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
# GLVH @ 2019-08-18 18:05:34
# =============================================================================

class customer(db.Model):
    __tablename__ = 'Customers'
    Cus_Id   = db.Column( db.Integer, primary_key=True, autoincrement=True )
    Cus_Name = db.Column( db.String(45) )
    CC_Id    = db.Column( db.Integer, db.ForeignKey('Cost_Centers.CC_Id') )

    configuration_items = db.relationship('configuration_item',backref='customer')
    rates    = db.relationship('rate',backref='customer')

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
# GLVH @ 2019-08-18 18:05:34
# =============================================================================

class cu_type(db.Model):
    __tablename__ = 'CU_Types'
    Typ_Code        = db.Column( db.String(10), primary_key=True )
    Typ_Description = db.Column( db.String(45) )

    charge_units    = db.relationship('charge_unit',backref='cu_type')
    rates           = db.relationship('rate',backref='cu_type')

    def __init__(self, Typ_Code='None', Typ_Description='None'):
        self.Typ_Code        = Typ_Code
        self.Typ_Description = Typ_Description

    def __repr__(self):
        return "<CU_Types( Typ_Code='%s', Typ_Description='%s')>" % \
                ( self.Typ_Code, self.Typ_Description)

# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-18 18:05:34
# =============================================================================

class dev_form(db.Model):
    __tablename__ = 'Dev_Forms'
    Id                = db.Column( db.Integer, primary_key=True, autoincrement=True )
    Table             = db.Column( db.String(45) )
    Field             = db.Column( db.String(45) )
    Type              = db.Column( db.String(45) )
    Null              = db.Column( db.String(45) )
    Key               = db.Column( db.String(45) )
    Default           = db.Column( db.String(45) )
    Extra             = db.Column( db.String(45) )
    Foreign_Key       = db.Column( db.String(45) )
    Referenced_Table  = db.Column( db.String(45) )
    Foreign_Field     = db.Column( db.String(45) )
    Foreign_Value     = db.Column( db.String(45) )
    Length            = db.Column( db.Integer )
    Validation        = db.Column( db.Boolean )
    Validation_Type   = db.Column( db.String(45) )
    Validation_String = db.Column( db.String(128) )
    Caption_String    = db.Column( db.String(45) )
    Field_Order       = db.Column( db.Integer )
    Field_Format      = db.Column( db.String(45) )
    Form_Editable     = db.Column( db.Boolean, default=1 )
    ORM_Schema        = db.Column( db.Boolean, default=1 )


    def __init__(self, Id=0, Table='None', Field='None', Type='None', Null='None', Key='None', Default='None', Extra='None', Foreign_Key='None', Referenced_Table='None', Foreign_Field='None', Foreign_Value='None', Length=None, Validation=None, Validation_Type='None', Validation_String='None', Caption_String='None', Field_Order=None, Field_Format='None', Form_Editable=1, ORM_Schema=1):
        self.Id                = Id
        self.Table             = Table
        self.Field             = Field
        self.Type              = Type
        self.Null              = Null
        self.Key               = Key
        self.Default           = Default
        self.Extra             = Extra
        self.Foreign_Key       = Foreign_Key
        self.Referenced_Table  = Referenced_Table
        self.Foreign_Field     = Foreign_Field
        self.Foreign_Value     = Foreign_Value
        self.Length            = Length
        self.Validation        = Validation
        self.Validation_Type   = Validation_Type
        self.Validation_String = Validation_String
        self.Caption_String    = Caption_String
        self.Field_Order       = Field_Order
        self.Field_Format      = Field_Format
        self.Form_Editable     = Form_Editable
        self.ORM_Schema        = ORM_Schema

    def __repr__(self):
        return "<Dev_Forms( Id='%s', Table='%s', Field='%s', Type='%s', Null='%s', Key='%s', Default='%s', Extra='%s', Foreign_Key='%s', Referenced_Table='%s', Foreign_Field='%s', Foreign_Value='%s', Length='%s', Validation='%s', Validation_Type='%s', Validation_String='%s', Caption_String='%s', Field_Order='%s', Field_Format='%s', Form_Editable='%s', ORM_Schema='%s')>" % \
                ( self.Id, self.Table, self.Field, self.Type, self.Null, self.Key, self.Default, self.Extra, self.Foreign_Key, self.Referenced_Table, self.Foreign_Field, self.Foreign_Value, self.Length, self.Validation, self.Validation_Type, self.Validation_String, self.Caption_String, self.Field_Order, self.Field_Format, self.Form_Editable, self.ORM_Schema)

# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-18 18:05:34
# =============================================================================

class dev_table(db.Model):
    __tablename__ = 'Dev_Tables'
    Id                        = db.Column( db.Integer, primary_key=True, autoincrement=True )
    Name                      = db.Column( db.String(45) )
    Caption                   = db.Column( db.String(45) )
    Entity                    = db.Column( db.String(45) )
    Class_Name                = db.Column( db.String(45) )
    Child_Table               = db.Column( db.String(45) )
    Parent_Table              = db.Column( db.String(45) )
    Use_Pagination            = db.Column( db.Boolean )
    Use_Children_Pagination   = db.Column( db.Boolean )
    Generate_Form_One         = db.Column( db.Boolean )
    Generate_Form_All         = db.Column( db.Boolean )
    Generate_Form_Filter      = db.Column( db.Boolean )
    Generate_Children         = db.Column( db.Boolean )
    Generate_Foreign_Fields   = db.Column( db.Boolean )
    Permission_View           = db.Column( db.Boolean )
    Permission_Delete         = db.Column( db.Boolean )
    Permission_Modify         = db.Column( db.Boolean )
    Permission_Report         = db.Column( db.Boolean )
    Permission_Export         = db.Column( db.Boolean )
    Permission_View_Private   = db.Column( db.Boolean )
    Permission_Modify_Private = db.Column( db.Boolean )
    Permission_Administer     = db.Column( db.Boolean )


    def __init__(self, Id=0, Name='None', Caption='None', Entity='None', Class_Name='None', Child_Table='None', Parent_Table='None', Use_Pagination=None, Use_Children_Pagination=None, Generate_Form_One=None, Generate_Form_All=None, Generate_Form_Filter=None, Generate_Children=None, Generate_Foreign_Fields=None, Permission_View=None, Permission_Delete=None, Permission_Modify=None, Permission_Report=None, Permission_Export=None, Permission_View_Private=None, Permission_Modify_Private=None, Permission_Administer=None):
        self.Id                        = Id
        self.Name                      = Name
        self.Caption                   = Caption
        self.Entity                    = Entity
        self.Class_Name                = Class_Name
        self.Child_Table               = Child_Table
        self.Parent_Table              = Parent_Table
        self.Use_Pagination            = Use_Pagination
        self.Use_Children_Pagination   = Use_Children_Pagination
        self.Generate_Form_One         = Generate_Form_One
        self.Generate_Form_All         = Generate_Form_All
        self.Generate_Form_Filter      = Generate_Form_Filter
        self.Generate_Children         = Generate_Children
        self.Generate_Foreign_Fields   = Generate_Foreign_Fields
        self.Permission_View           = Permission_View
        self.Permission_Delete         = Permission_Delete
        self.Permission_Modify         = Permission_Modify
        self.Permission_Report         = Permission_Report
        self.Permission_Export         = Permission_Export
        self.Permission_View_Private   = Permission_View_Private
        self.Permission_Modify_Private = Permission_Modify_Private
        self.Permission_Administer     = Permission_Administer

    def __repr__(self):
        return "<Dev_Tables( Id='%s', Name='%s', Caption='%s', Entity='%s', Class_Name='%s', Child_Table='%s', Parent_Table='%s', Use_Pagination='%s', Use_Children_Pagination='%s', Generate_Form_One='%s', Generate_Form_All='%s', Generate_Form_Filter='%s', Generate_Children='%s', Generate_Foreign_Fields='%s', Permission_View='%s', Permission_Delete='%s', Permission_Modify='%s', Permission_Report='%s', Permission_Export='%s', Permission_View_Private='%s', Permission_Modify_Private='%s', Permission_Administer='%s')>" % \
                ( self.Id, self.Name, self.Caption, self.Entity, self.Class_Name, self.Child_Table, self.Parent_Table, self.Use_Pagination, self.Use_Children_Pagination, self.Generate_Form_One, self.Generate_Form_All, self.Generate_Form_Filter, self.Generate_Children, self.Generate_Foreign_Fields, self.Permission_View, self.Permission_Delete, self.Permission_Modify, self.Permission_Report, self.Permission_Export, self.Permission_View_Private, self.Permission_Modify_Private, self.Permission_Administer)

# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-18 18:05:34
# =============================================================================

class exchange_rate(db.Model):
    __tablename__ = 'Exchange_Rates'
    ER_Id     = db.Column( db.Integer, primary_key=True, autoincrement=True )
    Cur_Code  = db.Column( db.String(3), db.ForeignKey('Currencies.Cur_Code') )
    ER_Factor = db.Column( db.Numeric(20,10) )
    ER_Date   = db.Column( db.Date )


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
# GLVH @ 2019-08-18 18:05:34
# =============================================================================

class measure_unit(db.Model):
    __tablename__ = 'Measure_Units'
    MU_Code        = db.Column( db.String(3), primary_key=True )
    MU_Description = db.Column( db.String(45) )

    rates          = db.relationship('rate',backref='measure_unit')

    def __init__(self, MU_Code='None', MU_Description='None'):
        self.MU_Code        = MU_Code
        self.MU_Description = MU_Description

    def __repr__(self):
        return "<Measure_Units( MU_Code='%s', MU_Description='%s')>" % \
                ( self.MU_Code, self.MU_Description)

# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-18 18:05:34
# =============================================================================

class platform(db.Model):
    __tablename__ = 'Platforms'
    Pla_Id       = db.Column( db.Integer, primary_key=True, autoincrement=True )
    Pla_Name     = db.Column( db.String(45) )
    Pla_Host     = db.Column( db.String(45) )
    Pla_Port     = db.Column( db.String(45) )
    Pla_User     = db.Column( db.String(45) )
    Pla_Password = db.Column( db.String(45) )

    configuration_items = db.relationship('configuration_item',backref='platform')
    rates        = db.relationship('rate',backref='platform')

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
# GLVH @ 2019-08-18 18:05:34
# =============================================================================

class rate(db.Model):
    __tablename__ = 'Rates'
    Rat_Id     = db.Column( db.Integer, primary_key=True, autoincrement=True )
    Typ_Code   = db.Column( db.String(10), db.ForeignKey('CU_Types.Typ_Code') )
    Cus_Id     = db.Column( db.Integer, db.ForeignKey('Customers.Cus_Id') )
    Pla_Id     = db.Column( db.Integer, db.ForeignKey('Platforms.Pla_Id') )
    CC_Id      = db.Column( db.Integer, db.ForeignKey('Cost_Centers.CC_Id') )
    CI_Id      = db.Column( db.Integer, db.ForeignKey('Configuration_Items.CI_Id') )
    Rat_Price  = db.Column( db.Numeric(20,6) )
    Cur_Code   = db.Column( db.String(3), db.ForeignKey('Currencies.Cur_Code') )
    MU_Code    = db.Column( db.String(3), db.ForeignKey('Measure_Units.MU_Code') )
    Rat_Period = db.Column( db.Integer, db.ForeignKey('Rat_Periods.Rat_Period') )
    Rat_Type   = db.Column( db.Integer )


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
# GLVH @ 2019-08-18 18:05:34
# =============================================================================

class rat_period(db.Model):
    __tablename__ = 'Rat_Periods'
    Rat_Period = db.Column( db.Integer, primary_key=True )
    Value      = db.Column( db.String(45) )

    rates      = db.relationship('rate',backref='rat_period')

    def __init__(self, Rat_Period=None, Value='None'):
        self.Rat_Period = Rat_Period
        self.Value      = Value

    def __repr__(self):
        return "<Rat_Periods( Rat_Period='%s', Value='%s')>" % \
                ( self.Rat_Period, self.Value)

# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-18 18:05:34
# =============================================================================

class Role(db.Model):
    __tablename__ = 'Roles'
    id          = db.Column( db.Integer, primary_key=True )
    name        = db.Column( db.String(64) )
    default     = db.Column( db.Boolean )
    permissions = db.Column( db.Integer )

    users       = db.relationship('User',backref='role')

    def __init__(self, id=None, name='None', default=None, permissions=None):
        self.id          = id
        self.name        = name
        self.default     = default
        self.permissions = permissions

    def __repr__(self):
        return "<Roles( id='%s', name='%s', default='%s', permissions='%s')>" % \
                ( self.id, self.name, self.default, self.permissions)

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
# GLVH @ 2019-08-18 18:05:34
# =============================================================================

class st_use_per_cu(db.Model):
    __tablename__ = 'ST_Use_Per_CU'
    CU_Id                  = db.Column( db.Integer, primary_key=True )
    From                   = db.Column( db.DateTime, primary_key=True )
    To                     = db.Column( db.DateTime, primary_key=True )
    Total_Slices           = db.Column( db.Integer, default=0 )
    Found_Slices           = db.Column( db.Integer, default=0 )
    Not_Found_Slices       = db.Column( db.Integer, default=0 )
    Period_Initial_Q       = db.Column( db.Numeric(20,6), default=0.000000 )
    Period_Increase        = db.Column( db.Numeric(20,6), default=0.000000 )
    Period_Increase_Count  = db.Column( db.Integer, default=0 )
    Period_Reduction       = db.Column( db.Numeric(20,6), default=0.000000 )
    Period_Reduction_Count = db.Column( db.Integer, default=0 )
    Period_Final_Q         = db.Column( db.Numeric(20,6), default=0.000000 )
    CI_Id                  = db.Column( db.Integer, default=1 )
    CC_Id                  = db.Column( db.Integer, default=1 )
    Cus_Id                 = db.Column( db.Integer, default=1 )
    Rat_Id                 = db.Column( db.Integer, default=1 )
    Typ_Code               = db.Column( db.String(10), default='NUL' )
    Pla_Id                 = db.Column( db.Integer, default=1 )
    Mean                   = db.Column( db.Numeric(20,6), default=0.000000 )
    Variance               = db.Column( db.Numeric(20,6), default=0.000000 )
    StdDev                 = db.Column( db.Numeric(20,6), default=0.000000 )
    Min                    = db.Column( db.Numeric(20,6), default=0.000000 )
    Max                    = db.Column( db.Numeric(20,6), default=0.000000 )


    def __init__(self, CU_Id=None, From=None, To=None, Total_Slices=0, Found_Slices=0, Not_Found_Slices=0, Period_Initial_Q=0.000000, Period_Increase=0.000000, Period_Increase_Count=0, Period_Reduction=0.000000, Period_Reduction_Count=0, Period_Final_Q=0.000000, CI_Id=1, CC_Id=1, Cus_Id=1, Rat_Id=1, Typ_Code='NUL', Pla_Id=1, Mean=0.000000, Variance=0.000000, StdDev=0.000000, Min=0.000000, Max=0.000000):
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
# GLVH @ 2019-08-18 18:05:34
# =============================================================================

class st_use_per_type(db.Model):
    __tablename__ = 'ST_Use_Per_Type'
    Typ_Code = db.Column( db.String(10), primary_key=True )
    Cus_Id   = db.Column( db.Integer, primary_key=True, default=1 )
    Pla_Id   = db.Column( db.Integer, primary_key=True, default=1 )
    CC_Id    = db.Column( db.Integer, primary_key=True, default=1 )
    CI_Id    = db.Column( db.Integer, primary_key=True, default=1 )
    Year     = db.Column( db.Integer, primary_key=True )
    Month    = db.Column( db.Integer, primary_key=True )
    Count    = db.Column( db.Integer, default=0 )
    Mean     = db.Column( db.Numeric(20,6), default=0.000000 )
    Variance = db.Column( db.Numeric(20,6), default=0.000000 )
    StdDev   = db.Column( db.Numeric(20,6), default=0.000000 )
    Min      = db.Column( db.Numeric(20,6), default=0.000000 )
    Max      = db.Column( db.Numeric(20,6), default=0.000000 )


    def __init__(self, Typ_Code='None', Cus_Id=1, Pla_Id=1, CC_Id=1, CI_Id=1, Year=None, Month=None, Count=0, Mean=0.000000, Variance=0.000000, StdDev=0.000000, Min=0.000000, Max=0.000000):
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
# GLVH @ 2019-08-18 18:05:34
# =============================================================================

class trace(db.Model):
    __tablename__ = 'Trace'
    ID   = db.Column( db.Integer, primary_key=True, autoincrement=True )
    LINE = db.Column( db.String(128) )


    def __init__(self, ID=0, LINE='None'):
        self.ID   = ID
        self.LINE = LINE

    def __repr__(self):
        return "<Trace( ID='%s', LINE='%s')>" % \
                ( self.ID, self.LINE)

# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-18 18:05:34
# =============================================================================

class User(UserMixin, db.Model):
    __tablename__ = 'Users'
    id            = db.Column( db.Integer, primary_key=True, autoincrement=True )
    username      = db.Column( db.String(64) )
    role_id       = db.Column( db.Integer, db.ForeignKey('Roles.id') )
    email         = db.Column( db.String(64) )
    password_hash = db.Column( db.String(128) )
    confirmed     = db.Column( db.Boolean, default=0 )
    CC_Id         = db.Column( db.Integer, db.ForeignKey('Cost_Centers.CC_Id'), default=1 )


    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        if self.role is None:
            if self.username == current_app.config['COLLECTOR_ADMIN']:
                self.role = Role.query.filter_by(permissions=0xfe).first()
            if self.role is None:
                self.role = Role.query.filter_by(default=True).first()


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

