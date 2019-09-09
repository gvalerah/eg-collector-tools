
# --------------------------------------------
# Collector Menu Auto-Generator
# --------------------------------------------
print()
print("************************************************************")
print("** gen collector menu                                     **")
print("************************************************************")
print()

from gen.gen_menu_functions import *

# define Menu Options
Menu=[]
Menu.append(Option('<h3>Collector</h3>'))
Menu.append(Option('<h3>Customer</h3>'))
Menu.append(Option('<h3>Tables</h3>'))
Menu.append(Option('<h3>Charging Data</h3>'))
Menu.append(Option('<h3>Reports</h3>'))
Menu.append(Option('<h3>Options</h3>'))
Menu.append(Option('<h3>Help</h3>'))

# define Menu Sub Options (cero Based)
# Home
# roles key indicate which Roles will be presented this dub-menu to ...
Menu[HOME]['roles']=(ROLE_CUSTOMER,ROLE_REPORTER,ROLE_CHARGER,ROLE_ADMINISTRATOR,ROLE_AUDITOR,ROLE_GOD)
Menu[HOME]['options'].append(Sub_Option('Login',                               url='/auth/login',hr=True))
Menu[HOME]['options'].append(Sub_Option('Logout',                              url='/auth/logout'))

# Customer
Menu[CUSTOMER]['roles']=(ROLE_CUSTOMER,ROLE_GOD)
Menu[CUSTOMER]['options'].append(Sub_Option('Query User Data',                 url='/forms/User_Data_View',hr=True))
Menu[CUSTOMER]['options'].append(Sub_Option('View Charging Data',              url='/forms/Get_User_Resume'))
Menu[CUSTOMER]['options'].append(Sub_Option('Report Charging Data',            url='/forms/Export_User_Resume',hr=True))
Menu[CUSTOMER]['options'].append(Sub_Option('Claims',                          url='/demo'))

# Tables

Menu[TABLES]['roles']=(ROLE_CHARGER,ROLE_ADMINISTRATOR,ROLE_GOD)
Menu[TABLES]['options'].append(Sub_Option('Platforms',                         url='/select/Platforms_Query'))
Menu[TABLES]['options'].append(Sub_Option('Customers',                         url='/select/Customers_Query'))
Menu[TABLES]['options'].append(Sub_Option('Cost Centers',                      url='/select/Cost_Centers_Query',hr=True))

Menu[TABLES]['options'].append(Sub_Option('Configuration Items',               url='/select/Configuration_Items_Query'))
Menu[TABLES]['options'].append(Sub_Option('Charge Units',                      url='/select/Charge_Units_Query'))
Menu[TABLES]['options'].append(Sub_Option('Charge Items',                      url='/select/Charge_Items_Query'))
Menu[TABLES]['options'].append(Sub_Option('Rates',                             url='/select/Rates_Query',hr=True))


Menu[TABLES]['options'].append(Sub_Option('Countries',                         url='/select/Countries_Query'))
Menu[TABLES]['options'].append(Sub_Option('Currencies',                        url='/select/Currencies_Query'))
Menu[TABLES]['options'].append(Sub_Option('Countries & Currencies',            url='/select/Countries_Currencies_Query',hr=True))

Menu[TABLES]['options'].append(Sub_Option('Exchange Rates',                    url='/select/Exchange_Rates_Query'))
Menu[TABLES]['options'].append(Sub_Option('Measure Units',                     url='/select/Measure_Units_Query',hr=True))

Menu[TABLES]['options'].append(Sub_Option('Charge Items Generation Types',     url='/select/CIT_Generations_Query'))

# GV 20190314 OJO OJO OJO REVISAR ESTE PROGRAMA DESPUES DE DEMO
#Menu[TABLES]['options'].append(Sub_Option('Charge Items Status Types',         url='/select/CIT_Statuses_Query'))
Menu[TABLES]['options'].append(Sub_Option('Charge Items Status Types',         url='/demo'))

