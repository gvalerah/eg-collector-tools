# GV Flask required modules
from flask_wtf              import FlaskForm as Form
from wtforms                import Field
from wtforms                import StringField, IntegerField, DecimalField, DateTimeField
from wtforms                import StringField, IntegerField, DecimalField, DateTimeField
from wtforms_components     import TimeField
# GV 20220310 from wtforms.fields.html5   import DateField
from wtforms.fields         import DateField
from wtforms                import BooleanField, SelectField, SubmitField, RadioField
# GV 20220310 from wtforms.validators     import Required
from wtforms.validators     import AnyOf
from wtforms.validators     import DataRequired
from wtforms.validators     import Email
from wtforms.validators     import EqualTo
from wtforms.validators     import HostnameValidation
from wtforms.validators     import IPAddress
from wtforms.validators     import DataRequired
from wtforms.validators     import Length
from wtforms.validators     import MacAddress
from wtforms.validators     import NoneOf
from wtforms.validators     import NumberRange
from wtforms.validators     import Optional
from wtforms.validators     import Regexp

# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2022-04-22 16:39:33
# =============================================================================

# gen_model_flask.py:289 => /home/gvalera/GIT/EG-Suite-Tools/Collector/code/auto/forms/frm_charge_items.py
from decimal import ROUND_HALF_UP

class frm_charge_item(Form):
    CU_Id                 = SelectField("Charge Unit Id?", coerce=int, validators=[DataRequired()])
    CIT_Date              = DateField("Date?", validators=[DataRequired()], format='%Y-%m-%d')
    CIT_Time              = TimeField("Time?", validators=[DataRequired()], format='%H-%M-%S')
    CIT_Quantity          = DecimalField("Quantity?", validators=[DataRequired()], places=12, rounding=ROUND_HALF_UP)
    CIT_Status            = SelectField("Status?", coerce=int, validators=[DataRequired()])
    CIT_Is_Active         = BooleanField("Is Active?")

    submit_Save           = SubmitField  ('Save')
    submit_New            = SubmitField  ('New')
    submit_Cancel         = SubmitField  ('Cancel')

    has_FKs               = True

class frm_charge_item_delete(Form):
    submit_Delete         = SubmitField  ('Delete')
    submit_Cancel         = SubmitField  ('Cancel')

# =============================================================================
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2022-04-22 16:39:33
# =============================================================================

# gen_model_flask.py:289 => /home/gvalera/GIT/EG-Suite-Tools/Collector/code/auto/forms/frm_charge_resumes.py
from decimal import ROUND_HALF_UP

class frm_charge_resume(Form):
    User_Id                        = IntegerField("User_Id?", validators=[DataRequired()])
    Cus_Id                         = IntegerField("Cus_Id?", validators=[DataRequired()])
    CR_Date_From                   = DateField("CR_Date_From?", validators=[DataRequired()], format='%Y-%m-%d')
    CR_Date_To                     = DateField("CR_Date_To?", validators=[DataRequired()], format='%Y-%m-%d')
    CIT_Status                     = IntegerField("CIT_Status?", validators=[DataRequired()])
    Cur_Code                       = StringField("Cur_Code?", validators=[DataRequired()])
    CU_Id                          = IntegerField("CU_Id?", validators=[DataRequired()])
    CIT_Count                      = IntegerField("CIT_Count?")
    CIT_Quantity                   = DecimalField("CIT_Quantity?", places=12, rounding=ROUND_HALF_UP)
    CIT_Generation                 = IntegerField("CIT_Generation?")
    CI_CC_Id                       = IntegerField("CI_CC_Id?")
    CU_Operation                   = StringField("CU_Operation?")
    Typ_Code                       = StringField("Typ_Code?")
    CC_Cur_Code                    = StringField("CC_Cur_Code?")
    CI_Id                          = IntegerField("CI_Id?")
    Rat_Id                         = IntegerField("Rat_Id?")
    Rat_Price                      = DecimalField("Rat_Price?", places=12, rounding=ROUND_HALF_UP)
    Rat_MU_Code                    = StringField("Rat_MU_Code?")
    Rat_Cur_Code                   = StringField("Rat_Cur_Code?")
    Rat_Period                     = IntegerField("Rat_Period?")
    Rat_Hourly                     = DecimalField("Rat_Hourly?", places=12, rounding=ROUND_HALF_UP)
    Rat_Daily                      = DecimalField("Rat_Daily?", places=12, rounding=ROUND_HALF_UP)
    Rat_Monthly                    = DecimalField("Rat_Monthly?", places=12, rounding=ROUND_HALF_UP)
    CR_Quantity                    = DecimalField("CR_Quantity?", places=12, rounding=ROUND_HALF_UP)
    CR_Quantity_at_Rate            = DecimalField("CR_Quantity_at_Rate?", places=12, rounding=ROUND_HALF_UP)
    CC_XR                          = DecimalField("CC_XR?", places=12, rounding=ROUND_HALF_UP)
    CR_Cur_XR                      = DecimalField("CR_Cur_XR?", places=12, rounding=ROUND_HALF_UP)
    CR_ST_at_Rate_Cur              = DecimalField("CR_ST_at_Rate_Cur?", places=12, rounding=ROUND_HALF_UP)
    CR_ST_at_CC_Cur                = DecimalField("CR_ST_at_CC_Cur?", places=12, rounding=ROUND_HALF_UP)
    CR_ST_at_Cur                   = DecimalField("CR_ST_at_Cur?", places=12, rounding=ROUND_HALF_UP)
    Cus_Name                       = StringField("Cus_Name?")
    CI_Name                        = StringField("CI_Name?")
    CU_Description                 = StringField("CU_Description?")
    CC_Description                 = StringField("CC_Description?")
    Rat_Period_Description         = StringField("Rat_Period_Description?")
    CC_Code                        = StringField("CC_Code?")
    Pla_Id                         = IntegerField("Pla_Id?")
    Pla_Name                       = StringField("Pla_Name?")

    submit_Save                    = SubmitField  ('Save')
    submit_New                     = SubmitField  ('New')
    submit_Cancel                  = SubmitField  ('Cancel')

    has_FKs                        = False

