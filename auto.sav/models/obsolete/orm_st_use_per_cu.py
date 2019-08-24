# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-15 15:05:30
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


