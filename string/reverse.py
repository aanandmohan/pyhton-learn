s=input("enter the string ")
word=""
i=0
while i<len(s):
    if s[i]!=' ':
        word=s[i]+word
    else:
        print(word,end=" ")
        word=''
    i+=1
print(word,end=" ")