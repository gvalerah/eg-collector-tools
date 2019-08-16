# =============================================================================

# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-11-30 16:47:18
# =============================================================================


class charge_item(db.Model):
    __tablename__ = 'Charge_Items'
    CU_Id         = db.Column( db.Integer, db.ForeignKey('Charge_Units.CU_Id'), primary_key=True )
    CIT_Date      = db.Column( db.Date, primary_key=True )
    CIT_Time      = db.Column( db.String(10), primary_key=True )
    CIT_Quantity  = db.Column( db.Numeric(20,6) )
    CIT_Status    = db.Column( db.Integer, db.ForeignKey('CIT_Statuses.CIT_Status') )
    CIT_Is_Active = db.Column( db.Boolean )


    def __init__(self, CU_Id=0, CIT_Date=None, CIT_Time=None, CIT_Quantity=0.000000, CIT_Status=0, CIT_Is_Active=0):
        self.CU_Id         = CU_Id
        self.CIT_Date      = CIT_Date
        self.CIT_Time      = CIT_Time
        self.CIT_Quantity  = CIT_Quantity
        self.CIT_Status    = CIT_Status
        self.CIT_Is_Active = CIT_Is_Active

    def __repr__(self):
        return "<Charge_Items( CU_Id='%s', CIT_Date='%s', CIT_Time='%s', CIT_Quantity='%s', CIT_Status='%s', CIT_Is_Active='%s')>" % \
                ( self.CU_Id, self.CIT_Date, self.CIT_Time, self.CIT_Quantity, self.CIT_Status, self.CIT_Is_Active)

# =============================================================================

class frm_charge_item(Form):
    CU_Id                 = SelectField  ("Charge Unit Id?", coerce=int, validators=[Required()])
    CIT_Date              = DateField    ("Date?", validators=[Required()], format='%Y-%m-%d')
    CIT_Time              = StringField  ("Time?", validators=[Required()])
    CIT_Quantity          = DecimalField ("Quantity?", validators=[Required()])
    CIT_Status            = SelectField  ("Status?", coerce=int, validators=[Required()])
    CIT_Is_Active         = BooleanField ("Is Active?")

    submit_Save           = SubmitField  ('Save')
    submit_New            = SubmitField  ('New')
    submit_Cancel         = SubmitField  ('Cancel')

    has_FKs               = True

# =============================================================================

class frm_charge_item_delete(Form):
    submit_Delete         = SubmitField  ('Delete')
    submit_Cancel         = SubmitField  ('Cancel')

# =============================================================================

class Charge_Items(Base):
    __tablename__ = 'Charge_Items'
    engine        = None

    CU_Id         = Column( Integer, ForeignKey('Charge_Units.CU_Id'), primary_key=True )
    CIT_Date      = Column( Date, primary_key=True )
    CIT_Time      = Column( String(10), primary_key=True )
    CIT_Quantity  = Column( Numeric(20,6) )
    CIT_Status    = Column( Integer, ForeignKey('CIT_Statuses.CIT_Status') )
    CIT_Is_Active = Column( Boolean )

    def __init__(self, CU_Id, CIT_Date, CIT_Time, CIT_Quantity, CIT_Status, CIT_Is_Active):
        self.set( CU_Id, CIT_Date, CIT_Time, CIT_Quantity, CIT_Status, CIT_Is_Active)

    def __repr__(self):
        return "<Charge_Items( CU_Id='%s', CIT_Date='%s', CIT_Time='%s', CIT_Quantity='%s', CIT_Status='%s', CIT_Is_Active='%s')>" % \
                ( self.CU_Id, self.CIT_Date, self.CIT_Time, self.CIT_Quantity, self.CIT_Status, self.CIT_Is_Active)

# =============================================================================


