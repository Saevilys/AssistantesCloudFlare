import json
data = json.load(open('data-roomservice.json', encoding='utf-8'))
for e in data:
    if e['name'] == 'Roksolana':
        print(f"Photos: {len(e['photos'])}")
        for p in e['photos']:
            print(f"  {p}")
        break
else:
    print("NOT FOUND")
print(f"Total entries: {len(data)}")
