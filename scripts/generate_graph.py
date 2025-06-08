import os
import requests

API_KEY = os.environ.get("WAKATIME_API_KEY")
if not API_KEY:
    print("❌ WAKATIME_API_KEY not found in environment")
    exit(1)

url = "https://wakatime.com/api/v1/users/current/stats/last_7_days"
headers = {"Authorization": f"Bearer {API_KEY}"}
res = requests.get(url, headers=headers)
data = res.json()

if "data" not in data:
    print("❌ Error from WakaTime API:", data)
    exit(1)

languages = data["data"]["languages"][:5]  
bar_unit = 2  
max_hours = max(lang["total_seconds"] / 3600 for lang in languages)

# Generate bar lines
graph_lines = ["WakaTime Weekly Coding Hours\n"]
for y in range(int(max_hours)+1, -1, -2):
    line = f"{y:>4}h ┤"
    for lang in languages:
        hours = lang["total_seconds"] / 3600
        block = "█" * 20 if hours >= y else " " * 20
        line += f" {block}"
    graph_lines.append(line)

footer = "    ┼" + "─" * (22 * len(languages))
labels = ""
for lang in languages:
    hours = int(lang["total_seconds"] // 3600)
    mins = int((lang["total_seconds"] % 3600) // 60)
    labels += f"  {lang['name']} ({hours}h {mins}m)\n"

graph_lines.append(footer)
graph_lines.append(labels)

final_output = "\n".join(graph_lines)
print(final_output)

with open("waka_graph_vertical.md", "w") as f:
    f.write("```\n" + final_output + "\n```\n")
