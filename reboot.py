import asyncio
import ipaddress
import httpx

HEADERS = {
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.9",
    "Authorization": "Digest username=\"root\", realm=\"antMiner Configuration\", nonce=\"636ab40de322ef7947390661933d122a\", uri=\"/cgi-bin/stats.cgi\", response=\"0c4af9698630ab342c9f4829a8b76565\", qop=auth, nc=00000069, cnonce=\"0225bed6c460240f\"",
    "Connection": "keep-alive",
    "DNT": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
}

async def reboot_device(ip_address):
    url = f"http://{ip_address}/cgi-bin/reboot.cgi"
    HEADERS["Referer"] = f"http://{ip_address}/"
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=HEADERS, timeout=10.0)
            if response.status_code == 200:
                print(f"Successfully rebooted {ip_address}")
            else:
                print(f"Failed to reboot {ip_address}. Status code: {response.status_code}")
        except Exception as e:
            print(f"Error rebooting {ip_address}: {str(e)}")

async def reboot_machines(start_ip, end_ip):
    start = ipaddress.IPv4Address(start_ip)
    end = ipaddress.IPv4Address(end_ip)
    
    ip_range = [str(ipaddress.IPv4Address(ip)) for ip in range(int(start), int(end) + 1)]
    
    tasks = [reboot_device(ip) for ip in ip_range]
    await asyncio.gather(*tasks)

def reboot_ip_range(start_ip, end_ip):
    asyncio.run(reboot_machines(start_ip, end_ip))

# Example usage
if __name__ == "__main__":
    start_ip = "0.0.0.1"
    end_ip = "0.0.0.2"
    reboot_ip_range(start_ip, end_ip)