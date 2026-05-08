x=int(input("enter first number "))

for i in range(1,x+1):
    t=1
    while t<=3:
        print(f"{t}*{i}=",i*t)
        t+=1
    print()    
    