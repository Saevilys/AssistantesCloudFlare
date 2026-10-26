import json
data = json.load(open('data.json', encoding='utf-8'))
names = set(e['name'].lower() for e in data)
for c in ['xiomara', 'rosalia', 'rosario', 'camila', 'dayana', 'nadia', 'zola', 'amara']:
    print(('TAKEN' if c in names else 'FREE'), c)
