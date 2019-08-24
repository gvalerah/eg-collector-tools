# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-20 18:43:44
# =============================================================================

class Charge_Items(Base):
    __tablename__ = 'Charge_Items'
    engine        = None
    CU_Id         = Column( Integer, ForeignKey('Charge_Units.CU_Id'), primary_key=True )
    CIT_Date      = Column( Date )
    CIT_Time      = Column( Time )
    CIT_Quantity  = Column( Numeric(20,6) )
    CIT_Status    = Column( Integer, ForeignKey('CIT_Statuses.CIT_Status') )
    CIT_Is_Active = Column( Boolean )
    CIT_DateTime  = Column( DateTime, primary_key=True )
    
    def __init__(self, CU_Id=0, CIT_Date=None, CIT_Time=None, CIT_Quantity=0.000000, CIT_Status=0, CIT_Is_Active=0, CIT_DateTime=None):
        self.CU_Id         = CU_Id
        self.CIT_Date      = CIT_Date
        self.CIT_Time      = CIT_Time
        self.CIT_Quantity  = CIT_Quantity
        self.CIT_Status    = CIT_Status
        self.CIT_Is_Active = CIT_Is_Active
        self.CIT_DateTime  = CIT_DateTime

    def __repr__(self):
        return "<Charge_Items( CU_Id='%s', CIT_Date='%s', CIT_Time='%s', CIT_Quantity='%s', CIT_Status='%s', CIT_Is_Active='%s', CIT_DateTime='%s')>" % \
                ( self.CU_Id, self.CIT_Date, self.CIT_Time, self.CIT_Quantity, self.CIT_Status, self.CIT_Is_Active, self.CIT_DateTime)


