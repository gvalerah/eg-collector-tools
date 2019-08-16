# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-16 15:51:37
# =============================================================================

from decimal import ROUND_HALF_UP

class frm_exchange_rate(Form):
    Cur_Code          = SelectField("Currency Code?", validators=[Required()])
    ER_Factor         = DecimalField("Factor?", validators=[Required()], places=6, rounding=ROUND_HALF_UP)
    ER_Date           = DateField("Date?", format='%Y-%m-%d')

    submit_Save       = SubmitField  ('Save')
    submit_New        = SubmitField  ('New')
    submit_Cancel     = SubmitField  ('Cancel')

    has_FKs           = True

class frm_exchange_rate_delete(Form):
    submit_Delete     = SubmitField  ('Delete')
    submit_Cancel     = SubmitField  ('Cancel')

# =============================================================================
