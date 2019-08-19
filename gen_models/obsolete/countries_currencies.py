# =============================================================================

# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-11-30 16:47:18
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

# =============================================================================

class frm_country_currency(Form):
    Cou_Code                = SelectField  ("Country Code?", validators=[Required()])
    Cur_Code                = SelectField  ("Currency Code?", validators=[Required()])
    Cou_Cur_Comment         = StringField  ("Comment?")

    submit_Save             = SubmitField  ('Save')
    submit_New              = SubmitField  ('New')
    submit_Cancel           = SubmitField  ('Cancel')

    has_FKs                 = True

# =============================================================================

class frm_country_currency_delete(Form):
    submit_Delete           = SubmitField  ('Delete')
    submit_Cancel           = SubmitField  ('Cancel')

# =============================================================================

class Countries_Currencies(Base):
    __tablename__ = 'Countries_Currencies'
    engine        = None

    Cou_Code        = Column( String(2), ForeignKey('Countries.Cou_Code'), primary_key=True )
    Cur_Code        = Column( String(3), ForeignKey('Currencies.Cur_Code'), primary_key=True )
    Cou_Cur_Comment = Column( String(45) )

    def __init__(self, Cou_Code, Cur_Code, Cou_Cur_Comment):
        self.set( Cou_Code, Cur_Code, Cou_Cur_Comment)

    def __repr__(self):
        return "<Countries_Currencies( Cou_Code='%s', Cur_Code='%s', Cou_Cur_Comment='%s')>" % \
                ( self.Cou_Code, self.Cur_Code, self.Cou_Cur_Comment)

# =============================================================================


