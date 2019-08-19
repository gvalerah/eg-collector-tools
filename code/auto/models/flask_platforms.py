# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-18 18:05:34
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

