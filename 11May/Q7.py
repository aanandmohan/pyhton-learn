    # - - - -
    # 2 - - -
    # 4 3 - -
    # 6 5 4 -
    # 8 7 6 5

n=int(input("enter n "))

i=0
while i<n:
    print()
    j=1
    while j<=i:
        print(j,end="")
        j+=1
    for k in range(i+1,n):
        print("-",end="")
    i+=1