class frm_charge_resume_delete(Form):
    submit_Delete                  = SubmitField  ('Delete')
    submit_Cancel                  = SubmitField  ('Cancel')

# =============================================================================
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2022-04-22 16:39:33
# =============================================================================

# gen_model_flask.py:289 => /home/gvalera/GIT/EG-Suite-Tools/Collector/code/auto/forms/frm_charge_unit_egm.py
from decimal import ROUND_HALF_UP

class frm_charge_unit_egm(Form):
    CU_Id                   = SelectField("Charge Unit Id?", coerce=int, validators=[DataRequired()])
    Archive                 = IntegerField("Archive?")
    Path                    = StringField("Path?")
    Metric                  = StringField("Metric?")
    Host                    = StringField("Host?")
    Port                    = IntegerField("Port?")
    User                    = StringField("User?")
    Password                = StringField("Password?")
    Public_Key_File         = StringField("Public_Key_File?")
    Passphrase              = StringField("Passphrase?")

    submit_Save             = SubmitField  ('Save')
    submit_New              = SubmitField  ('New')
    submit_Cancel           = SubmitField  ('Cancel')

    has_FKs                 = True

class frm_charge_unit_egm_delete(Form):
    submit_Delete           = SubmitField  ('Delete')
    submit_Cancel           = SubmitField  ('Cancel')

# =============================================================================
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2022-04-22 16:39:33
# =============================================================================

# gen_model_flask.py:289 => /home/gvalera/GIT/EG-Suite-Tools/Collector/code/auto/forms/frm_charge_units.py
from decimal import ROUND_HALF_UP

class frm_charge_unit(Form):
    CI_Id                          = SelectField("Configuration Item Id?", coerce=int, validators=[DataRequired()])
    CU_Description                 = StringField("Description?")
    CU_UUID                        = StringField("UUID?")
    CU_Is_Billeable                = BooleanField("Is Billeable?")
    CU_Is_Always_Billeable         = BooleanField("Is Always Billeable?")
    CU_Quantity                    = DecimalField("Quantity?", validators=[DataRequired()], places=12, rounding=ROUND_HALF_UP)
    CU_Operation                   = SelectField("Conversion Operation?", validators=[DataRequired()])
    Typ_Code                       = SelectField("Type?", validators=[DataRequired()])
    CIT_Generation                 = SelectField("Item Generation Type?", coerce=int, validators=[DataRequired()])
    Rat_Id                         = IntegerField("Rate Id?")
    CU_Reference_1                 = StringField("Reference 1?")
    CU_Reference_2                 = StringField("Reference 2?")
    CU_Reference_3                 = StringField("Reference 3?")

    submit_Save                    = SubmitField  ('Save')
    submit_New                     = SubmitField  ('New')
    submit_Cancel                  = SubmitField  ('Cancel')

    has_FKs                        = True

class frm_charge_unit_delete(Form):
    submit_Delete                  = SubmitField  ('Delete')
    submit_Cancel                  = SubmitField  ('Cancel')

# =============================================================================
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2022-04-22 16:39:33
# =============================================================================

# gen_model_flask.py:289 => /home/gvalera/GIT/EG-Suite-Tools/Collector/code/auto/forms/frm_cit_generations.py
from decimal import ROUND_HALF_UP

class frm_cit_generation(Form):
    CIT_Generation         = IntegerField("CIT_Generation?", validators=[DataRequired()])
    Value                  = StringField("Value?")

    submit_Save            = SubmitField  ('Save')
    submit_New             = SubmitField  ('New')
    submit_Cancel          = SubmitField  ('Cancel')

    has_FKs                = False

class frm_cit_generation_delete(Form):
    submit_Delete          = SubmitField  ('Delete')
    submit_Cancel          = SubmitField  ('Cancel')

# =============================================================================
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2022-04-22 16:39:33
# =============================================================================

# gen_model_flask.py:289 => /home/gvalera/GIT/EG-Suite-Tools/Collector/code/auto/forms/frm_cit_statuses.py
from decimal import ROUND_HALF_UP

class frm_cit_status(Form):
    CIT_Status         = IntegerField("CIT Status?", validators=[DataRequired()])
    Value              = StringField("Vallue?")

    submit_Save        = SubmitField  ('Save')
    submit_New         = SubmitField  ('New')
    submit_Cancel      = SubmitField  ('Cancel')

    has_FKs            = False

class frm_cit_status_delete(Form):
    submit_Delete      = SubmitField  ('Delete')
    submit_Cancel      = SubmitField  ('Cancel')

# =============================================================================
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2022-04-22 16:39:33
# =============================================================================

# gen_model_flask.py:289 => /home/gvalera/GIT/EG-Suite-Tools/Collector/code/auto/forms/frm_configuration_items.py
from decimal import ROUND_HALF_UP

class frm_configuration_item(Form):
    CI_Name                             = StringField("Name?", validators=[DataRequired()])
    CI_UUID                             = StringField("UUID?", validators=[DataRequired()])
    Pla_Id                              = SelectField("Platform Id?", coerce=int, validators=[DataRequired()])
    CC_Id                               = SelectField("Cost Center Id?", coerce=int, validators=[DataRequired()])
    Cus_Id                              = SelectField("Customer Id?", coerce=int, validators=[DataRequired()])
    CI_Commissioning_DateTime           = DateTimeField("Commissioning Date and Time?", validators=[DataRequired()], format='%Y-%m-%d %H:%M:%S')
    CI_Decommissioning_DateTime         = DateTimeField("Decommissioning Date and Time?", validators=[Optional()], format='%Y-%m-%d %H:%M:%S')

    submit_Save                         = SubmitField  ('Save')
    submit_New                          = SubmitField  ('New')
    submit_Cancel                       = SubmitField  ('Cancel')

    has_FKs                             = True

class frm_configuration_item_delete(Form):
    submit_Delete                       = SubmitField  ('Delete')
    submit_Cancel                       = SubmitField  ('Cancel')

# =============================================================================
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2022-04-22 16:39:33
# =============================================================================

# gen_model_flask.py:289 => /home/gvalera/GIT/EG-Suite-Tools/Collector/code/auto/forms/frm_cost_centers.py
from decimal import ROUND_HALF_UP

