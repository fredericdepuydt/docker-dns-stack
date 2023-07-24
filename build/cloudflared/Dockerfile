# Smallest base image
FROM cloudflare/cloudflared:2023.7.2

LABEL maintainer="Frederic Depuydt <frederic.depuydt@outlook.com>"

# Health Check
HEALTHCHECK --interval=600s --timeout=10s --retries=3 CMD wget -q --tries=1 --spider https://1.1.1.1/ || wget -q --tries=1 --spider https://1.0.0.1/ || exit 1

# Command / entrypoint of container
CMD ["proxy-dns", "--address", "0.0.0.0", "--port", "53", "--upstream", "https://1.1.1.1/.well-known/dns-query", "--upstream", "https://1.0.0.1/.well-known/dns-query"]

