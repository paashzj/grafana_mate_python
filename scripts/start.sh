#!/bin/bash

cd $GRAFANA_HOME/mate
python3 $GRAFANA_HOME/mate/app/main.py >>$GRAFANA_HOME/grafana_mate.stdout.log 2>>$GRAFANA_HOME/grafana_mate.stderr.log
tail -f /dev/null