short=input("enter string ")
res=short[0]
for i in range(1,len(short)-1):
    if short[i]==" ":
        res+=short[i+1]
print(res)
