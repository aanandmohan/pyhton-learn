n=int(input("enter n "))
for i in range(1,n):
    for k in range(1,n-i):
        print(" ",end="")
    for l in range(1,i):
        
        print(l,end="")
        
    print()