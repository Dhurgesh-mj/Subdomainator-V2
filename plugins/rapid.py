import aiohttp
import re

async def run(domain, config):
    try:
        url = f"https://rapiddns.io/subdomain/{domain}?full=1"
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=10) as r:
                html = await r.text()
                return list(set(re.findall(rf"([\w.-]+\.{re.escape(domain)})", html)))
    except:
        return []
