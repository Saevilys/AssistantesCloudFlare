import json
data = json.load(open("data.json"))
for name in ["Sayaka", "Soyun", "Qiao"]:
    found = [e for e in data if e["name"] == name]
    if found:
        e = found[0]
        print(f"{name}: region={e['region']}, special={e['special']}, active={e['active']}, photos={len(e['photos'])}")
        for p in e["photos"]:
            print(f"  {p}")
    else:
        print(f"{name}: NOT FOUND")
print(f"Total: {len(data)}")
