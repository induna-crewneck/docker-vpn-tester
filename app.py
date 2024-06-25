# Docker VPN Checker v1.0
# https://github.com/induna-crewneck/docker-vpn-tester
# Developed and tested on Raspberry Pi OS x64 / Debian 1:6.6.20-1+rpt1 (2024-03-07)

import requests
import time
import sys

def get_ip_and_location():
    try:
        response = requests.get("https://ipinfo.io")
        data = response.json()
        ip = data.get("ip", "N/A")
        location = f'{data.get("city", "N/A")}, {data.get("region", "N/A")}, {data.get("country", "N/A")}'
        return ip, location
    except Exception as e:
        return "N/A", "N/A"

def log_ip_and_location():
    ip, location = get_ip_and_location()
    sys.stdout.write(f"Public IP:   {ip}    {location}\n")
    sys.stdout.flush()
    
sys.stdout.write(f"Starting up...")
if __name__ == "__main__":
    while True:
        log_ip_and_location()
        time.sleep(60)
