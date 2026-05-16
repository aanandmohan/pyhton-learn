n=int(input("enter number "))

l=1
for i in range(1,n+1):
    print()
    for j in range(n-i):
        print("-",end="")
    t=i
    for k in range(i):
        print(t,end="")
        t+=1
        

