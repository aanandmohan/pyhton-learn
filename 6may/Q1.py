import math
while True:
    print("Menu Option ")
    print("1 check prime number")
    print("2 check palindrom number")
    print("3Reverse a Number")
    print("4 Count digit ")
    print("5 Exit")
    choice=int(input('enter your choice '))
    match choice:
        case 1:
            n=int(input('enter a number '))
            if n<2:
                print("prime number")

            for i in range(2,int(math.sqrt(n))):
                if n%i==0:
                    print("Not a prime number ")
                    break
            else:
                print("Prime number")
        case 2:
            n=int(input("enter a number "))
            rev=0
            temp=n
            while n>0:
                t=n%10
                rev=rev*10+t
                n=n//10
            if rev==temp:
                print("palindrom number ")
            else:
                print('not a palindrom')
        case 3:
            n=int(input("enter a number "))
            rev=0
            temp=n
            while n>0:
                t=n%10
                rev=rev*10+t
                n=n//10
            print("Reverse number is ",rev)
        case 4:
            n=int(input("enter a number "))
            re=0
            temp=n
            while n>0:
                t=n%10
                re+=1
                n=n//10
            print("count is ",re)
        case 5:
            print("Exit programm Thankyou")
            break


