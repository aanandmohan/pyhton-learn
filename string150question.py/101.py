s="((())))(()"
r=" "
for i in s:
    if i=="(":
        r+=i
    elif i==")":
        if len(r)==0:
            print("not valid ")
            break
    r=r[:-1]
else:
    print("vlid")
    