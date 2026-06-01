a=[2,2,2,3,5,1,5,7,2]
count=0
ch=0
l=[]
for i in a:
    if i not in l:
        if a.count(i)>1:
            count+=1
            l.append(i)

        
l.sort()
print("the duplicate list is ",l)
print("total duplicate number is ",count)