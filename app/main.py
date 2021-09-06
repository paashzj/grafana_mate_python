import os
import sys

sys.path.append(os.getcwd())

import subprocess
import time
from sys import platform

from flask import Flask

from app.const.path import PathConst
from app.service.account_service import AccountService
from app.service.datasource_service import DataSourceService
from app.service.dashboard_service import DashboardService

if platform == "linux":
    subprocess.call(['/bin/bash', PathConst.grafana_init_script])
    subprocess.call(['/bin/bash', PathConst.grafana_start_script])

time.sleep(5)

# password
account_service = AccountService()
account_service.init_password()

# datasource
data_source_service = DataSourceService()
data_source_service.init_datasource()

# folder

# dashboard
dashboard_service = DashboardService()
DashboardService.init_dashboard(dashboard_service)

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run(port=31017)
