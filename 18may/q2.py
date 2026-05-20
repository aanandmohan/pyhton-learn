num=input("enter a number ")
count=0
for i in range(len(num)):
    if num[i]>='0' and num[i]<='9':
        count+=1
print("total digit is ",count)