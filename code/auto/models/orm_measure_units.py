# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-16 15:51:37
# =============================================================================

class Measure_Units(Base):
    __tablename__ = 'Measure_Units'
    engine        = None
    MU_Code        = Column( String(3), primary_key=True )
    MU_Description = Column( String(45) )
    
    def __init__(self, MU_Code='None', MU_Description='None'):
        self.MU_Code        = MU_Code
        self.MU_Description = MU_Description

    def __repr__(self):
        return "<Measure_Units( MU_Code='%s', MU_Description='%s')>" % \
                ( self.MU_Code, self.MU_Description)


