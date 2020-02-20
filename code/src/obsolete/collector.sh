#!/usr/bin/bash

# Collector Application requires exports
COLLECTOR_CONFIG_FILE=/home/gvalera/collector/collector.ini
COLLECTOR_CONFIG=development

SECRET_KEY="Hard to guess string"
COLLECTOR_ADMIN=collector

DEV_DATABASE_URL=mysql+pymysql://collector:Password1\$@localhost:3306/collector
TEST_DATABASE_URL=mysql+pymysql://collector:Password1\$@localhost:3306/collector
TOOLS_DATABASE_URL=mysql+pymysql://collector:Password1\$@localhost:3306/collector
DATABASE_URL=mysql+pymysql://collector:Password1\$@localhost:3306/collector

MAIL_USERNAME=gvalera@sertechno.com
MAIL_PASSWORD=password

LINES_PER_PAGE=10

export COLLECTOR_CONFIG
export COLLECTOR_CONFIG_FILE
export COLLECTOR_ADMIN
export SECRET_KEY
export LINES_PER_PAGE

export DEV_DATABASE_URL
export TEST_DATABASE_URL
export TOOLS_DATABASE_URL
export DATABASE_URL
export MAIL_USERNAME
export MAIL_PASSWORD

export FLASK_APP=collector.py
export FLASK_DEBUG=1
