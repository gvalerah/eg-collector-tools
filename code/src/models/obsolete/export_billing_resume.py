# =============================================================================
# Export Billing Resume FORM
# (c) Sertechno 2018
# GLVH @ 2018-11-17
# =============================================================================

# =============================================================================
class frm_export_billing_resume(Form):
    Cus_Id          = SelectField ("Customer?", validators=[Required()], coerce=int)
    CIT_Date_From   = StringField ("Billing Data from?", validators=[Required()])
    CIT_Date_To     = StringField ("Billing Data up to?", validators=[Required()])
    CIT_Status      = SelectField ("Status to Export?", coerce=int)
    Cur_Code        = SelectField ("Currency to Report?", coerce=str)

    submit_PDF      = SubmitField ('PDF')
    submit_XLS      = SubmitField ('XLS')
    submit_CSV      = SubmitField ('CSV')
    submit_JSON     = SubmitField ('JSON')
    submit_FIX      = SubmitField ('FIX')
    submit_Cancel   = SubmitField ('Cancel')
    
    has_FKs         = False
