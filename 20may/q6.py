s=input("enter a string ")
tar=input("given that string we want to search in string ")
word=s.split()
i=0
count=0
while i<len(word):
    if word[i]==tar:
        count+=1
    i+=1
print("total occurence of thar word is ",count)