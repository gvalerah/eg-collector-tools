# ------------------------------------------------ 
# ORM Models File
# Static File. 
# GLVH 2018-12-13
# ------------------------------------------------
from datetime               import datetime

from sqlalchemy             import Column, String, Integer, Numeric, Date, Time, Boolean, DateTime
from sqlalchemy             import ForeignKey
# ------------------------------------------------



# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-09-09 13:44:02
# =============================================================================

from sqlalchemy                 import Table, Column, MetaData, ForeignKey
from sqlalchemy                 import Integer, String, Date, Time
from sqlalchemy                 import Numeric, DateTime, Boolean


# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-09-09 13:44:02
# =============================================================================
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-09-09 13:44:02
# =============================================================================

class CIT_Generations(Base):
    __tablename__ = 'CIT_Generations'
    engine        = None
    CIT_Generation = Column( Integer, primary_key=True )
    Value          = Column( String(45) )
    
    def __init__(self, CIT_Generation=None, Value='None'):
        self.CIT_Generation = CIT_Generation
        self.Value          = Value

    def __repr__(self):
        return "<CIT_Generations( CIT_Generation='%s', Value='%s')>" % \
                ( self.CIT_Generation, self.Value)


# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-09-09 13:44:02
# =============================================================================

class CIT_Statuses(Base):
    __tablename__ = 'CIT_Statuses'
    engine        = None
    CIT_Status = Column( Integer, primary_key=True )
    Value      = Column( String(45) )
    
    def __init__(self, CIT_Status=None, Value='None'):
        self.CIT_Status = CIT_Status
        self.Value      = Value

    def __repr__(self):
        return "<CIT_Statuses( CIT_Status='%s', Value='%s')>" % \
                ( self.CIT_Status, self.Value)


# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-09-09 13:44:02
# =============================================================================

class CU_Operations(Base):
    __tablename__ = 'CU_Operations'
    engine        = None
    CU_Operation = Column( String(10), primary_key=True )
    Value        = Column( String(45) )
    Is_Multiply  = Column( Boolean )
    Factor       = Column( Integer )
    
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
# GLVH @ 2019-09-09 13:44:02
# =============================================================================

class CU_Types(Base):
    __tablename__ = 'CU_Types'
    engine        = None
    Typ_Code        = Column( String(10), primary_key=True )
    Typ_Description = Column( String(45) )
    
    def __init__(self, Typ_Code='None', Typ_Description='None'):
        self.Typ_Code        = Typ_Code
        self.Typ_Description = Typ_Description

    def __repr__(self):
        return "<CU_Types( Typ_Code='%s', Typ_Description='%s')>" % \
                ( self.Typ_Code, self.Typ_Description)


# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-09-09 13:44:02
# =============================================================================

class Charge_Items(Base):
    __tablename__ = 'Charge_Items'
    engine        = None
    CU_Id         = Column( Integer, ForeignKey('Charge_Units.CU_Id'), primary_key=True )
    CIT_Date      = Column( Date )
    CIT_Time      = Column( Time )
    CIT_Quantity  = Column( Numeric(20,6) )
    CIT_Status    = Column( Integer, ForeignKey('CIT_Statuses.CIT_Status') )
    CIT_Is_Active = Column( Boolean )
    CIT_DateTime  = Column( DateTime, primary_key=True )
    
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
# GLVH @ 2019-09-09 13:44:02
# =============================================================================

