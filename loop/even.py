n=int(input("enter n "))

rev=0
count=0
while n>0:
    t=n%10 
    if t%2==0:
        count+=1
    n=n//10

print("the count of even digit is ",count)