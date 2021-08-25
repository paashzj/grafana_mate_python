FROM ttbb/grafana:nake

LABEL maintainer="shoothzj@gmail.com"

RUN pip3 install flask

COPY mate /opt/sh/grafana/mate

WORKDIR /opt/sh/grafana

CMD ["/usr/local/bin/dumb-init", "bash", "-vx", "/opt/sh/grafana/mate/scripts/start.sh"]