class frm_cost_center(Form):
    CC_Code                = StringField("Code?")
    CC_Description         = StringField("Description?")
    Cur_Code               = SelectField("Currency Code?", validators=[DataRequired()])
    CC_Parent_Code         = StringField("Parent Code?")
    CC_Reg_Exp             = StringField("Regular Expression?")
    CC_Reference           = StringField("Reference?")
    Cus_Id                 = IntegerField("Cus_Id?")

    submit_Save            = SubmitField  ('Save')
    submit_New             = SubmitField  ('New')
    submit_Cancel          = SubmitField  ('Cancel')

    has_FKs                = True

class frm_cost_center_delete(Form):
    submit_Delete          = SubmitField  ('Delete')
    submit_Cancel          = SubmitField  ('Cancel')

# =============================================================================
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2022-04-22 16:39:33
# =============================================================================

# gen_model_flask.py:289 => /home/gvalera/GIT/EG-Suite-Tools/Collector/code/auto/forms/frm_countries_currencies.py
from decimal import ROUND_HALF_UP

class frm_country_currency(Form):
    Cou_Code                = SelectField("Country Code?", validators=[DataRequired()])
    Cur_Code                = SelectField("Currency Code?", validators=[DataRequired()])
    Cou_Cur_Comment         = StringField("Comment?")

    submit_Save             = SubmitField  ('Save')
    submit_New              = SubmitField  ('New')
    submit_Cancel           = SubmitField  ('Cancel')

    has_FKs                 = True

class frm_country_currency_delete(Form):
    submit_Delete           = SubmitField  ('Delete')
    submit_Cancel           = SubmitField  ('Cancel')

# =============================================================================
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2022-04-22 16:39:33
# =============================================================================

# gen_model_flask.py:289 => /home/gvalera/GIT/EG-Suite-Tools/Collector/code/auto/forms/frm_countries.py
from decimal import ROUND_HALF_UP

class frm_country(Form):
    Cou_Code         = StringField("Code?", validators=[DataRequired()])
    Cou_Name         = StringField("Name?")
    Cou_A3           = StringField("Alphanum Code?")
    Cou_N            = IntegerField("ISO Numeric Code?")

    submit_Save      = SubmitField  ('Save')
    submit_New       = SubmitField  ('New')
    submit_Cancel    = SubmitField  ('Cancel')

    has_FKs          = False

class frm_country_delete(Form):
    submit_Delete    = SubmitField  ('Delete')
    submit_Cancel    = SubmitField  ('Cancel')

# =============================================================================
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2022-04-22 16:39:33
# =============================================================================

# gen_model_flask.py:289 => /home/gvalera/GIT/EG-Suite-Tools/Collector/code/auto/forms/frm_cu_operations.py
from decimal import ROUND_HALF_UP

class frm_cu_operation(Form):
    CU_Operation         = StringField("Operation?", validators=[DataRequired()])
    Value                = StringField("Value?")
    Is_Multiply          = BooleanField("Is Multiply?")
    Factor               = IntegerField("Factor?")

    submit_Save          = SubmitField  ('Save')
    submit_New           = SubmitField  ('New')
    submit_Cancel        = SubmitField  ('Cancel')

    has_FKs              = False

class frm_cu_operation_delete(Form):
    submit_Delete        = SubmitField  ('Delete')
    submit_Cancel        = SubmitField  ('Cancel')

# =============================================================================
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2022-04-22 16:39:33
# =============================================================================

# gen_model_flask.py:289 => /home/gvalera/GIT/EG-Suite-Tools/Collector/code/auto/forms/frm_currencies.py
from decimal import ROUND_HALF_UP

class frm_currency(Form):
    Cur_Code            = StringField("Code?", validators=[DataRequired()])
    Cur_Name            = StringField("Name?")
    Cur_Id              = IntegerField("Id?")
    Cur_Comment         = StringField("Comment?")

    submit_Save         = SubmitField  ('Save')
    submit_New          = SubmitField  ('New')
    submit_Cancel       = SubmitField  ('Cancel')

    has_FKs             = False

class frm_currency_delete(Form):
    submit_Delete       = SubmitField  ('Delete')
    submit_Cancel       = SubmitField  ('Cancel')

# =============================================================================
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2022-04-22 16:39:33
# =============================================================================

# gen_model_flask.py:289 => /home/gvalera/GIT/EG-Suite-Tools/Collector/code/auto/forms/frm_customers.py
from decimal import ROUND_HALF_UP

class frm_customer(Form):
    Cus_Name         = StringField("Name?")
    CC_Id            = SelectField("Cost Center Id?", coerce=int, validators=[DataRequired()])

    submit_Save      = SubmitField  ('Save')
    submit_New       = SubmitField  ('New')
    submit_Cancel    = SubmitField  ('Cancel')

    has_FKs          = True

class frm_customer_delete(Form):
    submit_Delete    = SubmitField  ('Delete')
    submit_Cancel    = SubmitField  ('Cancel')

# =============================================================================
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2022-04-22 16:39:33
# =============================================================================

# gen_model_flask.py:289 => /home/gvalera/GIT/EG-Suite-Tools/Collector/code/auto/forms/frm_cu_types.py
from decimal import ROUND_HALF_UP

class frm_cu_type(Form):
    Typ_Code                = StringField("Type?", validators=[DataRequired()])
    Typ_Description         = StringField("Description?")

    submit_Save             = SubmitField  ('Save')
    submit_New              = SubmitField  ('New')
    submit_Cancel           = SubmitField  ('Cancel')

    has_FKs                 = False

class frm_cu_type_delete(Form):
    submit_Delete           = SubmitField  ('Delete')
    submit_Cancel           = SubmitField  ('Cancel')

# =============================================================================
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2022-04-22 16:39:33
# =============================================================================

# gen_model_flask.py:289 => /home/gvalera/GIT/EG-Suite-Tools/Collector/code/auto/forms/frm_exchange_rates.py
from decimal import ROUND_HALF_UP

