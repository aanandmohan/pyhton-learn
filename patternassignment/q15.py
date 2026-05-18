n=int(input("enter a number "))

for i in range(n,0,-1):
    
    for k in range(1,i+1):
        if i==n or k==1 or k==i:
            print(i,end="")
            
        else:
            print(" ",end="")
    print()