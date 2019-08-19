# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-18 18:05:34
# =============================================================================

class currency(db.Model):
    __tablename__ = 'Currencies'
    Cur_Code    = db.Column( db.String(3), primary_key=True )
    Cur_Name    = db.Column( db.String(45) )
    Cur_Id      = db.Column( db.Integer )
    Cur_Comment = db.Column( db.String(128) )

    cost_centers = db.relationship('cost_center',backref='currency')
    countries_currencies = db.relationship('country_currency',backref='currency')
    exchange_rates = db.relationship('exchange_rate',backref='currency')
    rates       = db.relationship('rate',backref='currency')

    def __init__(self, Cur_Code='None', Cur_Name='None', Cur_Id=None, Cur_Comment='None'):
        self.Cur_Code    = Cur_Code
        self.Cur_Name    = Cur_Name
        self.Cur_Id      = Cur_Id
        self.Cur_Comment = Cur_Comment

    def __repr__(self):
        return "<Currencies( Cur_Code='%s', Cur_Name='%s', Cur_Id='%s', Cur_Comment='%s')>" % \
                ( self.Cur_Code, self.Cur_Name, self.Cur_Id, self.Cur_Comment)

