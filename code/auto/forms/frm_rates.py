# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-16 15:51:37
# =============================================================================

from decimal import ROUND_HALF_UP

class frm_rate(Form):
    Typ_Code           = SelectField("Charge Unit Type?", validators=[Required()])
    Cus_Id             = SelectField("Customer Id?", coerce=int, validators=[Required()])
    Pla_Id             = SelectField("Platform Id?", coerce=int, validators=[Required()])
    CC_Id              = SelectField("Cost Center Id?", coerce=int, validators=[Required()])
    CI_Id              = SelectField("Configuration Item?", coerce=int, validators=[Required()])
    Rat_Price          = DecimalField("Rate Price?", validators=[Required()], places=6, rounding=ROUND_HALF_UP)
    Cur_Code           = SelectField("Currency Code?", validators=[Required()])
    MU_Code            = SelectField("Measure Unit?", validators=[Required()])
    Rat_Period         = RadioField("Period?", coerce=int, validators=[Required()])

    submit_Save        = SubmitField  ('Save')
    submit_New         = SubmitField  ('New')
    submit_Cancel      = SubmitField  ('Cancel')

    has_FKs            = True

class frm_rate_delete(Form):
    submit_Delete      = SubmitField  ('Delete')
    submit_Cancel      = SubmitField  ('Cancel')

# =============================================================================
