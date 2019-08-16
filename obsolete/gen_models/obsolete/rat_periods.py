# =============================================================================

# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-11-30 16:47:18
# =============================================================================


class rat_period(db.Model):
    __tablename__ = 'Rat_Periods'
    Rat_Period = db.Column( db.Integer, primary_key=True )
    Value      = db.Column( db.String(45) )

    rates      = db.relationship('rate',backref='rat_period')

    def __init__(self, Rat_Period=None, Value='None'):
        self.Rat_Period = Rat_Period
        self.Value      = Value

    def __repr__(self):
        return "<Rat_Periods( Rat_Period='%s', Value='%s')>" % \
                ( self.Rat_Period, self.Value)

# =============================================================================

class frm_rat_period(Form):
    Rat_Period         = IntegerField ("Rate Period?", validators=[Required()])
    Value              = StringField  ("Value?")

    submit_Save        = SubmitField  ('Save')
    submit_New         = SubmitField  ('New')
    submit_Cancel      = SubmitField  ('Cancel')

    has_FKs            = False

# =============================================================================

class frm_rat_period_delete(Form):
    submit_Delete      = SubmitField  ('Delete')
    submit_Cancel      = SubmitField  ('Cancel')

# =============================================================================

class Rat_Periods(Base):
    __tablename__ = 'Rat_Periods'
    engine        = None

    Rat_Period = Column( Integer, primary_key=True )
    Value      = Column( String(45) )

    def __init__(self, Rat_Period, Value):
        self.set( Rat_Period, Value)

    def __repr__(self):
        return "<Rat_Periods( Rat_Period='%s', Value='%s')>" % \
                ( self.Rat_Period, self.Value)

# =============================================================================


