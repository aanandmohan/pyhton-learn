number=input("enter vehical number ")
if len(number)<10:
    print("invalid number")
else:
    k=number[0:2]

    if k.isalpha():
        t=number[2:4]
        if t.isdigit():
            print("valid number")
        
        else:
            print("invalid number ")
               
    else:
        print("invalid number ")

