s={1,2,3,4,2,11,22,33,44,44}
#accesing set elments
for i in s:
    print(i)
'''print(s)'''
print(20 in s)
t=set([44,34,55,11,34,55])
t.add(999)
t.update(["vish",8988,723])
print(t)
s.remove(11)
print(s)

#pop()
s.pop()
print(s)