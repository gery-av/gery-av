import requests
import matplotlib.pyplot as plt
from datetime import datetime
import os

api_key = os.getenv("WAKATIME_API_KEY")

headers = {
    "Authorization": f"Basic {api_key.encode('utf-8').hex()}",
}
params = {
    "range": "last_7_days"
}
response = requests.get(
    "https://wakatime.com/api/v1/users/current/stats",
    headers={"Authorization": f"Bearer {api_key}"},
    params=params
)

data = response.json()
languages = data["data"]["languages"]

labels = [lang["name"] for lang in languages]
minutes = [lang["total_seconds"] / 60 for lang in languages]

plt.figure(figsize=(10, 6))
plt.plot(labels, minutes, marker='o')
plt.title("Coding Time per Language (Last 7 Days)")
plt.xlabel("Language")
plt.ylabel("Minutes")
plt.grid(True)
plt.tight_layout()
plt.savefig("waka_graph.png")
