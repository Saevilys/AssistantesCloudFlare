import urllib.request, json
url = "https://raw.githubusercontent.com/Saevilys/AssistantesCloudFlare/nemini/data.json"
with urllib.request.urlopen(url) as r:
    data = json.load(r)
print(f"Total: {len(data)}")
print(f"Last 5: {[c['name'] for c in data[-5:]]}")
for name in ["Aimi","Ploi","Lan"]:
    found = [c for c in data if c.get("name") == name]
    if found:
        c = found[0]
        print(f"  {name}: id={c['id']}, photos={len(c.get('photos',[]))}")
    else:
        print(f"  {name}: MISSING")
