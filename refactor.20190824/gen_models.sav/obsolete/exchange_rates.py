# =============================================================================

# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-11-30 16:47:18
# =============================================================================


class exchange_rate(db.Model):
    __tablename__ = 'Exchange_Rates'
    ER_Id     = db.Column( db.Integer, primary_key=True, autoincrement=True )
    Cur_Code  = db.Column( db.String(3), db.ForeignKey('Currencies.Cur_Code') )
    ER_Factor = db.Column( db.Numeric(20,6) )
    ER_Date   = db.Column( db.Date )


    def __init__(self, ER_Id=0, Cur_Code='USD', ER_Factor=None, ER_Date=None):
        self.ER_Id     = ER_Id
        self.Cur_Code  = Cur_Code
        self.ER_Factor = ER_Factor
        self.ER_Date   = ER_Date

    def __repr__(self):
        return "<Exchange_Rates( ER_Id='%s', Cur_Code='%s', ER_Factor='%s', ER_Date='%s')>" % \
                ( self.ER_Id, self.Cur_Code, self.ER_Factor, self.ER_Date)

# =============================================================================

class frm_exchange_rate(Form):
    Cur_Code          = SelectField  ("Currency Code?", validators=[Required()])
    ER_Factor         = DecimalField ("Factor?", validators=[Required()])
    ER_Date           = DateField    ("Date?", format='%Y-%m-%d')

    submit_Save       = SubmitField  ('Save')
    submit_New        = SubmitField  ('New')
    submit_Cancel     = SubmitField  ('Cancel')

    has_FKs           = True

# =============================================================================

class frm_exchange_rate_delete(Form):
    submit_Delete     = SubmitField  ('Delete')
    submit_Cancel     = SubmitField  ('Cancel')

# =============================================================================

class Exchange_Rates(Base):
    __tablename__ = 'Exchange_Rates'
    engine        = None

    ER_Id     = Column( Integer, primary_key=True, autoincrement=True )
    Cur_Code  = Column( String(3), ForeignKey('Currencies.Cur_Code') )
    ER_Factor = Column( Numeric(20,6) )
    ER_Date   = Column( Date )

    def __init__(self, ER_Id, Cur_Code, ER_Factor, ER_Date):
        self.set( ER_Id, Cur_Code, ER_Factor, ER_Date)

    def __repr__(self):
        return "<Exchange_Rates( ER_Id='%s', Cur_Code='%s', ER_Factor='%s', ER_Date='%s')>" % \
                ( self.ER_Id, self.Cur_Code, self.ER_Factor, self.ER_Date)

# =============================================================================


