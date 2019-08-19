# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-18 18:05:34
# =============================================================================

class Configuration_Items(Base):
    __tablename__ = 'Configuration_Items'
    engine        = None
    CI_Id                       = Column( Integer, primary_key=True, autoincrement=True )
    CI_Name                     = Column( String(45) )
    CI_UUID                     = Column( String(45) )
    Pla_Id                      = Column( Integer, ForeignKey('Platforms.Pla_Id') )
    CC_Id                       = Column( Integer, ForeignKey('Cost_Centers.CC_Id') )
    Cus_Id                      = Column( Integer, ForeignKey('Customers.Cus_Id') )
    CI_Commissioning_DateTime   = Column( DateTime )
    CI_Decommissioning_DateTime = Column( DateTime )
    
    def __init__(self, CI_Id=0, CI_Name='None', CI_UUID='None', Pla_Id=None, CC_Id=None, Cus_Id=1, CI_Commissioning_DateTime=None, CI_Decommissioning_DateTime=None):
        self.CI_Id                       = CI_Id
        self.CI_Name                     = CI_Name
        self.CI_UUID                     = CI_UUID
        self.Pla_Id                      = Pla_Id
        self.CC_Id                       = CC_Id
        self.Cus_Id                      = Cus_Id
        self.CI_Commissioning_DateTime   = CI_Commissioning_DateTime
        self.CI_Decommissioning_DateTime = CI_Decommissioning_DateTime

    def __repr__(self):
        return "<Configuration_Items( CI_Id='%s', CI_Name='%s', CI_UUID='%s', Pla_Id='%s', CC_Id='%s', Cus_Id='%s', CI_Commissioning_DateTime='%s', CI_Decommissioning_DateTime='%s')>" % \
                ( self.CI_Id, self.CI_Name, self.CI_UUID, self.Pla_Id, self.CC_Id, self.Cus_Id, self.CI_Commissioning_DateTime, self.CI_Decommissioning_DateTime)


