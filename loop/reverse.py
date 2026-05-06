# n=int(input("enter n "))
# temp=n
# rev=0
# while n>0:
#     t=n%10
#     rev=rev*10 +t
#     n=n//10

# print("the revrse number is ",rev)

  #reverse using for loop

n=int(input("enter number"))
rev=""
for i in str(n):
    rev=i+rev
print("reverse number is ",rev)