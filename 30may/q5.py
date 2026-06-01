# a=[1,7,3,6,5,6]
a=[1,3,5,2,2]
left=[]
left.append(a[0])

right=[]
right.append(a[len(a)-1])
for i in range(1,len(a)):
    left.append(left[i-1]+a[i])
print(left)
j=len(a)-2
k=1
while j>=0:
    right.append(right[k-1]+a[j])
    j-=1
    k+=1
print(right)

for i in range(len(left)):
    if left[i] in right:
        print("eubilibrium  index is two ",i+1)
        break