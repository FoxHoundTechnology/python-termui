import asyncio
import aiohttp
from requests.auth import HTTPDigestAuth
import requests

import json

# Define the stats function
async def check_stats(ip):
    url = f"http://{ip}/cgi-bin/stats.cgi"
    username = "root"
    password = "root"
    
    try:
        response = await asyncio.to_thread(requests.get, url, auth=HTTPDigestAuth(username, password))
        response.raise_for_status()
        data = response.json()

        rate_avg = data['STATS'][0]['rate_avg']/1000
        rate_avg = round(rate_avg, 2)
        return {"rate_avg": rate_avg}
       
    except Exception as e:
        error_message = f"Unexpected error for IP {ip}: {e}"
        print(error_message)
        return {"error": error_message}
                