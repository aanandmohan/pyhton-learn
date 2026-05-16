n=int(input("ente number "))

for i in range(n+1):
    print()
    for j in range(n-i):
        print(" ",end="")

    for k in range(((2*i)-1)):
        t=0
        if k==0 or k==(2*i):
            t+=1
            print("*",end="")
        else:
            print(" ",end='')

        
