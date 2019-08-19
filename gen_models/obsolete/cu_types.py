# =============================================================================

# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-11-30 16:47:18
# =============================================================================


class cu_type(db.Model):
    __tablename__ = 'CU_Types'
    Typ_Code        = db.Column( db.String(10), primary_key=True )
    Typ_Description = db.Column( db.String(45) )

    charge_units    = db.relationship('charge_unit',backref='cu_type')
    rates           = db.relationship('rate',backref='cu_type')

    def __init__(self, Typ_Code='None', Typ_Description='None'):
        self.Typ_Code        = Typ_Code
        self.Typ_Description = Typ_Description

    def __repr__(self):
        return "<CU_Types( Typ_Code='%s', Typ_Description='%s')>" % \
                ( self.Typ_Code, self.Typ_Description)

# =============================================================================

class frm_cu_type(Form):
    Typ_Code                = StringField  ("Type?", validators=[Required()])
    Typ_Description         = StringField  ("Description?")

    submit_Save             = SubmitField  ('Save')
    submit_New              = SubmitField  ('New')
    submit_Cancel           = SubmitField  ('Cancel')

    has_FKs                 = False

# =============================================================================

class frm_cu_type_delete(Form):
    submit_Delete           = SubmitField  ('Delete')
    submit_Cancel           = SubmitField  ('Cancel')

# =============================================================================

class CU_Types(Base):
    __tablename__ = 'CU_Types'
    engine        = None

    Typ_Code        = Column( String(10), primary_key=True )
    Typ_Description = Column( String(45) )

    def __init__(self, Typ_Code, Typ_Description):
        self.set( Typ_Code, Typ_Description)

    def __repr__(self):
        return "<CU_Types( Typ_Code='%s', Typ_Description='%s')>" % \
                ( self.Typ_Code, self.Typ_Description)

# =============================================================================


