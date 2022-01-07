#!/bin/bash

cd $GRAFANA_HOME/mate
mkdir $GRAFANA_HOME/logs
nohup python3 $GRAFANA_HOME/mate/app/main.py >>$GRAFANA_HOME/logs/grafana_mate.stdout.log 2>>$GRAFANA_HOME/logs/grafana_mate.stderr.log &
