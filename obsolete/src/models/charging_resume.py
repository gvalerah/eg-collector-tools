# =============================================================================
# Billing Resume FORM
# (c) Sertechno 2018
# GLVH @ 2018-11-10 22:23:58
# =============================================================================


# =============================================================================
class frm_charging_resume(Form):
    Cus_Id           = SelectField  ("Customer?", validators=[Required()], coerce=int)
    CIT_Date_From    = StringField  ("Billing Data from?", validators=[Required()])
    CIT_Date_To      = StringField  ("Billing Data up to?", validators=[Required()])
    CIT_Status       = SelectField  ("Status to Report?", coerce=int)
    Cur_Code         = SelectField  ("Currency to Report?", coerce=str)

    submit_Report    = SubmitField  ('Report')
    submit_Update    = SubmitField  ('Update & Report')
    submit_Cancel    = SubmitField  ('Cancel')

