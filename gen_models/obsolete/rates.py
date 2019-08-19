# =============================================================================

# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-11-30 16:47:18
# =============================================================================


class rate(db.Model):
    __tablename__ = 'Rates'
    Rat_Id     = db.Column( db.Integer, primary_key=True, autoincrement=True )
    Typ_Code   = db.Column( db.String(10), db.ForeignKey('CU_Types.Typ_Code') )
    Cus_Id     = db.Column( db.Integer, db.ForeignKey('Customers.Cus_Id') )
    Pla_Id     = db.Column( db.Integer, db.ForeignKey('Platforms.Pla_Id') )
    CC_Id      = db.Column( db.Integer, db.ForeignKey('Cost_Centers.CC_Id') )
    CU_Id      = db.Column( db.Integer, db.ForeignKey('Charge_Units.CU_Id') )
    Rat_Price  = db.Column( db.Numeric(20,6) )
    Cur_Code   = db.Column( db.String(3), db.ForeignKey('Currencies.Cur_Code') )
    MU_Code    = db.Column( db.String(3), db.ForeignKey('Measure_Units.MU_Code') )
    Rat_Period = db.Column( db.Integer, db.ForeignKey('Rat_Periods.Rat_Period') )
    Rat_Type   = db.Column( db.Integer )


    def __init__(self, Rat_Id=0, Typ_Code='None', Cus_Id=None, Pla_Id=None, CC_Id=None, CU_Id=None, Rat_Price=None, Cur_Code='None', MU_Code='None', Rat_Period=None, Rat_Type=None):
        self.Rat_Id     = Rat_Id
        self.Typ_Code   = Typ_Code
        self.Cus_Id     = Cus_Id
        self.Pla_Id     = Pla_Id
        self.CC_Id      = CC_Id
        self.CU_Id      = CU_Id
        self.Rat_Price  = Rat_Price
        self.Cur_Code   = Cur_Code
        self.MU_Code    = MU_Code
        self.Rat_Period = Rat_Period
        self.Rat_Type   = Rat_Type

    def __repr__(self):
        return "<Rates( Rat_Id='%s', Typ_Code='%s', Cus_Id='%s', Pla_Id='%s', CC_Id='%s', CU_Id='%s', Rat_Price='%s', Cur_Code='%s', MU_Code='%s', Rat_Period='%s', Rat_Type='%s')>" % \
                ( self.Rat_Id, self.Typ_Code, self.Cus_Id, self.Pla_Id, self.CC_Id, self.CU_Id, self.Rat_Price, self.Cur_Code, self.MU_Code, self.Rat_Period, self.Rat_Type)

# =============================================================================

class frm_rate(Form):
    Typ_Code           = SelectField  ("Charge Unit Type?", validators=[Required()])
    Cus_Id             = SelectField  ("Customer Id?", coerce=int, validators=[Required()])
    Pla_Id             = SelectField  ("Platform Id?", coerce=int, validators=[Required()])
    CC_Id              = SelectField  ("Cost Center Id?", coerce=int, validators=[Required()])
    CU_Id              = SelectField  ("Charge Unit Id?", coerce=int, validators=[Required()])
    Rat_Price          = DecimalField ("Rate Price?", validators=[Required()])
    Cur_Code           = SelectField  ("Currency Code?", validators=[Required()])
    MU_Code            = SelectField  ("Measure Unit?", validators=[Required()])
    Rat_Period         = RadioField   ("Period?", coerce=int, validators=[Required()])

    submit_Save        = SubmitField  ('Save')
    submit_New         = SubmitField  ('New')
    submit_Cancel      = SubmitField  ('Cancel')

    has_FKs            = True

# =============================================================================

class frm_rate_delete(Form):
    submit_Delete      = SubmitField  ('Delete')
    submit_Cancel      = SubmitField  ('Cancel')

# =============================================================================

class Rates(Base):
    __tablename__ = 'Rates'
    engine        = None

    Rat_Id     = Column( Integer, primary_key=True, autoincrement=True )
    Typ_Code   = Column( String(10), ForeignKey('CU_Types.Typ_Code') )
    Cus_Id     = Column( Integer, ForeignKey('Customers.Cus_Id') )
    Pla_Id     = Column( Integer, ForeignKey('Platforms.Pla_Id') )
    CC_Id      = Column( Integer, ForeignKey('Cost_Centers.CC_Id') )
    CU_Id      = Column( Integer, ForeignKey('Charge_Units.CU_Id') )
    Rat_Price  = Column( Numeric(20,6) )
    Cur_Code   = Column( String(3), ForeignKey('Currencies.Cur_Code') )
    MU_Code    = Column( String(3), ForeignKey('Measure_Units.MU_Code') )
    Rat_Period = Column( Integer, ForeignKey('Rat_Periods.Rat_Period') )
    Rat_Type   = Column( Integer )

    def __init__(self, Rat_Id, Typ_Code, Cus_Id, Pla_Id, CC_Id, CU_Id, Rat_Price, Cur_Code, MU_Code, Rat_Period, Rat_Type):
        self.set( Rat_Id, Typ_Code, Cus_Id, Pla_Id, CC_Id, CU_Id, Rat_Price, Cur_Code, MU_Code, Rat_Period, Rat_Type)

    def __repr__(self):
        return "<Rates( Rat_Id='%s', Typ_Code='%s', Cus_Id='%s', Pla_Id='%s', CC_Id='%s', CU_Id='%s', Rat_Price='%s', Cur_Code='%s', MU_Code='%s', Rat_Period='%s', Rat_Type='%s')>" % \
                ( self.Rat_Id, self.Typ_Code, self.Cus_Id, self.Pla_Id, self.CC_Id, self.CU_Id, self.Rat_Price, self.Cur_Code, self.MU_Code, self.Rat_Period, self.Rat_Type)

# =============================================================================


