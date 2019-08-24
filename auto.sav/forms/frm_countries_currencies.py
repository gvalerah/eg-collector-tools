# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-20 18:43:44
# =============================================================================

from decimal import ROUND_HALF_UP

class frm_country_currency(Form):
    Cou_Code                = SelectField("Country Code?", validators=[Required()])
    Cur_Code                = SelectField("Currency Code?", validators=[Required()])
    Cou_Cur_Comment         = StringField("Comment?")

    submit_Save             = SubmitField  ('Save')
    submit_New              = SubmitField  ('New')
    submit_Cancel           = SubmitField  ('Cancel')

    has_FKs                 = True

class frm_country_currency_delete(Form):
    submit_Delete           = SubmitField  ('Delete')
    submit_Cancel           = SubmitField  ('Cancel')

# =============================================================================
