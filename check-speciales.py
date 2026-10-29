import json

with open("/data/desk/github/assistantescloudflare/data.json", encoding="utf-8") as f:
    data = json.load(f)

names = [d["name"].lower() for d in data]
check = ["rin", "ilona", "lilith", "ondine", "delta", "samara", "lyra", "mira", "nyx", "arya", "sable", "vespera", "callidora"]
for c in check:
    if c in names:
        print(f"  {c}: TAKEN")
    else:
        print(f"  {c}: free")
