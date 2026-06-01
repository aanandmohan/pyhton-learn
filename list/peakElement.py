arr=[2,3,8,12,45,5,0]
# for i in range(len(arr)-1):
#     if arr[i]>arr[i+1]:
#         print(arr[i])
# print(arr[len(arr)-1])

peakindex=-1
for i in range(len(arr)):
    if i==0:
        if arr[i]>=arr[i+1]:
            peakindex=i
            break
    elif i==len(arr)-1:
        if arr[i]>=arr[i-1]:
            peakindex=i
    else:
        if arr[i]>=arr[i-1] and arr[i+1]:
            peakindex=i
print("the peak element is ",arr[peakindex])