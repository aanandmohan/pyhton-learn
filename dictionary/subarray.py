a=[1,2,12,4,5,6,7]
tar=9
min=len(a)
z=[]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        # print(a[i:j])
        t=sum(a[i:j+1])
        if t>=tar :
            if len(a[i:j])>min:
                min=len(a[i:j])
                z=a[i:j]

        
print(min)
print(z)