k=""
def palindrom(n):
    s=str(n)
    
    if len(s)==1:
        s+=str(n)
        return s
    return s+palindrom(n//10)

t=palindrom(121)
if t==str(121):
    print("palindrom")
else:
    print("not a palindrom")