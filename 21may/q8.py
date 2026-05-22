s=input("enter a string ")
words=s.split()
flag=0
for i in range(len(words)):
    ch=words[i]
    st=""
    j=len(ch)-1
    while j>=0:
        st+=ch[j]
        j-=1
    if st==ch:
        print(ch," is palindrom")
        flag=1
if flag==0:
    print("no plaindrom found ")
