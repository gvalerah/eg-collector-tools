# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-16 15:51:37
# =============================================================================

from decimal import ROUND_HALF_UP

class frm_charge_resume(Form):
    Cus_Id                         = IntegerField("Cus_Id?", validators=[Required()])
    CR_Date_From                   = DateField("CR_Date_From?", validators=[Required()], format='%Y-%m-%d')
    CR_Date_To                     = DateField("CR_Date_To?", validators=[Required()], format='%Y-%m-%d')
    CIT_Status                     = IntegerField("CIT_Status?", validators=[Required()])
    Cur_Code                       = StringField("Cur_Code?", validators=[Required()])
    CIT_Count                      = IntegerField("CIT_Count?")
    CIT_Quantity                   = DecimalField("CIT_Quantity?", places=6, rounding=ROUND_HALF_UP)
    CIT_Generation                 = IntegerField("CIT_Generation?")
    CU_Id                          = IntegerField("CU_Id?", validators=[Required()])
    CI_CC_Id                       = IntegerField("CI_CC_Id?")
    CU_Operation                   = StringField("CU_Operation?")
    Typ_Code                       = StringField("Typ_Code?")
    CC_Cur_Code                    = StringField("CC_Cur_Code?")
    CI_Id                          = IntegerField("CI_Id?")
    Rat_Id                         = IntegerField("Rat_Id?")
    Rat_Price                      = DecimalField("Rat_Price?", places=6, rounding=ROUND_HALF_UP)
    Rat_MU_Code                    = StringField("Rat_MU_Code?")
    Rat_Cur_Code                   = StringField("Rat_Cur_Code?")
    Rat_Period                     = IntegerField("Rat_Period?")
    Rat_Hourly                     = DecimalField("Rat_Hourly?", places=6, rounding=ROUND_HALF_UP)
    Rat_Daily                      = DecimalField("Rat_Daily?", places=6, rounding=ROUND_HALF_UP)
    Rat_Monthly                    = DecimalField("Rat_Monthly?", places=6, rounding=ROUND_HALF_UP)
    CR_Quantity                    = DecimalField("CR_Quantity?", places=6, rounding=ROUND_HALF_UP)
    CR_Quantity_at_Rate            = DecimalField("CR_Quantity_at_Rate?", places=6, rounding=ROUND_HALF_UP)
    CC_XR                          = DecimalField("CC_XR?", places=6, rounding=ROUND_HALF_UP)
    CR_Cur_XR                      = DecimalField("CR_Cur_XR?", places=6, rounding=ROUND_HALF_UP)
    CR_ST_at_Rate_Cur              = DecimalField("CR_ST_at_Rate_Cur?", places=6, rounding=ROUND_HALF_UP)
    CR_ST_at_CC_Cur                = DecimalField("CR_ST_at_CC_Cur?", places=6, rounding=ROUND_HALF_UP)
    CR_ST_at_Cur                   = DecimalField("CR_ST_at_Cur?", places=6, rounding=ROUND_HALF_UP)
    Cus_Name                       = StringField("Cus_Name?")
    CI_Name                        = StringField("CI_Name?")
    CU_Description                 = StringField("CU_Description?")
    CC_Description                 = StringField("CC_Description?")
    Rat_Period_Description         = StringField("Rat_Period_Description?")
    Pla_Id                         = IntegerField("Pla_Id?")

    submit_Save                    = SubmitField  ('Save')
    submit_New                     = SubmitField  ('New')
    submit_Cancel                  = SubmitField  ('Cancel')

    has_FKs                        = False

class frm_charge_resume_delete(Form):
    submit_Delete                  = SubmitField  ('Delete')
    submit_Cancel                  = SubmitField  ('Cancel')

# =============================================================================
