import requests, json, time, os
from datetime import datetime

# Human token - use yours
TOKEN = os.getenv("GH_TOKEN")
HEADERS = {"Authorization": f"token {TOKEN}", "User-Agent": "k8s-researcher-vijayawada"}

QUERIES = [
    "repo:kubernetes/kubernetes OOMKilled in:issues is:closed",
    "repo:kubernetes-sigs/karpenter FailedScheduling in:issues",
    "repo:aws/karpenter-provider-aws scale down stuck"
]

all_issues = []
for q in QUERIES:
    r = requests.get(f"https://api.github.com/search/issues?q={q}&per_page=20", headers=HEADERS)
    data = r.json()
    for it in data.get("items", [])[:17]: # total 50+
        all_issues.append({
            "id": it["id"],
            "url": it["html_url"],
            "title": it["title"],
            "body": it["body"][:2000],
            "closed_at": it["closed_at"],
            "type": "OOMKilled" if "OOM" in it["title"] else "Karpenter",
            "logs": "N/A - see thread", # real logs extracted manually for quality
            "human_fix_time_hours": round((datetime.fromisoformat(it["closed_at"][:-1]) - datetime.fromisoformat(it["created_at"][:-1])).total_seconds()/3600, 2) if it["closed_at"] else 4
        })
    time.sleep(2) # avoid rate limit - human behavior

with open("data/raw_issues/k8s_50.json", "w") as f:
    json.dump(all_issues[:50], f, indent=2)
print(f"Mined {len(all_issues[:50])} issues")
