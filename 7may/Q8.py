x=int(input("enter number of classes "))
clas=int(input("enter number of per class "))
sub=int(input("enter subject per student "))

for i in range(1,x+1):
    print("class ",i)

    for j in range(1,clas+1):
        print("student ",j)
        marks=0
        for k in range(1,sub+1):
            m=int(input("enter marks "))
            marks+=m
        print("Student ",j,"total",marks)
