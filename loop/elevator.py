n1=int(input("enter current floor "))
n2=int(input("enter destination floor "))
if n1<n2:
    for i in range(n1,n2+1):
        # print(i,end="->")
        print("->",i)
else:
    for i in range(n1,n2-1,-1):
        # print(i,end="->")
        print("->",i,end=" ")