def count(n):
    if n==0:
        return 0
    return 1+count(n//10)

def main():
    x=count(12345)
    print(x)
main()