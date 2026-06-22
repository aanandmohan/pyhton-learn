def sum(n):
    if n==0:
        return 0
    return n+sum(n-1)

def main():
    x=int(input("enter number "))
    t=sum(x)
    print("the sum of n natural number is ",t)

main()