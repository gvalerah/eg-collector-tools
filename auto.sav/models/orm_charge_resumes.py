# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-20 18:43:44
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


