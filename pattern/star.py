n=int(input("enter n "))

i=1
while i<=n:
    print()
    j=1
    while j<=i:
        if i%2==0:
            print("*",end=" ")
        else:
            print(j,end=" ")
        j+=1
        
    i+=1

print()

i=1
while i<=n:
    print()
    j=1
    while j<=i:
        if j%2==0:
            print("*",end=" ")
        else:
            print(j,end=" ")
            
        j+=1

        
        
    i+=1

print()

i=1
k=1
while i<=n:
    print()
    j=1
    while j<=i:
        print(k,end=" ")
        k+=1
        j+=1
     
        
    i+=1



i=1
while i<=n:
    print()
    sp=1
    while sp<=(n-i):
        print(" ",end="")
        sp+=1


    dec=1
    ch=65
    while dec<=i:
        print(chr(ch),end="")
        ch+=1
        dec+=1
    i+=1