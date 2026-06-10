d={1:"vishnu",2:"ramesh",3:"ram",4:"alok",5:"anish"}
'''n=int(input("enter  number of stundent "))
i=1
while i<=n:
    name=input("enter name ")
    marks=input("enter % of marks")
    d[name]=marks
    i+=1
print("name of student is ","\t","% marks is")
for x in d:
    print(x,"\t\t",d[x])'''

#adding and updating in dictionary item
# k={1:"dipu",2:"lita",}
# k[3]="virat"
# k[8]="sikunj"
# print(k)
# #updating
# k[1]="vaibhav"
# print(k)
# print(k.pop(8))
# k[9]="vishnukant"
# print(k.popitem())

#fuction of del
'''del k[1]
if 10 in k:
    del k[10]
print(k)'''
# print(k.keys())
# print(list(k.keys()))
# print(k.values())
# print(list(k.values()))



'''for key,val in d.items():
    print(key,val)
d.update({"age":"somewhow"})
d.update({12:"rajveer"})
print(d)'''
t=d.copy()
print(t)
t.update({"chalbe":"ha aa rha hu"})
print(d)
print(t)