import requests
import json

base = "https://example.com/api"  # Replace with the actual API endpoint

resp = requests.get(base , headers=headers)
print(resp.json())