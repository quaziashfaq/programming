#!/usr/bin/env python3

import requests
import pprint

url = 'https://api.github.com/search/repositories'
url += '?q=language:python+sort:stars+stars:>10000'

headers = {
        'Accept': 'application/vnd.github.v3+json'
        }
raw_response = requests.get(url, headers = headers)
print(f'Status code: {raw_response.status_code}')

response_dict = raw_response.json()

print(response_dict.keys())

print(f"Count: {response_dict['total_count']}")
print(f"Complete Result: {not response_dict['incomplete_results']}")

repo_dicts = response_dict['items']
print(f"Number of repo_dicts: {len(repo_dicts)}")
repo_dict = repo_dicts[0]
#print(repo_dict)

pp = pprint.PrettyPrinter(indent = 4)
pp.pprint(repo_dict)

print(f"Keys: {len(repo_dict)}")
#print(sorted(repo_dict.keys()))

print("\nSelected information:")
for repo_dict in repo_dicts:
    print(f"Name: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Created: {repo_dict['created_at']}")
    print(f"Updated: {repo_dict['updated_at']}")
    print(f"Description: {repo_dict['description']}")
