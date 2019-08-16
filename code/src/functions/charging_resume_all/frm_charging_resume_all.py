# =============================================================================
# Billing Resume FORM All CIs
# (c) Sertechno 2019
# GLVH @ 2019-03-12
# =============================================================================


# =============================================================================
class frm_charging_resume_all(Form):
    CIT_Date_From    = DateField    ("Billing Data from?", validators=[Required()], format="%Y-%m-%d")
    CIT_Date_To      = DateField    ("Billing Data up to?", validators=[Required()], format="%Y-%m-%d")
    CIT_Status       = SelectField  ("Status to Report?", coerce=int)
    Cur_Code         = SelectField  ("Currency to Report?", coerce=str)

    submit_Report    = SubmitField  ('Report')
    submit_Update    = SubmitField  ('Update & Report')
    submit_Cancel    = SubmitField  ('Cancel')

