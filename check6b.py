#!/usr/bin/env python3
import json
with open("data.json", encoding="utf-8") as f:
    data = json.load(f)
names = {e["name"].lower() for e in data}
for n in ["Rasha","Kiko","Maysa","Nori","Rima","Kairi"]:
    print(f"{n}: {'TAKEN' if n.lower() in names else 'OK'}")
