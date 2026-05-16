n=int(input("entr n "))
for i in range(1,n+1):
    print()
    for k in range(1,i+1):
        if k==i:
            print("*",end="")
        else:
            print(" ",end="")
        
        