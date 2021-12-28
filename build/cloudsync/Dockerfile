## URLs:
##   https://devopsheaven.com/cron/docker/alpine/linux/2017/10/30/run-cron-docker-alpine.html

# Smallest base image
FROM alpine

LABEL maintainer="Frederic Depuydt <frederic.depuydt@outlook.com>"

## Installing git
RUN apk add git

## Directories used by cloudsync:
# - /usr/local/bin/my-pihole-lists   (Contains your own github repo)
# - /usr/local/bin/pihole-cloudsync  (Contains the cloudsync script)
# - /etc/pihole
# - /etc/dnsmasq.d

WORKDIR /usr/local/bin
RUN git clone https://github.com/stevejenkins/pihole-cloudsync.git pihole-cloudsync
RUN git clone --bare https://github.com/stevejenkins/my-pihole-lists my-pihole-lists
WORKDIR /usr/local/bin/my-pihole-lists
RUN git push --mirror https://github.com/fredericdepuydt/docker-pihole-cloudsync

RUN . /usr/local/bin/pihole-cloudsync/pihole-cloudsync --initpush

## Mirroring repo
WORKDIR /tmp/pihole-cloudsync
#https://github.com/stevejenkins/my-pihole-lists


## Cleaning up image
RUN rm -rf /tmp/* /var/tmp/* /var/cache/apk/* /var/cache/distfiles/*