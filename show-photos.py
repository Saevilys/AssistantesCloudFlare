import json

with open("data.json") as f:
    data = json.load(f)

for name in ["Kiana","Miral","Daria"]:
    a = next(x for x in data if x["name"] == name)
    p = a["photos"]
    print(f"\n{name}:")
    for i,u in enumerate(p):
        print(f"  [{i}] {u}")
