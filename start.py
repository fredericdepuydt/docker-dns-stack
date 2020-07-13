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

## TITLE
echo.section("DOCKER DEPLOYING","Pi-Hole, Cloudflared, OpenVPN (Starting)");

## Starting All Containers
docker.compose.up("-d");

