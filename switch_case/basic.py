a=int(input("enter first number "))
b=int(input("entr second number "))
op=input("enter operator (+,-,*,/)")

match op:
    case"+":
        print("Result ",a+b)
    case"-":
        print("result is ",abs(a-b))
    case"*":
        print("result is ",a*b)
    case"/":
        if b!=0:
            print("result is ",(a/b))
        else:
            print("avoid code ")
   

print("out of match")

