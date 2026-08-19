FROM yonder00/dnscrypt-proxy:latest AS dnscrypt-proxy

# The upstream image deliberately contains only a BusyBox userspace, not apk.
# Copy its dnscrypt runtime into an Alpine image that can install keepalived.
FROM alpine:3.23

COPY --from=dnscrypt-proxy /usr/local/bin/dnscrypt-proxy /usr/local/bin/dnscrypt-proxy
COPY --from=dnscrypt-proxy /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/ca-certificates.crt
COPY --from=dnscrypt-proxy /app/example-dnscrypt-proxy.toml /app/example-dnscrypt-proxy.toml
COPY --from=dnscrypt-proxy /sbin/su-exec /sbin/su-exec
COPY --from=dnscrypt-proxy /entrypoint.sh /entrypoint.sh

LABEL maintainer="Frederic Depuydt <frederic.depuydt@outlook.com>"
LABEL org.opencontainers.image.created="2026-05-02"

ARG S6_OVERLAY_VERSION=3.2.2.0
ARG TARGETPLATFORM

# Alpine provides apk for the s6-overlay and keepalived dependencies.
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