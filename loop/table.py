n=int(input("enyter number "))
# for i in range(1,11):
#     print(n*i)
mul=1
while n>0:
    t=n%10
    mul=mul*t
    n=n//10
print(mul)