Menu[TABLES]['options'].append(Sub_Option('Charge Unit Types',                 url='/select/CU_Types_Query'))
Menu[TABLES]['options'].append(Sub_Option('Charge Unit Conversion Operations', url='/select/CU_Operations_Query'))
Menu[TABLES]['options'].append(Sub_Option('Rate Periods',                      url='/select/Rat_Periods_Query',hr=True))
Menu[TABLES]['options'].append(Sub_Option('Trace records',                     url='/select/Trace_Query',header='Demo Version Only'))
Menu[TABLES]['options'].append(Sub_Option('Tables',                            url='/select/Dev_Tables_Query'))
Menu[TABLES]['options'].append(Sub_Option('Forms',                             url='/select/Dev_Forms_Query'))
Menu[TABLES]['options'].append(Sub_Option('DB Status',                         url='/reports/DB_Status'))


# Processes
Menu[PROCESSES]['roles']=(ROLE_CHARGER,ROLE_ADMINISTRATOR,ROLE_GOD)
Menu[PROCESSES]['options'].append(Sub_Option('Data Consistency Check',         url='/reports/Data_Consistency',hr=True))
Menu[PROCESSES]['options'].append(Sub_Option('Monthly Pre-Charging View (Customer)',            url='/forms/Get_Charging_Resume'))
Menu[PROCESSES]['options'].append(Sub_Option('Monthly Pre-Charging View (Customer) Resume',            url='/forms/Get_Charging_Resume_Level',hr=True))
Menu[PROCESSES]['options'].append(Sub_Option('Monthly Pre-Charging View (Cost Center)',            url='/forms/Get_Charging_Resume_CC'))
# OJO OJO OJO Menu[PROCESSES]['options'].append(Sub_Option('Monthly Pre-Charging View (Platform)',            url='/forms/Get_Charging_Resume_Platform'))
#Menu[PROCESSES]['options'].append(Sub_Option('Monthly Pre-Charging View (Platform)',            url='/demo'))
Menu[PROCESSES]['options'].append(Sub_Option('Monthly Pre-Charging View (Platform)',            url='/forms/Get_Charging_Resume_Platform'))
#Menu[PROCESSES]['options'].append(Sub_Option('Monthly Pre-Charging View (All)',            url='/demo',hr=True))
Menu[PROCESSES]['options'].append(Sub_Option('Monthly Pre-Charging View (All)',            url='/forms/Get_Charging_Resume_All',hr=True))
Menu[PROCESSES]['options'].append(Sub_Option('Delete Saved Pre-Charging Views',            url='/demo'))

Menu[PROCESSES]['options'].append(Sub_Option('Change Charge Items State',       url='/forms/Change_CIT_State'))
Menu[PROCESSES]['options'].append(Sub_Option('Create Periodic Charge Unit',     url='/demo'))
Menu[PROCESSES]['options'].append(Sub_Option('Create Manual Charge Item',       url='/demo',hr=True))
Menu[PROCESSES]['options'].append(Sub_Option('Inject Cost centers',      url='/forms/Import_Cost_Centers'))
Menu[PROCESSES]['options'].append(Sub_Option('Inject Configuration Items',      url='/demo'))
Menu[PROCESSES]['options'].append(Sub_Option('Inject Charge Units',             url='/demo'))
Menu[PROCESSES]['options'].append(Sub_Option('Inject Charge Items',             url='/demo'))
Menu[PROCESSES]['options'].append(Sub_Option('Inject Rates',      url='/demo'))
# Reports
Menu[REPORTS]['roles']=(ROLE_REPORTER,ROLE_CHARGER,ROLE_ADMINISTRATOR,ROLE_AUDITOR,ROLE_GOD)
Menu[REPORTS]['options'].append(Sub_Option('Monthly Pre_Charging (Customer)',              url='/forms/Export_Charging_Resume'))
Menu[REPORTS]['options'].append(Sub_Option('Monthly Pre_Charging (Cost Center)',              url='/demo'))
Menu[REPORTS]['options'].append(Sub_Option('Monthly Pre_Charging (Platform)',              url='/demo'))
Menu[REPORTS]['options'].append(Sub_Option('Monthly Pre_Charging (All)',              url='/demo',hr=True))
Menu[REPORTS]['options'].append(Sub_Option('Delete Saved Pre-Charging Reports',            url='/demo'))
# Options
Menu[OPTIONS]['roles']=(ROLE_ADMINISTRATOR,ROLE_GOD)
Menu[OPTIONS]['options'].append(Sub_Option('Custom Add Ons',                   url='/plugins',hr=True))
Menu[OPTIONS]['options'].append(Sub_Option('System Status',                   url='/demo',header='Administrator',hr=True))
Menu[OPTIONS]['options'].append(Sub_Option('Statistics: Use Per Type',       url='/forms/Get_Stats_Per_Type',header='BETA VERSION'))
Menu[OPTIONS]['options'].append(Sub_Option('Statistics: Graph: Use Per Type',       url='/forms/Get_Graph_Stats_Per_Type'))
Menu[OPTIONS]['options'].append(Sub_Option('Statistics: Graph: Use Per Type Advanced',       url='/forms/Get_Graph_Stats_Per_Type_Filter'))
# Help
Menu[HELP]['roles']=(ROLE_CUSTOMER,ROLE_REPORTER,ROLE_CHARGER,ROLE_ADMINISTRATOR,ROLE_AUDITOR,ROLE_GOD)
Menu[HELP]['options'].append(Sub_Option('FAQ',url='/collector_faq',hr=True))
Menu[HELP]['options'].append(Sub_Option('About Collector',url='/collector_about'))

