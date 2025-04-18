import re

def filter_subdomains(subdomains):
    # Convert to lowercase to handle case-insensitive duplicates
    subdomains = [sub.lower() for sub in subdomains]
    
    # Remove wildcard subdomains (e.g., *.example.com)
    filtered_subdomains = [sub for sub in subdomains if not re.match(r'^\*\.', sub)]

    # Remove duplicates by converting to a set and back to a list
    return list(set(filtered_subdomains))
