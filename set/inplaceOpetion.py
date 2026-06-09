s={1,2,3}
t={3,4,5}
'''s.update(t)'''
print(s)
print(t)

#inplace intersection
s.intersection_update(t)
s&=t
print(s)