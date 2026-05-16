n=int(input("enter n "))
for i in range(n):
    print()
    for j in range(i):
        print(" ",end="")
    for k in range(n):
        print("*",end="")