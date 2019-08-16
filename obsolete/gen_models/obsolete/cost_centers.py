# =============================================================================

# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2018-11-30 16:47:18
# =============================================================================


class cost_center(db.Model):
    __tablename__ = 'Cost_Centers'
    CC_Id          = db.Column( db.Integer, primary_key=True, autoincrement=True )
    CC_Code        = db.Column( db.String(45) )
    CC_Description = db.Column( db.String(45) )
    Cur_Code       = db.Column( db.String(3), db.ForeignKey('Currencies.Cur_Code') )

    charge_units   = db.relationship('charge_unit',backref='cost_center')
    configuration_items = db.relationship('configuration_item',backref='cost_center')
    customers      = db.relationship('customer',backref='cost_center')
    rates          = db.relationship('rate',backref='cost_center')

    def __init__(self, CC_Id=0, CC_Code='None', CC_Description='None', Cur_Code='None'):
        self.CC_Id          = CC_Id
        self.CC_Code        = CC_Code
        self.CC_Description = CC_Description
        self.Cur_Code       = Cur_Code

    def __repr__(self):
        return "<Cost_Centers( CC_Id='%s', CC_Code='%s', CC_Description='%s', Cur_Code='%s')>" % \
                ( self.CC_Id, self.CC_Code, self.CC_Description, self.Cur_Code)

# =============================================================================

class frm_cost_center(Form):
    CC_Code                = StringField  ("Code?")
    CC_Description         = StringField  ("Description?")
    Cur_Code               = SelectField  ("Currency Code?", validators=[Required()])

    submit_Save            = SubmitField  ('Save')
    submit_New             = SubmitField  ('New')
    submit_Cancel          = SubmitField  ('Cancel')

    has_FKs                = True

# =============================================================================

class frm_cost_center_delete(Form):
    submit_Delete          = SubmitField  ('Delete')
    submit_Cancel          = SubmitField  ('Cancel')

# =============================================================================

class Cost_Centers(Base):
    __tablename__ = 'Cost_Centers'
    engine        = None

    CC_Id          = Column( Integer, primary_key=True, autoincrement=True )
    CC_Code        = Column( String(45) )
    CC_Description = Column( String(45) )
    Cur_Code       = Column( String(3), ForeignKey('Currencies.Cur_Code') )

    def __init__(self, CC_Id, CC_Code, CC_Description, Cur_Code):
        self.set( CC_Id, CC_Code, CC_Description, Cur_Code)

    def __repr__(self):
        return "<Cost_Centers( CC_Id='%s', CC_Code='%s', CC_Description='%s', Cur_Code='%s')>" % \
                ( self.CC_Id, self.CC_Code, self.CC_Description, self.Cur_Code)

# =============================================================================


