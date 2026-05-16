# 9) Hollow Diamond Square
#     ***********
#     ****   ****
#     ***     ***
#     **       **
#     *         *
#     *         *
#     **       **
#     ***     ***
#     ****   ****
#     ***********

n=int(input("enter n "))
for i in range(n):
    print()
    for k in range(1,(n-i)+1):
        print(k,end="")
    for l in range(i*2):
        print("*",end="")
    k=(n-i)
    while k>=1:
        print(k,end="")
        k-=1
for i in range(n+1):
    print()
    for k in range(i+1):
        print("*",end="")
    for l in range((i*2)-1):
        print(" ",end="")
    k=n-i
    while k>=1:
        print(k,end="")
        k-=1