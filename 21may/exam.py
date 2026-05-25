s=input("enter string ")
tar=input("enter target word ")
words=s.split()
count=0
i=0
while i<len(words):
    word=words[i]
    if tar in word:
        count+=1
    i+=1

print("the number is ",count)