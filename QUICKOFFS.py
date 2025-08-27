import requests
import json
print(json.dumps({"ok": True}))



# Fetch and extract fields
resp = requests.get("https://api.football-data.org")
data=resp.json()
print(data)




