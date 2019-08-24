# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-20 18:43:44
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

