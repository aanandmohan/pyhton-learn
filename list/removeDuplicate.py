arr=[10,10,20,33,45,9,9]
'''uni=[]
for i in arr:
    if i not in uni:
        uni.append(i)
print(uni)'''

for i in arr:
    count=0
    for j in arr:
        if i==j:
            count+=1
    if count>1:
        arr.remove(i)
print(arr)