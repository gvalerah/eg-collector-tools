# =============================================================================

# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-11-30 16:47:18
# =============================================================================


class country(db.Model):
    __tablename__ = 'Countries'
    Cou_Code = db.Column( db.String(2), primary_key=True )
    Cou_Name = db.Column( db.String(45) )
    Cou_A3   = db.Column( db.String(3) )
    Cou_N    = db.Column( db.Integer )

    countries_currencies = db.relationship('country_currency',backref='country')

    def __init__(self, Cou_Code='None', Cou_Name='None', Cou_A3='None', Cou_N=None):
        self.Cou_Code = Cou_Code
        self.Cou_Name = Cou_Name
        self.Cou_A3   = Cou_A3
        self.Cou_N    = Cou_N

    def __repr__(self):
        return "<Countries( Cou_Code='%s', Cou_Name='%s', Cou_A3='%s', Cou_N='%s')>" % \
                ( self.Cou_Code, self.Cou_Name, self.Cou_A3, self.Cou_N)

# =============================================================================

class frm_country(Form):
    Cou_Code         = StringField  ("Code?", validators=[Required()])
    Cou_Name         = StringField  ("Name?")
    Cou_A3           = StringField  ("Alphanum Code?")
    Cou_N            = IntegerField ("ISO Numeric Code?")

    submit_Save      = SubmitField  ('Save')
    submit_New       = SubmitField  ('New')
    submit_Cancel    = SubmitField  ('Cancel')

    has_FKs          = False

# =============================================================================

class frm_country_delete(Form):
    submit_Delete    = SubmitField  ('Delete')
    submit_Cancel    = SubmitField  ('Cancel')

# =============================================================================

class Countries(Base):
    __tablename__ = 'Countries'
    engine        = None

    Cou_Code = Column( String(2), primary_key=True )
    Cou_Name = Column( String(45) )
    Cou_A3   = Column( String(3) )
    Cou_N    = Column( Integer )

    def __init__(self, Cou_Code, Cou_Name, Cou_A3, Cou_N):
        self.set( Cou_Code, Cou_Name, Cou_A3, Cou_N)

    def __repr__(self):
        return "<Countries( Cou_Code='%s', Cou_Name='%s', Cou_A3='%s', Cou_N='%s')>" % \
                ( self.Cou_Code, self.Cou_Name, self.Cou_A3, self.Cou_N)

# =============================================================================


