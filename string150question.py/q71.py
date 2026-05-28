s=input("enter string ")
for i in range(len(s)):
    j=i+1
    while j<=len(s):
        print(s[i:j])
        j+=1
