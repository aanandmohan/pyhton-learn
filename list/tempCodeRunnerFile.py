n=int(input("eneter size "))
arr=[]
sum=0
for i in range(n):
    x=int(input('enter elemt '))
    arr.append(x)
print(arr)
for i in range(1,len(arr)+1):
    if i%2==0:
        sum+=arr[i]
print(sum)