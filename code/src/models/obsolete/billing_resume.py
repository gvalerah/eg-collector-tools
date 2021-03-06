# =============================================================================
# Billing Resume FORM
# (c) Sertechno 2018
# GLVH @ 2018-11-10 22:23:58
# =============================================================================

"""
class country(db.Model):
    __tablename__ = 'Countries'
    Cou_Code = db.Column( db.String(2), primary_key=True )
    Cou_Name = db.Column( db.String(45) )
    Cou_A3   = db.Column( db.String(3) )
    Cou_N    = db.Column( db.Integer )

    countries_currencies = db.relationship('country_currency',backref='country')

    def __init__(self, Cou_Code=None, Cou_Name=None, Cou_A3=None, Cou_N=None):
        self.Cou_Code = Cou_Code
        self.Cou_Name = Cou_Name
        self.Cou_A3   = Cou_A3
        self.Cou_N    = Cou_N

    def __repr__(self):
        return "<Countries( Cou_Code='%s', Cou_Name='%s', Cou_A3='%s', Cou_N='%s')>" % \
                ( self.Cou_Code, self.Cou_Name, self.Cou_A3, self.Cou_N)
"""
# =============================================================================
class frm_billing_resume(Form):
    Cus_Id           = SelectField ("Customer?", validators=[Required()], coerce=int)
    CIT_Date_From    = StringField  ("Billing Data from?", validators=[Required()])
    CIT_Date_To      = StringField  ("Billing Data up to?", validators=[Required()])
    CIT_Status       = SelectField ("Status to Report?", coerce=int)
    Cur_Code         = SelectField  ("Currency to Report?", coerce=str)

    submit_Report    = SubmitField  ('Report')
    submit_Cancel    = SubmitField  ('Cancel')
    
    has_FKs          = False
