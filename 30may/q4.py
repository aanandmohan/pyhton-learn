a=[100,4,200,1,3,2]
# a=[10,11,12,20]

a.sort()
print(a)
count=0
sum=a[0]
for i in range(len(a)):
    
    if a[i]==sum:
        count+=1
    sum+=1
print("count is ",count)