l=[10,30,20,30,50]
# for i in range(len(l)):
#     print("the is index is",i,"and vlue is ",l[i])
i=0
while i<len(l):
    print(l[i])
    i+=1
l.append(90)
l.append(500)
for i in range(len(l)):
    print(l[i],end=" ")