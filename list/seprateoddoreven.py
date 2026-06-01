arr=[10,13,9,5,4,8]
odd=[]
even=[]
for i in arr:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)