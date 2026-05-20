str=input(" enter string ")
n=len(str)
i=0
while i<n:
    print(str[i],end="")
    i+=1
print()
i=n-1
while i>=0:
    print(str[i],end="")
    i-=1
print()
i=-1
while i>=-n:
    print(str[i],end="")
    i-=1
print()
print()
print(str[n-1:0:-1],end="")

