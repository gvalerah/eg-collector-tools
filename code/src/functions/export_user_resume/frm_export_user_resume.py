# =============================================================================
# Export User Resume FORM
# (c) Sertechno 2019
# GLVH @ 2019-01-05
# =============================================================================

# =============================================================================
class frm_export_User_Resume(Form):
    Export          = SelectField ("Export?", validators=[Required()])

    submit_PDF      = SubmitField ('PDF')
    submit_XLS      = SubmitField ('XLS')
    submit_CSV      = SubmitField ('CSV')
    submit_JSON     = SubmitField ('JSON')
    submit_FIX      = SubmitField ('FIX')
    submit_Cancel   = SubmitField ('Cancel')

