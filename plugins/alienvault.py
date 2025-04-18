import aiohttp

async def run(domain, config):
    api_key = config.get("alienvault")
    if not api_key:
        return []

    headers = {"X-OTX-API-KEY": api_key}
    url = f"https://otx.alienvault.com/api/v1/indicators/domain/{domain}/url_list"

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers, timeout=10) as r:
                if r.status == 200:
                    data = await r.json()
                    subdomains = set()
                    for entry in data.get("url_list", []):
                        host = entry.get("domain")
                        if host and host.endswith(domain):
                            subdomains.add(host)
                    return list(subdomains)
                else:
                    return []
    except Exception as e:
        return []
