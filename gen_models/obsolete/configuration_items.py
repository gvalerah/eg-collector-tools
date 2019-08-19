# =============================================================================

# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-11-30 16:47:18
# =============================================================================


class configuration_item(db.Model):
    __tablename__ = 'Configuration_Items'
    CI_Id          = db.Column( db.Integer, primary_key=True, autoincrement=True )
    CI_Name        = db.Column( db.String(45) )
    CI_UUID        = db.Column( db.String(45) )
    Pla_Id         = db.Column( db.Integer, db.ForeignKey('Platforms.Pla_Id') )
    CC_Id          = db.Column( db.Integer, db.ForeignKey('Cost_Centers.CC_Id') )
    CIT_Generation = db.Column( db.Integer, db.ForeignKey('CIT_Generations.CIT_Generation') )
    Cus_Id         = db.Column( db.Integer, db.ForeignKey('Customers.Cus_Id') )

    charge_units   = db.relationship('charge_unit',backref='configuration_item')

    def __init__(self, CI_Id=0, CI_Name='None', CI_UUID='None', Pla_Id=None, CC_Id=None, CIT_Generation=0, Cus_Id=1):
        self.CI_Id          = CI_Id
        self.CI_Name        = CI_Name
        self.CI_UUID        = CI_UUID
        self.Pla_Id         = Pla_Id
        self.CC_Id          = CC_Id
        self.CIT_Generation = CIT_Generation
        self.Cus_Id         = Cus_Id

    def __repr__(self):
        return "<Configuration_Items( CI_Id='%s', CI_Name='%s', CI_UUID='%s', Pla_Id='%s', CC_Id='%s', CIT_Generation='%s', Cus_Id='%s')>" % \
                ( self.CI_Id, self.CI_Name, self.CI_UUID, self.Pla_Id, self.CC_Id, self.CIT_Generation, self.Cus_Id)

# =============================================================================

class frm_configuration_item(Form):
    CI_Name                = StringField  ("Name?")
    CI_UUID                = StringField  ("UUID?")
    Pla_Id                 = SelectField  ("Platform Id?", coerce=int, validators=[Required()])
    CC_Id                  = SelectField  ("Cost Center Id?", coerce=int, validators=[Required()])
    CIT_Generation         = SelectField  ("Default Item Generation Type?", coerce=int, validators=[Required()])
    Cus_Id                 = SelectField  ("Customer Id?", coerce=int, validators=[Required()])

    submit_Save            = SubmitField  ('Save')
    submit_New             = SubmitField  ('New')
    submit_Cancel          = SubmitField  ('Cancel')

    has_FKs                = True

# =============================================================================

class frm_configuration_item_delete(Form):
    submit_Delete          = SubmitField  ('Delete')
    submit_Cancel          = SubmitField  ('Cancel')

# =============================================================================

class Configuration_Items(Base):
    __tablename__ = 'Configuration_Items'
    engine        = None

    CI_Id          = Column( Integer, primary_key=True, autoincrement=True )
    CI_Name        = Column( String(45) )
    CI_UUID        = Column( String(45) )
    Pla_Id         = Column( Integer, ForeignKey('Platforms.Pla_Id') )
    CC_Id          = Column( Integer, ForeignKey('Cost_Centers.CC_Id') )
    CIT_Generation = Column( Integer, ForeignKey('CIT_Generations.CIT_Generation') )
    Cus_Id         = Column( Integer, ForeignKey('Customers.Cus_Id') )

    def __init__(self, CI_Id, CI_Name, CI_UUID, Pla_Id, CC_Id, CIT_Generation, Cus_Id):
        self.set( CI_Id, CI_Name, CI_UUID, Pla_Id, CC_Id, CIT_Generation, Cus_Id)

    def __repr__(self):
        return "<Configuration_Items( CI_Id='%s', CI_Name='%s', CI_UUID='%s', Pla_Id='%s', CC_Id='%s', CIT_Generation='%s', Cus_Id='%s')>" % \
                ( self.CI_Id, self.CI_Name, self.CI_UUID, self.Pla_Id, self.CC_Id, self.CIT_Generation, self.Cus_Id)

# =============================================================================


