# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-16 15:51:37
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

