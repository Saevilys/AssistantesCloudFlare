import json
data = json.load(open('data.json', encoding='utf-8'))
names = set(e['name'].lower() for e in data)
print(f"Total: {len(names)}")
for c in ['ximena', 'yejin', 'amara', 'valentina', 'soo-ah', 'minji', 'fatou', 'zola', 'chioma', 'renata', 'nadia']:
    print(('TAKEN' if c in names else 'FREE'), c)
