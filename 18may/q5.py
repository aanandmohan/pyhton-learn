num=input("enter a nummber ")
n=len(num)
for i in range(1,n):
    j=0
    k=n-1
    if num[j]==num[k]:
        j+=1
        k-=1
    else:
        print("not palindrom ")
        break
else:
    print("palindrom code ")