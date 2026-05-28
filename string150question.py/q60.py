s1=input("enter string ")
s2=input("enter string ")
res=s1[0]
r=0
'''for i in range(1,len(s1)+len(s2)):
    if i<len(s1):
        if s1[i]!=res[r]:
            res+=s1[i]
            r+=1
    else:
        if s2[i]!=res[r]:
            res+=s1[i]
            r+=1
print(res)'''


for i in range(1,len(s1)):
    if s1[i]!=res[r]:
            res+=s1[i]
            r+=1
for i in range(0,len(s2)):
     if s2[i]!=res[r]:
            res+=s2[i]
            r+=1
print(res)