l=[92,60,32,55,76]
def fun(x):
    return x%2==0

r=filter(fun,l)
t=filter(lambda a:a%2==0,l)
print(list(t))
print(list(r))