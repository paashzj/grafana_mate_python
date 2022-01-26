#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#
import json
from urllib import request

from app.const.constant import Const
from app.service.grafana_req_util import GrafanaReqUtil


class DataSourceService:
    def init_datasource(self):
        self.init_prometheus()
        self.init_elasticsearch()
        self.init_influxdb()
        self.init_influxdb2()

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

    @staticmethod
    def init_influxdb2():
        print("begin to init influx")
        dumps = json.dumps(
            {"name": "InfluxDB2", "type": "influxdb", "url": "http://" + Const.influx_host + ":8086",
             "access": "proxy", "jsonData": {"defaultBucket": "telegraf", "version": "Flux"}})
        body = dumps.encode(encoding='utf-8')
        f = request.urlopen(GrafanaReqUtil.new_datasource_post_req(), body)
        print(f.status)
