# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-18 18:05:34
# =============================================================================

from decimal import ROUND_HALF_UP

class frm_platform(Form):
    Pla_Name             = StringField("Name?")
    Pla_Host             = StringField("Host?")
    Pla_Port             = StringField("Port?")
    Pla_User             = StringField("User?")
    Pla_Password         = StringField("Password?")

    submit_Save          = SubmitField  ('Save')
    submit_New           = SubmitField  ('New')
    submit_Cancel        = SubmitField  ('Cancel')

    has_FKs              = False

class frm_platform_delete(Form):
    submit_Delete        = SubmitField  ('Delete')
    submit_Cancel        = SubmitField  ('Cancel')

# =============================================================================
