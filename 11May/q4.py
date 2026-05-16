n=int(input('enter n '))

for i in range(n):
    print()
    for k in range((n-i)+1):
        if k==n-i:
            print("*",end="")
        else:
            print(" ",end='')
    j=1
    while j<=i:
        if j==i:
            print(j,end="")
        else:
            print(" ",end="")
        j+=1
    
    
    

    