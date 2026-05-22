s=input("enter string ")
i=0
while i<len(s):
    j=0
    count=0
    while j<len(s):
        if s[i]==s[j]:
            count+=1
        j+=1
    if count==1:
        print("the first non repted charter is ",s[i])
        break
    i+=1