class frm_exchange_rate(Form):
    Cur_Code          = SelectField("Currency Code?", validators=[DataRequired()])
    ER_Factor         = DecimalField("Factor?", validators=[DataRequired()], places=12, rounding=ROUND_HALF_UP)
    ER_Date           = DateField("Date?", format='%Y-%m-%d')

    submit_Save       = SubmitField  ('Save')
    submit_New        = SubmitField  ('New')
    submit_Cancel     = SubmitField  ('Cancel')

    has_FKs           = True

class frm_exchange_rate_delete(Form):
    submit_Delete     = SubmitField  ('Delete')
    submit_Cancel     = SubmitField  ('Cancel')

# =============================================================================
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2022-04-22 16:39:33
# =============================================================================

# gen_model_flask.py:289 => /home/gvalera/GIT/EG-Suite-Tools/Collector/code/auto/forms/frm_interface.py
from decimal import ROUND_HALF_UP

class frm_interface(Form):
    User_Id             = IntegerField("User_Id?")
    Table_name          = StringField("Table_name?")
    Option_Type         = IntegerField("Option_Type?")
    Argument_1          = StringField("Argument_1?")
    Argument_2          = StringField("Argument_2?")
    Argument_3          = StringField("Argument_3?")
    Is_Active           = BooleanField("Is_Active?")

    submit_Save         = SubmitField  ('Save')
    submit_New          = SubmitField  ('New')
    submit_Cancel       = SubmitField  ('Cancel')

    has_FKs             = False

class frm_interface_delete(Form):
    submit_Delete       = SubmitField  ('Delete')
    submit_Cancel       = SubmitField  ('Cancel')

# =============================================================================
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2022-04-22 16:39:33
# =============================================================================

# gen_model_flask.py:289 => /home/gvalera/GIT/EG-Suite-Tools/Collector/code/auto/forms/frm_measure_units.py
from decimal import ROUND_HALF_UP

class frm_measure_unit(Form):
    MU_Code                = StringField("Code?", validators=[DataRequired()])
    MU_Description         = StringField("Description?")

    submit_Save            = SubmitField  ('Save')
    submit_New             = SubmitField  ('New')
    submit_Cancel          = SubmitField  ('Cancel')

    has_FKs                = False

class frm_measure_unit_delete(Form):
    submit_Delete          = SubmitField  ('Delete')
    submit_Cancel          = SubmitField  ('Cancel')

# =============================================================================
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2022-04-22 16:39:33
# =============================================================================

# gen_model_flask.py:289 => /home/gvalera/GIT/EG-Suite-Tools/Collector/code/auto/forms/frm_platforms.py
from decimal import ROUND_HALF_UP

class frm_platform(Form):
    Pla_Name             = StringField("Name?")
    Pla_Host             = StringField("Host?")
    Pla_Port             = StringField("Port?")
    Pla_User             = StringField("User?")
    Pla_Password         = StringField("Password?")

    submit_Save          = SubmitField  ('Save')
    submit_New           = SubmitField  ('New')
    submit_Cancel        = SubmitField  ('Cancel')

    has_FKs              = False

class frm_platform_delete(Form):
    submit_Delete        = SubmitField  ('Delete')
    submit_Cancel        = SubmitField  ('Cancel')

# =============================================================================
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2022-04-22 16:39:33
# =============================================================================

# gen_model_flask.py:289 => /home/gvalera/GIT/EG-Suite-Tools/Collector/code/auto/forms/frm_rates.py
from decimal import ROUND_HALF_UP

class frm_rate(Form):
    Typ_Code           = SelectField("Charge Unit Type?", validators=[DataRequired()])
    Cus_Id             = SelectField("Customer Id?", coerce=int, validators=[DataRequired()])
    Pla_Id             = SelectField("Platform Id?", coerce=int, validators=[DataRequired()])
    CC_Id              = SelectField("Cost Center Id?", coerce=int, validators=[DataRequired()])
    CI_Id              = SelectField("Configuration Item?", coerce=int, validators=[DataRequired()])
    Rat_Price          = DecimalField("Rate Price?", validators=[DataRequired()], places=12, rounding=ROUND_HALF_UP)
    Cur_Code           = SelectField("Currency Code?", validators=[DataRequired()])
    MU_Code            = SelectField("Measure Unit?", validators=[DataRequired()])
    Rat_Period         = RadioField("Period?", coerce=int, validators=[DataRequired()])

    submit_Save        = SubmitField  ('Save')
    submit_New         = SubmitField  ('New')
    submit_Cancel      = SubmitField  ('Cancel')

    has_FKs            = True

class frm_rate_delete(Form):
    submit_Delete      = SubmitField  ('Delete')
    submit_Cancel      = SubmitField  ('Cancel')

# =============================================================================
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2022-04-22 16:39:33
# =============================================================================

# gen_model_flask.py:289 => /home/gvalera/GIT/EG-Suite-Tools/Collector/code/auto/forms/frm_rat_periods.py
from decimal import ROUND_HALF_UP

class frm_rat_period(Form):
    Rat_Period         = IntegerField("Rate Period?", validators=[DataRequired()])
    Value              = StringField("Value?")

    submit_Save        = SubmitField  ('Save')
    submit_New         = SubmitField  ('New')
    submit_Cancel      = SubmitField  ('Cancel')

    has_FKs            = False

class frm_rat_period_delete(Form):
    submit_Delete      = SubmitField  ('Delete')
    submit_Cancel      = SubmitField  ('Cancel')

# =============================================================================
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2022-04-22 16:39:33
# =============================================================================

# gen_model_flask.py:289 => /home/gvalera/GIT/EG-Suite-Tools/Collector/code/auto/forms/frm_roles.py
from decimal import ROUND_HALF_UP

class frm_Role(Form):
    id                  = IntegerField("id?", validators=[DataRequired()])
    name                = StringField("name?")
    default             = BooleanField("default?")
    permissions         = IntegerField("permissions?")

    submit_Save         = SubmitField  ('Save')
    submit_New          = SubmitField  ('New')
    submit_Cancel       = SubmitField  ('Cancel')

    has_FKs             = False

class frm_Role_delete(Form):
    submit_Delete       = SubmitField  ('Delete')
    submit_Cancel       = SubmitField  ('Cancel')

# =============================================================================
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2022-04-22 16:39:33
# =============================================================================

# gen_model_flask.py:289 => /home/gvalera/GIT/EG-Suite-Tools/Collector/code/auto/forms/frm_statistics.py
from decimal import ROUND_HALF_UP

