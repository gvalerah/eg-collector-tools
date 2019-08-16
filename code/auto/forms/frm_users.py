# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-16 15:51:37
# =============================================================================

from decimal import ROUND_HALF_UP

class frm_User(Form):
    username              = StringField("username?")
    role_id               = SelectField("role_id?", coerce=int, validators=[Required()])
    email                 = StringField("email?")
    password_hash         = StringField("password_hash?")
    confirmed             = BooleanField("confirmed?")
    CC_Id                 = SelectField("CC_Id?", coerce=int, validators=[Required()])

    submit_Save           = SubmitField  ('Save')
    submit_New            = SubmitField  ('New')
    submit_Cancel         = SubmitField  ('Cancel')

    has_FKs               = True

class frm_User_delete(Form):
    submit_Delete         = SubmitField  ('Delete')
    submit_Cancel         = SubmitField  ('Cancel')

# =============================================================================
