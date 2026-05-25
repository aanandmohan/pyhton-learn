s=input("enter string ")
i=0
res=""
while i<len(s):
    ch=s[i]
    j=i+1
    while j<len(s) and ch ==s[j]:
        j+=1
    res+=ch
    i=j
print(res)