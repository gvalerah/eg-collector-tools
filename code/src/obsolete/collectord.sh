#!/usr/bin/bash

WORKING_FOLDER=/home/gvalera/collector
cd $WORKING_FOLDER

# Collector Application requires exports
source collector.sh

# Activates Python environment
source /home/gvalera/venv/bin/activate

# Excecutes Daemon
python collectord.py
