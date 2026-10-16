import json

with open("data.json") as f:
    data = json.load(f)

for name in ["Niko","Yara","Savi","Liana","Sumaq"]:
    for a in data:
        if a["name"] == name:
            a["photos"] = [p.replace(".jpg", ".png") for p in a["photos"]]
            print(f"{name}: fixed to .png")
            for p in a["photos"]:
                print(f"  {p}")

with open("data.json", "w") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)

print(f"\nTotal: {len(data)}")
