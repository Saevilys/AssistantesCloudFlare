import json, re, sys, collections

base = "./"
data = json.load(open(base+"data.json"))
rs = json.load(open(base+"data-roomservice.json"))

# 1. tagged entries without special:true
tagged_no_special = [(a["name"], a.get("tag")) for a in data if a.get("tag") and not a.get("special")]
print(f"data.json: {len(data)} entries")
print(f"tagged sans special:true ({len(tagged_no_special)}):")
for n,t in tagged_no_special: print(f"  - {n} [{t}]")

# 2. pick.py is_speciale
pick = None
for p in ("/code/rotation/pick.py","/github/assistantescloudflare/pick.py"):
    try:
        pick = open(p).read(); print(f"pick.py trouvé: {p}")
    except FileNotFoundError:
        pass
if pick:
    m = re.search(r"def is_speciale.*?(?=\ndef |\Z)", pick, re.S)
    print("--- is_speciale ---")
    print(m.group(0)[:800] if m else "INTRUVABLE")

# 3. duplicates data vs roomservice
names_rs = {a["name"] for a in rs}
dupes = sorted({a["name"] for a in data} & names_rs)
print(f"\ndata-roomservice.json: {len(rs)} entries")
print(f"dupes data↔roomservice ({len(dupes)}): {dupes}")

# 4. dupes inside data.json
c = collections.Counter(a["name"] for a in data)
print(f"dupes internes data.json: {[n for n,k in c.items() if k>1]}")
