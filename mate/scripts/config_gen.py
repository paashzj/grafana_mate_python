import os
import sys

if len(sys.argv) == 1:
    GRAFANA_CONF_DIR = "../config/"
else:
    GRAFANA_CONF_DIR = sys.argv[1] + "/conf/"
GRAFANA_CONF = GRAFANA_CONF_DIR + "grafana.ini"

with open(GRAFANA_CONF, "a") as file:
    smtp_enabled = os.getenv("GRAFANA_SMTP_ENABLED")
    if smtp_enabled is None:
        exit()
    file.write("\n")
    file.write("[smtp]\n")
    file.write("enabled = " + smtp_enabled)
    file.write("\n")
    if smtp_enabled == "false":
        exit()
    file.write("host = " + os.getenv("GRAFANA_SMTP_HOST"))
    file.write("\n")
    file.write("user = " + os.getenv("GRAFANA_SMTP_USER"))
    file.write("\n")
    file.write("password = " + os.getenv("GRAFANA_SMTP_PASSWORD"))
    file.write("\n")
    file.write("skip_verify = " + os.getenv("GRAFANA_SMTP_SKIP_VERIFY"))
    file.write("\n")
    file.write("from_address = " + os.getenv("GRAFANA_SMTP_FROM_ADDRESS"))
    file.write("\n")
    file.write("from_name = " + os.getenv("GRAFANA_SMTP_FROM_NAME"))
    file.write("\n")
