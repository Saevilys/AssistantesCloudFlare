#!/usr/bin/env python3
import json

with open('data.json', encoding='utf-8') as f:
    data = json.load(f)

BASE = "https://pub-a88b6eff97bc4ebb9c2158d3a1f98b4b.r2.dev"
PREFIX = "img/seolhwa"

new_photos = [
    f"{BASE}/{PREFIX}/seolhwa-divine-lanternes.png",
    f"{BASE}/{PREFIX}/seolhwa-divine-escalier.png",
    f"{BASE}/{PREFIX}/seolhwa-divine-spot.png",
    f"{BASE}/{PREFIX}/seolhwa-divine-lanternes-2.png",
    f"{BASE}/{PREFIX}/seolhwa-divine-lanternes-3.png",
    f"{BASE}/{PREFIX}/seolhwa-divine-lanternes-4.png",
    f"{BASE}/{PREFIX}/seolhwa-divine-kpop.png",
    f"{BASE}/{PREFIX}/seolhwa-divine-kpop-2.png",
    f"{BASE}/{PREFIX}/seolhwa-divine-kpop-3.png",
]

idle_url = f"{BASE}/{PREFIX}/seolhwa-idle.mp4"

found = False
for e in data:
    if e['name'] == 'Seolhwa':
        e['photos'] = new_photos
        e['idle'] = idle_url
        found = True
        print(f"Updated Seolhwa: {len(new_photos)} photos + idle")
        break

if not found:
    print("ERROR: Seolhwa not found")
    exit(1)

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write('\n')

print("data.json saved")
