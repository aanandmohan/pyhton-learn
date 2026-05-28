s=input("enter string ")
words=s.split()
long=0
longest=''
for i in words:
    if len(i)>long:
        long=len(i)
        longest=i
print("the longest word is ",longest)