#!/usr/bin/env python3

############################################################################
## Author: Frederic Depuydt                                               ##
## Mail: frederic.depuydt@outlook.com                                     ##
############################################################################

## INCLUDES
from depuydt import docker

#env = Environment("./pihole/.env")
#env.require("WEBPASSWORD")
#env.require("ServerIP")

## Creating the volumes, networks and containers
#docker.Compose.up("--build --no-start")
docker.cp("config/pihole/.","pihole:/etc/pihole/")
#docker.cp("pihole/dnsmasq.d/.","pihole:/etc/dnsmasq.d/")

## Setting up openvpn
#container = "openvpn"
#docker.compose.run("--rm", container, "ovpn_genconfig -u \"tcp://openvpn." + environment.get("DOMAINNAME") + ":443\" -n \"10.0.0.3\"")
#docker.compose.run("--rm", container, "ovpn_initpki")

