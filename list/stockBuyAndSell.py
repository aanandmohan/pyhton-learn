'''a=[7,1,5,3,6,4]'''
a=[7,6,5,4,3,1]
profit=0
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[j]-a[i]>profit:
            profit=a[j]-a[i]

print(profit)