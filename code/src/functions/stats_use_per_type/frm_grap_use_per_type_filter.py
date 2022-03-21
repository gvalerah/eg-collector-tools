# =============================================================================
# Select Year and Type for Statistics Graph Generation with multiple filters
# (c) Sertechno 2019
# GLVH @ 2019-01-24
# =============================================================================


# =============================================================================
class frm_graph_use_per_type_filter(Form):
    Graph            = SelectField  ("Type of Graphic?", validators=[DataRequired()],coerce=int) # Line, Bar, Min_Max, ....
    Year             = IntegerField ("Year ?", validators=[DataRequired(),NumberRange(min=2000, max=2030,message='Valid years are between 2000 and 2030')])
    From             = IntegerField ("Month From ?", validators=[DataRequired(),NumberRange(min=1, max=12,message='Valid months are between %(min)d and %(max)d')])
    To               = IntegerField ("Month To   ?", validators=[DataRequired(),NumberRange(min=1, max=12,message='Valid months are between 1 and 12')])  
    Type             = SelectField  ("Charge Unit Type ?", validators=[DataRequired(),
                                        Length(min=3,message='CU length should be at least %(min)d chars'),
                                        NoneOf(['NUL'], message='CU Type invalid')],
                                        coerce=str)         # Choices from available in ST Tables ... ?
    Field            = SelectField  ("Field To Report ?", validators=[DataRequired()], coerce=int)          # Choices: Count, Mean, Use (Count*Mean)
    Customer         = SelectField  ("Customer   ?", coerce=int)               # Choices from available for Customer (all for admin)
    Platform         = SelectField  ("Platform   ?", coerce=int)               # Choices from available for Customer (all for admin)
    CC               = SelectField  ("Cost Center?", coerce=int)               # Choices from available for Customer (all for admin)
    CI               = SelectField  ("Configuration Item ?", coerce=int)       # Choices from available for Customer (all for admin)
    Estimation       = SelectField  ("Next Year Estimation Required ?", coerce=int) # None, Lineal, Season, Lineal+Season, Exponential, ....

    submit_Report    = SubmitField  ('Generate Graphic')
    submit_Cancel    = SubmitField  ('Cancel')

