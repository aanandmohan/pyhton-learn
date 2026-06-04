row=int(input("enter row "))
col=int(input(" enter column "))
matrix=[]
larg=0
small=99999999999999
mal=1
for i in range(row):
    rows=[]
    for j in range(col):
        x=int(input("enter that "))
        mal*=x
        if x>=larg:
            larg=x
        if x<=small:
            small=x
        rows.append(x)
    matrix.append(rows)
print(matrix)
print('multipliction is ',mal)
print("total element in matix is ",row*col)
print('largest value is ',larg)
print("samlles value is ",small)