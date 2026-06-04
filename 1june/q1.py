# a=[10,20,30,40,50,60,70]
a=[10,10,10,10]

max1=0
max2=0
for i in a:
    if i>max1:
        max2=max1
        max1=i
    elif i>max2 and i!=max1:
        max2=i

    
if max1==max2:
    print("non sencond elemt ")
else:
    print("second highest element is ",max2)