import os

var_grafana_host = os.getenv("GRAFANA_HOST")
var_grafana_port = os.getenv("GRAFANA_PORT")
if var_grafana_host is None:
    var_grafana_host = "localhost"
if var_grafana_port is None:
    var_grafana_port = "3000"


class Const:
    grafana_host = var_grafana_host
    grafana_port = var_grafana_port
    username = "admin"
    password = "grafana_pwd"
    old_password = "admin"
