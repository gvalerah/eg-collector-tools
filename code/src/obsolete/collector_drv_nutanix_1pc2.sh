#!/usr/bin/bash
HOME_FOLDER=/home/gvalera
COLLECTOR_FOLDER=${HOME_FOLDER}/collector
cd $COLLECTOR_FOLDER

# Collector Application requires exports
source collector.sh

# Activates Python environment
# development version only
source ${HOME_FOLDER}/venv/bin/activate

# Excecutes Daemon setups initialization file
PLUGINS_FOLDER=${COLLECTOR_FOLDER}/service/plugins
COLLECTOR_INI_FILE=${COLLECTOR_FOLDER}/collector.ini
DRIVER_INI_FILE=eg_lab_nutanix_1_pc_v2.ini
DRIVER_INITIALIZATION=${PLUGINS_FOLDER}/${DRIVER_INI_FILE}
#echo python collector_drv_nutanix.py ${DRIVER_INITIALIZATION}
#python collector_drv_nutanix.py ${COLLECTOR_INI_FILE} ${DRIVER_INITIALIZATION}
echo ${COLLECTOR_FOLDER}/dist/collector_drv_nutanix/collector_drv_nutanix ${COLLECTOR_INI_FILE} ${DRIVER_INITIALIZATION}
${COLLECTOR_FOLDER}/dist/collector_drv_nutanix/collector_drv_nutanix ${COLLECTOR_INI_FILE} ${DRIVER_INITIALIZATION}
