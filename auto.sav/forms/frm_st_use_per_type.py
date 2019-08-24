# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-20 18:43:44
# =============================================================================

from decimal import ROUND_HALF_UP

class frm_st_use_per_type(Form):
    Typ_Code         = StringField("Typ_Code?", validators=[Required()])
    Cus_Id           = IntegerField("Cus_Id?", validators=[Required()])
    Pla_Id           = IntegerField("Pla_Id?", validators=[Required()])
    CC_Id            = IntegerField("CC_Id?", validators=[Required()])
    CI_Id            = IntegerField("CI_Id?", validators=[Required()])
    Year             = IntegerField("Year?", validators=[Required()])
    Month            = IntegerField("Month?", validators=[Required()])
    Count            = IntegerField("Count?")
    Mean             = DecimalField("Mean?", places=6, rounding=ROUND_HALF_UP)
    Variance         = DecimalField("Variance?", places=6, rounding=ROUND_HALF_UP)
    StdDev           = DecimalField("StdDev?", places=6, rounding=ROUND_HALF_UP)
    Min              = DecimalField("Min?", places=6, rounding=ROUND_HALF_UP)
    Max              = DecimalField("Max?", places=6, rounding=ROUND_HALF_UP)

    submit_Save      = SubmitField  ('Save')
    submit_New       = SubmitField  ('New')
    submit_Cancel    = SubmitField  ('Cancel')

    has_FKs          = False

class frm_st_use_per_type_delete(Form):
    submit_Delete    = SubmitField  ('Delete')
    submit_Cancel    = SubmitField  ('Cancel')

# =============================================================================
