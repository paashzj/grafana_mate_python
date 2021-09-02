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
