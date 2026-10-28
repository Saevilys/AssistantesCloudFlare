import json
data = json.load(open("data.json"))
rs = json.load(open("data-roomservice.json"))
print("roster:", len(data))
for a in data + rs:
    if a["name"].lower() in ("dahye", "carmen"):
        print(json.dumps(a, ensure_ascii=False, indent=1)[:900])
