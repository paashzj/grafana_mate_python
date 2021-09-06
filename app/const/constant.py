import os

var_grafana_host = os.getenv("GRAFANA_HOST")
var_grafana_port = os.getenv("GRAFANA_PORT")
var_prom_host = os.getenv("PROM_HOST")
var_es_host = os.getenv("ES_HOST")
if var_grafana_host is None:
    var_grafana_host = "localhost"
if var_grafana_port is None:
    var_grafana_port = "3000"
if var_prom_host is None:
    var_prom_host = "localhost"
if var_es_host is None:
    var_es_host = "localhost"


class Const:
    grafana_host = var_grafana_host
    grafana_port = var_grafana_port
    prom_host = var_prom_host
    es_host = var_es_host
    username = "admin"
    password = "grafana_pwd"
    old_password = "admin"
