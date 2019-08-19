# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-18 18:05:34
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


