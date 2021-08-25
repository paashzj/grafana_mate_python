#!/bin/bash

DIR="$( cd "$( dirname "$0"  )" && pwd  )"

echo > $GRAFANA_HOME/conf/grafana.ini
cat $GRAFANA_HOME/mate/config/part1.ini >> $GRAFANA_HOME/conf/grafana.ini
python3 $GRAFANA_HOME/mate/scripts/config_gen.py $GRAFANA_HOME
cat $GRAFANA_HOME/mate/config/part2.ini >> $GRAFANA_HOME/conf/grafana.ini

bash -x $DIR/start-grafana.sh

sleep 5

curl -X PUT -H 'Content-Type: application/json' 'http://admin:admin@127.0.0.1:3000/api/user/password' -d '{"oldPassword" : "admin", "newPassword" : "grafana_pwd","confirmNew":"grafana_pwd"}'

curl -X POST -H 'Content-Type: application/json' 'http://admin:grafana_pwd@127.0.0.1:3000/api/datasources' -d '{"name":"Prometheus", "type":"prometheus", "url":"http://localhost:9090", "access":"proxy"}'
python3 $GRAFANA_HOME/mate/scripts/config_dashboard.py $GRAFANA_HOME

python3 $GRAFANA_HOME/mate/app.py >$GRAFANA_HOME/grafana_mate.stdout.log 2>$GRAFANA_HOME/grafana_mate.stderr.log
tail -f /dev/null