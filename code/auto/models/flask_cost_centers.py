# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-18 18:05:34
# =============================================================================

class cost_center(db.Model):
    __tablename__ = 'Cost_Centers'
    CC_Id          = db.Column( db.Integer, primary_key=True, autoincrement=True )
    CC_Code        = db.Column( db.String(45) )
    CC_Description = db.Column( db.String(45) )
    Cur_Code       = db.Column( db.String(3), db.ForeignKey('Currencies.Cur_Code') )
    CC_Parent_Code = db.Column( db.String(45), default='1' )

    configuration_items = db.relationship('configuration_item',backref='cost_center')
    customers      = db.relationship('customer',backref='cost_center')
    rates          = db.relationship('rate',backref='cost_center')
    users          = db.relationship('User',backref='cost_center')

    def __init__(self, CC_Id=0, CC_Code='None', CC_Description='None', Cur_Code='None', CC_Parent_Code='1'):
        self.CC_Id          = CC_Id
        self.CC_Code        = CC_Code
        self.CC_Description = CC_Description
        self.Cur_Code       = Cur_Code
        self.CC_Parent_Code = CC_Parent_Code

    def __repr__(self):
        return "<Cost_Centers( CC_Id='%s', CC_Code='%s', CC_Description='%s', Cur_Code='%s', CC_Parent_Code='%s')>" % \
                ( self.CC_Id, self.CC_Code, self.CC_Description, self.Cur_Code, self.CC_Parent_Code)

