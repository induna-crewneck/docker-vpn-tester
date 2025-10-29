# Docker VPN Checker v2.1
# https://github.com/induna-crewneck/docker-vpn-tester
# Developed and tested on Raspberry Pi OS x64 / Debian 1:6.6.20-1+rpt1 (2024-03-07)

import requests
import time
import sys
from datetime import datetime

def get_ip_and_location():
    try:
        response = requests.get("https://ipinfo.io")
        data = response.json()
        ip = data.get("ip", "N/A")
        location = f'{data.get("city", "N/A")}, {data.get("region", "N/A")}, {data.get("country", "N/A")}'
        if "N/A, N/A, N/A" in location and ip == "N/A":
            response2 = requests.get("https://ipv4.icanhazip.com")
            ip = response2.text.replace('\n', '')
            location = "N/A (ipinfo rate likely exceeded)"
        return ip, location
    except Exception as e:
        print(f"Exception: {e}")
        return "N/A", f"N/A ({e})"

def log_ip_and_location():
    ip, location = get_ip_and_location()
    spaces = " " * (20 - len(ip))
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sys.stdout.write(f"[{timestamp}] Public IP:   {ip}{spaces} {location}\n")
    sys.stdout.flush()
    
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
sys.stdout.write(f"[{timestamp}] Starting up...\n")

if __name__ == "__main__":
    while True:
        log_ip_and_location()
        time.sleep(60)
