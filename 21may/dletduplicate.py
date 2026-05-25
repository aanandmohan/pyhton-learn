'''s=input("enter string ")
words=s.split()
res=words[0]

i=1
while i<len(words):
    ch=words[i]
    
    j=i+1
    count=1
    while j<len(words)-1 and ch==words[j]:
        
        j+=1
    i=j
    res+=words[j]
    

        
print(res)'''
s = input("enter string: ")

words = s.split()

res = words[0]

i = 1

while i < len(words):

    if words[i] != words[i - 1]:
        res += " " + words[i]

    i += 1

print(res)