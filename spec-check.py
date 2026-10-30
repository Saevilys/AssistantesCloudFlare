h=open("specials.html").read()
# Check tagGlow for kungfupunk
i=h.find("tagGlow")
while i!=-1:
    ctx=h[max(0,i-50):i+200]
    if "kungfu" in ctx.lower():
        print("FOUND kungfu in tagGlow:",repr(ctx))
        break
    i=h.find("tagGlow",i+1)
if i==-1:
    print("tagGlow with kungfu: NOT FOUND")
    # Show tagGlow context
    i=h.find("tagGlow")
    print(repr(h[i:i+300]))