class frm_statistics(Form):
    CR_Date_From                = DateField("CR_Date_From?", validators=[DataRequired()], format='%Y-%m-%d')
    CR_Date_To                  = DateField("CR_Date_To?", validators=[DataRequired()], format='%Y-%m-%d')
    User_Id                     = IntegerField("User_Id?", validators=[DataRequired()])
    Cus_Id                      = IntegerField("Cus_Id?", validators=[DataRequired()])
    CC_Id                       = IntegerField("CC_Id?", validators=[DataRequired()])
    CI_Id                       = IntegerField("CI_Id?", validators=[DataRequired()])
    CU_Id                       = IntegerField("CU_Id?", validators=[DataRequired()])
    Typ_Code                    = StringField("Typ_Code?", validators=[DataRequired()])
    Period                      = StringField("Period?", validators=[DataRequired()])
    Agregation                  = IntegerField("Agregation?", validators=[DataRequired()])
    CR_Quantity_at_Rate         = DecimalField("CR_Quantity_at_Rate?", places=12, rounding=ROUND_HALF_UP)
    CR_Quantity                 = DecimalField("CR_Quantity?", places=12, rounding=ROUND_HALF_UP)
    CR_ST_at_Cur                = DecimalField("CR_ST_at_Cur?", places=12, rounding=ROUND_HALF_UP)
    Cur_Code                    = StringField("Cur_Code?")
    CIT_Status                  = IntegerField("CIT_Status?")
    CIT_Count                   = IntegerField("CIT_Count?")
    Pla_Id                      = IntegerField("Pla_Id?")

    submit_Save                 = SubmitField  ('Save')
    submit_New                  = SubmitField  ('New')
    submit_Cancel               = SubmitField  ('Cancel')

    has_FKs                     = False

class frm_statistics_delete(Form):
    submit_Delete               = SubmitField  ('Delete')
    submit_Cancel               = SubmitField  ('Cancel')

# =============================================================================
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2022-04-22 16:39:33
# =============================================================================

# gen_model_flask.py:289 => /home/gvalera/GIT/EG-Suite-Tools/Collector/code/auto/forms/frm_st_use_per_cu.py
from decimal import ROUND_HALF_UP

class frm_st_use_per_cu(Form):
    CU_Id                          = IntegerField("CU_Id?", validators=[DataRequired()])
    From                           = DateTimeField("From?", validators=[DataRequired()], format='%Y-%m-%d %H:%M:%S')
    To                             = DateTimeField("To?", validators=[DataRequired()], format='%Y-%m-%d %H:%M:%S')
    Total_Slices                   = IntegerField("Total_Slices?")
    Found_Slices                   = IntegerField("Found_Slices?")
    Not_Found_Slices               = IntegerField("Not_Found_Slices?")
    Period_Initial_Q               = DecimalField("Period_Initial_Q?", places=12, rounding=ROUND_HALF_UP)
    Period_Increase                = DecimalField("Period_Increase?", places=12, rounding=ROUND_HALF_UP)
    Period_Increase_Count          = IntegerField("Period_Increase_Count?")
    Period_Reduction               = DecimalField("Period_Reduction?", places=12, rounding=ROUND_HALF_UP)
    Period_Reduction_Count         = IntegerField("Period_Reduction_Count?")
    Period_Final_Q                 = DecimalField("Period_Final_Q?", places=12, rounding=ROUND_HALF_UP)
    CI_Id                          = IntegerField("CI_Id?")
    CC_Id                          = IntegerField("CC_Id?")
    Cus_Id                         = IntegerField("Cus_Id?")
    Rat_Id                         = IntegerField("Rat_id?")
    Typ_Code                       = StringField("Typ_Code?")
    Pla_Id                         = IntegerField("Pla_Id?")
    Mean                           = DecimalField("Mean?", places=12, rounding=ROUND_HALF_UP)
    Variance                       = DecimalField("Variance?", places=12, rounding=ROUND_HALF_UP)
    StdDev                         = DecimalField("StdDev?", places=12, rounding=ROUND_HALF_UP)
    Min                            = DecimalField("Min?", places=12, rounding=ROUND_HALF_UP)
    Max                            = DecimalField("Max?", places=12, rounding=ROUND_HALF_UP)

    submit_Save                    = SubmitField  ('Save')
    submit_New                     = SubmitField  ('New')
    submit_Cancel                  = SubmitField  ('Cancel')

    has_FKs                        = False

class frm_st_use_per_cu_delete(Form):
    submit_Delete                  = SubmitField  ('Delete')
    submit_Cancel                  = SubmitField  ('Cancel')

# =============================================================================
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2022-04-22 16:39:33
# =============================================================================

# gen_model_flask.py:289 => /home/gvalera/GIT/EG-Suite-Tools/Collector/code/auto/forms/frm_st_use_per_type.py
from decimal import ROUND_HALF_UP

class frm_st_use_per_type(Form):
    Typ_Code         = StringField("Typ_Code?", validators=[DataRequired()])
    Cus_Id           = IntegerField("Cus_Id?", validators=[DataRequired()])
    Pla_Id           = IntegerField("Pla_Id?", validators=[DataRequired()])
    CC_Id            = IntegerField("CC_Id?", validators=[DataRequired()])
    CI_Id            = IntegerField("CI_Id?", validators=[DataRequired()])
    Year             = IntegerField("Year?", validators=[DataRequired()])
    Month            = IntegerField("Month?", validators=[DataRequired()])
    Count            = IntegerField("Count?")
    Mean             = DecimalField("Mean?", places=12, rounding=ROUND_HALF_UP)
    Variance         = DecimalField("Variance?", places=12, rounding=ROUND_HALF_UP)
    StdDev           = DecimalField("StdDev?", places=12, rounding=ROUND_HALF_UP)
    Min              = DecimalField("Min?", places=12, rounding=ROUND_HALF_UP)
    Max              = DecimalField("Max?", places=12, rounding=ROUND_HALF_UP)

    submit_Save      = SubmitField  ('Save')
    submit_New       = SubmitField  ('New')
    submit_Cancel    = SubmitField  ('Cancel')

    has_FKs          = False

