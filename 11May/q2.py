row=int(input("enter row "))
colm=int(input("enter column "))

for i in range(1,row+1):
    print()
    if i==1 or i==row:
        for j in range(1,colm+1):
            print("*",end="")
    else:
        for k in range(1,colm+1):
            if k==1 or k==colm:
                print("*",end="")
            else:
                print(" ",end="")

    