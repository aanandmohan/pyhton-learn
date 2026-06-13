word=["ram","sita","kalu","oye","virat","vishn","a","b"]
c={}
for x in word:
    l=len(x)
    if l not in c:
        c[l]=[]
    c[l].append(x)
print(c)
