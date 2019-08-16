# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-16 15:51:37
# =============================================================================

class CU_Types(Base):
    __tablename__ = 'CU_Types'
    engine        = None
    Typ_Code        = Column( String(10), primary_key=True )
    Typ_Description = Column( String(45) )
    
    def __init__(self, Typ_Code='None', Typ_Description='None'):
        self.Typ_Code        = Typ_Code
        self.Typ_Description = Typ_Description

    def __repr__(self):
        return "<CU_Types( Typ_Code='%s', Typ_Description='%s')>" % \
                ( self.Typ_Code, self.Typ_Description)


