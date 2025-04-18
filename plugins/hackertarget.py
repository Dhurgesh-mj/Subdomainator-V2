import aiohttp

async def run(domain , config):
    try:
        url = f"https://api.hackertarget.com/hostsearch/?q={domain}"
        async with aiohttp.ClientSession(url,timeout= 10) as r:
            if r.status != 200:
                return []
            text = await r.text()
            for line in text.spiltlines():
                if domain in line:
                    return [line.spilt(",")[0]]
    except:
        return [] 