import re
lines = open("data.json", encoding="utf-8").read().split("\n")
for i, l in enumerate(lines):
    if "ruka-v1.png" in l or "ruka-v4.png" in l:
        print(i, repr(l))
