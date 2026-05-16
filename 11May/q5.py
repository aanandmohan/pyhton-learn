# 5) Number-Star Palindrome
#     12344321
#     123**321
#     12****21
#     1******1


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
'''n=int(input("enter n "))
for i in range(n+1):
    print()
    for j in range(1,n-i):
        print(" ",end="")
    k=n-i
    while k>=1:
        print(k,end="")
        k-=1
    '''
    
