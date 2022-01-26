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


class PathConst:
    home_path = os.getenv("GRAFANA_HOME")
    if home_path is None:
        home_path = ""
    mate_path = home_path + "/mate"
    scripts_path = mate_path + "/scripts"
    grafana_init_script = scripts_path + "/init-grafana.sh"
    grafana_start_script = scripts_path + "/start-grafana.sh"
    grafana_dashboard_dir = mate_path + "/dashboard"
