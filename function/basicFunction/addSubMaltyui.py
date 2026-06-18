while True:
    print(" 1the sum")
    print("2 the subtraction ")
    print("3 multipilciton ")
    choice=int(input("enter choice "))
    def sum(a,b):
        c=a+b
        return c
    def sub(a,b):
        return b-a
    def mul(a,b):
        return a*b
    match choice:
        case 1:
            a=int(input("enter first number "))
            b=int(input("enetr second number "))
            print("the sum is ",sum(a,b))
        case 2:
            a=int(input("enter first number "))
            b=int(input("enetr second number "))
            print("the subtartion is  is ",sub(a,b))
        case 3:
            a=int(input("enter first number "))
            b=int(input("enetr second number "))
            print("the multipliction is ",mul(a,b))
