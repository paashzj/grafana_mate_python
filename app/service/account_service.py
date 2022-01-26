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

import base64
import json
from urllib import request

from app.const.constant import Const
from app.const.url_constant import UrlConst


class AccountService:
    @staticmethod
    def init_password():
        print("begin to init password")
        req = request.Request(UrlConst.password_url, method='PUT')
        credentials = ('%s:%s' % (Const.username, Const.old_password))
        encoded_credentials = base64.b64encode(credentials.encode('ascii'))
        req.add_header('Authorization', 'Basic %s' % encoded_credentials.decode("ascii"))
        req.add_header('Content-Type', 'application/json')
        dumps = json.dumps({"oldPassword": "admin", "newPassword": "grafana_pwd", "confirmNew": "grafana_pwd"})
        body = dumps.encode(encoding='utf-8')
        f = request.urlopen(req, body)
        print(f.status)
