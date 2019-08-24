# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-20 18:43:44
# =============================================================================

class Cost_Centers(Base):
    __tablename__ = 'Cost_Centers'
    engine        = None
    CC_Id          = Column( Integer, primary_key=True, autoincrement=True )
    CC_Code        = Column( String(45) )
    CC_Description = Column( String(45) )
    Cur_Code       = Column( String(3), ForeignKey('Currencies.Cur_Code') )
    CC_Parent_Code = Column( String(45) )
    
    def __init__(self, CC_Id=0, CC_Code='None', CC_Description='None', Cur_Code='None', CC_Parent_Code='1'):
        self.CC_Id          = CC_Id
        self.CC_Code        = CC_Code
        self.CC_Description = CC_Description
        self.Cur_Code       = Cur_Code
        self.CC_Parent_Code = CC_Parent_Code

    def __repr__(self):
        return "<Cost_Centers( CC_Id='%s', CC_Code='%s', CC_Description='%s', Cur_Code='%s', CC_Parent_Code='%s')>" % \
                ( self.CC_Id, self.CC_Code, self.CC_Description, self.Cur_Code, self.CC_Parent_Code)


