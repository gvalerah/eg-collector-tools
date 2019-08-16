# =============================================================================

# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-11-30 16:47:18
# =============================================================================


class cit_status(db.Model):
    __tablename__ = 'CIT_Statuses'
    CIT_Status = db.Column( db.Integer, primary_key=True )
    Value      = db.Column( db.String(45) )

    charge_items = db.relationship('charge_item',backref='cit_status')

    def __init__(self, CIT_Status=None, Value='None'):
        self.CIT_Status = CIT_Status
        self.Value      = Value

    def __repr__(self):
        return "<CIT_Statuses( CIT_Status='%s', Value='%s')>" % \
                ( self.CIT_Status, self.Value)

# =============================================================================

class frm_cit_status(Form):
    CIT_Status         = IntegerField ("CIT Status?", validators=[Required()])
    Value              = StringField  ("Vallue?")

    submit_Save        = SubmitField  ('Save')
    submit_New         = SubmitField  ('New')
    submit_Cancel      = SubmitField  ('Cancel')

    has_FKs            = False

# =============================================================================

class frm_cit_status_delete(Form):
    submit_Delete      = SubmitField  ('Delete')
    submit_Cancel      = SubmitField  ('Cancel')

# =============================================================================

class CIT_Statuses(Base):
    __tablename__ = 'CIT_Statuses'
    engine        = None

    CIT_Status = Column( Integer, primary_key=True )
    Value      = Column( String(45) )

    def __init__(self, CIT_Status, Value):
        self.set( CIT_Status, Value)

    def __repr__(self):
        return "<CIT_Statuses( CIT_Status='%s', Value='%s')>" % \
                ( self.CIT_Status, self.Value)

# =============================================================================


