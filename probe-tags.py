import json, re

raw = open("data.json", encoding="utf-8").read()
data = json.loads(raw)

targets = [d for d in data if d.get("flirty", 0) >= 5 or d.get("region") == "Androides"]
print(len(targets), "cibles")
for d in targets:
    print(d["name"], "| flirty:", d.get("flirty"), "| region:", d.get("region"), "| special:", d.get("special"))

# Raw text blocks: find each name's position and show surrounding raw lines
print("\n--- raw sample (Salma) ---")
i = raw.find('"name": "Salma"')
print(raw[i-200:i+900])
