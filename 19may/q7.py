st=input("enter string ")
res=''
prev=''
for i in st:
    if i.isalpha():
        if i>="A" and i<="Z":
            res=res+i.lower()
            prev=i.lower()
        else:
            res=res+i
            prev=i
    else:
        res=res+prev*(int(i)-1)
print("result is ",res)