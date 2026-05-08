'''n=int(input('enter n '))

i=1
while i<=n:
    print()
    s=1
    while s<=(n-i):
        print(" ",end="")
        s+=1
    
    j=1
    ch=65
    while j<=i:
        print(chr(ch),end="")
        j+=1
        ch+=1
    i+=1'''


n=int(input('enter n '))


for i in range(1,n+1):
    print()
    ch=65
    for j in range(i):
        print(chr(ch),end="")
        ch+=1
