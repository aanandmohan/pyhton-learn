a=[4,5,1,2,1,2,4]
for i in range(len(a)):
    count=1
    for j in range(i+1,len(a)):
        if a[i]==a[j]:
            count+=1
    if count==1:
        print("first non repeting char is ",a[i])
        break