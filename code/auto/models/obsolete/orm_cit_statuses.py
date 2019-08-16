# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-15 15:05:30
# =============================================================================

class CIT_Statuses(Base):
    __tablename__ = 'CIT_Statuses'
    engine        = None
    CIT_Status = Column( Integer, primary_key=True )
    Value      = Column( String(45) )
    
    def __init__(self, CIT_Status=None, Value='None'):
        self.CIT_Status = CIT_Status
        self.Value      = Value

    def __repr__(self):
        return "<CIT_Statuses( CIT_Status='%s', Value='%s')>" % \
                ( self.CIT_Status, self.Value)


