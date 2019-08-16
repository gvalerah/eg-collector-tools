# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-16 15:51:37
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

