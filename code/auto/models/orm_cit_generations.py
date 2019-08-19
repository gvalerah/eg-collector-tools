# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-18 18:05:34
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


