arr=["abc","de","fg","ad","ta"]
count=0
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        ch=arr[i]
        for k in ch:
            if k in arr[j]:
                break
        else:
            count+=1
print(count)