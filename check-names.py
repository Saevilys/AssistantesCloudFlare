import json
data = json.load(open('data.json', encoding='utf-8'))
names = sorted([e['name'] for e in data])
print(f"Total: {len(names)}")
# Check for succubus-related names
candidates = ['Lilith', 'Succubus', 'Morana', 'Eisheth', 'Naamah', 'Abyzou', 'Ardat', 'Tiamat', 'Lamashtu', 'Mara', 'Nocnitsa', 'Alukah', 'Estrie', 'Brunhild', 'Hecate', 'Carmilla', 'Mircalla', 'Succubae', 'Nyx', 'Seraphine', 'Lilis']
existing = set(names)
for c in candidates:
    if c in existing:
        print(f"  TAKEN: {c}")
    else:
        print(f"  FREE: {c}")
