st=input("enter string ")
count=0
res=" "
for i in range(0,len(st)):
    if st[i]==" ":
        count+=1
    else:
        res+=st[i]
    if count>=1:
        res+=" "
        count=0
    else:
        count=0
print(res)