class frm_st_use_per_type_delete(Form):
    submit_Delete    = SubmitField  ('Delete')
    submit_Cancel    = SubmitField  ('Cancel')

# =============================================================================
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2022-04-22 16:39:33
# =============================================================================

# gen_model_flask.py:289 => /home/gvalera/GIT/EG-Suite-Tools/Collector/code/auto/forms/frm_trace.py
from decimal import ROUND_HALF_UP

class frm_trace(Form):
    LINE         = StringField("LINE?")

    submit_Save  = SubmitField  ('Save')
    submit_New   = SubmitField  ('New')
    submit_Cancel = SubmitField  ('Cancel')

    has_FKs      = False

class frm_trace_delete(Form):
    submit_Delete = SubmitField  ('Delete')
    submit_Cancel = SubmitField  ('Cancel')

# =============================================================================
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2022-04-22 16:39:33
# =============================================================================

# gen_model_flask.py:289 => /home/gvalera/GIT/EG-Suite-Tools/Collector/code/auto/forms/frm_user_resumes.py
from decimal import ROUND_HALF_UP

class frm_user_resumes(Form):
    User_Id                        = IntegerField("User_Id?", validators=[DataRequired()])
    Cus_Id                         = IntegerField("Cus_Id?")
    CR_Date_From                   = DateField("CR_Date_From?", validators=[DataRequired()], format='%Y-%m-%d')
    CR_Date_To                     = DateField("CR_Date_To?", validators=[DataRequired()], format='%Y-%m-%d')
    CIT_Status                     = IntegerField("CIT_Status?", validators=[DataRequired()])
    Cur_Code                       = StringField("Cur_Code?", validators=[DataRequired()])
    CIT_Count                      = IntegerField("CIT_Count?")
    CIT_Quantity                   = DecimalField("CIT_Quantity?", places=12, rounding=ROUND_HALF_UP)
    CIT_Generation                 = IntegerField("CIT_Generation?")
    CU_Id                          = IntegerField("CU_Id?", validators=[DataRequired()])
    CI_CC_Id                       = IntegerField("CI_CC_Id?")
    CU_Operation                   = StringField("CU_Operation?")
    Typ_Code                       = StringField("Typ_Code?")
    CC_Cur_Code                    = StringField("CC_Cur_Code?")
    CI_Id                          = IntegerField("CI_Id?", validators=[DataRequired()])
    Rat_Id                         = IntegerField("Rat_Id?")
    Rat_Price                      = DecimalField("Rat_Price?", places=12, rounding=ROUND_HALF_UP)
    Rat_MU_Code                    = StringField("Rat_MU_Code?")
    Rat_Cur_Code                   = StringField("Rat_Cur_Code?")
    Rat_Period                     = IntegerField("Rat_Period?")
    Rat_Hourly                     = DecimalField("Rat_Hourly?", places=12, rounding=ROUND_HALF_UP)
    Rat_Daily                      = DecimalField("Rat_Daily?", places=12, rounding=ROUND_HALF_UP)
    Rat_Monthly                    = DecimalField("Rat_Monthly?", places=12, rounding=ROUND_HALF_UP)
    CR_Quantity                    = DecimalField("CR_Quantity?", places=12, rounding=ROUND_HALF_UP)
    CR_Quantity_at_Rate            = DecimalField("CR_Quantity_at_Rate?", places=12, rounding=ROUND_HALF_UP)
    CC_XR                          = DecimalField("CC_XR?", places=12, rounding=ROUND_HALF_UP)
    CR_Cur_XR                      = DecimalField("CR_Cur_XR?", places=12, rounding=ROUND_HALF_UP)
    CR_ST_at_Rate_Cur              = DecimalField("CR_ST_at_Rate_Cur?", places=12, rounding=ROUND_HALF_UP)
    CR_ST_at_CC_Cur                = DecimalField("CR_ST_at_CC_Cur?", places=12, rounding=ROUND_HALF_UP)
    CR_ST_at_Cur                   = DecimalField("CR_ST_at_Cur?", places=12, rounding=ROUND_HALF_UP)
    Cus_Name                       = StringField("Cus_Name?")
    CI_Name                        = StringField("CI_Name?")
    CU_Description                 = StringField("CU_Description?")
    CC_Description                 = StringField("CC_Description?")
    Rat_Period_Description         = StringField("Rat_Period_Description?")
    CC_Code                        = StringField("CC_Code?")
    Pla_Id                         = IntegerField("Pla_Id?")
    Pla_Name                       = StringField("Pla_Name?")

    submit_Save                    = SubmitField  ('Save')
    submit_New                     = SubmitField  ('New')
    submit_Cancel                  = SubmitField  ('Cancel')

    has_FKs                        = False

class frm_user_resumes_delete(Form):
    submit_Delete                  = SubmitField  ('Delete')
    submit_Cancel                  = SubmitField  ('Cancel')

# =============================================================================
# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2022-04-22 16:39:33
# =============================================================================

# gen_model_flask.py:289 => /home/gvalera/GIT/EG-Suite-Tools/Collector/code/auto/forms/frm_users.py
from decimal import ROUND_HALF_UP

class frm_User(Form):
    username              = StringField("username?")
    name                  = StringField("name?")
    role_id               = SelectField("role_id?", coerce=int, validators=[DataRequired()])
    email                 = StringField("email?")
    password_hash         = StringField("password_hash?")
    confirmed             = BooleanField("confirmed?")
    CC_Id                 = SelectField("CC_Id?", coerce=int, validators=[DataRequired()])
    roles                 = StringField("roles?")
    ldap                  = BooleanField("ldap?")
    ldap_method           = StringField("ldap_method?")
    ldap_user             = StringField("ldap_user?")
    ldap_common           = StringField("ldap_common?")
    ldap_host             = StringField("ldap_host?")
    ldap_port             = IntegerField("ldap_port?")
    ldap_domain           = StringField("ldap_domain?")
    vars                  = StringField("vars?")

    submit_Save           = SubmitField  ('Save')
    submit_New            = SubmitField  ('New')
    submit_Cancel         = SubmitField  ('Cancel')

    has_FKs               = True

