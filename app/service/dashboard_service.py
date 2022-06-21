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

from app.const.path import PathConst
from app.service.grafana_req_util import GrafanaReqUtil


class DashboardService:

    def init_dashboard(self):
        print("init dashboard")
        self.init_prom_dashboard()
        self.init_es_dashboard()
        self.init_influx_dashboard()
        self.init_influx2_dashboard()

    def init_prom_dashboard(self):
        print("init prom dashboard")
        folder_id = self.create_folder("Prometheus")
        self.import_dashboard("Prometheus", folder_id, "prometheus", "zookeeper-by-prometheus_rev4.json")
        self.import_dashboard("Prometheus", folder_id, "prometheus", "bookkeeper-by-prometheus.json")
        self.import_dashboard("Prometheus", folder_id, "prometheus", "pulsaroverall-by-prometheus.json")
        self.import_dashboard("Prometheus", folder_id, "prometheus", "pulsarproxy-by-prometheus.json")
        self.import_dashboard("Prometheus", folder_id, "prometheus", "pulsartopics-by-prometheus.json")
        self.import_dashboard("Prometheus", folder_id, "prometheus", "pulsar-jvm-by-prometheus.json")
        self.import_dashboard("Prometheus", folder_id, "prometheus", "mysql_rev1.json")
        self.import_dashboard("Prometheus", folder_id, "prometheus", "coredns_rev2.json")
        self.import_dashboard("Prometheus", folder_id, "prometheus", "jvm-actuator_rev1.json")
        self.import_dashboard("Prometheus", folder_id, "prometheus", "jvm-micrometer_rev9.json")
        self.import_dashboard("Prometheus", folder_id, "prometheus", "go-processes_rev2.json")
        self.import_dashboard("Prometheus", folder_id, "prometheus", "pulsar-functions-by-prometheus.json")
        self.import_dashboard("Prometheus", folder_id, "prometheus", "pulsar-sinks-by-prometheus.json")
        self.import_dashboard("Prometheus", folder_id, "prometheus", "pulsar-sources-by-prometheus.json")

    def init_es_dashboard(self):
        print("init es dashboard")
        folder_id = self.create_folder("Elasticsearch")

    def init_influx_dashboard(self):
        print("init influx dashboard")
        folder_id = self.create_folder("Influx")

    def init_influx2_dashboard(self):
        print("init influx2 dashboard")
        folder_id = self.create_folder("Influx2")

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
    def import_dashboard(title, folder_id, directory, dashboard):
        with open(PathConst.grafana_dashboard_dir + "/" + directory + "/" + dashboard) as file:
            data = file.read()
        dumps = json.dumps({"uid": title, "folderId": folder_id, "dashboard": json.loads(data)})
        body = dumps.encode(encoding='utf-8')
        f = request.urlopen(GrafanaReqUtil.new_dashboard_import_req(), body)
        print(f.status)
        print(f.read().decode('utf-8'))
