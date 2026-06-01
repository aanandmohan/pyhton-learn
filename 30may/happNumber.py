n=int(input("enter number "))

sum=0
t=n
flag=0
while flag==0:
    
    while n>0:
        x=n%10
        sum+=x*x
        n=n//10
    if sum==1:
        flag=1
        print("happy number ")
        break
    print(sum)
print(sum)