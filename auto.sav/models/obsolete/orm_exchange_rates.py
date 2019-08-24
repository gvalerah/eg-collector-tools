# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-15 15:05:30
# =============================================================================

class Exchange_Rates(Base):
    __tablename__ = 'Exchange_Rates'
    engine        = None
    ER_Id     = Column( Integer, primary_key=True, autoincrement=True )
    Cur_Code  = Column( String(3), ForeignKey('Currencies.Cur_Code') )
    ER_Factor = Column( Numeric(20,10) )
    ER_Date   = Column( Date )
    
    def __init__(self, ER_Id=0, Cur_Code='None', ER_Factor=None, ER_Date=None):
        self.ER_Id     = ER_Id
        self.Cur_Code  = Cur_Code
        self.ER_Factor = ER_Factor
        self.ER_Date   = ER_Date

    def __repr__(self):
        return "<Exchange_Rates( ER_Id='%s', Cur_Code='%s', ER_Factor='%s', ER_Date='%s')>" % \
                ( self.ER_Id, self.Cur_Code, self.ER_Factor, self.ER_Date)


