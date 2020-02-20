#!/usr/bin/bash
HOME_FOLDER=/home/gvalera
COLLECTOR_FOLDER=${HOME_FOLDER}/collector
cd $COLLECTOR_FOLDER

# Collector Application requires exports
#source collector.sh

# Excecutes Daemon setups initialization file
COLLECTOR_INI_FILE=${COLLECTOR_FOLDER}/collector.ini
DRIVER_GROUP=Nutanix_1_PC_3
if [ $1  == "PYTHON" ]
then
    # Activates Python environment
    # development version only
    source ${HOME_FOLDER}/venv/bin/activate
    echo python collector_drv_nutanix.py ${COLLECTOR_INI_FILE} ${DRIVER_GROUP}
         python collector_drv_nutanix.py ${COLLECTOR_INI_FILE} ${DRIVER_GROUP}
else
    echo ${COLLECTOR_FOLDER}/dist/collector_drv_nutanix/collector_drv_nutanix ${COLLECTOR_INI_FILE} ${DRIVER_GROUP}
         ${COLLECTOR_FOLDER}/dist/collector_drv_nutanix/collector_drv_nutanix ${COLLECTOR_INI_FILE} ${DRIVER_GROUP}
fi
