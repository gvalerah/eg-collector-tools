# =============================================================================
# Change CI State
# (c) Sertechno 2018
# GLVH @ 2018-12-06 14:55:00
# =============================================================================

# =============================================================================
class frm_change_cit_state(Form):
    CU_Id            = SelectField  ("Charge Unit?", validators=[Required()], coerce=int)
    CIT_Date_From    = DateField    ("Billing Data from?", validators=[Required()], format="%Y-%m-%d")
    CIT_Time_From    = SelectField  ("Time from?", validators=[Required()])
    CIT_Date_To      = DateField    ("Billing Data up to?", validators=[Required()], format="%Y-%m-%d")
    CIT_Time_To      = SelectField  ("Time to?", validators=[Required()])
    CIT_Status       = SelectField  ("Status to Change from?", coerce=int)
    CIT_Status_To    = SelectField  ("Status to Change to?", coerce=int)

    submit_Search    = SubmitField  ('Search')
    submit_Cancel    = SubmitField  ('Cancel')

class frm_change_cit_state_confirm(Form):

    submit_Change    = SubmitField  ('Change')
    submit_Cancel    = SubmitField  ('Cancel')
# =============================================================================

