n=int(input('enter n '))
ch=97
for i in range(1,n+1):
    
    for j in range(1,i+1):
        if j==1 or j==i or i==n:
            print(chr(ch),end="")
            ch+=1
        else:
            print(" ",end="")
    print()