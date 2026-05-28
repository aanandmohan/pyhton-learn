l=[10,20,30,40,405,10]
b=l.copy()
l[0]=1000
print(l)
print(b)
'''print(l)
l.remove(10)
print(l)'''
'''l.pop()
print(l)
l.pop(7)

print(l)'''
'''for i in l:
    if i%2==0:
        l.remove(i)
print(l)

for i in l[:]:
    if i%2==0:
        l.remove(i)


print(l)
a=["acx","abwwec","abc","absdfhsdewrewc","sdj28328s","dsjo"]
print(a.count("abc"))
print(a.index("abc"))'''
'''name=input("enter name ")
if name in a:
    a.remove(name)
else:
    print("name not found ")
print(a)
print()
for i in a[:]:
    if i.startswith('a'):
        a.remove(i)
print(a)'''
'''b=[12,24,43,54,54,54,74.45]

b.sort()
a.sort(key=len)
b.sort(reverse=True)

print(a)
print(b)'''
k=["kdsfhsd","js","abc","sfshs"]
'''k.sort(key=len)
print(k)
t=[-10,-20,-3,4,5,6,-12]
t.sort(key=abs)
print(t)
t.sort(reverse=True)
print(t)'''

'''m=[11,3,4,5]
print(sum(m,10))
for i,val in enumerate(m,):
    print("index is ",i,"and ",val)'''
'''b=sorted(m)
print(b)
print(m)
m.reverse()
print(m)'''


m1=[11,3,4,50,880]
'''for i,j in zip(m,m1):
    if i==j:
        print("same ")
    else:
        print("not sme ")'''
'''a=[10,20,30,40]
c=['a','b','c']
for i,j in zip(a,c):
    print(i,"->",j)'''

z=list(map(int,input('enter number ').split()))
print(z)
print(len(z))
