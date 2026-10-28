import urllib.request, json
# Vérifier les URLs R2 directement
urls = [
    "https://pub-a88b6eff97bc4ebb9c2158d3a1f98b4b.r2.dev/img/sayaka/sayaka-v1.png",
    "https://pub-a88b6eff97bc4ebb9c2158d3a1f98b4b.r2.dev/img/soyun/soyun-v1.png",
    "https://pub-a88b6eff97bc4ebb9c2158d3a1f98b4b.r2.dev/img/qiao/qiao-v1.png",
]
for u in urls:
    try:
        req = urllib.request.Request(u, method="HEAD")
        r = urllib.request.urlopen(req, timeout=10)
        print(f"OK {r.status} — {u.split('/')[-1]}")
    except Exception as e:
        print(f"FAIL — {u} — {e}")
