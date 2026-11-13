#!/usr/bin/env python3
import json
with open('data.json') as f:
    data = json.load(f)
# Show entries 522, 523, 524 fully
for i in [522, 523, 524]:
    print(f'--- {i} ---')
    print(json.dumps(data[i], ensure_ascii=False, indent=2))
