import base64
import json
import urllib
from urllib import request

from app.const.constant import Const
from app.const.path import PathConst
from app.service.grafana_req_util import GrafanaReqUtil


class DashboardService:

    def init_dashboard(self):
        print("init dashboard")
        self.init_prom_dashboard()
        self.init_es_dashboard()
        self.init_influx_dashboard()

    def init_prom_dashboard(self):
        print("init prom dashboard")
        folder_id = self.create_folder("Prometheus")
        self.import_dashboard("Prometheus", folder_id, "zookeeper-by-prometheus_rev4.json")
        self.import_dashboard("Prometheus", folder_id, "bookkeeper-by-prometheus.json")
        self.import_dashboard("Prometheus", folder_id, "pulsaroverall-by-prometheus.json")
        self.import_dashboard("Prometheus", folder_id, "pulsarproxy-by-prometheus.json")
        self.import_dashboard("Prometheus", folder_id, "pulsartopics-by-prometheus.json")
        self.import_dashboard("Prometheus", folder_id, "pulsar-jvm-by-prometheus.json")
        self.import_dashboard("Prometheus", folder_id, "mysql_rev1.json")

    def init_es_dashboard(self):
        print("init es dashboard")
        folder_id = self.create_folder("Elasticsearch")

    def init_influx_dashboard(self):
        print("init influx dashboard")
        folder_id = self.create_folder("Influx")

    @staticmethod
    def create_folder(title):
        dumps = json.dumps({"title": title})
        body = dumps.encode(encoding='utf-8')
        f = request.urlopen(GrafanaReqUtil.new_folders_post_req(), body)
        print(f.status)
        decode = f.read().decode('utf-8')
        json_data = json.loads(decode)
        return json_data['id']

    @staticmethod
    def import_dashboard(title, folder_id, dashboard):
        with open(PathConst.grafana_dashboard_dir + "/" + dashboard) as file:
            data = file.read()
        dumps = json.dumps({"uid": title, "folderId": folder_id, "dashboard": json.loads(data)})
        body = dumps.encode(encoding='utf-8')
        f = request.urlopen(GrafanaReqUtil.new_dashboard_import_req(), body)
        print(f.status)
        print(f.read().decode('utf-8'))
