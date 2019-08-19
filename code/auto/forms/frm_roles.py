# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-18 18:05:34
# =============================================================================

from decimal import ROUND_HALF_UP

class frm_Role(Form):
    id                  = IntegerField("id?", validators=[Required()])
    name                = StringField("name?")
    default             = BooleanField("default?")
    permissions         = IntegerField("permissions?")

    submit_Save         = SubmitField  ('Save')
    submit_New          = SubmitField  ('New')
    submit_Cancel       = SubmitField  ('Cancel')

    has_FKs             = False

class frm_Role_delete(Form):
    submit_Delete       = SubmitField  ('Delete')
    submit_Cancel       = SubmitField  ('Cancel')

# =============================================================================
