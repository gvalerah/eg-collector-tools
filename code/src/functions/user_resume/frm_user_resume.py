# =============================================================================
# Billing Resume FORM for Customer's user
# (c) Sertechno 2018
# GLVH @ 2019-01-04
# =============================================================================


# =============================================================================
class frm_user_resume(Form):
    CIT_Date_From    = DateField    ("Billing Data from ?", validators=[DataRequired()], format="%Y-%m-%d")
    CIT_Date_To      = DateField    ("Billing Data up to ?", validators=[DataRequired()], format="%Y-%m-%d")
    CIT_Status       = SelectField  ("Status to Report ?", coerce=int)
    Cur_Code         = SelectField  ("Currency to Report ?", coerce=str)
    CC_Id            = SelectField  ("Parent Cost Center ?", coerce=int)

    submit_Report    = SubmitField  ('Report')
    submit_Update    = SubmitField  ('Update & Report')
    submit_Cancel    = SubmitField  ('Cancel')

