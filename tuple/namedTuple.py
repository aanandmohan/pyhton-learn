from collections import namedtuple
'''account=namedtuple("account",["accnonumber","nameholder","balnce"])
accno=int(input("enter acoount number "))
name=input("enter name ")
bal=int(input("enter balance "))
a1=account(accno,name,bal)
a2=account(1235,"ram",12354)
print(a1.accnonumber)
print(a1.nameholder)
print(a1.balnce)
print(a1)'''
student=namedtuple("student",["name","roll","marks"])
n=int(input("enter number of students "))
stu=[]
for i in range(n):
    r=int(input("enter roll number "))
    n=input("enter name ")
    m=int(input("enter marks "))
    stu.append(student(r,n,m))
print(stu)

for s in stu:
    print(s.roll)
    print(s.name)
    print(s.marks)