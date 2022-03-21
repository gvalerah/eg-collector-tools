# =============================================================================
# Select Year for Statistics Report
# (c) Sertechno 2019
# GLVH @ 2019-01-21
# =============================================================================


# =============================================================================
class frm_stats_use_per_type(Form):
    Year             = IntegerField    ("Year ?", validators=[DataRequired()])

    submit_Report    = SubmitField  ('Report')
    submit_Cancel    = SubmitField  ('Cancel')

