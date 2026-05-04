
num=int(input("enter a number "))
count=0
rev=0

while num>0:
    t=num%10
    
    if count ==0:
        print("Digit Process: ",end=" ")
    
    
    if t==0:
       
        print("\ncount",count)
        print("zero found process stop")
        break
    else:
        print(t,end=" ")
        count+=1
        num=num//10
else:
    
    print("\ncount",count)
    print("no zero found")