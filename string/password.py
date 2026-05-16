'''paassword=input("enter a password ")
digit=0
lower=0
upper=0
space=0
special=0
i=0
while i<len(paassword):
    
    ch=paassword[0]
    if ch>='a' and ch<='z':
        lower=1
    elif ch>='A' and ch<='Z':
        upper=1
    elif ch>='0' and ch<='9':
        digit=1
    elif ch==" ":
        space=1
    else:
        special=1

    i+=1
if upper==1 and lower==1 and digit==1 and space==0 and special==1:
    print("valid password")
else:
    print("invalid ")

'''

upper=0
lower=0
digit=0
space=0
special=0

password=input("enter paswword ")
i=0
while i<len(password):
    ch=password[i]
    if ch.isupper():
        upper=1
    elif ch.islower():
        lower=1
    elif ch.isdigit():
        digit=1
    elif ch.isspace():
        space=1
    else:
        special=1
    i+=1
if upper==1 and digit==1 and lower==1 and space==0 and special==1:
    print("valid ")
else:
    print("invalid ")