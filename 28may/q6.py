'''n=int(input("enter size "))
l=[]
for i in range(n):
    x=int(input('enter numbner '))
    l.append(i)

max=0
min=999999999999
digit=""
mindigit=""
for i in range(n):
    if l[i]!=0:

        ch=l[i]
        count=1
        j=i+1
        while j<n:
            if l[j]==ch:
                count+=1
                l[i]=0
            j+=1
        print(ch,"->",count)
        if count>=max:
            max=count
            digit+=str(ch)+" "
        if count<=min:
            min=count
            mindigit+=str(ch)+" "
    
print("max frequency is ",digit," ->",max)
print("min frequnecy is ",mindigit,"->",min)'''
n = int(input("enter size "))

l = []

for i in range(n):
    x = int(input("enter number "))
    l.append(x)

maxfreq = 0
minfreq = 999999999

digit = ""
mindigit = ""

for i in range(n):

    if l[i] != 0:

        count = 1
        ch = l[i]

        j = i + 1

        while j < n:

            if l[j] == ch:
                count += 1
                l[j] = 0

            j += 1

        print(ch, "->", count)

        if count >= maxfreq:
            maxfreq = count
            digit += str(ch)+" "

        if count <= minfreq:
            minfreq = count
            mindigit +=str(ch)+" "

print("max frequency is", digit, "->", maxfreq)
print("min frequency is", mindigit, "->", minfreq)


    


    


