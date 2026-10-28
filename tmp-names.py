import json
d1 = json.load(open("data.json"))
d2 = json.load(open("data-roomservice.json"))
names = set(a["name"].lower() for a in d1) | set(a["name"].lower() for a in d2)
alt = ["meiling","qian","yue","xia","fei","hong","mingxia","yulan","chenyu","xinyi","zhen","wenli","ruolan","yiling","jinyu","meihua"]
for n in alt:
    print(f"{n}: {'TAKEN' if n in names else 'free'}")
