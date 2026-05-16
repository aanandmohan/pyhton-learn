n=input("enter mesaagee ")
i=0
count=0
while i<len(n):
    ch=n[i]
    if ch=='a' or ch=='i' or ch=='o' or ch=='u' or ch=='e':
        count+=1
    i+=1
print("total vowel is ",count)