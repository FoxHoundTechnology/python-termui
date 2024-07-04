import asyncio
import ipaddress
from requests.auth import HTTPDigestAuth
import requests

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
                
async def check_total_stats(start_ip, end_ip):
    start = ipaddress.IPv4Address(start_ip)
    end = ipaddress.IPv4Address(end_ip)
    
    ip_range = [str(ipaddress.IPv4Address(ip)) for ip in range(int(start), int(end) + 1)]
    
    tasks = [check_stats(ip) for ip in ip_range]

    results = await asyncio.gather(*tasks)
    aggregated_stats = {
           "hashrate": 0,
           "machines": 0,
       }

    for stats in results:
               hashrate = stats['rate_avg']
               aggregated_stats['hashrate'] += round(hashrate/1000, 2)
               aggregated_stats['machines'] += 1

    return aggregated_stats

def check_stats_ip_range(start_ip, end_ip):
    asyncio.run(check_total_stats(start_ip, end_ip))

# Example usage
if __name__ == "__main__":
    start_ip = "0.0.0.1"
    end_ip = "0.0.0.2"
    check_stats_ip_range(start_ip, end_ip)

