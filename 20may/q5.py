s=input("enter string ")
n=len(s)
s=sorted(s)
cont=1
for i in range(0,n-1):
    if s[i+1]!=s[i]:
        cont+=1
print("count is ",cont)
