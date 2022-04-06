# =============================================================================
# Plugins Fixed Code
# (c) Sertechno 2018
# GLVH @ 2018-11-22
# GLVH @ 2022-03-07 Refactor to bootstrap 5
# =============================================================================
# General Plugins imports
import sys
from .          import main
from datetime   import datetime                         
from flask      import render_template, session, redirect, url_for, current_app, flash

# Application required libraries/modules
import importlib
import importlib.util
from inspect import getmembers, isfunction

# Import configuration functions
import configparser
from configparser import ConfigParser, ExtendedInterpolation
import json

from .. import logger

""" Application decorators for routes """
""" Decorators specify main routes to be handled by Collector Solution """

# Here we import al plugin specific members, classes & methods
#from .plugins_code import * OBSOLETE NOT FUNCTIONAL ON COMPILED ENVIRONMENT

@main.route('/plugins_old', methods=['GET', 'POST'])
def plugins_Menu():
    """ Show a list menu of installed plugins """    
    if logger is not None:
        logger.debug("index() IN")
    else:
        print("*** WARNING *** Route: plugins_Menu: logger is undefined. !!! No logging functions possible. !!!")

    print("logger                =",logger)
    print("Configuration File    =",current_app.config['COLLECTOR_CONFIG_FILE'])
    
    config = configparser.ConfigParser(interpolation=ExtendedInterpolation())
    config.read(current_app.config['COLLECTOR_CONFIG_FILE'])
    print("config                =",config)
    
    print("plugins list          =",config.get('Plugins','plugins',fallback='[]'))

    try:
        Installed_Plugins = json.loads(config['Plugins']['plugins'])
        for plugin in Installed_Plugins:
            print(plugin)
    except:
        flash("Coudn't load Plugins ")
        print("Coudn't load Plugins ")
        

    data = []

    for pi in Installed_Plugins:
        pcode = pi['code']
        pdesc = pi['name']
        purl  ="plugins/%s"%pcode
        data.append({'code':pcode,'description':pdesc,'url':purl})
    
    return render_template('plugins.html',data=data)

@main.route('/plugins_old/<code>', methods=['GET', 'POST'])
def plugins_Code(code):
    """ Calls the actual Plugin view function and renders plugins main page depending of Plugin code """
    data = []
    # data[0] will be populated with plugins metadata that should be used later
    plugin_func_name = 'pi_%06d'%int(code)
    # will import function from File system
    # 
    print("logger                =",logger)
    if True:
    #try:
        plugins_paths = [
                "%s/bin"%current_app.root_path[:-4],
                "%s/plugins"%current_app.root_path[:-4],
                "%s/bin/__pycache__"%current_app.root_path[:-4],
                "%s/plugins/__pycache__"%current_app.root_path[:-4],
                "%s/bin"%current_app.root_path,
                "%s/plugins"%current_app.root_path,
                "%s/bin/__pycache__"%current_app.root_path,
                "%s/plugins/__pycache__"%current_app.root_path,
        ]
        plugins_formats = [ 'pyc','py' ]
        
        method=None
        for fmt in plugins_formats:
            for path in plugins_paths:
                if method is None:
                    file_path='%s/%s.%s'%(path,plugin_func_name,fmt)
                    print("file_path             =",file_path)
                    try:
                        spec = importlib.util.spec_from_file_location(plugin_func_name,file_path)
                        module = importlib.util.module_from_spec(spec)
                        spec.loader.exec_module(module)
                        print("module                =",module)
                        method = getattr(module,plugin_func_name)
                        print("method                =",method)
                        print('found                   %s'%file_path)
                        break
                    except:
                        pass
                if method is not None:
                    break
        if method is not None:
            """            
            plugins_path = "%s/plugins"%current_app.root_path
            alternate_plugins_path="%s/plugins"%current_app.root_path[:-4]
            file_path="%s/%s.cpython-36.pyc"%(plugins_path,plugin_func_name)
            module_name=plugin_func_name
            print("current_app.root_path =",current_app.root_path)
            print("alternate plugins path=",alternate_plugins_path)
            print("plugins_path          =",plugins_path)
            print("file_path             =",file_path)
            print("module_name           =",module_name)
            spec = importlib.util.spec_from_file_location(module_name,file_path)
            print("spec                  =",spec)
            #print("spec=",spec,(dir(spec)))
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            print()
            print("module                =",module)
            #print("module=",module,(dir(module)))
            #print("module=",module,module.__dict__)
            
            method = getattr(module,plugin_func_name)
            print()
            #print("method                =",method,(dir(method)))
            print("method                =",method)
            """
            functions_list = [o for o in getmembers(module) if isfunction(o[1])]
            for f in functions_list:
                print("        ",f)
            
            """    
            except Exception as e:
                print("****************")
                print("EXCEPCION e")
                print("¨¨**************")
                Raise(e)
            """
            # Will populate data depending on plugin data gathering function

            #func = globals()[plugin_func_name]
            
            # Data is initialized here for the plugin 

            print("* reading data from method: %s"%method)
            # data is allways expected to be a list
            # evaluate handle it as JSON structure
            # for external process comunications ease
            data=method(data)
            print("data                  = %s"%data)

            form = data[0]['form']
              
            # ------------------------------------------------------------------------------------------------
            # Here executes standard plugins accions
            # Actual version supports up to 8 action buttons per plugin form
            # Each submit form should populate data list and indicate redirection URL in data[0]['redirect']
            # ------------------------------------------------------------------------------------------------
            if form.validate_on_submit():
                if     hasattr(form,'submit_0') and form.submit_0.data:
                    data=form.functions[0](data)
                elif   hasattr(form,'submit_1') and form.submit_1.data:
                    data=form.functions[1](data)
                elif   hasattr(form,'submit_2') and form.submit_2.data:
                    data=form.functions[2](data)
                elif   hasattr(form,'submit_3') and form.submit_3.data:
                    data=form.functions[2](data)
                elif   hasattr(form,'submit_4') and form.submit_4.data:
                    data=form.functions[2](data)
                elif   hasattr(form,'submit_5') and form.submit_5.data:
                    data=form.functions[2](data)
                elif   hasattr(form,'submit_6') and form.submit_6.data:
                    data=form.functions[2](data)
                elif   hasattr(form,'submit_7') and form.submit_7.data:
                    data=form.functions[2](data)
                else:
                    if logger is not None:
                        logger.error("%s: Form Validated but not submited ??? should never get here"%(__name__))
                    else:
                        print("*** ERROR *** Route: plugins_Menu: logger is undefined. !!! No logging functions possible. !!!")
                    data[0]['redirect']='.plugins'
                return redirect(data[0]['redirect'])
        
            # ---------------------------------------------------------
            # Plugin templates will live in app/main/templates/plugins
            # name format is fixed
            # ---------------------------------------------------------
            template="plugins/pi_%06d.html"%int(code)
            print("template              =",template)
            return render_template(template,data=data)
        else:
            return render_template(template,data=data)
        
# =============================================================================
# End of Plugins Fixed Code
# =============================================================================

