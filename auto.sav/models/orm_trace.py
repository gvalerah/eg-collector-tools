# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-20 18:43:44
# =============================================================================

class Trace(Base):
    __tablename__ = 'Trace'
    engine        = None
    ID   = Column( Integer, primary_key=True, autoincrement=True )
    LINE = Column( String(128) )
    
    def __init__(self, ID=0, LINE='None'):
        self.ID   = ID
        self.LINE = LINE

    def __repr__(self):
        return "<Trace( ID='%s', LINE='%s')>" % \
                ( self.ID, self.LINE)


