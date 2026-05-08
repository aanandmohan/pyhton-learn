x=int(input('enter a starting number '))
y=int(input("enter ending number "))

for i in range(x,y+1):
    

    sqr=i*i
    
    sum=0
    num=sqr
    while num>0:
        t=num%10
        sum+=t
        num=num//10
    if sum==i:
        print(i)
    
    
    

        



    
