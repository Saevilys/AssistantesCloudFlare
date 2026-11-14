import os
names = ["yojin", "yeojin", "yejin", "dulce", "elina", "sona", "miko"]
for f in os.listdir('.'):
    for n in names:
        if n in f.lower():
            print(f)
