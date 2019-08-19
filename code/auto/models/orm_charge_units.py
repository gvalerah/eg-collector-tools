# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-18 18:05:34
# =============================================================================

class Charge_Units(Base):
    __tablename__ = 'Charge_Units'
    engine        = None
    CU_Id                  = Column( Integer, primary_key=True, autoincrement=True )
    CI_Id                  = Column( Integer, ForeignKey('Configuration_Items.CI_Id') )
    CU_Description         = Column( String(45) )
    CU_UUID                = Column( String(45) )
    CU_Is_Billeable        = Column( Boolean )
    CU_Is_Always_Billeable = Column( Boolean )
    CU_Quantity            = Column( Numeric(20,6) )
    CU_Operation           = Column( String(10), ForeignKey('CU_Operations.CU_Operation') )
    Typ_Code               = Column( String(10), ForeignKey('CU_Types.Typ_Code') )
    CIT_Generation         = Column( Integer, ForeignKey('CIT_Generations.CIT_Generation') )
    Rat_Id                 = Column( Integer )
    CU_Reference_1         = Column( String(45) )
    CU_Reference_2         = Column( String(45) )
    CU_Reference_3         = Column( String(45) )
    
    def __init__(self, CU_Id=0, CI_Id=None, CU_Description='None', CU_UUID='None', CU_Is_Billeable=0, CU_Is_Always_Billeable=0, CU_Quantity=None, CU_Operation='None', Typ_Code='None', CIT_Generation=None, Rat_Id=None, CU_Reference_1='None', CU_Reference_2='None', CU_Reference_3='None'):
        self.CU_Id                  = CU_Id
        self.CI_Id                  = CI_Id
        self.CU_Description         = CU_Description
        self.CU_UUID                = CU_UUID
        self.CU_Is_Billeable        = CU_Is_Billeable
        self.CU_Is_Always_Billeable = CU_Is_Always_Billeable
        self.CU_Quantity            = CU_Quantity
        self.CU_Operation           = CU_Operation
        self.Typ_Code               = Typ_Code
        self.CIT_Generation         = CIT_Generation
        self.Rat_Id                 = Rat_Id
        self.CU_Reference_1         = CU_Reference_1
        self.CU_Reference_2         = CU_Reference_2
        self.CU_Reference_3         = CU_Reference_3

    def __repr__(self):
        return "<Charge_Units( CU_Id='%s', CI_Id='%s', CU_Description='%s', CU_UUID='%s', CU_Is_Billeable='%s', CU_Is_Always_Billeable='%s', CU_Quantity='%s', CU_Operation='%s', Typ_Code='%s', CIT_Generation='%s', Rat_Id='%s', CU_Reference_1='%s', CU_Reference_2='%s', CU_Reference_3='%s')>" % \
                ( self.CU_Id, self.CI_Id, self.CU_Description, self.CU_UUID, self.CU_Is_Billeable, self.CU_Is_Always_Billeable, self.CU_Quantity, self.CU_Operation, self.Typ_Code, self.CIT_Generation, self.Rat_Id, self.CU_Reference_1, self.CU_Reference_2, self.CU_Reference_3)


