# AGENTS.md

## Project Overview

This repository deploys a redundant DNS stack onto an existing external Docker network named `dns`:

- `dnscrypt` provides encrypted upstream DNS resolution.
- `pihole` provides DNS filtering and uses dnscrypt as its upstream resolver.
- `nebula-sync` replicates Pi-hole data between peers.
- `keepalived` runs inside both DNS service containers in separate VRRP groups: Pi-hole owns the redundant DNS VIP, while dnscrypt owns the redundant encrypted-upstream VIP.

The compose configuration reads deployment-specific values from an untracked `.env` file; copy `.env.example` as its starting point. Runtime configuration under `config/` is also intentionally untracked.

## Layout

- `docker-compose.yml`: main stack definition. The `dns` network is external.
- `.env.example`: documented, safe template for deployment-specific addresses, VRRP groups, priorities, and common settings.
- `docker-compose.override.yml`: local profile overrides; it is ignored by Git.
- `build/pihole/`: Pi-hole image extended with s6-overlay and keepalived.
- `build/dnscrypt/`: dnscrypt-proxy image extended with the same s6-overlay/keepalived pattern.
- `build/*/s6-rc.d/`: s6-overlay v3 service definitions.
- `build/*/keepalived/keepalived.conf.template`: keepalived template rendered from container environment variables at startup.

## Container Supervision

Custom service images use s6-overlay v3. Each service placed in `s6-rc.d/user/contents.d/` starts in parallel after the `base` bundle:

- The primary DNS daemon must be a `longrun` service and remain in the foreground.
- Keepalived must run as a separate `longrun` using `--dont-fork`; its run script renders `/run/keepalived.conf` from the container environment.
- DNS daemon `finish` scripts halt the container after an unexpected exit. Do not add this behavior to keepalived: s6 should restart keepalived independently.
- Dockerfiles install the architecture-specific s6-overlay tarballs, verify their SHA-256 checksums, install keepalived, copy service definitions/configuration, and set `ENTRYPOINT ["/init"]`.

When changing a base image, confirm its package manager and daemon entrypoint. The dnscrypt base is Alpine and starts via `/entrypoint.sh`; Pi-hole is Alpine and starts via `/usr/bin/start.sh`.

## High Availability Rules

- Both `dnscrypt` and `pihole` need `NET_ADMIN`, `NET_RAW`, and `NET_BROADCAST` so keepalived can manage the virtual address and VRRP traffic.
- Each service has its own VRRP group. Keep `PIHOLE_VRRP_INSTANCE`/`PIHOLE_VRRP_ID`/`PIHOLE_VIRTUAL_IP` identical across Pi-hole peers, and separately keep `DNSCRYPT_VRRP_INSTANCE`/`DNSCRYPT_VRRP_ID`/`DNSCRYPT_VIRTUAL_IP` identical across dnscrypt peers. The two VRRP IDs and virtual IPs must differ.
- Set `PIHOLE_VRRP_PRIORITY` and `DNSCRYPT_VRRP_PRIORITY` per peer to select an initial preferred owner; keep `nopreempt` unless planned failback is required.
- Define those variables in the ignored `.env` file (for example, Pi-hole VIP `192.168.2.100/24` and dnscrypt VIP `192.168.2.200/24`) rather than hard-coding addresses in tracked files. Docker Compose passes them to the containers, where the templates are rendered.
- Ensure the services share the same L2-capable external network; ordinary Docker bridge networks do not provide host-LAN VIP failover without suitable network configuration.

## Change and Validation Guidance

- Keep image changes architecture-aware: `TARGETPLATFORM` maps to the s6 release architecture in each Dockerfile.
- Use `docker compose -f docker-compose.yml config` to validate compose rendering.
- Build the affected image with `docker compose build dnscrypt` or `docker compose build pihole`.
- Verify both daemons under s6 after startup, then test VRRP ownership and failover from a second peer deployment.
- Do not commit `.env`, `config/`, or `docker-compose.override.yml`.
