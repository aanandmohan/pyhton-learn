l=[10,23,24,25,28]
l1=[20,30,80,100]

marks=[92,50,70,82,42]
k=map(lambda a:"A" if a>75 else "B" if a>60 else "c" if a>40 else "fail",marks)
print(list(k))
t=map(lambda a,b:a+b,l,l1)
print(list(t))
r=map(lambda a:"even" if a%2==0 else "odd",l)
print(list(r))