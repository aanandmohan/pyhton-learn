s=input("enter string ")
r=''
h=''
for i in range (len(s)):
    if s[i] not in r :
        r=r+s[i]
    else :
        if len(r)>len(h):
            h=r
            r=r[r.index(s[i])+1:]+s[i]

if len(r)>len(h):
    print(r)

else :
    print(h)                