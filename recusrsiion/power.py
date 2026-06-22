def power(num,x):
    if x==0:
        return 1
    return num*pow(num,x-1)


def main():
    x=int(input("enter number "))
    num=int(input('enter a number '))
    t=power(num,x)
    print(t)
main()