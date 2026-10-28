import json

raw = open("data.json", encoding="utf-8").read()

targets = ["Kirie","Meilin","Salma","Linh","Yumi","Lanfen","Tsukiko","Naïma","Miku","Nabi",
           "Yulia","Beatriz","Xihe","Yae","Hotaru","Reika","Zoraida","Sherine","Lilith","Keilani",
           "Sayuri","Yomi","Soline","Berenice","Zari","Eisheth","Alukah","Nyx",
           "Nova","Echo","Ember","Sayaka","Soyun","Qiao"]

for name in targets:
    i = raw.find(f'"name": "{name}"')
    j = raw.find('"flirty"', i)
    k = raw.find("\n", j)
    snippet = raw[i:k]
    # compress intermediate lines for readability check
    print(f"=== {name} ===")
    print(snippet)
    print()
