h=open("specials.html").read()
print("badge-anomalie:", "badge-anomalie" in h)
print("glowAnomalie:", "glowAnomalie" in h)
# check raw with cache-busting
import urllib.request
url="https://raw.githubusercontent.com/Saevilys/AssistantesCloudFlare/nemini/specials.html?t="+str(len(h))
r=urllib.request.urlopen(urllib.request.Request(url,headers={"User-Agent":"Mozilla/5.0","Cache-Control":"no-cache"}))
raw=r.read().decode()
print("raw badge-anomalie:", "badge-anomalie" in raw)
print("raw glowAnomalie:", "glowAnomalie" in raw)
print("raw len:", len(raw), "local len:", len(h))
