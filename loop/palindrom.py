n=int(input("enter n "))
temp=n
rev=0
while n>0:
    t=n%10
    rev=rev*10 +t
    n=n//10

if temp==rev:
    print("palindrom")
else:
    print("not palindrom")