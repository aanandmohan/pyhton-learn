'''l=[92,60,32,55,76]
def fun(x):
    return x%2==0

r=filter(fun,l)
t=filter(lambda a:a%2==0,l)
print(list(t))
print(list(r))'''
s=["1","2","3"]
'''name=["anksadha","vishnukant","sita","raguhever","",""]
k=map(lambda a:int(a),s)
print(list(k))
t=filter(lambda a:len(a)>5,name)
m=filter(lambda a :len(a)!=0,name)
print(list(m))
print(list(t))'''
'''l=[1,2,3,4,5,6]
r=map(lambda a:a*a,filter(lambda a:a%2==0,l))
r=filter(lambda a:a%2==0,map(lambda a:a*a,l))
print(list(r))
'''
word=["abc","vishnu","kanak","ritu"]
t=map(lambda a:a[::-1],word)
print(list(t))

z="sita"
