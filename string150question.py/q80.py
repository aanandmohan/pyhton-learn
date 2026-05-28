s=input("enter string ")

word=input("enter word ")
words=s.split()
for ch in words:
    j=0
    while j<len(word):
        s=word[j]
        if s in ch:
            j+=1
        else:
            break
    else:
        print(ch,end=" ")
