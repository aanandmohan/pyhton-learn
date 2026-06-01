a=[2,2,2,3,5,1,5,7,2]
count=0
ch=0
for i in a:
    if a.count(i)>count:
        count=a.count(i)
        ch=int(i)

print("the leader value is ",ch)