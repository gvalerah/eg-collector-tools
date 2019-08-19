# =============================================================================

# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-11-30 16:47:18
# =============================================================================


class cu_operation(db.Model):
    __tablename__ = 'CU_Operations'
    CU_Operation = db.Column( db.String(10), primary_key=True )
    Value        = db.Column( db.String(45) )
    Is_Multiply  = db.Column( db.Boolean )
    Factor       = db.Column( db.Integer )

    charge_units = db.relationship('charge_unit',backref='cu_operation')

    def __init__(self, CU_Operation='None', Value='None', Is_Multiply=None, Factor=None):
        self.CU_Operation = CU_Operation
        self.Value        = Value
        self.Is_Multiply  = Is_Multiply
        self.Factor       = Factor

    def __repr__(self):
        return "<CU_Operations( CU_Operation='%s', Value='%s', Is_Multiply='%s', Factor='%s')>" % \
                ( self.CU_Operation, self.Value, self.Is_Multiply, self.Factor)

# =============================================================================

class frm_cu_operation(Form):
    CU_Operation         = StringField  ("Operation?", validators=[Required()])
    Value                = StringField  ("Value?")
    Is_Multiply          = BooleanField ("Is Multiply?")
    Factor               = IntegerField ("Factor?")

    submit_Save          = SubmitField  ('Save')
    submit_New           = SubmitField  ('New')
    submit_Cancel        = SubmitField  ('Cancel')

    has_FKs              = False

# =============================================================================

class frm_cu_operation_delete(Form):
    submit_Delete        = SubmitField  ('Delete')
    submit_Cancel        = SubmitField  ('Cancel')

# =============================================================================

class CU_Operations(Base):
    __tablename__ = 'CU_Operations'
    engine        = None

    CU_Operation = Column( String(10), primary_key=True )
    Value        = Column( String(45) )
    Is_Multiply  = Column( Boolean )
    Factor       = Column( Integer )

    def __init__(self, CU_Operation, Value, Is_Multiply, Factor):
        self.set( CU_Operation, Value, Is_Multiply, Factor)

    def __repr__(self):
        return "<CU_Operations( CU_Operation='%s', Value='%s', Is_Multiply='%s', Factor='%s')>" % \
                ( self.CU_Operation, self.Value, self.Is_Multiply, self.Factor)

# =============================================================================


