c=0
def count(n,num):
    if n==0:
        return 0
    match=0
    last=n%10
    if last==num:
        match=1
    return match+count(n//10,num)

        


def main():
    x=int(input("enter a number "))
    num=int(input('enter a lucy digit '))
    
    print(f"digit {num} appered ",count(x,num),"times")
main()