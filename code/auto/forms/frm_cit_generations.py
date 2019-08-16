# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-16 15:51:37
# =============================================================================

from decimal import ROUND_HALF_UP

class frm_cit_generation(Form):
    CIT_Generation         = IntegerField("CIT_Generation?", validators=[Required()])
    Value                  = StringField("Value?")

    submit_Save            = SubmitField  ('Save')
    submit_New             = SubmitField  ('New')
    submit_Cancel          = SubmitField  ('Cancel')

    has_FKs                = False

class frm_cit_generation_delete(Form):
    submit_Delete          = SubmitField  ('Delete')
    submit_Cancel          = SubmitField  ('Cancel')

# =============================================================================
