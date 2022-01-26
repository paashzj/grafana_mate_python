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

import os

var_grafana_host = os.getenv("GRAFANA_HOST")
var_grafana_port = os.getenv("GRAFANA_PORT")
var_prom_host = os.getenv("PROM_HOST")
var_es_host = os.getenv("ES_HOST")
var_influx_host = os.getenv("INFLUX_HOST")
if var_grafana_host is None:
    var_grafana_host = "localhost"
if var_grafana_port is None:
    var_grafana_port = "3000"
if var_prom_host is None:
    var_prom_host = "localhost"
if var_es_host is None:
    var_es_host = "localhost"
if var_influx_host is None:
    var_influx_host = "localhost"


class Const:
    grafana_host = var_grafana_host
    grafana_port = var_grafana_port
    prom_host = var_prom_host
    es_host = var_es_host
    influx_host = var_influx_host
    username = "admin"
    password = "grafana_pwd"
    old_password = "admin"
