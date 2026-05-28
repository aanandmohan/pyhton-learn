s=input("enter string ")
n=int(input("enter n "))
l=len(s)//n
for i in range(0,len(s),2):
    print(s[i:i+2],end=" ")