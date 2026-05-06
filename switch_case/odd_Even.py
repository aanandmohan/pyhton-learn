n=int(input("enter age "))
match n:
    case x if x%2==0:
        print("even")
    case x:
        print("odd")
print("out of match")