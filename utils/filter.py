import re

def filter_subdomains(subdomains):
    unique_subdomains = set(subdomains)

    filtered_subdomains = [sub for sub in unique_subdomains if not re.match(r'^\*\.', sub)]

    return filtered_subdomains 