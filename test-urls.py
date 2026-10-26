import urllib.request
for u in ["https://pub-a88b6eff97bc4ebb9c2158d3a1f98b4b.r2.dev/img/nesrin/nesrin-nesrin-v1.png",
          "https://pub-a88b6eff97bc4ebb9c2158d3a1f98b4b.r2.dev/img/miko/miko-v1.png"]:
    try:
        r = urllib.request.urlopen(u, timeout=15)
        print(r.status, len(r.read()), u)
    except Exception as e:
        print("FAIL", u, e)
