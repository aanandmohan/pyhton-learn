s="this is not"
'''word=" "
i=0
while i<len(s):
    if s[i]!=" ":
        word=s[i]+word
    else:
        print(word,end=" ")
        word=" "
    i+=1
print(word,end=" ")'''

words=s.split()
i=len(words)-1
while i>=0:
    word=words[i]
    rev=""
    j=len(word)-1
    while j>=0:
        rev=rev+word[j]
        j-=1
    print(rev,end=" ")
    i-=1