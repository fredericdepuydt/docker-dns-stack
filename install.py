#!/usr/bin/env python3

############################################################################
## Raspberry-Pi installation script                                       ##
## Author: Frederic Depuydt                                               ##
## Mail: frederic.depuydt@outlook.com                                     ##
##                                                                        ##
## Executing this script requires the 'depuydt' python libraries          ##
############################################################################

## INCLUDES
import sys
sys.path.insert(1, '/usr/local/lib/depuydt/python/')

from echo import echo
from docker import docker
from environment import environment
from mysql import mysql

## TITLE
echo.section("DOCKER DEPLOYING", "Pi-Hole, Cloudflared, OpenVPN (Installing)");

## Checking external networks
docker.network.exists("web");

pihole_password = environment.get("PIHOLE_PASSWORD",True);

## Creating the volumes, networks and containers
docker.compose.up("--build --no-start");

## Setting up openvpn
#container = "openvpn";
#docker.compose.run("--rm", container, "ovpn_genconfig -u \"tcp://openvpn." + environment.get("DOMAINNAME") + ":443\" -n \"10.0.0.3\"");
#docker.compose.run("--rm", container, "ovpn_initpki");

