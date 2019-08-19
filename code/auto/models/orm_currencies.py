# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-18 18:05:34
# =============================================================================

class Currencies(Base):
    __tablename__ = 'Currencies'
    engine        = None
    Cur_Code    = Column( String(3), primary_key=True )
    Cur_Name    = Column( String(45) )
    Cur_Id      = Column( Integer )
    Cur_Comment = Column( String(128) )
    
    def __init__(self, Cur_Code='None', Cur_Name='None', Cur_Id=None, Cur_Comment='None'):
        self.Cur_Code    = Cur_Code
        self.Cur_Name    = Cur_Name
        self.Cur_Id      = Cur_Id
        self.Cur_Comment = Cur_Comment

    def __repr__(self):
        return "<Currencies( Cur_Code='%s', Cur_Name='%s', Cur_Id='%s', Cur_Comment='%s')>" % \
                ( self.Cur_Code, self.Cur_Name, self.Cur_Id, self.Cur_Comment)


