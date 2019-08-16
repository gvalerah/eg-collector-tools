# Import logging functions
import                  logging

# Import time formatter fuctions
from time       import  strftime

from gen_models import  create_app,C,db,logger

# General variables
Dash = "# "+"="*77+"\n"
Do_not_modify="# Auto-Generated code. do not modify\n# (c) Sertechno 2018\n# GLVH @ %s\n"%strftime("%Y-%m-%d %H:%M:%S")
Dash_Jinja = "{# "+"="*77+" #}\n\n"
Do_not_modify_Jinja ="{# Auto-Generated code. do not modify #}\n{# (c) Sertechno 2018 #}\n{# GLVH @ %s #}\n"%strftime("%Y-%m-%d %H:%M:%S")

def print_log(message):
    #print(message)
    logger.info(message)
    
def Mensaje(message):
    print_log("")
    print_log("******************")
    print_log(message)
    print_log("******************")
    print_log("")

def Gen_Views_Permissions(Tab,f):
    if Tab['permission_administer']:
        f.write('@admin_required\n')
    else:
        pass
        """
        if Tab['permission_view']           : f.write('@permission_required(Permission.VIEW)\n')
        if Tab['permission_delete']         : f.write('@permission_required(Permission.DELETE)\n')
        if Tab['permission_modify']         : f.write('@permission_required(Permission.MODIFY)\n')
        if Tab['permission_report']         : f.write('@permission_required(Permission.REPORT)\n')
        if Tab['permission_export']         : f.write('@permission_required(Permission.EXPORT)\n')
        if Tab['permission_view_private']   : f.write('@permission_required(Permission.VIEW_PRIVATE)\n')
        if Tab['permission_modify_private'] : f.write('@permission_required(Permission.MODIFY_PRIVATE)\n')
        """
