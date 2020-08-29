#!/usr/bin/env python3

############################################################################
## Raspberry-Pi installation script                                       ##
## Author: Frederic Depuydt                                               ##
## Mail: frederic.depuydt@outlook.com                                     ##
##                                                                        ##
## Executing this script requires the 'depuydt' python libraries          ##
############################################################################

## INCLUDES
import echo, docker
from depuydt import environment

##import mysql

## TITLE
echo.section("DOCKER DEPLOYING", "Pi-Hole, Cloudflared, OpenVPN (Installing)")

## Checking external networks
docker.Network.exists("web")

env = Environment("./pihole/.env")
env.require("WEBPASSWORD")
env.require("ServerIP")

## Creating the volumes, networks and containers
docker.Compose.up("--build --no-start")
docker.cp("pihole/pihole/.","pihole:/etc/pihole/")
docker.cp("pihole/dnsmasq.d/.","pihole:/etc/dnsmasq.d/")

## Setting up openvpn
#container = "openvpn"
#docker.compose.run("--rm", container, "ovpn_genconfig -u \"tcp://openvpn." + environment.get("DOMAINNAME") + ":443\" -n \"10.0.0.3\"")
#docker.compose.run("--rm", container, "ovpn_initpki")

