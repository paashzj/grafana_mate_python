import base64
import json
from urllib import request

from app.const.constant import Const
from app.service.grafana_req_util import GrafanaReqUtil


class DataSourceService:
    def init_datasource(self):
        self.init_prometheus()
        self.init_elasticsearch()
        self.init_influxdb()

    @staticmethod
    def init_prometheus():
        print("begin to init prometheus")
        dumps = json.dumps(
            {"name": "Prometheus", "type": "prometheus", "url": "http://" + Const.prom_host + ":9090",
             "access": "proxy"})
        body = dumps.encode(encoding='utf-8')
        f = request.urlopen(GrafanaReqUtil.new_datasource_post_req(), body)
        print(f.status)

    @staticmethod
    def init_elasticsearch():
        print("begin to init elasticsearch")
        dumps = json.dumps(
            {"name": "Elasticsearch", "type": "elasticsearch", "url": "http://" + Const.es_host + ":9200",
             "access": "proxy"})
        body = dumps.encode(encoding='utf-8')
        f = request.urlopen(GrafanaReqUtil.new_datasource_post_req(), body)
        print(f.status)

    @staticmethod
    def init_influxdb():
        print("begin to init influx")
        dumps = json.dumps(
            {"name": "InfluxDB", "type": "influxdb", "url": "http://" + Const.influx_host + ":8086",
             "access": "proxy", "user": "admin"})
        body = dumps.encode(encoding='utf-8')
        f = request.urlopen(GrafanaReqUtil.new_datasource_post_req(), body)
        print(f.status)
