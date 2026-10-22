raw = open("data.json").read()
for needle in ["kenza-souk", "diya-cafe"]:
    i = raw.find(needle)
    print(repr(raw[i-260:i+320]))
    print("---")
