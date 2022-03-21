# =============================================================================
# Select Year and Type for Statistics Graph Generation
# (c) Sertechno 2019
# GLVH @ 2019-01-21
# =============================================================================


# =============================================================================
class frm_graph_use_per_type(Form):
    Year             = IntegerField    ("Year ?", validators=[DataRequired(),NumberRange(min=2000, max=2030,message='Valid year are beween 2000 and 2030')])
    Graph            = SelectField   ("Graphic ?", validators=[DataRequired()],coerce=int)

    submit_Report    = SubmitField  ('Generate Graphic')
    submit_Cancel    = SubmitField  ('Cancel')

