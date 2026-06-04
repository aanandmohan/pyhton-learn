row=int(input("enter row "))
col=int(input('enter col '))
matrix1=[]

sum=0
for i in range(row):
    rows=[]
    for j in range(col):
        x=int(input("ente elemnt "))
        # if x%2!=0:
        #     sum+=x
        
        rows.append(x)
    matrix1.append(rows)
print(matrix1)
print()

matrix2=[]

sum=0
for i in range(row):
    rows=[]
    for j in range(col):
        x=int(input("ente elemnt "))
        # if x%2!=0:
        #     sum+=x
        
        rows.append(x)
    matrix2.append(rows)
print(matrix2)
print()


matrix3=[]

sum=0
for i in range(row):
    rows=[]
    for j in range(col):
        rows.append(0)
    matrix3.append(rows)
print(matrix3)

'''for i in range(row):
    for j in range(col):
        matrix3[i][j]=matrix1[i][j]+matrix2[i][j]'''
for i in range(len(matrix3)):
    for j in range(len(matrix3[i])):
        matrix3[i][j]=matrix1[i][j]+matrix2[i][j]
        
print()
print("after addition of matrix ")
'''for i in matrix3:
    for j in i:
        print(j,end=" ")
    print()'''

for i in range(col):
    for j in range(row):
        print(matrix3[i][j],end=" ")
    print()