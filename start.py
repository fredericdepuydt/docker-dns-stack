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

## TITLE
echo.section("DOCKER DEPLOYING","Pi-Hole, Cloudflared, OpenVPN (Starting)")

## Starting All Containers
docker.Compose.up("-d")

