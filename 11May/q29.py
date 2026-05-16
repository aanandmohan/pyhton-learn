n=int(input("enter n "))
k=1
for i in range(1,n+1):
    print()
    for j in range(1,n+1):
        if i==j:
            print(k,end="")
            k+=1
        else:
            print("-",end="")