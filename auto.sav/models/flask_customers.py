# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-20 18:43:44
# =============================================================================

class customer(db.Model):
    __tablename__ = 'Customers'
    Cus_Id   = db.Column( db.Integer, primary_key=True, autoincrement=True )
    Cus_Name = db.Column( db.String(45) )
    CC_Id    = db.Column( db.Integer, db.ForeignKey('Cost_Centers.CC_Id') )

    configuration_items = db.relationship('configuration_item',backref='customer')
    rates    = db.relationship('rate',backref='customer')

    def __init__(self, Cus_Id=0, Cus_Name='None', CC_Id=None):
        self.Cus_Id   = Cus_Id
        self.Cus_Name = Cus_Name
        self.CC_Id    = CC_Id

    def __repr__(self):
        return "<Customers( Cus_Id='%s', Cus_Name='%s', CC_Id='%s')>" % \
                ( self.Cus_Id, self.Cus_Name, self.CC_Id)

