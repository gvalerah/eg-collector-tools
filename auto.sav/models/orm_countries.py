# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-20 18:43:44
# =============================================================================

class Countries(Base):
    __tablename__ = 'Countries'
    engine        = None
    Cou_Code = Column( String(2), primary_key=True )
    Cou_Name = Column( String(45) )
    Cou_A3   = Column( String(3) )
    Cou_N    = Column( Integer )
    
    def __init__(self, Cou_Code='None', Cou_Name='None', Cou_A3='None', Cou_N=None):
        self.Cou_Code = Cou_Code
        self.Cou_Name = Cou_Name
        self.Cou_A3   = Cou_A3
        self.Cou_N    = Cou_N

    def __repr__(self):
        return "<Countries( Cou_Code='%s', Cou_Name='%s', Cou_A3='%s', Cou_N='%s')>" % \
                ( self.Cou_Code, self.Cou_Name, self.Cou_A3, self.Cou_N)


