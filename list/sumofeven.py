n=int(input("eneter size "))
arr=[]
sum=0
for i in range(n):
    x=int(input('enter elemt '))
    arr.append(x)
print(arr)
for i in range(len(arr)):
    if i%2==0:
        sum+=arr[i]
print(sum)


'''n=int(input("enter size "))
arr2=[]
sum=0
i=0
while i<n:
    x=int(input("enter elemt "))
    arr2.append(x)
    i+=1
j=0
while j<=len(arr2):
    if j%2==0:
        sum+=arr2[j]
    j+=1
print(sum)'''