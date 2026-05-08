x=int(input("enter starting number "))
y=int(input("enter ending number "))

for i in range(x,y+1):
    t=1
    fac=0
    while t<=i//2:
        if i%t==0:
            fac=fac+t

        t+=1
    if fac==i:
        print(i)

    