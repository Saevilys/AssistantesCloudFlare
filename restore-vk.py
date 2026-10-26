#!/usr/bin/env python3
"""Restore the 6 virgin killer assistants (Miko, Sona, Elina, Dulce, Yejin, Fatou)
from commit e56736f into current data.json."""
import json

# Read current data.json (279, missing VK)
with open("data.json", encoding="utf-8") as f:
    current = json.load(f)

current_names = {e["name"].lower() for e in current}
print(f"Current count: {len(current)}")

# The 6 VK assistants with their full data
vk_assistants = [
    {
        "name": "Miko",
        "age": 22,
        "origin": "Japon",
        "city": "Tokyo",
        "region": "Asie",
        "active": True,
        "flirty": 4,
        "desc": "",
        "voice": "",
        "trait": "",
        "photos": []
    },
    {
        "name": "Sona",
        "age": 23,
        "origin": "Azerbaïdjan",
        "city": "Bakou",
        "region": "Asie",
        "active": True,
        "flirty": 4,
        "desc": "",
        "voice": "",
        "trait": "",
        "photos": []
    },
    {
        "name": "Elina",
        "age": 24,
        "origin": "Finlande",
        "city": "Helsinki",
        "region": "Europe",
        "active": True,
        "flirty": 4,
        "desc": "",
        "voice": "",
        "trait": "",
        "photos": []
    },
    {
        "name": "Dulce",
        "age": 23,
        "origin": "Mexique",
        "city": "Guadalajara",
        "region": "Latines",
        "active": True,
        "flirty": 4,
        "desc": "",
        "voice": "",
        "trait": "",
        "photos": []
    },
    {
        "name": "Yejin",
        "age": 23,
        "origin": "Corée du Sud",
        "city": "Séoul",
        "region": "Asie",
        "active": True,
        "flirty": 4,
        "desc": "",
        "voice": "",
        "trait": "",
        "photos": []
    },
    {
        "name": "Fatou",
        "age": 24,
        "origin": "Sénégal",
        "city": "Dakar",
        "region": "Afrique",
        "active": True,
        "flirty": 4,
        "desc": "",
        "voice": "",
        "trait": "",
        "photos": []
    }
]

# I need the actual full data from the e56736f commit
# Let me fetch it
import urllib.request

url = "https://raw.githubusercontent.com/Saevilys/AssistantesCloudFlare/e56736f/data.json"
with urllib.request.urlopen(url) as r:
    old_data = json.loads(r.read().decode("utf-8"))

print(f"Old count (e56736f): {len(old_data)}")

vk_names = {"miko", "sona", "elina", "dulce", "yejin", "fatou"}
restored = []
for entry in old_data:
    if entry["name"].lower() in vk_names:
        restored.append(entry)
        print(f"  Found: {entry['name']} — {len(entry.get('photos', []))} photos")

# Add them back
current.extend(restored)
print(f"\nNew count: {len(current)}")

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(current, f, ensure_ascii=False, indent=2)
print("Saved.")