class frm_User_delete(Form):
    submit_Delete         = SubmitField  ('Delete')
    submit_Cancel         = SubmitField  ('Cancel')

# =============================================================================
# =============================================================================
# Change CI State
# (c) Sertechno 2018
# GLVH @ 2018-12-06 14:55:00
# =============================================================================

# =============================================================================
class frm_change_cit_state(Form):
    CU_Id            = SelectField  ("Charge Unit?", validators=[DataRequired()], coerce=int)
    CIT_Date_From    = DateField    ("Billing Data from?", validators=[DataRequired()], format="%Y-%m-%d")
    CIT_Time_From    = SelectField  ("Time from?", validators=[DataRequired()])
    CIT_Date_To      = DateField    ("Billing Data up to?", validators=[DataRequired()], format="%Y-%m-%d")
    CIT_Time_To      = SelectField  ("Time to?", validators=[DataRequired()])
    CIT_Status       = SelectField  ("Status to Change from?", coerce=int)
    CIT_Status_To    = SelectField  ("Status to Change to?", coerce=int)

    submit_Search    = SubmitField  ('Search')
    submit_Cancel    = SubmitField  ('Cancel')

class frm_change_cit_state_confirm(Form):

    submit_Change    = SubmitField  ('Change')
    submit_Cancel    = SubmitField  ('Cancel')
# =============================================================================

# =============================================================================
# Billing Resume FORM All CIs
# (c) Sertechno 2019
# GLVH @ 2019-03-12
# =============================================================================


# =============================================================================
class frm_charging_resume_all(Form):
    CIT_Date_From    = DateField    ("Billing Data from?", validators=[DataRequired()], format="%Y-%m-%d")
    CIT_Date_To      = DateField    ("Billing Data up to?", validators=[DataRequired()], format="%Y-%m-%d")
    CIT_Status       = SelectField  ("Status to Report?", coerce=int)
    Cur_Code         = SelectField  ("Currency to Report?", coerce=str)

    submit_Report    = SubmitField  ('Report')
    submit_Update    = SubmitField  ('Update & Report')
    submit_Cancel    = SubmitField  ('Cancel')

# =============================================================================
# Billing Resume FORM per CC
# (c) Sertechno 2019
# GLVH @ 2018-03-11
# =============================================================================


# =============================================================================
class frm_charging_resume_cc(Form):
    CC_Id           = SelectField  ("Cost Center?", validators=[DataRequired()], coerce=int)
    CIT_Date_From    = DateField    ("Billing Data from?", validators=[DataRequired()], format="%Y-%m-%d")
    CIT_Date_To      = DateField    ("Billing Data up to?", validators=[DataRequired()], format="%Y-%m-%d")
    CIT_Status       = SelectField  ("Status to Report?", coerce=int)
    Cur_Code         = SelectField  ("Currency to Report?", coerce=str)

    submit_Report    = SubmitField  ('Report')
    submit_Update    = SubmitField  ('Update & Report')
    submit_Cancel    = SubmitField  ('Cancel')

# =============================================================================
# Billing Resume FORM Multilevel Report
# (c) Sertechno 2019
# GLVH @ 2019-04-29
# =============================================================================


# =============================================================================
class frm_charging_resume_level(Form):
    Cus_Id           = SelectField  ("Customer?", validators=[DataRequired()], coerce=int)
    CIT_Date_From    = DateField    ("Billing Data from?", validators=[DataRequired()], format="%Y-%m-%d")
    CIT_Date_To      = DateField    ("Billing Data up to?", validators=[DataRequired()], format="%Y-%m-%d")
    CIT_Status       = SelectField  ("Status to Report?", coerce=int)
    Cur_Code         = SelectField  ("Currency to Report?", coerce=str)
    Level            = SelectField  ("Report Level?", coerce=int)

    submit_Report    = SubmitField  ('Report')
    submit_Update    = SubmitField  ('Update & Report')
    submit_Cancel    = SubmitField  ('Cancel')

# =============================================================================
# Billing Resume FORM Platforms
# (c) Sertechno 2019
# GLVH @ 2019-03-12
# =============================================================================


# =============================================================================
class frm_charging_resume_platform(Form):
    Pla_Id           = SelectField  ("Platform?", validators=[DataRequired()], coerce=int)
    CIT_Date_From    = DateField    ("Billing Data from?", validators=[DataRequired()], format="%Y-%m-%d")
    CIT_Date_To      = DateField    ("Billing Data up to?", validators=[DataRequired()], format="%Y-%m-%d")
    CIT_Status       = SelectField  ("Status to Report?", coerce=int)
    Cur_Code         = SelectField  ("Currency to Report?", coerce=str)

    submit_Report    = SubmitField  ('Report')
    submit_Update    = SubmitField  ('Update & Report')
    submit_Cancel    = SubmitField  ('Cancel')

# =============================================================================
# Billing Resume FORM
# (c) Sertechno 2018
# GLVH @ 2018-11-10 22:23:58
# =============================================================================


# ======================================================================
# Default form is as customer's
class frm_charging_resume(Form):
    User_Id          = 0 
    Cus_Id           = SelectField  ("Customer?", validators=[DataRequired()], coerce=int)
    CIT_Date_From    = DateField    ("Billing Data from?", validators=[DataRequired()], format="%Y-%m-%d")
    CIT_Date_To      = DateField    ("Billing Data up to?", validators=[DataRequired()], format="%Y-%m-%d")
    CIT_Status       = SelectField  ("Status to Report?", coerce=int)
    Cur_Code         = SelectField  ("Currency to Report?", coerce=str)

    submit_Report    = SubmitField  ('Report')
    submit_Update    = SubmitField  ('Update & Report')
    submit_Cancel    = SubmitField  ('Cancel')

# Customer filter form
class frm_charging_resume_customer(Form):
    User_Id          = 0 
    Cus_Id           = SelectField  ("Customer?", validators=[DataRequired()], coerce=int)
    CIT_Date_From    = DateField    ("Billing Data from?", validators=[DataRequired()], format="%Y-%m-%d")
    CIT_Date_To      = DateField    ("Billing Data up to?", validators=[DataRequired()], format="%Y-%m-%d")
    CIT_Status       = SelectField  ("Status to Report?", coerce=int)
    Cur_Code         = SelectField  ("Currency to Report?", coerce=str)

    submit_Report    = SubmitField  ('Report')
    submit_Update    = SubmitField  ('Update & Report')
    submit_Cancel    = SubmitField  ('Cancel')

