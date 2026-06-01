# a=[1,2,3,4,[22,55],6]
# print(a[4][1])
# travres in nested list

a=[
    [10,20,30,40,50],
    [1,2,3,4,5,6,7],
    [70,80,90,100]
]
# for r in a:
#     print(r)
# for  i in a:
#     for j in i:
#         print(j,end=" ")
#     print()

for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j],end=" ")
    print()