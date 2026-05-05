num=int(input("enter a number "))
s=len(str(num))
sum1=0
sum2=0
for i in range(s):
    t=num%10
    if i<s//2:
        sum1+=t
    else:
        sum2+=t
    num=num//10
print("sum of first hlaf ",sum1)
print("sum of second falf  ",sum2)
if sum1==sum2:
    print("balance number number")
else:
    print("unbalnce number ")