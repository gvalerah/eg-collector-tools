# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-16 15:51:37
# =============================================================================

from decimal import ROUND_HALF_UP

class frm_currency(Form):
    Cur_Code            = StringField("Code?", validators=[Required()])
    Cur_Name            = StringField("Name?")
    Cur_Id              = IntegerField("Id?")
    Cur_Comment         = StringField("Comment?")

    submit_Save         = SubmitField  ('Save')
    submit_New          = SubmitField  ('New')
    submit_Cancel       = SubmitField  ('Cancel')

    has_FKs             = False

class frm_currency_delete(Form):
    submit_Delete       = SubmitField  ('Delete')
    submit_Cancel       = SubmitField  ('Cancel')

# =============================================================================
