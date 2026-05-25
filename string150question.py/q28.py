s=input("enter stirng ")
tar=input("enter target ")
words=s.split()
count=0
for i in range(0,len(words)):
    if words[i]==tar:
        count+=1
print("the count is ",count)
