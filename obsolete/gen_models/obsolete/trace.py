# =============================================================================

# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-11-30 16:47:18
# =============================================================================


class trace(db.Model):
    __tablename__ = 'Trace'
    ID   = db.Column( db.Integer, primary_key=True, autoincrement=True )
    LINE = db.Column( db.String(128) )


    def __init__(self, ID=0, LINE='None'):
        self.ID   = ID
        self.LINE = LINE

    def __repr__(self):
        return "<Trace( ID='%s', LINE='%s')>" % \
                ( self.ID, self.LINE)

# =============================================================================

class frm_trace(Form):
    LINE         = StringField  ("LINE?")

    submit_Save  = SubmitField  ('Save')
    submit_New   = SubmitField  ('New')
    submit_Cancel = SubmitField  ('Cancel')

    has_FKs      = False

# =============================================================================

class frm_trace_delete(Form):
    submit_Delete = SubmitField  ('Delete')
    submit_Cancel = SubmitField  ('Cancel')

# =============================================================================

class Trace(Base):
    __tablename__ = 'Trace'
    engine        = None

    ID   = Column( Integer, primary_key=True, autoincrement=True )
    LINE = Column( String(128) )

    def __init__(self, ID, LINE):
        self.set( ID, LINE)

    def __repr__(self):
        return "<Trace( ID='%s', LINE='%s')>" % \
                ( self.ID, self.LINE)

# =============================================================================


