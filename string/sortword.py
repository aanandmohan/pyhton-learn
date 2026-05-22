s=input("enter string ")
words=s.split()
short=words[0]
i=1
while i<len(words):
    if len(words[i])<len(short):
        short=words[i]
    i+=1

print("shortest word h ->",short)