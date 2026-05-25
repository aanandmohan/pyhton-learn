s=input("enter string ")
tar=input("enter string ")
words=s.split()
res=""
for i in words:
    if i!=tar:
        res+=i+" "
print(res)
