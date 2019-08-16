# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-16 15:51:37
# =============================================================================

from decimal import ROUND_HALF_UP

class frm_cost_center(Form):
    CC_Code                = StringField("Code?")
    CC_Description         = StringField("Description?")
    Cur_Code               = SelectField("Currency Code?", validators=[Required()])
    CC_Parent_Code         = StringField("CC_Parent_Code?")

    submit_Save            = SubmitField  ('Save')
    submit_New             = SubmitField  ('New')
    submit_Cancel          = SubmitField  ('Cancel')

    has_FKs                = True

class frm_cost_center_delete(Form):
    submit_Delete          = SubmitField  ('Delete')
    submit_Cancel          = SubmitField  ('Cancel')

# =============================================================================
