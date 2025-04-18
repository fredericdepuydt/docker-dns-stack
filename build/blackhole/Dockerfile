FROM traefik:v2.10.4
LABEL maintainer="Frederic Depuydt <frederic.depuydt@outlook.com>"
LABEL release-date="2023-08-06"

# INSTALLING S6-OVERLAY
ARG S6_OVERLAY_VERSION=3.1.5.0
ADD https://github.com/just-containers/s6-overlay/releases/download/v${S6_OVERLAY_VERSION}/s6-overlay-noarch.tar.xz /tmp
RUN tar -C / -Jxpf /tmp/s6-overlay-noarch.tar.xz
ADD https://github.com/just-containers/s6-overlay/releases/download/v${S6_OVERLAY_VERSION}/s6-overlay-x86_64.tar.xz /tmp
RUN tar -C / -Jxpf /tmp/s6-overlay-x86_64.tar.xz
ADD ./s6-rc.d /etc/s6-overlay/s6-rc.d
ENTRYPOINT ["/init"]

# INSTALLING KEEPALIVED
RUN apk add keepalived
ADD ./keepalived /etc/keepalived
