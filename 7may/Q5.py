x=int(input("enter first number "))
y=int(input("enter second number "))

for i in range(x,y+1):
    t=i
    total=0
    
    while t>0:
        k=t%10
        fac=1
        for k in range(1,k+1):
            fac=fac*k
        total=total+fac
        t=t//10
    if total==i:
        print(i)

'''num=int(input("enter num "))
total=0
while num>0:
    t=num%10
    fac=0
    for i in range(1,t+1):'''





   