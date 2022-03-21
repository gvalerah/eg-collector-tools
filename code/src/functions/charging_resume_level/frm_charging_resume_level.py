# =============================================================================
# Billing Resume FORM Multilevel Report
# (c) Sertechno 2019
# GLVH @ 2019-04-29
# =============================================================================


# =============================================================================
class frm_charging_resume_level(Form):
    Cus_Id           = SelectField  ("Customer?", validators=[DataRequired()], coerce=int)
    CIT_Date_From    = DateField    ("Billing Data from?", validators=[DataRequired()], format="%Y-%m-%d")
    CIT_Date_To      = DateField    ("Billing Data up to?", validators=[DataRequired()], format="%Y-%m-%d")
    CIT_Status       = SelectField  ("Status to Report?", coerce=int)
    Cur_Code         = SelectField  ("Currency to Report?", coerce=str)
    Level            = SelectField  ("Report Level?", coerce=int)

    submit_Report    = SubmitField  ('Report')
    submit_Update    = SubmitField  ('Update & Report')
    submit_Cancel    = SubmitField  ('Cancel')

