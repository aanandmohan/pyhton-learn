s=input("enter string ")
words=s.split()

for i in range(len(words)):
    if words[i]!=0:
        
        ch=words[i]
        j=i+1
        count=1
        while j<len(words):

            if ch==words[j]:
                words[j]=0
                count+=1
            j+=1
        print(ch,": ",count)