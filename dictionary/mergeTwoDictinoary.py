l1={"goa":5,"nepal":3,"delhi":8}
l2={"goa":6,"hyderabad":6,"delhi":2}
print()
'''merge=l1.copy()

for k,v in l2.items():
    merge[k]=merge.get(k,0)+v
print(merge)'''


#without creating extra dictinary
for k,v in l2.items():
    l1[k]=l1.get(k,0)+v
print(l1)