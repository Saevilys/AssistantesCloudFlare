import json, sys

with open("/data/desk/github/assistantescloudflare/data.json", encoding="utf-8") as f:
    data = json.load(f)

print(f"Total: {len(data)}")
print()
for d in data:
    name = d.get("name", "?")
    tag = d.get("tag", "")
    flirty = d.get("flirty", "")
    print(f"  {name}  tag={tag}  flirty={flirty}")
