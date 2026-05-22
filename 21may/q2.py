s=input("enter string ")
ch=s[0]
i=0
res=""
while i<len(s):
    j=i+1
    while s[j]==ch:
        j+=1

    res+=ch
    ch=s[j]
    i+=j
print(res)


