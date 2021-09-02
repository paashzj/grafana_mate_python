from app.const.constant import Const


class UrlConst:
    api_prefix = "http://" + Const.grafana_host + ":" + Const.grafana_port + "/api"
    password_url = api_prefix + "/user/password"
