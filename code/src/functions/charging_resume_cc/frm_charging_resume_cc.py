# =============================================================================
# Billing Resume FORM per CC
# (c) Sertechno 2019
# GLVH @ 2018-03-11
# =============================================================================


# =============================================================================
class frm_charging_resume_cc(Form):
    CC_Id           = SelectField  ("Cost Center?", validators=[DataRequired()], coerce=int)
    CIT_Date_From    = DateField    ("Billing Data from?", validators=[DataRequired()], format="%Y-%m-%d")
    CIT_Date_To      = DateField    ("Billing Data up to?", validators=[DataRequired()], format="%Y-%m-%d")
    CIT_Status       = SelectField  ("Status to Report?", coerce=int)
    Cur_Code         = SelectField  ("Currency to Report?", coerce=str)

    submit_Report    = SubmitField  ('Report')
    submit_Update    = SubmitField  ('Update & Report')
    submit_Cancel    = SubmitField  ('Cancel')

