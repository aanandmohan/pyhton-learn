# 18) Binary Floyd Triangle
#     1
#     0 1
#     1 0 1
#     0 1 0 1

n=int(input("enter n "))
num=1
for i in range(1,n+1):
    print()
    for k in range(1,i+1):
        print(num%2,end='')
        num+=1
        