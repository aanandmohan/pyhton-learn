arr=[10,2,3,4,5,6]
arr2=[10,2,7,8,9,17]
res=[]
for i in arr:
    if i in arr2:
        res.append(i)
print(res)