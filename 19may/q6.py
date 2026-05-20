s=input("enter student id no. ")
ch=""
digit=""
res=''
for i in range(0,len(s)):
    if s[i]>='a' and s[i]<='z':
        ch+=s[i]
    elif s[i]>='0' and s[i]<='9':
        digit+=s[i]

for i in sorted(ch):
    res+=i
for i in sorted(digit):
    res+=i
print(res)
