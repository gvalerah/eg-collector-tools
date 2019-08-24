from .gen_functions     import print_log
# General variables
from .gen_functions                 import Dash,Do_not_modify,Dash_Jinja,Do_not_modify_Jinja
from .gen_templates_select_all      import Gen_Templates_Select_All
from .gen_templates_delete          import Gen_Templates_Delete
from .gen_templates_form            import Gen_Templates_Form


def Gen_Templates(Metadata,Tab,Chd,app_folder):


    Gen_Templates_Form          (Metadata,Tab,Chd,app_folder)    

    Gen_Templates_Delete        (Metadata,Tab,Chd,app_folder)    

    Gen_Templates_Select_All    (Tab,app_folder)

