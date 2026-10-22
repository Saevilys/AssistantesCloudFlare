import urllib.request, urllib.error
for n in ["zena-v1","zena-v2","zena-v3","zena-v4"]:
    u = f"https://pub-a88b6eff97bc4ebb9c2158d3a1f98b4b.r2.dev/img/zena/{n}.png"
    try:
        r = urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent":"Mozilla/5.0"}))
        print(n, r.status, r.headers.get("Content-Length"))
    except urllib.error.HTTPError as e:
        print(n, "HTTP", e.code)
