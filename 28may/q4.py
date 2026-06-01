import math
n=int(input("enter size "))
l=[]
for i in range(n):
    x=input("enter number ")
    l.append(x)
palindrom=[]
count=0
for i in l:
    ch=i
    rev=ch[::-1]
    if ch==rev:
        palindrom.append(int(ch))
        count+=1
print("count ",count)
print("palindrom list ",palindrom)
b=sorted(palindrom)
print("sorted palindrom ",b)
print("the longest palindrom ",b[-1])