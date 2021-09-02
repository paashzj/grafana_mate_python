#!/bin/bash

echo > $GRAFANA_HOME/conf/grafana.ini
cat $GRAFANA_HOME/mate/config/part1.ini >> $GRAFANA_HOME/conf/grafana.ini
python3 $GRAFANA_HOME/mate/scripts/config_gen.py $GRAFANA_HOME
cat $GRAFANA_HOME/mate/config/part2.ini >> $GRAFANA_HOME/conf/grafana.ini