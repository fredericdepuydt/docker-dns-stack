# Smallest base image
FROM alpine

LABEL maintainer="Frederic Depuydt <frederic.depuydt@outlook.com>"

# Preparing image
RUN apk update
RUN	apk add ca-certificates libc6-compat;

# Installing cloudflared
RUN	wget https://bin.equinox.io/c/VdrWdbjqyF/cloudflared-stable-linux-arm.tgz; \
	tar -xvzf cloudflared-stable-linux-arm.tgz; \
	cp ./cloudflared /usr/local/bin; \
	chmod +x /usr/local/bin/cloudflared; \
	rm -rf /var/cache/apk/*; \
	rm cloudflared; \ 
	rm cloudflared-stable-linux-arm.tgz; \
	cloudflared -v

HEALTHCHECK --interval=600s --timeout=10s --retries=3 CMD wget -q --tries=1 --spider https://1.1.1.1/ || wget -q --tries=1 --spider https://1.0.0.1/ || exit 1

CMD ["/bin/sh", "-c", "/usr/local/bin/cloudflared proxy-dns --address 0.0.0.0 --port 54 --upstream https://1.1.1.1/.well-known/dns-query --upstream https://1.0.0.1/.well-known/dns-query"]
