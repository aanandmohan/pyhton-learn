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

'''tar=int(input("enter target "))
flag=0
for i in matrix:
    for j in i:
        if j%2!=0:
            sum+=j
        if j==tar:
            print("element found ")
            flag=1
            break
if flag==0:
    print("not found ")'''
for i in matrix:
    i[::-1]

for i in range(row):
    for j in range(col):
        print(matrix[i][j],end=" ")
    print()

