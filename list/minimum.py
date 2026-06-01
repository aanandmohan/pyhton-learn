arr=[10,20,432,1,9,57]
max=arr[0]
for i in range(1,len(arr)):

    if arr[i]<max:
        max=arr[i]
print(max)