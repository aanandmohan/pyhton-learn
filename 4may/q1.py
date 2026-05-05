num=int(input("enter a number "))

rev=0
while num>0:
    t=num%10
    rev=rev*10+t
    num=num//10

max=-1
evencount=0
first=rev%10
rev=rev//10
second=rev%10
rev=rev//10
count=0
sub=abs(first-second)
print('difference ',sub,end=" ")
if sub%2==0:
    evencount+=1
while rev>0:
    t=rev%10
    
    sub1=abs(t-second)
    print(sub1,end=" ")
    if sub1%2==0:
        evencount+=1
    if max<sub1:
        max=sub1
    
    second=t
    
    
    rev=rev//10
print("\nmaximum difference is ",max)
print("evenm difference are ",evencount)
    



