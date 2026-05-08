x=int(input("enter starting point "))
y=int(input("enter ending point "))
print("palindrom number are: ")
for i in range(x,y+1):
    num=i
    final=num
    rev=0
    while i>0:
        t=i%10
        rev=rev*10+t
        i=i//10
    if rev==num:
        print(num)