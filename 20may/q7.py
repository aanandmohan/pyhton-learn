s=input("enter string ")
words=s.split()

res=''
i=0
while len(words)-1>i:
    if words[i+1]!=words[i]:
        res=res+words[i]
    i+=1

print("final string is ",res)
