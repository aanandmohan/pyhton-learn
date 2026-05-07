x=int(input("enter first number "))
y=int(input("enter second number "))

for i in range(x,y+1):
    t=1
    while t<=10:
        print(i*t)
        t+=1
    print()    
    