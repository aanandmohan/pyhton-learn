a={1,2,3,4,5,12,14,13}
b={1,2,5,8,9,13,23,24}
print(a)
print(b)
#union
print(a|b)
print(a.union(b)) 
#intersection
 
print(a&b)
print(a.intersection(b))

#difference 
print(a-b)
print(b-a)
print(a.difference(b))
#symmetric difference
print(a^b)
print(a.symmetric_difference(b))
#subset
s={"thapa","aman","muskan","deepika","rashmika"}
c={"krishna","aman","kuldeep","muskan","deepika","thapa","rashmika"}
print(s.issubset(c))
print(s<=c)
#super set

print(s.issuperset(c))
print(c>=s)
print(c.issuperset(s))