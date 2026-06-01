# n=int(input("enter size of list "))
# l=[]
# for i in range(n):
#     x=int(input("enter list "))
#     l.append(x)
# print(l)
a=[1,2,3,4,5,6,8]
n=len(a)
t=n+1
sum=0
final=(t*(t+1))//2
print(final)
for i in range(n):
    sum+=a[i]
miss=final-sum
print("the missing word id ",miss)
    
