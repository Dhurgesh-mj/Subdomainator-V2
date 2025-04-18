import asyncio
from core.plugin_loader import load_plugins
from utils.filter import filter_subdomains
import json 

with open("config.json") as f:
    CONFIG = json.load(f)

#found_subdomains = set()

async def run_plugins(plugin, domain, semaphore, timeout, silent):
    async with semaphore:
        try:
            if hasattr(plugin, "run"):
                result = await asyncio.wait_for(plugin.run(domain, CONFIG), timeout=timeout)
                return filter_subdomains(result)  # filter inside each plugin
        except Exception as e:
            print(f"[!] Plugin error: {e}")
            return []


async def subdomain_running(domain, threads=10, timeout=10, silent=False):
    plugins = load_plugins()
    semaphore = asyncio.Semaphore(threads)
    tasks = [run_plugins(plugin, domain, semaphore, timeout, silent=True) for plugin in plugins]
    results = await asyncio.gather(*tasks)
    all_subs = set(sub for res in results for sub in res)
    if not silent:
        for sub in sorted(all_subs):
            print(f"[+] {sub}")
    else:
        for sub in sorted(all_subs):
            print(sub)

    return sorted(all_subs)
