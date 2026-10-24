import json
data = json.load(open('data-roomservice.json', encoding='utf-8'))
for e in data:
    if e['name'] == 'Roksolana':
        print(json.dumps(e, indent=2, ensure_ascii=False))
        print(f"\nPhotos count: {len(e['photos'])}")
        break
else:
    print("Roksolana NOT found")
print(f"Total entries: {len(data)}")
