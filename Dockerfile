FROM ttbb/grafana:nake

LABEL maintainer="shoothzj@gmail.com"

RUN dnf install -yq pip && \
    dnf clean all
RUN pip install flask

COPY . /opt/sh/grafana/mate

WORKDIR /opt/sh/grafana

CMD ["/usr/bin/dumb-init", "bash", "-vx", "/opt/sh/grafana/mate/scripts/start.sh"]
