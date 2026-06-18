def prime(x):
    if x<2:
        print("prime number ")
    else:
        for i in range(2,x//2):
            if x%i==0:
                print("not prime number ")
                break
        else:

            print("prime number ")

def factorial(x):
    fact=1
    for i in range(1,x+1):
        fact*=i
    print(f"the factorial of {x} is :{fact}")

def reverse(x):
    num=x
    rev=0

    while x>0:
        t=x%10
        rev=rev*10+t
        x=x//10
    print(f"the reverse of {x} is {rev}")


def factor(x):
    fact=""
    for i in range(1,x):
        if x%i==0:
            t=str(i)
            fact+=t+" "
    print("the factor of given number is ",fact)

def perfect(x):
    num=x
    sum=0
    for i in range(1,x):
        if x%i==0:
      
            sum+=i

    print(sum)
    if sum==num:

        print("perfect Number ")
    else:
        print("not a perfect number")


while True:
    print("1 for perfect Number ")
    print("2 for factorial ")
    print("3 for reverse ")
    print("4 for factor ")
    print("5 for prime ")
    ch=int(input("enter choice "))
    match ch:
        case 1:
            x=int(input("enter number "))
            perfect(x)
        case 2:
            x=int(input("enter number "))
            factorial(x)
        case 3:
            x=int(input("enter a number "))
            reverse(x)
        case 4:
            x=int(input("enter a number "))
            factor(x)
        case 5:
            x=int(input("enter a number "))
            prime(x)
        case 6:
            print("process exit ")
            break
