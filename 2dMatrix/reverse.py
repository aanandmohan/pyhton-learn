row=int(input("enter row "))
col=int(input('enter col '))
matrix=[]

sum=0
for i in range(row):
    rows=[]
    for j in range(col):
        x=int(input("ente elemnt "))
        # if x%2!=0:
        #     sum+=x
        
        rows.append(x)
    matrix.append(rows)
print(matrix)

for rows in matrix:
    i=0
    j=len(rows)-1
    while i<j:
        t=rows[i]
        rows[i]=rows[j]
        rows[j]=t
        i+=1
        j-=1

for i in range(row):
    for j in range(col):
        print(matrix[i][j],end=" ")
    print()

    