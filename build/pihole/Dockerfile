FROM pihole/pihole:2026.04.0

LABEL maintainer="Frederic Depuydt <frederic.depuydt@outlook.com>"
LABEL org.opencontainers.image.created="2026-04-18"

ARG S6_OVERLAY_VERSION=3.2.2.0
ARG TARGETPLATFORM

RUN case "${TARGETPLATFORM}" in \
      "linux/amd64")   S6_ARCH="x86_64" ;; \
      "linux/386")     S6_ARCH="i686" ;; \
      "linux/arm64")   S6_ARCH="aarch64" ;; \
      "linux/arm/v7")  S6_ARCH="arm" ;; \
      "linux/arm/v6")  S6_ARCH="armhf" ;; \
      "linux/riscv64") S6_ARCH="riscv64" ;; \
      *) echo "Unsupported TARGETPLATFORM=${TARGETPLATFORM}" >&2; exit 1 ;; \
    esac && \
    wget -O /tmp/s6-overlay-noarch.tar.xz \
      "https://github.com/just-containers/s6-overlay/releases/download/v${S6_OVERLAY_VERSION}/s6-overlay-noarch.tar.xz" && \
    wget -O /tmp/s6-overlay-noarch.tar.xz.sha256 \
      "https://github.com/just-containers/s6-overlay/releases/download/v${S6_OVERLAY_VERSION}/s6-overlay-noarch.tar.xz.sha256" && \
    wget -O /tmp/s6-overlay-${S6_ARCH}.tar.xz \
      "https://github.com/just-containers/s6-overlay/releases/download/v${S6_OVERLAY_VERSION}/s6-overlay-${S6_ARCH}.tar.xz" && \
    wget -O /tmp/s6-overlay-${S6_ARCH}.tar.xz.sha256 \
      "https://github.com/just-containers/s6-overlay/releases/download/v${S6_OVERLAY_VERSION}/s6-overlay-${S6_ARCH}.tar.xz.sha256" && \
    cd /tmp && \
    sha256sum -c s6-overlay-noarch.tar.xz.sha256 && \
    sha256sum -c s6-overlay-${S6_ARCH}.tar.xz.sha256 && \
    tar -C / -Jxpf /tmp/s6-overlay-noarch.tar.xz && \
    tar -C / -Jxpf /tmp/s6-overlay-${S6_ARCH}.tar.xz && \
    apk add --no-cache keepalived && \
    rm -f /tmp/s6-overlay-*.tar.xz /tmp/s6-overlay-*.sha256

COPY ./s6-rc.d/ /etc/s6-overlay/s6-rc.d/
COPY ./keepalived/ /etc/keepalived/

ENTRYPOINT ["/init"]