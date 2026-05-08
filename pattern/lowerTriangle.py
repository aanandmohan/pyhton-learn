n=int(input("enter n "))

i=n
while i>=1:
    print()
    j=i
    while j>=1:
        print(j,end=" ")
        j-=1
    i-=1

print()

'''i=n
while i>=1:
    print()
    j=i
    while j>=i:
        print(j,end=" ")
        j-=1
    i-=1
    
that was for my practice


    '''

i=1
while i<=n:
    print()
    j=1
    while j<=(n-i)+1:
        print(j,end=" ")
        j+=1
    i+=1

print()


i=1
while i<=n:
    print()
    j=i
    while j<=n:
        print(j,end=" ")
        j+=1
    i+=1