row=int(input('enter the rows '))
col=int(input("enter the colimns "))
matrix=[]
for i in range(row):
    rows=[]
    for j in range(col):
        rows.append(int(input('enter elemt ')))
    matrix.append(rows)

sum=0
# for i in matrix:
#     for j in i:
#         sum+=j
# print("sum is ",sum)
'''for i in range(row):
    for j in range(col):
        sum+=matrix[i][j]
print("sum is ",sum)'''

i=0
while i<row:
    j=0
    while j<col:
        sum+=matrix[i][j]
        j+=1
    i+=1
print("sum is ",sum)