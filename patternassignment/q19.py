n=int(input("enter a number "))
for i in range(1,n+1):
    for k in range(1,i+1):
        print(" ",end="")
    for l in range(1,(n-i)+1):
        print(l,end="")
    print()