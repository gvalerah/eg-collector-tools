# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-16 15:51:37
# =============================================================================

from decimal import ROUND_HALF_UP

class frm_charge_item(Form):
    CU_Id                 = SelectField("Charge Unit Id?", coerce=int, validators=[Required()])
    CIT_Date              = DateField("Date?", validators=[Required()], format='%Y-%m-%d')
    CIT_Time              = TimeField("Time?", validators=[Required()], format='%H-%M-%S')
    CIT_Quantity          = DecimalField("Quantity?", validators=[Required()], places=6, rounding=ROUND_HALF_UP)
    CIT_Status            = SelectField("Status?", coerce=int, validators=[Required()])
    CIT_Is_Active         = BooleanField("Is Active?")

    submit_Save           = SubmitField  ('Save')
    submit_New            = SubmitField  ('New')
    submit_Cancel         = SubmitField  ('Cancel')

    has_FKs               = True

class frm_charge_item_delete(Form):
    submit_Delete         = SubmitField  ('Delete')
    submit_Cancel         = SubmitField  ('Cancel')

# =============================================================================
