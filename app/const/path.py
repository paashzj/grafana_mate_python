import os


class PathConst:
    home_path = os.getenv("GRAFANA_HOME")
    if home_path is None:
        home_path = ""
    mate_path = home_path + "/mate"
    scripts_path = mate_path + "/scripts"
    grafana_init_script = scripts_path + "/init-grafana.sh"
    grafana_start_script = scripts_path + "/start-grafana.sh"
    grafana_dashboard_dir = mate_path + "/dashboard"
