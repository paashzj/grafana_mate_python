#!/bin/bash

mkdir -p $GRAFANA_HOME/logs
nohup $GRAFANA_HOME/bin/grafana-server --homepath $GRAFANA_HOME --config $GRAFANA_HOME/conf/grafana.ini web >>$GRAFANA_HOME/logs/grafana.stdout.log 2>>$GRAFANA_HOME/logs/grafana.stderr.log &