class frm_charging_resume_costcenter(Form):
    CC_Id            = SelectField  ("Cost Center?", validators=[DataRequired()], coerce=int)
    CIT_Date_From    = DateField    ("Billing Data from?", validators=[DataRequired()], format="%Y-%m-%d")
    CIT_Date_To      = DateField    ("Billing Data up to?", validators=[DataRequired()], format="%Y-%m-%d")
    CIT_Status       = SelectField  ("Status to Report?", coerce=int)
    Cur_Code         = SelectField  ("Currency to Report?", coerce=str)

    submit_Report    = SubmitField  ('Report')
    submit_Update    = SubmitField  ('Update & Report')
    submit_Cancel    = SubmitField  ('Cancel')

class frm_charging_resume_platform_new(Form):
    Pla_Id           = SelectField  ("Platform?", validators=[DataRequired()], coerce=int)
    CIT_Date_From    = DateField    ("Billing Data from?", validators=[DataRequired()], format="%Y-%m-%d")
    CIT_Date_To      = DateField    ("Billing Data up to?", validators=[DataRequired()], format="%Y-%m-%d")
    CIT_Status       = SelectField  ("Status to Report?", coerce=int)
    Cur_Code         = SelectField  ("Currency to Report?", coerce=str)

    submit_Report    = SubmitField  ('Report')
    submit_Update    = SubmitField  ('Update & Report')
    submit_Cancel    = SubmitField  ('Cancel')

class frm_charging_resume_level_new(Form):
    Cus_Id           = SelectField  ("Customer?", validators=[DataRequired()], coerce=int)
    CIT_Date_From    = DateField    ("Billing Data from?", validators=[DataRequired()], format="%Y-%m-%d")
    CIT_Date_To      = DateField    ("Billing Data up to?", validators=[DataRequired()], format="%Y-%m-%d")
    CIT_Status       = SelectField  ("Status to Report?", coerce=int)
    Cur_Code         = SelectField  ("Currency to Report?", coerce=str)
    Level            = SelectField  ("Report Level?", coerce=int)

    submit_Report    = SubmitField  ('Report')
    submit_Update    = SubmitField  ('Update & Report')
    submit_Cancel    = SubmitField  ('Cancel')
    
class frm_charging_resume_all_new(Form):
    CIT_Date_From    = DateField    ("Billing Data from?", validators=[DataRequired()], format="%Y-%m-%d")
    CIT_Date_To      = DateField    ("Billing Data up to?", validators=[DataRequired()], format="%Y-%m-%d")
    CIT_Status       = SelectField  ("Status to Report?", coerce=int)
    Cur_Code         = SelectField  ("Currency to Report?", coerce=str)

    submit_Report    = SubmitField  ('Report')
    submit_Update    = SubmitField  ('Update & Report')
    submit_Cancel    = SubmitField  ('Cancel')



# =============================================================================
# Export Charging Resume FORM
# (c) Sertechno 2018
# GLVH @ 2018-11-27
# =============================================================================

# =============================================================================
class frm_export_Charging_Resume(Form):
    Export          = SelectField ("Export?", validators=[DataRequired()])
    #CC              = SelectField ("CC Filter?",coerce=str)
    #Platform        = SelectField ("Platform Filter?",coerce=int)

    submit_PDF      = SubmitField ('PDF')
    submit_XLS      = SubmitField ('XLS')
    submit_CSV      = SubmitField ('CSV')
    submit_JSON     = SubmitField ('JSON')
    submit_FIX      = SubmitField ('FIX')
    submit_Cancel   = SubmitField ('Cancel')
    submit_Delete   = SubmitField ('Delete')

# ======================================================================
# Export User Resume FORM
# (c) Sertechno 2019
# GLVH @ 2019-01-05
# ======================================================================
# 2021-04-22 GLVH Add Delete button
# ======================================================================
class frm_export_User_Resume(Form):
    Export          = SelectField ("Export?", validators=[DataRequired()])

    submit_PDF      = SubmitField ('PDF')
    submit_XLS      = SubmitField ('XLS')
    submit_CSV      = SubmitField ('CSV')
    submit_JSON     = SubmitField ('JSON')
    submit_FIX      = SubmitField ('FIX')
    submit_Cancel   = SubmitField ('Cancel')
    submit_Delete   = SubmitField ('Delete')

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

# =============================================================================
# Export User Resume FORM
# (c) Sertechno 2019
# GLVH @ 2019-01-05
# =============================================================================

# =============================================================================
from flask_wtf.file import FileField,FileRequired,FileAllowed

class frm_import_cost_centers(Form):
    Import          = FileField ("Import Cost Centers Data?", validators=[FileRequired(), FileAllowed(['xls'],'XLS Spreadsheets only!!!')])



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

# =============================================================================
# Set Period FORM
# (c) Sertechno 2020
# GLVH @ 2020-03-18
# =============================================================================

# =============================================================================
class frm_test_progress(Form):
    Period          = SelectField ("Active Period ? ", validators=[DataRequired()])

    submit_Set      = SubmitField ('SET')
    submit_Cancel   = SubmitField ('Cancel')

# =============================================================================
# Billing Resume FORM for Customer's user
# (c) Sertechno 2018
# GLVH @ 2019-01-04
# =============================================================================


# =============================================================================
class frm_user_resume(Form):
    CIT_Date_From    = DateField    ("Billing Data from ?", validators=[DataRequired()], format="%Y-%m-%d")
    CIT_Date_To      = DateField    ("Billing Data up to ?", validators=[DataRequired()], format="%Y-%m-%d")
    CIT_Status       = SelectField  ("Status to Report ?", coerce=int)
    Cur_Code         = SelectField  ("Currency to Report ?", coerce=str)
    CC_Id            = SelectField  ("Parent Cost Center ?", coerce=int)

    submit_Report    = SubmitField  ('Report')
    submit_Update    = SubmitField  ('Update & Report')
    submit_Cancel    = SubmitField  ('Cancel')

