# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-16 15:51:37
# =============================================================================

class Customers(Base):
    __tablename__ = 'Customers'
    engine        = None
    Cus_Id   = Column( Integer, primary_key=True, autoincrement=True )
    Cus_Name = Column( String(45) )
    CC_Id    = Column( Integer, ForeignKey('Cost_Centers.CC_Id') )
    
    def __init__(self, Cus_Id=0, Cus_Name='None', CC_Id=None):
        self.Cus_Id   = Cus_Id
        self.Cus_Name = Cus_Name
        self.CC_Id    = CC_Id

    def __repr__(self):
        return "<Customers( Cus_Id='%s', Cus_Name='%s', CC_Id='%s')>" % \
                ( self.Cus_Id, self.Cus_Name, self.CC_Id)


