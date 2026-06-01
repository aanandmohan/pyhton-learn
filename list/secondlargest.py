arr=[10,20,30,40,50,99]
max1=0
max2=0

for i in arr:
    if i>max1:
        max2=max1
        max1=i
    elif i>max2 and i!=max1:
        max2=i
print(max2)


uni=[]
for i in arr:
    if i not in uni:
        uni.append(i)
print(uni)
arr.sort()
print(arr[-2])