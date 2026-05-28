s=input('enter string ')
words=s.split()
i=len(words)-1
res=' '
while i>=0:
    res+=words[i]+" "
    i-=1
print(res)
