s=input("enter string ")
tar=input("enter target word ")
#words=s.split()
count=0
i=0
'''while i<len(words):
    if words[i]==tar:
        count+=1
    i+=1
print("no.of occurence is ",count)'''
'''while i<len(words):
    if tar in words[i]:
        count+=1
    i+=1
print("occurence word is-> ",count)'''

while i<len(s)-len(tar):
    j=0
    match=1
    while j<len(tar):
        if s[i+j]!=tar[j]:
            match=0
            break
        j+=1
    if match ==1:
        count+=1
    i+=1
print("number of count is ",count)