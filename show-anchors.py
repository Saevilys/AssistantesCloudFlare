#!/usr/bin/env python3
"""Show all anchor entries to understand the pattern for the new Chinese anchor."""
import json
with open('data.json') as f:
    data = json.load(f)

anchors = [e for e in data if e.get('tag') == 'anchor']
print(f"Anchors: {len(anchors)}")
for e in anchors:
    print(f"\n{e['name']} — {e.get('origin','?')} — {e.get('city','?')}")
    print(f"  age={e.get('age','?')} flirty={e.get('flirty',0)}")
    print(f"  photos={len(e.get('photos',[]))}")
    if e.get('photos'):
        print(f"  first: {e['photos'][0]}")
