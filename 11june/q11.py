s=["mobile","zaptop","mobile","tablet","zaptop","mobile","zaptop","zaptop"]
d={}
for x in s:
    d[x]=d.get(x,0)+1
print(d)

for x in sorted(d.keys()):
    print(f"{x}:{d[x]}")

for k,v in d.items():
    if v>3:
        print(k,":",v)


max=max(d,key=d.get)
print(max,"the value is",d[max])
'''t=sorted(d)
print(d.values())
print(t)'''