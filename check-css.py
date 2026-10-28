import re
raw = open("specials.html", encoding="utf-8").read()
for cls in [".flirt-lvl5", ".flirt-lvl6", ".flirt-androide", ".android-tag"]:
    m = re.search(re.escape(cls) + r"[^{]*\{([^}]+)\}", raw)
    if m:
        print(f"\n{cls} {{ {m.group(1)} }}")
    else:
        print(f"\n{cls}: NOT FOUND")
