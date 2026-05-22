s=input("enter string ")
res=''
for ch in s:
    if ch>='a' and ch<='z':
        res+=ch
    elif ch>="A" and ch<="Z":
        res+=ch
    elif ch>="0" and ch<="9":
        res+=ch
    
s=res
print("output is ",s)
