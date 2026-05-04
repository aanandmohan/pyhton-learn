
num=int(input("enter a number "))
rev=0
while num>0:
    t=num%10
    rev=rev*10+t
    num=num//10


n1=rev%10
rev=rev//10
n2=rev%10
rev=rev//10
sub=abs(n1-n2)

while rev>0:
    t=rev%10
    sub2=abs(n2-t)
    if sub2!=sub:
        print('intial gap is ',sub)
        print("pattern break detected")
        break
    else:
        n2=t
        rev=rev//10
else:
    print("intial Gap is ",sub)
    print("Consistent pattern")