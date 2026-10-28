import json

raw = open("data.json", encoding="utf-8").read()
data = json.loads(raw)

# Vérifier qu'aucune entrée avec tag n'a encore flirty
tagged = [d for d in data if "tag" in d]
print(f"Entrées avec tag: {len(tagged)}")
for d in tagged:
    if "flirty" in d:
        print(f"  PROBLÈME: {d['name']} a encore flirty={d['flirty']}")

# Vérifier qu'il n'y a plus de flirty >= 5
high = [d for d in data if d.get("flirty", 0) >= 5]
print(f"\nEncore flirty >= 5: {len(high)}")
for d in high:
    print(f"  {d['name']} flirty={d['flirty']}")

# Compter par tag
from collections import Counter
tags = Counter(d.get("tag") for d in tagged)
print(f"\nRépartition tags: {dict(tags)}")

# Vérifier que les androïdes ont bien region Androides + tag androide
androids = [d for d in data if d.get("region") == "Androides"]
print(f"\nAndroides: {len(androids)}")
for d in androids:
    print(f"  {d['name']} tag={d.get('tag')} region={d.get('region')}")
