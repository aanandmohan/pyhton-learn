n = int(input())
i=1
while i<n:
    print()
    j=1
    while j<=i:
        if j==1 or j==i :
            print(j,end="")
        else:
            print(" ",end="")
        j+=1
  
    i+=1
print()
for i in range(1,n+1):
    print(i,end="")