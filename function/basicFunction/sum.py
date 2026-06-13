'''def sum(a,b):
    a=10
    b=30
    d=a+b
    print(d)
sum(10,20)'''

'''def sum(a,b):
    print(a*b)
    return a*b
print(sum(10,10))
    
def hello(x):
    print("hello mr :",x)
hello("vishal")'''

def anagaram(x,b):
    for i in x:
        if x.count(i)!=b.count(i):
            return False
    else:
        return True


print(anagaram("listen","silenttt"))