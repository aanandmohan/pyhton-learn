n=int(input("enter number"))
digit=int(input("enter digit"))
count=0
while n>0:
    t=n%10
    if t==digit:
        count=count+1
    n=n//10
print("occurence of digit is ",count)