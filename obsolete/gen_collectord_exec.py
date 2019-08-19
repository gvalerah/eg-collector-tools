# ---------------------------------------------- #
# Generator of executioner for Collector Service #
# GLVH                                           #
# 2018-11-24                                     #
# ---------------------------------------------- #

import os
import sys
from time                       import strftime
# Import configuration functions
import configparser
from configparser import ConfigParser, ExtendedInterpolation

# Collector's imports
from common.context             import Context

if (len(sys.argv) > 1):
    config_file = sys.argv[1]
else:
    config_file = "collector.ini"
# Will work with configuration file
C = Context("Collector Daemon",config_file)

file_name=C.config['General']['service_folder']+"/collectord_exec.py"

plugins_folder = C.config['General']['service_folder']+"/plugins"
collectors_folder = C.config['General']['service_folder']+"/collectors"
platforms_folder = C.config['General']['service_folder']+"/platforms"

# General variables
Dash = "# "+"="*77+"\n"
Do_not_modify="# Auto-Generated code. do not modify\n# (c) Sertechno 2018\n# GLVH @ %s\n"%strftime("%Y-%m-%d %H:%M:%S")


# Read local Collector's Configurations from <Collector Service Folder>/plugins (*.ini files)
collector_configurations = [f for f in os.listdir(plugins_folder) if f.endswith('.ini')]

f = open(file_name,'w')

if (f):
    print("Generating '%s'"%(file_name))
    if (C):
        imported_collectors = []
        collectors = []
        
        # Get's the number of actual collector configurations
        installed_collectors = len(collector_configurations)

        f.write(Dash)
        f.write(Do_not_modify)
        f.write(Dash)
            
        f.write(        'from time import strftime\n\n')
        for c in range(installed_collectors):
            config = configparser.ConfigParser(interpolation=ExtendedInterpolation())
            print("\tLeyendo configuracion desde: '%s'"%collector_configurations[c])
            # Reads actual configuration file
            config.read("%s/%s"%(plugins_folder,collector_configurations[c]))
            # Looks for corresponfing collector Module
            collectors.append(config['General']['collector'])
            # Import Collector Module if not already imported 
            if collectors[c] not in imported_collectors:
                f.write(    'from .collectors.%-30s import %s_Collector\n'%(collectors[c],collectors[c]))
                imported_collectors.append(collectors[c])
                
        f.write(        '\n')
        f.write(        'def Execute_Collector_Daemon(C):\n')
        f.write(        '    C.logger.info("Collector Daemon Execution initiated @ %s"%strftime("%Y-%m-%d %H:%M:%S"))\n\n')
        f.write(        '    C.logger.info("\'%d\' collectors defined")\n'%installed_collectors)
        f.write(        '    C.logger.info("%s")\n'%('*'*40))
        f.write(        '    try:\n')
        
        for c in range(installed_collectors):
            f.write(    '        %s_Collector(C,\'%s/%s\')\n'%(collectors[c],plugins_folder,collector_configurations[c]))   
        
        f.write(        '    except Exception as e:\n')
        f.write(        '        C.logger.error("collectord_exec: Exception: %s"%(e))\n')

        f.write(        '    C.logger.info("%s")\n\n'%('*'*40))
        f.write(        '    C.logger.info("Collector Daemon Execution completed @ %s"%strftime("%Y-%m-%d %H:%M:%S"))\n')
        f.write(Dash)

    else:
        print("ERROR Context not created from '%s'"%config_file)
    print("\tGenerated '%s' for %d collectors."%(file_name,installed_collectors))
else:
    print("ERROR generating '%s'"%file_name)
print("Generation of '%s' completed."%(file_name))
print()
