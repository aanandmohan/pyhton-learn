n=input("enter mesaagee ")
i=0
count=0
while i<len(n):
    ch=n[i]
    if ch==' ':
        count+=1
    i+=1
print("total space is  ",count)