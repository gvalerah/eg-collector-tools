# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-20 18:43:44
# =============================================================================

class Roles(Base):
    __tablename__ = 'Roles'
    engine        = None
    id          = Column( Integer, primary_key=True )
    name        = Column( String(64) )
    default     = Column( Boolean )
    permissions = Column( Integer )
    
    def __init__(self, id=None, name='None', default=None, permissions=None):
        self.id          = id
        self.name        = name
        self.default     = default
        self.permissions = permissions

    def __repr__(self):
        return "<Roles( id='%s', name='%s', default='%s', permissions='%s')>" % \
                ( self.id, self.name, self.default, self.permissions)


