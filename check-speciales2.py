import json

with open("/data/desk/github/assistantescloudflare/data.json", encoding="utf-8") as f:
    data = json.load(f)

names = [d["name"].lower() for d in data]
check = ["lyra", "sable", "arya", "callidora", "tiamat", "ishtari", "astarte", "inanna", "qadita", "azra", "lilis", "namah", "sukuna", "mara"]
for c in check:
    if c in names:
        print(f"  {c}: TAKEN")
    else:
        print(f"  {c}: free")
