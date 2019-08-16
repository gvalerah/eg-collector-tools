from .gen_functions             import print_log
# General variables
from gen.gen_functions          import Dash,Do_not_modify,Dash_Jinja,Do_not_modify_Jinja
from gen.gen_menu_functions     import auto_models

def Gen_Model_Base(app_folder):
    # --------------------------------
    # Creating Base Connection module    
    # --------------------------------
    file_name=auto_models+"/base.py"

    #logger.debug("Creating '%s'..."%(file_name))

    f=open(file_name,'w')

    f.write(Dash)
    f.write(Do_not_modify)
    f.write(Dash)
    f.write("from sqlalchemy import create_engine\n")
    f.write("from sqlalchemy.ext.declarative import declarative_base\n")
    f.write("from sqlalchemy.orm import sessionmaker\n\n")
    
    f.write("Base = declarative_base()\n\n")

    f.close()

