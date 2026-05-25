s=input("enter string ")
res=''
for i in range(0,len(s)):
    if s[i]!="&":
        ch=s[i]
        j=i+1
        
        while j<len(s):
            if s[j]==ch:
                ch="&"
                res+=ch
            j+=1
    else:
        i+=1
print("result is ",res)