from collections import namedtuple
employ=namedtuple("employ",["employid","name","dep","sal"])
n=int(input("enter number of students "))
emp=[]
for i in range(n):
    id=int(input("enter employ id "))
    nam=input('enter employ name ')
    depart=input("enter employ departemnt ")
    salar=int(input("enter epmloy salray "))
    emp.append(employ(id,nam,depart,salar))

print(emp)

for s in emp:
    print(s.employid)
    print(s.name)
    print(s.dep)
    print(s.sal)