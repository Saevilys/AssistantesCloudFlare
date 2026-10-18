import json

with open("data.json") as f:
    data = json.load(f)

for a in data:
    if a["name"] == "Sayuri":
        photos = a["photos"]
        # Find v8
        v8 = None
        for p in photos:
            if "sayuri-v8" in p:
                v8 = p
                break
        if v8:
            photos.remove(v8)
            photos.insert(0, v8)
            print("v8 déplacée en première position")
        else:
            print("v8 pas trouvée")
        print("Ordre final:")
        for p in photos:
            print(f"  {p}")
        break

with open("data.json", "w") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("data.json updated")
