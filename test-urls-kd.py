import urllib.request, urllib.error
# Test with GET instead of HEAD, and try another known-working URL
urls = [
 "https://pub-a88b6eff97bc4ebb9c2158d3a1f98b4b.r2.dev/img/kenza/kenza-souk.png",
 "https://pub-a88b6eff97bc4ebb9c2158d3a1f98b4b.r2.dev/img/senna/senna-v1.png",
 "https://pub-a88b6eff97bc4ebb9c2158d3a1f98b4b.r2.dev/img/iliana/iliana-v1.png",
]
for u in urls:
    try:
        r = urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent":"Mozilla/5.0"}))
        print(u.split("/")[-1], r.status, r.headers.get("Content-Type"), r.headers.get("Content-Length"))
    except urllib.error.HTTPError as e:
        print(u.split("/")[-1], "HTTP", e.code, e.reason)
    except Exception as e:
        print(u.split("/")[-1], "ERR", e)
