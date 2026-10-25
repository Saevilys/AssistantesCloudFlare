import json
with open('data.json') as f:
    data = json.load(f)
names = [d['name'] for d in data]
for n in ['Jiyeon','Soomin','Hayoon','Eunji','Ryunhee','Jisun','Xueli','Meilin','Yan','Lin','Ksenia','Mika','Zara','Sujin','Yuna','Hyejin','Chaerin','Danbi','Sujin','Kyunghee','Miran','Sohee','Jiae','Wenjin','Liwei','Xinyi']:
    print(f"{n}: {'TAKEN' if n in names else 'FREE'}")
print(f"Total: {len(names)}")
