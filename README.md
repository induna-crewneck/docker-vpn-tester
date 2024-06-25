# Docker VPN Tester
A simple Docker container that checks the IP and location of your Docker VPN setup.

## Requiremenets
- Docker
- VPN Container in Docker (technically not required, but this project is pretty pointless without it)

## Setup
1. Create a folder, e.g. `mkdir Documents/docker-vpn-tester`
2. Download app.py and Dockerfile to that folder
3. `cd` into that directory, e.g. `cd Documents/docker-vpn-tester`
4. Build docker image: `sudo docker build -t docker-vpn-tester .`
5. Run container:
```
sudo docker run -d \
  --name docker-vpn-tester \
  --network=<NAME OF YOUR VPN NETWORK OR CONTAINER> \
  docker-vpn-tester
```
### Method A: Create a Docker network brdige
```
sudo docker network create --driver bridge vpn_bridge
```
And use `--network=vpn_bridge` when running the vpn docker container.
In this case, use `--network=vpn_bridge` in the run command above.
### Method B: Refer to the VPN Container directly
You can also refer to the installed VPN docker container directly. If, for example, you have a docker container named `openvpn`, you can use `--network=container:openvpn` in the run command above.
