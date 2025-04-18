import aiohttp

async def run(domain, config):
    if not config.get("otx"):
        return []
    try:
        url = f"https://otx.alienvault.com/api/v1/indicators/domain/{domain}/passive_dns"
        
        headers = {
            "X-OTX-API-KEY": config["otx"]  
        }
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers, timeout=10) as response:
                data = await response.json()
                return [item["hostname"] for item in data.get("passive_dns", []) if "hostname" in item]
    except Exception as e:
        return []
