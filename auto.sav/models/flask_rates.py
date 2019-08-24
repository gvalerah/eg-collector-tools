# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-20 18:43:44
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
