s=input("enter string ")
l=[]
for ch in s:
    if ch not in l:
        l.append(ch)
    else:
        l.remove(ch)
print("".join(l))