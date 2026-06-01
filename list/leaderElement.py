arr=[8,3,9,4,5]

sum=0
for i in range(len(arr)):
    isLeader=True
    for j in range(i+1,len(arr)):
        if arr[i]<=arr[j]:
            isLeader=False
            break
    if isLeader==True:
            sum+=arr[i]
print("the sum of leader is ",sum)