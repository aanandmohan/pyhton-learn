num=int(input("enter a number "))
temp=num
s=len(str(num))
sum1=0
sum2=0
rev=0
while num>0:
    t=num%10
    rev=rev*10+t
    num=num//10

rev1=0
rev2=0
for i in range(s):
    t=rev%10
    if i<s//2:
        rev1=rev1*10+t
    else:
        rev2=rev2*10+t
    rev=rev//10
print("first half  ",rev1)
print("second half ",rev2)
sq=rev1+rev2
print("sum is ",sq)
square=sq**2
if temp==square:
    print("tech number ")
else:
    print("non tech number ")
