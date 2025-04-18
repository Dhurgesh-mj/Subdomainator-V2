import asyncio
from core.plugin_loader import load_plugins
from utils.filter import filter_subdomains
import json 

with open("config.json") as f:
    CONFIG = json.load(f)

found_subdomains = set()

async def run_plugins(plugin , domain , semaphore , timeout , silent):
    async with semaphore:
        try :
            if hasattr(plugin,"run"):
                result = await asyncio.wait_for(plugin.run(domain,CONFIG),timeout=timeout)
                new_sub = filter_subdomains(result)
                for sub in new_sub:
                    if not silent:
                        print(f"[+]{sub}")
                    else:
                        print(sub)
                return new_sub
        except:
            return []

async def subdomain_running(domain , threads = 10 , timeout=10, silent = False):
    plugins = load_plugins()
    semaphore = asyncio.Semaphore(threads)
    task = [run_plugins(plugin , domain , semaphore , timeout , silent) for plugin in plugins]
    results = await asyncio.gather(*task)
    all_subs = set(sub for res in results for sub in res)
    return sorted(all_subs)