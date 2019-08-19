# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-18 18:05:34
# =============================================================================

from decimal import ROUND_HALF_UP

class frm_country(Form):
    Cou_Code         = StringField("Code?", validators=[Required()])
    Cou_Name         = StringField("Name?")
    Cou_A3           = StringField("Alphanum Code?")
    Cou_N            = IntegerField("ISO Numeric Code?")

    submit_Save      = SubmitField  ('Save')
    submit_New       = SubmitField  ('New')
    submit_Cancel    = SubmitField  ('Cancel')

    has_FKs          = False

class frm_country_delete(Form):
    submit_Delete    = SubmitField  ('Delete')
    submit_Cancel    = SubmitField  ('Cancel')

# =============================================================================