class Charge_Resumes(Base):
    __tablename__ = 'Charge_Resumes'
    engine        = None
    Cus_Id                 = Column( Integer, primary_key=True )
    CR_Date_From           = Column( Date, primary_key=True )
    CR_Date_To             = Column( Date, primary_key=True )
    CIT_Status             = Column( Integer, primary_key=True )
    Cur_Code               = Column( String(3), primary_key=True )
    CIT_Count              = Column( Integer )
    CIT_Quantity           = Column( Numeric(20,6) )
    CIT_Generation         = Column( Integer )
    CU_Id                  = Column( Integer, primary_key=True )
    CI_CC_Id               = Column( Integer )
    CU_Operation           = Column( String(10) )
    Typ_Code               = Column( String(10) )
    CC_Cur_Code            = Column( String(3) )
    CI_Id                  = Column( Integer )
    Rat_Id                 = Column( Integer )
    Rat_Price              = Column( Numeric(20,6) )
    Rat_MU_Code            = Column( String(3) )
    Rat_Cur_Code           = Column( String(3) )
    Rat_Period             = Column( Integer )
    Rat_Hourly             = Column( Numeric(20,6) )
    Rat_Daily              = Column( Numeric(20,6) )
    Rat_Monthly            = Column( Numeric(20,6) )
    CR_Quantity            = Column( Numeric(20,6) )
    CR_Quantity_at_Rate    = Column( Numeric(20,6) )
    CC_XR                  = Column( Numeric(20,10) )
    CR_Cur_XR              = Column( Numeric(20,10) )
    CR_ST_at_Rate_Cur      = Column( Numeric(20,6) )
    CR_ST_at_CC_Cur        = Column( Numeric(20,6) )
    CR_ST_at_Cur           = Column( Numeric(20,6) )
    Cus_Name               = Column( String(45) )
    CI_Name                = Column( String(45) )
    CU_Description         = Column( String(45) )
    CC_Description         = Column( String(45) )
    Rat_Period_Description = Column( String(10) )
    Pla_Id                 = Column( Integer )
    
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
# GLVH @ 2019-09-09 13:44:02
# =============================================================================

class Charge_Units(Base):
    __tablename__ = 'Charge_Units'
    engine        = None
    CU_Id                  = Column( Integer, primary_key=True, autoincrement=True )
    CI_Id                  = Column( Integer, ForeignKey('Configuration_Items.CI_Id') )
    CU_Description         = Column( String(45) )
    CU_UUID                = Column( String(45) )
    CU_Is_Billeable        = Column( Boolean )
    CU_Is_Always_Billeable = Column( Boolean )
    CU_Quantity            = Column( Numeric(20,6) )
    CU_Operation           = Column( String(10), ForeignKey('CU_Operations.CU_Operation') )
    Typ_Code               = Column( String(10), ForeignKey('CU_Types.Typ_Code') )
    CIT_Generation         = Column( Integer, ForeignKey('CIT_Generations.CIT_Generation') )
    Rat_Id                 = Column( Integer )
    CU_Reference_1         = Column( String(45) )
    CU_Reference_2         = Column( String(45) )
    CU_Reference_3         = Column( String(45) )
    
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
# GLVH @ 2019-09-09 13:44:02
# =============================================================================

class Configuration_Items(Base):
    __tablename__ = 'Configuration_Items'
    engine        = None
    CI_Id                       = Column( Integer, primary_key=True, autoincrement=True )
    CI_Name                     = Column( String(45) )
    CI_UUID                     = Column( String(45) )
    Pla_Id                      = Column( Integer, ForeignKey('Platforms.Pla_Id') )
    CC_Id                       = Column( Integer, ForeignKey('Cost_Centers.CC_Id') )
    Cus_Id                      = Column( Integer, ForeignKey('Customers.Cus_Id') )
    CI_Commissioning_DateTime   = Column( DateTime )
    CI_Decommissioning_DateTime = Column( DateTime )
    
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
# GLVH @ 2019-09-09 13:44:02
# =============================================================================

class Cost_Centers(Base):
    __tablename__ = 'Cost_Centers'
    engine        = None
    CC_Id          = Column( Integer, primary_key=True, autoincrement=True )
    CC_Code        = Column( String(45) )
    CC_Description = Column( String(45) )
    Cur_Code       = Column( String(3), ForeignKey('Currencies.Cur_Code') )
    CC_Parent_Code = Column( String(45) )
    
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
# GLVH @ 2019-09-09 13:44:02
# =============================================================================

class Countries(Base):
    __tablename__ = 'Countries'
    engine        = None
    Cou_Code = Column( String(2), primary_key=True )
    Cou_Name = Column( String(45) )
    Cou_A3   = Column( String(3) )
    Cou_N    = Column( Integer )
    
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
# GLVH @ 2019-09-09 13:44:02
# =============================================================================

class Countries_Currencies(Base):
    __tablename__ = 'Countries_Currencies'
    engine        = None
    Cou_Code        = Column( String(2), ForeignKey('Countries.Cou_Code'), primary_key=True )
    Cur_Code        = Column( String(3), ForeignKey('Currencies.Cur_Code'), primary_key=True )
    Cou_Cur_Comment = Column( String(45) )
    
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
# GLVH @ 2019-09-09 13:44:02
# =============================================================================

