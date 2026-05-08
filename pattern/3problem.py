n=int(input("enter n "))

i=1
while i<=n:
    print()
    inc=1
    while inc<=i:
        print(inc,end="")
        inc+=1
    
    s=1
    while s<=(n-i)*2:
        print('*',end="")
        s+=1
    dec=i
    while dec>=1:
        print(dec,end="")
        dec-=1
    i+=1