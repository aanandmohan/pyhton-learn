s=input("enter string ")
words=s.split()
max=0
chs=""
for i in range(len(words)):
    ch=words[i]
    j=0
    count=0
    while j<len(words):
        if ch==words[j]:
            count+=1
        j+=1
    if count>max:
        max=count
        chs=ch

print("this word",chs,max)