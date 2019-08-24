# General variables
from gen.gen_functions                  import Dash,Do_not_modify,Dash_Jinja,Do_not_modify_Jinja,print_log
from gen.gen_views_select_query         import Gen_Views_Select_Query
#from gen.gen_views_select_all_paginated import Gen_Views_Select_All_Paginated
from gen.gen_views_delete               import Gen_Views_Delete
from gen.gen_views_form                 import Gen_Views_Form
from gen.gen_menu_functions             import auto_views    
    
def Gen_Views(Tab,app_folder,f2): 

    #file_name = app_folder+"/tools/views/view_"+Tab['table'].lower()+".py"
    file_name = auto_views+"/view_"+Tab['table'].lower()+".py"
    print_log("Creating '%s'..."%(file_name))
    f = open(file_name,"w")

    f.write(Dash)
    f.write(Do_not_modify)
    f.write(Dash)
    f.write('\n')
    
    Gen_Views_Form(Tab,f,f2)
    
    Gen_Views_Delete(Tab,f)

    Gen_Views_Select_Query(Tab,f)

    f.close()

