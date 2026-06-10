s=[1,2,3,4,5,6,7,8,]
d={i:i*i   for i in range(1,11) if i%2==0}
print(d)
t={i:"even" if i%2==0 else "odd" for i in s}
print(t)