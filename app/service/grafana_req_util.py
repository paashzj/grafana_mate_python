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
