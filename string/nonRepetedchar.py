s=input("eneter string ")
i=0
f=0
while i<len(s):
    count=0
    j=0
    while j<len(s):
        if s[i]==s[j]:
            count+=1
        j+=1
    if count==1:
        print("first non rep ",s[i])
        f=1
        break
    i+=1
else:
    print("no repted element ")
    
