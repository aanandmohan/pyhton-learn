rev=int(input('enter a number '))

num=0
while rev>0:
    t=rev%10
    num=num*10+t
    rev=rev//10


first=num%10
num=num//10
product=1
count=1
sum=0
smallest=num


while num>0:
    t=num%10
    product=first*t
    print(product,end=" ")
    sum+=product
    if product<smallest:
        smallest=product
    count+=1
    first=t
    num=num//10

print("\nsum is ",sum)
print("smaalest =",smallest)
if sum%count==0:
    print("stable number ")
else:
    print("unstable number")