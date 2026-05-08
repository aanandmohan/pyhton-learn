x=int(input("enter first numbr"))
y=int(input("enter second number "))

while x<=y:
    n=x
    flag=True
    if n>1:
        i=2
        while i<n:
            if n%i==0:
                
                break
            i+=1
        else:
            print(n)
    x=x+1