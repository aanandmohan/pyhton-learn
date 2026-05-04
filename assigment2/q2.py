num=int(input("enter a number "))
count=len(str(num))
num1=num%10
num=num//10
print("count is ",count)
while num>0:
    count-=1
    t=num%10
    if t>num1:
        print("breaking at ",count)
        break
    else:
        num=num//10
else:
    print('strictly increasing number ')