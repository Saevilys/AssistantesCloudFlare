#!/usr/bin/env python3
import json
with open('data.json') as f:
    data = json.load(f)
for i in [525, 526]:
    e = data[i]
    print(f'{i}: {e["name"]} — {e["tag"]} — {e["station"]} — photos: {len(e["photos"])}')
    for p in e["photos"]:
        print(f'  {p}')
