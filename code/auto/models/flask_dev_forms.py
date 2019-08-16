# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-16 15:51:37
# =============================================================================

class dev_form(db.Model):
    __tablename__ = 'Dev_Forms'
    Id                = db.Column( db.Integer, primary_key=True, autoincrement=True )
    Table             = db.Column( db.String(45) )
    Field             = db.Column( db.String(45) )
    Type              = db.Column( db.String(45) )
    Null              = db.Column( db.String(45) )
    Key               = db.Column( db.String(45) )
    Default           = db.Column( db.String(45) )
    Extra             = db.Column( db.String(45) )
    Foreign_Key       = db.Column( db.String(45) )
    Referenced_Table  = db.Column( db.String(45) )
    Foreign_Field     = db.Column( db.String(45) )
    Foreign_Value     = db.Column( db.String(45) )
    Length            = db.Column( db.Integer )
    Validation        = db.Column( db.Boolean )
    Validation_Type   = db.Column( db.String(45) )
    Validation_String = db.Column( db.String(128) )
    Caption_String    = db.Column( db.String(45) )
    Field_Order       = db.Column( db.Integer )
    Field_Format      = db.Column( db.String(45) )
    Form_Editable     = db.Column( db.Boolean, default=1 )
    ORM_Schema        = db.Column( db.Boolean, default=1 )


    def __init__(self, Id=0, Table='None', Field='None', Type='None', Null='None', Key='None', Default='None', Extra='None', Foreign_Key='None', Referenced_Table='None', Foreign_Field='None', Foreign_Value='None', Length=None, Validation=None, Validation_Type='None', Validation_String='None', Caption_String='None', Field_Order=None, Field_Format='None', Form_Editable=1, ORM_Schema=1):
        self.Id                = Id
        self.Table             = Table
        self.Field             = Field
        self.Type              = Type
        self.Null              = Null
        self.Key               = Key
        self.Default           = Default
        self.Extra             = Extra
        self.Foreign_Key       = Foreign_Key
        self.Referenced_Table  = Referenced_Table
        self.Foreign_Field     = Foreign_Field
        self.Foreign_Value     = Foreign_Value
        self.Length            = Length
        self.Validation        = Validation
        self.Validation_Type   = Validation_Type
        self.Validation_String = Validation_String
        self.Caption_String    = Caption_String
        self.Field_Order       = Field_Order
        self.Field_Format      = Field_Format
        self.Form_Editable     = Form_Editable
        self.ORM_Schema        = ORM_Schema

    def __repr__(self):
        return "<Dev_Forms( Id='%s', Table='%s', Field='%s', Type='%s', Null='%s', Key='%s', Default='%s', Extra='%s', Foreign_Key='%s', Referenced_Table='%s', Foreign_Field='%s', Foreign_Value='%s', Length='%s', Validation='%s', Validation_Type='%s', Validation_String='%s', Caption_String='%s', Field_Order='%s', Field_Format='%s', Form_Editable='%s', ORM_Schema='%s')>" % \
                ( self.Id, self.Table, self.Field, self.Type, self.Null, self.Key, self.Default, self.Extra, self.Foreign_Key, self.Referenced_Table, self.Foreign_Field, self.Foreign_Value, self.Length, self.Validation, self.Validation_Type, self.Validation_String, self.Caption_String, self.Field_Order, self.Field_Format, self.Form_Editable, self.ORM_Schema)

