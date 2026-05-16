n=int(input("enter a number "))
t=1
for i in range(1,n+1):
    print()
    for j in range(n-i):
        print(" ",end="")

    for k in range(((2*i)-1)):
        print(t,end="")
        t+=1


