import json, random

with open("/data/desk/github/assistantescloudflare/data.json", encoding="utf-8") as f:
    data = json.load(f)

# Filtrer les actives avec photos
actives = [d for d in data if d.get("active", True) and d.get("photos")]

pick = random.choice(actives)
print(f"Name: {pick['name']}")
print(f"Age: {pick.get('age', '?')}")
print(f"Origin: {pick.get('origin', '?')}")
print(f"City: {pick.get('city', '?')}")
print(f"Region: {pick.get('region', '?')}")
print(f"Tag: {pick.get('tag', '')}")
print(f"Flirty: {pick.get('flirty', '')}")
print(f"Desc: {pick.get('desc', '')[:200]}")
print(f"Photos: {len(pick.get('photos', []))}")
print(f"First photo: {pick.get('photos', [''])[0]}")
