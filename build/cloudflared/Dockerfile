FROM alpine:latest

# Install dependencies:
# - ca-certificates: required for HTTPS
# - curl: used to download cloudflared
# - bind-tools: provides dig
RUN apk add --no-cache \
    ca-certificates \
    curl \
    bind-tools

# Download and install cloudflared for the target architecture
RUN set -eux; \
    ARCH="$(uname -m)"; \
    case "$ARCH" in \
        x86_64)  CF_ARCH="amd64" ;; \
        aarch64) CF_ARCH="arm64" ;; \
        armv7l)  CF_ARCH="arm" ;; \
        *) echo "Unsupported architecture: $ARCH" >&2; exit 1 ;; \
    esac; \
    curl -fsSL "https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-${CF_ARCH}" \
        -o /usr/local/bin/cloudflared; \
    chmod +x /usr/local/bin/cloudflared

# Expose DNS port
EXPOSE 53/udp
EXPOSE 53/tcp

# Healthcheck: query one.one.one.one via the local DNS listener
HEALTHCHECK --interval=30s --timeout=5s --retries=3 \
  CMD dig @127.0.0.1 one.one.one.one +short || exit 1

# Run cloudflared DNS proxy
CMD ["cloudflared", "proxy-dns", "--address", "0.0.0.0", "--port", "53", "--upstream", "https://1.1.1.1/.well-known/dns-query", "--upstream", "https://1.0.0.1/.well-known/dns-query"]