n=int(input('enter n '))
for i in range(1,n+1):
    ch=65
    for j in range(1,i+1):
        if j==1 or j==i or i==n:
            print(chr(ch),end="")
            ch+=1
        else:
            print(" ",end="")
    print()



n=int(input('enter n '))
for i in range(1,n+1):
    for j in range(1,i+1):
        if j==1 or j==i or i==n:
            print(i,end="")
            ch+=1
        else:
            print(" ",end="")
    print()