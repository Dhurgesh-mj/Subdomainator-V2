import aiohttp
import re

async def run(domain, config):
    try:
        url = f"https://crt.sh/?q=%25.{domain}&output=json"
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=10) as r:
                if r.status != 200:
                    return []
                data = await r.json(content_type=None)
                subdomains = set()
                for item in data:
                    name = item.get("name_value", "")
                    for entry in name.split("\n"):
                        if domain in entry:
                            subdomains.add(entry.strip())
                return list(subdomains)
    except:
        return []
