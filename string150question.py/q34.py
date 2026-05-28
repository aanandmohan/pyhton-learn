s=input('enter string ')
words=s.split()
min=words[0]
for i in range(1,len(words)):
    if len(words[i])<len(min):
        min=words[i]
print("the short word is ",min)
