from app.const.constant import Const


class UrlConst:
    api_prefix = "http://" + Const.grafana_host + ":" + Const.grafana_port + "/api"
    password_url = api_prefix + "/user/password"
    data_sources_url = api_prefix + "/datasources"
    folders_url = api_prefix + "/folders"
    databoards_url = api_prefix + "/dashboards"
    databoards_db_url = databoards_url + "/db"
