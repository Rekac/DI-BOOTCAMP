import requests
import json
print(json.dumps({"ok": True}))
from collections import defaultdict

# Your API token
headers = {"X-Auth-Token": "YOUR_TOKEN"}

# List of sample endpoints to explore
endpoints = [
    "/v4/areas/2267",
    "/v4/competitions",
    "/v4/competitions/PL/teams",
    "/v4/persons/44",
    "/v4/players/44/matches"
]

base = "https://api.football-data.org"

# Dictionary to accumulate field paths per endpoint
fields_by_endpoint = defaultdict(set)

def extract_fields(obj, prefix="", field_set=None):
    if field_set is None:
        return
    if isinstance(obj, dict):
        for k, v in obj.items():
            path = f"{prefix}.{k}" if prefix else k
            field_set.add(path)
            extract_fields(v, path, field_set)
    elif isinstance(obj, list):
        for i, item in enumerate(obj):
            extract_fields(item, prefix, field_set)

# Fetch and extract fields
for ep in endpoints:
    resp = requests.get(base + ep, headers=headers)
    if resp.ok:
        data = resp.json()
        fe = set()
        extract_fields(data, "", fe)
        fields_by_endpoint[ep] = fe
    else:
        print(f"Failed to fetch {ep}: {resp.status_code}")

# Output the fields per endpoint
for ep, fields in fields_by_endpoint.items():
    print(f"\nEndpoint: {ep}")
    for f in sorted(fields):
        print(f"  {f}")

