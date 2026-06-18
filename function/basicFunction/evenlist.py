def even(n):
    even=[]
    for i in range(1,n+1):
        if i%2==0:
            even.append(i)
    return even
    
t=even(10)
print(t)