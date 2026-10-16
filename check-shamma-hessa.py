#!/usr/bin/env python3
import json

with open("data.json", encoding="utf-8") as f:
    data = json.load(f)

print("Total:", len(data))
for name in ("Shamma", "Hessa"):
    hits = [x for x in data if x["name"] == name]
    for x in hits:
        print(name, "OK — flirty =", x["flirty"], "|", x["origin"], "|", x["city"], "|", len(x.get("photos", [])), "photos")
    if not hits:
        print(name, "ABSENT ⚠️")
