n=int(input("enter size "))
l=[]
for i in range(n):
    x=int(input("enter number "))
    l.append(x)

a=[]
b=[]
c=[]
fail=[]
for i in l:
    if i>=90:
        a.append(i)
    elif i>=75:
        b.append(i)
    elif i>=50:
        c.append(i)
    else:
        fail.append(i)

print("=======student report card======")
print("A grade strudent ",a)
print("B grade studnet ",b)
print("C garde student ",c)
print("fail strunnt ",fail)
print("===============================")
print("A count ",len(a))
print("B count ",len(b))
print("C count ",len(c))
print("fail count ",len(fail))
print("-------------------------")
print("total student ",n)