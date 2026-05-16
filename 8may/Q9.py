n=int(input("enter number "))

for i in range(n+1):
    print()
    j=n
    while j>i:
        print(" ",end="")
        j-=1
    k=1
    while k<=i:
        if k%2==0:
            print("0",end="")
        else:
            print("1",end="")
        
        k+=1
