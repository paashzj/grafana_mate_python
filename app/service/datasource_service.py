import base64
import json
from urllib import request

from app.const.constant import Const


class DatasourceService:
    @staticmethod
    def init_password():
        print("begin to init datasource")
        req = request.Request("http://localhost:3000/api/datasources", method='POST')
        credentials = ('%s:%s' % (Const.username, Const.password))
        encoded_credentials = base64.b64encode(credentials.encode('ascii'))
        req.add_header('Authorization', 'Basic %s' % encoded_credentials.decode("ascii"))
        req.add_header('Content-Type', 'application/json')
        dumps = json.dumps(
            {"name": "Prometheus", "type": "prometheus", "url": "http://localhost:9090", "access": "proxy"})
        body = dumps.encode(encoding='utf-8')
        f = request.urlopen(req, body)
        print(f.status)
