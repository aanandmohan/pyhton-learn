n=int(input("enter number "))

i=1
while i<=n:
    print()
    j=n-1
    while j>=i:
        print(" ",end="")
        j-=1
    k=1
    while k<=i:
        print(k,end="")
        k+=1
    i+=1    

