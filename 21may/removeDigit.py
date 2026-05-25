'''s=input("eneter stirng ")
res=""
for ch in s:
    if ch>='0' and ch<='9':
        pass
    else:
        res+=ch
print("digit is ",res)'''
#extract only digit 
s=input("eneter stirng ")
res=""
for ch in s:
    if ch>='0' and ch<='9':
        res+=ch
    
print("digit is ",res)
