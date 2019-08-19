# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-18 18:05:34
# =============================================================================

from decimal import ROUND_HALF_UP

class frm_dev_form(Form):
    Table                     = StringField("Table?")
    Field                     = StringField("Field?")
    Type                      = StringField("Type?")
    Null                      = StringField("Null?")
    Key                       = StringField("Key?")
    Default                   = StringField("Default?")
    Extra                     = StringField("Extra?")
    Foreign_Key               = StringField("Foreign Key?")
    Referenced_Table          = StringField("Referenced Table?")
    Foreign_Field             = StringField("Foreign Field?")
    Foreign_Value             = StringField("Foreign_Value?")
    Length                    = IntegerField("Length?")
    Validation                = BooleanField("Validation?")
    Validation_Type           = StringField("Validation Type?")
    Validation_String         = StringField("Validation String?")
    Caption_String            = StringField("Caption String?")
    Field_Order               = IntegerField("Field Order?")
    Field_Format              = StringField("Field Format?")
    Form_Editable             = BooleanField("Form Editable?")
    ORM_Schema                = BooleanField("None?")

    submit_Save               = SubmitField  ('Save')
    submit_New                = SubmitField  ('New')
    submit_Cancel             = SubmitField  ('Cancel')

    has_FKs                   = False

class frm_dev_form_delete(Form):
    submit_Delete             = SubmitField  ('Delete')
    submit_Cancel             = SubmitField  ('Cancel')

# =============================================================================
