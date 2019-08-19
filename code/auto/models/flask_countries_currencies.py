# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-18 18:05:34
# =============================================================================

class country_currency(db.Model):
    __tablename__ = 'Countries_Currencies'
    Cou_Code        = db.Column( db.String(2), db.ForeignKey('Countries.Cou_Code'), primary_key=True )
    Cur_Code        = db.Column( db.String(3), db.ForeignKey('Currencies.Cur_Code'), primary_key=True )
    Cou_Cur_Comment = db.Column( db.String(45) )


    def __init__(self, Cou_Code='None', Cur_Code='None', Cou_Cur_Comment='None'):
        self.Cou_Code        = Cou_Code
        self.Cur_Code        = Cur_Code
        self.Cou_Cur_Comment = Cou_Cur_Comment

    def __repr__(self):
        return "<Countries_Currencies( Cou_Code='%s', Cur_Code='%s', Cou_Cur_Comment='%s')>" % \
                ( self.Cou_Code, self.Cur_Code, self.Cou_Cur_Comment)