class Currencies(Base):
    __tablename__ = 'Currencies'
    engine        = None
    Cur_Code    = Column( String(3), primary_key=True )
    Cur_Name    = Column( String(45) )
    Cur_Id      = Column( Integer )
    Cur_Comment = Column( String(128) )
    
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
# GLVH @ 2019-09-09 13:44:02
# =============================================================================

class Customers(Base):
    __tablename__ = 'Customers'
    engine        = None
    Cus_Id   = Column( Integer, primary_key=True, autoincrement=True )
    Cus_Name = Column( String(45) )
    CC_Id    = Column( Integer, ForeignKey('Cost_Centers.CC_Id') )
    
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
# GLVH @ 2019-09-09 13:44:02
# =============================================================================

class Exchange_Rates(Base):
    __tablename__ = 'Exchange_Rates'
    engine        = None
    ER_Id     = Column( Integer, primary_key=True, autoincrement=True )
    Cur_Code  = Column( String(3), ForeignKey('Currencies.Cur_Code') )
    ER_Factor = Column( Numeric(20,10) )
    ER_Date   = Column( Date )
    
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
# GLVH @ 2019-09-09 13:44:02
# =============================================================================

class Measure_Units(Base):
    __tablename__ = 'Measure_Units'
    engine        = None
    MU_Code        = Column( String(3), primary_key=True )
    MU_Description = Column( String(45) )
    
    def __init__(self, MU_Code='None', MU_Description='None'):
        self.MU_Code        = MU_Code
        self.MU_Description = MU_Description

    def __repr__(self):
        return "<Measure_Units( MU_Code='%s', MU_Description='%s')>" % \
                ( self.MU_Code, self.MU_Description)


# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-09-09 13:44:02
# =============================================================================

class Platforms(Base):
    __tablename__ = 'Platforms'
    engine        = None
    Pla_Id       = Column( Integer, primary_key=True, autoincrement=True )
    Pla_Name     = Column( String(45) )
    Pla_Host     = Column( String(45) )
    Pla_Port     = Column( String(45) )
    Pla_User     = Column( String(45) )
    Pla_Password = Column( String(45) )
    
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
# GLVH @ 2019-09-09 13:44:02
# =============================================================================

class Rat_Periods(Base):
    __tablename__ = 'Rat_Periods'
    engine        = None
    Rat_Period = Column( Integer, primary_key=True )
    Value      = Column( String(45) )
    
    def __init__(self, Rat_Period=None, Value='None'):
        self.Rat_Period = Rat_Period
        self.Value      = Value

    def __repr__(self):
        return "<Rat_Periods( Rat_Period='%s', Value='%s')>" % \
                ( self.Rat_Period, self.Value)


# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-09-09 13:44:02
# =============================================================================

class Rates(Base):
    __tablename__ = 'Rates'
    engine        = None
    Rat_Id     = Column( Integer, primary_key=True, autoincrement=True )
    Typ_Code   = Column( String(10), ForeignKey('CU_Types.Typ_Code') )
    Cus_Id     = Column( Integer, ForeignKey('Customers.Cus_Id') )
    Pla_Id     = Column( Integer, ForeignKey('Platforms.Pla_Id') )
    CC_Id      = Column( Integer, ForeignKey('Cost_Centers.CC_Id') )
    CI_Id      = Column( Integer, ForeignKey('Configuration_Items.CI_Id') )
    Rat_Price  = Column( Numeric(20,6) )
    Cur_Code   = Column( String(3), ForeignKey('Currencies.Cur_Code') )
    MU_Code    = Column( String(3), ForeignKey('Measure_Units.MU_Code') )
    Rat_Period = Column( Integer, ForeignKey('Rat_Periods.Rat_Period') )
    Rat_Type   = Column( Integer )
    
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


# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-09-09 13:44:02
# =============================================================================

class Roles(Base):
    __tablename__ = 'Roles'
    engine        = None
    id          = Column( Integer, primary_key=True )
    name        = Column( String(64) )
    default     = Column( Boolean )
    permissions = Column( Integer )
    
    def __init__(self, id=None, name='None', default=None, permissions=None):
        self.id          = id
        self.name        = name
        self.default     = default
        self.permissions = permissions

    def __repr__(self):
        return "<Roles( id='%s', name='%s', default='%s', permissions='%s')>" % \
                ( self.id, self.name, self.default, self.permissions)


# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-09-09 13:44:02
# =============================================================================

