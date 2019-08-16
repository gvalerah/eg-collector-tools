# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-16 15:51:37
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

