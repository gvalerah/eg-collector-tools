# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-16 15:51:37
# =============================================================================

from decimal import ROUND_HALF_UP

class frm_dev_table(Form):
    Name                              = StringField("Name?")
    Caption                           = StringField("Caption?")
    Entity                            = StringField("Entity?")
    Class_Name                        = StringField("Class Name?")
    Child_Table                       = StringField("Child Table?")
    Parent_Table                      = StringField("Parent Table?")
    Use_Pagination                    = BooleanField("Use Pagination?")
    Use_Children_Pagination           = BooleanField("Use Children Pagination?")
    Generate_Form_One                 = BooleanField("Generate Form One?")
    Generate_Form_All                 = BooleanField("Generate form All?")
    Generate_Form_Filter              = BooleanField("Generate Form Filter?")
    Generate_Children                 = BooleanField("Generate Children?")
    Generate_Foreign_Fields           = BooleanField("Generate Foreign Fields?")
    Permission_View                   = BooleanField("Permission View?")
    Permission_Delete                 = BooleanField("Permission Delete?")
    Permission_Modify                 = BooleanField("Permission Modify?")
    Permission_Report                 = BooleanField("Permission Report?")
    Permission_Export                 = BooleanField("Permission Export?")
    Permission_View_Private           = BooleanField("Permission View Private?")
    Permission_Modify_Private         = BooleanField("Permission Modify Private?")
    Permission_Administer             = BooleanField("Permission Administer?")

    submit_Save                       = SubmitField  ('Save')
    submit_New                        = SubmitField  ('New')
    submit_Cancel                     = SubmitField  ('Cancel')

    has_FKs                           = False

class frm_dev_table_delete(Form):
    submit_Delete                     = SubmitField  ('Delete')
    submit_Cancel                     = SubmitField  ('Cancel')

# =============================================================================
