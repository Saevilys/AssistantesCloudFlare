import json
data = json.load(open("data.json"))
for i, a in enumerate(data):
    if a["name"] == "Dahye":
        # print the exact raw text around the photos
        raw = open("data.json", encoding="utf-8").read()
        idx = raw.find('"Dahye"')
        # find the photos block after this
        pidx = raw.find('"photos"', idx)
        end = raw.find(']', pidx)
        print(raw[pidx:end+1])
