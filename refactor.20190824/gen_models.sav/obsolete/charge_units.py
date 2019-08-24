# =============================================================================

# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-11-30 16:47:18
# =============================================================================


class charge_unit(db.Model):
    __tablename__ = 'Charge_Units'
    CU_Id                  = db.Column( db.Integer, primary_key=True, autoincrement=True )
    CI_Id                  = db.Column( db.Integer, db.ForeignKey('Configuration_Items.CI_Id') )
    CU_Description         = db.Column( db.String(45) )
    CU_UUID                = db.Column( db.String(45) )
    CU_Is_Billeable        = db.Column( db.Boolean )
    CU_Is_Always_Billeable = db.Column( db.Boolean )
    CU_Quantity            = db.Column( db.Numeric(20,6) )
    CU_Operation           = db.Column( db.String(10), db.ForeignKey('CU_Operations.CU_Operation') )
    Typ_Code               = db.Column( db.String(10), db.ForeignKey('CU_Types.Typ_Code') )
    CC_Id                  = db.Column( db.Integer, db.ForeignKey('Cost_Centers.CC_Id') )
    CIT_Generation         = db.Column( db.Integer, db.ForeignKey('CIT_Generations.CIT_Generation') )
    Rat_Id                 = db.Column( db.Integer )
    CU_Reference_1         = db.Column( db.String(45) )
    CU_Reference_2         = db.Column( db.String(45) )
    CU_Reference_3         = db.Column( db.String(45) )

    charge_items           = db.relationship('charge_item',backref='charge_unit')
    rates                  = db.relationship('rate',backref='charge_unit')

    def __init__(self, CU_Id=0, CI_Id=None, CU_Description='None', CU_UUID='None', CU_Is_Billeable=0, CU_Is_Always_Billeable=0, CU_Quantity=None, CU_Operation='None', Typ_Code='None', CC_Id=None, CIT_Generation=None, Rat_Id=None, CU_Reference_1='None', CU_Reference_2='None', CU_Reference_3='None'):
        self.CU_Id                  = CU_Id
        self.CI_Id                  = CI_Id
        self.CU_Description         = CU_Description
        self.CU_UUID                = CU_UUID
        self.CU_Is_Billeable        = CU_Is_Billeable
        self.CU_Is_Always_Billeable = CU_Is_Always_Billeable
        self.CU_Quantity            = CU_Quantity
        self.CU_Operation           = CU_Operation
        self.Typ_Code               = Typ_Code
        self.CC_Id                  = CC_Id
        self.CIT_Generation         = CIT_Generation
        self.Rat_Id                 = Rat_Id
        self.CU_Reference_1         = CU_Reference_1
        self.CU_Reference_2         = CU_Reference_2
        self.CU_Reference_3         = CU_Reference_3

    def __repr__(self):
        return "<Charge_Units( CU_Id='%s', CI_Id='%s', CU_Description='%s', CU_UUID='%s', CU_Is_Billeable='%s', CU_Is_Always_Billeable='%s', CU_Quantity='%s', CU_Operation='%s', Typ_Code='%s', CC_Id='%s', CIT_Generation='%s', Rat_Id='%s', CU_Reference_1='%s', CU_Reference_2='%s', CU_Reference_3='%s')>" % \
                ( self.CU_Id, self.CI_Id, self.CU_Description, self.CU_UUID, self.CU_Is_Billeable, self.CU_Is_Always_Billeable, self.CU_Quantity, self.CU_Operation, self.Typ_Code, self.CC_Id, self.CIT_Generation, self.Rat_Id, self.CU_Reference_1, self.CU_Reference_2, self.CU_Reference_3)

# =============================================================================

