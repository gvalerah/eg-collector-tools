# =============================================================================

# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-11-30 16:47:18
# =============================================================================


class platform(db.Model):
    __tablename__ = 'Platforms'
    Pla_Id       = db.Column( db.Integer, primary_key=True, autoincrement=True )
    Pla_Name     = db.Column( db.String(45) )
    Pla_Host     = db.Column( db.String(45) )
    Pla_Port     = db.Column( db.String(45) )
    Pla_User     = db.Column( db.String(45) )
    Pla_Password = db.Column( db.String(45) )

    configuration_items = db.relationship('configuration_item',backref='platform')
    rates        = db.relationship('rate',backref='platform')

    def __init__(self, Pla_Id=0, Pla_Name='None', Pla_Host='None', Pla_Port='None', Pla_User='None', Pla_Password='None'):
        self.Pla_Id       = Pla_Id
        self.Pla_Name     = Pla_Name
        self.Pla_Host     = Pla_Host
        self.Pla_Port     = Pla_Port
        self.Pla_User     = Pla_User
        self.Pla_Password = Pla_Password

    def __repr__(self):
        return "<Platforms( Pla_Id='%s', Pla_Name='%s', Pla_Host='%s', Pla_Port='%s', Pla_User='%s', Pla_Password='%s')>" % \
                ( self.Pla_Id, self.Pla_Name, self.Pla_Host, self.Pla_Port, self.Pla_User, self.Pla_Password)

# =============================================================================

class frm_platform(Form):
    Pla_Name             = StringField  ("Name?")
    Pla_Host             = StringField  ("Host?")
    Pla_Port             = StringField  ("Port?")
    Pla_User             = StringField  ("User?")
    Pla_Password         = StringField  ("Password?")

    submit_Save          = SubmitField  ('Save')
    submit_New           = SubmitField  ('New')
    submit_Cancel        = SubmitField  ('Cancel')

    has_FKs              = False

# =============================================================================

class frm_platform_delete(Form):
    submit_Delete        = SubmitField  ('Delete')
    submit_Cancel        = SubmitField  ('Cancel')

# =============================================================================

class Platforms(Base):
    __tablename__ = 'Platforms'
    engine        = None

    Pla_Id       = Column( Integer, primary_key=True, autoincrement=True )
    Pla_Name     = Column( String(45) )
    Pla_Host     = Column( String(45) )
    Pla_Port     = Column( String(45) )
    Pla_User     = Column( String(45) )
    Pla_Password = Column( String(45) )

    def __init__(self, Pla_Id, Pla_Name, Pla_Host, Pla_Port, Pla_User, Pla_Password):
        self.set( Pla_Id, Pla_Name, Pla_Host, Pla_Port, Pla_User, Pla_Password)

    def __repr__(self):
        return "<Platforms( Pla_Id='%s', Pla_Name='%s', Pla_Host='%s', Pla_Port='%s', Pla_User='%s', Pla_Password='%s')>" % \
                ( self.Pla_Id, self.Pla_Name, self.Pla_Host, self.Pla_Port, self.Pla_User, self.Pla_Password)

# =============================================================================


