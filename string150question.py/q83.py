s=input("enter string ")
words=s.split()
res=""
for i in words:
    t=int(i)
    res+=chr(t)
print(res)