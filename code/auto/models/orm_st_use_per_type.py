# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-18 18:05:34
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


