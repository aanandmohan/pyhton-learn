marks=[]
def adddetail(name,roll):
    print("Name is ",name)
    print("roll number is ",roll)
    for i in range(5):
        x=int(input(f'enter marks of {i}' ))
        marks.append(x)

name=input("enter name ")
roll=int(input("enter roll number "))
adddetail(name,roll)

def total():
    s=0
    for i in marks:
        s+=i
    return s

t=total()
print(t)

def percentage(x):
    l=(x/500)*100
    return l
per=percentage(t)
print(per)

def grade(per):
    if per>=90:
        print("A grade")
    elif per>=50 or per<=89:
        print("B garde ")
    else:
        print("fail")
grade(per)

def high():
    high=0
    for i in marks:
        if i>high:
            high=i
    return high
print('the hiighet numbr is ',high())
def lower():
    low=max(marks)
    for i in marks:
        if i <low:
            low=i
    return low
print('the lower numbr is ',lower())
def result():
    print("name is ",name)
    print("Roll number is ",roll)
    for i in range(1,len(marks)):
        print(f"the marks of subject {i}",marks[i])

    print("the total marks is ",t)
    print("the percentage is ",per)
    grade(per)
    print("the highest marks is ",high())
    print("the lowest marks is ",lower())

            

result()