class ST_Use_Per_CU(Base):
    __tablename__ = 'ST_Use_Per_CU'
    engine        = None
    CU_Id                  = Column( Integer, primary_key=True )
    From                   = Column( DateTime, primary_key=True )
    To                     = Column( DateTime, primary_key=True )
    Total_Slices           = Column( Integer )
    Found_Slices           = Column( Integer )
    Not_Found_Slices       = Column( Integer )
    Period_Initial_Q       = Column( Numeric(20,6) )
    Period_Increase        = Column( Numeric(20,6) )
    Period_Increase_Count  = Column( Integer )
    Period_Reduction       = Column( Numeric(20,6) )
    Period_Reduction_Count = Column( Integer )
    Period_Final_Q         = Column( Numeric(20,6) )
    CI_Id                  = Column( Integer )
    CC_Id                  = Column( Integer )
    Cus_Id                 = Column( Integer )
    Rat_Id                 = Column( Integer )
    Typ_Code               = Column( String(10) )
    Pla_Id                 = Column( Integer )
    Mean                   = Column( Numeric(20,6) )
    Variance               = Column( Numeric(20,6) )
    StdDev                 = Column( Numeric(20,6) )
    Min                    = Column( Numeric(20,6) )
    Max                    = Column( Numeric(20,6) )
    
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
# GLVH @ 2019-09-09 13:44:02
# =============================================================================

class ST_Use_Per_Type(Base):
    __tablename__ = 'ST_Use_Per_Type'
    engine        = None
    Typ_Code = Column( String(10), primary_key=True )
    Cus_Id   = Column( Integer, primary_key=True )
    Pla_Id   = Column( Integer, primary_key=True )
    CC_Id    = Column( Integer, primary_key=True )
    CI_Id    = Column( Integer, primary_key=True )
    Year     = Column( Integer, primary_key=True )
    Month    = Column( Integer, primary_key=True )
    Count    = Column( Integer )
    Mean     = Column( Numeric(20,6) )
    Variance = Column( Numeric(20,6) )
    StdDev   = Column( Numeric(20,6) )
    Min      = Column( Numeric(20,6) )
    Max      = Column( Numeric(20,6) )
    
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
# GLVH @ 2019-09-09 13:44:02
# =============================================================================

class Trace(Base):
    __tablename__ = 'Trace'
    engine        = None
    ID   = Column( Integer, primary_key=True, autoincrement=True )
    LINE = Column( String(128) )
    
    def __init__(self, ID=0, LINE='None'):
        self.ID   = ID
        self.LINE = LINE

    def __repr__(self):
        return "<Trace( ID='%s', LINE='%s')>" % \
                ( self.ID, self.LINE)


# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-09-09 13:44:02
# =============================================================================

