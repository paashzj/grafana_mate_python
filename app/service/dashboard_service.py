import base64
import json
import urllib
from urllib import request

from app.const.constant import Const
from app.const.path import PathConst


class DashboardService:
    @staticmethod
    def create_folder():
        req = request.Request("http://localhost:3000/api/folders")
        credentials = ('%s:%s' % (Const.username, Const.password))
        encoded_credentials = base64.b64encode(credentials.encode('ascii'))
        req.add_header('Authorization', 'Basic %s' % encoded_credentials.decode("ascii"))
        req.add_header('Content-Type', 'application/json')
        dumps = json.dumps({"title": "Prometheus"})
        body = dumps.encode(encoding='utf-8')
        f = request.urlopen(req, body)
        print(f.status)
        decode = f.read().decode('utf-8')
        json_data = json.loads(decode)
        return json_data['id']

    @staticmethod
    def import_dashboard(folder_id, dashboard):
        with open(PathConst.grafana_dashboard_dir + "/" + dashboard) as file:
            data = file.read()
        req = request.Request("http://localhost:3000/api/dashboards/db")
        credentials = ('%s:%s' % (Const.username, Const.password))
        encoded_credentials = base64.b64encode(credentials.encode('ascii'))
        req.add_header('Authorization', 'Basic %s' % encoded_credentials.decode("ascii"))
        req.add_header('Content-Type', 'application/json')

        dumps = json.dumps({"uid": "Prometheus", "folderId": folder_id, "dashboard": json.loads(data)})
        body = dumps.encode(encoding='utf-8')
        f = request.urlopen(req, body)
        print(f.status)
        print(f.read().decode('utf-8'))

        try:
            with request.urlopen(req, body) as response:
                print(response.status)
                print(response.reason)
                print(response.read().decode('utf-8'))
        except urllib.error.HTTPError as e:
            print(e.read().decode())

    @staticmethod
    def init_dashboard(self):
        print("init dashboard")
        prometheus_folder_id = self.create_folder()
        self.import_dashboard(prometheus_folder_id, "zookeeper-by-prometheus_rev4.json")
        self.import_dashboard(prometheus_folder_id, "bookkeeper-by-prometheus.json")
        self.import_dashboard(prometheus_folder_id, "pulsaroverall-by-prometheus.json")
        self.import_dashboard(prometheus_folder_id, "pulsarproxy-by-prometheus.json")
        self.import_dashboard(prometheus_folder_id, "pulsartopics-by-prometheus.json")
        self.import_dashboard(prometheus_folder_id, "pulsar-jvm-by-prometheus.json")
        self.import_dashboard(prometheus_folder_id, "mysql_rev1.json")
