# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-20 18:43:44
# =============================================================================

from decimal import ROUND_HALF_UP

class frm_configuration_item(Form):
    CI_Name                             = StringField("Name?", validators=[Required()])
    CI_UUID                             = StringField("UUID?", validators=[Required()])
    Pla_Id                              = SelectField("Platform Id?", coerce=int, validators=[Required()])
    CC_Id                               = SelectField("Cost Center Id?", coerce=int, validators=[Required()])
    Cus_Id                              = SelectField("Customer Id?", coerce=int, validators=[Required()])
    CI_Commissioning_DateTime           = DateTimeField("Commissioning Date and Time?", validators=[Required()], format='%Y-%m-%d %H:%M:%S')
    CI_Decommissioning_DateTime         = DateTimeField("Decommissioning Date and Time?", validators=[Optional()], format='%Y-%m-%d %H:%M:%S')

    submit_Save                         = SubmitField  ('Save')
    submit_New                          = SubmitField  ('New')
    submit_Cancel                       = SubmitField  ('Cancel')

    has_FKs                             = True

class frm_configuration_item_delete(Form):
    submit_Delete                       = SubmitField  ('Delete')
    submit_Cancel                       = SubmitField  ('Cancel')

# =============================================================================
