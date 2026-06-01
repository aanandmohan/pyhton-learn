a=[1,2,3,4,5,6]
d=[1,2,3,4,5,67,8,9,9,10,24,25,26]
# b=[]
# for i in a:
#     b.append(i*2)
# print(b)
# b=[ i*2 for i in a]
'''e=["even" if i%2==0 else "odd" for i in d]
print(e)
b=[i for i in a if i%2==0 if i>3]
print(b)'''

s=["deepika ","senha",'anushka',"rcb"]
# b=[i for i in s if len(i)>3]
# b=[i.upper() for i in s]
b=[i*10 if i%2==0 else i for i in a]
print(b)