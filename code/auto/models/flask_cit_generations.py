# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-16 15:51:37
# =============================================================================

class cit_generation(db.Model):
    __tablename__ = 'CIT_Generations'
    CIT_Generation = db.Column( db.Integer, primary_key=True )
    Value          = db.Column( db.String(45) )

    charge_units   = db.relationship('charge_unit',backref='cit_generation')

    def __init__(self, CIT_Generation=None, Value='None'):
        self.CIT_Generation = CIT_Generation
        self.Value          = Value

    def __repr__(self):
        return "<CIT_Generations( CIT_Generation='%s', Value='%s')>" % \
                ( self.CIT_Generation, self.Value)

