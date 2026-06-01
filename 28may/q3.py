import math
n=int(input("enter size "))
l=[]
for i in range(n):
    x=int(input("enter number "))
    l.append(x)

prime=[]
primes=" "
nonprime=[]
for i in l:
    if i>1:
        j=2
        while j<int(i)//2:
            if int(i)%j==0:
                nonprime.append(i)
                break
            j+=1
        else:
            primes+=str(i)+" "
            prime.append(i)
        


print("prime number is ",primes)
print("prime number ",prime)
print("sorted:",sorted(prime))
print("largest prime number ",prime[-1])

print("count of prime ",len(prime))
print("count of non prime",len(nonprime))  
        

