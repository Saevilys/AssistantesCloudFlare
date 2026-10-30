h=open("specials.html").read()
i=h.find("flirtDots=")
print(repr(h[i:i+1200]))
