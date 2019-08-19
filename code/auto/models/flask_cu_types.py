# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-18 18:05:34
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

