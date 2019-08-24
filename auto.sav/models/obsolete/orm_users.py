# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-15 15:05:30
# =============================================================================

class Users(Base):
    __tablename__ = 'Users'
    engine        = None
    id            = Column( Integer, primary_key=True, autoincrement=True )
    username      = Column( String(64) )
    role_id       = Column( Integer, ForeignKey('Roles.id') )
    email         = Column( String(64) )
    password_hash = Column( String(128) )
    confirmed     = Column( Boolean )
    CC_Id         = Column( Integer, ForeignKey('Cost_Centers.CC_Id') )
    
    def __init__(self, id=0, username='None', role_id=None, email='None', password_hash='None', confirmed=0, CC_Id=1):
        self.id            = id
        self.username      = username
        self.role_id       = role_id
        self.email         = email
        self.password_hash = password_hash
        self.confirmed     = confirmed
        self.CC_Id         = CC_Id

    def __repr__(self):
        return "<Users( id='%s', username='%s', role_id='%s', email='%s', password_hash='%s', confirmed='%s', CC_Id='%s')>" % \
                ( self.id, self.username, self.role_id, self.email, self.password_hash, self.confirmed, self.CC_Id)


