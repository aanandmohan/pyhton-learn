'''row=int(input("enterr row "))

for i in range(1,row+1):
    for j in range(1,i):
        print(j,end=" ")
    print()'''

n=int(input("enter number "))

i=1
while i<=n:
    j=1
    while j<=i:
        print(j,end=" ")
        j+=1
    print()
    i+=1


