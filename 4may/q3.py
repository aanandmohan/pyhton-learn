num=int(input("enter number "))
count=0
rev=0
while num>0:
    t=num%10
    rev=rev*10+t
    num=num//10

num1=rev%10
rev=rev//10
print("Matching Digit ",end=" ")
while rev>0:
    num2=rev%10
    rev=rev//10
    num3=rev%10
    if num1+num3==num2:
        print(num2,end=" ")
        count+=1
        num1=num2
    else:
        num1=num2

print("\ncount ",count)