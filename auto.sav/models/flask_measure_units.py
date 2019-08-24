# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-20 18:43:44
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

