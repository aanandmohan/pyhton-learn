s=input("enter string ")
l=[]
for i in range(len(s)):
    j=i+1
    while j<=len(s):
        print(s[i:j])
        l.append(s[i:j])

        j+=1
print(l)
t="a"
for i in l:
    ch=i
    re=ch[::-1]
    if re==ch:
        if len(re)>len(t):
            t=re

print(t)