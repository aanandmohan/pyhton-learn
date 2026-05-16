n=int(input("entr n "))
for i in range(1,n+1):
    print()
    for k in range(1,i+1):
        if i==n or k==i or k==1:
            print('*',end=" ")
        else:
            print(" ",end="")