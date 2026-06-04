row1=int(input("enter row "))
col1=int(input("enter column "))
matrix1=[]
for i in range(row1):
    rows=[]
    for j in range(col1):
        x=int(input("enter elemnt "))
        rows.append(x)
    matrix1.append(rows)

print(matrix1)
print()
row2=int(input("enter row "))
col2=int(input("enter column "))
matrix2=[]
for i in range(row2):
    rows=[]
    for j in range(col2):
        x=int(input("enter elemnt "))
        rows.append(x)
    matrix2.append(rows)

print(matrix2)

if col1!=row2:
    print("multiplication is not possible ")
else:
    result=[]
    for i in range(row1):
        r=[]
        for j in range(col2):
            r.append(0)
        result.append(r)
    
    for i in range(row1):
        for j in range(col2):
            for k in range(col1):
                result[i][j]=result[i][j]+matrix1[i][k]*matrix2[k][j]

print("result")
for row in result:
    print(*row)


