s=["pizza","burger","pizza","nod","pizza"]
d={}
for x in s:
    d[x]=d.get(x,0)+1

for k,v in d.items():
    print(f"{k}:{v}")

max=max(d,key=d.get)
print(max)
print(d[max])