inte = [[1,3],[2,6],[8,10],[15,18]]
""" b=intervals[0]
print(b.sort())
print(intervals.sort()) """
inte.sort()
print(inte)
ans=[]
for i in range(len(inte)):
    row=[]
    for j in range(i+1,len(inte)):
        t=inte[i]
        m=inte[j]
        n=len(m)-1
        for k in t:
            if k in m:
                row.append(t[0])
                row.append(m[n])
                break
    ans.append(row)
   
    
print(ans)
