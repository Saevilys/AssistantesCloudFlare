import json

with open('data.json', encoding='utf-8') as f:
    data = json.load(f)

names = [e['name'] for e in data] if isinstance(data, list) else None
if names is None:
    print(type(data), list(data)[:5])
else:
    print(len(names))
    hits = [i for i, n in enumerate(names) if 'ruoxi' in n.lower()]
    print('ruoxi at:', hits)
