#!/usr/bin/env python3
"""Show last 10 entries from data.json for reference."""
import json

data = json.load(open("data.json"))
for e in data[-10:]:
    print(f"  name={e.get('name')}, age={e.get('age')}, origin={e.get('origin')}, city={e.get('city')}, region={e.get('region')}, tag={e.get('tag')}, flirty={e.get('flirty')}")
    print(f"    desc={e.get('desc','')[:80]}...")
    print(f"    voice={e.get('voice','')[:80]}...")
    print(f"    trait={e.get('trait','')[:80]}...")
    print(f"    photos={len(e.get('photos',[]))}")
    print()
