#!/usr/bin/bash
# Default /home/collector
WORKING_FOLDER=/home/gvalera/collector
# Default gUnicorn configuration:
# timeout 300 Host 0.0.0.0 port 8000 workers 2-4 per CPU core
TIMEOUT=300
HOST=0.0.0.0
PORT=8000
WORKERS=2

cd $WORKING_FOLDER

# Collector Application requires exports
source collector.sh

# Activates Python environment
source /home/gvalera/venv/bin/activate

# Excecutes Daemon
# Test Command is:
# python collector.py runserver --host 0.0.0.0
# Runtime:
# gunicorn handles charge balance an runs service in port 8000
# NGinX then Reverses proxy calls to this server
#gunicorn collector:app --timeout 300
gunicorn collector:app --timeout $TIMEOUT --bind=$HOST:$PORT --workers=$WORKERS
