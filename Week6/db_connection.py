import requests
import json
json.dumps({"ok": True})

response = requests.get("https://api.football-data.org/v4/status")
print(response.json())  # JSON string of list of countries


