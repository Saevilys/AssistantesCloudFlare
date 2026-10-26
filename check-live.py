import json
data = json.load(open('data.json', encoding='utf-8'))
names = [e['name'].lower() for e in data]
print(f"Total: {len(names)}")
for c in ['miko', 'sona', 'elina']:
    print(('TAKEN' if c in names else 'FREE'), c)
print("Last 3:", [e['name'] for e in data[-3:]])
print(json.dumps(data[-1].get('photos', {}), ensure_ascii=False))
