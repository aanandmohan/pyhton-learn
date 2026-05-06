n=int(input("enter n "))
temp=n
t=0
arm=0
while n>0:
    t=n%10
    arm=t*t*t+arm 
    n=n//10
print("arm strong number is ",arm)

if n==arm:
    print("armstrong")
else:
    print("not arm strong")