arr=[99999,10,23,24,27,778]
max=0
'''for i in arr:
    if i>max:
        max=i'''

'''for i in range(len(arr)):
    if arr[i]>max:
        max=arr[i]'''
i=0
while i<len(arr):
    if arr[i]>max:
        max=arr[i]
    i+=1
print(max)