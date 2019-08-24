# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-20 18:43:44
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

