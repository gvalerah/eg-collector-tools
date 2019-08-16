# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-16 15:51:37
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

