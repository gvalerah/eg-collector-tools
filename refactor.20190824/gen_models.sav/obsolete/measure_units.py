# =============================================================================

# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-11-30 16:47:18
# =============================================================================


class measure_unit(db.Model):
    __tablename__ = 'Measure_Units'
    MU_Code        = db.Column( db.String(3), primary_key=True )
    MU_Description = db.Column( db.String(45) )

    rates          = db.relationship('rate',backref='measure_unit')

    def __init__(self, MU_Code='None', MU_Description='None'):
        self.MU_Code        = MU_Code
        self.MU_Description = MU_Description

    def __repr__(self):
        return "<Measure_Units( MU_Code='%s', MU_Description='%s')>" % \
                ( self.MU_Code, self.MU_Description)

# =============================================================================

class frm_measure_unit(Form):
    MU_Code                = StringField  ("Code?", validators=[Required()])
    MU_Description         = StringField  ("Description?")

    submit_Save            = SubmitField  ('Save')
    submit_New             = SubmitField  ('New')
    submit_Cancel          = SubmitField  ('Cancel')

    has_FKs                = False

# =============================================================================

class frm_measure_unit_delete(Form):
    submit_Delete          = SubmitField  ('Delete')
    submit_Cancel          = SubmitField  ('Cancel')

# =============================================================================

class Measure_Units(Base):
    __tablename__ = 'Measure_Units'
    engine        = None

    MU_Code        = Column( String(3), primary_key=True )
    MU_Description = Column( String(45) )

    def __init__(self, MU_Code, MU_Description):
        self.set( MU_Code, MU_Description)

    def __repr__(self):
        return "<Measure_Units( MU_Code='%s', MU_Description='%s')>" % \
                ( self.MU_Code, self.MU_Description)

# =============================================================================


