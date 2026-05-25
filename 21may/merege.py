s1=input('enter string 1 ')
s2=input("enter string 2 ")
res=''

for i in range(0,min(len(s1),len(s2))):
    j=i
    res+=s1[i]+s2[j]
if len(s1)<len(s2):
    res+=s2[len(s1):len(s2)]
else:
    res+=s1[len(s2):len(s1)]
print("result is ",res)