s=input("enter string ")

aplha=0
digit=0
spe=0
for ch in s:
    
    if ch.lower()>='a' and ch.lower()<='z':
        aplha+=1
    elif ch>="0" and ch<="9":
        digit+=1
    else:
        spe+=1
print("alphabet ",aplha,"digit ",digit,"special",spe)