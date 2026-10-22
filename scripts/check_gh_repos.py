import urllib.request
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

url = 'https://api.github.com/users/Kyumunhwang/repos?per_page=100'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as resp:
        repos = json.loads(resp.read().decode('utf-8'))
        print(f"Total repos: {len(repos)}")
        for r in repos:
            print(f"- {r['name']}: {r.get('description')} | {r['html_url']}")
except Exception as e:
    print('Error:', e)
