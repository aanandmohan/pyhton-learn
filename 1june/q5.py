row=int(input("enter row "))
col=int(input('enter col '))
matrix=[]
sum1=0
for i in range(row):
    rows=[]
    for j in range(col):
        x=int(input("ente elemnt "))
        sum1+=x
        rows.append(x)
    matrix.append(rows)
# print(matrix)
avg=[]
maximusum=0
maxrow=0
for i in range(row):
    sum=0
    for j in range(col):
        sum+=matrix[i][j]
    print(f"row {i+1} sum ",sum)
    avgg=sum/col
    avg.append(avgg)
    '''print("the avreage sum is ",sum/col)'''
    if sum>maximusum:
        maximusum=sum
        maxrow=i+1
print() 
for i in range(row):
    print(f"the average sum of {i+1} row is ",avg[i])

print()
print("the total sum is ",sum1)
print('the maximum sum of row is : ROW',maxrow)





