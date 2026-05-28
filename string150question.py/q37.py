s=input("enter string ")
words=s.split()
i=len(words)-1

while i>=0:
    word=words[i]
    res=''
    j=len(word)-1
    while j>=0:
        res+=word[j]
        j-=1
    print(res,end=" ")
    i-=1

