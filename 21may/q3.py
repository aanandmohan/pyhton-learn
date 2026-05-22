s=input("enter string ")
i=0
res=''
while i<len(s):
    j=i+1
    while s[i]==s[j] and len(s)-1:
        j+=1
    res=res+s[i]
    i+=1
print(res)


