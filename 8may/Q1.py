n=int(input("enter starting number "))
t=int(input("enter ending number "))
sum=0
for i in range(n,t+1):
    if i%9==0:
        sum+=i
        print(i,end=" ")
print("sum is ",sum)
