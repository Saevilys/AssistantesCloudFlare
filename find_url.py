import json, re
d = json.load(open("data.json"))
txt = json.dumps(d)[:3000]
urls = set(re.findall(r'https://[^"]+', txt))
print(urls)
