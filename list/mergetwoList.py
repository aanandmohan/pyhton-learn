a=[1,2,3,4,5]
b=[5,4,6,7,8]
c=a+b
result=[]
for i in c:
    if i not in result:
        result.append(i)
print(result)