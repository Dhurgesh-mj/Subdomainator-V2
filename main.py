import argparse
import asyncio
import os
import json
from core.runner import subdomain_running 
from core.brute import load_run

def display_banner():
    # """Display an ASCII art banner for the tool."""
    banner = r"""
             ____        _     ____                  _             _             
            / ___| _   _| |__ |  _ \  ___  _ __ ___ (_)_ __   __ _| |_ ___  _ __ 
            \___ \| | | | '_ \| | | |/ _ \| '_ ` _ \| | '_ \ / _` | __/ _ \| '__|     [V2]
            ___) | |_| | |_) | |_| | (_) | | | | | | | | | | (_| | || (_) | |   
            |____/ \__,_|_.__/|____/ \___/|_| |_| |_|_|_| |_|\__,_|\__\___/|_|   
                                                                                                                                
                                                                                                    - DHRUGESH M.J"""
    print(banner)
def parse_args():
    parser = argparse.ArgumentParser(description="Subfinder-like async subdomain finder")
    parser.add_argument('-d', '--domain', help='Target domain')
    parser.add_argument('-ld', '--list', help='File with list of domains')
    parser.add_argument('-o', '--output', help='Output file')
    parser.add_argument('-oJ', '--json', help='Output JSON file')
    parser.add_argument('-oD', '--output-dir', help='Save results in dir for each domain')
    parser.add_argument('-t', '--threads', type=int, default=10, help='Concurrency level')
    parser.add_argument('--silent', action='store_true', help='Only print subdomains')
    parser.add_argument('--timeout', type=int, default=10, help='Timeout per plugin')
    parser.add_argument('--bruteforce', action='store_true', help='Enable brute-force subdomain enumeration')
    parser.add_argument('--wordlist', help='Path to wordlist for brute-force')
    return parser.parse_args()

async def handle_domain(domain, args):
    results = await subdomain_running(domain, threads=args.threads, timeout=args.timeout, silent=args.silent)

    if args.output:
        with open(args.output, 'a') as f:
            f.write("\n".join(results) + "\n")

    if args.json:
        with open(args.json, 'a') as f:
            json.dump({domain: results}, f, indent=2)

    if args.output_dir:
        os.makedirs(args.output_dir, exist_ok=True)
        with open(os.path.join(args.output_dir, f"{domain}.txt"), 'w') as f:
            f.write("\n".join(results))

def main():
    os.system("clear" if os.name == "posix" else "cls")
    display_banner()
    args = parse_args()

    if args.bruteforce:
        if not args.domain:
            print("[-] Brute-force mode requires a single domain (use -d).")
            return
        if not args.wordlist:
            print("[-] To run Brute-force mode, a wordlist must be provided (e.g., --wordlist <file.txt>)")
            return
        print(f"running SubDomain Bruteforcer On The Given Domain {args.domain} With the Wordlist {args.wordlist}")
        subdomains = load_run(args.domain, args.wordlist, args.threads, args.timeout)

        if subdomains:
            if args.output:
                with open(args.output, 'a') as f:
                    f.write("\n".join(subdomains) + "\n")
            else:
                for sub in subdomains:
                    print(sub)

        else:
            print("[!] No subdomains found via brute-force.")
        return 

    # Passive mode
    domains = []

    if args.domain:
        domains.append(args.domain)
    elif args.list:
        with open(args.list, 'r') as f:
            domains = [line.strip() for line in f if line.strip()]
    else:
        print("[-] Please provide a domain (-d) or a list of domains (-ld).")
        return

    async def runner():
        await asyncio.gather(*[handle_domain(d, args) for d in domains])

    asyncio.run(runner())



if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt :
        print("Exiting gracefully.........")