# --------------------------------------------
print('gen_collector_menu: creating',navbar_file_name,"...")
Gen_Menu(Menu,ACCOUNT)
print('gen_collector_menu:',navbar_file_name,"generated.")

"""
These lines are excluded since .css and menu.html will no longer be used 
# --------------------------------------------
print('gen_collector_menu: creating',style_file_name,"...")
Style()
print('gen_collector_menu:',style_file_name,"generated.")

# --------------------------------------------

print('gen_collector_menu: creating',menu_file_name,"...")
Gen_Doc()
#f.close()
print('gen_collector_menu:',menu_file_name,"generated.")
"""
# --------------------------------------------
print('gen_collector_menu: creating',base_file_name,"...")
f=open(base_file_name,'w')

f.write('{%- extends "bootstrap/base.html" -%}\n')

f.write('{%- block head -%}\n')
f.write('{# { super() } #}\n')      #   Completely overrides twiter's bootstrap default header

Include_File(source_folder+"/base_header.html",f)
#f.write('\n')
f.write('{%- endblock -%}\n')
f.write('{%- block title -%}Collector{%- endblock -%}\n')
f.write('{%- block navbar -%}\n')

Include_File(navbar_file_name,f)

f.write('{%- endblock -%}\n')
f.write('{%- block scripts -%}\n')
f.write('{%- endblock -%}\n')

f.write('{%- block content -%}\n')
# FLASH Generation Code
f.write('    {%- with messages = get_flashed_messages() -%}\n')
f.write('      {%- if messages -%}\n')
f.write('         <ul class=flashes>\n')
f.write('         {%- for message in messages -%}\n')
f.write('           <div class="alert alert-warning">\n')
f.write('             <button type="button" class="close" data-dismiss="alert">&times;</button>\n')
f.write('             {{ message }}\n')
f.write('           </div>\n')
f.write('         {%- endfor -%}\n')
f.write('         </ul>\n')
f.write('      {%- endif -%}\n')
f.write('    {%- endwith -%}\n')
f.write('    {%- block page_content -%}\n')
f.write('    {%- endblock -%}\n')
f.write('</div>\n')


f.write('<!-- Exaple indicates that those scripts should run near the </body> tag -->\n')
f.write('<script src="/static/js/jquery-3.3.1.js"      crossorigin="anonymous"></script>\n')
f.write('<script src="/static/js/popper.min.js"      crossorigin="anonymous"></script>\n')
f.write('<script src="/static/js/bootstrap.min.js"   crossorigin="anonymous"></script>\n')

f.write('{%- endblock -%}\n')

f.close()
print('gen_collector_menu:',base_file_name,"generated.")
# --------------------------------------------
print('gen_collector_menu:',"Completed.")








