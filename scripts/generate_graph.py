import requests
import os
import sys

API_KEY = os.environ.get("WAKATIME_API_KEY")

if not API_KEY:
    print("❌ WAKATIME_API_KEY is not set")
    sys.exit(1)

headers = {
    "Authorization": f"Bearer {API_KEY}"
}
url = "https://wakatime.com/api/v1/users/current/stats/last_7_days"

response = requests.get(url, headers=headers)
data = response.json()

if "data" not in data or "languages" not in data["data"]:
    print("❌ Invalid response from WakaTime API")
    print(data)
    sys.exit(1)

languages = data["data"]["languages"]

for lang in languages:
    print(f"{lang['name']}: {lang['text']} ({lang['percent']}%)")
