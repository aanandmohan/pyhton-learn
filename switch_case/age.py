age=int(input("enter age "))
match age:
    case x if x<13:
        print("child")
    case x if x<20:
        print("teen")
    case x if x<50:
        print("adult")
print("out of match ")