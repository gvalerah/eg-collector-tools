# =============================================================================

# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-11-30 16:47:18
# =============================================================================


class cit_generation(db.Model):
    __tablename__ = 'CIT_Generations'
    CIT_Generation = db.Column( db.Integer, primary_key=True )
    Value          = db.Column( db.String(45) )

    charge_units   = db.relationship('charge_unit',backref='cit_generation')
    configuration_items = db.relationship('configuration_item',backref='cit_generation')

    def __init__(self, CIT_Generation=None, Value='None'):
        self.CIT_Generation = CIT_Generation
        self.Value          = Value

    def __repr__(self):
        return "<CIT_Generations( CIT_Generation='%s', Value='%s')>" % \
                ( self.CIT_Generation, self.Value)

# =============================================================================

class frm_cit_generation(Form):
    CIT_Generation         = IntegerField ("CIT_Generation?", validators=[Required()])
    Value                  = StringField  ("Value?")

    submit_Save            = SubmitField  ('Save')
    submit_New             = SubmitField  ('New')
    submit_Cancel          = SubmitField  ('Cancel')

    has_FKs                = False

# =============================================================================

class frm_cit_generation_delete(Form):
    submit_Delete          = SubmitField  ('Delete')
    submit_Cancel          = SubmitField  ('Cancel')

# =============================================================================

class CIT_Generations(Base):
    __tablename__ = 'CIT_Generations'
    engine        = None

    CIT_Generation = Column( Integer, primary_key=True )
    Value          = Column( String(45) )

    def __init__(self, CIT_Generation, Value):
        self.set( CIT_Generation, Value)

    def __repr__(self):
        return "<CIT_Generations( CIT_Generation='%s', Value='%s')>" % \
                ( self.CIT_Generation, self.Value)

# =============================================================================


