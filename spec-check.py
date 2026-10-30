import re
h=open("specials.html").read()
# Trouver le badge démone et sa fin (le :'' qui suit)
i=h.find("a.tag==='démone'?'<span class=\"profile-badge flirt-demone\"")
# Chercher le prochain :'' ou :''} après
ctx=h[i:i+600]
print(repr(ctx))