class User_Resumes(Base):
    __tablename__ = 'User_Resumes'
    engine        = None
    Cus_Id                 = Column( Integer )
    CR_Date_From           = Column( Date, primary_key=True )
    CR_Date_To             = Column( Date, primary_key=True )
    CIT_Status             = Column( Integer, primary_key=True )
    Cur_Code               = Column( String(3), primary_key=True )
    CIT_Count              = Column( Integer )
    CIT_Quantity           = Column( Numeric(20,6) )
    CIT_Generation         = Column( Integer )
    CU_Id                  = Column( Integer, primary_key=True )
    CI_CC_Id               = Column( Integer )
    CU_Operation           = Column( String(10) )
    Typ_Code               = Column( String(10) )
    CC_Cur_Code            = Column( String(3) )
    CI_Id                  = Column( Integer, primary_key=True )
    Rat_Id                 = Column( Integer )
    Rat_Price              = Column( Numeric(20,6) )
    Rat_MU_Code            = Column( String(3) )
    Rat_Cur_Code           = Column( String(3) )
    Rat_Period             = Column( Integer )
    Rat_Hourly             = Column( Numeric(20,6) )
    Rat_Daily              = Column( Numeric(20,6) )
    Rat_Monthly            = Column( Numeric(20,6) )
    CR_Quantity            = Column( Numeric(20,6) )
    CR_Quantity_at_Rate    = Column( Numeric(20,6) )
    CC_XR                  = Column( Numeric(20,10) )
    CR_Cur_XR              = Column( Numeric(20,10) )
    CR_ST_at_Rate_Cur      = Column( Numeric(20,6) )
    CR_ST_at_CC_Cur        = Column( Numeric(20,6) )
    CR_ST_at_Cur           = Column( Numeric(20,6) )
    Cus_Name               = Column( String(45) )
    CI_Name                = Column( String(45) )
    CU_Description         = Column( String(45) )
    CC_Description         = Column( String(45) )
    Rat_Period_Description = Column( String(10) )
    CC_Code                = Column( String(45) )
    
    def __init__(self, Cus_Id=None, CR_Date_From=None, CR_Date_To=None, CIT_Status=None, Cur_Code='None', CIT_Count=None, CIT_Quantity=None, CIT_Generation=1, CU_Id=None, CI_CC_Id=None, CU_Operation='None', Typ_Code='None', CC_Cur_Code='None', CI_Id=None, Rat_Id=None, Rat_Price=None, Rat_MU_Code='None', Rat_Cur_Code='None', Rat_Period=None, Rat_Hourly=None, Rat_Daily=None, Rat_Monthly=None, CR_Quantity=None, CR_Quantity_at_Rate=None, CC_XR=None, CR_Cur_XR=None, CR_ST_at_Rate_Cur=None, CR_ST_at_CC_Cur=None, CR_ST_at_Cur=None, Cus_Name='None', CI_Name='None', CU_Description='None', CC_Description='None', Rat_Period_Description='None', CC_Code='None'):
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
        self.CC_Code                = CC_Code

    def __repr__(self):
        return "<User_Resumes( Cus_Id='%s', CR_Date_From='%s', CR_Date_To='%s', CIT_Status='%s', Cur_Code='%s', CIT_Count='%s', CIT_Quantity='%s', CIT_Generation='%s', CU_Id='%s', CI_CC_Id='%s', CU_Operation='%s', Typ_Code='%s', CC_Cur_Code='%s', CI_Id='%s', Rat_Id='%s', Rat_Price='%s', Rat_MU_Code='%s', Rat_Cur_Code='%s', Rat_Period='%s', Rat_Hourly='%s', Rat_Daily='%s', Rat_Monthly='%s', CR_Quantity='%s', CR_Quantity_at_Rate='%s', CC_XR='%s', CR_Cur_XR='%s', CR_ST_at_Rate_Cur='%s', CR_ST_at_CC_Cur='%s', CR_ST_at_Cur='%s', Cus_Name='%s', CI_Name='%s', CU_Description='%s', CC_Description='%s', Rat_Period_Description='%s', CC_Code='%s')>" % \
                ( self.Cus_Id, self.CR_Date_From, self.CR_Date_To, self.CIT_Status, self.Cur_Code, self.CIT_Count, self.CIT_Quantity, self.CIT_Generation, self.CU_Id, self.CI_CC_Id, self.CU_Operation, self.Typ_Code, self.CC_Cur_Code, self.CI_Id, self.Rat_Id, self.Rat_Price, self.Rat_MU_Code, self.Rat_Cur_Code, self.Rat_Period, self.Rat_Hourly, self.Rat_Daily, self.Rat_Monthly, self.CR_Quantity, self.CR_Quantity_at_Rate, self.CC_XR, self.CR_Cur_XR, self.CR_ST_at_Rate_Cur, self.CR_ST_at_CC_Cur, self.CR_ST_at_Cur, self.Cus_Name, self.CI_Name, self.CU_Description, self.CC_Description, self.Rat_Period_Description, self.CC_Code)


# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-09-09 13:44:02
# =============================================================================

class Users(Base):
    __tablename__ = 'Users'
    engine        = None
    id            = Column( Integer, primary_key=True, autoincrement=True )
    username      = Column( String(64) )
    role_id       = Column( Integer, ForeignKey('Roles.id') )
    email         = Column( String(64) )
    password_hash = Column( String(128) )
    confirmed     = Column( Boolean )
    CC_Id         = Column( Integer, ForeignKey('Cost_Centers.CC_Id') )
    
    def __init__(self, id=0, username='None', role_id=None, email='None', password_hash='None', confirmed=0, CC_Id=1):
        self.id            = id
        self.username      = username
        self.role_id       = role_id
        self.email         = email
        self.password_hash = password_hash
        self.confirmed     = confirmed
        self.CC_Id         = CC_Id

    def __repr__(self):
        return "<Users( id='%s', username='%s', role_id='%s', email='%s', password_hash='%s', confirmed='%s', CC_Id='%s')>" % \
                ( self.id, self.username, self.role_id, self.email, self.password_hash, self.confirmed, self.CC_Id)



