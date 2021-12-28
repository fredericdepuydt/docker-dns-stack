# Pi-Hole base image
FROM pihole/pihole:2021.12

LABEL maintainer="Frederic Depuydt <frederic.depuydt@outlook.com>"

RUN apt-get update

# Port 53 - DNS Server 
EXPOSE 53/udp
EXPOSE 53/tcp

# Volume is handled by docker-compose
VOLUME ["/etc/pihole"]
VOLUME ["/etc/dnsmasq.d"]
