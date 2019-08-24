# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-20 18:43:44
# =============================================================================

from decimal import ROUND_HALF_UP

class frm_charge_unit(Form):
    CI_Id                          = SelectField("Configuration Item Id?", coerce=int, validators=[Required()])
    CU_Description                 = StringField("Description?")
    CU_UUID                        = StringField("UUID?")
    CU_Is_Billeable                = BooleanField("Is Billeable?")
    CU_Is_Always_Billeable         = BooleanField("Is Always Billeable?")
    CU_Quantity                    = DecimalField("Quantity?", validators=[Required()], places=6, rounding=ROUND_HALF_UP)
    CU_Operation                   = SelectField("Conversion Operation?", validators=[Required()])
    Typ_Code                       = SelectField("Type?", validators=[Required()])
    CIT_Generation                 = SelectField("Item Generation Type?", coerce=int, validators=[Required()])
    CU_Reference_1                 = StringField("Reference 1?")
    CU_Reference_2                 = StringField("Reference 2?")
    CU_Reference_3                 = StringField("Reference 3?")

    submit_Save                    = SubmitField  ('Save')
    submit_New                     = SubmitField  ('New')
    submit_Cancel                  = SubmitField  ('Cancel')

    has_FKs                        = True

class frm_charge_unit_delete(Form):
    submit_Delete                  = SubmitField  ('Delete')
    submit_Cancel                  = SubmitField  ('Cancel')

# =============================================================================
