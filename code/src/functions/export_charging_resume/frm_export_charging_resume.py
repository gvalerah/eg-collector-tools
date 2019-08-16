# =============================================================================
# Export Charging Resume FORM
# (c) Sertechno 2018
# GLVH @ 2018-11-27
# =============================================================================

# =============================================================================
class frm_export_Charging_Resume(Form):
    Export          = SelectField ("Export?", validators=[Required()])

    submit_PDF      = SubmitField ('PDF')
    submit_XLS      = SubmitField ('XLS')
    submit_CSV      = SubmitField ('CSV')
    submit_JSON     = SubmitField ('JSON')
    submit_FIX      = SubmitField ('FIX')
    submit_Cancel   = SubmitField ('Cancel')

