'''b=eval(input("enter dictionary "))
print(b)
print(type(b))'''

# a=eval(input("enter number "))
# print(a)
# print(type(a))

# c=eval(input("enter list "))
# print(c)
# print(type(c))

#without eval
n=int(input("enter number of items"))
d={}
for i in range(n):
    key=input("enter keys ")
    val=int(input("enter values "))
    d[key]=val
print(d)
print("the sum of values is ",sum(d.values()))


