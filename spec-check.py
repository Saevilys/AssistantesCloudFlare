h=open("specials.html").read()
i=h.find("@keyframes glowAnomalie")
print(repr(h[i:i+200]))
