# Docker VPN Checker v1.0
# https://github.com/induna-crewneck/docker-vpn-tester
# Developed and tested on Raspberry Pi OS x64 / Debian 1:6.6.20-1+rpt1 (2024-03-07)

FROM python:3.9-slim

RUN pip install requests

WORKDIR /app
COPY app.py /app/app.py

CMD ["python", "app.py"]
