'''up=ord(' ')-32
print(chr(up))
print(ord(' ')-32)
'''

str=input("ente string ")
result=''
'''i=0 
while i<len(str):
    if i==0 or str[i-1]==" ":
        asci=ord(str[i])-32
        result=result+chr(asci)
    else:
        result+=str[i]
    i+=1
print(result)'''

words=str.split()
for w in words:
    result=result+w.title() +" "
print(result)