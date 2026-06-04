row=int(input('enter the rows '))
col=int(input("enter the colimns "))
matrix=[]
# for i in range(row):
#     rows=[]
#     for j in range(col):
#         x=int(input('enter '))
#         rows.append(x)
#     matrix.append(rows)
# print(matrix)

for i in range(row):
    rows=[]
    for j in range(col):
        rows.append(int(input('enter elemt ')))
    matrix.append(rows)
print(matrix)
