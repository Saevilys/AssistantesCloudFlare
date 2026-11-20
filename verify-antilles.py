#!/usr/bin/env python3
import json
with open("data.json") as f:
    data = json.load(f)
for name in ['Joëlle', 'Calista', 'Naelle', 'Malya']:
    matches = [c for c in data if c.get('name') == name]
    if matches:
        c = matches[0]
        print(f"{name}: id={c['id']}, photos={len(c.get('photos',[]))}, region={c.get('region')}, tag={c.get('tag')}, flirty={c.get('flirty')}")
        for p in c.get('photos',[]):
            print(f"  {p}")
    else:
        print(f"{name}: NOT FOUND")
print(f"Total citizens: {len(data)}")
