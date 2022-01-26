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
from urllib import request

from app.const.constant import Const
from app.const.url_constant import UrlConst


class GrafanaReqUtil:
    @staticmethod
    def new_datasource_post_req():
        req = request.Request(UrlConst.data_sources_url, method='POST')
        credentials = ('%s:%s' % (Const.username, Const.password))
        encoded_credentials = base64.b64encode(credentials.encode('ascii'))
        req.add_header('Authorization', 'Basic %s' % encoded_credentials.decode("ascii"))
        req.add_header('Content-Type', 'application/json')
        return req

    @staticmethod
    def new_folders_post_req():
        req = request.Request(UrlConst.folders_url)
        credentials = ('%s:%s' % (Const.username, Const.password))
        encoded_credentials = base64.b64encode(credentials.encode('ascii'))
        req.add_header('Authorization', 'Basic %s' % encoded_credentials.decode("ascii"))
        req.add_header('Content-Type', 'application/json')
        return req

    @staticmethod
    def new_dashboard_import_req():
        req = request.Request(UrlConst.databoards_db_url)
        credentials = ('%s:%s' % (Const.username, Const.password))
        encoded_credentials = base64.b64encode(credentials.encode('ascii'))
        req.add_header('Authorization', 'Basic %s' % encoded_credentials.decode("ascii"))
        req.add_header('Content-Type', 'application/json')
        return req
