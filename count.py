#!/usr/bin/env python3
import json
with open("data.json") as f:
    data = json.load(f)
print(f"Total: {len(data)}")
print(f"Dernière: {data[-1]['name']}")
names = [a["name"] for a in data]
if "Valeria" in names:
    print("Valeria EXISTE DEJA")
else:
    print("Valeria absente")
if "Adaeze" in names:
    print("Adaeze EXISTE DEJA")
else:
    print("Adaeze absente")
