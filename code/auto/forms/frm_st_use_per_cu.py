# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-18 18:05:34
# =============================================================================

from decimal import ROUND_HALF_UP

class frm_st_use_per_cu(Form):
    CU_Id                          = IntegerField("CU_Id?", validators=[Required()])
    From                           = DateTimeField("From?", validators=[Required()], format='%Y-%m-%d %H:%M:%S')
    To                             = DateTimeField("To?", validators=[Required()], format='%Y-%m-%d %H:%M:%S')
    Total_Slices                   = IntegerField("Total_Slices?")
    Found_Slices                   = IntegerField("Found_Slices?")
    Not_Found_Slices               = IntegerField("Not_Found_Slices?")
    Period_Initial_Q               = DecimalField("Period_Initial_Q?", places=6, rounding=ROUND_HALF_UP)
    Period_Increase                = DecimalField("Period_Increase?", places=6, rounding=ROUND_HALF_UP)
    Period_Increase_Count          = IntegerField("Period_Increase_Count?")
    Period_Reduction               = DecimalField("Period_Reduction?", places=6, rounding=ROUND_HALF_UP)
    Period_Reduction_Count         = IntegerField("Period_Reduction_Count?")
    Period_Final_Q                 = DecimalField("Period_Final_Q?", places=6, rounding=ROUND_HALF_UP)
    CI_Id                          = IntegerField("CI_Id?")
    CC_Id                          = IntegerField("CC_Id?")
    Cus_Id                         = IntegerField("Cus_Id?")
    Rat_Id                         = IntegerField("Rat_id?")
    Typ_Code                       = StringField("Typ_Code?")
    Pla_Id                         = IntegerField("Pla_Id?")
    Mean                           = DecimalField("Mean?", places=6, rounding=ROUND_HALF_UP)
    Variance                       = DecimalField("Variance?", places=6, rounding=ROUND_HALF_UP)
    StdDev                         = DecimalField("StdDev?", places=6, rounding=ROUND_HALF_UP)
    Min                            = DecimalField("Min?", places=6, rounding=ROUND_HALF_UP)
    Max                            = DecimalField("Max?", places=6, rounding=ROUND_HALF_UP)

    submit_Save                    = SubmitField  ('Save')
    submit_New                     = SubmitField  ('New')
    submit_Cancel                  = SubmitField  ('Cancel')

    has_FKs                        = False

class frm_st_use_per_cu_delete(Form):
    submit_Delete                  = SubmitField  ('Delete')
    submit_Cancel                  = SubmitField  ('Cancel')

# =============================================================================
