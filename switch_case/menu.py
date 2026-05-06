
while True:
    print("MENU")
    print("1 ADD two number ")
    print("2 check even or  oddd")
    print("3 find square ")
    print("4 exit ")
    choice=int(input("enter the choice "))
    match choice:
        case 1:
            a=int("enter first numbr ")
            b=int("enter second number ")
            print("result is ",a+b)
        case 2:
            a=int(input("enter number"))
            if a%2==0:
                print("even numbr ")
            else:
                print("odd number")
        case 3:
            a=int(input("enter a number "))
            print("square of given number is ",a*a)
        case 4:
            print("Exist")
            break