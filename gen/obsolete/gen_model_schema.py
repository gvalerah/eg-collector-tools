import os
from sqlalchemy import text
# General variables
from gen.gen_functions          import Dash,Do_not_modify,Dash_Jinja,Do_not_modify_Jinja,print_log
from gen.gen_menu_functions     import auto_models
from gen.gen_menu_functions     import auto_forms
from gen.gen_menu_functions     import source_includes
from gen.gen_menu_functions     import Include_File



def Gen_Model_Schema():
    # ------------------------------------------------------------------
    # Create Class SQL Alchemy for direct non Flask DB Handling
    # ------------------------------------------------------------------

    list_files["orm_platforms_table.py",]


    file_name = auto_models+"/orm_model_schema.py"
    print_log("Creating '%s'..."%(file_name))


    f= open(file_name2,"w")
    
    f.write("from sqlalchemy                 import Table, Column, MetaData, ForeignKey")
    f.write("from sqlalchemy                 import Integer, String, Date, Time, Numeric, DateTime, Boolean")
    f.write("Meta = MetaData()")

    f.write(Dash)
    f.write(Do_not_modify)
    f.write(Dash)
    f.write('\n')
    f.write('def Create_Tables(db):\n')
    
    for filename in list_files:
        file_name = auto_models+filename
        Include_File(file_name,f)
    
    f.write('\n')
    
    f.close()
    

