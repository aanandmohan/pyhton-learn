def binary(x):
    if x==0:
        return "0"
    if x==1:
        return "1"
    
    return binary(x//2) + str(x%2)

def main():
    x=int(input("enter a digit "))
    t=binary(x)
    print(f"the binary of {x}is",t)
main()