# ---------------------------------------------- #
# Generator of executioner for Collector Service #
# GLVH                                           #
# 2018-11-24                                     #
# ---------------------------------------------- #

import sys
from time                       import strftime
from common.context             import Context

if (len(sys.argv) > 1):
    config_file = sys.argv[1]
else:
    config_file = "collector.ini"
# Will work with configuration file
C = Context("Collector Daemon",config_file)

file_name=C.config['General']['service_folder']+"/collectord_exec.py"

f=open(file_name,"w")

# General variables
Dash = "# "+"="*77+"\n"
Do_not_modify="# Auto-Generated code. do not modify\n# (c) Sertechno 2018\n# GLVH @ %s\n"%strftime("%Y-%m-%d %H:%M:%S")


if (f):
    print("Generating '%s'"%file_name)
    if (C):
        installed_collectors = int(C.config['Collectors']['Installed_Collectors'])

        f.write(Dash)
        f.write(Do_not_modify)
        f.write(Dash)
            
        f.write(        'from time import strftime\n\n')
        for c in range(installed_collectors):
            f.write(    'from service.collectord_%d import Collector_%d\n'%(c,c))

        f.write(        '\n')
        f.write(        'def Execute_Collector_Daemon(C):\n')
        f.write(        '    C.logger.info("Collector Daemon Execution initiated @ %s"%strftime("%Y-%m-%d %H:%M:%S"))\n')
        f.write(        '    installed_collectors = int(C.config[\'Collectors\'][\'Installed_Collectors\'])\n')
        f.write(        '    C.logger.info("\'%d\' collectors defined",installed_collectors)\n')
        f.write(        '    C.logger.info("%s")\n'%('*'*40))

        f.write(        '    for collector in range(installed_collectors):\n')
        f.write(        '        collector_ini_file = C.config[\'Collectors\'][\'Collector_%d_config\'%collector]\n')
        f.write(        '        C.logger.info("collector %d\'s ini file is \'%s\'",collector,collector_ini_file)\n')

        for c in range(installed_collectors):
            if (c==0):
                f.write('        if   (collector == 0):\n')
                f.write('            Collector_0(C,collector_ini_file)\n')
            else:
                f.write('        elif (collector == %d):\n'%c)
                f.write('            Collector_%d(C,collector_ini_file)\n'%c)
    
        f.write(        '        else:\n')
        f.write(        '            C.logger.error("Collector \'%d\' not installed/defined."%collector)\n')
        f.write(        '        C.logger.info("%s")\n\n'%('*'*40))
        f.write(        '    C.logger.info("Collector Daemon Execution completed @ %s"%strftime("%Y-%m-%d %H:%M:%S"))\n')
        f.write(Dash)

    else:
        print("ERROR Context not created from '%s'"%config_file)
    print("Generated  '%s'"%file_name)
else:
    print("ERROR generating '%s'"%file_name)
    
