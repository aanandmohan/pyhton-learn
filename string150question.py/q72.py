s=input("enter string ")
n=int(input('enter number '))
for i in range(len(s)):
    j=i+1
    while j<=len(s):
        if len(s[i:j])==n:
            print(s[i:j])
        j+=1

