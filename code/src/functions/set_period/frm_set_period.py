# =============================================================================
# Set Period FORM
# (c) Sertechno 2020
# GLVH @ 2020-03-18
# =============================================================================

# =============================================================================
class frm_set_period(Form):
    Period          = SelectField ("Active Period ? ", validators=[DataRequired()])

    submit_Set      = SubmitField ('SET')
    submit_Cancel   = SubmitField ('Cancel')

