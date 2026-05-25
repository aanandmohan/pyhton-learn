s=input("enter string ")
words=s.split()
res=""
for i in range(0,len(words)):
    if words[i]!='0' and words[i]!='9':
        ch=words[i]
        j=i+1
        count=1
        while j<len(words):
            if ch==words[j]:
                count+=1
                words[j]=count
            j+=1
        res+=ch+" "
print("the reuslt is ->",res)