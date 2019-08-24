# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-15 15:05:30
# =============================================================================

class Dev_Forms(Base):
    __tablename__ = 'Dev_Forms'
    engine        = None
    Id                = Column( Integer, primary_key=True, autoincrement=True )
    Table             = Column( String(45) )
    Field             = Column( String(45) )
    Type              = Column( String(45) )
    Null              = Column( String(45) )
    Key               = Column( String(45) )
    Default           = Column( String(45) )
    Extra             = Column( String(45) )
    Foreign_Key       = Column( String(45) )
    Referenced_Table  = Column( String(45) )
    Foreign_Field     = Column( String(45) )
    Foreign_Value     = Column( String(45) )
    Length            = Column( Integer )
    Validation        = Column( Boolean )
    Validation_Type   = Column( String(45) )
    Validation_String = Column( String(128) )
    Caption_String    = Column( String(45) )
    Field_Order       = Column( Integer )
    Field_Format      = Column( String(45) )
    Form_Editable     = Column( Boolean )
    ORM_Schema        = Column( Boolean )
    
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


