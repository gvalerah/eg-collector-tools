# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-20 18:43:44
# =============================================================================

from decimal import ROUND_HALF_UP

class frm_cu_operation(Form):
    CU_Operation         = StringField("Operation?", validators=[Required()])
    Value                = StringField("Value?")
    Is_Multiply          = BooleanField("Is Multiply?")
    Factor               = IntegerField("Factor?")

    submit_Save          = SubmitField  ('Save')
    submit_New           = SubmitField  ('New')
    submit_Cancel        = SubmitField  ('Cancel')

    has_FKs              = False

class frm_cu_operation_delete(Form):
    submit_Delete        = SubmitField  ('Delete')
    submit_Cancel        = SubmitField  ('Cancel')

# =============================================================================
