'''5
44
333
2222
11111'''

n=int(input("enter a number "))
for i in range(1,n-1):
    for j in range(1,n-i):
        print(" ",end="")
    l=j
    for k in range(n-i,n):
        print(l,end="")
    print()