class frm_charge_unit(Form):
    CI_Id                          = SelectField  ("Configuration Item Id?", coerce=int, validators=[Required()])
    CU_Description                 = StringField  ("Description?")
    CU_UUID                        = StringField  ("UUID?")
    CU_Is_Billeable                = BooleanField ("Is Billeable?")
    CU_Is_Always_Billeable         = BooleanField ("Is Always Billeable?")
    CU_Quantity                    = DecimalField ("Quantity?", validators=[Required()])
    CU_Operation                   = SelectField  ("Conversion Operation?", validators=[Required()])
    Typ_Code                       = SelectField  ("Type?", validators=[Required()])
    CC_Id                          = SelectField  ("Cost Center Id?", coerce=int, validators=[Required()])
    CIT_Generation                 = SelectField  ("Item Generation Type?", coerce=int, validators=[Required()])
    CU_Reference_1                 = StringField  ("Reference 1?")
    CU_Reference_2                 = StringField  ("Reference 2?")
    CU_Reference_3                 = StringField  ("Reference 3?")

    submit_Save                    = SubmitField  ('Save')
    submit_New                     = SubmitField  ('New')
    submit_Cancel                  = SubmitField  ('Cancel')

    has_FKs                        = True

# =============================================================================

class frm_charge_unit_delete(Form):
    submit_Delete                  = SubmitField  ('Delete')
    submit_Cancel                  = SubmitField  ('Cancel')

# =============================================================================

class Charge_Units(Base):
    __tablename__ = 'Charge_Units'
    engine        = None

    CU_Id                  = Column( Integer, primary_key=True, autoincrement=True )
    CI_Id                  = Column( Integer, ForeignKey('Configuration_Items.CI_Id') )
    CU_Description         = Column( String(45) )
    CU_UUID                = Column( String(45) )
    CU_Is_Billeable        = Column( Boolean )
    CU_Is_Always_Billeable = Column( Boolean )
    CU_Quantity            = Column( Numeric(20,6) )
    CU_Operation           = Column( String(10), ForeignKey('CU_Operations.CU_Operation') )
    Typ_Code               = Column( String(10), ForeignKey('CU_Types.Typ_Code') )
    CC_Id                  = Column( Integer, ForeignKey('Cost_Centers.CC_Id') )
    CIT_Generation         = Column( Integer, ForeignKey('CIT_Generations.CIT_Generation') )
    Rat_Id                 = Column( Integer )
    CU_Reference_1         = Column( String(45) )
    CU_Reference_2         = Column( String(45) )
    CU_Reference_3         = Column( String(45) )

    def __init__(self, CU_Id, CI_Id, CU_Description, CU_UUID, CU_Is_Billeable, CU_Is_Always_Billeable, CU_Quantity, CU_Operation, Typ_Code, CC_Id, CIT_Generation, Rat_Id, CU_Reference_1, CU_Reference_2, CU_Reference_3):
        self.set( CU_Id, CI_Id, CU_Description, CU_UUID, CU_Is_Billeable, CU_Is_Always_Billeable, CU_Quantity, CU_Operation, Typ_Code, CC_Id, CIT_Generation, Rat_Id, CU_Reference_1, CU_Reference_2, CU_Reference_3)

    def __repr__(self):
        return "<Charge_Units( CU_Id='%s', CI_Id='%s', CU_Description='%s', CU_UUID='%s', CU_Is_Billeable='%s', CU_Is_Always_Billeable='%s', CU_Quantity='%s', CU_Operation='%s', Typ_Code='%s', CC_Id='%s', CIT_Generation='%s', Rat_Id='%s', CU_Reference_1='%s', CU_Reference_2='%s', CU_Reference_3='%s')>" % \
                ( self.CU_Id, self.CI_Id, self.CU_Description, self.CU_UUID, self.CU_Is_Billeable, self.CU_Is_Always_Billeable, self.CU_Quantity, self.CU_Operation, self.Typ_Code, self.CC_Id, self.CIT_Generation, self.Rat_Id, self.CU_Reference_1, self.CU_Reference_2, self.CU_Reference_3)

# =============================================================================


