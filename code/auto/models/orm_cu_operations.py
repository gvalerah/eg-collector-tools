# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-18 18:05:34
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


