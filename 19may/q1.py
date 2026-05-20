s1=input("enter string ")
n=len(s1)
last=s1[n-3:n]
s=''
for i in range(1,n-3):
    s+="*"
print(s+last)
